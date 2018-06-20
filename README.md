# Asperathos - Broker (Development)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Overview
The **Broker** is the framework entry point for the user. It is responsible for receiving a submission from the user and preparing its execution.

**Asperathos** was developed by the [**LSD-UFCG**](https://www.lsd.ufcg.edu.br/#/) *(Distributed Systems Laboratory at Federal University of Campina Grande)* as one of the existing tools in **EUBra-BIGSEA** ecosystem.

**EUBra-BIGSEA** is committed to making a significant contribution to the **cooperation between Europe and Brazil** in the *area of advanced cloud services for Big Data applications*. See more about in [EUBra-BIGSEA website](http://www.eubra-bigsea.eu/).

To more info about **Broker** and how does it works in **BIGSEA Asperathos environment**, see [details.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/master/docs/details.md) and [asperathos-workflow.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/master/docs/asperathos-workflow.md).

## How does it works?
The broker is implemented following a **plugin architecture**, providing flexibility to customize your deployment using only the plugins you need, avoiding to include unnecessary dependencies (from others plugins) to your deploy environment.
All the integrations with different infrastructures and components are made by specific plugins.

## How to develop a plugin?
See [plugin-development.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/master/docs/plugin-development.md).

## Requirements
* Python 2.7
* Linux packages: python-dev and python-pip
* Python packages: setuptools, tox and flake8

To **apt** distros, you can use [pre-install.sh](https://github.com/bigsea-ufcg/bigsea-manager/tree/master/setup.sh) to install the requirements.

## Install
Clone the [Broker repository](https://github.com/bigsea-ufcg/bigsea-manager.git) in your machine.

### Configuration
A configuration file is required to run the Broker. **Edit and fill your broker.cfg in the root of Broker directory.** Make sure you have fill up all fields before run.
You can find a template in [config-example.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/master/docs/config-example.md). 

### Run
In the Broker root directory, start the service using run script:
```
$ ./run.sh
```

Or using tox command:
```
$ tox -e venv -- broker
```

## Broker REST API
Endpoints are avaliable on [restapi-endpoints.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/master/docs/restapi-endpoints.md) documentation.
