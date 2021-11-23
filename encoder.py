import random

input = "Looom"


def encode_word(word):
    is_encoded = False
    word_list = list(word)
    if len(word_list) < 2:
        return word

    for _ in range(32):
        word_part = word_list[1 : len(word_list) - 1]
        random.shuffle(word_part)
        encoded_word = (
            f"{word_list[0]}{''.join(word_part)}{word_list[len(word_list ) - 1]}"
        )

        if encoded_word != word:
            is_encoded = True
            break

    if not is_encoded:
        raise Exception("Couldn't encode the word, please try again")
    return encoded_word


if __name__ == "__main__":
    print(encode_word(input))
