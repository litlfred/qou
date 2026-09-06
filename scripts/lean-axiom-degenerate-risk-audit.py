#!/usr/bin/env python3
"""Rank Lean `axiom` declarations by degenerate-instance refutation risk.

Motivation
----------
On 2026-09-05 all five SDP uniqueness axioms in `QOU/MathlibExt/` were shown
to be **false** — each one alone derives `False` (bean `qou-i6u4`).  Two prior
audits of that exact family (2026-08-26, 2026-09-03) had cleared them, because
both asked *is the citation real* and *can Mathlib close it*.  Neither asked the
third question:

    is the Lean statement the theorem that citation names?

An axiom with an impeccable citation to a true published theorem can still be a
false Lean proposition, when the formalisation drops a hypothesis the paper
requires.  Here the missing hypothesis was dual nondegeneracy, and the five
axioms fell to a one-dimensional zero-cost SDP.

What this flags
---------------
The shared signature of all five: a **collapsing conclusion** — an equality, a
`= 0`, or a uniqueness claim — reached from hypotheses that a *degenerate*
instance of the axiom's own structures satisfies vacuously.  Concretely the
counterexample worked because `S = 0` makes `S * (X - Y) = 0` hold for every
`X`, `Y`: the hypothesis looks like a guard and constrains nothing.

So this ranks by:

  * `collapsing`   the conclusion is `a = b`, `... = 0`, `Unique ...`,
                   `Subsingleton ...`, or `-> v = 0`.
  * `vacuous_risk` a hypothesis is an equation whose left side is a product or
                   an application involving a bound variable — the shape that
                   goes vacuous when a factor degenerates.
  * `unconstrained` the axiom quantifies over a structure but constrains none
                   of its components with a positivity / definiteness /
                   nondegeneracy / rank hypothesis.

This is a **triage aid, not a decision**.  A high score means "write the
degenerate instance and try to refute it"; it is not evidence of falsity, and a
low score is not evidence of soundness.  The only proof either way is a Lean
term.

Self-test
---------
`--selftest` reconstructs the five known-false axioms from git history and
requires all five to score in the flagged band.  The audit aborts if they do
not, so a future narrowing cannot silently report a clean tree.
"""
from __future__ import annotations
import argparse, pathlib, re, subprocess, sys

DECL_START = re.compile(r"^(axiom|theorem|lemma|def|abbrev|instance|structure|class|example|opaque|noncomputable|@\[|/--|/-!|namespace|end|section|variable|open|import|universe|set_option)\b")
AXIOM_RE = re.compile(r"^axiom\s+([A-Za-z_][A-Za-z0-9_.'!?]*)")

# Identifiers here are Unicode -- `Φ'`, `sc.Φstar`, `y_λ`. An ASCII-only
# character class silently fails to see the very conclusion shape this audit
# exists to find; the self-test caught exactly that on the first run.
IDENT = r"[^\s(),:=]+"
COLLAPSING = re.compile(
    r"(=\s*0\s*$|=\s*" + IDENT + r"\s*$|\bUnique\b|\bSubsingleton\b)")
PRODUCT_HYP = re.compile(r"\([_A-Za-z][A-Za-z0-9_']*\s*:[^)]*[*·]\s*\(?[^)]*\)?\s*=\s*0")
GUARD = re.compile(r"\b(PosDef|PosSemidef|nondegener|Nondegener|0\s*<|rank|Rank|Injective|IsUnit|Invertible|≠\s*0|Function\.Bijective)\b")


def axioms_in(text: str, path: str):
    """Yield (name, line, full declaration text) for each top-level axiom."""
    lines = text.split("\n")
    out = []
    i = 0
    while i < len(lines):
        m = AXIOM_RE.match(lines[i])
        if not m:
            i += 1
            continue
        body = [lines[i]]
        j = i + 1
        # A declaration continues while lines are indented or blank-then-indented.
        while j < len(lines):
            nxt = lines[j]
            if nxt.strip() == "":
                # peek: a blank line ends the decl unless the next non-blank is indented
                k = j
                while k < len(lines) and lines[k].strip() == "":
                    k += 1
                if k < len(lines) and lines[k].startswith((" ", "\t")) and not DECL_START.match(lines[k].lstrip()):
                    body.extend(lines[j:k + 1]); j = k + 1; continue
                break
            if not nxt.startswith((" ", "\t")):
                break
            body.append(nxt)
            j += 1
        out.append((m.group(1), i + 1, "\n".join(body), path))
        i = j
    return out


def score(decl: str):
    """Return (score, reasons). Higher = more worth attempting to refute."""
    # Split hypotheses from conclusion at the final top-level ':' of the binder list.
    flat = decl
    reasons = []
    s = 0
    # conclusion = text after the last ',\n' or the final ':' at depth 0
    tail = flat.strip().split("\n")
    concl = ""
    for ln in reversed(tail):
        if ln.strip():
            concl = ln.strip()
            break
    if COLLAPSING.search(concl):
        s += 3; reasons.append("collapsing-conclusion")
    if PRODUCT_HYP.search(flat):
        s += 2; reasons.append("product-equation-hypothesis(vacuous-when-a-factor-is-0)")
    if not GUARD.search(flat):
        s += 2; reasons.append("no-positivity/rank/nondegeneracy-guard")
    if re.search(r"∀|\{[^}]*:\s*Type", flat) and "Empty" not in flat:
        s += 1; reasons.append("universally-quantified-over-an-index-type")
    return s, reasons


KNOWN_FALSE = [
    ("SDP.lean", "strict_complementarity_unique_axiom"),
    ("SDPRealUniqueness.lean", "slater_strict_complementarity_kernel_axiom"),
    ("SDPRealUniqueness.lean", "SDPRankUniqueness"),
    ("SDPRankEquality.lean", "strict_complementarity_kernel_disjoint"),
    ("SDPRankEquality.lean", "affine_slater_rigidity"),
]
BASE = "content/quantum-observable-universe/lean/QOU/MathlibExt/"
THRESHOLD = 5


def selftest(rev: str) -> bool:
    ok = True
    for fname, name in KNOWN_FALSE:
        try:
            text = subprocess.run(["git", "show", f"{rev}:{BASE}{fname}"],
                                  capture_output=True, text=True, check=True).stdout
        except subprocess.CalledProcessError:
            print(f"  SELFTEST ERROR: cannot read {fname} at {rev}", file=sys.stderr)
            ok = False
            continue
        found = [a for a in axioms_in(text, fname) if a[0] == name]
        if not found:
            print(f"  SELFTEST FAIL: parser did not find `{name}` in {fname}@{rev}", file=sys.stderr)
            ok = False
            continue
        sc, reasons = score(found[0][2])
        mark = "ok " if sc >= THRESHOLD else "FAIL"
        if sc < THRESHOLD:
            ok = False
        print(f"  {mark} {name:<46} score={sc}  {','.join(reasons)}", file=sys.stderr)
    return ok


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--rev", default="origin/main",
                    help="revision holding the five known-false axioms (default origin/main)")
    ap.add_argument("--root", default="content")
    ap.add_argument("--top", type=int, default=25)
    args = ap.parse_args()

    print(f"self-test against the five known-false SDP axioms at {args.rev}:", file=sys.stderr)
    if not selftest(args.rev):
        print("\nSELF-TEST FAILED — the detector no longer flags axioms it is known to need "
              "to flag. Its verdicts are about itself, not the corpus. Aborting.", file=sys.stderr)
        return 2
    print("self-test passed\n", file=sys.stderr)
    if args.selftest:
        return 0

    rows = []
    for p in sorted(pathlib.Path(args.root).rglob("*.lean")):
        # `.lake/packages/` holds vendored Mathlib/Aesop, including their own
        # TEST files, which declare axioms freely. Counting those inflates the
        # corpus total several-fold -- the first run of this audit reported 364
        # axioms and ~40 of the flagged rows were Mathlib test fixtures.
        if ".lake" in p.parts or "SDPUniquenessCounterexamples" in str(p):
            continue
        for name, line, decl, path in axioms_in(p.read_text(errors="replace"), str(p)):
            sc, reasons = score(decl)
            rows.append((sc, path, line, name, reasons))
    rows.sort(key=lambda r: (-r[0], r[1], r[2]))
    flagged = [r for r in rows if r[0] >= THRESHOLD]
    print(f"axioms scanned : {len(rows)}")
    print(f"flagged (>= {THRESHOLD}) : {len(flagged)}")
    print()
    print("These are candidates for a degenerate-instance refutation attempt.")
    print("A high score is NOT evidence of falsity; only a Lean term settles it.")
    print()
    for sc, path, line, name, reasons in flagged[:args.top]:
        print(f"  [{sc}] {name}")
        print(f"       {path}:{line}")
        print(f"       {', '.join(reasons)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
