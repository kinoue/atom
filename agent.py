from os.path import dirname

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.prompts import SystemMessagePromptTemplate, PromptTemplate
from langchain.tools import ShellTool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain import hub
from llms import llms

llm = llms['gpt4']['model']

file_management_toolkit = FileManagementToolkit(root_dir=dirname(__file__))

shell_tool = ShellTool()
shell_tool.description = (
    shell_tool.description +
    "Use this tool to execute git only. " +
    f"args {shell_tool.args}".replace("{", "{{").replace("}", "}}") 
)

tools = file_management_toolkit.get_tools() + [shell_tool]

prompt = hub.pull("hwchase17/openai-tools-agent")
system_message_prompt_template_text = '''
    You are a helful assistant for building streamlit apps. You suggest python
    codes based on the user's ideas, and deploy it as part of the steamlit app
    through which the user and you are communicating.
    
    The main script for the app is main.py.
    If the user requests to deploy the python code, you will save the code in a
    file with an appropriate name. Make sure the script is wrapped in a function
    definition called 'app' except the import statements. Then, modify main.py so that the app is displayed
    in the sidebar of the main screen, as part of the radio button option.
'''
prompt.messages[0] = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=[],
        template=system_message_prompt_template_text
    )
)

agent = create_openai_tools_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def ask_agent(message):
    return agent_executor.invoke({"input": message})