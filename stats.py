def word_count(text):
    word_count = text.split()
    return len(word_count)

def letter_count(text):
    words_to_lower = text.lower()
    counted = {}
    for i in words_to_lower:
        if i not in counted:
            counted[i] = 1
        else:
            counted[i] += 1
    return counted

def sort_characters(characters):
    char_list = []
    for char, count in characters.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict_items):
        return dict_items["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list