import os
import json

from openai import OpenAI


class LLMClient:
    def __init__(self, api_key=None, api_base=None, model=None):
        self.api_key = api_key or os.environ.get("DASHSCOPE_API_KEY", "")
        self.api_base = api_base or "https://dashscope.aliyuncs.com/compatible-mode/v1"
        self.model = model or "qwen-plus"
        self.client = OpenAI(api_key=self.api_key, base_url=self.api_base)

    def chat(self, messages, temperature=0.7, max_tokens=2048):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content or ""
        except Exception:
            return ""

    def chat_with_tools(self, messages, tools, temperature=0.7):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools,
                temperature=temperature,
            )
            choice = response.choices[0]
            reply_text = choice.message.content or ""
            raw_tool_calls = choice.message.tool_calls
            if not raw_tool_calls:
                return (reply_text, [])
            tool_calls = []
            for tc in raw_tool_calls:
                tool_calls.append(
                    {
                        "name": tc.function.name,
                        "arguments": json.loads(tc.function.arguments),
                    }
                )
            return (reply_text, tool_calls)
        except Exception:
            return ("", [])

    def chat_json(self, messages, temperature=0.7):
        try:
            augmented = messages + [
                {"role": "system", "content": "请以JSON格式返回"}
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=augmented,
                temperature=temperature,
                response_format={"type": "json_object"},
            )
            content = response.choices[0].message.content or ""
            return json.loads(content)
        except Exception:
            return {}
