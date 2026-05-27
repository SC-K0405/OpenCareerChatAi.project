def update_memory(user_input, memory):

    text = user_input.lower()

    if "교사" in text:
        if "교육" not in memory["관심사"]:
            memory["관심사"].append("교육")

    if "게임" in text:
        if "게임개발" not in memory["관심사"]:
            memory["관심사"].append("게임개발")

    if "ai" in text:
        if "AI" not in memory["걱정"]:
            memory["걱정"].append("AI 발전")

    if "저출산" in text:
        if "저출산" not in memory["걱정"]:
            memory["걱정"].append("저출산")

    if "사람" in text:
        if "사람을 돕는 것" not in memory["가치"]:
            memory["가치"].append("사람을 돕는 것")

    return memory