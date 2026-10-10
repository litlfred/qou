import json

with open("max_queue.json") as f:
    data = json.load(f)

batches = data["batches"][82:93]
print(f"Extracted {len(batches)} batches.")
for i, b in enumerate(batches):
    print(f"Batch index: {82+i}, Batch ID: {b.get('batch_id')}, Chapter: {b.get('chapter')}, Blocks: {len(b.get('blocks', []))}")

with open("my_batches.json", "w") as f:
    json.dump(batches, f, indent=2)
