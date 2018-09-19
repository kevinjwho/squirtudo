#!/usr/bin/python3

import sys
import os
import subprocess
import argparse

#Launcher for Squirtudov2

def parse_cli_args():
    parser = argparse.ArgumentParser(description="Squirtudo Launcher - Pokemon Go Bot for Discord")
    parser.add_argument("--start","-s",help="Starts Squirtudo",action="store_true")
    parser.add_argument("--auto-restart","-r",help="Auto-Restarts Squirtudo in case of a crash.",action="store_true")
    parser.add_argument("--debug","-d",help="Prevents output being sent to Discord DM, as restarting could occur often.",action="store_true")
    return parser.parse_args()

def run_Squirtudo(autorestart):
    interpreter = sys.executable
    if interpreter is None:
        raise RuntimeError("Python could not be found")

    cmd = [interpreter, "squirtudo", "launcher"]

    while True:
        if args.debug:
            cmd.append("debug")
        try:
            code = subprocess.call(cmd)
        except KeyboardInterrupt:
            code = 0
            break
        else:
            if code == 0:
                break
            elif code == 26:
                #standard restart
                print("")
                print("Restarting Squirtudo")
                print("")
                continue
            else:
                if not autorestart:
                    break
                print("")
                print("Restarting Squirtudo from crash")
                print("")

    print("Squirtudo has closed. Exit code: {exit_code}".format(exit_code=code))

args = parse_cli_args()

if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dirname = os.path.dirname(abspath)
    os.chdir(dirname)

    if args.start:
        print("Launching Squirtudo...")
        run_Squirtudo(autorestart=args.auto_restart)
