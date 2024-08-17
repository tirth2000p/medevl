# %%


from medspacy.visualization import visualize_ent
from spacy import displacy
import spacy
import json
import os
import re
from spacy.tokens import Span

from scispacy.linking import EntityLinker
from scispacy.abbreviation import AbbreviationDetector

# %%
# setting up nlp pipeline
# nlp = medspacy.load()
nlp = spacy.load("en_core_sci_sm")
nlp.add_pipe("abbreviation_detector")
nlp.add_pipe("scispacy_linker", config={"resolve_abbreviations": True, "linker_name": "umls"})




# %%
# call to set the case of the file, which will fill cuis list with relevant information
def set_case(case, section):
    """
The set_case function takes two arguments:
    case - the name of the case to be used for testing.
    section - the section of that case to be tested.

:param case: Determine which case to use
:param section: Determine which section of the config
:return: A tuple of two lists
:doc-author: Trelent
"""
    with open("config.json") as json_file:
        cases = json.load(json_file)
    rules_fail = cases[case.lower()][section.lower()]["fail"]
    rules_review = cases[case.lower()][section.lower()]["review"]
    return (rules_fail, rules_review)

# %%
# search by cuis
def cui_search(nlp_doc, rule):
    """
The cui_search function takes in a spaCy NLP document and a rule dictionary.
The function then searches the NLP document for entities that match the CUI(s)
specified in the rule dictionary. If an entity is found, it returns True and
the name of the term being searched for. If no entity is found, it returns False
and the name of the term being searched for.

:param nlp_doc: Pass the doc object from spacy to the function
:param rule: Pass in the rule that is being used to search for a term
:return: A list of two items
:doc-author: Trelent
"""
    term_name = rule["name"]
    search_cuis = rule["cuis"]
    matched_entities = []
    for entity in nlp_doc.ents:
        for umls_ent in entity._.kb_ents:
            for cui in search_cuis:
                if umls_ent[0] == cui[0]:
                    matched_entities.append(entity)
                    continue
                else:
                    return [False, term_name]

    return [True, term_name]


# %%
# search by term using regex
def term_search(text, nlp_doc, rule):
    """
The term_search function takes a text string, an nlp_doc object, and a rule dictionary as input.
It returns the term name (from the rule dictionary) if it finds any matches in the text string.
If no matches are found, it returns False.

:param text: Pass the text of a document to the function
:param nlp_doc: Create the matched_span object
:param rule: Pass the name and term of each rule to the function
:return: A list containing the following:
:doc-author: Trelent
"""
    term_name = rule["name"]
    search_term = rule["term"]
    matched_terms = []  # Add this line
    for match in re.finditer(search_term, text, re.IGNORECASE):
        start, end = match.span()
        matched_span = nlp_doc.char_span(start, end)
        if matched_span is not None:
            matched_terms.append(matched_span)  # Add this line
    if matched_terms:  # Modify this line
        return [True, term_name, matched_terms]
    else:
        return [False, term_name, matched_terms]


# Span.set_extension("is_highlighted", default=False, force=True)
# %%
def check(case, section, text):
    """
The check function takes in a case, section, and text.
It then expands abbreviations in the text using abbreviation_expansion.
It sets the rules for that case and section using set_case.
The function then parses the text into tokens with nlp(text).
The pass conditions are initialized as an empty list to be filled later on.  The matched terms are also initialized as an empty list to be filled later on (this is used for highlighting).

:param case: Determine which rules to use
:param section: Determine which rules to use
:param text: Pass the text to be checked
:return: A tuple of (true/false, [list of missing terms], &quot;pass&quot;/&quot;review&quot;)
:doc-author: Trelent
"""
    text = abbreviation_expansion(text)
    rules_fail, rules_review = set_case(case, section)
    doc = nlp(text)
    pass_conditions = []
    matched_terms = []

    for rule in rules_fail:
        if 'cuis' in rule:
            flag = cui_search(doc, rule)
            if flag[0] == False:
                flag.append("Fail")
                pass_conditions.append(flag[:-1])
                htmlvs = highlight_terms(doc, matched_terms)  # Move this line here
                return False, pass_conditions[0][1], "Fail", htmlvs
            else:
                flag.append("Review")
                pass_conditions.append(flag[:-1])
                matched_terms.extend(flag[2])  # Add this line

        if 'term' in rule:
            flag = term_search(text, doc, rule)
            if flag[0] == False:
                flag.append("Fail")
                pass_conditions.append(flag[:-1])
                htmlvs = highlight_terms(doc, matched_terms)  # Move this line here
                return False, pass_conditions[0][1], "Fail", htmlvs
            else:
                flag.append("Review")
                pass_conditions.append(flag[:-1])
                matched_terms.extend(flag[2])  # Add this line

    for rule in rules_review:
        if 'cuis' in rule:
            flag = cui_search(doc, rule)
            if flag[0] == True:
                flag.append("Pass")
            else:
                flag.append("Review")
            pass_conditions.append(flag[:-1])
            matched_terms.extend(flag[2])  # Add this line

        if 'term' in rule:
            flag = term_search(text, doc, rule)
            if flag[0] == True:
                flag.append("Pass")
            else:
                flag.append("Review")
            pass_conditions.append(flag[:-1])
            matched_terms.extend(flag[2])  # Add this line

    htmlvs = highlight_terms(doc, matched_terms)  # Move this line to after the matched_terms have been updated

    if all(flag == True for (flag, _, _,) in pass_conditions):
        return True, ["All terms found"], "Pass", htmlvs
    else:
        missing = []
        for term in pass_conditions:
            if term[0] == False:
                missing.append(term)
        return False, missing[0][1], "Review", htmlvs


# %%
# def highlight_terms(doc, matched_terms):
#     for term in matched_terms:
#         for span in term:
#             span.ent_type_ = "HIGHLIGHTED"
#     html = displacy.render(doc, style="ent", jupyter=False, options={"ents": ["HIGHLIGHTED"], "colors": {"HIGHLIGHTED": "teal"}})
#     return html

def highlight_terms(doc, matched_terms):
    """
The highlight_terms function takes a spaCy Doc object and a list of matched terms,
and returns an HTML string with the matched terms highlighted.


:param doc: Pass in the document that we want to highlight
:param matched_terms: Pass in the list of matched terms
:return: An html string that can be rendered in a jupyter notebook
:doc-author: Trelent
"""
    unique_labels = {}
    color_mapping = {}
    for idx, term in enumerate(matched_terms):
        label = f"{str(term).upper()}"
        unique_labels[label] = term
        color_mapping[label] = f"hsl({idx * 60 % 360}, 100%, 50%)"
        for span in term:
            span.ent_type_ = label
    html = displacy.render(doc, style="ent", jupyter=False,
                           options={"ents": list(unique_labels.keys()), "colors": color_mapping})
    print(html)
    return html


# %%
def abbreviation_expansion(text):
    """
The abbreviation_expansion function takes a string as input and returns the same string with abbreviations expanded.
The function uses a JSON file to store the abbreviations and their expansions. The JSON file is read in, then each
abbreviation is searched for in the text using regex, and replaced with its expansion.

:param text: Pass in the text that will be searched for abbreviations
:return: The text with the abbreviations expanded
:doc-author: Trelent
"""
    new_text = text
    with open("config.json") as json_file:
        abbr = json.load(json_file)
    for abbreviation in abbr["abbreviations"]:
        new_text = re.sub(abbreviation["term"], abbreviation["replace"], text, flags=re.IGNORECASE)
    return new_text


# %%


# %%
# print(abbreviation_expansion(test_string_4))


# %%
