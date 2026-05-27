import requests
import streamlit as st

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

def get_ai_response(user_input, memory):

```
url = "https://openrouter.ai/api/v1/chat/completions"

system_prompt = f"""
```

너는 청소년 진로상담 AI이다.

반드시 아래 원칙을 지켜라.

1. 사용자의 삶을 대신 결정하지 마라.
2. 직업을 단정적으로 추천하지 마라.
3. 정보가 부족하면 함부로 결론 내리지 마라.
4. 사용자가 스스로 방향을 탐색하도록 도와라.
5. 현실적 가능성과 사용자의 가치관을 함께 고려하라.
6. 존중하는 말투를 사용하라.
7. 공감은 하되 과장하지 마라.
8. 모르는 사실을 아는 척하지 마라.

현재 사용자 정보:
관심사: {memory["관심사"]}
걱정: {memory["걱정"]}
가치: {memory["가치"]}
"""

```
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
}

try:
    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    ai_message = result["choices"][0]["message"]["content"]

    return ai_message

except Exception as e:
    return f"오류 발생: {str(e)}"
```
