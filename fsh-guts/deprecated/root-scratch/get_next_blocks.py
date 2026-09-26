import sys
import json

if len(sys.argv) < 2:
    print("Usage: python3 get_next_blocks.py <start_index>")
    sys.exit(1)

start = int(sys.argv[1])
count = 5

with open("todos/qa-agent-drain-queue.json", "r") as f:
    data = json.load(f)

all_blocks = []
for batch in data.get("batches", []):
    for block in batch.get("blocks", []):
        all_blocks.append(block["block"])

for i in range(start, start + count):
    if i < len(all_blocks):
        print(f'{i}: {all_blocks[i]}')
