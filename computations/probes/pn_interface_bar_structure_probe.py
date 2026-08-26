#!/usr/bin/env python3
"""The bar structure of the three inter-nucleon interface factors.

# What this establishes

The canonical atomic braid assigns one factor per nearest-neighbour bond:

    f_pp = z                 (pure sigma,      positive crossing)
    f_nn = z - h             (pure sigma^-1,   negative crossing)
    f_pn = z - h/2           (strict_averaged, delta = 0)
      or   z - h(1/2 - delta/4)   (bring_color_weighted, canonical per R3)

with z = q^3/(q^2+1) (convention D), h = q - 1/q, and delta the substrate
flavour split (m_n - m_p)/M_N = (q-1)^2 (1 - q^-4)/3.

Four facts, all exact and none of them previously recorded in the corpus:

1. `bar(f_pp) = f_nn`. The p-p and n-n factors are BAR-CONJUGATES of each
   other. (`bar` is the involution q <-> 1/q.)

2. Therefore `f_pn(strict) = (f_pp + bar(f_pp)) / 2` -- the blind p-n factor
   IS the bar-symmetriser of the p-p factor, hence exactly bar-even. The name
   "uniform bar-invariant projection" in the producers is literal, not
   descriptive.

3. `f_pn(canonical) = w_p . f_pp + w_n . f_nn` with `w_p = 1/2 + delta/4`,
   `w_n = 1/2 - delta/4`, `w_p + w_n = 1`. The colour weighting is exactly a
   delta-TILT of that same mean, toward the p-p side.

   This answers a question the corpus does not: why is the colour weighting
   applied ONLY at p-n and not at p-p or n-n? Because the p-n factor IS the
   weighted mean OF the other two. A like-flavour bond has no mean to tilt --
   averaging f_pp with itself returns f_pp for any weights summing to one, so
   "colour-averaging the p-p bond" is a no-op by construction.

4. **The canonical form is NOT bar-invariant.** `delta` is bar-mixed
   (`bar(delta) = -q^2 . delta`), and

       bar(f_canonical) - f_canonical = (q-1)^5 (q+1)^3 (q^2+1) / (12 q^5)

   which is nonzero for q != 1 (1.67e-05 at the proton pin).

# Why fact 4 matters

`content/quantum-observable-universe/mass-theory/pn-averaging-uniqueness.md`
(`prop:pn-averaging-uniqueness`) states:

    "The two production candidates are the uniform bar-invariant form and the
     Bring color-tube weighted form. Both satisfy bar-invariance and standard
     normalisation."

Bar-invariance is hypothesis (a) of its own uniqueness theorem. Measured here,
the colour-weighted candidate does **not** satisfy it.

The **Lean is not affected**: `pn_averaging_unique` is the section-3b-cond
conditional-class pattern (`BarInvariant`, `StandardNorm`,
`ColorFlavorCompatible` as instance hypotheses), so it proves the implication
and says nothing about which candidate discharges it. The defect is the prose
restating the antecedent as established for both -- the
"conditional-proved != premise-established" pattern in AGENTS.md.

Consequence, stated as scope rather than resolved here: the uniqueness
proposition covers the bar-invariant family; the convention the owner made
canonical on 2026-08-15 (R3) sits OUTSIDE its hypotheses. Whether the right
move is to relax hypothesis (a), or to re-derive the colour weighting in a
bar-invariant form, or to accept that canonicity and bar-invariance part ways
here, is an owner call and is not made by this probe.

No float64 anywhere: exact sympy throughout, evaluated only for display.
"""
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import json  # noqa: E402
import time  # noqa: E402

import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

_HERE = _Path(__file__).resolve().parent

Q = sp.Symbol("q", positive=True)
H = Q - 1 / Q
Z = Q ** 3 / (Q ** 2 + 1)                       # convention D
DELTA = (Q - 1) ** 2 * (1 - Q ** -4) / 3        # flavor_split_leading
Q0 = sp.Float(Q_50_DIGIT_STR, 50)

F_PP = Z
F_NN = Z - H
F_PN_STRICT = Z - H / 2
F_PN_CANON = Z - H * (sp.Rational(1, 2) - DELTA / 4)

W_P = sp.Rational(1, 2) + DELTA / 4
W_N = sp.Rational(1, 2) - DELTA / 4


def bar(expr):
    """The bar involution q <-> 1/q."""
    return sp.simplify(expr.subs(Q, 1 / Q))


def main() -> int:
    started = time.monotonic()
    w = WitnessBuilder("pn-interface-bar-structure", engine="sympy",
                       output_dir=_HERE, start_time=started)
    w.set_description(
        "Exact bar structure of the three inter-nucleon interface factors: "
        "f_pp and f_nn are bar-conjugates, the strict_averaged p-n factor is "
        "their bar-symmetriser (exactly bar-even), and the canonical "
        "colour-weighted p-n factor is their delta-tilted mean and is NOT "
        "bar-invariant -- contradicting a prose claim in "
        "prop:pn-averaging-uniqueness that both candidates satisfy its "
        "hypothesis (a)."
    )
    w.set_content_block("prop:pn-averaging-uniqueness")
    w.add_parameter("q0", str(Q0))
    w.add_parameter("q0Anchor", "proton")

    checks = [
        ("f_nn_is_bar_conjugate_of_f_pp", bar(F_PP) - F_NN),
        ("strict_pn_is_the_bar_symmetriser", F_PN_STRICT - (F_PP + bar(F_PP)) / 2),
        ("strict_pn_is_bar_even", bar(F_PN_STRICT) - F_PN_STRICT),
        ("canonical_pn_is_the_delta_tilted_mean", F_PN_CANON - (W_P * F_PP + W_N * F_NN)),
        ("tilt_weights_sum_to_one", W_P + W_N - 1),
    ]
    for name, residual in checks:
        r = sp.simplify(residual)
        print(f"  {name:42s} residual = {r}", flush=True)
        w.add_assertion(name, str(r), "0")

    # The one that does NOT vanish.
    bar_defect = sp.factor(sp.simplify(bar(F_PN_CANON) - F_PN_CANON))
    at_q0 = sp.N(bar_defect.subs(Q, Q0), 20)
    print(f"\n  canonical bar defect = {bar_defect}", flush=True)
    print(f"  at q0                = {sp.N(at_q0, 8)}", flush=True)
    w.add_assertion("canonical_pn_is_NOT_bar_even", str(bar_defect != 0), "True",
                    source="bar(f) - f = (q-1)^5 (q+1)^3 (q^2+1) / (12 q^5)")
    w.add_assertion("canonical_bar_defect_at_q0", str(at_q0), "0.0000166849",
                    tolerance="1e-9")
    w.add_assertion("delta_is_bar_mixed",
                    str(sp.simplify(bar(DELTA) / DELTA)), "-q**2",
                    source="bar(delta) = -q^2 . delta")

    w.add_data("factors", {
        "f_pp": str(F_PP), "f_nn": str(F_NN),
        "f_pn_strict_averaged": str(F_PN_STRICT),
        "f_pn_bring_color_weighted": str(F_PN_CANON),
        "tilt_weight_p": str(sp.simplify(W_P)),
        "tilt_weight_n": str(sp.simplify(W_N)),
        "canonical_bar_defect": str(bar_defect),
    })
    w.add_caveat(
        "SCOPE (a) in the AGENTS.md sense: this is a scope-limited negative "
        "about ONE stated property of ONE convention. It does not say the "
        "colour weighting is wrong, and it does not say the owner's 2026-08-15 "
        "R3 ruling should be revisited. It says the uniqueness proposition's "
        "hypothesis (a) is not satisfied by the colour-weighted candidate, so "
        "that proposition does not cover it."
    )
    w.add_caveat(
        "The Lean of prop:pn-averaging-uniqueness is UNAFFECTED. It is the "
        "conditional-class pattern and proves only the implication. Do not "
        "read this probe as finding a defect in pn_averaging_unique."
    )

    path = w.save()
    built = json.loads(_Path(path).read_text())
    print(f"\nwitness -> {path}\nallPassed = {built['allPassed']} "
          f"({len(built['assertions'])} assertions)", flush=True)
    return 0 if built["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
