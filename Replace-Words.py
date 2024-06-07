def replaceWords(dictionary, sentence):
    sentence_new = sentence.split(' ')
    temp = []
    shortest_string = ''
    for word in range(len(sentence_new)):
        temp = [s for s in dictionary if sentence_new[word].startswith(s)]
        for d in temp:
            if d in sentence_new[word]:
                shortest_string = min(temp, key=len)
                sentence_new[word] = sentence_new[word].replace(sentence_new[word], shortest_string)
                print('hello')
                break
        temp.clear()

    result = " ".join(sentence_new)
    print(result)


replaceWords(["catt", "cat", "bat", "rat"], 'the cattle was rattled by the battery')
