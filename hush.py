#!/usr/bin/python3

import glob
import os
from sys import stdin

def expandWildcards():
    args = []
    for command in commands:
        matches = glob.glob(command)
        if len(matches) == 0:
            args.append(command)
        else:
            args.extend(matches)
    return args

def cd():
    try:
        os.chdir(commands[1])
    except FileNotFoundError:
        print(f'cd: {commands[1]}: no such directory')

def fork():
    pid = os.fork()
    if pid == 0:
        exec()
    else:
        os.waitpid(pid, 0)

def exec():
    try:
        os.execvp(commands[0], commands)
    except FileNotFoundError:
        print(f'{commands[0]}: command not found')

print('HUSH> ', end='', flush=True)
for line in stdin:

    commands = line.split()
    commands = expandWildcards()
    if commands[0].lower() == 'exit':
        break
    elif commands[0].lower() == 'cd':
        if len(commands) != 2:
            print('cd: wrong number of arguments')
        else:
            cd()
    else:
        fork()

    print('HUSH> ', end='', flush=True)
