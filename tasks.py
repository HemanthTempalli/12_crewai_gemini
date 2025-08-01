from crewai import Task
from tools import tool
from agents import news_research_agent,writer_agent

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}. "
    "Focus on identifying pros and cons and the overall narrative. "
    "Your final report should clearly articulate the key points, "
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3-paragraph report on the latest AI trends.',
  tools=[tool],
  agent=news_research_agent,
)


# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an insightful article on {topic}. "
    "Focus on the latest trends and how it's impacting the industry. "
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='A 4-paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=writer_agent,
  async_execution=False,
  output_file='new-blog-post.txt'
)
