#### Python Versions
**The problem**

Due to Pythons fluid and continuous development, the new versions often have new features, and previous features removed. It is not uncommon for a system developed in Python to require a particular version as a minimum or, to not work correctly after a certain version. Due to this, a Dev will frequently have to have a number of Python versions available.

Pythons release cycle is typically one new major version per year, usually support for previous versions will last around 5 years.


#### PyPi - The cheese shop

Something brilliant about Python is that it is rich in available packages from PyPi. If a complex system is written in Python, it will likely rely on a particular package, or even a particular version of a particular package. This continues further as these packages will rely on other specific packages and so on. This results in the system having a network of interrelated dependencies.


#### Dependencies

This problem is usually referred to as dependency management, there are different solutions to this for different languages, however Pythons is Virtual Environments. This allows for projects built on multiple versions of Python to be available on the same system.

Python's standard package manager is pip. It can install the latest version of a package, or a specific version. If this package has its own dependencies (most likely will), pip can find and download these also.


#### Using a manager

using pip we can also list all currently installed packages, and list these in a documentation in the conventional file. The "requirements" file need to be kept up to date, and sits in the project root directory. Most IDEs will detect it, and use it to build a virtual environment, or it can be done by hand. This is demonstrated below:

	$ pip install tabulate
	$ pip install django==5.0.1
	$ pip freeze
	$ pip freeze > requirements.txt


#### Virtual Environments

A virtual environment (usually "vee-env) is a copy of a specific Python instalment, along with the dependencies needed for the it.

It should be stored in the project root directory, typically this would be in a folder called venv or .venv (this is a hidden file in Unix systems). It includes a copy of pip, which will install within that venv!

**Creating a venv**

First, we must create a venv. The command uses whatever version of Python which is currently being used. On every use, it must be activated so that the correct copy of Python is in use. This will usually change the prompt as shown

	$ python3 -m venv venv
	$ source venv/bin/active 
	(venv) $

If all is well, the version of Python in use will be that in the venv.

	$ python3 -m venv venv
	$ source venv/bin/active 
	(venv) $
	(venv) $ which python3
	/home/tony/project/venv/python3


**Using a venv**

The venv contains binary files, so does not belong to Git. The requirements file however does belong to Git, because it can be used to rebuild the venv.

	$ python3 -m venv venv
	$ source venv/bin/active 
	(venv) $
	(venv) $ which python3
	/home/tony/project/venv/python3
	$ git add requirements.txt
	$ git commit -m "Add project dependencies"


#### Programming Tools

A venv will allow us to experiment with two important tools that support development:

- Linters, used for static code analysis
- Formatters, used to check and reformat code according to given rules.

Some or all of these are now available within an IDE but, obviously, the IDE might not always be available.


**Formatters**

Note that there are several options here, we are just picking one of the most popular. The formatter in this example is Black, it processes a Python source file and reformats it according to the PEP-8 spec

	(venv) $ pip install black 
	(venv) $ black my_prog.py


**Linters**

We pick ruff as our linter (not because it sits on top of others). A linter analyses code, spots and reports errors and code smells. It may also be able to suggest ways to improve code speed or efficiency.

	(venv) $ pip install ruff 
	(venv) $ ruff check 