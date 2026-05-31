from .base_agent import BaseAgent


class AftersaleAgent(BaseAgent):
    name = "aftersale"

    TOOL_NAMES = ["query_aftersale", "create_aftersale"]

    def _build_system_prompt(self, context: dict = None) -> str:
        return (
            "你是售后服务专家，帮助用户处理退款、换货、维修等售后问题。\n"
            "你需要使用工具查询售后进度或创建售后申请，然后给出清晰的指导。\n"
            "回答时要耐心、体贴，理解用户的不满，提供切实可行的解决方案。"
        )

    def process(self, message: str, session_id: str, context: dict = None) -> str:
        return self._process_with_tools(message, session_id, self.TOOL_NAMES)
