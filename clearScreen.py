import subprocess, platform

def clear_screen():
    if platform.system() == "Windows":
        subprocess.call(['cls'], shell=True)
    else:
        subprocess.call(['clear'], shell=True)

if __name__ == "__main__":
    clear_screen()