import os
cwd = os.getcwd()
os.chdir(cwd+ "Squid game_reviews\\reviews\\review")

files = os.listdir()
helpful = {}

for f in files:
    if not (f.endswith(",txt")):
        continue
    infile = open(f, "r", encoding = "utf-8")

    interest = []
    wordnum = 0
    for lines in infile:
        line = lines.strip()
        word = line.split()
        if (line.endswith("helpful")):
            if word[1] == "out" and word[2] == "of" and word[3] != "0":
                help = int(word[0])
                all = int(word[3]) # helpful과 not-helpful을 다 합친 '관심'의 수
                help_ratiop = round((help/all) * 100, 2) # 관심에서 helpful의 비율
                interest.append(help)
                interest.append(all)
                interest.append(help_ratio)
                helpful[f] = interest
    infile.close()

    # 관심의 크기 순으로 배열 후 관심이 가장 많은 20개 추출
    helpful_sort = dict(sorted(helpful.items(), key = lambda x:x[1][1], reverse = True))
    res = {}
    cnt = 0

    print("관심 수, 단어 개수, 파일명")
    for i in helpful_sort:
        res[i] = helpful_sort[i]
        print(res[i][1], rs[i][3], i)
        cnt += 1
        if cnt == 20:
            break
    print("x" * 40)
    
    # 관심 Top 20에서 helpful의 비율순으로 Top 10과 Bottom 10을 나눔
    res_sort = dict(sorted(res.items(), key = lambda x:x[1][2], reverse = True))
    top = {}
    bottom = {}
    cnt = 0
    for i in res_sort:
        if cnt < 10:
            top[i] = res_sort[i]
            cnt += 1
        else:
            bottom[i] = res_sort[i]

    # 관심 Top 10의 단어들 추출
    table = [',', ';', '}', '{', '-', '/', '\\', '?', '!']
    top_words = {}
    bottom_words = {}
    for f in top:
        infile = open(f, "r", encoding = "utf-8")
        for lines in infile:
            for x in table:
                lines = lines.lower().replace(x, ' ')
            words = lines.strip().split()
            for i in words:
                if i in top_words:
                    top_words[i] += 1
                else: top_words[i] = 1

    # 관심 bottom 10의 단어들 추출
    for f in bottom:
        infile = open(f, "r", encoding = "utf-8")
        for lines in infile:
            for x in table:
                lines = lines.lower().replace(x, ' ')
            words = lines.strip().split()
            for i in words:
                if i in bottom_words:
                    bottom_words[i] += 1
                else: bottom_words[i] = 1

    table = ["a", "the", "are", "is", "this", "i", "am", "an", "and", "did", "or", "on",
    "of", "it", "you", "your", "my", "where", "which", "who", "that", "thats", "their", 
    "them", "be", "if", "to", "in", "was", "all", "helpful", "sign", "in", "vote", "permalink", 
    "found", "review", "out", "but", "as", "they", "at", "from", "with", "for", "by", "he", "it\s"] # 제외시킬 단어 리스트

    for x in table:
        if x in top_words:
            del top_words[x]
        if x in bottom_words:
            del bottom_words
    
    top_sort = sorted(top_words.items(), key = lambda x:x[1], reverse = True)
    bottom_sort = sorted(bottom_words.items(), key = lambda x:x[1], reverse = True)
    for i in range(0, 5):
        print(top_sort[i])

    print("x" * 40)

    for i in range(0, 5):
        print(bottom_sort[i])