#!/usr/bin/env python3
"""THEOREMS carrying a syntactic tautology -- a binder or the conclusion of the
form `t = t` where the two sides are identical AND the match spans the WHOLE
slot, not a suffix of the left side.

Why the anchor matters: without a left delimiter, `f (e l) = e l` matches as
`e l = e l`.  A first pass without it reported 51 hits, essentially all of that
shape.
"""
import re, pathlib, importlib.util
spec = importlib.util.spec_from_file_location("risk", "scripts/lean-axiom-degenerate-risk-audit.py")
risk = importlib.util.module_from_spec(spec); spec.loader.exec_module(risk)

DECL = re.compile(r"^\s*(?:private\s+|protected\s+|noncomputable\s+)?(theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_.'!?]*)")

def tautologies(text: str):
    """Yield `t = t` occurrences that fill a whole binder or the conclusion."""
    out = []
    # binder slots:  ( name : BODY )   and the conclusion after the final `:`
    for slot in re.findall(r"\(\s*[A-Za-z_][A-Za-z0-9_'!?]*\s*:\s*([^()]+?)\s*\)", text):
        out.append(slot)
    # conclusion: last top-level `:` .. end (crude but only used for equality shape)
    m = re.search(r":\s*([^:]+?)\s*(?::=|$)", text.strip().split("\n")[-1])
    if m: out.append(m.group(1))
    for s in out:
        s = s.strip()
        parts = s.split("=")
        if len(parts) != 2: continue
        a, b = parts[0].strip(), parts[1].strip()
        if a and a == b and len(a) > 1:
            yield f"{a} = {a}"

hits = []
for p in sorted(pathlib.Path("content").rglob("*.lean")):
    if ".lake" in p.parts: continue
    try: raw = p.read_text()
    except Exception: continue
    lines = risk.strip_block_comments(raw).split("\n")
    for i, line in enumerate(lines):
        m = DECL.match(line)
        if not m: continue
        stmt, j = [], i
        while j < min(i + 30, len(lines)):
            stmt.append(re.sub(r"--.*", "", lines[j]))
            if ":=" in lines[j] or re.search(r"\bby\b\s*$", lines[j]): break
            j += 1
        for t in tautologies("\n".join(stmt)):
            hits.append((m.group(2), str(p), i + 1, t)); break

print(f"theorems whose STATEMENT carries a whole-slot tautology: {len(hits)}\n")
for n, f, ln, what in hits:
    print(f"  {n}\n      {f}:{ln}\n      -> {what}")


# MEASURED, 2026-09-07, on `main`:  ONE hit corpus-wide --
# `figure_eight_branching_rule`, whose hypothesis `chi_actual = chi_actual` is
# discharged by `rfl` and whose conclusion is `E = E`.  Found by hand first;
# this scan then found it and nothing else, which is the only reason it is
# committed.
#
# WHY IT EXISTS.  `lean-axiom-provability-probe.py` scans `axiom` only: a
# vacuous THEOREM has no axiom to convert and no axiom status to move, so it is
# structurally invisible there.  The corpus vacuity audit
# (`content/pipeline/lean-vacuity-axiom-audit.ts`) keys on a `: True`
# conclusion, which `E = E` is not.  Between them the shape had no detector.
#
# KNOWN LIMITS, asserted rather than discovered later:
#   * CONCLUSION detection is crude -- the last line after `:`.  The one true
#     positive was caught on its HYPOTHESIS; its conclusion is also a tautology
#     and this scan did not report that.  So treat it as hypothesis-focused.
#   * A tautology spelled with different-but-defeq sides (`f x = id (f x)`) is
#     not syntactic and is not found.
#   * A first version without a left anchor reported **51** hits, essentially
#     all of the form `f (e l) = e l` -- a suffix of the left side matching the
#     right.  Anchoring both ends took it to 1.  Do not relax the anchor.
