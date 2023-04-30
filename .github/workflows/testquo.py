name: Test Quo module

on: [pull_request]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest, macos-latest]
        python-version: ["3.7", "3.8", "3.9", "3.10", "3.11.0"]
    defaults:
      run:
        shell: bash
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
          architecture: x64
      - name: Install and configure Poetry
        # TODO: workaround for https://github.com/snok/install-poetry/issues/94
        uses: snok/install-poetry@v1.3.3
        with:
          version: 1.3.1
          virtualenvs-in-project: true
      - name: Install dependencies
        run: poetry install
        if: steps.cached-poetry-dependencies.outputs.cache-hit != 'true'
      - name: Format check with black
        run: |
          source $VENV
          make format-check
      - name: Typecheck with mypy
        run: |
          source $VENV
          make typecheck
      - name: Test with pytest (with coverage)
        run: |
          source $VENV
          pytest tests -v --cov=./quo --cov-report=xml:./coverage.xml --cov-report term-missing
      - name: Upload code coverage
        uses: codecov/codecov-action@v3
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          file: ./coverage.xml
          name: quo
          flags: unittests
          env_vars: OS,PYTHON
