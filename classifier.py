def classify_question(user_input):

    text = user_input.lower()

    future_keywords = [
        "ai", "저출산", "취업",
        "경쟁", "미래", "사라질"
    ]

    emotion_keywords = [
        "불안", "걱정", "우울",
        "힘들", "무섭"
    ]

    value_keywords = [
        "행복", "의미", "삶",
        "꿈", "가치"
    ]

    for word in future_keywords:
        if word in text:
            return "future"

    for word in emotion_keywords:
        if word in text:
            return "emotion"

    for word in value_keywords:
        if word in text:
            return "value"

    return "career"