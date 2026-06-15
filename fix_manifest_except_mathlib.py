import json

with open("lake-manifest.json", "r") as f:
    manifest = json.load(f)

for pkg in manifest.get("packages", []):
    if pkg.get("type") == "git" and pkg.get("name") != "mathlib":
        if "dir" not in pkg:
            pkg["dir"] = ""

with open("lake-manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
