# Hackathon csv
During the first week of [osoc](https://osoc.be/), there is a small hackathon. This repo was one of the results of this hackathon.
The goal of this repo was to find a way to convert an xml file to a table, so it could be analyzed with the same service as the csv-analyzer. The hardest part of this is finding the piece of data the user is most probably wants to analyze (since you've got multiple levels of data in xml files).

The output is an `output.csv` file, ready to be analyzed with the `hackathon-csv` code.
## Running
This repository was mainly for testing, so it won't be really useful te run it yourself. The most important pieces of this code are used in the ```shmdoc-analyzer-service```
### Install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
### Running
The input file is specified at line `10`. Since this was only for the hackathon, there was only a hardcoded version of the input file. 
Since we didn't have enough time during the hackathon to automate it, the xml level we want to analyze is also hardcoded (`resource.creators.creator`).

The code can be run using the following code. 
```bash
python3 shmdoc_xml.py
```