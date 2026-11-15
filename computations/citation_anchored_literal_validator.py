#!/usr/bin/env python3
"""Detect CITATION-ANCHORED LITERALS: high-precision numeric constants that
claim a published source in a comment but are neither recomputed in-file nor
pinned to a witness.

Why this checker exists
-----------------------
Two defects of the same class landed within one week (2026-07-26/27):

* `V₁`, `V₃` for the 5₂ saddle were hardcoded across four probes with the
  comment `# GGM eq 21 σ₃ (real connection)`. Reconciliation against both
  source papers showed the values match **neither** published convention,
  and eq (21) of that paper is the Stokes/3D-index identity — not a saddle
  value at all. The *cubic* the corpus used was correct, so nothing upstream
  caught it.
* `nzImVolume` used `sin(2φ)` where the Neumann–Zagier formula has
  `cos(2φ)`, caught only when a sibling checked against the 4₁ A-polynomial
  (`docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md`).

Both share one signature: **a number asserting provenance it does not
verify.** A citation in a comment reads as authority to every later agent,
but nothing recomputes it, so a transcription slip, a version renumbering,
or a convention mismatch propagates silently into phases and amplitudes.

What is flagged
---------------
A literal is reported when ALL of:

1. it carries ≥ `MIN_SIG_DIGITS` significant digits (default 8) — precision
   nobody types from memory, so it came from *somewhere*;
2. a citation-shaped comment sits on the line or within `LOOKBACK` lines
   above (`eq 21`, `GGM`, `arXiv:…`, `[author2021]`, `Table 3`, `§4.2`, …);
3. no verification evidence sits **local to the literal** — nothing on its
   own line or the line below matching a witness load, assertion, gate, or
   recomputation.

Condition 3 is what keeps the signal high: a hardcoded reference value used
as an assertion target is good practice and is NOT flagged. What is flagged
is a citation-anchored number consumed as an *input*.

**Gating is local, not file-level** (clarified 2026-08-01 after a Copilot
review caught this docstring describing the wrong scope). A file-level rule
would be far too coarse — a probe with one assertion anywhere would suppress
every finding in it, and these files are full of assertions. The separate
`file_has_verification` field is an **annotation only**: it marks findings in
files with no gates at all as extra-suspicious in the report, and suppresses
nothing.

How to clear a finding
----------------------
Preferred: compute the value from its published formula (see
`computations/probes/fivetwo_saddle_values.py` for the pattern — the
formula, both normalizations, and the source equation numbers in the
docstring). Otherwise: pin it to a witness, or add an in-file gate that
recomputes it and asserts agreement.

Usage
-----
    python3 computations/citation_anchored_literal_validator.py           # warn
    python3 computations/citation_anchored_literal_validator.py --strict  # exit 1
    python3 computations/citation_anchored_literal_validator.py --json

auditOnly; heuristic and high-recall by design — a finding is a prompt to
verify provenance, not proof of an error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MIN_SIG_DIGITS = 8
LOOKBACK = 2

# mp.mpf("…"), mp.mpc("…","…"), Decimal("…"), or a bare float literal
LITERAL_RE = re.compile(
    r'(?:mp\.mp[fc]|Decimal)\s*\(\s*["\']([-+]?[\d.eE+-]+)["\']'
    r'(?:\s*,\s*["\']([-+]?[\d.eE+-]+)["\'])?\s*\)'
    r'|(?<![\w.])([-+]?\d+\.\d{7,})(?![\w.])')

CITATION_RE = re.compile(
    r'\beq\.?\s*\(?\d+|\bequation\s*\(?\d+|\bGGMW?\b|\barXiv\b|\bTable\s*\d+'
    r'|\bFig(?:ure)?\.?\s*\d+|§\s*\d+|\bsec(?:tion)?\.?\s*\d+'
    r'|\[[A-Za-z][A-Za-z+-]*\d{2,4}[a-z]?\]|\bp\.\s*\d+',
    re.IGNORECASE)

# evidence the file checks its own numbers
VERIFIED_RE = re.compile(
    r'witness|add_assertion|assert\b|np\.testing|pytest|approx'
    r'|findroot|polyroots|solve\(|recompute|cross[_-]?check|gate',
    re.IGNORECASE)

# `"key": "value",` — a witness/dict payload line *records* a number, it does
# not consume one, so the citation-anchored-input signature does not apply.
DICT_ENTRY_RE = re.compile(r'^\s*["\'][^"\']+["\']\s*:\s*')

SKIP_DIRS = {"_deprecated", "fsh-guts", "__pycache__", ".git", "script-qa"}


def docstring_mask(lines: list[str]) -> list[bool]:
    """`True` on every line inside a triple-quoted block (or opening one).

    Module and function docstrings routinely *quote* the very literals a
    probe was fixed to stop consuming — the reference table in
    `fivetwo_saddle_values.py` is the motivating example — so prose must
    not read as a call site.
    """
    mask = [False] * len(lines)
    delim = None
    for i, line in enumerate(lines):
        rest, opened = line, delim is not None
        while True:
            if delim is None:
                m = re.search(r'"""|\'\'\'', rest)
                if not m:
                    break
                delim, rest, opened = m.group(0), rest[m.end():], True
            else:
                idx = rest.find(delim)
                if idx < 0:
                    break
                delim, rest = None, rest[idx + 3:]
        mask[i] = opened
    return mask


def sig_digits(tok: str) -> int:
    """Significant digits of a numeric token."""
    t = tok.strip().lstrip("+-").split("e")[0].split("E")[0]
    t = t.replace(".", "").lstrip("0")
    return len(t.rstrip("0")) if t else 0


def scan_file(path: Path):
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []
    verified_file = bool(VERIFIED_RE.search("\n".join(lines)))
    in_doc = docstring_mask(lines)
    out = []
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#") or in_doc[i]:
            continue
        if DICT_ENTRY_RE.match(line):
            continue
        for m in LITERAL_RE.finditer(line):
            toks = [t for t in m.groups() if t]
            if not toks or max(sig_digits(t) for t in toks) < MIN_SIG_DIGITS:
                continue
            ctx = "\n".join(lines[max(0, i - LOOKBACK): i + 1])
            cite = CITATION_RE.search(ctx)
            if not cite:
                continue
            # Is this literal itself gated, on its own line or the next?
            # Deliberately LOCAL, not file-level: `verified_file` below is an
            # annotation only and must not suppress, or one assertion
            # anywhere in a probe would mask every finding in it.
            near = "\n".join(lines[i: i + 2])
            if VERIFIED_RE.search(near):
                continue
            out.append({
                "file": str(path),
                "line": i + 1,
                "literal": m.group(0).strip(),
                "citation": cite.group(0).strip(),
                "source_line": line.strip()[:140],
                "file_has_verification": verified_file,
            })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any finding")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default="computations")
    args = ap.parse_args()

    root = Path(args.root)
    findings = []
    n_files = 0
    for p in sorted(root.rglob("*.py")):
        if any(d in p.parts for d in SKIP_DIRS):
            continue
        n_files += 1
        findings.extend(scan_file(p))

    if args.json:
        print(json.dumps({"files_scanned": n_files,
                          "findings": findings}, indent=2))
    else:
        print(f"citation-anchored-literal scan: {n_files} files, "
              f"{len(findings)} finding(s)\n")
        for f in findings:
            flag = "" if f["file_has_verification"] else "  [no gates in file]"
            print(f"  {f['file']}:{f['line']}{flag}")
            print(f"      literal : {f['literal']}")
            print(f"      cites   : {f['citation']}")
            print(f"      line    : {f['source_line']}")
        if findings:
            print("\n  Clear a finding by computing the value from its "
                  "published formula (pattern: "
                  "computations/probes/fivetwo_saddle_values.py), pinning it "
                  "to a witness, or adding an in-file recomputation gate.")
    return 1 if (args.strict and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
