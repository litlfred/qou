import os

files_to_print = [
    "quantum-flatness.md",
    "knot-particle-generation.md",
    "markov-axiom-recursive-ascent.md",
    "delta-q-decoration.md",
    "glossary-q-bit-skein.md"
]

for root, _, files in os.walk('/Users/litlfred/space_cats/qou/content/quantum-observable-universe'):
    for file in files:
        if file in files_to_print:
            path = os.path.join(root, file)
            print(f"--- {file} ---")
            with open(path, 'r') as f:
                print(f.read())
