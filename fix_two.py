import json

files = [
    (
        "content/quantum-observable-universe/information-theory/dispersion-suppression-scale",
        "qou:QOU.Information.DispersionSuppressionScale.dispersion_suppression_scale",
        "../qou/content/quantum-observable-universe/lean/QOU/Information/DispersionSuppressionScale.lean"
    ),
    (
        "content/quantum-observable-universe/quantum-observable-universes/archimedean-realisation-volume-compatibility",
        "qou:QOU.Archimedean.RealisationVolumeCompatibility.realisation_volume_compatibility",
        "../qou/content/quantum-observable-universe/lean/QOU/Archimedean/RealisationVolumeCompatibility.lean"
    )
]

for base, lean_ref, lean_path in files:
    ts_path = base + ".ts"
    with open(ts_path, "r") as f:
        ts = f.read()
    if "lean: {" not in ts:
        ts = ts.replace("tags: [", f"lean: {{\n    ref: \"{lean_ref}\"\n  }},\n  tags: [")
        with open(ts_path, "w") as f:
            f.write(ts)

    qa_path = base + ".qa.json"
    with open(qa_path, "r") as f:
        qa = json.load(f)

    if "paths" not in qa:
        qa["paths"] = {}
    qa["paths"]["lean"] = lean_path

    latest = sorted(qa["criteria"]["proof-narrative-lean-equiv"], key=lambda x: x["reviewed_at"])[-1]
    latest["result"] = "warn"
    latest["notes"] = "Class B: Lean stub detected (proper Lean signature created, but proof is sorry)."
    with open(qa_path, "w") as f:
        json.dump(qa, f, indent=2)

