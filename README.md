# Introduction to FastAPI

_This repository contains code that will be used during the **Introduction to FastAPI** Workshop at [Hack the Valley 5](https://hackthevalley.io/) on Saturday, October 16, 2021 at 12:00 AM._

## About the Workshop

**[FastAPI](https://fastapi.tiangolo.com/)** is a Python 3.6+ web framework for building APIs with type hints. Since its launch more than two years ago, companies like Microsoft, Netflix, and Uber have used this framework to quickly build web APIs due to its high-performance and fast to code features. In this introductory workshop, you will be introduced to FastAPI's basic capabilities and features, such as automatic API documentation, validation, security/authentication and more while reading and updating resources persisted in a relational database. The workshop will be run by Alvin Tang, a Software Developer who volunteered at Vaccine Hunters Canada this past summer and utilized FastAPI firsthand to provide vaccine availability data to millions of Canadians.

## Prerequisites

Please install the following prerequisites before attending the workshop, if you want to follow along.

**Required**:

- [Python 3.6+ w/ Pip](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

**Recommended**:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html#pragmatic-installation-of-pipenv)

## Installation

1. Clone the repository via Git

   ```bash
   git clone https://github.com/alvintangz/fastapi-workshop.git
   ```

2. Change directory to root

   ```bash
   cd ./fastapi-workshop
   ```

3. Install all python dependencies with [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/).

   ```bash
   pipenv install
   ```

## Running the Server

1. Spawn a shell within a virtual environment.

   ```bash
   pipenv shell
   ```

   All python dependencies should be installed within the virtual environment from the previous installation steps.

2. Run the server on port `8000` from the root of the project within the shell.

   ```bash
   python -m app.main
   ```

   - Swagger: [http://localhost:8000/swagger](http://localhost:8000/swagger)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
   - OpenAPI Spec (JSON): [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

## Helpful Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI GitHub Repository](https://github.com/tiangolo/fastapi)
- [Pydantic Official Documentation](https://pydantic-docs.helpmanual.io/)

## License

All contents in this repository are under the [MIT License](./LICENSE).
