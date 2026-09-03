#!/usr/bin/env python3
"""magnus_gauge_hook_decay_bound_probe.py — does the reduced-Burau closed form make the hook-column
decay of the gauge-invariant curvature a THEOREM? Measure two rigorous bounds (qou-o6ov).

#6464 / #6480: on a hook (k,1^{n-k}) = Λ^j(V), j = n−k, the projector curvature has the closed form
    tr_hook(ρ·Ω₂^P) = (4/[2]_q²) · q^{(L+2)(1−j)} · Σ_a [ e_j(eig M_a⁺) − e_j(eig M_a⁻) ],
    M_a⁺ = W σ^V_a σ^V_{a+1},  M_a⁻ = W σ^V_{a+1} σ^V_a,  W = ρ^V (reduced Burau of the word).
For hooks b(λ) = n − λ_1 = j, so a bound in j IS the hook-column decay statement.

TWO RIGOROUS BOUNDS, both from |e_j| ≤ (something) applied term by term, T_j := (4/[2]²)·q^{(L+2)(1−j)}:
  CRUDE  (spectral radius):  |e_j(μ)| ≤ C(n−1,j)·r^j,  r = max|μ| over all 2(ngen−1) matrices.
         B_j = T_j · 2(ngen−1) · C(n−1,j) · r^j  — a binomial hump ∝ C(n−1,j)·d^j, d := q^{−(L+2)}·r,
         peaking near j ≈ (n−1)·d/(1+d). It decays only PAST the peak. (First run: d = 0.82, 0.90.)
  SHARP  (triangle inequality): |e_j(μ)| ≤ e_j(|μ|), the elementary symmetric of the MODULI.
         B'_j = T_j · Σ_a [ e_j(|eig M_a⁺|) + e_j(|eig M_a⁻|) ].
         This keeps the whole spectrum shape. Formalizable in one lemma (|Σ∏| ≤ Σ∏|·|).
The structural point the crude bound hides: r ≈ q^L (the dominant Burau eigenvalue of a positive
word of length L is ≈ q^L — each generator contributes q on its symmetric channel), so the twist
q^{−(L+2)(j−1)} exactly cancels the dominant eigenvalue and d ≈ q^{−2}·(r/q^L). The decay in j must
therefore come from the SUBDOMINANT eigenvalues, which only the sharp bound sees.

THIS PROBE MEASURES (A=2,3; exact mpf; dps 140):
  (1) self-check: closed form == direct seminormal tr_hook(ρΩ₂^P) — relative in the interior,
      ABSOLUTE at the two exact-zero endpoints (a relative test there is a false alarm);
  (2) r, r/q^L, the driver d, and the SORTED Burau moduli of W (dominant vs subdominant);
  (3) both bounds per hook: HOLD (|tr| ≤ B, B'), DECAY (monotone for j ≥ 1), tightness.
scope-(a); NO-FLOAT64 (mpf). No fit, no witness, nothing wired.
"""
from __future__ import annotations

import argparse
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

mp.mp.dps = 140  # pin explicitly (do not rely on an imported side effect)

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from magnus_gauge_invariant_curvature_probe import projector_curvature_trace  # noqa: E402
from magnus_gauge_hook_closed_form_probe import reflection_generators, hook_closed_form  # noqa: E402
from magnus_hook_exterior_power_probe import elem_sym_from_eigs  # noqa: E402

ABS_ZERO_TOL = mp.mpf(10) ** -100   # endpoint absolute tolerance (exact zeros)
REL_TOL = mp.mpf(10) ** -100        # interior relative tolerance


def moduli(M):
    E, _ = mp.eig(M)
    return sorted((abs(mu) for mu in E), reverse=True)


def analyze(A):
    q = base.Q0
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1
    L = len(gens)
    two_q = q + 1 / q
    coef = 4 / two_q ** 2

    sV, dimV = reflection_generators(n, ngen, q)
    W = sV[gens[0]]
    for g in gens[1:]:
        W = W * sV[g]

    # per-matrix moduli (sorted desc) for the 2(ngen-1) commutator members
    mods = []
    for a in range(ngen - 1):
        mods.append(moduli(W * sV[a] * sV[a + 1]))
        mods.append(moduli(W * sV[a + 1] * sV[a]))
    r = max(m[0] for m in mods)
    d = q ** (-(L + 2)) * r
    qL = q ** L

    print(f"[bound] A={A} (n={n}); ngen={ngen}, L={L}, Burau dim n-1={dimV}")
    print(f"[bound] r = max spectral radius over {2*(ngen-1)} matrices = {mp.nstr(r,10)};  "
          f"q^L = {mp.nstr(qL,8)};  r/q^L = {mp.nstr(r/qL,8)}")
    print(f"[bound] driver d = q^-(L+2)·r = {mp.nstr(d,8)}  (≈ q^-2·(r/q^L) = {mp.nstr(r/qL/q**2,8)})")
    wm = moduli(W)
    print(f"[bound] sorted Burau moduli of W = ρ^V: {[mp.nstr(x,6) for x in wm]}")
    print(f"        dominant/q^L = {mp.nstr(wm[0]/qL,6)};  subdominant/dominant = {mp.nstr(wm[1]/wm[0],6)}\n")

    print("   j  hook           dim   |tr|          |tr|/dim     B_j(crude)     B'_j(sharp)    |tr|/B'_j   B'_{j+1}/B'_j")
    Bs, Bps, trs, dims = [], [], [], []
    worst_rel, worst_abs = mp.mpf(0), mp.mpf(0)
    for j in range(0, n):
        k = n - j
        hook = tuple([k] + [1] * j)
        cf = mp.re(hook_closed_form(k, n, W, sV, ngen, q, L))
        direct, dim = projector_curvature_trace(hook, gens, q)
        direct = mp.re(direct)
        if j == 0 or j == n - 1:
            worst_abs = max(worst_abs, abs(cf - direct))          # exact-zero endpoints: absolute
        else:
            worst_rel = max(worst_rel, abs(cf - direct) / abs(direct))
        Tj = coef * q ** ((L + 2) * (1 - j))
        B = Tj * 2 * (ngen - 1) * mp.mpf(math.comb(n - 1, j)) * r ** j
        Bp = Tj * sum(elem_sym_from_eigs(m)[j] for m in mods)
        Bs.append(B); Bps.append(Bp); trs.append(abs(direct)); dims.append(dim)
    for j in range(0, n):
        step = (Bps[j + 1] / Bps[j]) if j + 1 < n else None
        ratio = trs[j] / Bps[j]
        print(f"  {j:>2}  {str(tuple([n-j]+[1]*j)):<14} {dims[j]:>4}  {mp.nstr(trs[j],8):>10}  "
              f"{mp.nstr(trs[j]/dims[j],6):>9}  {mp.nstr(Bs[j],7):>12}  {mp.nstr(Bps[j],7):>12}  "
              f"{mp.nstr(ratio,4):>8}  {(mp.nstr(step,6) if step is not None else '—'):>10}")

    print()
    ok1 = worst_rel < REL_TOL and worst_abs < ABS_ZERO_TOL
    print(f"  (1) self-check closed form vs direct: interior worst |Δ_rel| = {mp.nstr(worst_rel,3)}, "
          f"endpoint worst |Δ_abs| = {mp.nstr(worst_abs,3)}  {'✓' if ok1 else '✗'}")
    holds = all(trs[j] <= Bs[j] * (1 + mp.mpf(10) ** -30) for j in range(n))
    holds_p = all(trs[j] <= Bps[j] * (1 + mp.mpf(10) ** -30) for j in range(n))
    print(f"  (2) bounds HOLD?  crude B_j: {'YES ✓' if holds else 'NO ✗'}   sharp B'_j: {'YES ✓' if holds_p else 'NO ✗'}")
    # The arc's decay target is PER DIMENSION: |tr(ρ_λ Ω)|/dim_λ (the single-window bound
    # |tr| = o(dim)). For hooks dim = C(n−1, j). Raw |tr| itself need not be monotone from j=1
    # (at A=3 it peaks at j=2: 269 → 371 → 74), and the sharp bound faithfully tracks that bump —
    # so the raw-B' monotonicity is reported but the PER-DIM one is the verdict that matters.
    decays = all(Bs[j + 1] < Bs[j] for j in range(1, n - 1))
    decays_p_raw = all(Bps[j + 1] < Bps[j] for j in range(1, n - 1))
    decays_p_dim = all(Bps[j + 1] / dims[j + 1] < Bps[j] / dims[j] for j in range(0, n - 1))
    tr_dim_mono = all(trs[j + 1] / dims[j + 1] < trs[j] / dims[j] for j in range(1, n - 1))
    print(f"  (3) DECAY?  crude B_j (raw, j≥1): {'YES' if decays else 'NO (binomial hump)'}   "
          f"sharp B'_j (raw, j≥1): {'YES' if decays_p_raw else 'NO (tracks the real |tr| bump)'}")
    print(f"      sharp PER-DIM B'_j/C(n-1,j) strictly decreasing for ALL j ≥ 0?  "
          f"{'YES ✓' if decays_p_dim else 'NO ✗'}     (actual |tr|/dim monotone for j≥1: {'yes' if tr_dim_mono else 'no'})")
    print("      B'_j/dim: " + ", ".join(mp.nstr(Bps[j] / dims[j], 5) for j in range(n)))
    tight = max(trs[j] / Bps[j] for j in range(1, n - 1))
    print(f"      sharp-bound tightness: max_j |tr|/B'_j over interior j = {mp.nstr(tight,4)}")
    if holds_p and decays_p_dim:
        print("      ⇒ the SHARP bound PER DIMENSION is strictly decreasing in b(λ)=j: the hook column of")
        print("        the gauge-invariant curvature satisfies |tr_hook|/dim_hook ≤ B'_j/C(n−1,j) ↓ — a")
        print("        rigorous decay statement given the Burau moduli. The only inequality used is")
        print("        |e_j(μ)| ≤ e_j(|μ|) (Lean: abs_esymm_le_esymm_abs / abs_mul_sum_esymm_sub_le).")
    elif holds_p:
        print("      ⇒ the sharp bound holds but its per-dim form is not monotone here; a per-matrix")
        print("        triangle inequality does not capture the decay — cancellation must be ACROSS the")
        print("        commutator members (e_j(M⁺) − e_j(M⁻)). That would be the next handle.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, nargs="+", default=[2, 3])
    args = ap.parse_args()
    for A in args.A:
        analyze(A)
        print()


if __name__ == "__main__":
    main()
