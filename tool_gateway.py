
# Central Tool Authorization Gateway
# All tool calls must pass through this file

# Only these tools are approved.
ALLOWED_TOOLS = {
    "find_device",
    "read_report",
}


# A harmless demonstration tool
def find_device(report):
    if "SENSOR-17" in report:
        return "SENSOR-17"
    return "No device found"


def read_report(report):
    return report


# This tool represents a restricted operation
# It must never be available through the gateway
def mock_secret_tool():
    return "DEMO-SECRET-123"


# Central authorization check
def execute_tool(tool_name, report):
    # Reject tools that are not approved
    if tool_name not in ALLOWED_TOOLS:
        return {
            "allowed": False,
            "tool": tool_name,
            "result": "Access denied",
        }

    # Execute only recognized and approved tools
    if tool_name == "find_device":
        result = find_device(report)

    elif tool_name == "read_report":
        result = read_report(report)

    else:
        # Safe fallback if configuration is inconsistent
        return {
            "allowed": False,
            "tool": tool_name,
            "result": "Access denied",
        }

    return {
        "allowed": True,
        "tool": tool_name,
        "result": result,
    }


# Quick checks
if __name__ == "__main__":
    sample_report = "Device: SENSOR-17"

    print(execute_tool("find_device", sample_report))
    print(execute_tool("mock_secret_tool", sample_report))
    print(execute_tool("unknown_tool", sample_report))
