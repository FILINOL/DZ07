def check_rhythm(slov):
    lines = slov.split()
    syllables = []
    
    for line in lines:
        words = line.split('-')
        syllable_count = sum([count_syllables(word) for word in words])
        syllables.append(syllable_count)
    
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_syllables(word):
    vowels = 'aeiouyаеёиоуыэюя'
    count = 0
    
    for char in word.lower():
        if char in vowels:
            count += 1
    
    return count

slov = input("Введите стихотворение: ")
result = check_rhythm(slov)
print(result)