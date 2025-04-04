
#### Types of programming languages

Roughly we can suggest these types of programming languages:

- Procedural: COBOL, Pascal, C
- Object-oriented: C++, Java, Scala, Kotlin
- Multi-Paradigm: Python, PHP, Kotlin
- Functional: Haskell, Lisp

We could also think in terms of low-level (machine Code) or high-level (Python, Java).


#### Abstraction

A programming language allows us to control the underlying machine (specifically its CPU, Registers, and Memory). Post-1GLS, there is some level of abstraction that hides the details of how the machine works. 2GLs, for example, still involve working with Registers.

Some 3GLs, notably C, really require some knowledge of the workings of the machine. Others like Python and Java, effectively hide all the details. Some more than others.


#### Features of languages

Languages differ in their capabilities of what they provide, for example:

- Syntax: Readability and Symbolism
- Typing Strategy: Static, Dynamic, Supported Types
- Speed: Compile times, Run times
- Community: Ownership, Support, Development, Packages, Tools
- Use: Extent, Trends, Applications
- Extensions: Web, GUIs, etc


#### Object Orientation

OOP is based on the assumption that we view the world as made up of objects, that have properties and behaviours.

OO Languages allow us to model these objects, and to develop programs that manipulate the properties of these objects, via their behaviour.

Thus there should be considerable opportunity for code reuse, especially when we add in concepts such as inheritance and polymorphism.


#### Multi-paradigm

Some problems naturally fit an OO solution. Very roughly, these are large problems that have multiple interacting elements. Some problems do not, they tend to smaller, less liable to change, and better understood. It is a mistake to start on an OO solution in the second case, and to start on the procedural option first.


It is possible to use Python in an OO way, or in a strictly procedural way. This is a deliberate design feature, and one of Pythons key strengths. (It can even be used for functional programming). Other OO languages are only appropriate for an OO solution, and "don't make sense" used in a strictly procedural way. Hence why we looked at Python first and then Java.


#### Sample Problem

Suppose you have a file of data where each line represents the score achieved in a contest by some competitor. Statistics, such as a leaderboard, are required.

Procedural solution:

1. Read each line of the file
2. Split the line, and store the data in some suitable list-like structure.
3. Once all read, process the data structure to generate statistics
4. Use a standard algorithm to sort the resulting statistics as needed
5. Display the results

OO solution:

1. Build a competitor class, with suitable attributes and methods
2. Read each line of the file
3. Create a competitor from the data just read. Add to a list-like structure
4. Sort the list-like structure
5. Display the results

Suppose you have a file of data where each line represents the score achieved in a contest by some competitor. Statistics, such as a leaderboard, are required.

We see that the OO solutions requires more work "up front" to create the class, but the program itself is probably simpler.

Maybe there is also some potential for reusing (or, more likely, generalising) the class. OO only makes sense when we think in objects, in Java, everything is an object.


#### Making a class in OO

A class definition consists of:

- Attributes
- At least one constructor
- Methods that implements the class's behaviour
- (Probably) a method to return a string representation
- (Possibly) methods that implement comparison
- (Occasionally) a Destructor


#### The naming of files

A class is defined in a separate file to maximise its potential use. Java requires that the filename is the name of the class defined therein. Python does not, but by convention the name of the class is used, in lowercase.


#### Constructor

A class must have at least one constructor, a method to create an instance of that class. Java supports multiple constructors. Python achieves the same using optional or default arguments. We assume here that the input is comma-separated.


#### Magic Methods

A class may have methods with a special name that perform "magic". A common example is a method that provides a string representation of an object. This method will be used "magically" by functions that print an object. In Java, this is toString, in Python, _ _str_ _


#### Attributes

Internally, an object is represented by the values of its attributes (sometimes called instance variables).

In java these are defined with their type, as private.

In Python, they are instantiated in the constructor, and the type is implied.


#### Public & Private

In some languages, the class is split into a private section, and a public interface.

Attributes are private, and are accessed via methods called" getters" and "setters".

This is possible in Python, but it is more usual to access values directly.


#### Methods

Python classes can obviously have "setters", especially if it adds to code readability. Other methods always take a parameter called self that represents the object itself. Per "Clean Code", method names are chosen to aid readability (Python code should make sense when read aloud).


#### Sorting

A common problem is to need to sort a collection of objects. To do this, the class needs to define the rules for comparing two objects of the class. It is enough to just define "Less than", but good form to also add equality.


#### Using a class

To use a python class, it just needs to be imported.

Note: There are rules for where Python will "look" for the class. Here it is just in the same folder.

Use the name of the class to create an object. Class names have an initial capital.

E.g.

	from competitor import Competitor

	c_1 = Competitor()
	c_2 = Competitor('Jane, 12')


Attributes can be manipulated directly. Incidentally, because the class has a definition for less than, it gets greater than for free. Since a class will be imported, the main is often used for test code.

E.g.

	from competitor import Competitor

	c_1 = Competitor()
	c_2 = Competitor('Jane, 12')

	c_1.name = 'Terry'
	c_1.score = 20

	if c_1 > c_2:
		print (f'{c.name} wins!');

Armed with the class, the program to process the file of scores is really very easy. After checking the CLA (boilerplate code), read the contents into a list of objects.

E.g.

	def read_scores(score_file):

		scores = []
		with open(score_file, 'r') as sf:
			for entry in sf:
				scores.append(Competitor(entry))
		
		return scores 

Printing results is also easy, Here we use a new function that prints a neat line.

	def print_leaderboard(sorted_scores):

		for entry in sorted_scores:
			print(entry.leaderboard_line())



	scores = read_scores(sys.argv[1])
	scores.sort(reverse = True)
	print_leaderboard(scores)

Our possible error is here. What happens if the line in the file is invalid?

Well we would get an IndexError, which would be thrown and generate a confusing error message. This a handy place to throw a custom exception.

E.g.

	def read_scores(scores_file):

		scores = []
		with open(scores_file, 'r') as sf:
			for entry in sf:
				scores.append(Competitor(entry))
		
		return scores 

Declaring a new exception type is easy. Add this to the class definition (it makes sense to keep them together). this is an example of inheritance, but that is not important right now.

E.g.

	Class CompetitorFileFormatError(Exception):
		pass

Now tweak the code to throw this new exception. remember that good Clean Code does not print errors, it throws exceptions.