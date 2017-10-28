// Copyright 2017 FAQ Authors
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

import Inferno from 'inferno';
import Component from 'inferno-component';
import InfernoCreateClass from 'inferno-create-class';
import 'inferno-devtools';
import 'materialize-css';
import Remarkable from 'remarkable';

const SOLR_ROWS_RETURN_COUNT = 10;
const THREAD_ID_PATTERN = 'last-thread-<thread_no>';
const SEARCH_URL = '/search';

var AnswerThread = InfernoCreateClass({
  getDefaultProps: function() {
    return {
      answer: '',
      title: ''
    };
  },
  rawMarkup: function() {
    var md = new Remarkable();
    var rawMarkup = md.render(this.props.answer.toString());
    return {
      __html: rawMarkup
    };
  },
  render: function() {
    var md = new Remarkable();
    return (
      <div id={this.props.id}>
        <div className='section'>
          <h5>{this.props.title}</h5>
          <span dangerouslySetInnerHTML={this.rawMarkup()} />
        </div>
        <div className='divider'></div>
      </div>
    );
  }
});

var AnswerContainer = InfernoCreateClass({
  getDefaultProps: function() {
    return {
      results: []
    };
  },
  renderResults: function() {
    return this.props.results.map(function(item, index) {
      var id = THREAD_ID_PATTERN.replace('<thread_no>', index);
      return (
        <AnswerThread id={id} title={item.title} answer={item.response} />
      );
    });
  },
  render: function() {
    return (
      <div>
        {this.renderResults()}
      </div>
    );
  }
});

var FAQContainer = InfernoCreateClass({
  getInitialState: function() {
    return {
      query: '',
      results: []
    };
  },
  componentDidMount: function() {
    this.fetchAnswers();
  },
  handleChange: function(event) {
    this.setState({
      query: event.target.value
    });
    this.fetchAnswers();
  },
  fetchMoreAnswers: function() {
    var payload = {
      query: this.state.query,
      start: this.state.results.length
    };

    $.get(SEARCH_URL, payload, function(data) {
      var newResults = this.state.results.concat(data.docs);
      this.setState({
        results: newResults
      });
    }.bind(this))
      .done(function(data) {
        var threadLength = data.docs.length + this.state.results.length;
        if (threadLength < data.numFound) {
          var selector = '#' + THREAD_ID_PATTERN.replace(
            '<thread_no>', threadLength - 1);

          // Materialize scrollfire settings, see
          // http://materializecss.com/scrollfire.html
          var options = [{
            selector: selector,
            offset: 0,
            callback: this.fetchMoreAnswers
          }];
          Materialize.scrollFire(options);
        }
      }.bind(this))
        .fail(function(data) {
          var backendFailThread = [{
            'title': 'Oh no, mothership is not calling!',
            'response': 'Something has gone wrong with the connection or server'
          }];
          this.setState({
            results: backendFailThread
          });
        }.bind(this));
  },
  // Fetches answers from the backend for a new query.
  fetchAnswers: function(startThread) {
    var payload = {
      query: this.state.query,
    };

    // Grab answer threads from the backend.
    $.get(SEARCH_URL, payload, function(data) {
      this.setState({
        results: data.docs,
      });
    }.bind(this))
      .done(function(data) {
        if (data.docs.length < data.numFound) {
          var selector = '#' + THREAD_ID_PATTERN.replace(
            '<thread_no>', data.docs.length - 1);

          // Materialize scrollfire settings, see
          // http://materializecss.com/scrollfire.html
          var options = [{
            selector: selector,
            offset: 0,
            callback: this.fetchMoreAnswers
          }];
          Materialize.scrollFire(options);
        }
      }.bind(this))
      .fail(function() {
        var backendFailThread = [{
          'title': 'Oh no, mothership is not calling!',
          'response': 'Something has gone wrong with the connection or server'
        }];
        this.setState({
          results: backendFailThread
        });
      }.bind(this));
  },
  render: function() {
    return (
      <div className='row'>
        <div className='input-field col s12'>
          <i className='material-icons prefix'>search</i>
          <input id='icon_prefix' type='text' value={this.state.query}
            onInput={this.handleChange}></input>
          <label for='icon_prefix'>Hi, what can I help you with?</label>
        </div>
        <div className='col s12'>
          <AnswerContainer results={this.state.results} />
        </div>
      </div>
    );
  }
});

Inferno.render(
  <FAQContainer />,
  document.getElementById('content')
);
