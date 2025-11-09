import subprocess

def open_browser(urls=[]):
    if not urls or type(urls) != list:
        try:
            subprocess.Popen(["open",  "-n","-a", "Google Chrome","--args","--profile-directory=Default"])
            return True
        except Exception:
            return False
    try:
        command = ["open",  "-n","-a", "Google Chrome","--args","--profile-directory=Default","-u"]
        command.extend(urls)
        subprocess.Popen(command)
        return True
    except Exception:
        return False
    
if __name__ == "__main__":
    open_browser(["https://google.com"])