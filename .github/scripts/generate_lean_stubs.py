"""
Generate Lean 4 Stub Files from proof-objects.json

Reads `proof-objects.json` and populates the Lean chapter files under
`lean/QOU/` with `sorry`-based stubs for every theorem-like object that
has a `lean.decl` field but no existing Lean declaration.

Usage:
    python .github/scripts/generate_lean_stubs.py [--manifest proof-objects.json]

The script is idempotent: it will not overwrite declarations that already
exist in the Lean files.  New stubs are appended within the chapter's
namespace block.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
LEAN_DIR = REPO_ROOT / "lean"
DEFAULT_MANIFEST = REPO_ROOT / "proof-objects.json"

# Map from chapter number to Lean file (relative to lean/)
CHAPTER_LEAN_FILES = {
    1: "QOU/QuantumObservableUniverse.lean",
    2: "QOU/Elaboration.lean",
    3: "QOU/PathIntegrals.lean",
    4: "QOU/Torsion.lean",
    5: "QOU/BringsSurface.lean",
    6: "QOU/DescartesUniverse.lean",
    7: "QOU/PAdicQuantumGroups.lean",
    8: "QOU/GaugeFieldFluidDynamics.lean",
    9: "QOU/InformationTheory.lean",
    # Chapters 10-12 are stubs with minimal mathematical content
}

# Map object_type to Lean keyword
LEAN_KEYWORDS = {
    "theorem": "theorem",
    "lemma": "lemma",
    "proposition": "theorem",  # Lean doesn't have proposition keyword
    "corollary": "theorem",
    "definition": "def",
    "conjecture": "theorem",  # conjectures become theorems with sorry
}


def label_to_lean_name(label):
    """Convert a LaTeX label like 'thm:lifting-exists' to a Lean name
    like 'lifting_exists'."""
    # Remove the prefix (thm:, def:, etc.)
    name = label.split(":", 1)[-1] if ":" in label else label
    # Replace hyphens with underscores
    name = name.replace("-", "_")
    # Remove characters invalid in Lean identifiers
    name = re.sub(r"[^a-zA-Z0-9_]", "", name)
    return name


def generate_stub(obj):
    """Generate a Lean stub declaration for a proof object."""
    label = obj["label"]
    obj_type = obj["object_type"]
    title = obj.get("title", "")
    lean_keyword = LEAN_KEYWORDS.get(obj_type, "theorem")

    # Use the lean decl name if specified, otherwise derive from label
    if "lean" in obj and "decl" in obj["lean"]:
        # Extract just the final component
        decl_name = obj["lean"]["decl"].rsplit(".", 1)[-1]
    else:
        decl_name = label_to_lean_name(label)

    latex_file = obj.get("latex", {}).get("file", "")
    latex_line = obj.get("latex", {}).get("line", "")

    lines = []
    lines.append(f"/-- {title or label}")
    lines.append(f"")
    lines.append(f"LaTeX: `{latex_file}:{latex_line}` (`\\label{{{label}}}`)")
    lines.append(f"-/")

    lines.append(f"{lean_keyword} {decl_name} : Sorry := sorry")

    lines.append("")
    return "\n".join(lines)


def get_existing_decls(filepath):
    """Read a Lean file and return the set of declaration names found."""
    decls = set()
    if not filepath.exists():
        return decls
    content = filepath.read_text(encoding="utf-8")
    # Match theorem/lemma/def declarations
    for m in re.finditer(r"(?:theorem|lemma|def)\s+(\w+)", content):
        decls.add(m.group(1))
    return decls


def main():
    parser = argparse.ArgumentParser(description="Generate Lean stubs from proof-objects.json.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="Path to proof-objects.json",
    )
    args = parser.parse_args()

    if not args.manifest.exists():
        print(f"❌ Manifest not found: {args.manifest}")
        print("Run extract_proof_objects.py first.")
        sys.exit(1)

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)

    # Group objects by chapter
    by_chapter = {}
    for obj in manifest.get("objects", []):
        chapter = obj.get("latex", {}).get("chapter")
        if chapter and chapter in CHAPTER_LEAN_FILES:
            by_chapter.setdefault(chapter, []).append(obj)

    total_new = 0
    for chapter_num, objects in sorted(by_chapter.items()):
        lean_file = LEAN_DIR / CHAPTER_LEAN_FILES[chapter_num]
        if not lean_file.exists():
            print(f"⚠️  Lean file missing: {lean_file}")
            continue

        existing = get_existing_decls(lean_file)
        stubs = []

        for obj in objects:
            obj_type = obj["object_type"]
            if obj_type not in LEAN_KEYWORDS:
                continue  # skip examples, remarks

            if "lean" in obj and "decl" in obj["lean"]:
                decl_name = obj["lean"]["decl"].rsplit(".", 1)[-1]
            else:
                decl_name = label_to_lean_name(obj["label"])

            if decl_name in existing:
                continue  # already declared

            stubs.append(generate_stub(obj))

        if not stubs:
            print(f"  Chapter {chapter_num}: no new stubs needed")
            continue

        # Insert stubs before the final `end` line
        content = lean_file.read_text(encoding="utf-8")
        # Find the last `end` line
        end_match = list(re.finditer(r"^end\s+", content, re.MULTILINE))
        if end_match:
            insert_pos = end_match[-1].start()
            new_content = (
                content[:insert_pos]
                + "\n".join(stubs)
                + "\n"
                + content[insert_pos:]
            )
        else:
            new_content = content + "\n" + "\n".join(stubs)

        lean_file.write_text(new_content, encoding="utf-8")
        print(f"  Chapter {chapter_num}: added {len(stubs)} stubs to {lean_file.name}")
        total_new += len(stubs)

    print(f"\n✅ Generated {total_new} new Lean stubs")


if __name__ == "__main__":
    main()
