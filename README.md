# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

## Pre-requisites 

You'll need to have a [Trello](https://trello.com/) account and an API key/token pair to setup this app. Details on how to obtain these can be found [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

You'll also want to have a Trello board setup for your todos with 3 lists with the following names:
* To Do
* Doing
* Done

You'll also want to have your board id to hand. See [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#boards) on how to locate your board id.

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).

Please note that the following mandatory environment variables must be set in order to allow the application to fulfil its functionality relating to calling the [Trello REST API](https://developers.trello.com/reference):
* [TRELLO_API_KEY](https://trello.com/app-key)
* [TRELLO_TOKEN](https://trello.com/app-key)
* [TRELLO_BOARD_ID](https://community.atlassian.com/t5/Trello-questions/How-to-get-Trello-Board-ID/qaq-p/1347525)

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Tests
In .env.test, replace the dummy values of both TRELLO_API_KEY and TRELLO_TOKEN.

Tests can be run as a whole by running `poetry run pytest`. To skip the slow end to end tests, you can run `poetry run pytest tests`.

To run the tests individually in vscode run `>Python: Discover Tests` from the command window (`Ctrl/Cmd + Shift + P`), select `pytest` as the test runner and then `.` as the test folder.
* To get the end to end tests running you'll need to [download the applicable chromedriver](https://chromedriver.chromium.org/downloads) for your version of Chrome + OS and add it the project root folder or your PATH.
* We'd recommend installing the [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) extension for VSCode as it doesn't have issues like all the tests vanishing when one file has a syntax error (plus it's easier to view individual test log output).