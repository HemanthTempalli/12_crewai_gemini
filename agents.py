from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # ✅ Use model= NOT model_name=
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


# Creating a senior researcher agent with memory and verbose mode
news_research_agent = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of "
        "innovation, eager to explore and share knowledge that could change "
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a writer agent with custom tools responsible for writing news blogs
writer_agent = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))
