# Indexify Demo Project

### Requirements
```
pip install -U indexify-extractor-sdk indexify indexify-langchain
```

### Start Indexify Server - Terminal 1
```
curl https://www.tensorlake.ai | sh
./indexify server -d
```

### Download & Join Extractors to Server
| Terminal 2                                                                                                                                   | Terminal 3                                                                                                                              | Terminal 4                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ```<br>indexify-extractor download hub://pdf/pdf-extractor<br>indexify-extractor join-server pdf-extractor.pdf_extractor:PDFExtractor<br>``` | ```<br>indexify-extractor download hub://text/chunking<br>indexify-extractor join-server chunking.chunk_extractor:ChunkExtractor<br>``` | ```<br>indexify-extractor download hub://embedding/arctic<br>indexify-extractor join-server arctic.arctic:ArcticExtractor<br>``` |
|                                                                                                                                              |                                                                                                                                         |                                                                                                                                  |
|                                                                                                                                              |                                                                                                                                         |                                                                                                                                  |
|                                                                                                                                              |                                                                                                                                         |                                                                                                                                  |

### Upload Files to Server - Terminal 5
```
python test_upload.py
```

### Perform RAG from Files - Terminal 6
```
python test_rag.py
```