import os

files_to_fix = {
    "content/quantum-observable-universe/quantum-observable-universes/quantum-flatness.md": [
        ("**quantum flat**", "**:defterm[quantum flat]{#quantum-flatness}**")
    ],
    "content/quantum-observable-universe/mass-theory/markov-axiom-recursive-ascent.md": [
        ("(:defterm[Markov-axiom recursive ascent]{#markov-axiom-recursive-ascent})", ":defterm[Markov-axiom recursive ascent]{#markov-axiom-recursive-ascent}")
    ],
    "content/quantum-observable-universe/mass-theory/delta-q-decoration.md": [
        (":defterm[q-dimension decoration]{#delta-q-decoration}", ":defterm[delta-q-decoration]"),
        (":defterm[layer]{#q-dimension-layer}", ":defterm[q-dimension-layer]")
    ],
    "content/quantum-observable-universe/particle-interactions/knot-particle-generation.md": [
        (":defterm[torus knot generators]{#torus-knot-generators}", ":defterm[torus-knot-generators]")
    ],
    "content/quantum-observable-universe/glossary/glossary-q-bit-skein.md": [
        ("One $q$-bit $=$ one crossing resolution", ":defterm[q-bit-skein]\n\nOne $q$-bit $=$ one crossing resolution")
    ]
}

for filepath, replacements in files_to_fix.items():
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        for old, new in replacements:
            content = content.replace(old, new)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed {filepath}")
    else:
        print(f"Missing {filepath}")
