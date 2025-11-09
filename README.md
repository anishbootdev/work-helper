# Work Helper

A development environment automation tool that orchestrates multiple services and applications based on YAML configuration files. Automate your entire dev setup with a single command.

## Features

- **Docker Management**: Start Docker containers via docker-compose with automatic Docker daemon detection
- **VS Code Integration**: Open projects in VS Code with optional git branch checkout
- **VPN Connection**: Connect to VPN (Tunnelblick) with connection polling
- **Browser Automation**: Open Chrome with specific URLs and profiles
- **tmux Sessions**: Start tmux sessions with custom commands

## Prerequisites

- Python 3.11 or higher
- macOS (currently uses macOS-specific commands)
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip
- Docker Desktop (if using docker automation)
- Tunnelblick (if using VPN automation)
- VS Code with `code` CLI command
- Google Chrome
- tmux

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd work-helper
```

2. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

Note: You'll need to install PyYAML:
```bash
uv add pyyaml
# or
pip install pyyaml
```

## Configuration

Create YAML configuration files in the `config/` directory. Each file represents a different environment setup.

### Configuration File Format

```yaml
steps:
  - type: docker
    filepath: path/to/docker-compose.yml  # Relative to home directory

  - type: vscode
    filepath: path/to/project  # Relative to home directory
    branch: main  # Optional: git branch to checkout

  - type: vpn
    vpn_name: your-vpn-name  # Name as it appears in Tunnelblick

  - type: browser
    urls:  # List of URLs to open
      - https://example.com
      - https://localhost:3000

  - type: tmux
    command: your-command-here  # Command to run in tmux session
```

### Example Configuration

See `config/local-dev.yaml` for a working example:

```yaml
steps:
  - type: docker
    filepath: Desktop/TWID/issuer-service/deployment/dev/docker-compose.yml
  - type: vscode
    filepath: Desktop/TWID/issuer-service
  - type: tmux
    command: docker logs -f twidpay
```

### Configuration Options

#### Docker
- `type`: `"docker"`
- `filepath`: Path to docker-compose.yml (relative to home directory)
- Automatically starts Docker Desktop if not running
- Waits up to 30 seconds for Docker daemon to be ready
- Runs `docker compose up -d --build`

#### VS Code
- `type`: `"vscode"`
- `filepath`: Path to project directory (relative to home directory)
- `branch`: (optional) Git branch to checkout after opening

#### VPN
- `type`: `"vpn"`
- `vpn_name`: VPN configuration name in Tunnelblick
- Waits up to 30 seconds for connection to establish
- Polls connection status every 2 seconds

#### Browser
- `type`: `"browser"`
- `urls`: List of URLs to open in Chrome
- Opens in Default Chrome profile (hardcoded)

#### tmux
- `type`: `"tmux"`
- `command`: Command to run in new tmux session
- Creates session named "local-dev"

## Usage

Run the tool with your environment configuration name:

```bash
python main.py <environment-name>
```

Example:
```bash
python main.py local-dev
```

This will execute all steps defined in `config/local-dev.yaml` sequentially.

### Creating Your Own Configuration

1. Create a new YAML file in the `config/` directory:
```bash
touch config/my-project.yaml
```

2. Define your steps using the configuration format above

3. Run it:
```bash
python main.py my-project
```

## Project Structure

```
work-helper/
├── main.py                 # Entry point and orchestration logic
├── config/
│   ├── __init__.py
│   ├── config.py          # YAML config parser
│   ├── local-dev.yaml     # Example config
│   ├── prod-debug.yaml    # Example config
│   ├── beta-debug.yaml    # Example config
│   └── cug-debug.yaml     # Example config
├── services/
│   ├── __init__.py
│   ├── docker.py          # Docker automation
│   ├── vscode.py          # VS Code automation
│   ├── vpn.py             # VPN automation
│   ├── browser.py         # Browser automation
│   └── tmux.py            # tmux automation
├── pyproject.toml
└── README.md
```

## How It Works

1. You specify an environment name as a command-line argument
2. The tool loads the corresponding YAML file from `config/<environment>.yaml`
3. Each step is executed sequentially in the order defined
4. File paths are automatically expanded from `~` (home directory)
5. The tool provides feedback for each step and handles errors gracefully

## Customization

### Adding New Service Types

1. Create a new file in `services/` directory
2. Implement your service function
3. Add it to `services/__init__.py`
4. Add a new case in `main.py`'s `run_functions()` match statement

### Modifying Behavior

- **Docker retry attempts**: Edit `retries` variable in `services/docker.py:11`
- **VPN timeout**: Edit `timeout` variable in `services/vpn.py:20`
- **Chrome profile**: Edit profile name in `services/browser.py:6,11`
- **tmux session name**: Edit session name in `services/tmux.py:8`

## Troubleshooting

- **"THIS CONFIG DOES NOT EXIST"**: Check that your YAML file exists in `config/` directory
- **Docker fails to start**: Ensure Docker Desktop is installed and you have proper permissions
- **VPN connection timeout**: Verify VPN name matches exactly as shown in Tunnelblick
- **VS Code doesn't open**: Ensure `code` command is in your PATH
- **tmux session conflicts**: Close existing "local-dev" tmux session first

## Platform Support

Currently macOS only due to:
- `open` command usage for Docker Desktop and Chrome
- Tunnelblick AppleScript integration
- Chrome profile path assumptions

Linux/Windows support would require platform-specific adaptations.

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
