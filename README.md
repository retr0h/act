# act

act - A python task runner.

> 1a : the doing of a thing : deed
> 2 : the process of doing something : action

[Poe the Poet][] is probably a better all around library,
with fewer dependencies and setup.  However, I wanted to
experiment with dependency graphs, and a more general
purpose framework for building CLI tools.

I often find myself creating utility based python projects,
since it can be tested, easy to work with YAML, and the
community has a wealth of great projects (e.g. Rich/Click).

Act experiments with gluing shell and python code together
as a general purpose framework for building CLIs.

[Poe the Poet]: https://github.com/nat-n/poethepoet

## Usage

TODO

## Testing

Install dependencies:

    $ pip3 install poetry
    $ poetry install

To execute unit tests:

    $ poetry run poe test

List tasks:

    $ poetry run poe help
