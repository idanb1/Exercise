# Exercise (RegexInFiles)
RegexInFiles helps to search regex in text files,
    using parameters from user(cli) or directly from another test
    module (TestClass)
## Install

<b>make build-image</b>

## Requirements

- bash
- make
- docker
- git

## Usage

There's a MakeFile with 6 pre-configured methods (build-image, tests-run, tests-run-verbose, app_runner, run-colorized-verbose, run-interactive)

###### Basic Use

There's a several options to use this app, all of them including the use of docker.io:

First step - create a docker image:
<br>
  <b># make build-image</b>
<br>

# running tests:
<br>
  <b># make tests-run</b>
  <br>
  tests-run will run all tests written in pytest folder from given container then docker will remove the container
 <br>

# tests-run-verbose:
<br>
  <b># make tests-run-verbose</b>
  <br>
  tests-run-verbose will run all tests written in pytest folder including verbose from given container then docker will remove the container
  <br>

# app_runner:
<br>
  <b># make app_runner</b>
  <br>

  app_runner will run basic functionality of RegexInFiles app on the created container with optional files / regex
  - running 'make app_runner' without any files or regex will run default values (FILE=Exercise/pytest/example1.txt, REGEX=grows)
  <br>
  Example to use external files\regex:
  <br>
  <b># make app_runner FILE=/your_dir_path/your_file.txt REGEX=your_regex</b>
  <br>

 # run-colorized-verbose:
 <br>
  <b># make run-colorized-verbose</b>
  <br>

  app_runner will run basic functionality of RegexInFiles app with colored matched lines on the created container with optional files / regex
  - running 'make app_runner' without any files or regex will run default values (FILE=Exercise/pytest/example1.txt, REGEX=grows)
  <br>
  Example to use external files\regex:
  <br>
  <b># make app_runner FILE=/your_dir_path/your_file.txt REGEX=your_regex</b>
<br>

# run-interactive:
<br>
  <b># make run-interactive</b>
  <br>

  run-interactive will generate container in interactive mode, in this mode you'll enter to ubuntu 14.04 container including the 'Exercise' repository (mounted).
  <br>
  Basic Example(from container bash, without using pytest):
  <br>
  <b># python3 Exercise/run_app.py -c -f ./Exercise/pytest/example1.txt -r grows</b>
  <br>
  -c & -m is mutually exclusive parameters
  <br>
  -f & -r is a required parameters & Unique (not support several appearanses)
  <br>

## General help:
<br>

usage:
<br>
        This application is designed to search for regex matches in text files
        <br>
       [-h] -f FILES -r REGEX [-c | -m]
       <br>
<br>

RegexInFiles
<br>

optional arguments:
<br>

  -h, --help            show this help message and exit
<br>
  -f FILES, --files FILES
  <br>
                        This is the files flag - **required flag
<br>
  -r REGEX, --regex REGEX
<br>
                        This is the regex flag - **required flag
<br>
  -c, --color           This is the color flag
  <br>
  -m, --machine         This is the machine readable output flag
 

<br>
<br>

Example of use: python run_app.py -c -f "./pytest/example1.txt" -r grows<br>

Example of output:<br>

example1.txt:2:2020-06-28 15:10:00.382291:Banana grows on trees<br>


<br>

example1.txt:3:2020-06-28 15:10:00.383258:Coconut grows on trees



* BTW - inside scatches dir there's a module that I create to parse parameters from CLI, later I understand argparse module is a better solution.
