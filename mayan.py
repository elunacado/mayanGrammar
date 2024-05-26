import nltk
from nltk import CFG

mayanGrammar = CFG.fromstring("""
    S -> PP DET
    
    DET ->  PMPV MPV V N

    PMPV -> AV|P
    
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
            #I am drinking water regularly
            'Tene_ kin ukic já',
            #You are eating food regularly
            'Teche_ ka hantic janal',
            #He/She is stretching the rope regularly
            'Leti_e_ ku haylic summ',
            #We are lifting the stone
            'Tone_ táan k naaczik tunich',
            #They are killing fish
            'Te_exe_ táan a cimzik kay',
            #They are learning python
            'Leti_obe_ ku canic python',
            #I drink water regularly
            'Tene_ kin ukul já',
            #you eat food regularly
            'Teche_ ka hanal janal',
            #He/She stretch the rope regularly
            'Leti_e_ ku hayal summ',
            #We lift the stone
            'Tone_ táan k naacal tunich',
            #They kill fish
            'Te_exe_ táan a cimil kay',
            #They learn python
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
