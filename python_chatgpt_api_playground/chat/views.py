import os
import openai
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

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


@api_view(['POST'])
def chat_api(request):
    user_input = request.data.get('user_input')
    reply = chat(user_input)
    return Response({"reply": reply})
