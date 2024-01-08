from langchain.agents import AgentType, initialize_agent, AgentExecutor, create_openai_tools_agent
from llms import llms
from langchain.tools import ShellTool
from langchain_community.agent_toolkits import FileManagementToolkit
from os.path import dirname
from langchain import hub
# hub.pull("hwchase17/openai-tools-agent")

llm = llms['gpt4']['model']

file_management_toolkit = FileManagementToolkit(root_dir=dirname(__file__))

shell_tool = ShellTool()
shell_tool.description = (
    shell_tool.description +
    "Use this tool to execute git only. " +
    f"args {shell_tool.args}".replace("{", "{{").replace("}", "}}") 
)

tools = file_management_toolkit.get_tools() + [shell_tool]
agent = create_openai_tools_agent(
    llm=llm,
    tools=tools,
    prompt = hub.pull("hwchase17/openai-tools-agent")
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


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

def ask_agent1(message):
    return agent.run(message)

def ask_agent(message):
    return agent_executor.invoke({"input": message})