#!/usr/bin/env python3
"""
qou-ales step 7 — candidates up to ten vertices: numerical cross-check of
`QOU/Mass/GammaGammaSelectionTen.lean` at the proton pin.

The Lean file carries the Chebyshev closed forms chi_k = tr V^k (x = h^2) to
k = 10 and proves: on 0 < x <= 1/10 the signs for k = 6..10 are (+,-,-,+,-), so
on H_3 the reading-3 survivors with k <= 10 are exactly 3 | k; on the H_6
interface the (3,3) condition 1 + 2 chi_m has the same pattern on
0 < x <= 1/18 (1 + 2 chi_8 changes sign near x = 0.058); both selections stay
at three vertices.

This probe does NOT re-derive any of that. It checks:

  * the closed forms chi_6..chi_10 equal the directly computed tr(V^k) from
    the Hoefsmit (2,1) matrix at 60 dps;
  * the feasible sets at the pin: H_3 {k <= 10 : chi_k >= 0} = {3, 6, 9} and
    H_6 {m <= 10 : 1 + 2 chi_m >= 0} = {3, 6, 9};
  * the pin lies in both Lean intervals (1 < q <= 23/20 and 1 < q <= 10/9,
    i.e. h^2 <= 1/10 and h^2 <= 1/18).

Informational (no assertion): the roots x*_5 and x*_8 of 1 + 2 chi_k on
(0, 1/10) — why the H_6 intervals are 1/12 and 1/18 rather than 1/10.

## Precision
mpmath at 60 dps end to end; q_0 is the proton pin `Q_50_DIGIT_STR`. Nothing
here reads AME2020, CODATA masses beyond the pin, or a census.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/qou-substrate/python", "computations/substrate", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def matpow(A, k):
    M = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]
    for _ in range(k):
        M = matmul(M, A)
    return M


def chi_closed(k: int, x):
    """Lean trace_vtx_pow_one..ten, x = h^2 (k = 0: dim 2)."""
    return {
        0: mp.mpf(2),
        1: -1 - x,
        2: x ** 2 + 2 * x - 1,
        3: 2 - 3 * x ** 2 - x ** 3,
        4: x ** 4 + 4 * x ** 3 + 2 * x ** 2 - 4 * x - 1,
        5: -x ** 5 - 5 * x ** 4 - 5 * x ** 3 + 5 * x ** 2 + 5 * x - 1,
        6: x ** 6 + 6 * x ** 5 + 9 * x ** 4 - 4 * x ** 3 - 12 * x ** 2 + 2,
        7: -x ** 7 - 7 * x ** 6 - 14 * x ** 5 + 21 * x ** 3 + 7 * x ** 2 - 7 * x - 1,
        8: x ** 8 + 8 * x ** 7 + 20 * x ** 6 + 8 * x ** 5 - 30 * x ** 4 - 24 * x ** 3
           + 12 * x ** 2 + 8 * x - 1,
        9: -x ** 9 - 9 * x ** 8 - 27 * x ** 7 - 21 * x ** 6 + 36 * x ** 5 + 54 * x ** 4
           - 9 * x ** 3 - 27 * x ** 2 + 2,
        10: x ** 10 + 10 * x ** 9 + 35 * x ** 8 + 40 * x ** 7 - 35 * x ** 6 - 98 * x ** 5
            - 15 * x ** 4 + 60 * x ** 3 + 15 * x ** 2 - 10 * x - 1,
    }[k]


def main() -> int:
    t0 = time.time()
    q = Q_MP
    qi = 1 / q
    h = q - qi
    x = h ** 2
    # Hoefsmit (2,1) data, closed form (Lean hoefsmitA / hoefsmitA' / hoefsmitB)
    a = h / (1 - q ** 4)
    a2 = h / (1 - q ** -4)
    b = mp.sqrt(a * a2 + 1)
    V = [[q * (a - h), q * b], [-qi * b, -qi * (a2 - h)]]
    print(f"qou-ales step 7 probe — candidates to ten vertices (proton pin, {DPS} dps)")
    print(f"  q_0 = {mp.nstr(q, 20)}   h^2 = {mp.nstr(x, 20)}")

    dev_max = mp.mpf(0)
    rows = []
    print(f"\n  {'k':>3}{'tr V^k (direct)':>30}{'closed form':>30}{'dev':>10}{'1+2chi':>22}")
    for k in range(0, 11):
        M = matpow(V, k)
        direct = M[0][0] + M[1][1]
        closed = chi_closed(k, x)
        dev = abs(direct - closed)
        dev_max = max(dev_max, dev)
        rows.append({"k": k, "chi": fmt(closed), "one_plus_2chi": fmt(1 + 2 * closed)})
        print(f"  {k:>3}{mp.nstr(direct, 22):>30}{mp.nstr(closed, 22):>30}{mp.nstr(dev, 3):>10}"
              f"{mp.nstr(1 + 2 * closed, 14):>22}")
    print(f"  max |dev| = {mp.nstr(dev_max, 3)}")

    h3_feasible = [k for k in range(1, 11) if chi_closed(k, x) >= 0]
    h6_feasible = [m for m in range(1, 11) if 1 + 2 * chi_closed(m, x) >= 0]
    h3_ok = h3_feasible == [3, 6, 9]
    h6_ok = h6_feasible == [3, 6, 9]
    print(f"\n  H_3 feasible k <= 10 (chi_k >= 0):        {h3_feasible}")
    print(f"  H_6 feasible m <= 10 (1 + 2 chi_m >= 0): {h6_feasible}")

    in_wide = bool(1 < q <= mp.mpf(23) / 20) and bool(x <= mp.mpf(1) / 10)
    in_narrow = bool(1 < q <= mp.mpf(10) / 9) and bool(x <= mp.mpf(1) / 18)
    print(f"  pin in 1 < q <= 23/20, h^2 <= 1/10: {in_wide};  in 1 < q <= 10/9, h^2 <= 1/18: {in_narrow}")

    r5 = mp.findroot(lambda t: 1 + 2 * chi_closed(5, t), mp.mpf("0.09"))
    r8 = mp.findroot(lambda t: 1 + 2 * chi_closed(8, t), mp.mpf("0.058"))
    print(f"  informational: 1 + 2 chi_5 = 0 at x = {mp.nstr(r5, 10)};  1 + 2 chi_8 = 0 at x = {mp.nstr(r8, 10)}"
          f"  (1/18 = {mp.nstr(mp.mpf(1) / 18, 6)}, 1/12 = {mp.nstr(mp.mpf(1) / 12, 6)})")

    elapsed = time.time() - t0
    print(f"\n  wall {elapsed:.1f} s")

    from qou_substrate.witness import WitnessBuilder  # noqa: PLC0415
    w = WitnessBuilder("gamma-gamma-selection-ten-probe", engine="python", start_time=t0)
    w.set_description(
        "qou-ales step 7: candidates up to ten vertices. Cross-checks QOU/Mass/GammaGammaSelectionTen.lean "
        "at the proton pin: the Chebyshev closed forms chi_6..chi_10 equal the direct tr(V^k) of the "
        "Hoefsmit (2,1) vertex image; the reading-3 feasible sets with k, m <= 10 are {3, 6, 9} on H_3 "
        "and on the H_6 interface (3,3) condition; the pin lies in both Lean intervals. Informational: "
        "the roots of 1 + 2 chi_5 and 1 + 2 chi_8. No AME/CODATA binding value or census is read.")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("convention", "D (Hoefsmit (2,1) block; two-row weight support at n = 6)")
    w.add_parameter("dps", DPS)
    w.add_parameter("tolerance", fmt(TOL))
    w.add_data("h_sq", fmt(x))
    w.add_data("chebyshev_table_0_to_10", rows)
    w.add_data("h3_feasible_k_le_10", h3_feasible)
    w.add_data("h6_feasible_m_le_10", h6_feasible)
    w.add_data("root_1_plus_2chi5", fmt(r5))
    w.add_data("root_1_plus_2chi8", fmt(r8))
    w.add_assertion(name="closed_forms_match_direct_powers_k_le_10", computed=fmt(dev_max), expected="0",
                    tolerance="1e-50", source="Lean trace_vtx_pow_six..ten via pow_eq_lin")
    w.add_assertion(name="h3_feasible_set_is_multiples_of_three", computed=str(int(h3_ok)), expected="1",
                    tolerance="0", source="Lean vertexPow_frobeniusFeasible_iff_three_dvd")
    w.add_assertion(name="h6_feasible_set_is_multiples_of_three", computed=str(int(h6_ok)), expected="1",
                    tolerance="0", source="Lean interface_frobeniusFeasible_iff_three_dvd")
    w.add_assertion(name="pin_inside_wide_interval", computed=str(int(in_wide)), expected="1",
                    tolerance="0", source="Lean h_sq_le_of_q_le")
    w.add_assertion(name="pin_inside_narrow_interval", computed=str(int(in_narrow)), expected="1",
                    tolerance="0", source="Lean h_sq_le_eighteenth_of_q_le")
    out = w.save()
    print(f"  witness -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
