#!/usr/bin/env python3
"""The negative `(1^3)` weight is an INTERVAL fact — and it deflates two of the
corpus's own findings, including one of mine. (bean `qou-cds1`.)

## What was claimed, twice

`QOU.QBeta.AdmissibleRoots.one_not_root` proves the `(1^3)`-block Ocneanu weight
numerator is nonzero at `z = 1`, and two probes then read its *negative value*
as a finding about a distinguished point:

  * `qbeta-admissibility-is-a-magnitude` (2026-08-30) records
    `y_(1^3)(z=1) = -0.0139947872229` at the proton pin;
  * PR #6340 (2026-08-31, mine) reports `y_(1^3)(z*) = -0.014131` at the `z*`
    the Q_beta inversion demands and calls it "a sign violation, not a small
    perturbation, so no positive-weight trace in this family reaches it".

## What is actually true

`wtNumer(q,z) = (z - q)*((q^2+1)*z - q^3)` is an UPWARD PARABOLA in `z` whose
two real roots are exactly the two admissible Markov parameters `z_D < q`. So it
is negative on the whole open interval `(z_D, q)` and positive outside — proved
here in Lean, unconditionally:

    QOU.QBeta.AdmissibleRoots.zD_lt_self            z_D < q  for every q > 0
    QOU.QBeta.AdmissibleRoots.sub_zD_eq             q - z_D = q/(q^2+1)
    QOU.QBeta.AdmissibleRoots.wtNumer_neg_of_between  z_D < z < q  =>  wtNumer < 0
    QOU.QBeta.AdmissibleRoots.wtNumer_pos_of_lt_zD     z < z_D      =>  wtNumer > 0
    QOU.QBeta.AdmissibleRoots.one_not_root_of_interval one_not_root as a COROLLARY

The interval has width `q/(q^2+1) = 0.497` at the pin. `z = 1` and `z*` both lie
in it, 0.15 % apart. So the two negative values above are ONE fact, they are not
about the points they were measured at, and neither carries information beyond
`z in (z_D, q)`. My #6340 framing overstated its own; this records that.

## Convention C sits on the OTHER side, for every q > 1

`z_C = sqrt(q)/(q+1) < z_D` for every `q > 1`, so `wtNumer(q, z_C) > 0` — proved
here as `zC_lt_zD` / `zC_not_root`. The corpus carried only the point
measurement (`three_row_share` 3.16 % at the pin, sign discarded). Two
consequences:

  * convention C's Markov parameter is inadmissible on the WHOLE substrate
    window, not merely at the pin — sympy independently gives the only roots of
    `wtNumer(q, z_C)` as `q = 1` and the real root of `x^3 + 2x^2 + x - 1`
    (~0.4656), neither on the window; and
  * the counit `z = 1` (the ladder's base) and convention C lie on OPPOSITE
    sides of the admissible set. The ladder's base has never descended to the
    two-row quotient under EITHER convention, so "re-derive under D" is not a
    change of frame that repairs admissibility.

## A denominator defect found on the way, in the Lean this probe cites

`ConventionDAdmissibleRoots`'s module docstring stated
`y_(1^3)(z) = q^2 N(q,z)/(q^4+q^2+1)`. The denominator is short by `(q^2+1)`
(`2.232` at the pin); the weight is `q^2 N/((q^2+1)(q^4+q^2+1))`. Reading the
docstring is how this probe first got `y_(1^3)(1) = -0.03124` against the
committed `-0.0139948`.

**No theorem in that file changes** -- every result there is about `wtNumer`, the
numerator, and both candidate denominators are strictly positive over `R`, so the
root set, the completeness `iff` and `one_not_root` are untouched. Only a
consumer that computes from the stated formula is affected.

Three corpus sources already carried the correct form (`schurweyl/
ocneanu_weight_general_n.py::PROVED3`, the `y_111_symbolic` of
`qbeta-admissibility-is-a-magnitude.witness.json`, and the symbolic-`z` Borromean
Markov solve). Consensus is not a derivation, so this probe pins it instead by
the defining normalisation `sum_lambda dim(lambda) W_lambda = 1` at `n = 3`,
which holds for `(q^2+1)(q^4+q^2+1)` and FAILS for `q^4+q^2+1` -- decisive rather
than majoritarian.

## Scope

(a) Structural, and DEFLATIONARY: it removes content from two prior claims and
adds the all-`q` convention-C statement. It does NOT exclude the decay base —
`QOU.QBeta.DecayFibreBarParity` already records that the two-row cap is the MASS
channel's forcing and that transporting it to the decay channel rests on the
2026-08-15 owner ruling, not a theorem. Nothing wired; free_parameters = 0.

-- Ref: [manuscript] QOU.QBeta.AdmissibleRoots (all five lemmas above, sorry-free)
-- Ref: [manuscript] computations/qbeta/qbeta_admissibility_is_a_magnitude_probe.py
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors",
--      Invent. Math. 92 (1988) 349-383.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate"),
                str(_COMP.parent / "tools" / "qou-substrate" / "python")]
import _path_bridge  # noqa: F401,E402

mp.mp.dps = 60


def _fmt(x, n=20):
    return mp.nstr(x, n)


def main() -> int:
    from q_parameter import Q_MP  # exact mpf, proton pin (owner directive)
    q = mp.mpf(Q_MP)
    zD = q ** 3 / (q ** 2 + 1)
    zC = mp.sqrt(q) / (q + 1)
    # y_(1^3) denominator: (q^2+1)(q^4+q^2+1) = q^6+2q^4+2q^2+1. NOT q^4+q^2+1 --
    # the ConventionDAdmissibleRoots docstring said the latter and was short by
    # (q^2+1); corrected in this PR. Two independent corpus derivations agree on
    # this form (the admissibility-is-a-magnitude witness's y_111_symbolic and the
    # symbolic-z Borromean Markov solve).
    den = (q ** 2 + 1) * (q ** 4 + q ** 2 + 1)

    def wt(z):
        return (q ** 2 + 1) * z ** 2 - (2 * q ** 3 + q) * z + q ** 4

    def y111(z):
        return q ** 2 * wt(z) / den

    width = q - zD
    width_closed = q / (q ** 2 + 1)

    # z* : the Markov parameter the Q_beta inversion demands. g_required is
    # F_required(augmentation) from the PROTON-pinned correction-search witness
    # (qbeta-d-frame-admissible-base-correction-search, 2026-08-29), and this
    # probe is proton throughout -- so unlike PR #6340, no layer is straddled.
    g_req = mp.mpf("0.88912581036021176")           # = F_required(aug), proton
    h = q - 1 / q
    # g(z) = tr_M(Delta_S)(z)/tr_M(Delta_S)(q) = (h/2 - z)/(h/2 - q)
    z_star = h / 2 - g_req * (h / 2 - q)

    pts = [
        ("z_C  (convention C)", zC),
        ("z_D  (convention D / Wenzl r=2)", zD),
        ("z*   (Q_beta inversion)", z_star),
        ("z=1  (counit / ladder base)", mp.mpf(1)),
        ("z=q  (augmentation)", q),
    ]
    print(f"q0 = {_fmt(q, 30)}")
    print(f"admissible roots: z_D = {_fmt(zD, 18)},  q = {_fmt(q, 18)}")
    print(f"interval width q - z_D = {_fmt(width, 18)}  (closed form q/(q^2+1) = {_fmt(width_closed, 18)})")
    print()
    for name, z in pts:
        inside = zD < z < q
        print(f"  {name:34s} z={_fmt(z, 16):>20s}  wtNumer={_fmt(wt(z), 12):>16s}"
              f"  y_(1^3)={_fmt(y111(z), 12):>16s}  in(z_D,q)={inside}")

    # --- the deflation, stated as a number -------------------------------------
    y1, ys = y111(mp.mpf(1)), y111(z_star)
    sep = abs(z_star - 1)
    print(f"\n[deflation] |z* - 1|/1 = {_fmt(sep * 100, 6)} %   "
          f"y_(1^3)(1) = {_fmt(y1, 12)}   y_(1^3)(z*) = {_fmt(ys, 12)}")
    print("  both negative for the SAME reason: both lie in (z_D, q).")

    # --- the denominator, pinned by the normalisation identity ------------------
    # Three corpus sources give y_(1^3) with denominator (q^2+1)(q^4+q^2+1) while
    # the ConventionDAdmissibleRoots docstring said q^4+q^2+1. Consensus is not a
    # derivation, so pin it by the defining condition instead: the Ocneanu weights
    # satisfy sum_lambda dim(lambda) * W_lambda = 1 (tr_M(1) = 1). At n = 3 the
    # dimensions are (1, 2, 1). Only one of the two denominators can satisfy it.
    qs2, zs2 = sp.Symbol("q"), sp.Symbol("z")
    d2, d3 = qs2 ** 2 + 1, qs2 ** 4 + qs2 ** 2 + 1
    W3 = (qs2 * zs2 + 1) * (qs2 ** 3 * zs2 + qs2 * zs2 + 1) / (d2 * d3)
    W21 = -qs2 * (zs2 - qs2) * (qs2 * zs2 + 1) / d3
    W111 = qs2 ** 2 * (zs2 - qs2) * (zs2 * (qs2 ** 2 + 1) - qs2 ** 3) / (d2 * d3)
    norm_ok = sp.simplify(W3 + 2 * W21 + W111 - 1) == 0
    W111_doc = qs2 ** 2 * ((qs2 ** 2 + 1) * zs2 ** 2 - (2 * qs2 ** 3 + qs2) * zs2
                           + qs2 ** 4) / d3
    norm_doc = sp.simplify(W3 + 2 * W21 + W111_doc - 1) == 0
    print(f"\n[denominator] sum_lam dim*W = 1 with (q^2+1)(q^4+q^2+1): {norm_ok}")
    print(f"[denominator] same with the docstring's q^4+q^2+1:        {norm_doc}")

    # --- convention C, all q ---------------------------------------------------
    qs, zs = sp.Symbol("q", positive=True), sp.Symbol("z")
    zCs = sp.sqrt(qs) / (qs + 1)
    Nc = sp.simplify(sp.radsimp(
        (qs ** 2 + 1) * zCs ** 2 - (2 * qs ** 3 + qs) * zCs + qs ** 4))
    roots = sp.solve(sp.Eq(Nc, 0), qs)
    print(f"\n[convention C, all q] wtNumer(q, z_C) = 0  only at q in {roots}")
    print("  neither is on the substrate window (1 < q < plastic ~ 1.4656).")

    try:
        from witness_base import WitnessBuilder
    except Exception:
        print("(witness_base unavailable — printing only)")
        return 0

    w = WitnessBuilder("qbeta-three-row-weight-sign-is-an-interval", engine="mpmath+sympy")
    w.set_description(
        "bean qou-cds1: the negative (1^3) Ocneanu weight is an INTERVAL fact, not a "
        "point fact. wtNumer = (z-q)((q^2+1)z-q^3) is an upward parabola with roots "
        "exactly the two admissible Markov parameters z_D < q, so it is negative on "
        "ALL of (z_D, q) (width q/(q^2+1) = 0.497 at the pin) and positive outside. "
        "DEFLATES two prior readings of its value at a point — y_(1^3)(z=1) = -0.01399 "
        "(qbeta-admissibility-is-a-magnitude, 2026-08-30) and y_(1^3)(z*) = -0.014131 "
        "(PR #6340, mine) — which are one fact and carry no information beyond "
        "z in (z_D, q). ADDS: z_C < z_D for every q > 1, so convention C's Markov "
        "parameter is inadmissible on the whole window (sympy: wtNumer(q,z_C)=0 only "
        "at q=1 or the root of x^3+2x^2+x-1), and the counit z=1 lies on the OPPOSITE "
        "side of the admissible set from convention C — the ladder's base never "
        "descended to the two-row quotient under either convention. Lean-proved "
        "sorry-free: zD_lt_self, sub_zD_eq, wtNumer_neg_of_between, "
        "wtNumer_pos_of_lt_zD, one_not_root_of_interval (one_not_root as a corollary), "
        "zC_lt_zD, zC_not_root. Scope-(a), deflationary; nothing wired; the decay "
        "base is NOT excluded here (DecayFibreBarParity: the cap is the mass "
        "channel's forcing)."
    )
    w.set_content_block("conj:binding-qbeta-complex-volume")
    w.add_data("q0", _fmt(q, 30))
    w.add_data("q0Anchor", "proton")
    w.add_data("z_D", _fmt(zD, 25))
    w.add_data("z_C", _fmt(zC, 25))
    w.add_data("z_star", _fmt(z_star, 25))
    w.add_data("interval_width", _fmt(width, 25))
    w.add_data("interval_width_closed_form", "q/(q^2+1)")
    w.add_data("y_111_at_z1", _fmt(y111(mp.mpf(1)), 20))
    w.add_data("y_111_at_z_star", _fmt(ys, 20))
    w.add_data("y_111_at_zC", _fmt(y111(zC), 20))
    w.add_data("z_star_vs_one_pct", _fmt(sep * 100, 10))
    w.add_data("g_required_source", "qbeta-d-frame-admissible-base-correction-search "
               "F_required_augmentation (proton pin); no layer straddle")
    w.add_data("wtNumer_zC_zero_only_at", [sp.srepr(r) for r in roots])
    w.add_data("counit_and_conventionC_on_opposite_sides", True)
    w.add_data("y111_denominator", "(q^2+1)(q^4+q^2+1) = q^6+2q^4+2q^2+1")
    w.add_data("lean_docstring_denominator_was_short_by", "(q^2+1)")
    w.add_data("free_parameters", 0)

    w.add_assertion(
        "interval_width_matches_closed_form",
        computed=_fmt(abs(width - width_closed), 12), expected="0",
        tolerance="1e-40",
        source="q - z_D = q/(q^2+1)  (Lean sub_zD_eq)")
    w.add_assertion(
        "z1_and_zstar_both_inside_admissible_interval",
        computed=1 if (zD < 1 < q and zD < z_star < q) else 0, expected=1,
        source="both negatives are the same interval fact (Lean wtNumer_neg_of_between)")
    w.add_assertion(
        "zC_strictly_left_of_zD",
        computed=1 if zC < zD else 0, expected=1,
        source="convention C lies outside the admissible interval (Lean zC_lt_zD)")
    w.add_assertion(
        "zC_weight_positive_counit_weight_negative",
        computed=1 if (y111(zC) > 0 and y111(mp.mpf(1)) < 0) else 0, expected=1,
        source="opposite sides of the admissible set (Lean zC_not_root vs one_not_root)")
    w.add_assertion(
        "y111_denominator_pinned_by_normalisation",
        computed=1 if (norm_ok and not norm_doc) else 0, expected=1,
        source="sum_lambda dim(lambda) W_lambda = 1 at n=3 holds for denominator "
               "(q^2+1)(q^4+q^2+1) and FAILS for the docstring's q^4+q^2+1")
    w.add_assertion(
        "conventionC_not_a_root_for_any_window_q",
        computed=1 if not any(
            sp.re(sp.N(r)) > 1 and sp.re(sp.N(r)) < sp.Rational(14656, 10000)
            for r in roots) else 0,
        expected=1,
        source="sympy: wtNumer(q,z_C)=0 only at q=1 or root(x^3+2x^2+x-1); "
               "neither on 1 < q < plastic")

    out = w.save()
    print(f"witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
