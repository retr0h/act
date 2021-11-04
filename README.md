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

List the graph:

    $ act graph ls

List a specific task's graph:

    $ act graph ls <node>

## Testing

Install dependencies:

    $ pip3 install poetry
    $ poetry install

To execute unit tests:

    $ poetry run poe test

List tasks:

    $ poetry run poe help
