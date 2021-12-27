#####yan_knowledge_extraction_to_neo4j.py#####
import re
from yan_neo4j import start_neo4j
from yan_neo4j import create_neo4j_session
from yan_neo4j import ingest_knowledge_triplets_to_neo4j

start_neo4j(http_port = "4567", bolt_port = "8765")
neo4j_session = create_neo4j_session(bolt_port = "8765")

from jessica_relation_extraction import relation_extraction

def knowwledge_extraction_to_neo4j(text):
	triplets = relation_extraction(text)
	###
	for t in triplets:
		t['subject_name'] = re.sub(r'[\'\"\.]+', r' ', t['subject_name'])
		t['object_name'] = re.sub(r'[\'\"\.]+', r' ', t['object_name'])
	###
	ingest_knowledge_triplets_to_neo4j(
		triplets, 
		neo4j_session)

#####yan_knowledge_extraction_to_neo4j.py#####
