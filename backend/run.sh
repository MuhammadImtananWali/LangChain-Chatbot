#!/bin/bash

set -e

pip install -r requirements.txt

uvicorn main:app --reload
