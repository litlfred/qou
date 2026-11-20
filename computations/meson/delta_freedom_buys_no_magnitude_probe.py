#!/usr/bin/env python3
"""
delta_freedom_buys_no_magnitude_probe.py — the Δ freedom is real in the
valuation and worth NOTHING in magnitude.

THE QUESTION.  Addendum 32 found that Δ(β₁,β₂;A) is not pinned the way the
interface is, and localised the carrier: the p–n letter `σ − h(½ − δ/4)·1`,
whose coefficient carries `δ = flavor_split_leading(q)`.  That is a statement
about a `q → 0` VALUATION.  It says nothing about whether the same letter can
move `tr_M(β_D)` toward `√B_AME = 1.491498`, which is the §C/§E question.

THE CRUX, and it is a one-line check.  Using `σ⁻¹ = σ − h`, the p–n letter is

    σ − h(½ − δ/4)·1  =  (½ + δ/4)·σ  +  (½ − δ/4)·σ⁻¹,

weights summing to 1.  §C/§E's `convex_comb_le_bound` (Lean, sorry-free)
bounds any CONVEX combination of the branches by `max_b tr_M = 1.018275`, and
its companion `bound_fails_without_nonneg` shows non-negativity is exactly
what the bound needs.  So everything turns on whether BOTH weights are
non-negative at the substrate — i.e. on whether `|δ| ≤ 2`.

WHY THE TWO REGIMES CAN DISAGREE.  `δ = (q−1)²(1−q⁻⁴)/3`
(`prop:flavor-split-substrate`).  As `q → 0` the `q⁻⁴` term diverges, which is
what buys Addendum 32's four extra units of pole order.  At `q₀ ≈ 1.11` the
`(q−1)²` prefactor is ~0.012 and the whole thing is small.  The same
expression is enormous in one regime and negligible in the other.

NO FLOAT64: `mpmath.mpf` end to end; `float()` only inside f-strings.
Audit-only, emits no witness.

@module computations/meson/delta_freedom_buys_no_magnitude_probe
"""

from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from hecke_characters import standard_young_tableaux  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()
mp.mp.dps = max(mp.mp.dps, 60)

Q = Q_MP
H = Q - 1 / Q
SQRT_B_AME = mp.mpf("1.491498")      # √B_AME(²H), the §C bar
MAX_B = mp.mpf("1.018275")           # §C's convex ceiling over the 32 branches
SEC_C_BASELINE = mp.mpf("0.575172")  # §C's tr_M(β_D)


def seminormal(shape, q):
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    hq = q - 1 / q
    sigmas = []
    for k in range(1, n):
        rows = [[mp.mpf(0)] * dim for _ in range(dim)]
        seen = set()
        for i in range(dim):
            if i in seen:
                continue
            ci, ci1 = syts[i][k], syts[i][k + 1]
            rho = contents[ci1] - contents[ci]
            a = hq / (1 - q ** (-2 * rho))
            sw = dict(syts[i]); sw[k], sw[k + 1] = ci1, ci
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == sw), None)
            if j is None:
                rows[i][i] = a; seen.add(i)
            else:
                ap = hq / (1 - q ** (2 * rho))
                b = mp.sqrt(a * ap + 1)
                rows[i][i], rows[j][j] = a, ap
                rows[i][j] = rows[j][i] = b
                seen.update((i, j))
        sigmas.append(mp.matrix(rows))
    return sigmas, dim


def qint(m):
    return (Q ** m - Q ** (-m)) / (Q - 1 / Q)


def two_row(n):
    return [(n,)] + [(n - k, k) for k in range(1, n // 2 + 1)]


_CACHE = {}


def chi(shape, letters):
    if shape not in _CACHE:
        _CACHE[shape] = seminormal(shape, Q)
    sig, dim = _CACHE[shape]
    m = mp.eye(dim)
    for (c, d, g) in letters:
        m = (mp.mpf(c) * sig[g] + mp.mpf(d) * mp.eye(dim)) * m
    return sum(m[i, i] for i in range(dim))


def tr_M(letters, n=6):
    """Convention-D Markov trace: only ℓ(λ) ≤ 2 carries nonzero y_λ."""
    return mp.fsum(
        (qint(n - 2 * (lam[1] if len(lam) > 1 else 0) + 1) / qint(2) ** n) * chi(lam, letters)
        for lam in two_row(n))


def with_interface_weight(base, idx, w):
    """`base` with letter `idx` replaced by `w·σ + (1−w)·σ⁻¹ = σ − h(1−w)·1`."""
    out = list(base)
    _c, _d, g = out[idx]
    out[idx] = (mp.mpf(1), -H * (1 - w), g)
    return out


def main() -> int:
    print("=" * 76)
    print("Does the δ-carrying letter buy any MAGNITUDE, or only valuation?")
    print("=" * 76)
    checks = []

    def check(ok, detail):
        checks.append((bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] A{len(checks)}: {detail}")

    delta = flavor_split_leading(Q)
    w_plus, w_minus = mp.mpf(1) / 2 + delta / 4, mp.mpf(1) / 2 - delta / 4
    print(f"\n1. The colour weight at the substrate")
    print(f"   δ = (q−1)²(1−q⁻⁴)/3 at q₀ = {mp.nstr(Q, 20)}")
    print(f"   δ            = {mp.nstr(delta, 18)}")
    print(f"   w(σ)   = ½+δ/4 = {mp.nstr(w_plus, 18)}")
    print(f"   w(σ⁻¹) = ½−δ/4 = {mp.nstr(w_minus, 18)}")

    check(abs(w_plus + w_minus - 1) < mp.mpf("1e-40"),
          f"the two weights sum to 1 exactly — the letter IS an affine "
          f"combination of σ and σ⁻¹, as `σ⁻¹ = σ − h` requires")
    check(w_plus >= 0 and w_minus >= 0,
          f"and BOTH are non-negative (min = {mp.nstr(min(w_plus, w_minus), 12)}), so the "
          f"letter is INSIDE the convex hull of {{σ, σ⁻¹}} — `convex_comb_le_bound` "
          f"applies verbatim and §C's ceiling {mp.nstr(MAX_B, 8)} holds")
    check(abs(delta / 4) < mp.mpf("1e-3"),
          f"the colour weighting moves the interface off colour-blind ½ by only "
          f"δ/4 = {mp.nstr(delta / 4, 8)}, i.e. {mp.nstr(100 * delta / 2, 6)} % — a "
          f"perturbation, not a lever")

    print("\n2. What it does to the trace, measured")
    w_word = atom_braid_word_3A(1, 1)                               # colour-weighted
    b_word = atom_braid_word_3A(1, 1, pn_convention="strict_averaged")
    tw, tb = tr_M(w_word), tr_M(b_word)
    print(f"   bring_color_weighted   tr_M = {mp.nstr(tw, 12)}")
    print(f"   strict_averaged        tr_M = {mp.nstr(tb, 12)}")
    print(f"   difference             {mp.nstr(tw - tb, 8)}  "
          f"({mp.nstr(100 * (tw - tb) / tb, 6)} %)")
    print(f"   §C baseline            {mp.nstr(SEC_C_BASELINE, 12)}   (control)")

    check(abs(tw - SEC_C_BASELINE) < mp.mpf("1e-5"),
          f"CONTROL: the colour-weighted trace reproduces §C's committed "
          f"{mp.nstr(SEC_C_BASELINE, 8)} to {mp.nstr(abs(tw - SEC_C_BASELINE), 4)} — this "
          f"probe is measuring the same object §C bounded")
    check(abs(tw - tb) / tb < mp.mpf("1e-2"),
          f"the entire effect of colour weighting on the trace is "
          f"{mp.nstr(100 * abs(tw - tb) / tb, 6)} % — the 4 units of pole order it buys "
          f"at q → 0 are worth this much at q₀")
    check(tw < MAX_B and tw < SQRT_B_AME,
          f"and it lands at {mp.nstr(tw, 8)}: below §C's ceiling {mp.nstr(MAX_B, 8)}, and "
          f"{mp.nstr(SQRT_B_AME / tw, 6)}× short of the bar {mp.nstr(SQRT_B_AME, 8)}")

    print("\n3. How far outside would it have to go?")
    t0, t1 = tr_M(with_interface_weight(b_word, 11, mp.mpf(0))), \
             tr_M(with_interface_weight(b_word, 11, mp.mpf(1)))
    print(f"   tr_M is affine in the interface weight w:")
    print(f"      w = 0 (pure σ⁻¹)  tr_M = {mp.nstr(t0, 12)}")
    print(f"      w = 1 (pure σ)    tr_M = {mp.nstr(t1, 12)}")
    w_need = (SQRT_B_AME - t0) / (t1 - t0)
    delta_need = 4 * (w_need - mp.mpf(1) / 2)
    print(f"   reaching {mp.nstr(SQRT_B_AME, 8)} needs w = {mp.nstr(w_need, 10)}, "
          f"i.e. δ = {mp.nstr(delta_need, 10)}")
    print(f"   the substrate supplies δ = {mp.nstr(delta, 10)}  → short by "
          f"{mp.nstr(abs(delta_need / delta), 8)}×")

    check(not (0 <= w_need <= 1),
          f"the required weight w = {mp.nstr(w_need, 8)} is OUTSIDE [0,1] — no convex "
          f"interface reaches the bar, which is §C/§E restated at this one letter")
    check(abs(delta_need) > 2,
          f"and the required |δ| = {mp.nstr(abs(delta_need), 8)} exceeds 2, the threshold "
          f"at which a weight goes negative. The substrate's δ is "
          f"{mp.nstr(abs(delta_need / delta), 6)}× smaller")

    print("\n4. Reconciling with Addendum 32")
    print("   δ = (q−1)²(1−q⁻⁴)/3 — the q⁻⁴ term diverges as q → 0, the (q−1)²")
    print("   prefactor vanishes as q → 1.  Evaluated:")
    for lbl, qq in [("q → 0  (3⁻¹⁵)", mp.mpf(3) ** -15), ("q₀ (substrate)", Q)]:
        dd = flavor_split_leading(qq)
        print(f"      {lbl:16s} δ = {mp.nstr(dd, 8):>16s}   "
              f"|δ| > 2 ? {'YES — outside the hull' if abs(dd) > 2 else 'no — inside'}")
    d_far = flavor_split_leading(mp.mpf(3) ** -15)
    check(abs(d_far) > 2 and abs(delta) < 2,
          "the SAME δ is outside the hull at q → 0 and far inside it at q₀ — so "
          "Addendum 32's valuation freedom and §C's magnitude bound are both correct "
          "and describe different regimes. The freedom is a q → 0 artefact")

    print("\n" + "=" * 76)
    print("VERDICT: free in the valuation, bounded in magnitude — the second branch.")
    passed = sum(1 for ok, _ in checks if ok)
    print(f"{passed}/{len(checks)} assertions passed")
    print("=" * 76)
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
