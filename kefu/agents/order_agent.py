from .base_agent import BaseAgent


class OrderAgent(BaseAgent):
    name = "order"

    TOOL_NAMES = ["query_orders", "get_order_detail"]

    def _build_system_prompt(self, context: dict = None) -> str:
        prompt = (
            "你是订单服务专家，帮助用户查询订单状态、物流信息。\n"
            "你需要使用工具查询用户的订单信息，然后清晰地展示订单状态和物流详情。\n"
            "回答时要准确、耐心，帮助用户了解订单的当前状态。"
        )
        if context and context.get("user_id"):
            prompt += f"\n当前用户ID为: {context['user_id']}"
        return prompt

    def process(self, message: str, session_id: str, context: dict = None) -> str:
        if context and context.get("user_id"):
            self.memory.set_context(session_id, "user_id", context["user_id"])
        return self._process_with_tools(message, session_id, self.TOOL_NAMES)
