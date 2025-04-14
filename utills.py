import json


def format_available_tools(mcp_response):
    """格式化可用工具列表"""
    return [
        {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            }
        }
        for tool in mcp_response.tools
    ]

def handle_tool_call(content):
    """处理工具调用"""
    tool_call = content.message.tool_calls[0]
    tool_name = tool_call.function.name
    tool_args = json.loads(tool_call.function.arguments)
    return tool_name, tool_args