# SSHTarpit

SSHTarpit is an implementation of a tarpit server designed to keep a connection
open to a client without actually doing anything.

I was inspired by the [Endlessh: an SSH Tarpit](https://nullprogram.com/blog/2019/03/22/)
blog post about an implementation in Python 3 using async and I ported this
example as a server using python [Twisted](https://twistedmatrix.com)
event-based framework.

The whole thing is packaged so it can be installed using pip as follows:

````console
# pip install https://github.com/westfeld/ssh_tarpit/archive/master.zip
````

This will install SSHTarpit and its dependencies.

It has been tested with Python 3.7.3.
