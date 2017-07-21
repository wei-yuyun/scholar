#coding:utf-8
"""
@file:      kmp
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/22 0:58
@description:
            --
"""
def kmp_match(text, pattern):
    # By checking the largest word suffix which matches the word prefix, we can
    # generate a 'prefix table' that can then be used as a state machine, where 0 is the
    # initial state and the last character in the table being the accpeting state.
    #
    # We generate the prefix table by maintaining a running count of character matches
    # starting from the 2nd character as we are walking the word character by character.
    #
    # The reason this works is because the prefix count reveals how many prefix
    # matches at any point in the string. The prefix matches will let us know where in
    # the word to jump to (state change) if we see a mismatch as we are actually
    # matching the word.
    #

    def init_prefix_table(word):
        prefix_count = 0
        prefix_table = [0]*len(word)
        # start from the 2nd character
        for i in range(1, len(word)):
            if word[i] == word[prefix_count]:
                prefix_count+=1
            else:
                prefix_count = 0
            prefix_table[i] = prefix_count
        return prefix_table

    prefix_table = init_prefix_table(pattern)
    #print prefix_table

    # now that we have the state_table (aka prefix table) created, we can do the string matching
    # using it as a guide for state transitions
    pattern_index = 0
    for text_index, text_ch in enumerate(text):
        # Check for failure; if failure, then transition to the correct
        # intermediate state. If no intermediate state is found, then we will go
        # to the initial state and thus exit the while loop
        # the state variable also informs the correct index into the pattern string
        while pattern_index > 0 and text_ch != pattern[pattern_index]:
            pattern_index = prefix_table[pattern_index-1]

        if text_ch == pattern[pattern_index]:
            if pattern_index == len(pattern)-1:
                return text_index-pattern_index
            # update the automaton pattern_index
            pattern_index+=1

    return -1

if __name__ == '__main__':
    Input = 'wewq','wewq'
    print(Input)
    res = kmp_match(Input[0],Input[1])
    print (res, "{}".format(Input[0][res:res+len(Input[1])]))