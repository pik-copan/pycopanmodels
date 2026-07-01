# pycopan-more

This repository contains additional model components and example models using the [copan:CORE modelling framework](http://www.pik-potsdam.de/copan), developed at the Potsdam Institute for Climate Impact Research.

The base reference implementation can be found in [pik-copan/pycopancore](https://github.com/pik-copan/pycopancore).

## Running the models

To run the models, first, setup your environment. The recommended way is using [uv](https://docs.astral.sh/uv/) for that:

```console
$ uv sync
$ uv pip install .
```

However, you can also set up using pure Python:

```console
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install .
``` 