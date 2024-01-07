from langchain.agents import AgentType, initialize_agent
from llms import llms
from langchain.tools import ShellTool

shell_tool = ShellTool()
llm = llms['gpt4']['model']

shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
    "{", "{{"
).replace("}", "}}")

agent = initialize_agent(
    [shell_tool], llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

'''
agent.run(
    "Download the langchain.com webpage and grep for all urls. Return only a sorted list of them. Be sure to use double quotes."
)
'''

def ask_agent(message):
    return agent.run(message)

def ask_agent0(messages):
    response = llm(messages)
    return response.content

def ask_agent(message):
    return agent.run(message)