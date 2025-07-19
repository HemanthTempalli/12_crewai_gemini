import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load environment variables from .env file
load_dotenv()

# Validate key
if not os.getenv("SERPER_API_KEY"):
    raise ValueError("SERPER_API_KEY is missing in .env file")

# Correct tool initialization
tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))
