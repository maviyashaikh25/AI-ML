from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")
@mcp.tool()
def get_weather(location: str) -> str:  
    """
    Docstring for get_weather
    
    :param location: Description
    :type location: str
    :return: Description
    :rtype: str
    """
    # Placeholder implementation, replace with actual weather fetching logic
    return f"The current weather in {location} is sunny with a temperature of 25°C."


# tells the server to use standard input/output for communication
if __name__ == "__main__":  
    mcp.run(transport="streamable--http")