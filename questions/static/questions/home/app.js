// Copyright 2016 FAQ Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

var AnswerThread = React.createClass({
  getDefaultProps: function() {
    return {
      title: '',
      answer: ''
    };
  },
  rawMarkup: function() {
    var md = new Remarkable();
    var rawMarkup = md.render(this.props.answer.toString());
    return { __html: rawMarkup };
  },
  render: function() {
    var md = new Remarkable();
    return (
      <div>
        <div className="section">
          <h5>{this.props.title}</h5>
          <span dangerouslySetInnerHTML={this.rawMarkup()} />
        </div>
        <div className="divider"></div>
      </div>
    );
  }
});

var AnswerContainer = React.createClass({
  getDefaultProps: function() {
    results: []
  },
  renderResults: function() {
    return this.props.results.map(function(item) {
      return (
        <AnswerThread title={item.title} answer={item.response} />
      );
    });
  },
  render: function() {
    return (
      <div> {this.renderResults()}</div>
    );
  }
});

var FAQContainer = React.createClass({
  getInitialState: function() {
    return {
      query: '',
      results: []
    };
  },
  componentDidMount: function() {
    this.getAnswers();
  },
  handleChange: function(event) {
    this.setState({
      query: event.target.value
    });
    this.getAnswers();
  },
  getAnswers: function() {
    var urlSearch = '/search/' + this.state.query;
    $.ajax({
      url: urlSearch,
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({results: data.answers});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(urlSearch, status, err.toString());
      }.bind(this)
    });
  },
  render: function() {
    return (
      <div className="row">
        <div className="input-field col s12">
          <i className="material-icons prefix">search</i>
          <input id="icon_prefix" type="text" value={this.state.query} onChange={this.handleChange}></input>
          <label htmlFor="icon_prefix">Hi, what can I help you with?</label>
        </div>
        <div className="col s12">
          <AnswerContainer results={this.state.results} />
        </div>
      </div>
    );
  }
});

ReactDOM.render(
  <FAQContainer />,
  document.getElementById('content')
);
