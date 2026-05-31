from .base_agent import BaseAgent


class PresaleAgent(BaseAgent):
    name = "presale"

    TOOL_NAMES = ["search_products", "get_product_detail"]

    def _build_system_prompt(self, context: dict = None) -> str:
        return (
            "你是电商售前咨询专家，帮助用户了解产品、比较产品、推荐产品。\n"
            "你需要根据用户的需求，使用工具搜索和查询产品信息，然后给出专业的建议。\n"
            "回答时要友好、专业，尽量提供详细的产品信息帮助用户做出购买决策。"
        )

    def process(self, message: str, session_id: str, context: dict = None) -> str:
        return self._process_with_tools(message, session_id, self.TOOL_NAMES)
