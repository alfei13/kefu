import json

from .base_agent import BaseAgent


class RouterAgent(BaseAgent):
    name = "router"

    VALID_AGENTS = ["presale", "product", "order", "coupon", "aftersale", "chitchat"]

    def _build_system_prompt(self, context: dict = None) -> str:
        return (
            "你是一个意图分类助手，负责将用户的咨询问题路由到正确的处理Agent。\n"
            "可选的Agent类型如下：\n"
            "- presale: 售前咨询，包括产品推荐、产品比较、购买建议\n"
            "- product: 产品知识，包括产品规格、功能、使用方法\n"
            "- order: 订单服务，包括查询订单状态、物流信息\n"
            "- coupon: 优惠券服务，包括查询优惠券、验证优惠券\n"
            "- aftersale: 售后服务，包括退款、换货、维修\n"
            "- chitchat: 闲聊及其他无法分类的问题\n"
            "请根据用户的消息判断应该路由到哪个Agent，并返回JSON格式：\n"
            '{"agent": "presale|product|order|coupon|aftersale|chitchat", "confidence": 0.0-1.0}\n'
            "只返回JSON，不要返回其他内容。"
        )

    def process(self, message: str, session_id: str, context: dict = None) -> str:
        system_prompt = self._build_system_prompt(context)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ]
        result = self.llm.chat_json(messages)
        agent = result.get("agent", "chitchat")
        confidence = result.get("confidence", 0.0)

        if agent not in self.VALID_AGENTS or confidence < 0.5:
            agent = "chitchat"

        return agent
