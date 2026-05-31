import gradio as gr
from kefu.gateway import Gateway
from kefu.config import Config

gateway = None


def init_gateway():
    global gateway
    if gateway is None:
        config = Config()
        gateway = Gateway(config)


def chat(message, history, user_id):
    init_gateway()
    session_id = f"user_{user_id}"
    try:
        reply = gateway.process(message, session_id=session_id, user_id=int(user_id))
        return reply
    except Exception as e:
        return f"抱歉，系统出现异常，请稍后重试。错误信息: {str(e)}"


def main():
    init_gateway()
    with gr.Blocks(title="AI电商客服系统", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 🤖 AI电商客服系统\n多智能体架构 | 售前咨询 · 产品问答 · 订单查询 · 优惠券 · 售后服务")

        with gr.Row():
            user_id_input = gr.Number(value=1, label="用户ID", precision=0)

        chatbot = gr.Chatbot(height=500, type="messages")
        msg_input = gr.Textbox(placeholder="请输入您的问题，例如：我想查订单、有什么优惠、手机推荐...", show_label=False)

        def respond(message, chat_history, user_id):
            reply = chat(message, chat_history, user_id)
            chat_history.append({"role": "user", "content": message})
            chat_history.append({"role": "assistant", "content": reply})
            return "", chat_history

        msg_input.submit(respond, [msg_input, chatbot, user_id_input], [msg_input, chatbot])

        gr.Examples(
            examples=["我想买一部手机，有什么推荐？", "查一下我的订单", "有没有优惠券可以用？", "我想退货", "你好呀"],
            inputs=msg_input
        )

    config = Config()
    demo.launch(server_name=config.gradio_server_name, server_port=config.gradio_server_port)


if __name__ == "__main__":
    main()
