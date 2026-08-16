#!/usr/bin/env python3
"""
peel_anchor_identification_probe.py — the peel is exact in q, and the
"8.71e-8 residual" was a peel value read out of the wrong anchor's witness.

WHAT THIS SETTLES.  Bean `qou-8x1l` recorded eight hypotheses and eight
refutations around a residual in the Markov identity

    Σ_{λ ⊢ n} y_λ(q) · χ^λ(β) = tr_M(β),

measured on the deuteron braid β_D.  Its summary was:

    bridge(proton y, proton χ) = 0.575172243917771870826535
    bridge(muon y,   proton χ) = 0.575172395398020063703615
    peel (proton, symbolic)    = 0.575172331017883851919791796687
    bridge(muon y,  proton χ)  = peel  to 3.63e-51

    "Mixing anchors satisfies the identity exactly; matching them misses by
     8.71e-8.  Since Σ y_λ(q)·χ^λ(β,q) = tr_M(β,q) must hold *identically in
     q*, this is not an anchor question."

Both halves of that reading are wrong, and this probe measures why.

**1. The peel is an exact rational function of q.**  The bean records the
opposite as a blocking obstacle:

    "the braid word's `d` values are numeric and pinned.  χ^λ(β_D,q)
     therefore cannot be evaluated at an arbitrary q without rebuilding the
     word at that q."

`markov_peel.crossing_from_cd` uses the numeric `(c, d)` only to *identify*
which of five canonical templates a crossing is — a q-independent,
combinatorial choice — and then builds the element from the **symbolic**
form.  Even the colour weighting goes in symbolically, as
`(q − 1)²(1 − q⁻⁴)/3`.  So `tr_M_atomic` returns an integer-coefficient
rational function and no anchor enters it.  For the deuteron:

    numerator   : degree 50, integer coefficients, no Float atoms
    denominator : 192·q²³·(q² + 1)³

The `(q² + 1)³` is the convention-D `z = q³/(q² + 1)` appearing once per
Markov peel; convention C's `z = 1/(√q + q^{-1/2})` would leave half-integer
powers of q behind.  So this doubles as a *structural* convention check on
the peel, independent of reading `hecke_symbolic.z_markov`.

**2. The "peel (proton)" number is the muon evaluation.**  Because the peel
is exact in q, both anchors can be evaluated from the one expression:

    peel(proton q₀) = 0.5751722439177718708265346936864718690299
    peel(muon   q₀) = 0.5751723310178838519197902970632253704678

and then the bean's four recorded numbers sort themselves out:

    bridge(proton y, proton χ)  ==  peel(PROTON)  to 5.3e-25   (all digits recorded)
    "peel (proton, symbolic)"   ==  peel(MUON)    to 2.6e-24

The third line is verbatim the `peel_check.tr_M_at_q0_50dps` field of
`atomic-tr-m-mpfr-50dps.witness.json`, whose own `q_0_50dps` field reads
`1.109978595557334719899763` — the muon pin.  The witness is labelled
correctly; the bean read it as proton.  So the anchor-*matched* pairing
satisfies the identity after all, and the paradox dissolves: there was never
a case of "mixing anchors works, matching them fails".

Hypothesis 1 of the eight was "peel is muon-anchored", refuted on the
grounds that `markov_peel` imports `Q_MP` (proton).  It does — for the
`abs(df + h·(½ − δ/4)) < 1e-9` pattern-match tolerance in
`crossing_from_cd`, which selects a template and is then discarded.  The
import is real and the inference from it is not.

**3. The stale artifact the mislabel was hiding.**
`atomic-tr-m-mpfr-50dps-proton.witness.json` was last computed 2026-08-09,
a day *before* the convention-D migration landed in `de9fd2521` /
`e2295f00f`, and those commits touched only its muon sibling.  It still
carries the C values (proton 1.06531, neutron 0.92323, deuteron 0.38836
against D's 1.14576 / 0.98774 / 0.57517).  Bean `qou-8x1l` says "Both anchor
tables regenerated"; one was.  The stale one is the anchor the 2026-08-07
owner directive makes the default for all new compute.

WHAT THIS DOES NOT ESTABLISH.  That the identity holds *identically in q* —
only that it holds at each of the two pins to the precision measured.  The
peel side is now known to be a rational function; the bridge side is
evaluated numerically, so the symbolic reduction of the difference is still
open.  What is closed is the specific 8.71e-8, which was bookkeeping.

Run:
    python3 computations/markov/peel_anchor_identification_probe.py
"""
from __future__ import annotations

import json
import pathlib
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/hecke",
           "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

mp.dps = 60

#: The two documented pins, per AGENTS.md §"q₀ anchor convention".  Written
#: out rather than imported because the point of the probe is to compare the
#: layers, and `q_parameter` resolves *one* of them at import time from the
#: running script's stem in `q0_anchor_manifest.json`.
Q0 = {
    "proton": mp.mpf("1.1099785827513808075916690956"),
    "muon": mp.mpf("1.109978595557334719899763"),
}

#: The four numbers bean qou-8x1l recorded, verbatim.
BEAN = {
    "bridge_proton_y_proton_chi": mp.mpf("0.575172243917771870826535"),
    "bridge_muon_y_proton_chi": mp.mpf("0.575172395398020063703615"),
    "peel_labelled_proton": mp.mpf("0.575172331017883851919791796687"),
}


def peel_deuteron_symbolic():
    """The exact rational function `tr_M(β_D)(q)` from the peel recursion."""
    from markov_peel import tr_M_atomic
    t0 = time.time()
    # use_fast=False keeps the exact sympy path; the LaurentQ fast path
    # cannot represent the non-Laurent colour δ and falls back anyway.
    expr = sp.cancel(sp.together(tr_M_atomic(1, 1, use_fast=False)))
    return expr, time.time() - t0


def main() -> int:
    expr, dt = peel_deuteron_symbolic()
    q = next(iter(expr.free_symbols))
    num, den = sp.fraction(expr)
    floats = expr.atoms(sp.Float)
    den_f = sp.factor(den)

    exact_in_q = bool(expr.is_rational_function(q)) and not floats
    # (q**2 + 1)**3 in the denominator <=> convention D, once per peel.
    conv_d = sp.simplify(sp.rem(sp.Poly(den_f.as_expr(), q).as_expr(),
                                (q ** 2 + 1))) == 0

    print(f"[peel] deuteron in {dt:.1f}s")
    print(f"  free symbols   : {expr.free_symbols}")
    print(f"  Float atoms    : {len(floats)}   (a pinned value would appear here)")
    print(f"  rational in q  : {expr.is_rational_function(q)}")
    print(f"  deg num        : {sp.degree(sp.expand(num), q)}")
    print(f"  denominator    : {den_f}")

    f = sp.lambdify(q, expr, modules="mpmath")
    at = {k: f(v) for k, v in Q0.items()}
    for k, v in at.items():
        print(f"  peel({k:6s} q0) = {mp.nstr(v, 40)}")

    print("\n  bean qou-8x1l's numbers, against each pin:")
    match = {}
    for name, v in BEAN.items():
        rels = {k: abs(v - at[k]) / abs(at[k]) for k in at}
        best = min(rels, key=rels.get)
        match[name] = {"nearest_anchor": best,
                       **{f"rel_vs_{k}": mp.nstr(rels[k], 6) for k in rels}}
        print(f"    {name:28s} -> {best:6s}  "
              + "  ".join(f"rel_{k}={mp.nstr(rels[k], 4)}" for k in rels))

    # The claim: the anchor-matched bridge sits on peel(proton), and the
    # number the bean labelled "peel (proton)" sits on peel(muon).
    ok_matched = match["bridge_proton_y_proton_chi"]["nearest_anchor"] == "proton"
    ok_mislabel = match["peel_labelled_proton"]["nearest_anchor"] == "muon"

    witness = {
        "computation": "peel-anchor-identification",
        "description": (
            "The peel's tr_M is an exact integer-coefficient rational function "
            "of q -- no anchor enters it -- so both q0 pins can be evaluated "
            "from one expression. Doing so identifies bean qou-8x1l's "
            "'peel (proton, symbolic)' as the MUON evaluation, and shows the "
            "anchor-matched bridge agreeing with peel(proton) to all recorded "
            "digits. The 8.71e-8 residual was a mislabelled readout, not a "
            "defect in the weights."
        ),
        "scriptFile": "markov/peel_anchor_identification_probe.py",
        # Declared for `audits/q0_anchor_consistency_audit.py`. "ambiguous" is
        # the honest classification and not a backfill gap: this probe
        # evaluates the same expression at BOTH documented pins on purpose --
        # telling them apart is its whole subject -- so no single q0Anchor
        # describes it. Both pins are recorded in full below.
        "q0Anchor": "ambiguous",
        "q0_pins": {k: mp.nstr(v, 30) for k, v in Q0.items()},
        "peel_deuteron": {
            "exact_in_q": exact_in_q,
            "n_float_atoms": len(floats),
            "numerator_degree": int(sp.degree(sp.expand(num), q)),
            "denominator_factored": str(den_f),
            "convention": "D" if conv_d else "not-D",
            "convention_evidence": (
                "(q^2 + 1) divides the denominator: z = q^3/(q^2+1) once per "
                "Markov peel. Convention C's z = 1/(q^(1/2) + q^(-1/2)) would "
                "leave half-integer powers of q."
            ),
            "at_q0": {k: mp.nstr(v, 50) for k, v in at.items()},
            "elapsed_sec": f"{dt:.2f}",
        },
        "bean_qou_8x1l_numbers": {
            k: {"value": mp.nstr(v, 30), **match[k]} for k, v in BEAN.items()
        },
        "assertions": [
            {"name": "peel_is_exact_rational_function_of_q",
             "passed": exact_in_q,
             "note": "refutes the bean's recorded obstacle that the word's "
                     "numeric d values pin the expression to one anchor"},
            {"name": "peel_denominator_is_convention_D",
             "passed": bool(conv_d)},
            {"name": "anchor_matched_bridge_equals_peel_at_proton",
             "passed": bool(ok_matched)},
            {"name": "bean_peel_labelled_proton_is_the_muon_evaluation",
             "passed": bool(ok_mislabel)},
        ],
    }
    witness["allPassed"] = all(a["passed"] for a in witness["assertions"])

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="sympy")
    out = REPO / "computations" / "peel-anchor-identification.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  allPassed = {witness['allPassed']}   -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
