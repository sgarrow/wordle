import pprint as pp

def loadWords(N):
    with open('words_alpha.txt') as word_file:
        validWords  = set(word_file.read().split())
    validWords = set( x for x in validWords if len(x) == N )
    return validWords

def prn(lst):
    lst.sort()
    print()
    if len(lst)<600: pp.pprint(lst)
    print(len(lst))
    print()

if __name__ == '__main__':
    N = int(input( 'Enter word size -> ' ))
    wordLst = loadWords(N)

    suggest = []
    must = input( 'Enter must be in -> ' )
    for word in wordLst:
        if all( x in word for x in must):
            suggest.append(word)
    prn(suggest)

    suggest2 = []
    mustnt = input('Enter must NOT be in -> ')
    for word in suggest:
        if not any(x in word for x in mustnt):
            suggest2.append(word)
    prn(suggest2)

    suggest3 = []
    exacts = input('Enter exacts -> ').split()
    for word in suggest2:
        hasAllExacts = True
        for exact in exacts:
            if not word[int(exact[1])] == exact[0]:
                hasAllExacts = False
        if hasAllExacts:
            suggest3.append(word)
    prn(suggest3)

    suggest4 = []
    notExacts = input('Enter not exacts -> ').split()
    for word in suggest3:
        hasAnyNonExact = False
        for notExact in notExacts:
            if word[int(notExact[1])] == notExact[0]:
                hasAnyNonExact = True
        if not hasAnyNonExact:
            suggest4.append(word)
    prn(suggest4)

    aph = list(map(chr, range(ord('a'), ord('z')+1)))
    hist = {}
    for ch in aph:
        hist[ch] = 0

    for word in suggest4:
        for ch in word:
            if ch in word:
                hist[ch] += 1

    for k,v in hist.items():
        if k not in must:
            if v != 0 and v <= len(suggest4):
                print(' ', k, ":", v)
    print()
