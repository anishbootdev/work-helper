import subprocess
import os
import time

def open_docker(filepath):
    if not filepath:
        return False
    try:
        if subprocess.run(["docker", "info"], capture_output=True, text=True, timeout=5).returncode != 0:
            subprocess.run(["open", "-a", "Docker"], check=False)
        retries = 6
        while subprocess.run(["docker", "info"], capture_output=True, text=True, timeout=5).returncode != 0 and retries:
            print(f"Waiting for Docker... ({6-retries+1}/6)")
            time.sleep(5)
            retries -= 1
        if subprocess.run(["docker", "info"], capture_output=True, text=True, timeout=5).returncode != 0:
            print("Docker failed to start after retries")
            return False
        subprocess.run(["docker", "compose", "-f", filepath, "up", "-d" ,"--build"], text=True, check=True)
        return True
    except Exception as e:
        print("error is", e)
        return False
    
if __name__ == "__main__":
    home_directory = os.path.expanduser('~')
    full_path = os.path.join(home_directory,"Desktop/TWID/issuer-service/deployment/dev/docker-compose.yml")
    print(open_docker(full_path))