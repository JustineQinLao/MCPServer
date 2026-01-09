# MCPServer (FastMCP) – Ubuntu Setup and GitHub Guide

This repository contains a minimal Model Context Protocol (MCP) server built with `FastMCP` from the `mcp` package. It exposes:

- Tools: `greet_user(name)`, `add_numbers(a,b)`, `list_files(directory)` in `server.py`
- Example server with resources and prompts in `main.py` (`add`, `greeting://{name}`, and `greet_user` prompt)

The project is configured with a `pyproject.toml` that depends on `mcp[cli]` and includes an optional `mcp_settings.json` for MCP-aware clients.

## Requirements

- Ubuntu (tested on 22.04+)
- Python 3.12+
- Git

Optional:
- `uv` for faster Python dependency management (you can also use `pip`)

## Quickstart (Ubuntu)

1) Install system prerequisites

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv git
```

2) Create and activate a virtual environment

```bash
python3.12 -m venv venv
source venv/bin/activate
```

3a) Install dependencies with pip

```bash
pip install --upgrade pip
pip install "mcp[cli]>=1.25.0"
```

3b) Or install with uv (optional)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv
source venv/bin/activate
uv pip install "mcp[cli]>=1.25.0"
```

## Running the server

You have two entry points. Pick the one that matches your use case.

1) Minimal tool server (`server.py`)

```bash
source venv/bin/activate
python server.py
```

This exposes tools:
- `greet_user(name: str) -> str`
- `add_numbers(a: int, b: int) -> int`
- `list_files(directory: str = ".") -> str`

2) Example server with resources and prompts (`main.py`)

```bash
source venv/bin/activate
python main.py
```

This exposes:
- Tool: `add(a: int, b: int)`
- Resource: `greeting://{name}`
- Prompt: `greet_user(name: str, style: str = "friendly")`

The example runs with `transport="streamable-http"` (see `main.py`).

## MCP client settings (optional)

If your MCP client supports a settings file (e.g., Windsurf, IDEs), you can point it to your server via `mcp_settings.json`:

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "/absolute/path/to/your/project/venv/bin/python",
      "args": [
        "/absolute/path/to/your/project/server.py"
      ]
    }
  }
}
```

Note: In this repo, `mcp_settings.json` is configured with an absolute path under this user's home directory. You should update the paths to match your machine if you use it locally.

## Project layout

- `server.py` – Minimal FastMCP server exposing three tools
- `main.py` – Demo FastMCP server with a tool, a resource, and a prompt
- `pyproject.toml` – Project metadata and dependency on `mcp[cli]`
- `mcp_settings.json` – Example MCP client configuration (absolute paths; edit for your machine)
- `.gitignore` – Ignores `venv/` and build artifacts

## Publish to GitHub (first time)

You can publish this local project to GitHub using SSH or HTTPS. SSH is recommended once you have SSH keys configured.

1) Configure Git (one-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

2) Initialize the repository (if not already a git repo)

```bash
git init
git add .
git commit -m "Initial commit: FastMCP server"
```

3) Create a new GitHub repository

- Go to https://github.com/new and create a repo, e.g., `MCPServer`.
- Leave it empty (no README/license) since you already have files locally.

4a) Add remote via SSH (recommended)

```bash
# Replace USERNAME and REPO with yours
git remote add origin git@github.com:USERNAME/REPO.git
git branch -M main
git push -u origin main
```

If you don’t have SSH keys yet:

```bash
ssh-keygen -t ed25519 -C "you@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
# Copy the printed key and add it at https://github.com/settings/keys
```

4b) Add remote via HTTPS (alternative)

```bash
# Replace USERNAME and REPO with yours
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

## Development tips

- Keep your virtual environment out of Git: `.gitignore` already excludes `.venv` and `venv/`.
- When moving the project to another machine, recreate the venv and install `mcp[cli]`.
- If you want to package this repo later, consider adding a proper module and entry points in `pyproject.toml`.

## License

Add your preferred license (e.g., MIT) here.

