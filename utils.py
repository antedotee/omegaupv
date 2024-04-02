import json

from enums import Model
from prompts import PROMPT


def create_openai_chat_completion(openai_client, messages, model=Model.GPT_4.value, temperature=0, stream=False, **kwargs):
    additional_request_params = {}
    response_format = kwargs.get('response_format')
    if response_format:
        additional_request_params['response_format'] = response_format

    response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            stream=stream,
            **additional_request_params
    )

    if stream:
        streamed_response = ""
        for chunk in response:
            try:
                message = chunk.choices[0].delta.content or ""
                streamed_response += message
            except:
                continue
            yield streamed_response
        return

    data = response.choices[0].message.content
    yield {
            'success': True,
            'data': data,
            'response': response.model_dump()
    }


def get_user_message_category(openai_client, messages):
    user_message = messages[-1]['content']
    message_history = messages[:-1]
    prompt = PROMPT['MESSAGE_CATEGORY_DETECTION'].format(user_message=user_message)
    response = create_openai_chat_completion(
            openai_client,
            message_history + [{'role': 'system', 'content': prompt}],
            model=Model.GPT_4_PREVIEW.value,
            temperature=0,
            stream=False,
            response_format={'type': 'json_object'}
    )
    response = next(response)

    return json.loads(response['data'])['category']


def get_answer_bucket(openai_client, messages):
    user_message = messages[-1]['content']
    message_history = messages[:-1]
    prompt = PROMPT['ANSWER_BUCKET'].format(user_message=user_message)
    response = create_openai_chat_completion(
            openai_client,
            message_history + [{'role': 'system', 'content': prompt}],
            model=Model.GPT_4_PREVIEW.value,
            temperature=0,
            stream=False,
            response_format={'type': 'json_object'}
    )
    response = next(response)

    return json.loads(response['data'])['bucket']

