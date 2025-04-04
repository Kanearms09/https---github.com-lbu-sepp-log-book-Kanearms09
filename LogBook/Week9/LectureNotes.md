### Lecture 9 - Virtualisation and Cloud 

#### Context - Infrastructure and Devs

We live in a time of technological prosperity, the luxury of a personal computer is not one that has always existed. Now we have an ideal world where developers aren't restrained by multi-user computers, and each developer can have their own personalised setup tailored to their every need.

In an organisation that has a IT setup, the traditional way to arrange this would be to overview and tend to its own hardware, most likely having a dedicated facility where this is all stored, this is known as the prod environment/server. This is also where you would find "Ops", the draw back from this is that hardware is cost extensive. Not just for material, but for security, power, maintenance etc.

These Data Centres consist of racks of servers, which are essentially a headless PC but far more powerful. They are also multi-user. If a business wishes to have the luxury of using a server but do not want to take on the costly overheads, they have the option of renting servers in commercial data centres.


**Dev & Prod revisited**

As we know, a Dev has the luxury of choosing whatever platform they choose, however once this code has went to prod it must be able to execute correctly. As we know the cost effect of running data centres, we know that it would be unreasonable to give each Dev a physical Prod Server. The solution to this is virtualisation, or more specifically a virtual server.


#### Virtualisation

Virtualisation is an overarching term that essentially consists of a set of technological tools that allow the splitting and delegating of computing resources into virtual machines or other virtual resources.

With virtualisation technology we can bypass the need to give every Dev their own physical server and instead give them their own virtual environment in which it is so powerful it feels as if it is their own. It should be noted that right now we are strictly speaking of hardware virtualisation, however their are other types.

A very easy and obvious example of virtualisation in practice is the OneDrive, this gives the user the impression that their is a USB plugged into their computer, even though it is strictly virtual.

When an entire system is being virtually emulated, there is always a host machine and a guest machine. On the host machine, we run a hypervisor which is essentially a guest manager that manages on guest VMs. The hypervisor can give access, privileges and resources to the guest machines also. Quite often as well a guest will be running on a completely different OS which will not affect the users ability. An example of a Dev requiring the use of a guest machine would be if a Mac based Dev needed to test his code on Linux servers or vice versa.


#### Tech

**VirtualBox**

VirtualBox is a well known, well established open source hypervisor. In order to run a guest OS you just need a disk image (ISO), and the VirtualBox download.


**WSL**

A Windows Sub-system for Linux (WSL) is essentially a VM that runs ubuntu on a Windows OS. A Dev can run Linux apps on this that appear to be running on windows.


**Vagrant**

Hypervisors such as VirtualBox solve the issues of running on different VMs with different operating systems, however we still have to deal with dependency management of our code (e.g. packages, versions etc). We require a system that describes exactly what is installed on the VM.

Our solution is Vagrant which is text-based and kept in Git. Vagrant takes a text file (as a VagrantFile), and creates you a VM based upon the contents and dependencies required. It is VirtualBox based however it is ran from the command-line. Here is an example of what it may look like:

	Vagrant.config("2") do |config|
		config.vm,box = "ubuntu/jammy64"
		config.vm.synced_folder "../src/python", "src"

		config.vm.provision "shell", inline: <<-SHELL
			apt-get update
			apt-get install -y apache2
		SHELL

	$ vagrant up
	$ vagrant ssh


#### Aside: Working with VMs

It should be noted that if we break a VM, we can simply just make another one. This allows us to have a lot less worry than we would working on our own OS, as we can freely change or install something and just see what happens. This is, however, assuming that we have a copy of all our files on the host so that we don't risk losing anything. As a VagrantFile deals with a specified single VM, we must wonder what we can do when attempting to manage an array of servers. This is a complex issue as it involves more system permissions, setting up users and so on. However there is available technologies to do so.


The tech's we have previously mentioned "virtualise" a complete machine, this is a bit over the top, and in being over the top it is considered wasteful of resources.

An example of this is imagine that you're attempting to write in PHP in MariaDB, all you need is the MariaDB server and web server with PHP enabled. Using a "virtualised" complete machine would provide you with lots of extra OS features such as sound, networking etc. Therefore we need minimal VMs that run single processes also.


#### Containerisation

This type of minimalist virtualisation is called containerisation, this is related to something we may have heard of before - containers. A simple way to explain containers would be an independent isolated environment running a single application. So we can have different types of containers for different types of processes, e.g. a MariaDB container. A collection of containers can then be used to provide the required specific environment.


**Docker**

Docker is a well known set of virtualisation tools for managing software in containers, these containers are isolated but can communicate. Complex systems can be specified using a Dockerfile. So far we have only referred to virtualisation in terms of development, however it is possible to containerise an application and then deploy it using docker. This approach has been very popular recently, as it solves issues for the developer and server config.


#### Cloud

This takes us onto our last topic, Cloud. People who provide cloud services are using virtualisation to provide IT services to their customers. Traditionally this would be server farms, however in more recent years they are also delivering packaged independent services (similar to containers).

This has provided a revolution of widespread availability of Virtual Private Servers, as one physical server can host many VPSs. This gives businesses an affordable option over owning a physical onsite server.

From a conceptual perspective, you could view cloud servers as a remote computing resource that are consistlently available and can be used as and when needed. If we were to be more specific as to the functionality of this process, we could say that the cloud is a bunch of servers in data centers that are accessed via the internet.


#### PAYG

Cloud usually operates under a PAYG model, the customer pays the vendor for the resources they end up using, such as:

- CPU cycles
- Disk space or access
- Network traffic

AWS claims that on this pay model using cloud services over time is around 95% cheaper than purchasing the hardware.

Cloud vendors benefit from massive economies of scale.

- they deal in hardware servers in massive quantities, and score huge discounts.
- They consume resources at large scale, again attracting discounts.
- They can invest in expensive facilities.
- Sys admin tasks have little marginal cost.

And they pass this on to the customer and as vendor grows, their economies grow too. Remember that with virtualisation, one physical server can serve multiple customers.

However we should not just think of Cloud as just offering computing power, it can also be:

- Infrastructure as a service
- Platform as a service
- Software as a service

Some other features illustrate how Cloud will be "the future":

- Scalability
- Resiliency
- Geographical Reach
- Green Computing
- Implicit Cost Reduction in non-Cloud hardware

On the other hand, legislation is yet to catch up with the rise of Cloud.