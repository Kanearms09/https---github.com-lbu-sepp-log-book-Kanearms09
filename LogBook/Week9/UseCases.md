### Topic Use Cases 

#### Virtualisation

1. **Server Consolidation**

Companies reduce physical hardware by running multiple virtual servers on one physical host, leading to savings on money, power and space.


2. **Test & Dev Environments**

Dev teams can quickly create isolated environments for testing different OS versions or application configurations without needing extra machines.


3. **Disaster recovery**

Snapshots and virtual machine backups make restoring systems after a failure fast and effortless.


4. **Running legacy software**

Businesses can run outdated apps in a virtualised Windows XP or Server 2003 machine without affecting their modern systems.


5. **Load Balancing and Failover**

Virtual machines can be moved between physical servers for load balancing or when a host fails, usually without downtime.


---

#### Cloud Computing

1. **Web and Mobile App Hosting**

Startups and enterprises host apps on the cloud (e.g. AWS, Azure, GCP) so they can scale instantly as traffic grows.


2. **Big Data Processing**

Cloud services like AWS EMR and Azure Data Lake process massive amounts of datasets without buying servers.


3. **Disaster Recovery as a Service(DRaaS)**

Cloud backup and similar services replicate data to off-site cloud regions, improving their resilience to unplanned disasters.


4. **Streaming Services**

Netflix, Spotify, and Youtube rely on the cloud to deliver content globally as cloud services allow you to scale with user demands.


5. **AI and Machine Learning**

Companies use cloud platforms for ML model training and deployment using on demand GPU/TPU instances.


---

#### Docker & Containers

1. **Microservices Architecture**

This is the process previously mentioned in the lecture, processes within large apps being separated into their own containers allowing easier updates and scalability.


2. **CI/CD Pipelines**

Containers are perfect for automated testing and deployments. GitHub Actions, GitLab CI, Jenkins etc often use Dockers to ensure consistent build environments.


3. **Local Developement**

Devs can replicate production environments on their laptops using Docker Compose


4. **API gateways and Edge Services**

Containers are lightweight and fast to start and deploy anywhere. This makes them ideal for running small, network-heavy services like API gateways.


5. **Hybrid Cloud Deployment**

Containers make it easier to deploy the same app across physical servers using Kubernetes. 