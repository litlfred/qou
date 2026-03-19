"""
Extract Proof Objects from LaTeX Source

Parses all chapter .tex files for theorem-like environments (theorem, lemma,
proposition, corollary, definition, example, remark, conjecture) and their
labels.  Outputs or updates `proof-objects.json` in the repository root.

Usage:
    python .github/scripts/extract_proof_objects.py [--output proof-objects.json]

The script preserves existing review records and Lean linkage data when
updating — it only adds new objects and removes objects whose labels no
longer exist in the LaTeX source.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CHAPTERS_DIR = REPO_ROOT / "chapters"
SCHEMA_PATH = REPO_ROOT / "schemas" / "proof-objects.schema.json"
DEFAULT_OUTPUT = REPO_ROOT / "proof-objects.json"

# Map from LaTeX environment name to object_type in the schema.
ENV_TYPES = {
    "theorem": "theorem",
    "lemma": "lemma",
    "proposition": "proposition",
    "corollary": "corollary",
    "definition": "definition",
    "example": "example",
    "remark": "remark",
    "conjecture": "conjecture",
}

# Chapter file order (matches main.tex \input order).
CHAPTER_FILES = [
    "quantum-observable-universe.tex",
    "qou-elaboration.tex",
    "path-integrals-and-braiding.tex",
    "lifting-of-quantum-torsion.tex",
    "brings-surface.tex",
    "descartes-universe.tex",
    "p-adic-quantum-groups.tex",
    "gauge-field-fluid-dynamics.tex",
    "information-theory.tex",
    "interpretations.tex",
    "experimental-evidence.tex",
    "speculations.tex",
]

# Map chapter number to Lean file (for populating lean.file, lean.gh_pages_url, etc.)
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
}

GITHUB_REPO = "litlfred/qou"
GH_PAGES_BASE = "https://litlfred.github.io/qou"

# Regex patterns
# Matches \begin{theorem}, \begin{lemma}[title], etc.
BEGIN_RE = re.compile(
    r"\\begin\{("
    + "|".join(ENV_TYPES.keys())
    + r")\}(?:\[([^\]]*)\])?"
)
# Matches \label{...}
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
# Matches \lean{...}
LEAN_RE = re.compile(r"\\lean\{([^}]+)\}")
# Matches \uses{...}
USES_RE = re.compile(r"\\uses\{([^}]+)\}")
# Matches \leanok
LEANOK_RE = re.compile(r"\\leanok\b")

# Maximum lines to scan within a LaTeX environment body.
MAX_ENV_SCAN_LINES = 50

# Keys to preserve when merging Lean linkage data from existing records.
LEAN_MERGE_KEYS = ("url", "file", "sorry_free", "mathlib_links")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_commit_sha():
    """Return the current HEAD commit SHA."""
    try:
        return (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def parse_chapter(filepath, chapter_num):
    """Parse a single .tex file and return a list of proof objects."""
    objects = []
    rel_path = str(filepath.relative_to(REPO_ROOT))

    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i]
        m = BEGIN_RE.search(line)
        if not m:
            i += 1
            continue

        env_name = m.group(1)
        title = m.group(2)  # may be None
        begin_line = i + 1  # 1-indexed

        # Scan the environment body for \label, \lean, \uses, \leanok
        label = None
        lean_decl = None
        uses = []
        leanok = False
        j = i + 1
        # Look within the next 20 lines (or until \end{env})
        end_re = re.compile(r"\\end\{" + re.escape(env_name) + r"\}")
        while j < min(i + MAX_ENV_SCAN_LINES, len(lines)):
            body_line = lines[j]
            if end_re.search(body_line):
                break

            lm = LABEL_RE.search(body_line)
            if lm and label is None:
                label = lm.group(1)

            lean_m = LEAN_RE.search(body_line)
            if lean_m:
                lean_decl = lean_m.group(1).strip()

            uses_m = USES_RE.search(body_line)
            if uses_m:
                uses = [u.strip() for u in uses_m.group(1).split(",")]

            if LEANOK_RE.search(body_line):
                leanok = True

            j += 1

        if label:
            obj = {
                "label": label,
                "object_type": ENV_TYPES[env_name],
                "latex": {
                    "file": rel_path,
                    "line": begin_line,
                    "chapter": chapter_num,
                },
            }
            if title:
                obj["title"] = title.strip()
            if lean_decl:
                lean_ref = {"decl": lean_decl}
                # Populate file path and URLs if chapter has a Lean file
                if chapter_num in CHAPTER_LEAN_FILES:
                    lean_file = CHAPTER_LEAN_FILES[chapter_num]
                    lean_ref["file"] = lean_file
                    lean_ref["gh_pages_url"] = f"{GH_PAGES_BASE}/lean/{lean_file}"
                    commit = get_commit_sha()
                    lean_ref["github_source_url"] = (
                        f"https://github.com/{GITHUB_REPO}/blob/{commit}/lean/{lean_file}"
                    )
                    lean_ref["last_edited_commit"] = commit
                obj["lean"] = lean_ref
                if leanok:
                    obj["formalization_status"] = "proved"
                else:
                    obj["formalization_status"] = "stated"
            else:
                obj["formalization_status"] = "not_started"
            if uses:
                obj["uses"] = uses

            objects.append(obj)

        i = j + 1 if j > i else i + 1

    return objects


def merge_with_existing(new_objects, existing_path):
    """Merge newly extracted objects with existing proof-objects.json.

    Preserves review records and Lean linkage data for objects that still
    exist.  Removes objects whose labels are no longer in the LaTeX source.
    """
    if not existing_path.exists():
        return new_objects

    with open(existing_path, encoding="utf-8") as f:
        existing = json.load(f)

    existing_by_label = {obj["label"]: obj for obj in existing.get("objects", [])}
    merged = []

    for new_obj in new_objects:
        label = new_obj["label"]
        if label in existing_by_label:
            old = existing_by_label[label]
            # Preserve reviews
            if "reviews" in old:
                new_obj["reviews"] = old["reviews"]
            # Preserve Lean linkage if not overridden by LaTeX macro
            if "lean" not in new_obj and "lean" in old:
                new_obj["lean"] = old["lean"]
                new_obj["formalization_status"] = old.get(
                    "formalization_status", "not_started"
                )
            elif "lean" in new_obj and "lean" in old:
                # Merge: keep fields from old that new doesn't have
                for key in LEAN_MERGE_KEYS:
                    if key in old["lean"] and key not in new_obj["lean"]:
                        new_obj["lean"][key] = old["lean"][key]
        merged.append(new_obj)

    return merged


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Extract proof objects from LaTeX.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output path for proof-objects.json",
    )
    args = parser.parse_args()

    all_objects = []
    for chapter_num, filename in enumerate(CHAPTER_FILES, start=1):
        filepath = CHAPTERS_DIR / filename
        if not filepath.exists():
            print(f"⚠️  Skipping missing chapter: {filepath}")
            continue
        objects = parse_chapter(filepath, chapter_num)
        print(f"  Chapter {chapter_num:2d} ({filename}): {len(objects)} objects")
        all_objects.extend(objects)

    print(f"\nTotal objects extracted: {len(all_objects)}")

    # Merge with existing data
    all_objects = merge_with_existing(all_objects, args.output)

    # Build dependency edges from uses
    dependencies = []
    for obj in all_objects:
        if "uses" in obj:
            for dep_label in obj["uses"]:
                dependencies.append(
                    {"from": obj["label"], "to": dep_label, "relation": "uses"}
                )

    # Build manifest
    manifest = {
        "version": "1.0",
        "manuscript": {
            "repo": "litlfred/qou",
            "commit_sha": get_commit_sha(),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "pdf_url": "https://litlfred.github.io/qou/quantum-observable-universe.pdf",
            "lean_docs_url": "https://litlfred.github.io/qou/lean/",
        },
        "objects": all_objects,
        "dependencies": dependencies,
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Wrote {args.output}")


if __name__ == "__main__":
    main()
