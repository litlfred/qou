#!/usr/bin/env python3
"""mu_p_sigma235_ohtsuki_resolution_probe.py — the Sigma(2,3,5) route cannot
carry the mu-p residual, and the reason is a resolution bound rather than a
magnitude miss.

BEAN `qou-6gf9`. Closes the measurement opened by
`mu_p_habiro_basis_order_probe.py`, which established that the Habiro basis IS
the bar-even tower and that six consecutive orders bracket `t` *with unit
coefficients* — recorded there as a caution, because the informative quantity is
the actual coefficient. This probe computes them.

Source: `library/arxiv-2605.15740v1` (Lovejoy, Osburn & Storzer, `lovejoy2026`),

    I(Sigma(2,3,5); q) = (1-q)^-1 * sum_{n>=0} q^n (q^{n+1})_{n+1},
    (a)_n = (a;q)_n = prod_{k=1}^{n} (1 - a q^{k-1}).

## Why this route was the last one standing

`qou-6gf9`'s GAP asks for a bar-even correction whose coefficient is fixed
BEFORE comparison — the entropy bound (`sigma_exp/t ~ 10 %`) makes a matched
coefficient worthless. Sigma(2,3,5) was the corpus's one named candidate whose
coefficients come from quantum topology rather than from matching, and the
sibling probe showed the obstruction that appears to block it
(`HabiroMagnitudeA3.pochAbs_unbounded`, stated for `1 < q`) does not reach the
bar-image evaluation.

## What this computes

The Taylor expansion of `I` at `q = 1` in `x = q - 1`, exactly over the
rationals. Only terms `n <= N` contribute to order `N`: term `n` carries `n+1`
factors each vanishing to order 1, less one from the `1/(1-q)`, so it vanishes
to order `n`.

## Result 1 — the coefficients are exact integers, and they are the Ohtsuki series

    1, -6, 45, -464, 6224, -102816, 2015237, -45679349, 1175123730, ...

**Free sanity check, not assumed:** `lambda_1 = -6`. Ohtsuki's normalisation
gives `lambda_1 = 6 * lambda_Casson`, and the Casson invariant of the Poincare
homology sphere is `-1`. The computation reproduces a known invariant of the
manifold from the q-series alone.

## Result 2 — the series is factorially DIVERGENT

`|lambda_{n+1} / lambda_n|` is **linear in n** (7.5, 10.3, 13.4, 16.5, 19.6,
22.7, 25.7, 28.8, 31.8, ... ~ 3n), which is the signature of `n!` growth. So
`I(Sigma(2,3,5); q)` at `q = 1` is an **asymptotic** series, not a convergent
one — as expected for a WRT/Ohtsuki expansion, and as the sibling probe's
divergence at `q0 > 1` already hinted.

## Result 3 — the resolution floor, and this is the finding

At the substrate `x0 = q0 - 1 = 0.10998` the terms `|lambda_n x0^n|` are

    n:      0      1      2      3      4      5      6      7
    |term|: 1.00   0.660  0.544  0.617  0.911  1.654  3.566  8.889

They turn over at **n = 2** and grow thereafter. **An asymptotic series cannot
resolve anything below its least term** — that is what optimal truncation
means. So this object's intrinsic resolution at the substrate is

    least term = 0.5443   against   t = 2.1116e-7,

a factor of **2.58e6**. The residual is more than six orders of magnitude below
the floor, so *no* truncation of this expansion — not the best one, not any
other — can supply it.

This is a stronger statement than "the terms happen to miss `t`". It says the
question cannot be asked of this object in this coordinate: the correction being
sought is far finer than anything the expansion can express at this `q`.

## It also explains the sibling probe's caution

`mu_p_habiro_basis_order_probe` found six consecutive orders of the *basis*
`omega_n` bracketing `t` with unit coefficients, and flagged that as dense
rather than informative. This is why: the basis elements do pass through `t`'s
magnitude, but the manifold's own coefficients grow factorially, so the products
never land there. The caution was correct and this supplies the mechanism.

## SCOPE — read before citing

**Scope-(b) for the stated class**: no truncation of the Taylor/Ohtsuki
expansion of `I(Sigma(2,3,5))` at `q0` supplies a correction of size `t`. The
argument is the optimal-truncation floor, which quantifies over every
truncation, not a numerical miss at one order.

**Scope-(a) for the route as a whole.** It does NOT exclude:

- a **resummation** (Borel, median, Ecalle-Borel) of the same series, which is
  precisely how a divergent asymptotic series is given a value finer than its
  least term — the corpus holds resurgence sources (`arxiv-2304.07001v3`);
- evaluation at a **root of unity**, which is where the Habiro element is
  actually defined and where `I(M;zeta) = Z_zeta(M)` exactly;
- a **different** Brieskorn sphere or a different invariant of this one;
- the exact **Habiro-basis coefficients** `a_n(q) in Z[q^{+-1}]`, which this
  does not compute — the Taylor coefficients at `q=1` are a different (coarser)
  object, and the relation between them is not used here.

Nothing here is fitted; nothing is proposed as a correction. The coefficients
are exact integers determined by the manifold and were computed before any
comparison to `t`.

Anchor: the experimental (proton) pin, per the 2026-08-07 owner directive.
Residual read from the live witness (CODATA 2022), not hard-coded.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from math import comb
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

N = 16  # Taylor order in x = q - 1

_TENSION = (
    Path(__file__).resolve().parent / "mu-substrate-tension-audit-100dps.witness.json"
)


def live_residual() -> mp.mpf:
    with _TENSION.open() as fh:
        w = json.load(fh)
    return mp.mpf(str(w["data"]["residual_ppb_at_canonical_q0"])) / mp.mpf(10) ** 9


def _mul(a, b):
    out = [F(0)] * (N + 1)
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b):
            if i + j > N:
                break
            if bj:
                out[i + j] += ai * bj
    return out


def _qpow(m):
    """`q^m = (1+x)^m`, truncated."""
    return [F(comb(m, i)) if i <= m else F(0) for i in range(N + 1)]


def _one_minus_qpow(m):
    """`1 - q^m`, which vanishes to order 1 in x."""
    s = _qpow(m)
    return [(-s[i] if i else F(1) - s[0]) for i in range(N + 1)]


def taylor_coefficients():
    """Exact Taylor coefficients of `I(Sigma(2,3,5);q)` at `q = 1` in `x = q-1`."""
    total = [F(0)] * (N + 1)
    for n in range(N + 2):
        p = _qpow(n)
        for k in range(1, n + 2):
            p = _mul(p, _one_minus_qpow(n + k))
        if all(c == 0 for c in p):
            break
        total = [total[i] + p[i] for i in range(N + 1)]
    assert total[0] == 0, "the 1/(1-q) pole did not cancel"
    # divide by (1-q) = -x : shift down one, negate
    return [-total[i + 1] if i + 1 <= N else F(0) for i in range(N + 1)]


def main() -> int:
    q0 = q_at()
    x0 = q0 - 1
    t = live_residual()
    lam = taylor_coefficients()

    print("=" * 78)
    print(" Sigma(2,3,5): the Ohtsuki series, and what it can resolve at the substrate")
    print("=" * 78)
    print(f"""
  q0 = {mp.nstr(q0, 18)}    x0 = q0 - 1 = {mp.nstr(x0, 12)}
  t  = {mp.nstr(t, 12)}   (CODATA 2022, live tension witness)
""")

    print("  RESULT 1  exact Taylor coefficients at q = 1 (integers):")
    print("            " + ", ".join(str(lam[n]) for n in range(9)) + ", ...")
    casson_ok = lam[1] == -6
    print(f"            lambda_1 = {lam[1]}  ->  Casson invariant "
          f"{'-1 as expected (lambda_1 = 6*lambda_Casson)' if casson_ok else 'MISMATCH'}")
    print()

    ratios = [abs(F(lam[n + 1], lam[n])) for n in range(1, 11) if lam[n]]
    print("  RESULT 2  |lambda_(n+1)/lambda_n| is LINEAR in n -> factorial divergence:")
    print("            " + ", ".join(f"{float(r):.1f}" for r in ratios))
    print()

    print("  RESULT 3  terms at the substrate, and the optimal-truncation floor")
    print(f"            {'n':>3} {'|lambda_n x0^n|':>18} {'/ t':>14}")
    print("            " + "-" * 38)
    rows = []
    best_n, best_a = None, None
    for n in range(N):
        term = mp.mpf(str(lam[n])) * x0 ** n
        a = abs(term)
        rows.append({"n": n, "lambda_n": str(lam[n]), "abs_term": fmt(a),
                     "over_t": fmt(a / t)})
        if a > 0 and (best_a is None or a < best_a):
            best_n, best_a = n, a
        if n <= 8:
            print(f"            {n:>3} {mp.nstr(a, 8):>18} {mp.nstr(a / t, 7):>14}")
    floor_over_t = best_a / t
    print(f"""
            LEAST TERM at n = {best_n}: |term| = {mp.nstr(best_a, 8)}
            = {mp.nstr(floor_over_t, 7)} x the residual

  An asymptotic series cannot resolve anything below its least term. This
  object's intrinsic resolution at the substrate is {mp.nstr(best_a, 4)}, and t is
  {mp.nstr(floor_over_t, 6)} times smaller. NO truncation can supply it -- not the
  optimal one, not any other. That is a statement about the whole class,
  not a numerical miss at one order.

  It also explains the sibling probe's caution: the BASIS omega_n does pass
  through t's magnitude at six consecutive orders, but the manifold's own
  coefficients grow factorially, so the products never land there.
""")

    wb = WitnessBuilder("mu-p-sigma235-ohtsuki-resolution", engine="python")
    wb.add_data("pin", {"q0": fmt(q0), "x0": fmt(x0), "t": fmt(t)})
    wb.add_data("taylor_coefficients", [str(c) for c in lam])
    wb.add_data("growth_ratios", [fmt(mp.mpf(str(r))) for r in ratios])
    wb.add_data("terms_at_substrate", rows)
    wb.add_data("optimal_truncation", {
        "n": best_n, "least_term": fmt(best_a), "floor_over_t": fmt(floor_over_t),
    })
    wb.add_data("source", {
        "series": "I(Sigma(2,3,5);q) = (1-q)^-1 sum_{n>=0} q^n (q^{n+1})_{n+1}",
        "reference": "lovejoy2026, library/arxiv-2605.15740v1, display after eq. 1.3",
    })

    wb.add_assertion(
        name="lambda_1_reproduces_the_casson_invariant",
        computed=str(lam[1]), expected="-6", tolerance=0,
        source=(
            "Ohtsuki's normalisation gives lambda_1 = 6*lambda_Casson, and "
            "lambda_Casson(Sigma(2,3,5)) = -1. Computing -6 from the q-series "
            "alone reproduces a known invariant of the manifold and is a free "
            "check that the transcription and the extraction are both correct."
        ),
    )
    wb.add_assertion(
        name="series_is_factorially_divergent",
        computed=str(int(float(ratios[-1]) > 3 * float(ratios[0]))),
        expected="1", tolerance=0,
        source=(
            "|lambda_(n+1)/lambda_n| grows LINEARLY in n ("
            + ", ".join(f"{float(r):.1f}" for r in ratios[:6])
            + ", ...), the signature of n! growth. So the expansion at q=1 is "
            "asymptotic, not convergent."
        ),
    )
    wb.add_assertion(
        name="resolution_floor_exceeds_residual_by_over_1e6",
        computed=str(int(floor_over_t > mp.mpf(10) ** 6)), expected="1", tolerance=0,
        source=(
            f"Least term at n={best_n} is {mp.nstr(best_a, 8)}, which is "
            f"{mp.nstr(floor_over_t, 7)}x the residual t = {mp.nstr(t, 8)}. An "
            "asymptotic series cannot resolve below its least term, so NO "
            "truncation of this expansion at q0 supplies a correction of size "
            "t. Scope-(b) for that class (it quantifies over every "
            "truncation); scope-(a) for the route, which does NOT exclude a "
            "Borel/median resummation, evaluation at a root of unity where the "
            "Habiro element is actually defined, a different Brieskorn sphere, "
            "or the exact Habiro-basis coefficients a_n(q) in Z[q^{+-1}] -- "
            "none of which this computes."
        ),
    )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
