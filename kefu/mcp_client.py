import httpx


class MCPClient:
    TOOL_MAP = {
        "search_products": {"method": "GET", "path": "/api/products/search", "params": {"query": "keyword"}},
        "get_product_detail": {"method": "GET", "path": "/api/products/{product_id}", "params": {}},
        "query_orders": {"method": "GET", "path": "/api/orders", "params": {"user_id": "userId"}},
        "get_order_detail": {"method": "GET", "path": "/api/orders/{order_id}", "params": {}},
        "query_coupons": {"method": "GET", "path": "/api/coupons", "params": {"user_id": "userId"}},
        "check_coupon": {"method": "GET", "path": "/api/coupons/{code}", "params": {}},
        "create_aftersale": {"method": "POST", "path": "/api/aftersale", "params": {}},
        "query_aftersale": {"method": "GET", "path": "/api/aftersale", "params": {"order_id": "orderId"}},
    }

    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(base_url=self.base_url, timeout=30.0)

    def call(self, tool_name: str, params: dict) -> dict:
        try:
            if tool_name not in self.TOOL_MAP:
                return {"error": f"Unknown tool: {tool_name}", "detail": ""}
            mapping = self.TOOL_MAP[tool_name]
            method = mapping["method"]
            path = mapping["path"]
            param_map = mapping["params"]
            params = params or {}

            if method == "GET":
                if param_map:
                    query_params = {}
                    for src_key, dst_key in param_map.items():
                        if src_key in params:
                            query_params[dst_key] = params[src_key]
                    resp = self.client.get(path, params=query_params)
                else:
                    path_parts = path.split("/")
                    resolved_parts = []
                    for part in path_parts:
                        if part.startswith("{") and part.endswith("}"):
                            key = part[1:-1]
                            resolved_parts.append(str(params.get(key, part)))
                        else:
                            resolved_parts.append(part)
                    resolved_path = "/".join(resolved_parts)
                    resp = self.client.get(resolved_path)
            elif method == "POST":
                resp = self.client.post(path, json=params)
            else:
                return {"error": f"Unsupported method: {method}", "detail": ""}

            return resp.json()
        except Exception as e:
            return {"error": "MCP call failed", "detail": str(e)}

    def get_tools_definition(self) -> list:
        return [
            {
                "type": "function",
                "function": {
                    "name": "search_products",
                    "description": "搜索商品，根据关键词查找匹配的商品列表",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "搜索关键词"}
                        },
                        "required": ["query"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_product_detail",
                    "description": "获取商品详情，根据商品ID查询商品的详细信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "product_id": {"type": "string", "description": "商品ID"}
                        },
                        "required": ["product_id"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "query_orders",
                    "description": "查询用户订单列表，根据用户ID查询该用户的所有订单",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "用户ID"}
                        },
                        "required": ["user_id"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_order_detail",
                    "description": "获取订单详情，根据订单ID查询订单的详细信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "order_id": {"type": "string", "description": "订单ID"}
                        },
                        "required": ["order_id"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "query_coupons",
                    "description": "查询用户优惠券列表，根据用户ID查询该用户的所有优惠券",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "string", "description": "用户ID"}
                        },
                        "required": ["user_id"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "check_coupon",
                    "description": "验证优惠券，根据优惠券代码查询优惠券信息及有效性",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "code": {"type": "string", "description": "优惠券代码"}
                        },
                        "required": ["code"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "create_aftersale",
                    "description": "创建售后服务申请，提交售后工单",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "orderId": {"type": "string", "description": "订单ID"},
                            "type": {"type": "string", "description": "售后类型，如退款、换货等"},
                            "reason": {"type": "string", "description": "售后原因"}
                        },
                        "required": ["orderId", "type", "reason"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "query_aftersale",
                    "description": "查询售后服务进度，根据订单ID查询售后工单状态",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "order_id": {"type": "string", "description": "订单ID"}
                        },
                        "required": ["order_id"]
                    }
                }
            }
        ]
