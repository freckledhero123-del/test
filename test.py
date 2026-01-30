# Список вопросов, вариантов ответов и правильных ответов
questions = [
    {
        "question": "Столица России?",
        "options": ["1. Москва", "2. Санкт-Петербург", "3. Казань", "4. Новосибирск"],
        "answer": 1
    },
    {
        "question": "2 + 2?",
        "options": ["1. 3", "2. 4", "3. 5", "4. 6"],
        "answer": 2
    },
    {
        "question": "Самый большой океан?",
        "options": ["1. Атлантический", "2. Индийский", "3. Тихий", "4. Северный Ледовитый"],
        "answer": 3
    },
    # Добавьте остальные 12 вопросов по аналогии
    {
        "question": "Какой язык мы сейчас используем?",
        "options": ["1. Java", "2. C++", "3. Python", "4. JavaScript"],
        "answer": 3
    },
    {
        "question": "Сколько цветов у радуги?",
        "options": ["1. 5", "2. 6", "3. 7", "4. 8"],
        "answer": 3
    }
]

# Можно добавить еще вопросы, чтобы было 15
# Просто скопируйте структуру и измените текст

print("Добро пожаловать в тест из 15 вопросов!")
print("Выбирайте вариант ответа, вводя цифру от 1 до 4")
print("=" * 40)

correct_answers = 0
total_questions = len(questions)

for i, q in enumerate(questions, 1):
    print(f"\nВопрос {i}: {q['question']}")
    

    for option in q['options']:
        print(option)
    

    while True:
        try:
            user_answer = int(input("Ваш ответ (1-4): "))
            if 1 <= user_answer <= 4:
                break
            else:
                print("Пожалуйста, введите число от 1 до 4")
        except ValueError:
            print("Пожалуйста, введите число от 1 до 4")
    

    if user_answer == q['answer']:
        print("✅ Правильно!")
        correct_answers += 1
    else:
        print(f"❌ Неправильно. Правильный ответ: {q['answer']}")


print("\n" + "=" * 40)
print("Тест завершен!")
print(f"Ваш результат: {correct_answers} из {total_questions}")

