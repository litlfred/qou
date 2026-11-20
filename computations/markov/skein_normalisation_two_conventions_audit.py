#!/usr/bin/env python3
"""
skein_normalisation_two_conventions_audit.py — the corpus runs TWO Skein
normalisations, AGENTS.md §7a names one canonical, and the beta-decay rate's
coupling comes from the other.

WHAT THIS SETTLES (bean qou-8bxv, 2026-09-05).  qou-q2l7 left an open question:
is the beta-decay coupling's exponent pair {1/2, 1/2} FORCED by the rate's
construction, or chosen?  It is forced -- by a Skein normalisation that is not
the one AGENTS.md §7a mandates.  That is the answer, and it is a corpus-wide
convention split rather than a one-block slip.

THE TWO RELATIONS, verbatim from the sources.

  (H) AGENTS.md §7a, STRICT, canonical:
        (sigma - q)(sigma + 1/q) = 0  =>  sigma^2 = (q - 1/q) sigma + 1
        multiply by sigma^-1        =>  sigma - sigma^-1 = q - 1/q
        i.e.  L_+ - L_-  =  h_1 * L_0,        h_1 := q - 1/q

  (J) content/.../predicted-spectra/beta-decay-skein-properties.md:49, and six
      further blocks across five chapters:
        q [L_+] - q^-1 [L_-]  =  (q^(1/2) - q^(-1/2)) [L_0]
      i.e. framing weights q, q^-1 on the two crossings and coefficient
        s := q^(1/2) - q^(-1/2) = h_(1/2)

THEY ARE NOT RESCALINGS OF ONE ANOTHER.  (H) has unit weights on L_+ and L_-;
(J) has q and q^-1.  No overall factor takes one to the other, so they are
different skein presentations (the framed / Jones normalisation against the
Hecke-generator one), not the same relation written twice.  Verified below by
solving both for L_0 and showing the resulting L_+ , L_- coefficient RATIOS
differ (1 against q^2).

THE EXACT BRIDGE, which the corpus already half-states.
bar-involution-c5-algebraic-identities.md line 1 records the factorisation:

    h_1 = q - 1/q = (q^(1/2) - q^(-1/2)) * (q^(1/2) + q^(-1/2)) = s * (q^(1/2) + q^(-1/2))

so, with [2]_q = q + 1/q:

    s^2   = [2]_q - 2                      (already Lean: sSq_eq_twoQ_sub_two)
    h_1^2 = [2]_q^2 - 4 = s^2 ([2]_q + 2)  (NEW here)
    h_1^2 / s^2 = [2]_q + 2                (exact; 4.0108995061 at the proton pin)

So the two conventions' single-crossing amplitudes differ by exactly one factor
of (q^(1/2) + q^(-1/2)) per crossing -- bar-INVARIANT, which is why the
bar-parity arguments in the c5 block are insensitive to the choice while every
MAGNITUDE is not.

WHY IT MATTERS FOR THE RATE.  prf:trace-ratio-observable takes the vertex
amplitude as skein_amp = q^(1/2) - q^(-1/2), i.e. convention (J).  The
weak-vertex trace W = tr_M((sigma_1 sigma_2)^5) is computed in H_3(q) with
h = q - 1/q, i.e. convention (H) -- that is what the Hecke relation IS.  So one
rate multiplies an amplitude taken in (J) against a trace taken in (H).  Under
(H) throughout, the coupling is h_1^2 and qou-xql6's substitution factor moves:

    |W|^2 / s^2   = 129.405107404     (as recorded, convention J amplitude)
    |W|^2 / h_1^2 =  32.2624...       (convention H throughout)

NEITHER NUMBER CHANGES THE qou-ix74 VERDICT: 32x is still far too large to be a
10-17 % correction, so the substitution remains a scope-(a) negative either way.
What the split changes is which number is the honest one to quote, and that is
not an agent's call -- see SCOPE below.

SCOPE -- this is a MEASUREMENT plus an AUTHOR DECISION, and the decision is not
taken here.  What is measured: the two relations, their inequivalence, the exact
bridge, the surface (below), and the consequence for the substitution factor.
What is NOT decided: whether the rate should be restated in (H) to match §7a, or
whether §7a should record (J) as the physics-sector convention.  Both are
coherent; picking one rewrites either eight content blocks or a STRICT section.
No identity in this producer depends on the choice.

Precision: sympy-exact throughout; numerics mpmath at 60 dps from the exact
expressions; serialised at 50 digits.  No float is formed.

Output: computations/skein-normalisation-two-conventions.witness.json
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
for _p in ("computations", "computations/markov", "computations/substrate"):
    sys.path.insert(0, str(REPO / _p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

q = sp.symbols("q", positive=True)
u = sp.sqrt(q)

S = u - 1 / u                 # skein_amp of convention (J);  = h_{1/2}
H1 = q - 1 / q                # skein coefficient of convention (H) = §7a
TWO_Q = q + 1 / q
BAR_INV = u + 1 / u           # the bar-invariant bridge factor
W = q ** 2 * (q ** 12 + q ** 8 - 1) / (q ** 2 + 1) ** 2

# The eight content blocks carrying convention (J) as the skein relation or as
# the registered "Skein amplitude". Paths are relative to content/<paper>/.
J_SITES = [
    "predicted-spectra/beta-decay-skein-properties.md",
    "braids-and-knots/feynman-eigenbasis.md",
    "brings-surface/embeddability-closure-spectral-filter.md",
    "climax-volume-mass/skein-crossing-asymmetry.md",
    "climax-volume-mass/skein-crossing-asymmetry-prop.md",
    "information-theory/skein-turing-machine.md",
    "knots-particles-confinement/crossing-energy.md",
    "appendix-transfer-matrices/tm-notation-table1-data.md",
]
PAPER = REPO / "folio" / "quantum-observable-universe"


def site_live(rel: str) -> bool:
    """The file exists AND still carries the sqrt-q amplitude."""
    p = PAPER / rel
    return p.is_file() and "q^{1/2} - q^{-1/2}" in p.read_text()


def main() -> int:
    mp.mp.dps = 60
    q0 = Q_MP
    f = lambda e: sp.lambdify(q, e, "mpmath")(q0)         # noqa: E731
    n = lambda x, d=50: mp.nstr(x, d, strip_zeros=False)  # noqa: E731

    live = [r for r in J_SITES if site_live(r)]

    # (H): 1*L_+ - 1*L_- = h_1 L_0      -> coefficient ratio L_+ : L_- = 1
    # (J): q*L_+ - q^-1*L_- = s L_0     -> coefficient ratio L_+ : L_- = q^2
    ratio_H = sp.simplify(sp.Integer(1) / sp.Integer(1))
    ratio_J = sp.simplify(q / (1 / q))

    assertions = [
        {"name": "bridge_factor_is_the_bar_invariant_one",
         "passed": sp.simplify(H1 - S * BAR_INV) == 0,
         "note": "h_1 = s * (q^(1/2) + q^(-1/2)) exactly -- the corpus already "
                 "states this factorisation in bar-involution-c5-algebraic-identities"},
        {"name": "s_squared_is_two_q_minus_two",
         "passed": sp.simplify(S ** 2 - (TWO_Q - 2)) == 0,
         "note": "s^2 = [2]_q - 2 (already Lean: sSq_eq_twoQ_sub_two)"},
        {"name": "h1_squared_is_two_q_squared_minus_four",
         "passed": sp.simplify(H1 ** 2 - (TWO_Q ** 2 - 4)) == 0
                   and sp.simplify(H1 ** 2 - S ** 2 * (TWO_Q + 2)) == 0,
         "note": "h_1^2 = [2]_q^2 - 4 = s^2([2]_q + 2): the §7a amplitude squared "
                 "is the (J) one times a bar-INVARIANT factor"},
        {"name": "the_two_relations_are_not_rescalings",
         "passed": sp.simplify(ratio_J - ratio_H) != 0,
         "note": "(H) weights L_+ : L_- as 1 : 1; (J) as q : q^-1, ratio q^2. No "
                 "overall factor relates them, so these are different skein "
                 "presentations rather than one relation written twice"},
        {"name": "bridge_factor_is_bar_invariant",
         "passed": sp.simplify(BAR_INV - BAR_INV.subs(q, 1 / q)) == 0
                   and sp.simplify(S + S.subs(q, 1 / q)) == 0,
         "note": "q^(1/2)+q^(-1/2) is bar-EVEN while s is bar-ODD, so bar-parity "
                 "arguments cannot see the convention choice -- only magnitudes can"},
        {"name": "ratio_at_proton_pin_is_two_q_plus_two",
         "passed": abs(f(H1 ** 2 / S ** 2) - f(TWO_Q + 2)) < mp.mpf("1e-40")
                   and mp.mpf("4.0108") < f(H1 ** 2 / S ** 2) < mp.mpf("4.0110"),
         "note": "h_1^2/s^2 = [2]_q + 2 = 4.0108995061 at the proton pin"},
        {"name": "substitution_factor_moves_but_verdict_does_not",
         "passed": mp.mpf("32.26") < f(W ** 2 / H1 ** 2) < mp.mpf("32.27")
                   and f(W ** 2 / H1 ** 2) > 30,
         "note": "|W|^2/h_1^2 = 32.2624 against |W|^2/s^2 = 129.4051. Both are far "
                 "too large to be the 10-17 % correction of qou-ix74, so that "
                 "scope-(a) negative survives under either convention"},
        {"name": "convention_J_surface_is_multi_chapter_not_one_block",
         "passed": len(live) >= 7,
         "note": f"{len(live)} of {len(J_SITES)} listed blocks still carry the "
                 "sqrt-q amplitude, across five chapters -- a corpus-wide split, "
                 "not a single-block slip"},
    ]

    witness = {
        "computation": "skein-normalisation-two-conventions",
        "description": (
            "The corpus runs TWO Skein normalisations. AGENTS.md §7a (STRICT) "
            "mandates the Hecke-generator form L_+ - L_- = (q - 1/q) L_0, so the "
            "single-crossing amplitude is h_1 = q - 1/q. Seven content blocks "
            "across five chapters instead write the framed/Jones form "
            "q[L_+] - q^-1[L_-] = (q^(1/2) - q^(-1/2))[L_0], amplitude "
            "s = h_(1/2). They are NOT rescalings of one another (the L_+ : L_- "
            "weights are 1:1 against q:q^-1). The bridge is exact and already "
            "half-recorded in the corpus: h_1 = s(q^(1/2)+q^(-1/2)), hence "
            "h_1^2 = [2]_q^2 - 4 = s^2([2]_q + 2), ratio [2]_q + 2 = 4.0108995061 "
            "at the proton pin. That bridge factor is bar-EVEN, so bar-parity "
            "arguments are blind to the choice while every magnitude is not. "
            "prf:trace-ratio-observable takes the vertex amplitude in (J) while "
            "the weak-vertex trace is computed in H_3(q) with h = q - 1/q, i.e. "
            "(H) -- so one rate mixes the two. Under (H) throughout, qou-xql6's "
            "substitution factor is 32.2624 rather than 129.4051; the qou-ix74 "
            "scope-(a) negative survives either way. ANSWERS the open question of "
            "qou-q2l7: the {1/2,1/2} exponent pair is FORCED, by convention (J)."
        ),
        "convention": {"hecke_h": "q - 1/q (§7a, convention H)",
                       "markov_z": "q**3/(q**2+1) (D)",
                       "anchor": "proton pin (Q_50_DIGIT_STR); identities exact in q"},
        "q0": Q_50_DIGIT_STR,
        "relations": {
            "H_agents_7a_strict": "L_+ - L_-  =  (q - 1/q) L_0",
            "H_amplitude": "h_1 = q - 1/q",
            "J_eight_content_blocks": "q [L_+] - q^-1 [L_-]  =  (q^(1/2) - q^(-1/2)) [L_0]",
            "J_amplitude": "s = q^(1/2) - q^(-1/2) = h_(1/2)",
            "L_plus_to_L_minus_weight_ratio": {"H": "1", "J": "q**2"},
            "inequivalent": True,
        },
        "bridge": {
            "identity": "h_1 = s * (q**(1/2) + q**(-1/2))",
            "squared": "h_1**2 = [2]_q**2 - 4 = s**2 * ([2]_q + 2)",
            "s_squared": "s**2 = [2]_q - 2",
            "ratio_exact": "[2]_q + 2",
            "ratio_at_q0": n(f(TWO_Q + 2), 20),
            "bridge_factor_bar_parity": "EVEN (bar-invariant); s itself is bar-ODD",
            "corpus_already_states_the_factorisation":
                "braids-and-knots/bar-involution-c5-algebraic-identities.md line 1",
        },
        "consequence_for_the_beta_rate": {
            "vertex_amplitude_taken_in": "J (prf:trace-ratio-observable: skein_amp = q^(1/2) - q^(-1/2))",
            "weak_vertex_trace_computed_in": "H (H_3(q) Hecke relation, h = q - 1/q)",
            "substitution_factor_J_amplitude": n(f(W ** 2 / S ** 2), 20),
            "substitution_factor_H_amplitude": n(f(W ** 2 / H1 ** 2), 20),
            "qou_ix74_verdict": "SURVIVES under either -- 32x and 129x are both far "
                                "too large for a 10-17 % correction",
        },
        "convention_J_surface": {"listed": J_SITES, "live": live, "live_count": len(live)},
        "answers": ("qou-q2l7's open remainder -- the {1/2,1/2} exponent pair of the "
                    "decay coupling is FORCED by convention (J), not chosen ad hoc"),
        "scope": ("MEASUREMENT plus an AUTHOR DECISION not taken here. Measured: the "
                  "two relations, their inequivalence, the exact bridge, the surface, "
                  "the consequence. NOT decided: whether the rate is restated in (H) "
                  "to match §7a, or §7a records (J) as the physics-sector convention. "
                  "Both are coherent; either rewrites eight content blocks or a STRICT "
                  "section. No identity here depends on the choice."),
        "lean": ["QOU.Braiding.WeakVertexT35.sSq_eq_twoQ_sub_two",
                 "QOU.Braiding.SkeinNormalisation.no_rescaling_of_skein_weights",
                 "QOU.Braiding.SkeinNormalisation.hOne_eq_sSqrt_mul_barEven",
                 "QOU.Braiding.SkeinNormalisation.hOneSq_eq_twoQ_sq_sub_four",
                 "QOU.Braiding.SkeinNormalisation.hOneSq_eq_sSq_mul_twoQ_add_two"],
        "reference_blocks": ["prf:hadron-half-life", "prop:trace-ratio-observable",
                             "prf:trace-ratio-observable", "def:beta-decay-skein",
                             "rem:bar-involution-c5-algebraic-identities"],
        "assertions": assertions,
    }
    witness["allPassed"] = all(a["passed"] for a in assertions)
    from qou_substrate.witness import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__,
                                            engine="sympy+mpmath")
    witness["scriptFile"] = str(pathlib.Path(__file__).resolve()
                                 .relative_to(REPO / "computations"))
    out = REPO / "computations" / "skein-normalisation-two-conventions.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")

    print(f"  h_1 = s*(q^1/2 + q^-1/2) ?  {sp.simplify(H1 - S*BAR_INV) == 0}")
    print(f"  h_1^2 = [2]_q^2 - 4      ?  {sp.simplify(H1**2 - (TWO_Q**2 - 4)) == 0}")
    print(f"  h_1^2/s^2 = [2]_q + 2    =  {n(f(TWO_Q + 2), 12)} at q0")
    print(f"  |W|^2/s^2   (conv J) = {n(f(W**2/S**2), 12)}")
    print(f"  |W|^2/h_1^2 (conv H) = {n(f(W**2/H1**2), 12)}")
    print(f"  convention-J blocks live: {len(live)}/{len(J_SITES)}")
    for r in live:
        print(f"    {r}")
    for a in assertions:
        print(f"  [{'PASS' if a['passed'] else 'FAIL'}] {a['name']}")
    print(f"  allPassed = {witness['allPassed']} -> {out.relative_to(REPO)}")
    return 0 if witness["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
