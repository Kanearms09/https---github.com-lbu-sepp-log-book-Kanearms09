### Lecture 3 - Introducing processes

#### Socio-Technical Systems

We can identify 3 aspects of any system that uses a piece of software:

- **Hardware**- The physical technology being used

- **Software**- The programmed layer that creates applications

- **Wetware** - The user of the system


**Hardware**

Hardware is usually straightforward. There is probably a single optimal solution, these days cloud computing is giving a lot of flexibility in hardware provision, with rapid scaling and so on. Cloud also moves hardware from a one-off capital cost to a recurring subscription-type cost.


**Software**

There are also two (arguably three these days) types of software in a system.

Traditionally:

1. System Software - The OS, networking and so on.
2. Application Software - The app that runs on the above.

However we should probably add:

3. Framework software - The framework on which the app runs


**Wetware**

The is arguably the most important aspect, we always should remember that any system has users. We need to understand what they want to be able to do. There will be different categories of users, with different needs, different technical know-how, and different exposure to the system.

---


#### History

Like anything that is engineered, systems are big. So we need some sort of structure in order o help build them. We need plans, processes, and a way to know we are finished.

Systems Development started in the 60s/70s, and they needed a plan. The types of systems and tools used back then however are very different to the ones we have now and so are the plans.

---


#### Methodology - waterfall

A long time ago it was agreed that software development efforts needed some sort of structure E.g. methodology.

For a long time, the waterfall methodology model dominated. It worked well with the technologies of the time, there are still use cases now where it works well.

waterfall relies on on rigorous analysis of requirements, which are "signed off" before development starts. There is also further sign-off between each phase. The penultimate phase involves demonstrating that the implemented software matches these requirements.


**Issues**

In no particular order:

- waterfall takes a long time
- Specifically, there is a long wait to see any benefit
- A lot of time is spent on writing documents, which do not deliver benefit
- Likewise, there is a lot of planning, which does not deliver benefit.
- It is based on what a system does, not user needs
---


#### Waste

Waste is an important thing to consider when a dev spends there time, Examples of waste could be;

- Commenting code
- Updating project plans
- Updating a requirement spec
- Writing any sort of documentation (E.g. user manuals)

**Specific Example - Gantt Charts**

There are many Gantt charts in this world, many projects require the production and maintenance of Gantt charts.

However they are extremely useless and unnecessary.

---

#### post-waterfall

After Waterfall, various other approaches have emerged since. The lessons that we learnt from waterfall were implemented into these, here are some examples:

- Iteration
- Rapid delivery, even continuous
- Close interactions between developers and end-users
- A recognition of the partnership between Devs and end-users.

However, it should be noted that approaches that focus on fast-delivery can lead to corners being cut. To an extent, this is fine, as long as there is some idea to one day go back and fix this when there is more time available. The cost of the hours going back to fix this is known as technical debt.

There is another downside to these new methodologies. Usually, approaches that focus on fast delivery can lead to projects that never end. This is clearly documented in Jenkin's Law of Software Products:

*"Every good software product will one day reach its optimum in terms of performance, features, and usability. After this point, developers will inevitably add features that the users do not want or need until the software product is no longer fit for purpose."*

-----


#### Agile Manifesto


	Individuals and interactions over processes and tools.
	Working software over comprehensive documentation.  
	Customer collaboration over contract negotiation.  
	Responding to change over following a plan.

Some things that we can extract from this manifesto are:

- Tools & processes are important, but competence and ability are more important.

- Following a process does not itself produce valuable software that solves a problem or delivers value.

- Working on a problem will change one's understanding of it, so any process must take changes into account.

- Modelling can be useful, but it does not itself deliver business value.

- A contract is useful, but it is more important to work with a customer to meet their needs.

- A plan is important, but it must adapt.


#### Agile - in a nutshell

Agile focuses on delivering valuable software:

- Anything that does not contribute to this is waste
- Success in this is the primary measure of success

It is important however to remember that Agile, is not a methodology. It is instead the opposite, without sounding too abstract it is almost a philosophy to keep in mind whilst approaching your work. 