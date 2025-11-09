import subprocess
import os
import time

def open_vpn(vpn_name):
    if not vpn_name:
        raise ValueError("vpn_name is non valid")

    # Send connect command
    print(f"Connecting to VPN '{vpn_name}'...")
    try:
        connect_cmd = f'tell application "Tunnelblick" to connect "{vpn_name}"'
        subprocess.run(["osascript", "-e", connect_cmd], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to send connect command: {e}")
        print(f"Error output: {e.stderr}")
        return False

    # Poll for connection status with 30-second timeout
    timeout = 30
    poll_interval = 2
    elapsed = 0

    while elapsed < timeout:
        time.sleep(poll_interval)
        elapsed += poll_interval

        try:
            # Check VPN connection state
            state_cmd = f'tell application "Tunnelblick" to get state of first configuration where name = "{vpn_name}"'
            result = subprocess.run(["osascript", "-e", state_cmd], capture_output=True, text=True, check=True)
            state = result.stdout.strip()

            if state == "CONNECTED":
                print(f"✓ Successfully connected to VPN '{vpn_name}'")
                return True
            elif state == "EXITING":
                print(f"✗ VPN connection failed (state: {state})")
                return False
            else:
                # Still connecting
                if elapsed % 6 == 0:  # Print every 6 seconds
                    print(f"Waiting for connection... ({elapsed}s elapsed, state: {state})")
        except subprocess.CalledProcessError as e:
            print(f"Error checking VPN state: {e.stderr}")
            return False

    print(f"✗ Connection timeout after {timeout} seconds")
    return False
    
if __name__ == "__main__":
    vpn_name = "twid"
    open_vpn(vpn_name)