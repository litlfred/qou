#!/usr/bin/env python3
"""mu_p_habiro_basis_order_probe.py — the Habiro basis IS the bar-even tower,
and the orders that bracket the mu-p residual.

BEAN `qou-6gf9`. Successor to `mu_p_cyclotomic_ladder_magnitude_probe.py`, which
closed the 4_1 cyclotomic ladder (floor 5430x the residual). Source for the
Sigma(2,3,5) series: `library/arxiv-2605.15740v1` (Lovejoy, Osburn & Storzer,
*Bailey pairs, Eichler integrals and unified WRT invariants*), registered as
`lovejoy2026` in `content/schema/references.ts` at intake and — until now —
cited nowhere in the corpus.

## Result 1 (structural, exact): the bar-even precondition is FREE in the Habiro ring

The corpus's standing precondition on a mu-p correction is that it be bar-even
(`q -> q^-1` fixed), and that precondition is *argued* from the amphichirality
of 4_1, never proved (`MuPCorrectionAdmissibility` says so explicitly, and
every exclusion drawn from it is conditional on it).

The Habiro basis makes it automatic. With `(a)_n = (a;q)_n = prod (1 - a q^{k-1})`,

    (q;q)_n * (q^-1;q^-1)_n = prod_{j=1..n} (1 - q^j)(1 - q^-j)
                            = prod_{j=1..n} (2 - q^j - q^-j)
                            = (-1)^n prod_{j=1..n} f_j,    f_j := q^j + q^-j - 2

which is *identically* the bar-even tower of `MuPCarrierBarParity` — `f_1 = w`
and `f_j = j^2 w + O(w^2)`. So a Habiro-ring element expanded in its own basis
is bar-even term by term, with no appeal to the carrier's symmetry at all.
Verified here to 8e-52 at an off-anchor point.

## Result 2 (magnitude): six consecutive orders bracket the residual

Required coefficient `t / |omega_n|` at the proton pin, `omega_n` the basis
element above:

    n     |omega_n|      t/|omega_n|
    5     2.315e-6       0.0912
    6     9.373e-7       0.2253   <- small height
    7     5.226e-7       0.4040   <- small height
    8     3.858e-7       0.5473   <- small height
    9     3.660e-7       0.5770   <- small height, and the minimum
    10    4.359e-7       0.4844   <- small height
    11    6.401e-7       0.3299   <- small height
    12    1.142e-6       0.1850

The tower turns over at n = 9. Contrast the cyclotomic ladder, whose floor was
5430x; here the basis passes *through* the residual's magnitude.

## 🛑 Result 3 (the caution, and it is the important one)

**Six CONSECUTIVE orders qualify.** That is the entropy bound reappearing in a
new coordinate: with the tower this dense near `t`, "order n has the right
magnitude" is nearly free and carries almost no information. Anyone reading
result 2 as evidence has mistaken a dense basket for an identification — the
same error `qbeta_d_frame_terminus_probe.py` refuses to make about its own
value match, and the same one `qou-6gf9`'s entropy prune exists to forbid.

**What would carry information is the coefficient, and it is NOT computed
here.** Habiro's theorem gives `I(M;q) = sum_n a_n(M) (q;q)_n` with
`a_n(M) in Z[q^{+-1}]` — Laurent polynomials, *not* plain integers, so there is
no cheap integrality argument to run either. Until `a_n(Sigma(2,3,5))` is in
hand, everything above is a statement about the BASIS, not about Sigma(2,3,5).

## Result 4: no contradiction with the landed Lean, and why

`MuPCorrectionAdmissibility.no_small_height_w_monomial` proves NO order `j`
admits `|c| w^j = t` with `|c|` small-height. Result 2 does not contradict it:
`omega_n` is not `w^n`. Since `f_j = j^2 w + O(w^2)`,

    omega_n ~ (n!)^2 * w^n

and `(n!)^2` is emphatically not small-height — at n = 9 it is 1.32e11, and the
pure-`w` coefficient the residual would need at that order is `t/w^9 = 9.75e10`.
So the Habiro basis realises exactly the escape the Lean leaves open: a
**genuinely non-unit-height coefficient that is structurally determined rather
than chosen**. The `(n!)^2` is not a fit; it is what the basis is.

## Regime note — where `HabiroMagnitudeA3` does and does not reach

`QOU.MassTheory.HabiroMagnitudeA3.pochAbs_unbounded` is stated for `1 < q`, and
the series diverges violently there (measured: partial sum ~ -9.2e246 after 60
terms at `q0`). At the bar image `1/q0 = 0.9009` it converges cleanly —
`I(Sigma(2,3,5); 1/q0) = 14.917498476497690554`, last term 8.3e-19 by n = 399.
The theorem's other binder, `forall n, 1 <= |a n|`, is also not satisfied by
`Z[q^{+-1}]` coefficients in general. So that obstruction does not close this
route, and reading it as "Habiro is dead at the substrate" would close the one
route `qou-6gf9` names.

SCOPE. Result 1 is exact algebra, scope-(b) for "the bar-even precondition is
automatic in the Habiro basis". Results 2-4 are measurements at the proton pin,
scope-(a), and result 3 is the reason none of them is offered as evidence for
anything. Nothing here is fitted and nothing is proposed as a correction.

Anchor: the experimental (proton) pin, per the 2026-08-07 owner directive.
Residual read from the live witness (CODATA 2022), not hard-coded.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

N_MAX = 15
LO = mp.mpf(1) / 5
HI = mp.mpf(5)

_TENSION = (
    Path(__file__).resolve().parent / "mu-substrate-tension-audit-100dps.witness.json"
)


def live_residual() -> mp.mpf:
    with _TENSION.open() as fh:
        w = json.load(fh)
    return mp.mpf(str(w["data"]["residual_ppb_at_canonical_q0"])) / mp.mpf(10) ** 9


def omega(n: int, q: mp.mpf) -> mp.mpf:
    """`(q;q)_n (q^-1;q^-1)_n` — the bar-symmetric Habiro basis element."""
    p = mp.mpf(1)
    for j in range(1, n + 1):
        p *= (1 - q ** j) * (1 - q ** (-j))
    return p


def bar_even_tower(n: int, q: mp.mpf) -> mp.mpf:
    """`(-1)^n prod_{j=1..n} f_j` with `f_j = q^j + q^-j - 2` — the corpus's tower."""
    p = mp.mpf(1)
    for j in range(1, n + 1):
        p *= -(q ** j + q ** (-j) - 2)
    return p


def I_sigma235(q: mp.mpf, n_max: int = 400):
    """`I(Sigma(2,3,5);q) = (1-q)^-1 sum_{n>=0} q^n (q^{n+1})_{n+1}`.

    Transcribed from `library/arxiv-2605.15740v1/sections/sec-000-1-introduction.md`
    (the display after eq. 1.3), with `(q^{n+1})_{n+1} = prod_{k=1..n+1}(1-q^{n+k})`.
    """
    s = mp.mpf(0)
    last = mp.mpf(0)
    used = 0
    for n in range(n_max):
        p = mp.mpf(1)
        for k in range(1, n + 2):
            p *= 1 - q ** (n + k)
        term = q ** n * p
        s += term
        last = abs(term)
        used = n
        if n > 5 and last < mp.mpf(10) ** (-55):
            break
    return s / (1 - q), used, last


def main() -> int:
    q0 = q_at()
    qb = 1 / q0
    w = q0 + 1 / q0 - 2
    t = live_residual()

    print("=" * 78)
    print(" The Habiro basis is the bar-even tower; which orders bracket the residual?")
    print("=" * 78)
    print(f"""
  q0 = {mp.nstr(q0, 20)}   bar image 1/q0 = {mp.nstr(qb, 18)}
  w  = {mp.nstr(w, 20)}    t = {mp.nstr(t, 12)}  (CODATA 2022, live witness)
""")

    # ── Result 1: the identity ─────────────────────────────────────────────
    probe_q = mp.mpf("1.37")          # deliberately off-anchor
    ident = max(abs(omega(n, probe_q) - bar_even_tower(n, probe_q)) for n in range(1, 9))
    print("  RESULT 1  (q;q)_n (q^-1;q^-1)_n  ==  (-1)^n prod (q^j + q^-j - 2)")
    print(f"            max |difference| over n <= 8 at q = 1.37 : {mp.nstr(ident, 5)}")
    print("            -> the Habiro basis IS the bar-even tower, identically.")
    print("               The bar-even precondition is FREE for a Habiro element;")
    print("               it needs no appeal to 4_1 amphichirality.\n")

    # ── Result 2: the orders ───────────────────────────────────────────────
    rows = []
    bracketing = []
    for n in range(1, N_MAX + 1):
        o = abs(omega(n, q0))
        c = t / o
        small = LO <= c <= HI
        if small:
            bracketing.append(n)
        rows.append({"n": n, "abs_omega": fmt(o), "required_coefficient": fmt(c),
                     "small_height": bool(small)})
    print(f"  RESULT 2  {'n':>3} {'|omega_n|':>16} {'t/|omega_n|':>14}")
    print("            " + "-" * 46)
    for r in rows:
        if 4 <= r["n"] <= 13:
            mark = "  <- small height" if r["small_height"] else ""
            print(f"            {r['n']:>3} {mp.nstr(mp.mpf(r['abs_omega']),8):>16} "
                  f"{mp.nstr(mp.mpf(r['required_coefficient']),6):>14}{mark}")
    print()

    # ── Result 3: the caution ──────────────────────────────────────────────
    print(f"  RESULT 3  {len(bracketing)} CONSECUTIVE orders qualify: {bracketing}")
    print("            The tower is DENSE near t, so 'order n has the right")
    print("            magnitude' is nearly free and is not evidence. The")
    print("            informative quantity is a_n(Sigma(2,3,5)), which is NOT")
    print("            computed here — Habiro coefficients live in Z[q^{+-1}],")
    print("            not Z, so there is no cheap integrality argument either.\n")

    # ── Result 4: (n!)^2, and why the Lean is untouched ────────────────────
    print("  RESULT 4  omega_n ~ (n!)^2 w^n, so this is the NON-UNIT-HEIGHT escape")
    print(f"            {'n':>3} {'|omega_n|':>16} {'(n!)^2 w^n':>16} {'ratio':>8}")
    print("            " + "-" * 48)
    fact_rows = []
    for n in (6, 9, 11):
        o = abs(omega(n, q0))
        a = mp.mpf(mp.factorial(n)) ** 2 * w ** n
        fact_rows.append({"n": n, "abs_omega": fmt(o), "factorial_estimate": fmt(a),
                          "ratio": fmt(o / a)})
        print(f"            {n:>3} {mp.nstr(o,8):>16} {mp.nstr(a,8):>16} {mp.nstr(o/a,6):>8}")
    print(f"\n            pure-w coefficient needed at order 9: t/w^9 = {mp.nstr(t / w ** 9, 6)}")
    print("            -> no contradiction with no_small_height_w_monomial, which")
    print("               excludes SMALL-height coefficients on w^j.\n")

    # ── Regime ─────────────────────────────────────────────────────────────
    val, used, last = I_sigma235(qb)
    print(f"  REGIME    I(Sigma(2,3,5); 1/q0) = {mp.nstr(val, 22)}")
    print(f"            converged by n = {used}, last term {mp.nstr(last, 4)}")
    div, dused, dlast = I_sigma235(q0, n_max=60)
    print(f"            at q0 > 1 the series DIVERGES: partial sum {mp.nstr(div, 6)}")
    print(f"            after {dused + 1} terms, last term {mp.nstr(dlast, 4)}")
    print("            -> HabiroMagnitudeA3.pochAbs_unbounded (stated for 1 < q)")
    print("               does not reach the bar-image evaluation.\n")

    wb = WitnessBuilder("mu-p-habiro-basis-order", engine="python")
    wb.add_data("pin", {"q0": fmt(q0), "bar_image": fmt(qb), "w": fmt(w), "t": fmt(t)})
    wb.add_data("basis_identity_residual_at_q_1p37", fmt(ident))
    wb.add_data("orders", rows)
    wb.add_data("bracketing_orders", bracketing)
    wb.add_data("factorial_asymptotic", fact_rows)
    wb.add_data("sigma235_series", {
        "value_at_bar_image": fmt(val),
        "terms_used": used,
        "last_term": fmt(last),
        "diverges_at_q0_gt_1": True,
        "source": "library/arxiv-2605.15740v1 (lovejoy2026), display after eq. 1.3",
    })

    wb.add_assertion(
        name="habiro_basis_is_the_bar_even_tower",
        computed=str(int(ident < mp.mpf("1e-40"))), expected="1", tolerance=0,
        source=(
            "(q;q)_n (q^-1;q^-1)_n = prod (1-q^j)(1-q^-j) = prod (2 - q^j - q^-j) "
            "= (-1)^n prod f_j, the bar-even tower of MuPCarrierBarParity. Max "
            f"|difference| over n <= 8 at the off-anchor point q = 1.37 is "
            f"{mp.nstr(ident,5)}. Scope-(b), exact algebra: the bar-even "
            "precondition — which the corpus ARGUES from 4_1 amphichirality and "
            "does not prove — is automatic for any Habiro-ring element expanded "
            "in its own basis."
        ),
    )
    wb.add_assertion(
        name="six_consecutive_orders_bracket_the_residual",
        computed=str(len(bracketing)), expected="6", tolerance=0,
        source=(
            f"Orders {bracketing} all have t/|omega_n| in [1/5, 5]; the minimum "
            "is n = 9 at 0.5770. Recorded as a CAUTION, not a finding: six "
            "consecutive orders qualifying means the tower is dense near t, so "
            "magnitude agreement here is nearly free and carries almost no "
            "information — the entropy bound in a new coordinate. The "
            "informative quantity is a_n(Sigma(2,3,5)), not computed here."
        ),
    )
    wb.add_assertion(
        name="sigma235_series_converges_at_bar_image_diverges_above_one",
        computed=str(int(last < mp.mpf("1e-18") and dlast > 1)), expected="1",
        tolerance=0,
        source=(
            f"I(Sigma(2,3,5); 1/q0) = {mp.nstr(val, 20)}, last term "
            f"{mp.nstr(last,4)} by n = {used}; at q0 > 1 the partial sum reaches "
            f"{mp.nstr(div,6)} after {dused+1} terms. So the evaluation regime "
            "this route uses is the convergent one, and "
            "HabiroMagnitudeA3.pochAbs_unbounded — stated for 1 < q, and "
            "additionally requiring |a_n| >= 1 — does not reach it."
        ),
    )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
