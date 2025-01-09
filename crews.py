from crewai import Crew
from agents import Research_Writer_Agents
from tasks import Research_Writer_Tasks
from dotenv import load_dotenv
load_dotenv()
import time

topic = "Artificial Intelligence"

agents= Research_Writer_Agents()
plannerAgent=agents.plannerAgent()
writerAgent=agents.writerAgent()
editorAgent=agents.editorAgent()

tasks=Research_Writer_Tasks()
planer_task=tasks.planer_task(plannerAgent,topic)
writer_task=tasks.writer_task(writerAgent,topic)
editor_task=tasks.editor_task(editorAgent)

crew = Crew(
    agents=[plannerAgent, writerAgent, editorAgent],
    tasks=[planer_task, writer_task, editor_task]
)

# crew = Crew(
#     agents=[
#         email_personalizer,
#         ghostwriter
#     ],
#     tasks=[
#         *personalize_email_tasks,
#         *ghostwrite_email_tasks
#     ],
#     max_rpm=29
# )
start_time = time.time()

results = crew.kickoff()

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Crew kickoff took {elapsed_time} seconds.")