from subprocess import run,CalledProcessError,PIPE
import shlex
from sys import executable,exit

    
def is_tool_installed(tool):
    try:
        run([tool, "--version"], stdout=PIPE, stderr=PIPE, check=True)
        return True
    except CalledProcessError:
        return False

def install_pipx():
    try:
        if is_tool_installed("pipx"):
            print("pipx is already installed.")
        else:
            run([executable, "-m", "pip", "install", "--user", "pipx"], check=True)
            print("pipx installed successfully.")
    except CalledProcessError as e:
        print(f"Error installing pipx: {e}")
        exit(1)

def install_poetry():
    try:
        if is_tool_installed("poetry"):
            print("poetry is already installed.")
        else:
            run(["pipx", "install", "poetry"], check=True)
            print("poetry installed successfully.")
    except CalledProcessError as e:
        print(f"Error installing poetry: {e}")
        exit(1)
        
def setup_package():
    try:
        #this will check if system is having 
        run(shlex.split("poetry -V"))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        #this commands will setup package
        run(shlex.split("poetry install"))
        run(shlex.split("poetry update"))
        run(shlex.split("poetry shell"))
def main():
    install_pipx()
    install_poetry()
    setup_package()

if __name__ == "__main__":
    main()
