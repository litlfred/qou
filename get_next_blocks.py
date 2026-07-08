import json

with open("todos/qa-agent-drain-queue.json", "r") as f:
    data = json.load(f)

all_blocks = []
for batch in data.get("batches", []):
    for block in batch.get("blocks", []):
        all_blocks.append(block["block"])

for i in range(360, 365):
    if i < len(all_blocks):
        print(f'{i}: {all_blocks[i]}')
