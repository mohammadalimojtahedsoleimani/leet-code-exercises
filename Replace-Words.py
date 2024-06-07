def replaceWords(dictionary, sentence):
    sentence_new = sentence.split(' ')
    for word in range(len(sentence_new)):
        for substring in dictionary:
            if substring in sentence_new[word] and sentence_new[word].startswith(substring):
                relevant_sub = [s for s in dictionary if sentence_new[word].startswith(s)]
                print(relevant_sub)
                shortest_string = min(relevant_sub, key=len)
                sentence_new[word] = sentence_new[word].replace(sentence_new[word], shortest_string)
                break
    result = " ".join(sentence_new)
    print(result)


replaceWords(["catt","cat","bat","rat"], 'the cattle was rattled by the battery')
