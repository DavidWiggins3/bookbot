def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    word_count = count_words(text)
    #print(word_count)
    character_counts = count_characters(text)
    #print(character_counts)
    sorted_list = convert_to_list_of_dict(character_counts)
    #print(sorted_list)

    print_report(sorted_list, book_path, word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(content):
    words = content.split()
    return len(words)

def count_characters(content):
    result = {}
    lowered_string = content.lower()
    for c in lowered_string:
        if c.isalpha():
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
    return result


def convert_to_list_of_dict(dict):
    result = []
    for c in dict:
        result.append({"character":c, "num":dict[c]})
    
    def sort_on(dict):
        return dict["num"]
    
    result.sort(reverse=True, key=sort_on)
    return result

def print_report(sorted_list, book_path, word_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for entry in sorted_list:
        print(f"The '{entry['character']}' character was found {entry['num']} times")
    print("--- End report ---")

    
main()