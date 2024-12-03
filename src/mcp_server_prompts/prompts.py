import os
from mcp.types import PromptMessage, TextContent, Prompt

current_file_path = os.path.dirname(os.path.abspath(__file__))
async def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

reactAndTailwindCssInfo = Prompt(
    name="react-and-tailwind-css",
    description="Create a React component that uses Tailwind CSS to style Prompt"
)

async def reactAndTailwindCssPrompt() -> PromptMessage:
    return PromptMessage(
        role="user",
        content=TextContent(
            type="text",
            text=await read_file(os.path.join(current_file_path, "prompt_texts/react_and_tailwindcss.txt")),
        ),
    )

modelContextProtocolInfo = Prompt(
    name="model-context-protocol",
    description="Information about the model context protocol Prompt"
)

async def modelContextProtocolPrompt():
    return PromptMessage(
        role="user",
        content=TextContent(
            type="text",
            text=await read_file(os.path.join(current_file_path, "prompt_texts/model_context_protocol.txt")),
        ),
    )
    
djangoNinjaInfo = Prompt(
    name="django-ninja",
    description="Create a django ninja project and app Prompt"
)

async def djangoNinjaPrompt():
    return PromptMessage(
        role="user",
        content=TextContent(
            type="text",
            text=await read_file(os.path.join(current_file_path, "prompt_texts/django-ninja.txt")),
        ),
    )