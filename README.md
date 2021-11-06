[![Lint](https://github.com/retr0h/act/actions/workflows/lint.yml/badge.svg)](https://github.com/retr0h/act/actions/workflows/lint.yml)
[![Unit Test](https://github.com/retr0h/act/actions/workflows/unit.yml/badge.svg)](https://github.com/retr0h/act/actions/workflows/unit.yml)
[![codecov](https://codecov.io/gh/retr0h/act/branch/main/graph/badge.svg?token=BLPDRRJCUK)](https://codecov.io/gh/retr0h/act)

# act

act - A simple task runner.

> 1a : the doing of a thing : deed
> 2 : the process of doing something : action

[Poe the Poet][] is probably a better all around library,
with fewer dependencies and setup.  However, I wanted to
experiment with directed graphs, and a more general
purpose framework for building CLI tools.

[Poe the Poet]: https://github.com/nat-n/poethepoet

## Usage

### exec

Execute a particular phase:

    $ act exec <phase>

### ls

List all phases:

    $ act graph ls

List a specific phase:

    $ act graph ls <phase>

## Testing

Install dependencies:

    $ pip3 install poetry
    $ poetry install

To execute unit tests:

    $ poetry run poe test

List tasks:

    $ poetry run poe help
