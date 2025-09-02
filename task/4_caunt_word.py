'''
Напиши програму, яка:

1. Приймає на вхід довільний текст.

2. Рахує, скільки разів кожне слово зустрічається.

3. Виводить топ-5 найчастіших слів у порядку спадання частоти.


Умови:

Ігнорувати регістр (тобто "Сонце" = "сонце").

Видалити розділові знаки.

Виводити слова й кількість їх появ.
'''

### Моя не завершена спроба

text = 'Сонце світить. Сонце гріє. Люди радіють сонцю.'

punctuation_list = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
    '«', '»', '„', '“', '”', '…',
    '—', '–',  # різні тире
    '·', '•', '✔︎', '★', '☆', '✓'
]

for i in range(len(punctuation_list)):
    text = text.replace(punctuation_list[i], '')

text = text.lower()

bukvu = list(text)

slovo = []
rethennj = []

for i in range(len(bukvu)):
    if bukvu[i] != ' ':
        slovo.append(bukvu[i])
    else:
        rethennj.append(slovo.copy())
        slovo.clear()

# Додаємо останнє слово, якщо воно було
if slovo:
    rethennj.append(slovo.copy())

print(rethennj)


### Розв'язок моїм методом

text = 'Сонце світить. Сонце гріє. Люди радіють сонцю.'

# Розділові знаки
punctuation_list = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
    '«', '»', '„', '“', '”', '…', '—', '–', '·', '•', '✔︎', '★', '☆', '✓'
]

# Очищення тексту від розділових знаків
for p in punctuation_list:
    text = text.replace(p, '')

text = text.lower()

# Розбиваємо текст вручну на слова
bukvu = list(text)
slovo = []
rethennj = []

for i in range(len(bukvu)):
    if bukvu[i] != ' ':
        slovo.append(bukvu[i])
    else:
        rethennj.append(''.join(slovo))
        slovo.clear()

if slovo:
    rethennj.append(''.join(slovo))

# Тепер підрахунок частоти
result = []

for i in range(len(rethennj)):
    if rethennj[i] is None:
        continue

    word = rethennj[i]
    count = 1

    for j in range(i + 1, len(rethennj)):
        if rethennj[j] == word:
            count += 1
            rethennj[j] = None  # Затираємо повтор

    result.append((word, count))
    rethennj[i] = None  # Поточне слово теж затираємо

# Вивід
for word, count in result:
    print(f"{word}: {count}")
    
 
 
 ### Розв'язок GPT
 
 text = 'Сонце світить. Сонце гріє. Люди радіють сонцю.'

# Список розділових знаків
punctuation_list = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
    '«', '»', '„', '“', '”', '…', '—', '–', '·', '•', '✔︎', '★', '☆', '✓'
]

# Очищення тексту від розділових знаків
for p in punctuation_list:
    text = text.replace(p, '')

# Приводимо до нижнього регістру
text = text.lower()

# Розбиваємо текст на слова
words = text.split()

# Підрахунок частот
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Сортуємо за частотою у спадному порядку
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Виводимо топ-5 слів
for word, count in sorted_words[:5]:
    print(f"{word}: {count}")