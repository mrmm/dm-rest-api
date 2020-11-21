#!/bin/bash
set -xe

pip install pylint;
pylint /app/dm_api;
