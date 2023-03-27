import openai


def get_ChatGPT_API():
    sf = open('settings.txt', 'r')
    setfile = sf.readlines()
    return setfile[1].split()[1]


openai.api_key = get_ChatGPT_API()


def chat_ai(mes):
    a = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mes}])
    answer = a['choices'][0]['message']['content']
    ans = f'{answer}'.strip()
    return ans
