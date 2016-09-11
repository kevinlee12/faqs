# FAQ
FAQ is a simple web app that returns answers to a user submitted query.

FAQ is built using Django and ReactJS and powered with Postgres.

## Installation
FAQ is developed with Docker Compose with the idea that it will be easily hosted on a variety of cloud providers.

1. Verify that Docker Compose is installed, if not see the [official installation guide](https://docs.docker.com/compose/install/).
2. Clone this repo.
3. Run the following commands:
```
docker-compose build
docker-compose up
```
4. Close the docker containers by `Ctrl+C`.
5. Run `docker-compose run web python manage.py migrate`

## Notes
This application is still in very much a work in progress. If you would like to make a PR, please do! Any assistance would be very much appreciated!

## Support
If you find bugs or would like to suggest features, please file a new [issue](https://github.com/kevinlee12/faqs/issues/new).

## License
The FAQ code is licensed under the [Apache v2 License](https://github.com/kevinlee12/faqs/blob/master/LICENSE).
