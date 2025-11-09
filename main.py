from services import open_docker, open_vs_code, open_vpn, open_browser,open_tmux
from config import read_config
import os
import sys

def run_functions(steps):
    for step in steps:
        if "filepath" in step:
            home_directory = os.path.expanduser('~')
            step["filepath"] = os.path.join(home_directory, step["filepath"] )
        match step["type"]:
            case "docker":
                if "filepath" not in step:
                    raise ValueError("no filepath present for docker")
                open_docker(step["filepath"])
            case "vpn":
                if "vpn_name" not in step:
                    raise ValueError("no vpn_name present for vpn")
                open_vpn(step["vpn_name"])
            case "vscode":
                if "filepath" not in step:
                    raise ValueError("no filepath present for vscode")
                if "branch" not in step:
                    open_vs_code(step["filepath"])
                else:
                    open_vs_code(step["filepath"], step["branch"])
            case "browser":
                if "urls" not in step:
                    raise ValueError("no filepath present for vscode")
                if type(step["urls"]) != list:
                    raise ValueError("type of urls is not list")
                open_browser(step["urls"])
            case "tmux":
                if "command" not in step:
                    raise ValueError("no command present for tmux")
                open_tmux(step['command'])

def get_config_and_run(env):
    full_path = os.path.join("./config", f"{env}.yaml")
    if os.path.exists(full_path) and os.path.isfile(full_path):
        steps = read_config(full_path)
        run_functions(steps["steps"])
    print("THIS CONFIG DOES NOT EXIST")

if len(sys.argv) < 2:
    print("pass in an env")
    sys.exit(1)

if len(sys.argv) == 2:
    for i, arg in enumerate(sys.argv[1:]):
        print(f"Argument {i+1}: {arg}")
    get_config_and_run(sys.argv[1])
