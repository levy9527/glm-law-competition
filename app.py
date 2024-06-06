import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
from datetime import date

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model=os.environ['MODEL'])

@tool
def current_date() -> date:
    """get the current date"""
    today = date.today()
    return today

tools = [current_date]

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是个智能助手，擅长利用工具解决问题。当用户提问时，如果知道利用工具获取答案后，严谨地回答问题即可，不要反问"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

print(
    agent_executor.invoke({"input": "今天几号?"})
)
