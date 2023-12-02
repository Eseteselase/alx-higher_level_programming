#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[:1] == None:
        return
    else:
        return len(sentence), sentence[:1]
