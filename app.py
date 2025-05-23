import gradio
from groq import Groq
client = Groq(
    api_key="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",
)
def initialize_messages():
    return [{"role": "system",
             "content": "You are a skilled criminal lawyer with a successful track record in numerous cases. Your role is to assist people by providing guidance on Indian laws and offering answers in a professional legal manner."}]
messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
  iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to law"),
                     title="Lawyer ChatBot",
                     description="Chat bot for law assistance",
                     theme="soft",
                     examples=["hi","What is IPC sessions", "how to get a bail"],
                     submit_btn=True
                     )
iface.launch(share=True)
