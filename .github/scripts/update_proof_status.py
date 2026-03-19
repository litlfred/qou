"""
Update Proof Status from Lean Build

Reads `lake build` output to determine which declarations contain `sorry`
and updates `proof-objects.json` accordingly.

Usage:
    python .github/scripts/update_proof_status.py \\
        [--manifest proof-objects.json] \\
        [--build-log build.log]

This script is designed to run as part of CI after `lake build`.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_MANIFEST = REPO_ROOT / "proof-objects.json"


def parse_sorry_warnings(log_text):
    """Extract declaration names that use sorry from build log output.

    Lean emits warnings like:
        QOU/Torsion.lean:42:0: warning: declaration uses 'sorry'
    """
    sorry_decls = set()
    pattern = re.compile(
        r"(\S+\.lean):(\d+):\d+:\s*warning:\s*declaration uses 'sorry'"
    )
    for m in pattern.finditer(log_text):
        sorry_decls.add((m.group(1), int(m.group(2))))
    return sorry_decls


def parse_sorry_decl_names(log_text):
    """Extract sorry-using declaration names from build log.

    Also look for lines like:
        warning: 'QOU.Torsion.lifting_exists' uses sorry
    """
    names = set()
    pattern = re.compile(r"'([^']+)'\s+uses sorry")
    for m in pattern.finditer(log_text):
        names.add(m.group(1))
    return names


def main():
    parser = argparse.ArgumentParser(description="Update proof status from Lean build.")
    parser.add_argument(
        "--manifest", type=Path, default=DEFAULT_MANIFEST,
        help="Path to proof-objects.json",
    )
    parser.add_argument(
        "--build-log", type=Path, default=None,
        help="Path to build log file (reads stdin if omitted)",
    )
    args = parser.parse_args()

    if not args.manifest.exists():
        print(f"❌ Manifest not found: {args.manifest}")
        sys.exit(1)

    if args.build_log and args.build_log.exists():
        log_text = args.build_log.read_text(encoding="utf-8")
    else:
        log_text = sys.stdin.read()

    sorry_names = parse_sorry_decl_names(log_text)
    sorry_locations = parse_sorry_warnings(log_text)

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)

    updated = 0
    for obj in manifest.get("objects", []):
        lean_info = obj.get("lean")
        if not lean_info or "decl" not in lean_info:
            continue

        decl = lean_info["decl"]
        old_status = obj.get("formalization_status", "not_started")

        if decl in sorry_names:
            new_status = "has_sorry"
            lean_info["sorry_free"] = False
        elif old_status in ("stated", "has_sorry"):
            # If it was previously stated/has_sorry and no sorry warning,
            # it may now be proved
            new_status = "proved"
            lean_info["sorry_free"] = True
        else:
            continue

        if new_status != old_status:
            obj["formalization_status"] = new_status
            updated += 1

    # Update timestamp
    manifest["manuscript"]["generated_at"] = datetime.now(timezone.utc).isoformat()

    with open(args.manifest, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"✅ Updated {updated} object statuses in {args.manifest}")


if __name__ == "__main__":
    main()
