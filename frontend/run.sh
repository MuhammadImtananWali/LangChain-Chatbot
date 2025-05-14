#!/bin/bash

set -e

pip install -r requirements.txt

streamlit run app.py
