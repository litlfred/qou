import json, sys, os

blocks = [
    "categorical-q-connection-exists",
    "categorical-self-duality",
    "emergence-to-quantum-flat",
    "fai-projector-coadjoint-orbit",
    "categorical-lichnerowicz",
    "fibre-functor-atlas",
    "cs-evaluation-faithfulness",
    "hadron-q-self-correction",
    "gauge-coupling-uniqueness",
    "knot-operator-selection",
    "metallic-character-knot",
    "noble-gas-characterization"
]

for b in blocks:
    cmd = os.popen(f'find . -name "{b}.md"')
    files = cmd.read().strip().split('\n')
    for f in files:
        if not f: continue
        print(f)
