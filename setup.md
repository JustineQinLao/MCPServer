# MCP Server Setup Guide for Windsurf IDE

Complete guide to create and configure a Python MCP (Model Context Protocol) server in Windsurf IDE.

**Reference:** [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

---

## 📋 Prerequisites

- Python 3.12 or higher
- Windsurf IDE installed
- Terminal access

---

## 🚀 Step 1: Install UV Package Manager

Install `uv` (fast Python package manager):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal, then verify:

```bash
uv --version
```

---

## 📁 Step 2: Initialize Project

### Option A: Use Existing Folder

```bash
cd /path/to/your/project
uv init .
```

### Option B: Create New Project

```bash
uv init mcp-server-demo
cd mcp-server-demo
```

---

## 📦 Step 3: Install Dependencies

Add the MCP SDK with CLI support:

```bash
uv add "mcp[cli]"
```

Create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate
```

---

## 📝 Step 4: Create Your MCP Server

Create a file named `server.py`:

```python
from mcp.server.fastmcp import FastMCP

# Create server
mcp = FastMCP("My Windsurf MCP Server")

@mcp.tool()
def greet_user(name: str) -> str:
    """Greet a user by name"""
    return f"Hello, {name}! Welcome from your MCP server."

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def list_files(directory: str = ".") -> str:
    """List files in a directory"""
    import os
    try:
        files = os.listdir(directory)
        return "\n".join(files)
    except Exception as e:
        return f"Error: {str(e)}"

# Run the server
if __name__ == "__main__":
    mcp.run()
```

**⚠️ Important:** Make sure to include `mcp.run()` at the end, or the server won't start!

---

## 🧪 Step 5: Test Server Locally (Optional)

Test your server before adding to Windsurf:

```bash
python server.py
```

Press `Ctrl+C` to stop the server.

---

## ⚙️ Step 6: Configure Windsurf MCP Server

### Method 1: Using Windsurf Settings UI (Recommended)

1. **Open Windsurf Settings**
   - Press `Ctrl + ,` OR
   - Click the gear icon in the bottom left

2. **Search for "MCP"** in the settings search bar

3. **Click "Edit in mcp_config.json"** or **"Manage MCPs"**
   - This opens the MCP configuration file at:
     ```
     ~/.codeium/windsurf/mcp_config.json
     ```

4. **Add your server configuration:**
   
   Replace `/path/to/your/project` with your actual project path:
   
   ```json
   {
     "mcpServers": {
       "my-mcp-server": {
         "command": "/path/to/your/project/.venv/bin/python",
         "args": [
           "/path/to/your/project/server.py"
         ]
       }
     }
   }
   ```
   
   **Example:**
   ```json
   {
     "mcpServers": {
       "my-mcp-server": {
         "command": "/home/justine/Desktop/Work/Personal Project/MCPServer/.venv/bin/python",
         "args": [
           "/home/justine/Desktop/Work/Personal Project/MCPServer/server.py"
         ]
       }
     }
   }
   ```

5. **Save the file** (`Ctrl + S`)

### Method 2: Using MCP Server Templates Dialog

1. Open **Command Palette** (`Ctrl + Shift + P`)

2. Search for **"MCP"** and select **"Manage MCP Servers"**

3. Click **"Add custom server +"** button

4. Fill in the details:
   - **Name:** `my-mcp-server`
   - **Command:** `/path/to/your/project/.venv/bin/python`
   - **Arguments:** `/path/to/your/project/server.py`

5. Click **Save** or **Add Server**

---

## ✅ Step 7: Enable MCP in Windsurf

1. In **Settings** (`Ctrl + ,`), search for **"MCP"**
2. Toggle **"Enable Model Context Protocol"** to **ON**
3. Enable MCP in **Cascade** settings if available

---

## 🔄 Step 8: Restart Windsurf

1. **Completely quit** Windsurf (`Ctrl + Q` or File → Quit)
2. **Reopen** Windsurf
3. Your MCP server will auto-connect on startup

---

## 🔍 Step 9: Verify Connection

1. Open **Command Palette** (`Ctrl + Shift + P`)
2. Search for **"MCP"** and select **"Manage MCP Servers"**
3. You should see **"my-mcp-server"** with a **✅ Connected** status

**If you see an error**, check the Troubleshooting section below.

---

## 🎯 Step 10: Test Your MCP Server

In Windsurf's AI chat (Cascade), try asking:
```
Use the greet_user tool to greet John
```

Or:
```
Add the numbers 42 and 58 using the add_numbers tool
```

Or:
```
List the files in my current directory
```

---

## Available Tools in Your MCP Server

Your server provides these tools:

| Tool | Parameters | Description |
|------|-----------|-------------|
| `greet_user` | `name: str` | Greets a user by name |
| `add_numbers` | `a: int, b: int` | Adds two numbers together |
| `list_files` | `directory: str` | Lists files in a directory |

---

## 🛠️ Troubleshooting

### ❌ Error: "failed to initialize server: transport error: server terminated"

**This means your `server.py` is missing the `mcp.run()` code.**

**Fix:** Make sure your `server.py` ends with:

```python
# Run the server
if __name__ == "__main__":
    mcp.run()
```

After fixing, click **"Refresh"** in the Manage MCP Servers dialog or restart Windsurf.

---

### ❌ Server Not Showing Up

1. **Check config file exists:**
   ```bash
   cat ~/.codeium/windsurf/mcp_config.json
   ```

2. **Verify Python path is correct:**
   ```bash
   ls -la /path/to/your/project/.venv/bin/python
   ```

3. **Test server manually:**
   ```bash
   cd /path/to/your/project
   source .venv/bin/activate
   python server.py
   ```
   
   If it runs without errors, the server code is correct.

---

### ❌ Server Shows as Disconnected

1. Make sure MCP is **enabled** in Windsurf Settings
2. **Restart Windsurf** completely (`Ctrl + Q`, then reopen)
3. Check server logs in Windsurf's **Output** panel
4. Verify the paths in `mcp_config.json` are absolute paths (not relative)

---

### 📁 Config File Locations

Windsurf may use one of these locations:

- **Primary:** `~/.codeium/windsurf/mcp_config.json`
- **Alternative:** `~/.config/Windsurf/User/globalStorage/codeium.codeium-enterprise-updater/mcp_settings.json`

Use the primary location for new setups.

---

### 🔧 Common Issues

| Issue | Solution |
|-------|----------|
| Server won't start | Add `mcp.run()` to end of `server.py` |
| Path errors | Use absolute paths, not relative paths |
| Import errors | Make sure virtual environment is activated |
| Server disconnects | Check Python version is 3.12+ |

---

## 📚 Additional Resources

- [MCP Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP Examples](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples)


