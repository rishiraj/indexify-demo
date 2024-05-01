import os
import time
from indexify import IndexifyClient

client = IndexifyClient()

client.add_extraction_policy(extractor='tensorlake/pdf-extractor', name="datas")
client.add_extraction_policy(extractor='tensorlake/chunk-extractor', name="chunks", content_source="datas", input_params={"chunk_size": 512, "overlap": 150})
client.add_extraction_policy(extractor='tensorlake/arctic', name="info", content_source="chunks")

def monitor_directory(path):
    known_files = set()

    while True:
        files = set(os.listdir(path))
        new_files = files - known_files

        for filename in new_files:
            if filename.endswith(".pdf"):
                file_path = os.path.join(path, filename)
                print(f"New PDF file detected: {file_path}")
                client.upload_file(path=file_path)

        known_files = files
        time.sleep(1)

if __name__ == "__main__":
    path = "/Users/rishiraj/tensorlakeai/experiments/demo/docs"  # Replace with the directory you want to monitor
    monitor_directory(path)