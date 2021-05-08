# Petversocial

## Overview

We at Petversocial are the premier provider of cross species Customer Service
across the top tier of Domestic Animal Messaging platforms.

Out systems effortlessly allow our clients to facilitate walkies, snuggles, or
treats for good doggos, cattos or even sneks\*.

We do this by integrating with different species messaging and social platforms
and providing a unified paw friendly web interface for animal contact care
representatives and automation bots to work seamlessly together.

\* walkies for sneks not currently supported.

## Requirements

A host with docker-compose.

We don't need access to this host and Docker Desktop as well as docker-compose
should be fine.

This task will be assessed by you making a pull request against this private repo.

We are assessing why you make choice to solve the problems so communicating your
decisions and any assumptions you have made are as important as the changes
themselves.

We are looking to assess how you work in a distributed team and communicate as
well as technical skills.

### The Task

Add a new service to our existing stack - there are some limitations and bugs
on the existing setup that you will need to fix to do this.

Feel free to modify or upgrade any part of the setup you need to make it better
or to allow it to be extended - we are mainly interested in your ability to work
with containers so don't expect you to modify the example applications -
though you may want to look at them for hints.

1. Set up the existing development environment on your machine using the
docker-compose stack.

```
docker-compose up
```

There are some errors in some of the docker/app configuration you need to
correct to make the application work.

The status of the petversocial pawserver and it's dependant services can be
found at the /checkz endpoint of the pawserver.

When everything is working this is the output you should see.

```
curl http://localhost:8080/checkz
{
    "doggoface": "GOOD DOGGO!",
    "kittehnet": "miaow",
    "sneksville": "ssssoooo_nicessss_to_seeee_youuus"
}
```

Any other outputs will still return a 200, but different messages from the
individual pet platforms.

For example:

```
curl http://localhost:8080/checkz
{
    "doggoface": "GOOD DOGGO!",
    "kittehnet": "http error",
    "sneksville": "ssssoooo_nicessss_to_seeee_youuus"
}
```

You can find the source of the kittehnet platform and it's default configuration
file in the kittehnet directory and you may change it or it's
configuration as you need to.


2. Dockerize and add a new feline sentiment detector service.

This is a python service and you will find this in the feline-sentiment dir.

It predicts feline sentiment with 95% accuracy on the /sentiment endpoint.

This service will be consumed by the pawserver in a subsequent project but for
the moment we just want to check it's health as we do with existing services.

To run the app under python3 you need to do

```
pip install -r requirements.txt
FLASK_APP=main.py flask run
```

It will need it's configuration file fsd.cfg in the same directory as main.py is
run from.

It's health check endpoint is /health

Hints:
- The flask Quickstart guide is here: flask https://flask.palletsprojects.com/en/1.1.x/quickstart/
- You may push to a public docker repo if you want (a throwaway docker hub
account for example), or you can use docker-compose's ability to build the image
locally and run it.
- See the pawserver.cfg file for example config for depandant services.
- Attempt to dockerize the application as if it's a production application, take
hints from the other services if you like.
