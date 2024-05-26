# mayanGrammar
This is my hand in for:  Evidence 2 Generating and Cleaning a Restricted Context Free Grammar 
Were I'll deliver a RCFG (Restricted Context Free Grammar) which is a variation of a CFG and as explained in the webpage for Geeks for Geeks a CFG is a a type of formal grammar that has four tuples: (V,T,P,S). <br />
![alt text](https://github.com/elunacado/mayanGrammar/blob/main/rcfg.png)
so a RCFG follows the same rules as a CFG but witha added restrictions that simplify the parsing and reduce the ambiguity**

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

and  Regular present which describe actions that occur regularly, such as eating or sleeping, and for this tense, the rules are the next ones:

| Personal Pronoun      | Particle        | Mixed pronoun verbs | Verb                       | Noun |
|-----------------------|-----------------|---------------------|----------------------------|------|
| Tene'(I)              | k               | in                  |   Transitive               | Noun |
| Teche'(You)           | k               | a                   |   Intransitive             |      |
| Leti'e'(He/She)       | k               | u                   |                            |      |
| Tone' (We)            | k               | k                   |                            |      |
| Te'exe' (They)        | k               | a                   |                            |      | 
| Leti'obe'* (They)     | k               | u                   |                            |      |


## Verbs
For this hand-in i choosed the following verbs: <br />
Transitive Verbs -> 'ukic'|'hantic'|'haylic'|'naaczik'|'cimzik'|'canic' which means 'to drink'|'to eat'|'to stretch'|'to lift'|'to kill'|'to learn' <br />
Intransitive Verbs -> 'ukul'|'hanal'|'hayal'|'naacal'|'cimil'|'canal' which means 'drink'|'eat'|'stretch'|'lift'|'kill'|'learn' <br />

## Nouns
And my nouns for this hand-in are going to be: <br />
Já|janal|sumn|tunich|kay|python which means water|food|rope|stone|fish|python(the programming language) <br />

## Model

## Implementation

## Checking for ambiguity and Left Side Recursion

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

To run the code you just need to write in your terminal python name_of_the_file

### Appendix
*Leti'obe' is the plural for he and she or as we would say in spanish 'ellos o ellas' <br />
**Ambiguity: <br />
***Left Side Recursion: <br />

[1] https://www.geeksforgeeks.org/what-is-context-free-grammar/ <br />
[2] https://www.researchgate.net/publication/221212174_On_Restricted_Context-Free_Grammars
