import json

with open("lake-manifest.json", "r") as f:
    manifest = json.load(f)

for pkg in manifest.get("packages", []):
    if pkg.get("name") == "plausible":
        pkg["dir"] = ""
    # DO NOT touch mathlib or others, just see if plausible fix is enough

with open("lake-manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
