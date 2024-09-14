import spacy
from transformers import AutoModelForTokenClassification, AutoTokenizer

# TASK 2: Process text using SpaCy and BioBERT
# Load SpaCy models
nlp_sci_sm = spacy.load("en_core_sci_sm")
print("Loaded SpaCy model: en_core_sci_sm")

nlp_ner_bc5cdr_md = spacy.load("en_ner_bc5cdr_md")
print("Loaded SpaCy model: en_ner_bc5cdr_md")

# Load BioBERT model from Hugging Face Transformers
tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-v1.1")
print("Loaded BioBERT model: dmis-lab/biobert-v1.1")

# Example text
sample_text = "Aspirin is a medication used to reduce pain, fever, or inflammation."

# Process the text using the SpaCy models
doc = nlp_sci_sm(sample_text)
print(f"Processed text using en_core_sci_sm: {[ent.text for ent in doc.ents]}")

doc = nlp_ner_bc5cdr_md(sample_text)
print(f"Processed text using en_ner_bc5cdr_md: {[ent.text for ent in doc.ents]}")

# Tokenize the text using BioBERT
tokens = tokenizer(sample_text)
print(f"Tokens using BioBERT: {tokens}")
