# City Service - Serverless AWS Lambda

This repository hosts a serverless backend service built with AWS Lambda. It offers two key features:

1. Retrieving information about a specific city
2. Calculating the distance between two cities

## API Endpoints

There are two main endpoints:

**1. Retrieve City Information:**
```
GET /city?name=<city_name>
```
Returns data about a city specified in the query string.

**2. Calculate Distance Between Cities:**
```
POST /distance
```
Accepts a JSON body with the names of two cities, and returns the distance between them.
Example request body:
```json
{
    "city1": "<city_name_1>",
    "city2": "<city_name_2>"
}
```
## Function Names

For local invocation via AWS SDK, the function names are:

* `getCity`: city-service-dev-getCity
* `getDistance`: city-service-dev-getDistance

## Getting Started

### Prerequisites

* [Node.js](https://nodejs.org/) and [npm](https://www.npmjs.com/)
* [Serverless Framework](https://www.serverless.com/)
* [AWS CLI](https://aws.amazon.com/cli/) configured with your AWS credentials
* [Yarn](https://yarnpkg.com/)
* [Poetry](https://python-poetry.org/)

### Installation

1. Install the Serverless Framework globally:
    ```bash
    npm install -g serverless
    ```

2. Install the project dependencies:
    ```bash
    yarn install
    ```

3. Install the Python dependencies via Poetry:
    ```bash
    poetry install
    ```

Don't forget to set the right env as interpreter in your IDE.
## Local Development

To run the service locally, ensure the [serverless-offline](https://www.serverless.com/plugins/serverless-offline) plugin is installed. Then, use the command:

```bash
yarn sls offline
```
This will start the service on port 3000.

## Deployment

To deploy the service to AWS, run:

```bash
yarn sls deploy
```

## Testing

To execute the (small) test suite, run:

```bash
pytest
```

## Architecture

This project follows a simple architecture inspired by Domain-Driven Design (DDD) principles. The serverless framework is utilized for deployment and orchestration, while AWS Lambda serves as the compute provider. The Serverless Python Requirements plugin is used to handle Python dependencies.

