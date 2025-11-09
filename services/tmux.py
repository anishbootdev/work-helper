import subprocess
import os

def open_tmux(command):
    if not command:
        return False
    try:
        subprocess.run(["tmux", "new-session", "-s", "local-dev", command])
        return True
    except Exception:
        return False
    
if __name__ == "__main__":
    open_tmux('docker logs -f twidpay')