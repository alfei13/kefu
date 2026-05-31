import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    dashscope_api_key: str = ""
    dashscope_api_base: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    dashscope_model: str = "qwen-plus"
    mock_api_base: str = "http://localhost:8080"
    gradio_server_name: str = "0.0.0.0"
    gradio_server_port: int = 7860

    def __post_init__(self):
        self.dashscope_api_key = os.getenv("DASHSCOPE_API_KEY", self.dashscope_api_key)
