# Copyright (C) 2019 Jan Felix Langenbach
#
# This file is part of portsend.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http: //www.gnu.org/licenses/>.
"""The main module of portsend."""

import argparse
from portsend.portsend import send, receive

DEFAULT_PORT = 1199


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A Python script for quickly sharing files over a local network."
    )
    subgroup = parser.add_subparsers(dest="operation")
    send_parser = subgroup.add_parser("send", description="Send a file over a local port.")
    recv_parser = subgroup.add_parser("recv", description="Receive a file from a remote port.")

    send_parser.add_argument("files", nargs="+", help="the files and directories you want to send")
    send_parser.add_argument(
        "-p", "--port", default=DEFAULT_PORT, type=int, help="override the default port"
    )
    recv_parser.add_argument("hostname", help="the hostname or IP of the sending machine")
    recv_parser.add_argument(
        "-p", "--port", default=DEFAULT_PORT, type=int, help="override the default port"
    )
    recv_parser.add_argument(
        "-o", "--outdir", default=".", help="the directory where the files are extracted"
    )
    return parser.parse_args()


def main():
    """The main entry point of portsend."""
    args = _parse_args()
    if args.operation == "send":
        send(args.files, args.port)
    elif args.operation == "recv":
        receive(args.hostname, args.port, args.outdir)


if __name__ == "__main__":
    main()
