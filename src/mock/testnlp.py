import json
import spacy
from medspacy.visualization import visualize_ent
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from scispacy.linking import EntityLinker
from spacy.language import Language
from functools import partial

def get_terms_and_cuis_from_config():
    terms = []
    cuis = []
    with open("config.json") as json_file:
        cases = json.load(json_file)
        for case_key in cases:
            if case_key == "abbreviations":
                continue
            for section_key in cases[case_key]:
                for rule_type in cases[case_key][section_key]:
                    for rule in cases[case_key][section_key][rule_type]:
                        if 'term' in rule:
                            terms.append(rule["term"])
                        if 'cuis' in rule:
                            cuis.extend(rule["cuis"])
    return terms, cuis


def create_custom_nlp(terms, cuis):
    nlp_base = spacy.load("en_core_sci_sm")
    matcher = PhraseMatcher(nlp_base.vocab, attr="LOWER")
    patterns = [nlp_base.make_doc(term) for term in terms]
    matcher.add("TERMS", patterns)

    nlp = spacy.load("en_core_sci_sm")

    @Language.component("custom_entity_recognizer")
    def custom_entity_recognizer(doc):
        matches = matcher(doc)
        spans = [Span(doc, start, end, label="CUSTOM_ENTITY") for match_id, start, end in matches]
        doc.ents = spans
        return doc

    nlp.add_pipe("custom_entity_recognizer", before="ner")

    @Language.component("filter_entities")
    def filter_entities(doc):
        filtered_ents = []
        for ent in doc.ents:
            if ent.label_ not in cuis:
                continue
            for umls_ent in ent._.kb_ents:
                if umls_ent[0] in cuis:
                    filtered_ents.append(ent)
                    break

        doc.ents = filtered_ents
        return doc

    nlp.add_pipe("filter_entities", after="ner")

    return nlp



terms, cuis = get_terms_and_cuis_from_config()
nlp_custom = create_custom_nlp(terms, cuis)



test_string_1 = """Myocardial infarction (MI), colloquially known as "heart attack,"
is caused by decreased or complete cessation of blood flow to a portion of the myocardium. 
Myocardial infarction may be "silent," and go undetected, or it could be a catastrophic event
leading to hemodynamic deterioration and sudden death. Most myocardial infarctions are due to 
underlying coronary artery disease, the leading cause of death in the United States. 
With coronary artery occlusion, the myocardium is deprived of oxygen. 
Prolonged deprivation of oxygen supply to the myocardium can lead to myocardial cell death and necrosis. 
Patients can present with chest discomfort or pressure that can radiate to the neck, 
jaw, shoulder, or arm. In addition to the history and physical exam, myocardial ischemia 
may be associated with ECG changes and elevated biochemical markers such as cardiac troponins. 
This activity describes the pathophysiology, evaluation, and management of myocardial infarction 
and highlights the role of the interprofessional team in improving care for affected patients. Hypertension"""

doc = nlp_custom(test_string_1)
htmlvs = visualize_ent(doc, jupyter=False)
print(htmlvs)
