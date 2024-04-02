import dotenv
import gradio as gr
import pandas as pd
import os
from datetime import datetime
from openai import OpenAI


from prompts import SYSTEM_MESSAGES, BUCKET_PROMPT_MAPPING
from questions import QUESTIONS
from utils import create_openai_chat_completion, get_user_message_category, get_answer_bucket

dotenv.load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
openai_client = OpenAI()


def update_question(question_idx):
    return list(), render_question_text(QUESTIONS[question_idx])

def save_chat_history(chat_history):
    df = pd.DataFrame(chat_history, columns=["User", "Assistant"])
    filename = "data.csv"
    df.to_csv(filename, index=False)
    return gr.File(value="data.csv", visible=True)

def render_question_text(question):
    return f"""<h1>{question['title']}</h1>
<p>{question['text']}</p>
<h2>Input</h2>
<p>{question['input']}</p>
<h2>Output</h2>
<p>{question['output']}</p>
<h2>Example</h2>
<p>{question['example']}</p>
"""


with gr.Blocks() as app:
    with gr.Row():
        with gr.Column(scale=0):
            options = [f"{q['title']} - {q['difficulty']}" for q in QUESTIONS]  # Include difficulty level in dropdown options
            dropdown = gr.Dropdown(options, label="Question", type="index", value=options[0])
            html = gr.HTML(render_question_text(QUESTIONS[0]))
        with gr.Column(scale=1):
            chatbot = gr.Chatbot(height='60vh')
            msg = gr.Textbox()
            clear = gr.ClearButton([msg, chatbot])
            download = gr.Button(value="Save Chat History")
            csv = gr.File(interactive=False, visible=False)


    def user(user_message, history):
        return "", history + [[user_message, None]]


    def bot(chat_history, dropdown_idx):
        dropdown_value = options[dropdown_idx]  # Get the selected value from the dropdown options
        question_title = dropdown_value.split(" - ")[0] 
        question = next(q for q in QUESTIONS if q['title'] == question_title)  # Find question by title
        messages = [
                {'role': 'system', 'content': SYSTEM_MESSAGES['MAIN'].format(question=question)},
        ]
        for idx, history in enumerate(chat_history):
            messages.append({"role": "user", "content": history[0]})
            if idx != len(chat_history) - 1:
                messages.append({"role": "assistant", "content": history[1]})

        message_category = get_user_message_category(openai_client, messages)
        if message_category == 1:
            try:
                bot_message = create_openai_chat_completion(
                        openai_client,
                        messages, model='gpt-4',
                        temperature=0,
                        stream=True
                )
                messages.append(
                        {
                                "role": "system",
                                "content": SYSTEM_MESSAGES['GIVE_MINIMAL_HINT']
                        }
                )
                messages.append({"role": "assistant", "content": ""})
                for res in bot_message:
                    chat_history[-1][1] = res
                    yield chat_history
            except:
                return
        else:
            answer_bucket = get_answer_bucket(openai_client, messages)
            prompt = BUCKET_PROMPT_MAPPING[answer_bucket]
            try:
                bot_message = create_openai_chat_completion(
                        openai_client,
                        messages, model='gpt-4',
                        temperature=0,
                        stream=True
                )
                messages.append(
                        {
                                "role": "system",
                                "content": prompt
                        }
                )
                messages.append({"role": "assistant", "content": ""})
                for res in bot_message:
                    chat_history[-1][1] = res
                    yield chat_history
            except:
                return

    download.click(save_chat_history, chatbot, csv)
    
    dropdown.change(update_question, dropdown, [chatbot, html])
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, [chatbot, dropdown], chatbot)

# if __name__ == "__main__":
app.queue()
demo = app.launch(auth=(username, password))
