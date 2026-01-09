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