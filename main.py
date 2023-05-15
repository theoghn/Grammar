def grammar_check(grammar,word,nonTerminal):
    if len(word) == 0 and nonTerminal in grammar:
        for tupl in grammar[nonTerminal]:
            if tupl[0] == '`':
                #if tupl[0].islower() asta daca si cuvintele gen  gen doar 'a'sunt acceptat de gramatica
                return True
    else:
        if nonTerminal in grammar:
            for tupl in grammar[nonTerminal]:
                if word[0] in tupl:
                    # print(tupl,word) - use this for road
                    if len(tupl) == 1:
                        if len(word) == 1:
                            return True
                    elif grammar_check(grammar,word[1:],tupl[1]):
                        return True

grammar = {'S':[('a','A'),('d','E')]
           ,'A':[('a','B'),('a','S')]
           ,'B':[('b','C')]
           ,'C':[('b','D'),('b','B')]
           ,'D':[('c','D'),('e'),( '`')]
           ,'E':[('d')]}
start_nonTerminal = 'S'
word = 'aabbcc'
if grammar_check(grammar,word,start_nonTerminal):
    print("Acceptat")
else:
    print("Refuzat")
