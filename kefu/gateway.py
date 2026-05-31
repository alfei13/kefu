from kefu.llm_client import LLMClient
from kefu.mcp_client import MCPClient
from kefu.conversation_memory import ConversationMemory
from kefu.agents.router_agent import RouterAgent
from kefu.agents.presale_agent import PresaleAgent
from kefu.agents.product_agent import ProductAgent
from kefu.agents.order_agent import OrderAgent
from kefu.agents.coupon_agent import CouponAgent
from kefu.agents.aftersale_agent import AftersaleAgent
from kefu.agents.chitchat_agent import ChitchatAgent


class Gateway:
    def __init__(self, config=None):
        if config is None:
            from kefu.config import Config
            config = Config()

        self.llm = LLMClient(
            api_key=config.dashscope_api_key,
            api_base=config.dashscope_api_base,
            model=config.dashscope_model,
        )
        self.mcp = MCPClient(base_url=config.mock_api_base)
        self.memory = ConversationMemory()

        self.router = RouterAgent(self.llm, self.mcp, self.memory)

        self.agents_map = {
            "presale": PresaleAgent(self.llm, self.mcp, self.memory),
            "product": ProductAgent(self.llm, self.mcp, self.memory),
            "order": OrderAgent(self.llm, self.mcp, self.memory),
            "coupon": CouponAgent(self.llm, self.mcp, self.memory),
            "aftersale": AftersaleAgent(self.llm, self.mcp, self.memory),
            "chitchat": ChitchatAgent(self.llm, self.mcp, self.memory),
        }

    def process(self, message: str, session_id: str = "default", user_id: int = 1) -> str:
        try:
            self.memory.set_context(session_id, "user_id", str(user_id))

            agent_name = self.router.process(message, session_id)

            agent = self.agents_map.get(agent_name, self.agents_map["chitchat"])

            reply = agent.process(message, session_id)

            return reply
        except Exception as e:
            return f"抱歉，系统处理时出现异常，请稍后重试。"
