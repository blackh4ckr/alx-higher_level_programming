#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return (len(sentence), None)
    else:
        for str in sentence:
            return (len(sentence), str[0])
