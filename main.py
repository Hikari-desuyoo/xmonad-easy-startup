from os import listdir
from os.path import isfile, join
from script import Script

#cd /home/hikari/projetos/coding/pessoal/startup; python3 main.py

class Startup():
    def __init__(self):
        self.script_path = "scripts/"
        self.scripts = self.get_scripts()

    def get_all_script_filepaths(self):
        return [self.script_path+f for f in listdir(self.script_path) if isfile(join(self.script_path, f))]
    
    def get_scripts(self):
        all_script_filepaths = self.get_all_script_filepaths()
        scripts = [Script(filepath) for filepath in all_script_filepaths]
        active_scripts = filter(lambda script: script.active, scripts)
        return list(active_scripts)
    
    def run_scripts(self):
        [script.run() for script in self.scripts]
        

if __name__ == "__main__":
    startup = Startup()
    startup.run_scripts()
