import json

with open("qa-agent-drain-queue.json", "r") as f:
    data = json.load(f)

for idx, b in enumerate(data["batches"]):
    if 71 <= idx <= 81:
        print(f"Index {idx}: Batch id {b['batch_id']}, chapter={b['chapter']}, blocks={len(b['blocks'])}")
