# Tasks
# Task 1: Extract the data (`extract.py`)
# Task 2: Generate a custom database (`database.py`)
# Task 3: Inspect the data. (`neos.csv` and `cad.json`)
# Task 4: Build models to represent the data. (`models.py`)
# Task 5: Quering close approaches with user specified inputs (`filters.py`)

import csv
import requests
import json
import time
from step_1_data_discovery import *
from extract import *
from models import *
from database import *
from filters import *

def main():
    start_time = time.time()
    # ===========================
    # Step 1: Extract the data
    # ===========================
    print('Loading neos data...')
    neos = read_neos(filename='neos.csv')
    time_spent = round((time.time() - start_time),1)
    print('Loaded neos data in {seconds} seconds'.format(seconds=time_spent))
    _time_ = time.time()
    print()

    print('Loading approaches data...')
    cads = read_cads(filename='cad.json')
    time_spent = round((time.time() - _time_),1)
    print('Loaded approaches data in {seconds} seconds'.format(seconds=time_spent))
    _time_ = time.time()
    print()


    # ===========================
    # Step 2: Creating database
    # ===========================
    print('Creating neo db...')
    neo_db = create_neo_db(neos,cads)
    time_spent = round((time.time() - _time_),1)
    print('Created neo db in {seconds} seconds'.format(seconds=time_spent))
    _time_ = time.time()
    print()

    # ===========================
    # Step 3: data discovery
    # ===========================
    print('Starting data discovery...')
    data_discovery(neos,cads)
    time_spent = round((time.time() - _time_),1)
    print('Data discovery in {seconds} seconds'.format(seconds=time_spent))
    _time_ = time.time()
    print()

    # ===========================
    # Step 5: Quering close approaches with user specified inputs
    # ===========================
    print('Testing user filters...')
    dates_filtered_approaches = pull_on_dates('1900-01-01','1950-01-01',neo_db)
    print('Date filter...')
    for approach in dates_filtered_approaches:
        print(approach)
    print()


    dist_filtered_approaches = pull_on_distance(0,0.20,neo_db)
    print('Distance filter...')
    for approach in dist_filtered_approaches:
        print(approach)
    print()


    vel_filtered_approaches = pull_on_velocity(7,20,neo_db)
    print('Velocity filter...')
    for approach in vel_filtered_approaches:
        print(approach)
    print()


if __name__ == '__main__':
    main()
