**CMSI 1010** Computer Programming & Laboratory, Fall 2021

# Python Game Demos
This repository contains a collection of code and resources to play with for creating games with Python. The originals for these files are taken from various public locations across the web, and are collated here in one place for your convenience.

## Overview
The files in this repository represent different ways for implementing games in Python. They vary based on the Python library that they use:

| Base library | Examples |
|----|----|
| Tkinter | [tkinter_demo.py](./tkinter_demo.py), [all_user_input_widgets.py](./all_user_input_widgets.py) |
| _graphics.py_ | [tetris_sol.py](./tetris_sol.py) |
| Pillow | [whack_a_mole.py](./whack_a_mole.py) |
| PyGame | `chimp`, [test_pygame.py](./test_pygame.py) |

Tkinter serves as a foundation for any Python program that has graphics—you have already been using this via the _graphics.py_ module that has come with many of your psets! The included Tkinter-only demos aren’t really games; they show you how to open a window and how to code up basic widgets like buttons, lists, text fields, etc.

The trusty _graphics.py_ module has come with many of your psets so far. As you might recall, this module adds a number of basic computer graphics operations. If you put these together in the right way, you can implement games! However, _graphics.py_ does not include support for music or other sound 😔

Another area where Tkinter can use a boost is support for image files. The [Pillow](https://python-pillow.org) library helps here, making it easier to implement game graphics based on image files that you can create separately.

Finally, the most broad-based basic game support can be found by installing the [PyGame](https://www.pygame.org) Python library. Learning this library can give you a path toward creating Python games with the least possible boilerplate code, with support for images, music, and sound built-in.

These four are all independent alternatives to creating game-like programs in Python. If you prefer to stay with something you have used before and don’t mind not having music or sound, staying with _graphics.py_ will suffice. If you want to learn just enough additional code to handle images, you can use Pillow. However if you want all of the above _plus_ music/sound, and are willing to learn some new library code, PyGame would be the way to go.

## Set Yourself Up for Experimentation
If you want to modify and push your modifications to GitHub, you will need to _fork_ this repository. This will create your own personal copy which you can then clone as usual. Click on _Fork_ button near the top-right of https://github.com/lmu-cmsi1010-fall2021/python-game-demos in order to create a forked copy for yourself.

## Tkinter Demos
If you have been able to run the _graphics.py_ exercises from the problem sets, then you will be able to run the Tkinter demos without further setup:

    python3 tkinter_demo.py
    python3 all_user_input_widgets.py

As mentioned in the [Overview](#overview), these are not actually games but they show the basic graphics and user interface features that Tkinter provides.

## _graphics.py_ Demo: _tetris_sol.py_
Silent games are possible with just _graphics.py_. For convenience, this file is included with this repository just as it has been with past problem sets. To demonstrate this, we have a simple version of the Tetris game:

    python3 tetris_sol.py

Full documentation on _graphics.py_ can be found here: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

As long as _graphics.py_ is in the same folder as _tetris_sol.py_, the game should work. Use the ⬅️/➡️ keys to move a falling piece; the ⬆️ key rotates it; the <kbd>space bar</kbd> drops it.

Note, this is for demo purposes only: you may encounter bugs! (which may be just as educational as the working code itself 😁)

## Pillow Demo: _whack_a_mole.py_
This is an implementation of Whack-a-Mole, using images to represent hidden and uncovered moles via the Pillow library. This makes it easy to swap out the graphics without having to change the code!

### Required Library for Whack-a-Mole Demo: Pillow
Pillow is not included with most standard installations of Python. As such, it needs to be installed separately. There are many ways to install a Python library so if you know of others and prefer those, feel free to use them. If you are new to installing third-party libraries, _pip_ with the `user` option is a safe way to do so: the `user` option ensures that the library is saved as part of _your_ user account’s files, avoiding administrator passwords and possible interference with operating system files.

#### Windows

    py –m pip install –U Pillow -user

#### macOS

    python3 –m pip install –U Pillow --user

If the exact command doesn’t appear to work, try to replace `py` or `python3` with the Python command you’ve been using.

### Hammer Time!
With the Pillow library installed, the game should be fairly self-explanatory once you run it:

    python3 whack_a_mole.py

More information on this implementation (with different image files) can be found here: https://runestone.academy/runestone/books/published/thinkcspy/GUIandEventDrivenProgramming/11_gui_program_example.html

## PyGame Demos: `chimp` and _test_pygame.py_
For full game support including audio/music, [PyGame](https://www.pygame.org) is a viable option. Some self-teaching is involved since it’s optional for the class, but the time investment may be well worth it if games are your jam.

### Required Library: PyGame
PyGame is not included with most standard installations of Python. As such, it needs to be installed separately. There are many ways to install a Python library so if you know of others and prefer those, feel free to use them. If you are new to installing third-party libraries, _pip_ with the `user` option is a safe way to do so: the `user` option ensures that the library is saved as part of _your_ user account’s files, avoiding administrator passwords and possible interference with operating system files.

#### Windows

    py -m pip install -U pygame -user

#### macOS

    python3 -m pip install -U pygame --user

If the exact command doesn’t appear to work, try to replace `py` or `python3` with the Python command you’ve been using.

### Quick Start: `chimp`
If you want to try something out right away, the PyGame library comes with a built-in example called `chimp`. In fact, you don’t need _any_ extra code to run it; it’s already in PyGame! Do this:

    python3 -m pygame.examples.chimp

(substitute `python3` with your Python command if it’s different)

An article on how `chimp` works can be found here: https://www.pygame.org/docs/tut/ChimpLineByLine.html

The code for `chimp` can be seen here: https://www.pygame.org/docs/tut/chimp.py.html

### Code Included: _test_pygame.py_
The included PyGame test code implements a racecar-like game (so it’s just “A bit Racey”) with music and sound effects! How many barriers can you dodge before crashing?

    python3 test_pygame.py

A tutorial, with videos, that walks you through this program can be found here: https://pythonprogramming.net/pygame-python-3-part-1-intro

(this is a multipage tutorial so don’t hesitate to click to the next one at the bottom if you want to keep learning more)

Note how these libraries all make use of classes and objects, which is why we couldn’t really introduce these libraries until we got to this point. Make sure to review classes, objects, methods, and inheritance if you’re having trouble with any of these libraries.
