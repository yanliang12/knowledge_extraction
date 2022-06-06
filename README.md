# Knowledge Extraction Engine

## start the service

```bash
docker pull yanliang12/yan_knowledge_extraction:1.0.2

docker run -it ^
-p 4567:4567 ^
-p 8765:8765 ^
-p 7563:9000 ^
yanliang12/yan_knowledge_extraction:1.0.2
```

## input the text
input rest api: http://0.0.0.0:7563/

input example:

```python
{
"text": "Yan Liang is a student at Liverpool John Moores University. She lives in Abu Dhabi. She is Qichu Wang's mother."
}
```

<img src="input.png" width="800">


## see the output

outout neo4j: http://0.0.0.0:4567/browser/

password: neo4j1

input one line cypher code
```bash
MATCH p=()-->() RETURN p LIMIT 100
```

<img src="output.png" width="500">


## contact

I can transform your documents to knowledge graph, please contact me to show you the demo and start to build your own knowledge graph

Email: jimjywang@gmail.com
