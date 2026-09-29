#!/usr/bin/env python3
"""THEOREMS carrying a syntactic tautology — a binder or conclusion of the
form `t = t` whose two sides are token-identical.

WHY IT EXISTS.  `scripts/lean-axiom-provability-probe.py` scans `axiom` only:
a vacuous THEOREM has no axiom to convert and no axiom status to move, so it
is structurally invisible there.  The corpus vacuity audit
(`folio/pipeline/lean-vacuity-axiom-audit.ts`) keys on a `: True`
conclusion, which `E = E` is not.  Between them this shape had no detector,
which is how `figure_eight_branching_rule` stood with a `rfl` conclusion and
a `chi_actual = chi_actual` hypothesis.

TWO BUGS OF MINE, BOTH FOUND AFTER SHIPPING, BOTH RECORDED HERE:

  1. NO LEFT ANCHOR -> 51 FALSE POSITIVES.  The first regex matched a SUFFIX
     of the left side against the right, so `f (e l) = e l` read as
     `e l = e l`.  Essentially all 51 hits were that.  Anchoring both ends
     took it to 1.  Do not relax the anchor.

  2. `let` TRUNCATED THE CAPTURE.  Statement capture terminated on the first
     line containing `:=` — but `let h := q - 1/q` inside a statement contains
     `:=`, so capture stopped at the `let` and never reached the conclusion.
     A conclusion-side pass therefore reported 0 on a corpus that had a
     positive.  `_is_definition_sep` now distinguishes the proof separator
     from a `let`/`have`/`set` binder.

REMAINING LIMIT, asserted rather than discovered later: a tautology whose
sides are definitionally equal but not syntactically identical
(`f x = id (f x)`) is not found.  This scan is syntactic by design.
"""
import re
import sys
import pathlib
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "risk", str(pathlib.Path(__file__).with_name("lean-axiom-degenerate-risk-audit.py")))
risk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(risk)

DECL = re.compile(
    r"^\s*(?:private\s+|protected\s+|noncomputable\s+)?(theorem|lemma)\s+"
    r"([A-Za-z_][A-Za-z0-9_.'!?]*)")


def _is_definition_sep(line: str) -> bool:
    """True when `:=` on this line opens the PROOF, not a `let`/`have` binder."""
    if ":=" not in line:
        return False
    if re.match(r"\s*(let|have|set|obtain)\b", line):
        return False
    if re.search(r"\b(let|have|set)\b[^:]*:=", line):
        return False
    return True


def tautologies(text: str):
    """Whole-slot `t = t`: a binder body, or the conclusion.

    Both ends anchored — a bare `a = a` search matches suffixes (bug 1).
    """
    slots = re.findall(r"\(\s*[A-Za-z_][A-Za-z0-9_'!?]*\s*:\s*([^()]+?)\s*\)", text)
    tail = text.strip().split("\n")[-1]
    m = re.search(r":\s*([^:]+?)\s*(?::=|$)", tail)
    if m:
        slots.append(m.group(1))
    for s in slots:
        parts = s.strip().split("=")
        if len(parts) != 2:
            continue
        a, b = parts[0].strip(), parts[1].strip()
        if a and a == b and len(a) > 1:
            yield f"{a} = {a}"


def scan_text(text: str):
    """Yield (decl_name, tautology) for every declaration in `text`."""
    lines = risk.strip_block_comments(text).split("\n")
    for i, line in enumerate(lines):
        m = DECL.match(line)
        if not m:
            continue
        stmt, j = [], i
        while j < min(i + 40, len(lines)):
            cur = re.sub(r"--.*", "", lines[j])
            stmt.append(cur)
            if _is_definition_sep(cur) or re.search(r"\bby\b\s*$", cur):
                break
            j += 1
        for t in tautologies("\n".join(stmt)):
            yield (m.group(2), i + 1, t)
            break


# The fixture is EMBEDDED, not read from a revision.  This session twice
# shipped a self-test that read fixtures from a moving ref and went red the
# moment the fix landed; an embedded string cannot rot at all.
#
# It is the pre-fix `figure_eight_branching_rule`.  It exists because a scan
# reporting 0 has proved nothing — and this one DID report 0 for a bad reason
# (bug 2 above).  A self-test would have caught that immediately.
SELFTEST_FIXTURE = """theorem figure_eight_branching_rule (q : R) (hq : q > 1) (k : N)
    (hk : k >= 3) (lambda : List N) (hlam : lambda.sum = k)
    (chi_actual : R)
    (h_chi : chi_actual = chi_actual) :
    let h := q - 1/q
    let f3 := skewSYTCount [3] lambda
    (f3 : Z) = (f3 : Z) := by
  rfl
"""


def selftest() -> bool:
    found = list(scan_text(SELFTEST_FIXTURE))
    if not found:
        print("  SELFTEST FAIL: the embedded pre-fix fixture is not detected.",
              file=sys.stderr)
        print("  A corpus result of 0 proves nothing unless this still fires.",
              file=sys.stderr)
        return False
    print(f"  ok   figure_eight_branching_rule (pre-fix fixture) -> {found[0][2]}",
          file=sys.stderr)
    return True


def main() -> int:
    print("self-test against the embedded pre-fix fixture:", file=sys.stderr)
    if not selftest():
        print("\nSELF-TEST FAILED — the scan no longer finds a tautology it is "
              "known to need to find. Its corpus verdict is about itself.",
              file=sys.stderr)
        return 1
    print("self-test passed\n", file=sys.stderr)

    hits = []
    for p in sorted(pathlib.Path("folio").rglob("*.lean")):
        if ".lake" in p.parts:
            continue
        try:
            raw = p.read_text()
        except Exception:
            continue
        for name, ln, what in scan_text(raw):
            hits.append((name, str(p), ln, what))

    print(f"theorems whose statement carries a whole-slot tautology: {len(hits)}\n")
    for name, f, ln, what in hits:
        print(f"  {name}\n      {f}:{ln}\n      -> {what}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
