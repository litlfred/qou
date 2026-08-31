#!/usr/bin/env python3
# polynomial_q_not_applicable: reads a committed symbolic witness and tests
# the SHAPE of a recorded rational function. No q0 evaluation is performed
# for any conclusion; the two recorded floats are quoted only to show that
# quoting them is the error this probe is about.
"""
r5full_anchor_gate_evidence_probe.py — the r5full anchor gate is SOUND, and
the number everyone quotes for it is not the evidence.

## What the gate is

`conj:canonical-knot-id-sdp` (#604, R5-full) is the corpus's only route to a
nucleus->link assignment that is not an AME census fit.  It is blocked by an
"A<=3 anchor non-confirmation", stated in two audits as

    tr_M(2H) ~ 0.388   vs   J_{6_2}(q0) ~ 1.027   -- "they do not match"

(`docs/audits/2026-07-04-he4-vol4-gated-on-r5full.md` §3;
`docs/audits/2026-07-13-atom-knot-rule-a5plus-constraints.md` C2 and §4.)

## The raw-value comparison is not evidence, by construction

The producer those audits cite is `atom_nf_symbolic_D.py`.  Its conversion
step is:

    def markov_trace_to_jones(tr):
        \"\"\"Jones(K) = ((-1/sqrt q)^{n-1} * (q/(1-q^2))^{n-1})... (convention dep).
        For ease, we return tr as-is ...\"\"\"
        return sp.simplify(tr)

**It is the identity function.**  It names the normalisation factor in its own
docstring and then does not apply it.  `main()` calls it and compares the
result directly against a properly-normalised `J(6_2)` from Kawauchi/KnotInfo.
So the two sides are an UNNORMALISED 6-strand Markov trace and a NORMALISED
Jones polynomial: they are expected to differ, and the size of the gap carries
no information about the knot identification.

Quoting `0.388 vs 1.027` -- or any percentage derived from the pair -- is
therefore reading the wrong field.  That includes the C-vs-D scoping of the
`0.388` itself: correcting an input to a comparison that was never evidential
does not make it evidential.

## The producer supplies the RIGHT test, and it fails

`atom_nf_symbolic_D.main()` knows the normalisation is missing and computes
the convention-independent discriminator instead:

    # Ratio test: even if they differ by a writhe/normalization factor,
    # the ratio should be a pure power of -q^{1/2}.  Check.
    ratio = sp.simplify(tr_simp / J_62)

recorded as `symbolic_ratio` in the witness.  If the atom element's closure
were `6_2`, that ratio would be a monomial.  Measured below: it is a rational
function with **83 terms over 11**, in half-integer powers of `q` running past
`q^(2713/2)`.  Not a monomial by a wide margin.

## Verdict

**The gate stands, and it is better supported than its own citation suggests.**
The anchor non-confirmation is real; the evidence is the ratio test, not the
two floats.  A future attempt on `conj:canonical-knot-id-sdp` should aim at the
ratio -- and should not read the raw gap as "how far off" the identification
is, because that distance is dominated by an omitted normalisation.

Scope **(a)**: about the EVIDENCE for the gate, not about the knot.  Nothing
here shows `6_2` is right or wrong for the deuteron.
"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
WITNESS = ROOT / "computations" / "atom-nf-symbolic-D.witness.json"
PRODUCER = ROOT / "computations" / "atom_nf_symbolic_D.py"


def conversion_is_identity() -> tuple[bool, str]:
    """Parse the producer and decide whether markov_trace_to_jones applies a
    normalisation, by inspecting its AST rather than grepping its text."""
    tree = ast.parse(PRODUCER.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "markov_trace_to_jones":
            arg = node.args.args[0].arg
            body = [n for n in node.body if not isinstance(n, ast.Expr)
                    or not isinstance(n.value, ast.Constant)]  # drop docstring
            if len(body) != 1 or not isinstance(body[0], ast.Return):
                return False, "body is not a single return"
            r = body[0].value
            # sp.simplify(<arg>) or bare <arg> — either way, no factor applied.
            if isinstance(r, ast.Name) and r.id == arg:
                return True, f"returns `{arg}` unchanged"
            if (isinstance(r, ast.Call) and len(r.args) == 1
                    and isinstance(r.args[0], ast.Name) and r.args[0].id == arg):
                fn = ast.unparse(r.func)
                return True, f"returns `{fn}({arg})` — simplification only, no factor"
            return False, f"returns `{ast.unparse(r)}`"
    return False, "function not found"


def main() -> int:
    checks: list[tuple[bool, str]] = []
    print("=" * 74)
    print("r5full ANCHOR GATE — is the quoted number the evidence?")
    print("=" * 74)

    # ── 1. the conversion is a no-op ────────────────────────────────
    is_id, why = conversion_is_identity()
    print(f"\n[1] markov_trace_to_jones: {why}")
    checks.append((is_id, "markov_trace_to_jones applies no normalisation"))
    print("    => the compared pair is an UNNORMALISED 6-strand Markov trace")
    print("       against a NORMALISED Jones polynomial. The raw gap between")
    print("       them is not evidence about the knot identification.")

    w = json.loads(WITNESS.read_text())
    tr0, j0 = w["at_q0"]["tr_M_D"], w["at_q0"]["J_62"]
    print(f"\n    recorded tr_M_D(q0) = {tr0}")
    print(f"    recorded J_62(q0)   = {j0}")
    print("    (quoted here ONLY to identify the pair that should not be quoted)")

    # ── 2. the ratio test, which is the real discriminator ──────────
    print("\n[2] The producer's own ratio test — tr/J must be a pure power of")
    print("    -q^(1/2) if the closure is 6_2.\n")
    q = sp.Symbol("q", positive=True)
    ratio = sp.sympify(w["symbolic_ratio"], locals={"q": q})
    num, den = sp.fraction(sp.together(ratio))
    n_num = len(sp.Add.make_args(sp.expand(num)))
    n_den = len(sp.Add.make_args(sp.expand(den)))
    is_monomial = bool(ratio.is_Pow or ratio.is_Symbol or ratio.is_Number)
    print(f"    numerator terms   : {n_num}")
    print(f"    denominator terms : {n_den}")
    print(f"    is a pure power   : {is_monomial}")
    checks.append((not is_monomial,
                   "symbolic_ratio is NOT a pure power => ratio test FAILS"))
    checks.append((n_num > 1 and n_den > 1,
                   "ratio is a genuine rational function, not a monomial"))

    print("\n    => the ratio test FAILS, so the anchor non-confirmation is")
    print("       REAL. The gate stands — on this evidence, not on the two")
    print("       floats above.")

    # ── 3. what a future attempt should aim at ──────────────────────
    print("\n[3] Consequence")
    print("    - Do NOT quote `0.388 vs 1.027`, nor any percentage from it.")
    print("    - Correcting 0.388 for convention C-vs-D does not rescue the")
    print("      comparison: an unnormalised trace stays unnormalised.")
    print("    - A future attempt on conj:canonical-knot-id-sdp should aim at")
    print("      the RATIO being a pure power of -q^(1/2), which is the")
    print("      convention-independent statement.")

    print("\n" + "=" * 74)
    failed = [m for ok, m in checks if not ok]
    for ok, m in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {m}")
    print(f"{len(checks) - len(failed)}/{len(checks)} checks passed")
    print("=" * 74)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
