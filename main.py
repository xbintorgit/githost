import os
import subprocess

if __name__ == "__main__":
    print("main run ")
    os.system("curl -o 1.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
    os.system("unzip 1.zip && rm 1.zip")
    os.system("ls . -al")

    ngrok_config_content="""
authtoken: 1ylxDDekuZdmYwveMLSYSQBQnR5_6RwqYnWrZ3CgWMiQNjHFK
"""
    with open("ngrok.config.yaml",'w') as f :
        f.write(ngrok_config_content)
    os.system("ngrok tcp 22")
    