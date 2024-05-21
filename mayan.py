import nltk
from nltk import CFG

mayanGrammar = CFG.fromstring("""
    S -> PP DET
    
    DET -> AV MPV V N | P MPV V N

    
    AV -> 'táan'                                                    
    P -> 'k'
                            
    MPV -> 'in' | 'a' | 'u' | 'k'
    PP -> 'tene_' | 'teche_' | 'leti_e_' | 'tone_' | 'te_exe_' | 'leti_obe_'
    
    V -> IV | TV                              
    IV -> 'ukic'|'hantic'|'haylic'|'naaczik'|'cimzik'|'canic' 
    TV -> 'ukul'|'hanal'|'hayal'|'naacal'|'cimil'|'canal'
    
    N -> 'já'|'janal'|'summ'|'tunich'|'kay'|'python'
    """)

mayanParser = nltk.ChartParser(mayanGrammar)

def mayanTokenizer(sentence):
    sentence = sentence.lower()
    replacements = {
        #kin case
        'tene_ kin': 'tene_ k in',
        'teche_ kin': 'teche_ k in',
        'leti_e_ kin': 'leti_e_ k in',
        'tone_ kin': 'tone_ k in',
        'te_exe_ kin': 'te_exe_ k in',
        'leti_obe_ kin': 'leti_obe_ k in',

        #ka case
        'tene_ ka': 'tene_ k a',
        'teche_ ka': 'teche_ k a',
        'leti_e_ ka': 'leti_e_ k a',
        'tone_ ka': 'tone_ k a',
        'te_exe_ ka': 'te_exe_ k a',
        'leti_obe_ ka': 'leti_obe_ k a',

        #ku case
        'tene_ ku': 'tene_ k u',
        'teche_ ku': 'teche_ k u',
        'leti_e_ ku': 'leti_e_ k u',
        'tone_ ku': 'tone_ k u',
        'te_exe_ ku': 'te_exe_ k u',
        'leti_obe_ ku': 'leti_obe_ k u',

        #k case
        'tene_ kk': 'tene_ k k',
        'teche_ kk': 'teche_ k k',
        'leti_e_ kk': 'leti_e_ k k',
        'tone_ kk': 'tone_ k k',
        'te_exe_ kk': 'te_exe_ k k',
        'leti_obe_ kk': 'leti_obe_ k k',
        
    }
    for word, replacement in replacements.items():
        sentence = sentence.replace(word, replacement)
    return sentence.split()

sentences = [
            'Tene_ kin ukic já',
            'Teche_ ka hantic janal',
            'Leti_e_ ku haylic summ',
            'Tone_ táan k naaczik tunich',
            'Te_exe_ táan a cimzik kay',
            'Leti_obe_ ku canic python',
            'Tene_ kin ukul já',
            'Teche_ ka hanal janal',
            'Leti_e_ ku hayal summ',
            'Tone_ táan k naacal tunich',
            'Te_exe_ táan a cimil kay',
            'Leti_obe_ ku canal python',
            ]

for sentence in sentences:
    tokens = mayanTokenizer(sentence)
    if not tokens:
        print("Failed to tokenize sentence:", sentence)
    else:
        print("Tokens:", tokens)
        print("Loading trees...")
        for tree in mayanParser.parse(tokens):
            print("Parse tree:")
            tree.pretty_print()
