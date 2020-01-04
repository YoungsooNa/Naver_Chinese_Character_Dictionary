from search import NCSearch

already_searched = {}

result_file_name = "result"
if __name__ == '__main__':
    NCS = NCSearch()
    with open(result_file_name + ".txt", "w", encoding="utf-8") as wf:
        wf.write("result\n")

    with open("read.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            # 여백으로 라인을 단어로 쪼갬
            for word in line.strip().split(" "):
                with open(result_file_name + ".txt", "a", encoding="utf-8") as wf:
                    wf.write("-------------------------------------------------\n")
                clean_word = ""
                for c in word:
                    if ord('가') <= ord(c) <= ord('힣'):
                        pass
                    elif c in "\n\t\r ":
                        pass
                    else :
                        clean_word += c

                # 한자로만 이루어진 단어로 검색
                sound, meaning = NCS.searchLetters(clean_word)
                if sound is None or meaning is None:
                    pass
                else:
                    with open(result_file_name+".txt", "a", encoding="utf-8") as wf:
                        print(clean_word + ' : ' + sound + '\n   ' + meaning, end="\n")
                        wf.write(clean_word + ' : ' + sound + '\n   ' + meaning + "\n")
                        wf.close()
                for c in clean_word:
                    if c in already_searched.keys():
                        sound = already_searched[c][0]
                        meaning = already_searched[c][1]
                    else:
                        sound, meaning = NCS.search(c)
                        if sound is None or meaning is None:
                            continue
                        else:
                            already_searched[c] = (sound, meaning)
                    print(c + ' : ' + sound + '\n   ' + meaning, end="\n")
                    with open(result_file_name + ".txt", "a", encoding="utf-8") as wf:
                        wf.write(c + ' : ' + sound + '\n   ' + meaning + "\n")
                        wf.close()
                with open(result_file_name + ".txt", "a", encoding="utf-8") as wf:
                    wf.write("-------------------------------------------------\n\n")

    print("완료")

    NCS.close()

