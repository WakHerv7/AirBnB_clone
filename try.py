#!/usr/bin/python3
import cmd

class test(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

test().cmdloop()
