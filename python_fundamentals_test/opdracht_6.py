import keyword

def contains_keyword(*input):
    keyword_present=False
    
    for x in input:
        if keyword.iskeyword(x):
            keyword_present=True
            break
    print(keyword_present)

#test
contains_keyword("hello","goodbye")
contains_keyword("def","haha","lol",'chickens are evil','42')
contains_keyword('four','if','for')
contains_keyword('blabla','doggo','crab','anchor')
contains_keyword('grizzly','ignore','return','false')

