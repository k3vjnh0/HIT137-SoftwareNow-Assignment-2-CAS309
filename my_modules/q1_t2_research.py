import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification


class TextProcessor:
    def __init__(self):
        # Load SpaCy models
        self.nlp_sci_sm = spacy.load("en_core_sci_sm")
        print("Loaded SpaCy model: en_core_sci_sm")

        self.nlp_ner_bc5cdr_md = spacy.load("en_ner_bc5cdr_md")
        print("Loaded SpaCy model: en_ner_bc5cdr_md")

        # Load BioBERT model and tokenizer from Hugging Face
        self.tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
        self.model = AutoModelForTokenClassification.from_pretrained(
            "dmis-lab/biobert-v1.1"
        )
        print("Loaded BioBERT model: dmis-lab/biobert-v1.1")

    def process_text_with_spacy(self, text):
        # Process the text using en_core_sci_sm
        doc_sci_sm = self.nlp_sci_sm(text)
        sci_sm_ents = [ent.text for ent in doc_sci_sm.ents]
        print(f"Processed text using en_core_sci_sm: {sci_sm_ents}")

        # Process the text using en_ner_bc5cdr_md
        doc_ner_bc5cdr_md = self.nlp_ner_bc5cdr_md(text)
        ner_bc5cdr_md_ents = [ent.text for ent in doc_ner_bc5cdr_md.ents]
        print(f"Processed text using en_ner_bc5cdr_md: {ner_bc5cdr_md_ents}")

        return sci_sm_ents, ner_bc5cdr_md_ents

    def tokenize_with_biobert(self, text):
        # Tokenize the text using BioBERT
        tokens = self.tokenizer(text)
        print(f"Tokens using BioBERT: {tokens}")
        return tokens
