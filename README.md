# War

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## About <a name = "about"></a>
Python adaptation of the classic card game "War". Players draw one card each; the player with the higher card wins (Ace being highest). If the cards are equal in value, then war is declared. In war, each player contributes another card -- face-down -- and then both draw another set of cards to determine who wins the pot. The first player to hold all 52 cards is the victor.

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python 3

### Installing

It is recommended to run this application from within a virtual environment. Python makes this pretty simple with:

`python3 venv <environment_name_here>`

Activate this virtual environment then run the following to install the project's dependencies:

`pip3 install -r requirements.txt`

### Tests

To run the tests included in the package, invoke:

`python3 -m unittest discover` 

## Usage <a name = "usage"></a>

To run this application, invoke:

`python3 ./run.py [-i, --interactive]`

This will launch the application. The `-i` flag is an optional parameter to use if the user would like to interactively draw cards. Otherwise, the application will seamlessly auto-draw cards until a winner is declared.
