#!/usr/bin/env python3
"""mu_p_cyclotomic_ladder_magnitude_probe.py — can a term of the figure-eight
cyclotomic ladder carry the mu-p residual?

BEAN `qou-6gf9`. Companion to `docs/audits/scripts/mu_p_carrier_order_window_probe.py`
and to the Lean prunes `QOU/BraidKnot/MuPCarrier{BarParity,OrderWindow}.lean`,
`MuPCorrectionAdmissibility.lean`, `MuPTwoTermSum.lean`.

## Why this candidate and not another

`qou-6gf9`'s GAP asks for a **bar-even correction whose coefficient is fixed
before the fact** — the entropy bound (`sigma_exp/t ~ 10 %`) makes a matched
coefficient worthless, so only an a-priori one counts.

`QOU/BraidKnot/HabiroNewtonLadder.lean` (sorry-free, on main) proves the
cyclotomic expansion of the figure-eight colored Jones polynomial termwise:

    J_N(4_1; q) = sum_{k>=0} prod_{j=1..k} (Lam_N - lam_j),
    Lam_N = q^N + q^-N,   lam_j = q^j + q^-j

with `lam_bar_even`, `multiplier_bar_even`, `coloredJones41_bar_symmetric` all
proved: every term is bar-even, and **every cyclotomic coefficient is 1**. And
`Lam_1 - lam_0 = q + q^-1 - 2 = w` exactly — the same `w` the bar-parity prune
identifies as the bar-even tower's generator.

So this is literally "a bar-even correction whose coefficient is fixed before
the fact", on the muon's OWN carrier knot. It is the strongest a-priori
candidate the corpus holds. A six-path corpus-grep (2026-09-04) found that
**nobody had ever compared it to `t`** — no probe, no witness, no audit doc.

## What this measures

Every nonzero ladder term `P_k(N)` at the proton pin, against the residual
window `t in [1.8e-7, 2.4e-7]`. Terms with `k >= N` vanish identically (the
`j = N` factor is zero), so the family is `{(N, k) : 1 <= k < N}`.

## Result, and why it is structural rather than a coincidence

Each factor is an integer polynomial in `w` with lowest term `(N^2 - j^2)*w`:
`Lam_N - lam_j = f_N - f_j` where `f_m := q^m + q^-m - 2` is a polynomial in
`w` with `f_m = m^2 w + O(w^2)`, positive and increasing in `m` for `q > 1`.
Hence

    P_k(N) ~ M_k(N) * w^k,   M_k(N) = prod_{j=1..k} (N^2 - j^2),

and since the factors increase with `N`, the minimum over `N > k` is at
`N = k+1`, where `M_k(k+1) = k! * (2k+1)! / (k+1)!` — 1260 at `k = 3`, 72576 at
`k = 4`. `M_k w^k` bottoms out near `k = 4`-`5` at about `1e-3` and grows on
both sides (the ratio `M_{k+1}/M_k * w ~ 4k^2 w` exceeds 1 once `k > ~4.8`).

**The ladder's magnitude floor sits at order `w`; `t` sits at order `w^3`.**
Two orders of `w` apart, and no term comes near the window.

SCOPE. Scope-(a) on the proposition actually at issue — "a single term of the
4_1 cyclotomic ladder supplies the residual". A **sum** over the ladder is the
colored Jones polynomial itself, which is O(1); that is a different question
and is not addressed here. Nor does this touch a ladder in a different
variable, a different knot, or a Habiro element evaluated at the bar image
`1/q0` (where `HabiroMagnitudeA3.pochAbs_unbounded`, stated for `1 < q`, does
not reach).

Anchor: the experimental (proton) pin, per the 2026-08-07 owner directive.
Residual: CODATA 2022, from the live witness rather than the bean's
superseded CODATA-2018 `t = 2.09754920524e-7`.
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

N_MAX = 12
T_LO = mp.mpf("1.8e-7")
T_HI = mp.mpf("2.4e-7")

_TENSION_WITNESS = (
    Path(__file__).resolve().parent / "mu-substrate-tension-audit-100dps.witness.json"
)


def live_residual() -> mp.mpf:
    """`t` from the live tension witness, in relative units.

    Read rather than hard-coded: `qou-6gf9`'s own `2.09754920524e-7` is the
    CODATA-2018 value, superseded by the 2026-08-22 anchor ruling.
    """
    with _TENSION_WITNESS.open() as fh:
        w = json.load(fh)
    ppb = mp.mpf(str(w["data"]["residual_ppb_at_canonical_q0"]))
    return ppb / mp.mpf(10) ** 9


def ladder_term(q: mp.mpf, N: int, k: int) -> mp.mpf:
    """`prod_{j=1..k} (Lam_N - lam_j)`, the k-th cyclotomic multiplier at colour N."""
    p = mp.mpf(1)
    for j in range(1, k + 1):
        p *= q ** N + q ** (-N) - q ** j - q ** (-j)
    return p


def min_coefficient(k: int) -> int:
    """`M_k(k+1) = prod_{j=1..k} ((k+1)^2 - j^2)`, the minimum over `N > k`."""
    m = 1
    for j in range(1, k + 1):
        m *= (k + 1) ** 2 - j ** 2
    return m


def main() -> int:
    q0 = q_at()
    w = q0 + 1 / q0 - 2
    t = live_residual()

    print("=" * 78)
    print(" Can a 4_1 cyclotomic ladder term carry the mu-p residual?")
    print("=" * 78)
    print(f"""
  q0     = {mp.nstr(q0, 20)}   (proton pin)
  w      = {mp.nstr(w, 22)}
  t      = {mp.nstr(t, 12)}   (CODATA 2022, from the live tension witness)
  t/w^3  = {mp.nstr(t / w ** 3, 10)}      t/w^4 = {mp.nstr(t / w ** 4, 10)}
  window = [{mp.nstr(T_LO, 3)}, {mp.nstr(T_HI, 3)}]
""")

    terms = []
    inside = []
    for N in range(1, N_MAX + 1):
        for k in range(1, N):          # k >= N gives an exact zero
            P = ladder_term(q0, N, k)
            terms.append((abs(P), N, k, P))
            if T_LO <= abs(P) <= T_HI:
                inside.append((N, k, P))
    terms.sort(key=lambda r: r[0])

    print(f"  {'N':>3} {'k':>3} {'|P_k(N)|':>20} {'|P|/t':>14}")
    print("  " + "-" * 46)
    for a, N, k, _ in terms[:8]:
        print(f"  {N:>3} {k:>3} {mp.nstr(a, 12):>20} {mp.nstr(a / t, 8):>14}")

    floor_abs, floor_N, floor_k, _ = terms[0]

    print(f"""
  SMALLEST nonzero term: N={floor_N}, k={floor_k}  ->  {mp.nstr(floor_abs, 12)}
                         = {mp.nstr(floor_abs / t, 8)} x the residual
                         = {mp.nstr(floor_abs / w, 8)} x w    (i.e. order w)

  terms inside the residual window: {len(inside)}

  The floor is structural. Each factor is an integer polynomial in w with
  lowest term (N^2 - j^2)*w, so P_k(N) ~ M_k(N)*w^k, and the factors increase
  with N, so the minimum over N > k is at N = k+1:
""")
    print(f"  {'k':>3} {'M_k(k+1)':>14} {'M_k w^k':>18} {'/ t':>12}")
    print("  " + "-" * 50)
    asym_rows = []
    for k in range(1, 8):
        m = min_coefficient(k)
        est = mp.mpf(m) * w ** k
        asym_rows.append({"k": k, "min_coefficient": str(m),
                          "leading_estimate": fmt(est),
                          "over_t": fmt(est / t)})
        print(f"  {k:>3} {m:>14} {mp.nstr(est, 10):>18} {mp.nstr(est / t, 6):>12}")

    print(f"""
  M_k w^k bottoms out near k = 4-5 at ~1e-3 and grows on both sides
  (M_(k+1)/M_k * w ~ 4k^2 w exceeds 1 once k > ~4.8, with w = {mp.nstr(w, 6)}).

  READING. The ladder's magnitude floor sits at order w; t sits at order w^3
  (t/w^3 = {mp.nstr(t / w ** 3, 6)}). Two orders of w apart. Every cyclotomic
  coefficient is 1 and every term is bar-even, so this candidate had exactly
  the a-priori property qou-6gf9's GAP demands — and it misses by 5430x.

  Scope-(a) on "a single ladder term supplies the residual". A SUM over the
  ladder is J_N(4_1) itself, which is O(1); different question.
""")

    wb = WitnessBuilder("mu-p-cyclotomic-ladder-magnitude", engine="python")
    wb.add_data("pin", {"q0": fmt(q0), "w": fmt(w)})
    wb.add_data("residual", {
        "t": fmt(t),
        "t_over_w3": fmt(t / w ** 3),
        "t_over_w4": fmt(t / w ** 4),
        "window_lo": fmt(T_LO), "window_hi": fmt(T_HI),
        "source": "mu-substrate-tension-audit-100dps.witness.json "
                  "data.residual_ppb_at_canonical_q0 (CODATA 2022); NOT the "
                  "bean's superseded CODATA-2018 2.09754920524e-7",
    })
    wb.add_data("smallest_nonzero_term", {
        "N": floor_N, "k": floor_k,
        "value": fmt(floor_abs),
        "over_t": fmt(floor_abs / t),
        "over_w": fmt(floor_abs / w),
    })
    wb.add_data("leading_order_floor", asym_rows)
    wb.add_data("terms_scanned", {
        "N_max": N_MAX,
        "count": len(terms),
        "note": "k >= N vanishes identically (the j = N factor is zero)",
    })

    wb.add_assertion(
        name="no_cyclotomic_ladder_term_lies_in_the_residual_window",
        computed=str(len(inside)), expected="0", tolerance=0,
        source=(
            f"Scanned every nonzero term P_k(N) = prod_(j=1..k)(q^N+q^-N-q^j-q^-j) "
            f"for N <= {N_MAX} ({len(terms)} terms; k >= N vanishes identically). "
            f"None lies in [{mp.nstr(T_LO,3)}, {mp.nstr(T_HI,3)}]. Scope-(a) on "
            "'a single term of the 4_1 cyclotomic ladder supplies the residual'; "
            "a sum over the ladder is J_N(4_1) itself and is O(1)."
        ),
    )
    wb.add_assertion(
        name="ladder_magnitude_floor_is_order_w_not_order_w_cubed",
        computed=str(int(floor_abs / t > 1000)), expected="1", tolerance=0,
        source=(
            f"Smallest nonzero term is N={floor_N}, k={floor_k}: "
            f"{mp.nstr(floor_abs, 10)} = {mp.nstr(floor_abs / t, 6)}x the "
            f"residual and {mp.nstr(floor_abs / w, 6)}x w, i.e. order w. The "
            "residual is order w^3 (t/w^3 = "
            f"{mp.nstr(t / w ** 3, 6)}). Structural: each factor is an integer "
            "polynomial in w with lowest term (N^2-j^2)w and the factors "
            "increase with N, so the floor over N > k is M_k(k+1) w^k with "
            "M_k = k!(2k+1)!/(k+1)!, which bottoms out near k=4 at ~1e-3."
        ),
    )
    wb.add_assertion(
        name="min_coefficient_matches_the_closed_form",
        computed=str(min_coefficient(3)), expected="1260", tolerance=0,
        source=(
            "M_3(4) = (16-1)(16-4)(16-9) = 15*12*7 = 1260 = 3!*7!/4!. Guards "
            "the closed form M_k(k+1) = k!(2k+1)!/(k+1)! that the leading-order "
            "floor table is computed from, so a future edit to either cannot "
            "silently diverge from the other."
        ),
    )
    out = wb.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
