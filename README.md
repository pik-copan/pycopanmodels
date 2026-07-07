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

You can then run the models with `uv`. For example, for the seven dwarfs model, run: `uv run studies/seven_dwarfs.py`.

## Known issues

Some of the models showcased here have since fallen out of date and are no longer maintained to the current version of [pik-copan/pycopancore](https://github.com/pik-copan/pycopancore). Models which we know do not work:

- `models/exploit.py`
- `models/adaptive_voter_model.py`
- `models/carbon_voters_anderies_model.py`
- `models/example*.py`
- `models/coccon`

Other models will be fixed, once https://github.com/pik-copan/pycopancore/issues/213 and https://github.com/pik-copan/pycopancore/issues/211 are addressed.

For more information on current problems and to track the progress on fixing them, see https://github.com/pik-copan/pycopanmodels/issues/2.