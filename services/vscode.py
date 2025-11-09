import subprocess
import os

def open_vs_code(filepath, branch="master"):
    if not filepath:
        return False
    try:
        subprocess.Popen(["code", filepath, "-n"])
        subprocess.run(["git", "checkout", branch], cwd=filepath, capture_output=True, text=True, check=True)
        return True
    except Exception:
        return False
    
if __name__ == "__main__":
    home_directory = os.path.expanduser('~')
    full_path = os.path.join(home_directory,"Desktop/TWID/issuer-service")
    open_vs_code(full_path, "master")