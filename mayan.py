import nltk
from nltk import CFG

mayanGrammar = CFG.fromstring("""
    PP -> AV | P
    P -> MPV
    AV -> MPV
    MPV -> V
    PP ->  'tene_'|'teche_'|'teti_e_'|'toone_'|'te_exe_'|'leti_obe_|Ltio_'
    P -> 'k'
    AV -> 'táan'
    MPV -> 'in'|'a'|'u'|'k'
    V -> TV|IV
    TV -> 'ukic'|'hantic'|'haylic'|'naaczik'|'cimzik'|'canic'
    IV -> 'ukul'|'hanal'|'hayal'|'naacal'|'cimil'|'canal'
    """)

mayanParser = nltk.ChartParser(mayanGrammar)

def mayanTokenizer(sentence):
    sentence = sentence.lower()
    replacements = {
        'Tene_kin': 'k in',
        'Teche_ka': 'k a',
        'Leti_e_ ku': 'k u',
        'Te_exe_ka': 'Te_exe_ k a',
        'Ltio_ki': 'k i',
    }
    for word, replacement in replacements.items():
        sentence = sentence.replace(word, replacement)
    return sentence.split()  # split by space

sentences = ['Tene_ kin', 'tene_ táan in miis', 'teche_ táan a miis', 'leti_e_ táan u miis', 'toone_ táan k miis', 'te_exe_ táan in miis', 'Leti_obe_ táan a miis']

for sentence in sentences:
    tokens = mayanTokenizer(sentence)
    for tree in mayanParser.parse(tokens):
        print(tree)
        tree.pretty_print()