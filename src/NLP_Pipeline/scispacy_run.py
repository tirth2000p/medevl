try:
    import scispacy
except:
    pass
import spacy
import json

# from negspacy.negation import Negex
try:
    from scispacy.linking import EntityLinker
except:
    pass


text = """
  Myocardial Infarction is when the heart doesn't get enough oxygen.
  """



# pulls file locations from json file
with open("cuis.json") as json_file:
    data = json.load(json_file)
    cases = data["cases"]

# setting up nlp pipeline
nlp = spacy.load("en_core_sci_sm")
nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": "umls"})

# example text

doc = nlp(text)

# contains list of cui and name pairing
search_cuis = []

# call to set the case of the file, which will fill cuis list with relevant information
def set_case(case):
    with open(cases[case]) as f:
        file_lines = f.readlines()
    for entry in file_lines:
        line = entry.rstrip().split(",")
        search_cuis.append(line)

def check(text):
    print(list(doc.sents))
    print(doc.ents)
    linker = nlp.get_pipe("scispacy_linker")
    for entity in doc.ents:
        for umls_ent in entity._.kb_ents:
            for cui in search_cuis:
                if umls_ent[0] == cui[0]:
                    return True
    return False

set_case("cage")
print(check(text))

