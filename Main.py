spisoooooooooook = []
text = input('Введите любой текст: ')
text = text.lower()
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace('!', '')
text = text.replace('?', '')
saved_text = text[0:]
text = text.split()
longest_word = text[0]
shortest_word = text[0]
cimvoli = {}
clova = {}
print(text)
for i in text:
    if i not in spisoooooooooook:
        spisoooooooooook.append(i)
print("Кол-во слов:", len(text))
print("Кол-во уникальных слов:", len(spisoooooooooook))
for j in text:
    if len(j) > len(longest_word):
        longest_word = j
print("Самое длинное слово:", longest_word)
for k in text:
    if len(k) < len(shortest_word):
        shortest_word = k
print("Самое короткое слово:", shortest_word)
for l in saved_text:
    if l in cimvoli:
        cimvoli[l] += 1
    else:
        cimvoli[l] = 1
print(cimvoli)
for m in text:
    if m in clova:
        clova[m] += 1
    else:
        clova[m] = 1
print(clova)
