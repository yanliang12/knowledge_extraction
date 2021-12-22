#######server_path.py#######
import re
import time
import logging
import argsparser
from flask import *
from flask_restplus import *

from yan_knowledge_extraction_to_neo4j import knowwledge_extraction_to_neo4j

ns = Namespace('knowledge_graph')
args = argsparser.prepare_args()

parser = ns.parser()
parser.add_argument('text', type=str, location='json')

#######Text2Own_KnowledgeGraph
req_fields2 = {\
	'text': fields.String(
	example = u"Yan Liang is a student at Liverpool John Moores University. She lives in Abu Dhabi. She is Qichu Wang's mother.")
	}
jessica_api_req2 = ns.model('yan', req_fields2)

rsp_fields2 = {\
	'status':fields.String,\
	'running_time':fields.Float\
	}
jessica_api_rsp2 = ns.model('output', rsp_fields2)

@ns.route('/knowledge_extraction')
class jessica_api_own(Resource):
	def __init__(self, *args, **kwargs):
		super(jessica_api_own, self).__init__(*args, **kwargs)
	@ns.marshal_with(jessica_api_rsp2)
	@ns.expect(jessica_api_req2)
	def post(self):		
		start = time.time()
		output = {}
		try:			
			args = parser.parse_args()	
			knowwledge_extraction_to_neo4j(args['text'])
			output['status'] = "success"
			output['running_time'] = float(time.time()- start)
			return output, 200
		except Exception as e:
			output = {}
			output['status'] = 'error:'+str(e)
			output['running_time'] = float(time.time()- start)
			return output

#######server_path.py#######