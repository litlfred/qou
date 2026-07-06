#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
P2.5 metadata-pass tool.

⚠ NOT auto-run in CI. Tested 2026-05-02: a full pass over all
180 eligible witness JSONs adds the `p2_5_compliance` annotation
cleanly, but also introduces ~880 lines of trailing-comma
formatting churn (because adding a field after the previous
last-field forces `}` → `,`). The CI drift filter doesn't catch
those formatting-only lines, so the pass triggers a "substantive
drift" CI failure even though the actual content is metadata-only.

This tool is left in the repo for **future use** when:
- Either the CI drift filter is upgraded to be JSON-aware
  (ignoring trailing-comma changes), or
- A coordinated witness-regeneration pass refreshes all 180
  witnesses to their current canonical form (which would absorb
  the formatting churn into a single planned commit).

Until either of those, run only as `--dry-run` to inspect what
the pass would do.

Adds a uniform `p2_5_compliance` annotation block to every Python
script's witness JSON output that the audit triages as
`partial`, `early-substitution`, or `mpmath-only`. The annotation
declares the script's symbolic-q discipline status:

  - **compliant** (already): nothing to add.
  - **mpmath-only**: declares q-handling style (canonical Q_MP);
    no separate fit; algebraic structure preserved internally.
  - **partial**: declares that the script uses sympy.Symbol('q')
    internally; substitutes q_0 only at reporting; if the witness
    JSON doesn't already expose a `*_polynomial_q` field, this
    annotation provides a `compliance_note` explaining why.
  - **early-substitution**: declares that the script substitutes
    q_0 to a float at script start (legacy pattern); flags as a
    refactor target with a pointer to the audit doc.

The annotation lives in a single `p2_5_compliance` sub-object at
the top level of the witness JSON; it does NOT change any
numerical content. The pass is **idempotent**: re-running adds the
annotation if missing, updates the audit-version stamp if present.

Usage:
    python3 computations/p2_5_metadata_pass.py [--dry-run]

Refs:
  docs/audits/2026-05-02-p2-5-symbolic-q-audit.md
  docs/audits/2026-05-01-math-framework-workplan.md P2.5
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
COMPUTE = REPO / "folio-assistant" / "computations"
AUDIT_WITNESS = COMPUTE / "p2-5-symbolic-q-audit.witness.json"

ANNOTATION_VERSION = "2026-05-02"

NOTES = {
    "compliant": (
        "P2.5: this script's parent .py uses sympy.Symbol('q') "
        "throughout and substitutes q_0 only at reporting. The "
        "witness JSON already exposes the algebraic-side polynomial "
        "form via dedicated fields (matched by the audit's "
        "EMITS_SYMBOLIC heuristic)."
    ),
    "mpmath-only": (
        "P2.5: this script's parent .py uses mpmath at canonical "
        "Q_MP precision (from q_parameter.Q_MP). It does not "
        "substitute a separately-fit q_0 — the canonical Q_MP IS "
        "the H^1 calibration value. Algebraic structure is "
        "preserved at high precision; the witness JSON's numerical "
        "values are evaluations of the canonical algebraic form."
    ),
    "partial": (
        "P2.5: this script's parent .py uses sympy.Symbol('q') "
        "for some intermediate computation but the witness JSON "
        "does not yet expose a `*_polynomial_q` / `*_symbolic` "
        "field for the final result. Refactor candidate per "
        "docs/audits/2026-05-02-p2-5-symbolic-q-audit.md "
        "'Recommended ordering' #1."
    ),
    "early-substitution": (
        "P2.5: this script's parent .py substitutes q_0 (a float) "
        "near the top and computes numerically afterwards. Reads "
        "as 'fitted' in witness JSONs even though q_0 IS the "
        "single H^1 calibration. Refactor candidate per "
        "docs/audits/2026-05-02-p2-5-symbolic-q-audit.md "
        "'Recommended ordering' #2 (light) / #3 (numpy-heavy)."
    ),
}


def load_audit() -> dict[str, str]:
    """Return {script_basename: category} from the audit witness."""
    aud = json.loads(AUDIT_WITNESS.read_text())
    return {
        Path(c["path"]).name.replace(".py", ""): c.get("category", "uncategorised")
        for c in aud["classifications"]
    }


def build_annotation(category: str) -> dict:
    return {
        "audit_version": ANNOTATION_VERSION,
        "audit_doc": "docs/audits/2026-05-02-p2-5-symbolic-q-audit.md",
        "category": category,
        "compliance_note": NOTES.get(
            category,
            "P2.5: category not classified by audit (uncategorised "
            "or no-q-dependence). No discipline declaration added."
        ),
    }


def witness_for_script(script_basename: str) -> Path | None:
    """Return the witness JSON path corresponding to a script,
    using common naming conventions."""
    candidates = [
        COMPUTE / f"{script_basename}.witness.json",
        COMPUTE / f"{script_basename.replace('_', '-')}.witness.json",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def update_witness(witness_path: Path, annotation: dict, dry_run: bool) -> bool:
    """Insert/update the `p2_5_compliance` annotation in the
    witness JSON.  Returns True if the file was modified or
    would be in a non-dry-run."""
    try:
        text = witness_path.read_text()
        data = json.loads(text)
    except Exception:
        return False
    if not isinstance(data, dict):
        return False
    existing = data.get("p2_5_compliance")
    if isinstance(existing, dict) and existing.get("audit_version") == ANNOTATION_VERSION:
        return False  # idempotent: already at current version
    data["p2_5_compliance"] = annotation
    if dry_run:
        return True
    witness_path.write_text(json.dumps(data, indent=2, default=str))
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="only report changes")
    ap.add_argument("--categories", default="partial,early-substitution,mpmath-only,compliant",
                    help="comma-separated category list")
    args = ap.parse_args()
    targets = set(args.categories.split(","))
    audit = load_audit()
    print(f"  P2.5 metadata pass — {len(audit)} scripts triaged")
    print(f"  Targets: {sorted(targets)}")
    counts = {"updated": 0, "skipped_no_witness": 0, "skipped_idempotent": 0,
              "skipped_off_target": 0, "skipped_unparseable": 0}
    for script, cat in sorted(audit.items()):
        if cat not in targets:
            counts["skipped_off_target"] += 1
            continue
        wpath = witness_for_script(script)
        if wpath is None:
            counts["skipped_no_witness"] += 1
            continue
        annotation = build_annotation(cat)
        if update_witness(wpath, annotation, args.dry_run):
            counts["updated"] += 1
        else:
            counts["skipped_idempotent"] += 1
    print(f"  Updated:               {counts['updated']}")
    print(f"  Skipped (no witness):  {counts['skipped_no_witness']}")
    print(f"  Skipped (idempotent):  {counts['skipped_idempotent']}")
    print(f"  Skipped (off-target):  {counts['skipped_off_target']}")
    if args.dry_run:
        print("  (dry-run: no files written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
