# paper-thin-rest
[![Build Status](https://travis-ci.org/viktorasm/paper-thin-rest.svg?branch=master)](https://travis-ci.org/viktorasm/paper-thin-rest)

A base code for implementing REST services in Python, [Flask](http://flask.pocoo.org/), where only JSON services are implemented.

It's meant to be just a very simple bridge between your API and JSON over HTTP protocol. No other fancy stuff like automatic model CRUD or super cool hyperlinking stuff, see [Django REST framework](http://www.django-rest-framework.org/) or [Eve](http://python-eve.org/) for that type of thing.

I would very much prefer that whoever uses the code just embeds it into his own app rather than reuse as a framework. 
It's not meant to be reusable and configured, it's meant to be a "copy/paste and keep just the bits you need" type of thing.
