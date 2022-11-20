# Project

For `macOS` program can be callable from the `command line` (from `...\code` dictionary) as `cat test.json | python3 main.py`. To run a program on any other OS, you should probrably change `python3` to `py` or `python`, based on the version of python you have installed on your system.

For `windows` you can't use `cat` therefore `adquate command` is `py main.py < test.json` (with correct `python starting command` as mentioned above). 

**Tests**

Tests are also runable from `...\code` with the command `python3 -m unittest test.py -v` (again you might want to change `python3`, to be able to run tests).
