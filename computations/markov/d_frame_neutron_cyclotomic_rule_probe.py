#!/usr/bin/env python3
"""
d_frame_neutron_cyclotomic_rule_probe.py — the per-neutron `(q^2+1)^2`
cancellation fires iff some generator carries TWO OR MORE averaged crossings.

WHAT THIS SETTLES.  The residue of `qou-cxon` Q2.  Measured in
`d_frame_cyclotomic_exponent_probe`: under `bring_color_weighted` at
convention D a lone NEUTRON's trace denominator carries no power of
`(q^2 + 1)` at all, while a lone PROTON's carries 2.  Both are 3-strand words
with z-count `m = 2`.  This probe finds the rule behind that asymmetry.

## The two words

Both are 11 crossings, every `c = 1`, every `d` drawn from the three canonical
templates `{0, -h, -h/2}` with `h = q - q^-1`:

    proton   gen0 [zero zero zero zero  avg zero zero]   gen1 [full full full  avg]
    neutron  gen0 [zero zero zero  avg  avg zero zero]   gen1 [full full full full]

    proton  : 6 zero, 2 avg, 3 full  ->  (q^2+1)^2, cancelled 0
    neutron : 5 zero, 2 avg, 4 full  ->  (q^2+1)^0, cancelled 2

## The rule, and two count-matched controls that establish it

Composition does NOT determine the outcome.  Two variants settle that, in
opposite directions:

  * a proton word with ONE `zero -> full` has EXACTLY the neutron's
    composition (5 zero, 2 avg, 4 full) and still cancels **0**;
  * a neutron word with ONE `full -> zero` has EXACTLY the proton's
    composition (6 zero, 2 avg, 3 full) and still cancels **2**.

What separates every configuration is where the AVERAGED crossings sit:

    g0avg g1avg | cancelled
        1     1 |     0        <- proton
        2     0 |     2        <- neutron
        1     0 |     0
        0     0 |     0
        0     2 |     2
        3     0 |     2
        2     1 |     2

**Cancellation fires iff `max(g0avg, g1avg) >= 2`** — some single generator
carrying two or more averaged crossings.  It is not gen0-specific: two
averaged on gen1 cancels exactly as two on gen0 does.  And it SATURATES: three
averaged on one generator still cancels 2, not 3.

## Reading it

An averaged crossing is `sigma + d`, `d = -h/2`; two of them on the SAME
generator multiply to a quadratic in that generator, which the Hecke relation
`sigma^2 = h*sigma + 1` collapses -- and the collapse is what supplies the
`(q^2+1)^2` the denominator then loses.  Two averaged crossings on DIFFERENT
generators never meet under that relation, so nothing collapses.

Physically this is the isospin content: the neutron (udd) puts both of its
averaged ud-couplings on one generator; the proton (uud) spreads its two
across both.  The p/n asymmetry in cyclotomic content is that placement, not a
difference in how many couplings each nucleon has -- both have exactly two.

## Scope

Scope-(a): a measurement of these twelve 3-strand configurations under
`bring_color_weighted` at convention D.  The reading in the previous section
is an INTERPRETATION of the rule, not a proof of it; the falsifiable content
is the `max(g0avg, g1avg) >= 2` criterion and its saturation.

Exact symbols throughout; no float is formed in any measured quantity (the
`d` templates are numeric only so that `crossing_from_cd` can RECOGNISE which
template a crossing is -- it then substitutes the symbolic form, so every
number below is a polynomial degree or a factor multiplicity).

Output: `d-frame-neutron-cyclotomic-rule.witness.json`.
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
import hecke_symbolic as hs  # noqa: E402

q = hs.q
PHI_D = q ** 2 + 1
Z_D = q ** 3 / PHI_D
ZSYM = sp.Symbol("Zsym")
hs.z_markov = ZSYM


def main() -> int:
    from hecke_core import h as _h_num
    import markov_peel as mkp
    from markov_trace_canonical import tr_M_element
    from mass_at_3A_proper import atom_braid_word_3A

    hn = float(_h_num)
    ZERO, FULL, AVG = 0.0, -hn, -hn / 2

    def measure(word):
        div = mkp.SymbolicHeckeDivision()
        nf = mkp.incremental_reduced_element(
            word, div=div, max_iterations_per_step=10000)
        tr = sp.sympify(tr_M_element(nf, 3, simplify=False))
        m = sp.Poly(sp.expand(sp.numer(sp.cancel(sp.together(tr)))),
                    ZSYM).degree()
        sub = sp.cancel(sp.together(tr.subs(ZSYM, Z_D)))
        act = sum(e for b, e in sp.factor_list(
            sp.expand(sp.fraction(sub)[1]))[1] if sp.expand(b) == PHI_D)
        return int(m), int(act)

    def build(g0, g1):
        return [(1.0, d, 0) for d in g0] + [(1.0, d, 1) for d in g1]

    P0 = [ZERO] * 4 + [AVG] + [ZERO] * 2
    P1 = [FULL] * 3 + [AVG]
    N0 = [ZERO] * 3 + [AVG, AVG] + [ZERO] * 2
    N1 = [FULL] * 4

    CASES = [
        ("proton (real word)", P0, P1),
        ("neutron (real word)", N0, N1),
        ("proton + gen1 avg->full", P0, [FULL] * 4),
        ("proton + one gen0 zero->full",
         [ZERO] * 3 + [FULL] + [AVG] + [ZERO] * 2, P1),
        ("neutron - one gen1 full->zero", N0, [FULL] * 3 + [ZERO]),
        ("proton, avg moved gen1->gen0",
         [ZERO] * 3 + [AVG, AVG] + [ZERO] * 2, [FULL] * 3 + [ZERO]),
        ("2 avg on gen1", [ZERO] * 7, [FULL, FULL, AVG, AVG]),
        ("2 avg on gen0", [ZERO] * 5 + [AVG, AVG], [FULL] * 4),
        ("1 avg each", [ZERO] * 6 + [AVG], [FULL] * 3 + [AVG]),
        ("0 avg anywhere", [ZERO] * 7, [FULL] * 4),
        ("3 avg on gen0", [ZERO] * 4 + [AVG] * 3, [FULL] * 4),
        ("2 avg gen0 + 1 gen1", [ZERO] * 5 + [AVG, AVG], [FULL] * 3 + [AVG]),
    ]

    # sanity: the two "real word" cases must match the production builder
    real_ok = True
    for label, Z, N in [("proton", 1, 0), ("neutron", 0, 1)]:
        prod = measure(atom_braid_word_3A(Z, N))
        mine = measure(build(*(P0, P1) if Z else (N0, N1)))
        real_ok = real_ok and (prod == mine)

    rows = []
    print(f"{'variant':32s} | {'g0avg':>5s}{'g1avg':>5s} | {'m':>2s} "
          f"{'(q2+1)^':>7s} {'cancel':>6s} {'rule':>5s}")
    for name, g0, g1 in CASES:
        t0 = time.time()
        m, act = measure(build(g0, g1))
        g0a, g1a = g0.count(AVG), g1.count(AVG)
        pred = 2 if max(g0a, g1a) >= 2 else 0
        rows.append({
            "variant": name, "gen0_avg": g0a, "gen1_avg": g1a,
            "zero": (g0 + g1).count(ZERO), "avg": g0a + g1a,
            "full": (g0 + g1).count(FULL),
            "z_count_m": m, "phi_power": act, "cancelled": m - act,
            "rule_prediction": pred, "rule_holds": bool(m - act == pred),
            "elapsed_sec": f"{time.time() - t0:.2f}",
        })
        print(f"{name:32s} | {g0a:5d}{g1a:5d} | {m:2d} {act:7d} "
              f"{m-act:6d} {pred:5d}", flush=True)

    # the two count-matched controls, named explicitly
    by = {r["variant"]: r for r in rows}
    ctrl_a = by["proton + one gen0 zero->full"]
    ctrl_b = by["neutron - one gen1 full->zero"]
    prot, neut = by["proton (real word)"], by["neutron (real word)"]

    assertions = [
        {"name": "real_words_reproduce_production_builder",
         "passed": bool(real_ok),
         "note": "the hand-built proton/neutron template lists give the same "
                 "measurement as atom_braid_word_3A(Z, N)"},
        {"name": "rule_holds_on_all_twelve",
         "passed": all(r["rule_holds"] for r in rows),
         "note": "cancellation = 2 iff max(gen0_avg, gen1_avg) >= 2, else 0"},
        {"name": "composition_does_not_determine_outcome",
         "passed": bool(
             (ctrl_a["zero"], ctrl_a["avg"], ctrl_a["full"]) ==
             (neut["zero"], neut["avg"], neut["full"]) and
             ctrl_a["cancelled"] != neut["cancelled"] and
             (ctrl_b["zero"], ctrl_b["avg"], ctrl_b["full"]) ==
             (prot["zero"], prot["avg"], prot["full"]) and
             ctrl_b["cancelled"] != prot["cancelled"]),
         "note": "two count-matched controls in OPPOSITE directions: a proton "
                 "word with the neutron's exact composition still cancels 0, "
                 "and a neutron word with the proton's exact composition "
                 "still cancels 2"},
        {"name": "not_gen0_specific",
         "passed": bool(by["2 avg on gen1"]["cancelled"] == 2),
         "note": "two averaged on gen1 cancels exactly as two on gen0"},
        {"name": "cancellation_saturates_at_two",
         "passed": bool(by["3 avg on gen0"]["cancelled"] == 2),
         "note": "three averaged on one generator still cancels 2, not 3"},
    ]

    witness = {
        "computation": "d-frame-neutron-cyclotomic-rule",
        "description": (
            "The per-neutron (q^2+1)^2 cancellation in the convention-D "
            "atomic Markov trace fires iff SOME GENERATOR carries two or "
            "more averaged crossings. Twelve 3-strand configurations; the "
            "rule holds on all twelve. Composition does not determine the "
            "outcome: a proton word with the neutron's exact template "
            "composition still cancels 0, and a neutron word with the "
            "proton's still cancels 2. Not gen0-specific (two averaged on "
            "gen1 behaves identically) and it saturates (three on one "
            "generator still cancels 2). The physical content is isospin "
            "placement: the neutron (udd) puts both averaged ud-couplings on "
            "one generator, the proton (uud) spreads its two across both -- "
            "both nucleons have exactly two. The Hecke-collapse reading in "
            "the docstring is an INTERPRETATION; the falsifiable content is "
            "the max(g0avg,g1avg) >= 2 criterion and its saturation. "
            "Scope-(a): these twelve configurations under "
            "bring_color_weighted at convention D."
        ),
        "convention": {
            "markov_z": "q**3/(q**2 + 1)   (convention D, canonical per R1)",
            "pn_convention": "bring_color_weighted (canonical per R3)",
            "anchor": (
                "NONE enters: every measured number is a polynomial degree "
                "or a factor multiplicity. The numeric d templates exist "
                "only so crossing_from_cd can recognise which template a "
                "crossing is; it substitutes the symbolic form. Top-level "
                "q0Anchor/q0Value are the ambient WitnessBuilder stamp."
            ),
        },
        "reference_blocks": ["def:markov-trace",
                             "def:hecke-quadratic-relation",
                             "prop:atomic-braid-decomposition"],
        "variants": rows,
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)

    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="sympy")
    # stamp_staleness_metadata does NOT set scriptFile; without it the witness
    # lands in witness_provenance_audit's PROV_MISSING list.
    witness["scriptFile"] = str(
        pathlib.Path(__file__).resolve().relative_to(
            REPO / "computations"))
    out = REPO / "computations" / "d-frame-neutron-cyclotomic-rule.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  allPassed = {witness['allPassed']}   "
          f"-> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
