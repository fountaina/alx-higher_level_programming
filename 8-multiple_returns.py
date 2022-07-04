#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) >= 1:
        first_character = sentence[0]
    else:
        first_character = None
    return (length, first_character)
