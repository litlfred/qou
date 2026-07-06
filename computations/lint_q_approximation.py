#!/usr/bin/env python3
"""q = 111/100 approximation lint (ratchet — no NEW uses).

The exact-Fraction Hecke path evaluates at the rational q = 111/100 = 1.11
(z = 4993/10000), which is ~2e-4 from the true substrate q0 = 1.1099786.
"exact=True" therefore means *exact-rational at an approximate q*, NOT high
precision — a footgun at the framework's ppb precision goals
(docs/audits/2026-06-16-gram-q-approximation-audit.md).

The approximation has a small set of legitimate homes (the exact-rational
engine itself + a documented appendix table). This lint flags any NEW
occurrence outside that allowlist so the footgun cannot spread. The
true-q0 path is the float `G`/`nf_tr` or the 50-dps `gram_matrix_mp`/
`tr_m_mp` mpmath accessors.

Usage:
    python3 computations/lint_q_approximation.py            # report; warn
    python3 computations/lint_q_approximation.py --strict   # exit 1 on new
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

# Files that legitimately host the q = 111/100 exact-rational path:
#   - the exact-Fraction engine + its definitions
#   - re-export shims
#   - the documented appendix table (hadron-knot-table) — see its q0 note
ALLOWLIST = {
    "tools/pyhecke/python/pyhecke/gram.py",        # _Q_FRAC/_Z_FRAC/_H_FRAC definitions
    "computations/hecke/hecke_engine.py",          # HeckeRational(111, 100)
    "tools/pyhecke/python/pyhecke/atom.py",        # build_atom_nf_exact (exact path)
    "computations/hecke_core_legacy.py",           # re-exports the _*_FRAC constants
    "computations/substrate/hecke_core.py",        # re-exports
    "computations/hadron_knot_table.py",           # documented appendix table
}

PATTERN = re.compile(
    r"Fraction\(\s*111\s*,\s*100\s*\)"
    r"|Rational\(\s*111\s*,\s*100\s*\)"
    r"|Hecke(?:Engine|Rational)\(\s*111\b"
    r"|Fraction\(\s*4993\s*,\s*10000\s*\)"
    r"|\b_Q_FRAC\b|\b_QI_FRAC\b|\b_H_FRAC\b|\b_Z_FRAC\b"
)

SCAN_ROOTS = [HERE, REPO / "tools"]


def _rel(p: Path) -> str:
    # as_posix() so Windows backslash paths still match the forward-slash
    # ALLOWLIST entries (Gemini #2355).
    try:
        return p.relative_to(REPO).as_posix()
    except ValueError:
        return p.as_posix()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any NEW (non-allowlisted) occurrence")
    args = ap.parse_args()

    new_hits: list[tuple[str, int, str]] = []
    n_allow = 0
    for root in SCAN_ROOTS:
        if not root.is_dir():
            continue
        for py in root.rglob("*.py"):
            parts = py.parts
            if "_deprecated" in parts or ".lake" in parts:
                continue
            if py.name.startswith("test_") or "tests" in parts:
                continue
            if py.resolve() == Path(__file__).resolve():
                continue
            rel = _rel(py)
            try:
                lines = py.read_text(encoding="utf-8").splitlines()
            except (UnicodeDecodeError, OSError):
                continue
            for i, line in enumerate(lines, 1):
                if PATTERN.search(line):
                    if rel in ALLOWLIST:
                        n_allow += 1
                    else:
                        new_hits.append((rel, i, line.strip()))

    print(f"q=111/100 lint: {n_allow} allowlisted occurrence(s); "
          f"{len(new_hits)} NEW occurrence(s) outside the allowlist.")
    if new_hits:
        print("\nNEW q=111/100 uses (use the true-q0 float/mpmath path "
              "instead — gram_matrix_mp/tr_m_mp, or float G/nf_tr):")
        for rel, ln, txt in new_hits:
            print(f"  {rel}:{ln}: {txt[:90]}")
    return 1 if (new_hits and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
