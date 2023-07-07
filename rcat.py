#!/usr/bin/env python
import sys
import os
import argparse
import subprocess
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    if args.filenames and args.filenames[0] != "-":
        for filename in args.filenames:
            with open(filename, "rb") as f:
                if has_tmux():
                    tmux_passthrough_pipe(f.read())
                    subprocess.run("read -n1", shell=True)
                else:
                    write(f.read())
    else:
        buf = sys.stdin.buffer.read()
        if has_tmux():
            tmux_passthrough_pipe(buf)
            time.sleep(1)
        else:
            write(buf)


def write(b: bytes):
    os.write(1, b)


def has_tmux():
    return "TMUX" in os.environ


def tmux_passthrough(b: bytes):
    return b"\x1bPtmux;" + b.replace(b"\x1b", b"\x1b\x1b") + b"\x1b\\"


def tmux_passthrough_pipe(buf: bytes):
    start = buf.find(b"\x1b")
    if start < 0:
        write(buf)
    else:
        write(buf[:start])
        write(tmux_passthrough(buf[start:]))


if __name__ == "__main__":
    main()
