import openai

openai.api_key = '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'


def chat_ai(mes):
    a = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mes}])
    answer = a['choices'][0]['message']['content']
    ans = f'{answer}'.strip()
    return ans
