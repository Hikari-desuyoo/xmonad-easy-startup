import os
from subprocess import Popen as subprocess_run

def to_terminal(line):
    os.system(line)

class Script():
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            self.content = f.readlines()

        self.remove_content_linebreak()
        self.active = self.check_active()
        self.name = filepath.split("/")[-1]

    def remove_content_linebreak(self):
        self.content = [line.replace("\n","") for line in self.content]
        
    def check_active(self):
        if len(self.content)==0:
            return False
        if self.content[0].lower()=="dont":
            self.content.pop(0)
            return False
        return True
        
    def format(self):
        one_line_command = ";".join(self.content)
        return one_line_command

    def run(self):
        print("[Script]Running", self.name)
        one_line_command = self.format()
        subprocess_run(one_line_command, shell=True)

            