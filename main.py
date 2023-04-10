import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def print_hi(message):
    print(f'{message}')


message_history = []


def chat(inp, role='user'):
    message_history.append({'role': role, 'content': inp})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=message_history,
                                            temperature=0,
                                            max_tokens=400)

    reply_content = response.choices[0].message.content
    message_history.append({'role': 'assistant', 'content': reply_content})

    return reply_content


if __name__ == '__main__':
    print(chat('can you tell me the circumference of the sun thank you'))
