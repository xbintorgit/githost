import os
import subprocess

if __name__ == "__main__":
    print("main run ")
    os.system("curl -o 1.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
    os.system("unzip 1.zip")
    os.system("ls . -al")