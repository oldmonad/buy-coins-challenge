# buy-coins-challenge
Buy-coins challenge

[![Build Status](https://travis-ci.com/dbytecoderc/buy-coins-challenge.svg?branch=develop)](https://travis-ci.com/dbytecoderc/buy-coins-challenge)

This application converts bitcoin rates to naira based on exchange rate and margin

## Technologies

### Below is a list of technologies used to build this project

`Django`

`GraphQL (Graphene)`

### Installation

Follow these steps to set up the app.

#### Clone the repo:

`$ git clone https://github.com/dbytecoderc/buy-coins-challenge.git`

#### Navigate to the project directory:

`$ cd buy-coins-challenge`

#### Create a virtual environment by running

`pipenv --three`

#### Activate the environment

`pipenv shell`

### Running and Development 

#### Install dependencies

`pipenv install`

#### If installation fails, do

`pipenv uninstall`

`pipenv install --sequential`

#### Start the application

`python manage.py runserver`

#### Try out the endpoint with your GraphiQL testing tool

visit: `http://127.0.0.1:8000/graphql/` in your browser and run the query below

`query {
 calculatePrice(choiceType: SELL, margin: 2, exchangeRate: 360) {
  calculatedPrice
  }
}`

#### Author: Oparah Dimkpa