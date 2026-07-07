import os
import re

fixes = [
    ("categorical-dirac-operator.md", "categorical-dirac-operator", "categorical Dirac operator", True),
    ("categorical-action.md", "categorical-action", "categorical action", True),
    ("quantum-flatness.md", "quantum-flatness", "quantum flatness", True),
    ("descent-involution.md", "descent", "descent", False),
    ("per-nucleon-channel-decomposition.md", "per-nucleon-channel-decomposition", "per-nucleon channel decomposition", True),
    ("knot-particle-generation.md", "torus-knot-generators", "torus-knot generators", True),
    ("knot-particle-generation.md", "linking-operations", "linking operations", True),
    ("cemetery-group.md", "cemetery-group", "cemetery group", True),
    ("markov-axiom-recursive-ascent.md", "markov-axiom-recursive-ascent", "Markov axiom recursive ascent", True),
    ("delta-q-decoration.md", "delta-q-decoration", "$\Delta_q$-decoration", False),
    ("delta-q-decoration.md", "q-dimension-layer", "$q$-dimension layer", False),
    ("q-von-mangoldt-function.md", "q-von-mangoldt-function", "$q$-von Mangoldt function", False),
    ("q-chebyshev-function.md", "q-chebyshev-function", "$q$-Chebyshev function", False),
    ("local-q-zeta-function.md", "local-q-zeta-function", "local $q$-zeta function", False),
    ("glossary-no-quasi-zeros.md", "no-quasi-zeros", "no quasi-zeros", False),
    ("glossary-q-bit-skein.md", "q-bit-skein", "$q$-bit skein", False),
]

for root, _, files in os.walk('/Users/litlfred/space_cats/qou/content/quantum-observable-universe'):
    for file in files:
        for md_file, def_id, phrase, is_exact in fixes:
            if file == md_file:
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                
                # We need to find the definition. We can just do a regex replace.
                # Often it's bolded: **phrase**
                # Or just phrase. We want to replace the first occurrence or bolded occurrence.
                pattern = re.compile(rf"\*\*({re.escape(phrase)})\*\*", re.IGNORECASE)
                if pattern.search(content):
                    content = pattern.sub(rf"**:defterm[\1]{{#{def_id}}}**", content, count=1)
                else:
                    # If not bolded, find first occurrence of phrase and replace it
                    pattern2 = re.compile(rf"\b({re.escape(phrase)})\b", re.IGNORECASE)
                    if pattern2.search(content):
                        content = pattern2.sub(rf":defterm[\1]{{#{def_id}}}", content, count=1)
                    else:
                        print(f"Could not find {phrase} in {md_file}")
                        
                with open(path, 'w') as f:
                    f.write(content)

