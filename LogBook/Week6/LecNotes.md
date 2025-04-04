#### What is computer programming?

- A mechanism for defining the behaviour of a programmable device
- Usually in the form of a list of instructions
- On a digital device each instruction is a number
- Each number is used to determine which instruction is executed
- A program represented as a list of numbers is often called machine code
- Execution is usually the responsibility of the CPU
- Each specific type of CPU has its own Instruction Set


**Providing the instructions to the Computer**

How do we provide the list of numbers to the CPU for execution? In the past (circa 1950) we provided them using some physical representation, e.g. punchcards.

In Modern systems programs are usually stored and executed via some sort of memory, e.g. RAM, ROM, EPROM, FLASH

So how do we get this list of numbers into memory:

- Usually we store them in Secondary storage (in the form of a file), then ask the Operating System to load and execute the program
- But how do we get the numbers into the files - the answer to this is very important.


**From a programmers point of view**

A programming language is simply a mechanism of allowing programs to be more easily writeable (and therefore understandable) by human beings.

That is, a program is a human friendly representation of the numbers which are executable by a computer, i.e. they are an abstraction mechanism.

Use of programming languages gives us several other advantages also:

- They massively speed up productivity
- They allow less skilled individuals to develop working programs
- They allow the same program to target different CPU instruction sets (portability)
- They can be processed by other programs, and be improved in many ways (optimisation)


#### The evolutions of Languages
**Second generation**


- 2nd generation languages abstracted away from direct machine code by representing instructions as mnemonics (a few letters to help programmers remember an instruction)
- This type of language was usually referred to as Assembly Language, with each mnemonic representing single instruction.
- These programs were converted into the list of instructions (i.e. numbers) using another program called an Assembler
- Assembly language made it much easier to write programs, however it was still technically difficult; took a long time; and was not portable across different CPUs


**Third generation**


- The development of third generation languages (3GLs) was a major step in leveraging the advantages of using a programming language.
- This generation of languages uses keywords written in English, each mapping to multiple underlying instructions.
- therefore these languages provided a much higher level of abstraction, and make programs much more understandable and quicker to develop
- These programs are converted into the list of instructions using another program called a compiler, which generates Assembly language.
- Due ti the higher level of abstraction, and the use of a Compiler, means these language produce code that is portable across different CPU instruction sets


#### Tool-Chains

For all of the languages mentioned, we write code in a very similar way. We typically use either a text editor, or an IDE. If we use a text editor, then we have to manually execute any other tools required to convert the program into machine code, e.g. compiler. The tools used to convert a program written in a programming language, into a program that can be executed is generally referred to as the tool-chain. An IDE integrates the editor and tool-chain together for us, usually behind a nice GUI.


#### How do we learn to Program?

- Understanding language syntax
- looking at existing code
- Making mistakes
- Understanding syntax errors
- Understanding run-time (logical) errors
- Being able to design algorithms
- Communicating with other programmers
- fixing bugs


**What is an algorithm?**

- An algorithm is the set of rules to be followed to solve a problem.
- Programming involves a lot of different concepts, however the core of programming in a 3GL is the process of implementing algorithms.
- Larger programs also involve the skill of handling complexity
- All solvable solutions can be implemented using:
  -Sequence
  -Selection
  -Iteration


#### Summary

A program is a list of numbers that represent instructions, different target hardware have different instructions. Programming languages are an abstraction mechanism to make our life easier. Most programs are written using third generation languages (3GLs) of which they are many. Other programs are used to convert our program into code which will execute on a specific piece of hardware , these tools are usually called a toolchain.  
