# Copyright 2017 FAQ Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script creates a new search core (single) with SEARCH_CORE_NAME
# (see below). This name should match SOLR_CORE in fyi/settings.py. Then,
# loads the sample data unless --no_data_load is present. Note that this
# script must be run within the Solr Docker container.

SEARCH_CORE='search1'

if [ -z "$BASH_VERSION" ]
then
  echo ""
  echo "  Please run me using bash: "
  echo ""
  echo "     bash $0"
  echo ""
  return 1
fi

set -e

echo "Starting core creation"
bin/solr create -c $SEARCH_CORE

if [ $? != 0 ]
then
  echo "There was an error creating the search core"
  return $?
fi

LOAD_DATA=true
for arg in "$@"; do
  if [ "$arg" == "--no_data_load" ]; then
    LOAD_DATA=false
  fi
done

if [ $LOAD_DATA = true ]; then
  echo "Loading sample data"
  bin/post -c $SEARCH_CORE solr/data/sample_data.csv
  if [ $? == 0 ]; then
    echo "All done!"
    exit 0
  else
    echo "There was an error when loading sample data"
    exit $?
  fi
else
  echo "Did not load sample data"
  exit 0
fi
