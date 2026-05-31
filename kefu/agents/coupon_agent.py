from .base_agent import BaseAgent


class CouponAgent(BaseAgent):
    name = "coupon"

    TOOL_NAMES = ["query_coupons", "check_coupon"]

    def _build_system_prompt(self, context: dict = None) -> str:
        prompt = (
            "你是优惠券服务专家，帮助用户查询和使用优惠券。\n"
            "你需要使用工具查询用户的优惠券列表或验证优惠券的有效性，然后给出清晰的说明。\n"
            "回答时要友好、准确，帮助用户了解优惠券的使用条件和有效期。"
        )
        if context and context.get("user_id"):
            prompt += f"\n当前用户ID为: {context['user_id']}"
        return prompt

    def process(self, message: str, session_id: str, context: dict = None) -> str:
        if context and context.get("user_id"):
            self.memory.set_context(session_id, "user_id", context["user_id"])
        return self._process_with_tools(message, session_id, self.TOOL_NAMES)
