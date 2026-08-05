import logging
import warnings
import arabic_reshaper
from transformers import logging as tf_logging
from bidi.algorithm import get_display
from transformers import pipeline
import time
warnings.filterwarnings("ignore")
tf_logging.set_verbosity_error()
logging.getLogger("transformers").setLevel(logging.ERROR)

chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-1.5B-Instruct"
)

# streamer = TextIteratorStreamer(
#     chatbot.tokenizer,
#     skip_prompt=True,
#     skip_special_tokens=True
# )

messages = [
    {
        "role": "system",
        "content":"انت مساعد ذكي لمطعم. أجب عن أسئلة العميل باختصار"
    }
]


def fix_arabic(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


def ai_assistant():
    print("🤖 Bot: is typing...")
    time.sleep(3)
    print("""\n
=============================
    AI Assistant 🤖
=============================

Hello! I'm your restaurant assistant.

I can help you:
• Recommend meals 🍕
• Find food by name and ID 🔍
• Suggest meals within your budget 💰
• Answer questions about the menu 📋

Type "exit" to return to the main menu.
    \n""")


    while True:

        user_message = input("🧑🏻 You : ")

        if user_message.lower() == "exit":
            break

        messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        # print("\n🤖 Bot : ", end="", flush=True)

        # thread = Thread(
        #     target=chatbot,
        #     kwargs={
        #         "text_inputs": messages,
        #         "streamer": streamer,
        #         "max_new_tokens": 150,
        #         "truncation": True,
        #         "do_sample": True,
        #         "temperature": 0.7,
        #         "top_k": 50,
        #     },
        # )

        # thread.start()

        # bot_reply = ""

        # for new_text in streamer:
        #     bot_reply += new_text
        #     print(new_text, end="", flush=True)
        #     time.sleep(0.02)




        print("\n🤖 Bot is typing...")
        time.sleep(1)

        response = chatbot(
            messages,
            max_new_tokens=150,
            truncation=True,
            do_sample=True,
            temperature=0.7,
            top_k=50,
        )

        bot_reply = response[0]["generated_text"][-1]["content"]

        print(f"\n🤖 Bot: {fix_arabic(bot_reply)}\n")

        print("\n")

        messages.append({"role": "assistant","content": bot_reply})



