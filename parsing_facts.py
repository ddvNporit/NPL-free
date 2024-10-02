import spacy
import textacy.extract

# Загрузка английской NLP-модели
nlp = spacy.load('en_core_web_lg')
entity = "London"
# Текст для анализа
text = """London is the capital and most populous city of England and  the United Kingdom.  
Standing on the River Thames in the south east of the island of Great Britain, 
London has been a major settlement  for two millennia.  It was founded by the Romans, 
who named it Londinium.
"""

# Анализ
doc = nlp(text)
uniqueStatements = list()
# Извлечение полуструктурированных выражений со словом London
for cue in ["is", "be", "have", "write", "talk", "talk about"]:
    statements = textacy.extract.semistructured_statements(doclike=doc, entity=entity, cue=cue,
                                                           fragment_len_range=None)
    # Вывод результатов
    print("found", len(uniqueStatements), "statements.")
    for statement in statements:
        uniqueStatements.append(statement)

for statement in uniqueStatements:
    subject, verb, fact = statement
    # print(f" - {fact}")
    # format_fact = ''.join(fact)
    print("* entity:", entity, ", cue:", cue, ", fact:", fact)