from .base_agent import BaseAgent


class ChitchatAgent(BaseAgent):
    name = "chitchat"

    def _build_system_prompt(self, context: dict = None) -> str:
        return (
            "你是友好的客服助手，处理闲聊和无法分类的问题。\n"
            "你可以和用户进行轻松的对话，回答一般性问题。\n"
            "如果用户的问题涉及具体业务（如订单、产品、售后等），建议用户描述更具体的需求。"
        )

    def process(self, message: str, session_id: str, context: dict = None) -> str:
        history = self.memory.get_recent_messages(session_id, n=10)
        system_prompt = self._build_system_prompt(context)
        messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]

        reply_text = self.llm.chat(messages)

        self.memory.add_message(session_id, "user", message)
        self.memory.add_message(session_id, "assistant", reply_text)
        return reply_text
