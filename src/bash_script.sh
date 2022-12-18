#!/bin/bash
python3 -m venv venv
source venv/bin/activate
python -m pip install tabulate
python main.py