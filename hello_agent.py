import json

def load_mcp_config():
    with open("mcp_config_example.json", "r") as f:
        return json.load(f)

def dedalus_agent_init():
    print("Initializing MCP agent runtime...")

    config = load_mcp_config()

    status = "Ready to build"
    location = "Tripoli, Greece"

    print(f"Agent Status: {status} in {location}")
    print(f"Loaded MCP Tool: {config['tool_name']}")
    print(f"Tool Description: {config['description']}")
    print("Agent ready to execute MCP tools 🚀")

if __name__ == "__main__":
    dedalus_agent_init()
