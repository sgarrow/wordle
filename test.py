import msvcrt
import pprint as pp

def loadWords(N):
    with open('words_alpha.txt') as word_file:
        validWords  = set(word_file.read().split())
    validWords = set( x for x in validWords if len(x) == N )
    return validWords
##############################################################

def prn(lst):
    lst.sort()
    print()
    if len(lst)<600: pp.pprint(lst)
    print(len(lst))
##############################################################

def getUserInput(prompt, default):
    print( f' Enter {prompt} --> {default}', end = '')
    ui = default + input()
    print(ui)
    return ui
##############################################################

if __name__ == '__main__':

    mustDflt      = ''
    mustntDflt    = ''
    exactsDflt    = ''
    notExactsDflt = ''
    ##########################################################

    while 1:

        N = input( f' Enter word size or (q)uit--> ' )
        if N == 'q': exit()
        wordLst = loadWords(int(N))
        ######################################################
    
        suggest = []
        must = getUserInput('must be in', mustDflt)
        mustDflt = must
        for word in wordLst:
            if all( x in word for x in must):
                suggest.append(word)
        prn(suggest)
        ######################################################

        suggest2 = []
        mustnt = getUserInput('must NOT be in', mustntDflt)
        mustntDflt = mustnt
        for word in suggest:
            if not any(x in word for x in mustnt):
                suggest2.append(word)
        prn(suggest2)
        ######################################################
    
        suggest3 = []
        exacts = getUserInput('exacts', exactsDflt)
        exactsDflt = exacts
        for word in suggest2:
            hasAllExacts = True
            for exact in exacts.split():
                if not word[int(exact[1])] == exact[0]:
                    hasAllExacts = False
            if hasAllExacts:
                suggest3.append(word)
        prn(suggest3)
        ######################################################
    
        suggest4 = []
        notExacts = getUserInput('not exacts', notExactsDflt)
        notExactsDflt = notExacts
        for word in suggest3:
            hasAnyNonExact = False
            for notExact in notExacts.split():
                if word[int(notExact[1])] == notExact[0]:
                    hasAnyNonExact = True
            if not hasAnyNonExact:
                suggest4.append(word)
        prn(suggest4)
        ######################################################
    
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
    ##########################################################

