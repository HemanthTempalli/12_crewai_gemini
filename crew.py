

from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_research_agent,writer_agent

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_research_agent,writer_agent],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)