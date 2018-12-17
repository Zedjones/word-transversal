word-transversal [![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
==========
A program to recursively construct a tree of related words based off 
of an initial word and a list of topics (can also specify no topics). 
The depth of the recursion is also specified by the user. 


If using the command line, the tree will then be saved as a .png 
file in the root directory of the repository with the name 'root.png'.

If using the web application, the tree will be then be saved in
'static/images' as a png with the name being a concatenation of 
the current time with the initial word.

A demo of the web application can be found here: word-transversal.info.

## Table of Contents
<!-- vim-markdown-toc GFM --> 
* [Requirements](#requirements)
* [Setup and Running: Command Line](#setup-and-running:-command-line)
* [Usage: Command Line](#usage:-command-line)
* [Setup and Running: Web App](#setup-and-running:-web-app)
* [Usage: Web App](#usage:-web-app)
* [Licensing](#licensing)
* [Future Features](#future-features)

## Requirements
You must have Python 3 and pip installed to begin the setup process.

## Setup and Running: Command Line
To install the necessary dependencies, run `sudo python3 setup.py develop`. After installing the dependencies, you can run the program
with `python3 analyzer.py` or `python3 analyzer.py --help` to get
usage information.

## Usage: Command Line
    usage: analyzer.py [-h] [--initial INITIAL] [--topics TOPICS] --iterations
                   ITERATIONS [--breadth BREADTH]

    optional arguments:
    -h, --help            show this help message and exit
    --initial INITIAL, -s INITIAL
                            Initial word to start with
    --topics TOPICS, -t TOPICS
                            Comma separated topic list to make sure the words are
                            roughly related to. Type 'None' for no topics
    --iterations ITERATIONS, -i ITERATIONS
                            Number of iterations/depth to go down
    --breadth BREADTH, -b BREADTH
                            Number of related words on each depth level


## Setup and Running: Web App
To install the necessary dependencies, run `sudo python3 setup.py develop`. After installing the dependencies, you can run the program
locally using `FLASK_APP=web_app.py flask run -h '127.0.0.1'` on your local machine. 

## Usage: Web App 
Open a browser and navigate to http://127.0.0.1:5000. 

## Licensing
All files are licensed under GPL 2.0

## Future Features
* Looking into further uses for this, including cognitive flexibility training 
* Expanding the application to include a mode for the "meaning like" feature of the API