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

The server can be started using Twisted's twist tool.

````console
# twist SSHTarpit
````

## Monitoring SSHTarpit

To monitor how many clients are caught in the tarpit for how long, a HTTP
server is also implemented which emits statistics in JSON format which is
suitable to be parsed e.g. by Telegraf.

The JSON fields include 

* the duration of the connection in seconds
* the remote IP address
* the address family e.g. IPv4 or IPv6

````JSON
[{"duration": 60.977558, "ip_address": "127.0.0.1", "address_type": "IPv4"}]
````

If no client is currently connected to SSHTarpit, an emtpy HTTP response
with the HTTP status code 204 NO CONTENT is returned.

It has been tested with Python >=3.5.
