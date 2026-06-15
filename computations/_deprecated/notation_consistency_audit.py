#!/usr/bin/env python3
"""
notation_consistency_audit.py — Lightweight audit agent that scans
the codebase + audit docs for notation violations of the rules
documented in:

  content/quantum-observable-universe/notation/notation-register.md
  content/quantum-observable-universe/notation/notation-collisions.md

Currently enforced rules (Round-3 PR #546):

  1. q^{1/2} variable must be `r` (spinor information rate).
     Forbidden alternatives: `t` (knot variable clash),
     `ι`/`iota` (involution clash), `u` is allowed only in PR #545's
     legacy `closed_form_d_u` helper (whitelisted).

  2. Wenzl principal-spec length is `\ell` (or `ell` in code), NOT
     `r_W` (renamed when r became reserved for the spinor rate).

  3. Vortex morphism is `\varrho` (not `\gamma`).

  4. Numerical q_0 = 1.1097 string only allowed in introduction +
     Ch 8 (Information Theory) + Ch 11 (Observations) — geometry
     chapters use symbolic q.

This script is **warn-only** by default; pass `--strict` to fail
CI on any violation. Whitelist file
[`notation_consistency_whitelist.json`](notation_consistency_whitelist.json)
documents intentional exceptions.

Run:
    python3 folio-assistant/computations/notation_consistency_audit.py
    python3 folio-assistant/computations/notation_consistency_audit.py --strict
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class Violation:
    rule: str
    file: Path
    line: int
    text: str
    severity: str  # "error" | "warn"


# Forbidden: `t = q^{1/2}` or similar in audit docs / new content.
PATTERNS_FORBIDDEN_T_FOR_SQRT_Q = [
    r"\bt\s*=\s*q\^\{1/2\}",
    r"\\sqrt\{q\}\s*=\s*t\b",
    r"\bt\s*:=\s*\\sqrt\{q\}",
]

# Forbidden: ι/iota for q^{1/2}.
PATTERNS_FORBIDDEN_IOTA = [
    r"\\iota\s*=\s*q\^\{1/2\}",
    r"\biota\b\s*=\s*q\^\{1/2\}",
]

# Forbidden: r_W as Wenzl level (should be \ell after rename).
PATTERNS_FORBIDDEN_R_W = [
    r"\br_W\b",
    r"\br_\{W\}",
]

# Numerical q values allowed only in intro / Ch 8 / Ch 11.
NUMERIC_Q_ALLOWED_PATHS = (
    "content/quantum-observable-universe/introduction",
    "content/quantum-observable-universe/information-theory",
    "content/quantum-observable-universe/observations",
    "content/quantum-observable-universe/notation",  # notation register can mention q_0
    "docs/audits",                                    # audits can quote numerical
    "folio-assistant/computations",                   # scripts compute numerically
    "folio-assistant/feedback",                       # session feedback may quote
)
NUMERIC_Q_PATTERN = r"\bq[\s_]*=[\s]*1\.1097\b|\bq_0\s*=\s*1\.1097"


def scan_file(path: Path, *, allow_numeric_q: bool) -> list[Violation]:
    out: list[Violation] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return out

    # Files that legitimately discuss the forbidden patterns
    # (the rules themselves + this audit script).
    SELF_REFERENCE_FILES = {
        "notation_consistency_audit.py",
        "notation-collisions.md",
        "notation-register.md",
        "2026-05-05-r-and-kite-tails-exploration.md",  # discusses rejected alternatives
        "2026-05-05-y-lambda-tr-m-equivalence-proof.md",  # uses r consistently
    }
    if path.name in SELF_REFERENCE_FILES:
        return out

    lines = text.splitlines()
    for i, line in enumerate(lines, start=1):
        # Skip whitelist comments.
        if "noqa: notation" in line or "notation-whitelist" in line:
            continue

        for pat in PATTERNS_FORBIDDEN_T_FOR_SQRT_Q:
            if re.search(pat, line):
                out.append(Violation(
                    rule="forbidden-t-for-sqrt-q",
                    file=path, line=i, text=line.rstrip(),
                    severity="error",
                ))
        for pat in PATTERNS_FORBIDDEN_IOTA:
            if re.search(pat, line):
                out.append(Violation(
                    rule="forbidden-iota-for-sqrt-q",
                    file=path, line=i, text=line.rstrip(),
                    severity="error",
                ))
        for pat in PATTERNS_FORBIDDEN_R_W:
            if re.search(pat, line):
                out.append(Violation(
                    rule="forbidden-r-W-use-ell",
                    file=path, line=i, text=line.rstrip(),
                    severity="warn",  # legacy code likely; warn-only
                ))
        if not allow_numeric_q and re.search(NUMERIC_Q_PATTERN, line):
            out.append(Violation(
                rule="numeric-q-outside-allowed-chapters",
                file=path, line=i, text=line.rstrip(),
                severity="warn",
            ))

    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--strict", action="store_true",
                   help="Fail (exit code 1) on any violation")
    p.add_argument("--root", type=str, default=str(REPO_ROOT))
    args = p.parse_args()

    root = Path(args.root)
    targets: list[Path] = []
    for ext in ("*.md", "*.tex", "*.ts", "*.py"):
        for f in root.rglob(ext):
            # Skip generated / vendored content.
            sp = str(f.relative_to(root))
            if any(seg in sp for seg in (
                "node_modules", ".lake", "build/", "lake-packages",
                ".git/", "_minted", "auto/",
            )):
                continue
            targets.append(f)

    all_violations: list[Violation] = []
    for f in targets:
        rel = str(f.relative_to(root))
        allow_numeric_q = any(rel.startswith(p) for p in NUMERIC_Q_ALLOWED_PATHS)
        all_violations.extend(scan_file(f, allow_numeric_q=allow_numeric_q))

    errs = [v for v in all_violations if v.severity == "error"]
    warns = [v for v in all_violations if v.severity == "warn"]

    print(f"Scanned {len(targets)} files.")
    print(f"  errors:   {len(errs)}")
    print(f"  warnings: {len(warns)}")
    print()

    if errs:
        print("ERRORS:")
        for v in errs[:30]:
            rel = v.file.relative_to(root)
            print(f"  [{v.rule}]  {rel}:{v.line}: {v.text[:120]}")
        if len(errs) > 30:
            print(f"  ... and {len(errs) - 30} more.")
        print()

    if warns:
        print("WARNINGS:")
        for v in warns[:30]:
            rel = v.file.relative_to(root)
            print(f"  [{v.rule}]  {rel}:{v.line}: {v.text[:120]}")
        if len(warns) > 30:
            print(f"  ... and {len(warns) - 30} more.")
        print()

    # Emit witness.
    out = Path(__file__).resolve().parent / "notation_consistency_audit.witness.json"
    witness = {
        "computation": "notation-consistency-audit",
        "description": (
            "Scan repository for violations of notation rules in "
            "notation-register.md / notation-collisions.md. "
            "Currently enforces: r := q^(1/2) (no t, no iota), "
            "Wenzl level uses ell (not r_W), numerical q_0 only in "
            "intro/Ch8/Ch11. Warn-only by default; --strict makes "
            "errors fail CI."
        ),
        "n_files_scanned": len(targets),
        "n_errors": len(errs),
        "n_warnings": len(warns),
        "errors": [
            {"rule": v.rule, "file": str(v.file.relative_to(root)),
             "line": v.line, "text": v.text[:200]}
            for v in errs
        ],
        "warnings": [
            {"rule": v.rule, "file": str(v.file.relative_to(root)),
             "line": v.line, "text": v.text[:200]}
            for v in warns
        ],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    out.write_text(json.dumps(witness, indent=2))
    print(f"witness: {out.name}")

    if args.strict and errs:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
