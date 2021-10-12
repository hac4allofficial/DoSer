# DoSer.py - Simple DoSer in Python

## What is DoSer?
DoSer is basically an HTTP Denial of Service attack that affects threaded servers. It works like this:

1. We start making lots of HTTP requests.
2. We send headers periodically (every ~15 seconds) to keep the connections open.
3. We never close the connection unless the server does so. If the server closes a connection, we create a new one keep doing the same thing.

This exhausts the servers thread pool and the server can't reply to other people.

## Citation

If you found this work useful, please cite it as

```bibtex
@article{gkbrkDoSer,
  title = "DoSer",
  author = "D4RK~D3VIL",
  journal = "github.com",
  year = "2021",
  url = "https://github.com/hac4allofficial/DoSer"
}
```

## How to install and run?

You can clone the git repo or install using **pip**. Here's how you run it.

* `sudo pip3 install DoSer`
* `DoSer.py example.com`

### SOCKS5 proxy support

However, if you plan on using the `-x` option in order to use a SOCKS5 proxy for connecting instead of a direct connection over your IP address, you will need to install the `PySocks` library (or any other implementation of the `socks` library) as well. [`PySocks`](https://github.com/Anorov/PySocks) is a fork from [`SocksiPy`](http://socksipy.sourceforge.net/) by GitHub user @Anorov and can easily be installed by adding `PySocks` to the `pip` command above or running it again like so:

* `sudo pip3 install PySocks`

You can then use the `-x` option to activate SOCKS5 support and the `--proxy-host` and `--proxy-port` option to specify the SOCKS5 proxy host and its port, if they are different from the standard `127.0.0.1:8080`.

## Configuration options
It is possible to modify the behaviour of DoSer with command-line
arguments. In order to get an up-to-date help document, just run
`DoSer -h`.

* -p, --port
* * Port of webserver, usually 80
* -s, --sockets
* * Number of sockets to use in the test
* -v, --verbose
* * Increases logging (output on terminal)
* -ua, --randuseragents
* * Randomizes user-agents with each request
* -x, --useproxy
* * Use a SOCKS5 proxy for connecting
* --https
* * Use HTTPS for the requests
* --sleeptime
* * Time to sleep between each header sent

## License
The code is licensed under the MIT License.
                                               
