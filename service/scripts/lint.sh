#!/bin/bash
set -xe

pip install pylint;
pylint --reports=y --output-format=parseable --exit-zero /app/dm_api;
