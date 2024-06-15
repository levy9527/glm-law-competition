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
