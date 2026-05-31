from .base_agent import BaseAgent


class ProductAgent(BaseAgent):
    name = "product"

    TOOL_NAMES = ["search_products", "get_product_detail"]

    def _build_system_prompt(self, context: dict = None) -> str:
        return (
            "你是产品知识专家，回答关于产品规格、功能、使用方法的问题。\n"
            "你需要使用工具查询产品的详细信息，然后准确、专业地回答用户的问题。\n"
            "回答时要准确、详细，必要时引用产品参数说明。"
        )

    def process(self, message: str, session_id: str, context: dict = None) -> str:
        return self._process_with_tools(message, session_id, self.TOOL_NAMES)
