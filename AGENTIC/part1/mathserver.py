from mcp.server.fastmcp import FastMCP
mcp=FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Docstring for add
    
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    :return: Description
    :rtype: int
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Docstring for multiply
    
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    :return: Description
    :rtype: int
    """
    return a * b
# tells the server to use standard input/output for communication
if __name__ == "__main__":
    mcp.run(transport="stdio")

