#### Revolution

The UK has undergone a number of industrial revolutions, we are currently in our 4th. In previous revolutions the innovation was centred around physical commodities I.E. Bridges, Boats, Railway etc. The new revolution is now the capability to create new, cheap and widely available products through the medium of technology. 

This has completely opened up the entrepreneurial landscape, as it is now far easier to set up your own business with a marketable product. 


#### Envelopes - An example

Take this example, suppose we are tasked with filling 250 envelopes with election leaflets. There are multiple ways to do this, for example:

- Fold all the leaflets first, then put them all into envelopes, after this we could seal all of them and then stamp them finally.
- Or, we could take it one envelope at a time and complete the whole process before moving onto the next envelope. 

The latter is far superior than the previous, within manufacturing it is common knowledge that dealing with excess WIP leads to wastage. The first example takes the assumption that all is well with all of the products involved in assembly, therefore it would take a lot longer to find issues in merchandise using this method. This exists within software development also, except WIP is tested code that is not in production. 

In manufacturing, WIP implies wasted effort because:

- Resources have been used up before they were required.
- Resources may be left idle while WIP is used up.
- Physically moving WIP around uses up resources.

If we take WIP as 'tested code' not in Prod, we can see that the same is probably true of program code. 


#### Dev and Ops 

Most software development methodologies tell us a little how code is deployed. Traditionally raw code would be written by a "Dev" who would then send this over to "Ops" who are are responsible for deployment, patches etc. If errors were found, the Dev would be then notified and the whole cycle would begin again. 

This previous cycle was slow and monotonous, however most importantly it put in place a "Them and us" culture. In the mid 1990s the idea of DevOps had emerged. This is not simply merging the two roles into one, instead it simply promotes the automation and cohesion of the roles where appropriate. 

This approach is extremely inline with "Agile" and, as we'll come to see, Lean. The term DevOps consists of mainly 3 agreed upon aspects: 

- Shared Ownership of a system across all tech roles
- Rapid Feedback following a deployment 
- Automation of some aspects of the work flow

A key idea is to minimise the time from code being completed to that code running in Prod. 

There are also 4 key metrics to evaluate the function of a DevOps team: 

- **Change Lead Time**: the time taken to code test and deploy a feature.
- **Deployment Frequency**: How often new code is deployed. 
- **Change Failure Rate**: How often (or whether) any change causes issues.
- **Mean-Time to Recovery**: Time to restore Prod after some failure. 

The fifth is **Reliability** of the system, as measure in uptime, effectiveness, users satisfaction and the like. 


#### Deployment Frequency 

One brilliant way to avoid this WIP is to increase the frequency of deployment, this way code isn't sat sedentary awaiting use. Previously deployment was counted in months or years, now we work in minutes and at worst hours. An effective DevOps team will be able to deploy multiple times a day if needed, however this in of itself obviously has its own implications due to the need for some form of automation.

This implies that the codebase within the main branch must always represent a shippable product which could be deployed, this is achieved with git branching. In an ideal world, when the new code is merged with the main branch, it will still retain as a shippable product and there will be no conflict within the code. 


#### Continuous Delivery 

Continuous delivery is a fundamental aspect of the DevOps role. This is essentially the ides of committed code being passed through a deployment pipeline as it goes from final commit (This is done by the Dev) to deployment (Prod, or UAT). The pipeline will probably include operations such as building, testing, maybe validation and configuration before deployment. It is very important for as much of this pipeline to be as automated as possible. 


#### Continuous integration 

This is very similar, however slightly different, to the idea of continuous development, hence the phrase "CI/CD". The term CI refers to the frequent merging of a singular Devs code with others, this usually takes place in an integration branch. From this integration branch, valid code can then be merged into the main branch through the process of CD. The cohesive nature of CI/CD fosters collaboration with the team and promotes an "on the same page" ethos. 


#### Lean 
**Manufacturing**

The parallels between manufacturing and software are numerous, more specifically Japanese manufacturing. This idea of elimination of waste and pipeline processes are core ideas to the Japanese manufacturing system. Lean takes these principles even further. 


**Startups**

The writer Eric Ries builds upon these ideas that we've touched upon and applies it to tech startups, specifically in the novel "The Lean Startup". This is summarised below:

- Minimise inventory during production
- Use Kanban to limit the amount of WIP 
- Find issues early and address them 
- Maintain close connection with suppliers and customers. 


**A leap of faith**

A new product is often a leap of faith, this is due to the nature of building new products. They are always essentially built off of an assumption that we believe to be true, and from this we build the project. 

The leap of faith is based upon two ideas, which must be verified:

- **The value hypothesis** - Tests whether the product really delivers value when in the hands of customers

- **The growth hypothesis** - Is how new customers will be acquired, and how many. 

This is obviously only scratching the surface when considering an entire business E.g. digital transformation etc. However here we are only concerned with software. 

The traditional approach to this would be to carry out market research, take surveys, interview focus groups etc. 

However the lean/agile approach is more similar to "build it, and see what happens", very field of dreams esc. 


#### Testing the leap 

Building an entire system application is a very risky move with a lack of market research, here comes in the idea of an MVP. This is a Minimum Viable Product, which is essentially the smallest possible system we can put out from which we can learn and build up form. Although a key principle of the MVP is that it does not have to be a smaller version of the final system, however it can be. 

The main thing an MVP provides is validated learning, this gives us hindsight on what can be improved, aids the planning of further development or even tells us what didn't work. It provides us with metrics of the product, however these metrics must be valuable and not for boosting ones own ego. 

If a Dev was to readjust their ideas of how to make the checkout page or any aspect of a product, traditionally this would require meetings, budget talk and other formalities. Lean says to just build it, and arrange matters so that half the users see the new implementation. This is known as a split test, and provides us with validated learning and useful metrics. 

One aspect of it not representing the final project is the programming language itself, it is entirely possible that the MVP will be a cruft collection of Python scripts. However the final product will be beautifully engineered in Java.