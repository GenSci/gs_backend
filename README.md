# GenSci

#### The web project of a gentleman scientist.
---
**Disclamer:** The term "gentleman scientist" is not used here in a gender deterministic way.  Rather it is used to evoke a romantic period in scientific discovery during which many advances were made by scientists working independently of any larger institution or financial backing.  Charles Darwin, Alexander Von Humboldt, and even Marie Curie were at one time "gentlemen scientists".  It is in these footsteps the current GenSci project seeks to walk.

## Purpose
GenSci seeks to combine my interests in scientific programming and data visualization from my research work in physical oceanography with my career in building websites and web-based applications.  My goal is to not only build a site that displays some of the research I have done but facilitates others in identifying questions about the science presented and offering tools to assist in those inquiries.

## Approach
Based on the successes I have had in the past, I will be making extensive use of Docker containers to allow me to manage the various components of a complex web application as services.  It is my goal to host this site myself on, at first, a single Raspberry Pi.  I hope to scale out to running a Docker swarm on a cluster of Raspberry Pis.  Additionally I will likely have a branch of this repo that is tailored for deployment on Google Cloud Platform using the Kubernetes engine.  

## Components
All components listed here will have their own Docker containers
* DB:  [PostgreSQL](https://www.postgresql.org/)
* Web application:  [Wagtail CMS web framework](https://www.djangoproject.com/) + [Gunicorn](http://gunicorn.org/)
* Web Server: [NGINX](https://www.nginx.com/)


**Disclamer 2:** My knowledge of any of the above components are relatively thin.  I enjoy developing in the Wagtail framework and have cobbled together a set of tools that allow me to do some nifty things with it.  I realize there is likely much more I could do to optimize any specific component and I would welcome any *helpful* suggestions.

I am using this stack to deploy a REST API server that will serve up the content for Gentlemen Scientists.  The front end will be handled by a Vue based project and can be found in the gs_frontend repo.

