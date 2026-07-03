import re
import os
import glob

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # The pattern matches:
    # <<<<<<< HEAD
    #     ]
    #   },
    #   "updated_at": "..."
    # =======
    #     ],
    
    # We want to replace it with:
    #     ],
    
    pattern1 = re.compile(r'<<<<<<< HEAD\n.*?=======\n(.*?)\n', re.DOTALL)
    # Actually simpler:
    # just remove everything from <<<<<<< HEAD to ======= inclusive, but wait, the HEAD block might contain the closing bracket we need to change to comma.
    # The ======= is followed by `    ],`. We can just delete from <<<<<<< HEAD up to and including =======\n.
    
    content = re.sub(r'<<<<<<< HEAD\n.*?=======\n', '', content, flags=re.DOTALL)
    
    # And remove the >>>>>>> line
    content = re.sub(r'>>>>>>> .*\n?', '', content)

    with open(filepath, 'w') as f:
        f.write(content)

for filepath in [
    "content/quantum-observable-universe/mass-theory/chi-lambda-w0-sign-weighting.qa.json",
    "content/quantum-observable-universe/mass-theory/chirality-writhe-ribbon-derivation.qa.json",
    "content/quantum-observable-universe/mass-theory/em-spectral-completeness.qa.json",
    "content/quantum-observable-universe/mass-theory/hoefsmit-V21-cos-symmetrization.qa.json",
    "content/quantum-observable-universe/mass-theory/markov-pair-z2.qa.json",
    "content/quantum-observable-universe/mass-theory/six-term-mass-formula-complete.qa.json",
    "content/quantum-observable-universe/mass-theory/three-calibration-inputs.qa.json"
]:
    fix_file(filepath)

print("Conflicts fixed.")
