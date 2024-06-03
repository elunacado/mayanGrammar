# mayanGrammar
This is my hand in for:  Evidence 2 Generating and Cleaning a Restricted Context Free Grammar 
Were I'll deliver a RCFG (Restricted Context Free Grammar), which is a variation of a CFG and as explained in the webpage for Geeks for Geeks, a CFG is a a type of formal grammar that has four tuples: (V,T,P,S). <br />
![alt text](https://github.com/elunacado/mayanGrammar/blob/main/rcfg.png)
So a RCFG follows the same rules as a CFG but with added restrictions that simplify the parsing and reduce the ambiguity.

## Language Structure 
The language I chose for this hand-in was Mayan, but because of the complexity of this language, I'll be limiting it to the two types of present Mayas have which are Actual Present which describes an action that is taking place at the current moment the rules for this tense are as follows:
| Personal Pronoun     | Auxiliary verbs   | Mixed pronoun verbs | Verb                       | Noun|
|-----------------------|------------------|---------------------|----------------------------|-----|
| Tene'                 | táan             | in                  |   Transitive               |Noun |
| Teche'                | táan             | a                   |   Intransitive             |     |
| Leti'e'               | táan             | u                   |                            |     |
| Tone'                 | táan             | k                   |                            |     |
| Te'exe'               | táan             | a                   |                            |     |
| Leti'obe'             | táan             | u                   |                            |     |

and  Regular present, which describe actions that occur regularly, such as eating or sleeping, and for this tense, the rules are the next ones:

| Personal Pronoun      | Particle        | Mixed pronoun verbs | Verb                       | Noun |
|-----------------------|-----------------|---------------------|----------------------------|------|
| Tene'(I)              | k               | in                  |   Transitive               | Noun |
| Teche'(You)           | k               | a                   |   Intransitive             |      |
| Leti'e'(He/She)       | k               | u                   |                            |      |
| Tone' (We)            | k               | k                   |                            |      |
| Te'exe' (They)        | k               | a                   |                            |      | 
| Leti'obe'* (They)     | k               | u                   |                            |      |


## Verbs
For this hand-in, I chose the following verbs: <br />
Transitive Verbs: → 'ukic'|'hantic'|'haylic'|'naaczik'|'cimzik'|'canic' which means 'to drink'|'to eat'|'to stretch'|'to lift'|'to kill'|'to learn' <br />
Intransitive Verbs: → 'ukul'|'hanal'|'hayal'|'naacal'|'cimil'|'canal' which means 'drink'|'eat'|'stretch'|'lift'|'kill'|'learn' <br />

## Nouns
And my nouns for this hand-in are going to be: <br />
Já|janal|sumn|tunich|kay|python, which means water|food|rope|stone|fish|python (the programming language) <br />

## Model
![alt text](https://github.com/elunacado/mayanGrammar/blob/main/officialTree.jpg)
In this tree, we describe the language as follows:
```python
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
```
So let's explain it section by section
* S → PP DET: A sentence is formed by a Personal Pronoun and a Determinant
* DET → PMPV MPV V N: And the determinant is formed by a PMPV (previous mixed pronoun verbs), an MPV (mixed pronoun verb), a Verb and a Noun
* PMPV → AV|P: This is a placeholder for the parts of the sentence that define the tense of the sentence and can be an AV (auxiliary verb) or a P (particle)
* AV → 'táan'
* P  → 'k'
* MPV: → 'in' | 'a' | 'u' | 'k'
* PP → 'tene_' | 'teche_' | 'leti_e_' | 'tone_' | 'te_exe_' | 'leti_obe_'
* V → IV | TV: The verb can be either transitive or intransitive (is it happening right now or not)
* IV → 'ukic'|'hantic'|'haylic'|'naaczik'|'cimzik'|'canic'
* TV → 'ukul'|'hanal'|'hayal'|'naacal'|'cimil'|'canal'
* N → 'já'|'janal'|'summ'|'tunich'|'kay'|'python'

## Implementation and Complexity
I start the program by importing the natural-language-toolkit and the Context-Free-Grammar section
  ```python
import nltk
from nltk import CFG
```
I set up the sections of the rules of the language
```python
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
```
I parse the chart with the NLTK which has a O(n^3 * g) complexity n being the length of the sentence and the g being the complexity of the grammar </br>

```python
mayanParser = nltk.ChartParser(mayanGrammar)
```
I tokenize the sentences separating the particle from the mixed pronoun verb and return the sentence divided word by word
this process has a complexity of O(n * m) since the main variables are the length of the string and the amount of replacements that would take place
```python

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
```
I set up the test sentences
```python
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
```
For each sentence in sentences we'll tokenize it, check if any tokens have been generated, generate a tree with said tokens and print it.
```python
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
```
So the overall complexity of the grammar would be: </br>
O(n^3 * g) + O(n * m)

## Checking for Ambiguity and Left Side Recursion
Ambiguity: The ambiguity it's defined by a string that can be defined by 2 or more rules of the grammar, so this RCFG is clear of ambiguity

Left Side Recursion: The Left side recursion occurs when a symbol by example 'S' gives the option to reference itself, creating an infinite recursive loop of calling itself over and over and over. Luckily, there isn't any LSR in this code since each symbol is only used once and never references itself

## Tests
Some sentences that can be formed and are included as tests in my code are:
* I am drinking water regularly
* You are eating food regularly
* He/She is stretching the rope regularly
* We are lifting the stone
* They are killing fish
* They are learning python
* I drink water regularly
* you eat food regularly
* He/She stretch the rope regularly
* We lift the stone
* They kill fish
* They learn python

To run the code, you just need to write in your terminal python name_of_the_file

## Other ways to solve this
According to the AI ChatGPT from Open AI, another way of making this tree would be by using the following JS code:
```js
const grammar = {
    S: [['PP', 'DET']],
    DET: [['PMPV', 'MPV', 'V', 'N']],
    PMPV: [['AV'], ['P']],
    AV: ['táan'],
    P: ['k'],
    MPV: ['in', 'a', 'u', 'k'],
    PP: ['tene_', 'teche_', 'leti_e_', 'tone_', 'te_exe_', 'leti_obe_'],
    V: [['IV'], ['TV']],
    IV: ['ukic', 'hantic', 'haylic', 'naaczik', 'cimzik', 'canic'],
    TV: ['ukul', 'hanal', 'hayal', 'naacal', 'cimil', 'canal'],
    N: ['já', 'janal', 'summ', 'tunich', 'kay', 'python']
};

function tokenize(sentence) {
    return sentence.toLowerCase().split(' ');
}

function parse(tokens, grammar, startSymbol) {
    function helper(tokens, rule) {
        if (tokens.length === 0) return tokens.length === 0;
        if (grammar[rule]) {
            for (const production of grammar[rule]) {
                const remainingTokens = parseSequence(tokens, production);
                if (remainingTokens !== null) return remainingTokens;
            }
        } else if (tokens[0] === rule) {
            return tokens.slice(1);
        }
        return null;
    }

    function parseSequence(tokens, sequence) {
        let remainingTokens = tokens;
        for (const symbol of sequence) {
            remainingTokens = helper(remainingTokens, symbol);
            if (remainingTokens === null) return null;
        }
        return remainingTokens;
    }

    return helper(tokens, startSymbol) === [] ? 'Successfully parsed!' : 'Parsing failed.';
}

const sentences = [
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
];

for (const sentence of sentences) {
    const tokens = tokenize(sentence);
    console.log(`Parsing sentence: "${sentence}"`);
    console.log(parse(tokens, grammar, 'S'));
}

```
Where we tokenize and parse the sentences and has a complexity of O(n^2), however in this code we aren't printing any trees like on our original code, and JS is harder to understand than python

### Appendix
*Leti'obe' is the plural for he and she, or, as we would say in Spanish, 'ellos o ellas' <br />

[1] https://www.geeksforgeeks.org/what-is-context-free-grammar/ <br />
[2] https://www.researchgate.net/publication/221212174_On_Restricted_Context-Free_Grammars
