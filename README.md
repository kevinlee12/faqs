# FAQ
[![CircleCI](https://circleci.com/gh/kevinlee12/faqs.svg?style=svg)](https://circleci.com/gh/kevinlee12/faqs)
[![codecov](https://codecov.io/gh/kevinlee12/faqs/branch/master/graph/badge.svg)](https://codecov.io/gh/kevinlee12/faqs)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c6a2d77a0d6f46bb903de8d5a409e325)](https://www.codacy.com/app/kevinlee963/faqs?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kevinlee12/faqs&amp;utm_campaign=Badge_Grade)

FAQ is a simple web app that returns answers to a user submitted query.

FAQ is built using Django and InfernoJS and powered by Apache Solr.

## Installation
FAQ is developed with Docker Compose with the idea that it will be easily hosted on a variety of cloud providers.

1. Verify that Docker Compose is installed, if not see the [official installation guide](https://docs.docker.com/compose/install/).
2. Clone this repo.
3. Run the following commands:
```
docker-compose build
docker-compose up
```

## Notes
This application is still in very much a work in progress. If you would like to make a PR, please do! Any assistance would be very much appreciated!

## Support
If you find bugs or would like to suggest features, please file a new [issue](https://github.com/kevinlee12/faqs/issues/new).

## License
The FAQ code is licensed under the [Apache v2 License](https://github.com/kevinlee12/faqs/blob/master/LICENSE).
