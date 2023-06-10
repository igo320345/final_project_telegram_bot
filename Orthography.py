from spellchecker import SpellChecker
import pymorphy2


def padej(i):
    morph = pymorphy2.MorphAnalyzer()
    slovo = morph.parse(i)[0]
    gent = slovo.inflect({'nomn'})
    gent1 = slovo.inflect({'gent'})
    gent2 = slovo.inflect({'datv'})
    gent3 = slovo.inflect({'accs'})
    gent4 = slovo.inflect({'ablt'})
    gent5 = slovo.inflect({'loct'})
    gent6 = slovo.inflect({'voct'})
    gent7 = slovo.inflect({'gen2'})
    gent8 = slovo.inflect({'acc2'})
    gent9 = slovo.inflect({'loc2'})
    return gent.word,gent1.word,gent2.word,gent3.word,gent4.word,gent5.word,gent6.word,gent7.word,gent8.word,gent9.word


spell = SpellChecker(language='ru')
text = input()
m = []
for f in text.split():
    m.append(f)
    mistakes = spell.unknown(m)
    if len(mistakes) != 0:
        for mistake in mistakes:
            for i in spell.candidates(mistake):
                print(padej(i))
    else:
        print(f)
    m = []