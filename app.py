import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import StructuredTool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.1,
    model=os.environ['MODEL']
)

def load_functions(file_path):
    import importlib.util
    
    module_name = file_path.split('.')[0]
    
    # 创建模块 spec
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    # 加载模块
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # 遍历模块中的所有属性，筛选出函数
    functions = [obj for name, obj in module.__dict__.items()
                 if isinstance(obj, StructuredTool)]
    
    return functions

api_file_path = 'api.py'
tools = load_functions(api_file_path)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是个智能助手，擅长利用工具解决问题。当用户提问时，如果知道利用工具获取答案后，严谨地回答问题即可，不要反问"),
    # ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == '__main__':
    print(
        agent_executor.invoke({"input": "今天几号"})["output"]
    )

# from fastapi import FastAPI
# app = FastAPI(
#     title="Law API Server",
#     version="1.0",
#     description="glm law competition app created by levy",
# )
#
#
# from pydantic import BaseModel
# class Query(BaseModel):
#     q: str
#
# # 使用 post, 请求时没有 encode 的需求, 用 get 则需要客户端　encode，否则中文无法识别（curl里是这样)
# @app.post("/chat")
# def chat(query: Query):
#     return agent_executor.invoke({"input": query.q})
#
# if __name__ == "__main__":
#     import uvicorn
#
#     #curl "http://localhost:9000/chat" -X POST -H "Content-Type: application/json" -d "{\"q\":\"问题\"}"
#     uvicorn.run(app, host="localhost", port=9000)
