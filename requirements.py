import subprocess

subprocess.run(["pip", "freeze"], stdout=open("requirements.txt", "w"))
