def word_counter(text):
    word_list = text.split()
    word_counter = 0
    for word in word_list:
        word_counter += 1
    return word_counter

def char_counter(text):
    char_counter = {}
    for char in text:
        char = char.lower()
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter


def dict_sorter(dic):
    sorted = []
     # Transform the dictionary into a list of dictionaries
    for chararcter in dic:
        character_dic = {}
        character_dic["character"]=chararcter
        character_dic["number"]=dic[chararcter]
        sorted.append(character_dic)

    # return the number key from a dictionary
    def number_access(dict):
        return dict["number"]

    sorted.sort(reverse=True,key=number_access)

    return sorted