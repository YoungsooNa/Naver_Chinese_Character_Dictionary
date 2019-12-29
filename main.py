from search import NCSearch

already_searched = {}
result_word = ""

if __name__ == '__main__':
    NCS = NCSearch()

    with open("read.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            for c in line.strip():
                if ord('가') <= ord(c) <= ord('힣'):
                    pass
                elif c in "\n\t\r ":
                    pass
                else:
                    result_word += c
                    if c in already_searched.keys():
                        sound = already_searched[c][0]
                        result = already_searched[c][1]
                    else:
                        sound, meaning = NCS.search(c)
                        already_searched[c] = (sound, meaning)
                    print(c + ' : ' + sound + '\n' + meaning, end="\n")
    print("검색 완료")
    with open("result.txt", "w", encoding="utf-8") as wf:
        for c in result_word:
            if c in already_searched.keys():
                wf.write(c + ' : ' + already_searched[c][0] + '\n' + already_searched[c][1] + "\n")

        print("쓰기 완료")

    NCS.close()

