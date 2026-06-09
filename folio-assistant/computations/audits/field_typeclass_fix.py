#!/usr/bin/env python3
"""Witness-driven fixer for over-strong `[Field]` binders.

Reads `field-typeclass-audit.witness.json` and, for every finding classified
`over-strong`, relaxes the field-strength binder **inside that declaration's
block only** (per-decl, not file-wide — the same file may contain genuine
field-using decls that must keep `[Field]`):

* ``[Field V]``       → ``[CommRing V]``
* ``[DivisionRing V]``→ ``[Ring V]``
* ``[LinearOrderedField V]`` → skipped (no `LinearOrderedCommRing` in the
  pinned Mathlib; these stay as-is and should be recorded as exceptions).

A decl's block runs from its opener line to the next top-level opener
(same logic as the audit's ``split_decls``). The fixer edits in place and
prints a per-file summary; verification (`lake build`) is the caller's job —
revert any module that fails and record it in the exceptions file.

Exceptions: ``field-typeclass-audit.exceptions.json`` — decls whose relaxation
was attempted and **failed the build** (so the `[Field]` is genuine-by-build).
The audit script reclassifies these as `genuine` with the recorded reason.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from field_typeclass_audit import DECL_OPEN_RE  # reuse decl-boundary logic

WITNESS = Path("folio-assistant/computations/audits/field-typeclass-audit.witness.json")
RELAX = {"Field": "CommRing", "DivisionRing": "Ring"}


def decl_block_range(lines: list[str], start_idx: int) -> tuple[int, int]:
    end = len(lines)
    for j in range(start_idx + 1, len(lines)):
        if DECL_OPEN_RE.match(lines[j]):
            end = j
            break
    return start_idx, end


def main() -> int:
    data = json.loads(WITNESS.read_text())
    by_file: dict[str, list[dict]] = defaultdict(list)
    for f in data["findings"]:
        if f["classification"] == "over-strong":
            by_file[f["file"]].append(f)

    skipped, fixed = [], []
    for path, findings in sorted(by_file.items()):
        p = Path(path)
        lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
        changed = False
        for f in findings:
            fc, var = f["field_class"], f["type_var"]
            if fc not in RELAX:
                skipped.append(f"{path}:{f['line']} [{fc} {var}] (no weaker class available)")
                continue
            s, e = decl_block_range(lines, f["line"] - 1)
            pat = re.compile(r"\[\s*" + fc + r"\s+" + re.escape(var) + r"\s*\]")
            done = False
            for i in range(s, e):
                new, n = pat.subn(f"[{RELAX[fc]} {var}]", lines[i])
                if n:
                    lines[i] = new
                    done = True
                    break
            if done:
                fixed.append(f"{path}:{f['line']} {f['decl_name']} [{fc} {var}] -> [{RELAX[fc]} {var}]")
                changed = True
            else:
                skipped.append(f"{path}:{f['line']} [{fc} {var}] (binder not found in block)")
        if changed:
            p.write_text("".join(lines), encoding="utf-8")

    print(f"fixed {len(fixed)}:")
    for x in fixed:
        print(f"  {x}")
    if skipped:
        print(f"skipped {len(skipped)}:")
        for x in skipped:
            print(f"  {x}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
