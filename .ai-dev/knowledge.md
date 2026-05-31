# 知识管理

## 架构决策
- 选择Python自研Agent框架而非LangChain：MVP阶段轻量优先，避免重依赖
- 选择Gradio而非Streamlit：Gradio Chatbot组件更适合对话式UI
- 选择Spring Boot+H2做Mock：Java生态标准，内嵌数据库零安装
- MCP通过HTTP模拟而非gRPC：MVP阶段HTTP更简单，后续可升级

## 调试经验
- DashScope API需要OpenAI兼容接口：api_base=https://dashscope.aliyuncs.com/compatible-mode/v1
- .env文件不能提交git，API Key只能从环境变量读取

## 项目约定
- Python代码遵循PEP8
- Agent类统一接口：__init__(llm_client, mcp_client, memory) + process(message, context) -> str
- 工具调用统一通过MCPClient.call(tool_name, params)

## 已知陷阱
- DashScope function_calling返回格式与OpenAI略有不同，需要兼容处理
- H2内存数据库重启后数据丢失，需要在application.sql中初始化数据
