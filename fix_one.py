import json

ts_path = "content/quantum-observable-universe/molecular-construction/electron-shell-2n2-capacity.ts"
with open(ts_path, "r") as f:
    ts = f.read()
if "lean: {" not in ts:
    ts = ts.replace("content: {", "lean: {\n    ref: \"qou:QOU.Molecular.ElectronShellCapacity.electron_shell_capacity_2n2\"\n  },\n  content: {")
    with open(ts_path, "w") as f:
        f.write(ts)

qa_path = "content/quantum-observable-universe/molecular-construction/electron-shell-2n2-capacity.qa.json"
with open(qa_path, "r") as f:
    qa = json.load(f)

if "paths" not in qa:
    qa["paths"] = {}
qa["paths"]["lean"] = "../qou/content/quantum-observable-universe/lean/QOU/Molecular/ElectronShellCapacity.lean"

latest = sorted(qa["criteria"]["proof-narrative-lean-equiv"], key=lambda x: x["reviewed_at"])[-1]
latest["result"] = "warn"
latest["notes"] = "Class B: Lean stub detected (proper Lean signature created, but proof is sorry)."
with open(qa_path, "w") as f:
    json.dump(qa, f, indent=2)

