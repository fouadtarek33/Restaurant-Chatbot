from urllib import response

from ollama import chat
import arabic_reshaper
from bidi.algorithm import get_display
import time




# chatbot = pipeline(
#     "text-generation",
#     model="Qwen/Qwen2.5-1.5B-Instruct"
# )

# streamer = TextIteratorStreamer(
#     chatbot.tokenizer,
#     skip_prompt=True,
#     skip_special_tokens=True
# )




def fix_arabic(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


def ai_assistant(df, cart):








    menu = ""

    for _, row in df.iterrows():
        menu += (
            f"ID: {row['ID']}\n"
            f"Name: {row['Name']}\n"
            f"Category: {row['Category']}\n"
            f"Price: {row['Price']} EGP\n"
            f"Available Quantity: {row['Quantity']}\n"
            "-------------------------\n"
        )
    cart_info = str(cart)


    messages = [
{
    "role": "system",
    "content": f"""
أنت مساعد ذكاء اصطناعي احترافي لمطعم.

مهمتك هي مساعدة العميل في اختيار الطعام والإجابة عن أي سؤال يخص المطعم.

هذه هي قائمة الطعام الحالية:

{menu}

وهذه هي سلة العميل الحالية:

{cart_info}

التعليمات:

1- اعتمد فقط على البيانات الموجودة في قائمة الطعام السابقة.
2- لا تخترع أي وجبة أو سعر أو كمية غير موجودة.
3- قبل الإجابة، حلل البيانات بنفسك ثم استنتج الإجابة.
4- إذا سُئلت عن:
   - أرخص عنصر
   - أغلى عنصر
   - أفضل قيمة
   - جميع المشروبات
   - جميع الحلويات
   - العناصر الأقل من سعر معين
   - العناصر الأعلى من سعر معين
   - المقارنة بين عنصرين
   فيجب أن تستنتج الإجابة من القائمة، وليس من ذاكرتك.

5- إذا لم تجد العنصر داخل القائمة أخبر المستخدم بذلك.
6- إذا كانت السلة فارغة فأخبره أنها فارغة.
7- إذا طلب ترشيح وجبة، رشح من القائمة فقط مع ذكر السبب.
8- إذا كانت ميزانيته محددة، اقترح عناصر تناسبها.
9- لا تذكر معلومات غير موجودة.
10- أجب بالعربية إذا تحدث المستخدم بالعربية، وبالإنجليزية إذا تحدث بالإنجليزية.
11- اجعل إجاباتك قصيرة وواضحة ومهنية.
12- فكر خطوة بخطوة داخليًا ثم أعطِ النتيجة النهائية فقط.
13- اطلب من المستخدم ميزانيته إذا أراد اقتراح وجبةوتعامل مع ذلك كشرط أساسي.
14- إذا طلب المستخدم اقتراح وجبة، اسأله عن ميزانيته أولاً، ثم اقترح وجبة مناسبة من القائمة مع ذكر السبب.
15-  اذا طلب المستخدم اشياء خارج القائمة، اجبه بانك لا تستطيع مساعدته لانها خارج القائمة.
16- اذا طلب المستخدم اشياء قيمتها الاجماليه تتعدي ال 500 جنيه مصري اعمله خصم عشره ف الميزة على اجمالي الطلب وقل له انه تم عمل خصم 10% علي اجمالي الطلب لان قيمته تتعدي ال 500 جنيه مصري.
17- اذا طلب المستخدم اشياء قيمتها الاجماليه تتعدي ال 1000 جنيه مصري اعمله خصم عشره ف الميزة على اجمالي الطلب وقل له انه تم عمل خصم 15% علي اجمالي الطلب لان قيمته تتعدي ال 1000 جنيه مصري.
18- اجب ب اجابات مفهومه وواضحه واحترافيه وابتعد عن الاجابات الغامضه.
19- قبل ان تقترح عليه شي وقبل اي شي اساله عن ميزانيته وتعامل معه علي اساسها -
"""
}
    ]

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



        response = chat(
            model="qwen2.5:3b",
            messages=messages,
            options={
                "temperature": 0.2,
                "top_p": 0.9,
                "num_predict": 300,
            }
        )

        bot_reply = response["message"]["content"]

        print(f"\n🤖 Bot: {fix_arabic(bot_reply)}\n")

        print("\n")

        messages.append({"role": "assistant","content": bot_reply})



