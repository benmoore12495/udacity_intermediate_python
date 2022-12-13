import csv
import requests
import json

def read_neos(filename):
    with open(filename,'r') as file:
        neos = {}
        reader = csv.reader(file)
        i = 0
        for line in reader:
            neos[i] = line
            i += 1
        return neos

def read_cads(filename):
    f = open(filename)
    data = json.load(f)
    return data
