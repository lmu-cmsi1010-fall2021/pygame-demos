**CMSI 1010** Computer Programming & Laboratory, Fall 2021

# PyGame Demos
This repository contains a collection of code and resources to play with while exploring PyGame. The originals for these files are taken from various public locations across the web, and are collated here in one place for your convenience.

## Required Library: PyGame
PyGame is a Python library that is not included with most standard installations of Python. As such, it needs to be installed separately. There are many ways to install a Python library so if you know of others and prefer those, feel free to use them. If you are new to installing third-party libraries, _pip_ with the `user` option is a safe way to do so: the `user` option ensures that the library is saved as part of _your_ user account’s files, avoiding administrator passwords and possible interference with operating system files.

### Windows

    py –m pip install –U pygame -user

### macOS

    python3 –m pip install –U pygame --user

If the exact command doesn’t appear to work, try to replace `py` or `python3` with the command-line Python you’ve been using.

## Required Library for Whack-a-Mole Demo: Pillow
If you would like to play with the Whack-a-Mole demo, you will need an additional library called Pillow. Installing it via _pip_ with the `user` option is similar to PyGame; just change the library name.

### Windows

    py –m pip install –U Pillow -user

### macOS

    python3 –m pip install –U Pillow --user

