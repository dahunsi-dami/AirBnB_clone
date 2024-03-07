#!/usr/bin/python3
"""Entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """The command processor's model."""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Command to exit interpreter when EOF is encountered."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Override default emptyline() to do nothing."""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
