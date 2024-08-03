def count_word_frequency(words):
    result = dict()

    # for word in words:
    #     if word in result:
    #         result[word] += 1
    #     else:
    #         result[word] = 1

    result = {word: result.get(word, 0) + 1 for word in words}

    return result


if __name__ == "__main__":
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
    print(count_word_frequency(words))
