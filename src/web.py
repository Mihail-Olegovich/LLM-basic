import gradio as gr


class ChatbotInterface:
    def __init__(self, rag_chain):
        self.rag_chain = rag_chain

    def respond(self, message, history):
        response = self.rag_chain({"query": message})
        return response["result"]

    def launch(self):
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            msg = gr.Textbox()
            clear = gr.Button("Clear")

            def user(user_message, history):
                return "", history + [[user_message, None]]

            def bot(history):
                user_message = history[-1][0]
                bot_message = self.respond(user_message, history)
                history[-1][1] = bot_message
                return history

            msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
                bot, chatbot, chatbot
            )
            clear.click(lambda: None, None, chatbot, queue=False)

        demo.launch(
            server_name="0.0.0.0", server_port=7860, show_error=True, share=True
        )
