import json

with open('todos/research-queue.json', 'r') as f:
    queue = json.load(f)

for item in queue:
    if item['id'] == 'research-boiling-freezing-temps-from-braid-hbond':
        item['status'] = 'done'
        item['completedAt'] = '2026-06-13'
        item['verdict'] = 'Strict no-fit Q-EOS scanning misses experimental temperatures by ~6.4x. Tier: open.'
    elif item['id'] == 'research-multi-nucleon-interface-operator':
        item['status'] = 'done'
        item['completedAt'] = '2026-06-13'
        item['verdict'] = 'H_3^4 tensor fusion generates exactly the 2-row trace dominance and unique (4,4,4) PSD block, but rho_F approx 1.8891 cannot be naively extracted without fit-trap. Tier: open.'
    elif item['id'] == 'triage-alpha-em-4pi-sibling-family':
        item['status'] = 'done'
        item['completedAt'] = '2026-06-13'
        item['completedBy'] = 'Agent'
        item['verdict'] = 'Triaged 12 open PRs. Merged canonical walkthrough (#1505) and ledger (#1495) into main. Confirmed the main canonical branch is alpha-em-habiro-bar-involution. The remaining open PRs (e.g. Phase 1-4 Schwinger RT) are the stalled 57ppb piece and remain open research. Refuted PRs are noted for closure.'

with open('todos/research-queue.json', 'w') as f:
    json.dump(queue, f, indent=2)

