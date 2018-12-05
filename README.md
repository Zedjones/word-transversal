word-transversal [![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
==========
A program to recursively construct a tree of related words based off 
of an initial word and a list of topics (can also specify no topics). 
The depth of the recursion is also specified by the user. 
The tree will then be saved as a .png file in the root directory of 
the repository with the name 'root.png'. 

## Table of Contents
<!-- vim-markdown-toc GFM --> 
* [Requirements](#requirements)
* [Setup and Running](#setup-and-running)
* [Usage](#usage)
* [Licensing](#licensing)
* [Credits](#credits)
* [Future Features](#future-features)

## Requirements
You must have Python 3 and pip installed to begin the setup process.

## Setup and Running
To install the necessary dependencies, run `sudo python3 setup.py develop`. After installing the dependencies, you can run the program
with `python3 analyzer.py` or `python3 analyzer.py --help` to get
usage information.

## Usage
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

## Licensing
All files are licensed under GPL 2.0

## Credits
Related words are found using the [Datamuse API](https://www.datamuse.com/api/).

## Future Features
* GUI for ease of use by non-developers
* Packaging all dependencies and analyzer into executables for Linux, 
macOS, and Windows.
