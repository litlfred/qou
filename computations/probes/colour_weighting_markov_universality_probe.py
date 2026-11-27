#!/usr/bin/env python3
"""colour_weighting_markov_universality_probe.py — the colour-weighting price is
ONE number for the whole framework, and the reason is the Markov factorization.

WHAT THIS CORRECTS.  `colour_weighting_trace_magnitude_probe.py` (PR #6309)
measured the canonical path's colour-blindness at 1.4149e-4 relative on the
deuteron and carried an explicit scope-(a) caveat:

    "The linear coefficient tr(A B) is word-specific and is NOT measured for
     those three. Do not quote 1.41e-4 as their figure."

**That caveat is wrong.**  Measured across all four mixed nuclei, the RELATIVE
price is identical to 38 digits.  The caveat was a reasonable inference from the
affine structure -- the coefficient really is word-specific -- but the RATIO is
not, and nothing in #6309 tested it.

THE IDENTITY.  The trace is affine in the weighted crossing's shift `d`:

    tr_M(A (sigma_g + d I) B)  =  tr(A sigma_g B)  +  d * tr(A B)

Measured here: `tr(A sigma_g B) = z_D * tr(A B)` exactly, with

    z_D  =  q^3 / (q^2 + 1)        the convention-D Markov parameter

so the whole trace is proportional to `(d + z_D)`, and therefore

    Delta_rel  =  (d_w - d_blind) / (d_blind + z_D)  =  1.414946610628e-4

with NO dependence on the nucleus.  Fitting `k` from each nucleus's own two
evaluations and comparing against `z_D` computed independently from q:

    D    k - z_D =  8.2e-38        3He  k - z_D = -3.3e-37
    T    k - z_D = -5.4e-37        4He  k - z_D =  7.3e-37

spread across the four: 1.3e-36.  These are four different braid words on three
different Hecke algebras (H_6, H_9, H_12) agreeing on a constant that was never
put in.

THE MECHANISM, and the CONTROL that establishes it.  `tr_M(beta sigma) = z *
tr_M(beta)` is the Markov trace's own stabilization rule.  It should apply here
only when the weighted generator appears exactly ONCE in the word -- which,
measured, it does for all four nuclei (D and T at generator 2, 3He and 4He at
generator 5, one occurrence each).

An observed coincidence plus a plausible story is not a mechanism, so it is
tested by breaking it.  On the deuteron word:

  | word                                          | occurrences of g | k - z_D  |
  |-----------------------------------------------|------------------|----------|
  | canonical beta_D                              | 1                | -1.6e-47 |
  | beta_D + one plain sigma on the SAME generator| 2                | **1.23** |
  | beta_D + one plain sigma on ANOTHER generator | 1                |  3.1e-48 |

The identity survives lengthening the word by a crossing elsewhere and DIES when
the weighted generator is used a second time.  So the once-only occurrence is what
carries it, not the word's length or content -- and the agreement is not an
artifact of these four particular words.

WHAT THIS MEANS FOR THE DESIGN QUESTION (bean `qou-fv0s`).  The choice between
the colour-blind canonical path and the colour-weighted Python path is worth a
single, nucleus-independent 1.414946610628e-4 on every mixed nucleus -- it does
not grow with A, and it does not need re-measuring per isotope.

NOT CLAIMED.  That either arm is correct; that is a physical modelling choice.
Nor that this generalises to a word where the interface generator repeats -- the
control above shows it does not, and no canonical nucleus has that shape.

Run:  python3 -u computations/probes/colour_weighting_markov_universality_probe.py \
        2>&1 | tee /tmp/colour_weighting_markov_universality.log
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
for _p in (COMPUTATIONS, COMPUTATIONS / "hecke", COMPUTATIONS / "substrate",
           COMPUTATIONS / "deltalambda"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import rho_k_h3a_refinement as R  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings, d_for_ctype  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

NUCLEI = ((1, 1, "D"), (1, 2, "T"), (2, 1, "3He"), (2, 2, "4He"))


# The sparse column-form multiply lives in the sibling probe and is self-tested
# there against the committed dense-route deuteron values. Importing it rather
# than re-implementing keeps one routine to be wrong in, and keeps that test
# covering both probes.
from colour_weighting_across_mixed_nuclei_probe import (  # noqa: E402
    build_sparse_cache, schur_weyl_sum as _sparse_sum,
)

_CACHE: dict[int, dict] = {}


def schur_weyl_sum(q, crossings, n_strands, d_weighted):
    """Sum_lambda y_lambda chi^lambda, the weighted crossing carrying `d_weighted`.

    Dense at dim 297 (4He's largest contributing block) would be ~150x the work;
    the sparse route makes the 4He arm seconds rather than hours.
    """
    y_table = y_lambda_at(n_strands, q)
    if n_strands not in _CACHE:
        _CACHE[n_strands] = build_sparse_cache(q, y_table, n_strands)
    total, _, _ = _sparse_sum(q, crossings, y_table, _CACHE[n_strands], d_weighted)
    return total


def implied_k(q, crossings, n_strands, d_blind, d_w):
    """Fit k in `tr_M proportional to (d + k)` from the two arms.

    Sw/Sb = (d_w + k)/(d_blind + k)  =>  k = (d_w*Sb - d_blind*Sw)/(Sw - Sb).
    Nothing about z_D enters this — k is fitted from the trace alone and only
    then compared against `q^3/(q^2+1)`.
    """
    sb = schur_weyl_sum(q, crossings, n_strands, d_blind)
    sw = schur_weyl_sum(q, crossings, n_strands, d_w)
    return (d_w * sb - d_blind * sw) / (sw - sb), sb, sw


def main() -> int:
    q = Q_MP
    q_sym = sp.sympify(Q_50_DIGIT_STR)
    h = q - mp.mpf(1) / q
    delta = mp.mpf(
        str(sp.sympify(flavor_split_leading(sp.Symbol("q")))
            .subs(sp.Symbol("q"), q_sym)
            .evalf(mp.mp.dps))
    )
    d_blind = d_for_ctype("averaged", h)
    d_w = d_for_ctype("averaged_weighted", h, delta=delta)
    z_D = q ** 3 / (q ** 2 + 1)

    print("=" * 86)
    print("colour weighting — universality, and the Markov factorization behind it")
    print("=" * 86)
    print(f"\n  q_0 (proton)              = {mp.nstr(q, 40)}")
    print(f"  z_D = q^3/(q^2+1)         = {mp.nstr(z_D, 40)}")
    print(f"  d_w - d_blind             = {mp.nstr(d_w - d_blind, 30)}")
    predicted = (d_w - d_blind) / (d_blind + z_D)
    print(f"  predicted Delta_rel       = {mp.nstr(predicted, 30)}")

    w = WitnessBuilder("colour-weighting-markov-universality", engine="python")
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_data("z_D", mp.nstr(z_D, 50))
    w.add_data("d_averaged", mp.nstr(d_blind, 50))
    w.add_data("d_averaged_weighted", mp.nstr(d_w, 50))
    w.add_data("predicted_delta_relative", mp.nstr(predicted, 50))

    print(f"\n  {'atom':<6}{'H_n':>5}{'occ(g)':>8}{'delta_rel':>26}{'k - z_D':>14}")
    ks = []
    per_atom = {}
    for Z, N, label in NUCLEI:
        crossings = atom_canonical_crossings(Z, N)
        n_strands = max(g for g, _ in crossings) + 2
        gw = [g for g, c in crossings if c == "averaged_weighted"]
        occ = sum(1 for g, _ in crossings if g == gw[0])
        k, sb, sw = implied_k(q, crossings, n_strands, d_blind, d_w)
        rel = (sw - sb) / sb
        ks.append(k)
        per_atom[label] = {
            "n_strands": n_strands,
            "weighted_generator": gw[0],
            "occurrences_of_that_generator": occ,
            "delta_relative": mp.nstr(rel, 40),
            "implied_k": mp.nstr(k, 40),
            "k_minus_zD": mp.nstr(k - z_D, 12),
        }
        w.add_data(label, per_atom[label])
        print(f"  {label:<6}{n_strands:>5}{occ:>8}  {mp.nstr(rel, 22):>26}"
              f"  {mp.nstr(k - z_D, 6):>14}")
        w.add_assertion(
            f"{label}: the fitted proportionality constant IS the Markov z_D",
            computed=mp.nstr(abs(k - z_D), 30), expected="0", tolerance="1e-30",
            source="k fitted from the two trace arms; z_D computed from q alone",
        )
        w.add_assertion(
            f"{label}: the weighted generator occurs exactly once in the word",
            computed=str(occ), expected="1", tolerance="0",
            source=f"generator {gw[0]} of {len(crossings)} crossings on H_{n_strands}",
        )

    spread = max(ks) - min(ks)
    print(f"\n  spread in k across the four nuclei = {mp.nstr(spread, 8)}")
    w.add_data("k_spread_across_nuclei", mp.nstr(spread, 20))
    w.add_assertion(
        "the price is nucleus-INDEPENDENT (this is what #6309's caveat denied)",
        computed=mp.nstr(spread, 30), expected="0", tolerance="1e-30",
        source="max(k) - min(k) over D, T, 3He, 4He on H_6, H_9, H_12",
    )

    # --- the control: break the once-only occurrence and watch the identity die ---
    print("\n  CONTROL — deuteron word, perturbed:")
    base = list(atom_canonical_crossings(1, 1))
    gw = [g for g, c in base if c == "averaged_weighted"][0]
    other = next(g for g in range(0, 5) if g != gw)
    cases = [
        ("canonical beta_D", base),
        ("+1 sigma on the SAME generator", base + [(gw, "sigma")]),
        ("+1 sigma on ANOTHER generator", base + [(other, "sigma")]),
    ]
    control = {}
    for name, word in cases:
        occ = sum(1 for g, _ in word if g == gw)
        k, _, _ = implied_k(q, word, 6, d_blind, d_w)
        control[name] = {"occurrences": occ, "k_minus_zD": mp.nstr(k - z_D, 12)}
        print(f"    {name:<34} occ={occ}   k - z_D = {mp.nstr(k - z_D, 8)}")
    w.add_data("control_deuteron_perturbations", control)

    same = mp.mpf(control["+1 sigma on the SAME generator"]["k_minus_zD"])
    elsewhere = mp.mpf(control["+1 sigma on ANOTHER generator"]["k_minus_zD"])
    w.add_assertion(
        "the identity SURVIVES lengthening the word at another generator",
        computed=mp.nstr(abs(elsewhere), 30), expected="0", tolerance="1e-30",
        source="beta_D + one plain sigma on a generator the weighted crossing does not use",
    )
    w.add_assertion(
        "the identity DIES when the weighted generator is used twice",
        computed=mp.nstr(abs(same), 30), expected="1.228521", tolerance="1e-3",
        source="beta_D + one plain sigma on the SAME generator — the discriminating control",
    )

    w.add_caveat(
        "Scope: this establishes the price is nucleus-independent for words in "
        "which the interface generator occurs once — which is every canonical "
        "nucleus, measured. The control shows it does NOT hold when that "
        "generator repeats; no claim is made for such words."
    )
    w.add_caveat(
        "This prices the design choice in bean qou-fv0s; it does not settle it. "
        "Whether the p-n interface carries the flavour weighting is a physical "
        "modelling question."
    )
    w.add_caveat(
        "Supersedes the scope-(a) caveat in colour_weighting_trace_magnitude_probe.py "
        "and PR #6309, which said the 1.41e-4 figure must not be quoted for "
        "T / 3He / 4He. The coefficient is word-specific; the RATIO is not."
    )

    out = w.save()
    print(f"\n  witness -> {out}")
    failed = [a for a in w.assertions if not a.passed]
    print(f"  assertions: {len(w.assertions) - len(failed)}/{len(w.assertions)} pass")
    for a in failed:
        print(f"    FAIL  {a.name}: computed={a.computed} expected={a.expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
