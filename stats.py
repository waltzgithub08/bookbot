def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
            
    return char_count


def sort_on(items):
    return items["num"]


def sort_result_set(dictionary):
    sorted_list = []
    
    for key, value in dictionary.items():
        temp_dict = {}
        if key.isalpha():
            temp_dict["char"] = key
            temp_dict["num"] = value
            
            sorted_list.append(temp_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)
    
    
    return sorted_list
    

        
        


