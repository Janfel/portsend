# Portsend

> A Python script for quickly sharing files over a local network.

Portsend is a modern and cross-platform replacement for the old `cat file.txt | nc 127.0.0.1 1234` trick.
It is written in Python and works under Linux, Windows and Mac.

## Installation

```sh
pip install git://github.com/Janfel/portsend.git
```

## Usage example

On the sending machine:

```sh
portsend send myfile.txt mydir
```

This will result in an output like this:

```
Listening on port: 1199
Execute `portsend recv MyComputer` on the remote machine
```

On the receiving machine:

```sh
portsend recv -o my/target/directory MyComputer
```

If you are sending and receiving on the same machine, you have to use:

```sh
portsend recv localhost
```

You can find further information under:

```sh
portsend send --help
portsend recv --help
```

## Release History

- 0.1.0
  - The first proper release

## Meta

Jan Felix Langenbach – o.hase3@gmail.com

Distributed under the GPLv3. See `LICENSE` for more information.

[https://github.com/Janfel](https://github.com/Janfel/)

## Contributing

1. Fork it (<https://github.com/Janfel/portsend/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
