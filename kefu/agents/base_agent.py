import json


class BaseAgent:
    name: str = "base"

    def __init__(self, llm_client, mcp_client, memory):
        self.llm = llm_client
        self.mcp = mcp_client
        self.memory = memory

    def process(self, message: str, session_id: str, context: dict = None) -> str:
        raise NotImplementedError

    def _build_system_prompt(self, context: dict = None) -> str:
        return ""

    def _get_tools(self, tool_names: list) -> list:
        all_tools = self.mcp.get_tools_definition()
        return [t for t in all_tools if t["function"]["name"] in tool_names]

    def _execute_tool_calls(self, tool_calls: list) -> list:
        results = []
        for tc in tool_calls:
            result = self.mcp.call(tc["name"], tc["arguments"])
            results.append({"name": tc["name"], "result": result})
        return results

    def _process_with_tools(self, message: str, session_id: str, tool_names: list) -> str:
        history = self.memory.get_recent_messages(session_id, n=10)
        system_prompt = self._build_system_prompt()
        messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]

        tools = self._get_tools(tool_names)
        reply_text, tool_calls = self.llm.chat_with_tools(messages, tools=tools)

        if tool_calls:
            tool_results = self._execute_tool_calls(tool_calls)
            tool_results_str = ""
            for tr in tool_results:
                tool_results_str += f"\n工具 {tr['name']} 返回结果: {json.dumps(tr['result'], ensure_ascii=False)}"

            messages.append({"role": "assistant", "content": reply_text or "正在查询相关信息..."})
            messages.append({
                "role": "user",
                "content": f"以下是工具调用结果：{tool_results_str}\n请根据以上信息回答用户的问题。"
            })
            reply_text = self.llm.chat(messages)

        self.memory.add_message(session_id, "user", message)
        self.memory.add_message(session_id, "assistant", reply_text)
        return reply_text
