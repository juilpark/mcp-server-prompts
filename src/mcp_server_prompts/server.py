import logging
import mcp.types as types
from mcp.server import Server
from mcp_server_prompts.prompts import reactAndTailwindCssInfo, reactAndTailwindCssPrompt, modelContextProtocolInfo, modelContextProtocolPrompt, djangoNinjaInfo, djangoNinjaPrompt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("prompts-server")

app = Server(name="prompts-server")

@app.list_prompts()
async def list_prompts() -> list[types.Prompt]:
    return [
        reactAndTailwindCssInfo,
        modelContextProtocolInfo,
        djangoNinjaInfo,
    ]

@app.get_prompt()
async def get_prompt(name: str, arguments: dict[str, str] | None) -> types.GetPromptResult:
    if name == "react-and-tailwind-css":
        return types.GetPromptResult(
            description=reactAndTailwindCssInfo.description,
            messages=[await reactAndTailwindCssPrompt()],
        )
    elif name == "model-context-protocol":
        return types.GetPromptResult(
            description=modelContextProtocolInfo.description,
            messages=[await modelContextProtocolPrompt()],
        )
    elif name == "django-ninja":
        return types.GetPromptResult(
            description=djangoNinjaInfo.description,
            messages=[await djangoNinjaPrompt()],
        )
    else:
        raise ValueError(f"Unknown prompt: {name}")

async def run():
    from mcp.server.stdio import stdio_server
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())
