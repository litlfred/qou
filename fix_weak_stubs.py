import json

files = [
    'content/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.qa.json',
    'content/quantum-observable-universe/mass-theory/three-calibration-inputs.qa.json',
    'content/quantum-observable-universe/mass-theory/phi-q-tower-algebraic-stratification.qa.json',
    'content/quantum-observable-universe/mass-theory/s4-s3-half-symmetric-projection.qa.json',
    'content/quantum-observable-universe/particle-interactions/q-zero-stokes-region-identification.qa.json',
    'content/quantum-observable-universe/particle-interactions/nuclear-operator-regimes.qa.json'
]

for qa_path in files:
    with open(qa_path, "r") as f:
        qa = json.load(f)

    latest = sorted(qa["criteria"]["proof-narrative-lean-equiv"], key=lambda x: x["reviewed_at"])[-1]
    latest["result"] = "warn"
    latest["notes"] = "Class B: Lean stub detected (proper Lean signature created, but proof is sorry / Pattern C). False positive from heuristic script matched 'True := trivial' in comments."
    with open(qa_path, "w") as f:
        json.dump(qa, f, indent=2)

