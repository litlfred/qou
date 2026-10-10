import json

with open("lake-manifest.json", "r") as f:
    manifest = json.load(f)

for pkg in manifest.get("packages", []):
    if "subDir" in pkg and pkg["subDir"] is None:
        pkg["subDir"] = ""
    if pkg.get("type") == "git" and "dir" not in pkg:
        pkg["dir"] = ""

with open("lake-manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
