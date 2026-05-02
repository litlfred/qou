#!/usr/bin/env python3
"""
Per-braid mass tower — jet-level sum on Coulomb-corrected hybrid.

Implements the FRAMEWORK formula directly:

    𝔪 = Σ_{n=0}^{N} (Σ_ξ Φ_q(|tr_M(ξ^(n))|) + z² Σ_{ξ,ξ'} Φ_q(|tr_M(ξ^(n) ξ'^(n))|)) + R_N

where ξ^(n) is the jet-n prolongation of the level-0 sub-braid ξ
on A_{n+1} = A_n ⊗ Ω¹(A_n) (per def:recursive-brane-tower).

Two prolongation candidates from jet_lifted_hecke.py:
  - Markov-stabilisation: V^(n) = z^n · V^(0)
  - q-Plancherel-descent: V^(n) = T_q(strands)^n · V^(0)

Per docstring of jet_lifted_hecke: both are APPROXIMATIONS to the
true Kähler-differential jet lift; the explicit Ω¹(H_n(q)) action
is open. Using them as principled level-1 contributions per the
framework's lift mechanism — NOT empirical fits.

Tests both lifts on the Coulomb-corrected hybrid (q-Hecke pairs).
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import (
    per_braid_mass_hybrid, _safe_phi, _cached_sub_braid_trace,
    q0, qi0, z_mark, M_E_MEV, AME_MASS_MEV
)
from schur_weyl_q_hecke_v2 import markov_trace_q_hecke_atomic


# Inlined q-Plancherel transition factor (avoid pyhecke dep).
_QP_CACHE = {}


def _q_int(k):
    return (q0 ** k - qi0 ** k) / (q0 - qi0) if k else mpmath.mpf(0)


def _q_fact(n):
    p = mpmath.mpf(1)
    for k in range(1, n + 1):
        p *= _q_int(k)
    return p


def _q_dim(lam):
    if not lam or sum(lam) == 0:
        return mpmath.mpf(1)
    n = sum(lam)
    nfac = _q_fact(n)
    hp = mpmath.mpf(1)
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hp *= _q_int(arm + leg + 1)
    return nfac / hp


def _partitions_of(n):
    if n == 0: return [()]
    out = []
    def gen(rem, cap, prefix):
        if rem == 0:
            out.append(tuple(prefix)); return
        for k in range(min(cap, rem), 0, -1):
            gen(rem - k, k, prefix + [k])
    gen(n, n, [])
    return out


def _removable_corners(lam):
    return [i for i in range(len(lam))
            if i == len(lam) - 1 or lam[i] > lam[i + 1]]


def T_q_plancherel(n: int) -> mpmath.mpf:
    """Plancherel-averaged box-addition factor T_q(n→n+1).

    For n+1 ≤ 14, exact Σ over λ ⊢ n+1 + corners. For larger,
    asymptote 1/[n+1]_q.
    """
    if n in _QP_CACHE: return _QP_CACHE[n]
    if n + 1 > 14:
        T = max(mpmath.mpf("1e-9"), min(z_mark, 1 / _q_int(n + 1)))
        _QP_CACHE[n] = T; return T
    parts = _partitions_of(n + 1)
    nfac = _q_fact(n + 1)
    qn1 = _q_int(n + 1)
    total = mpmath.mpf(0)
    for lam in parts:
        d = _q_dim(lam)
        if d == 0: continue
        w = (d * d) / nfac
        t = mpmath.mpf(0)
        for ci in _removable_corners(lam):
            ll = list(lam); ll[ci] -= 1
            if ll[ci] == 0: ll = ll[:ci]
            dp = _q_dim(tuple(ll))
            if dp == 0: continue
            t += dp / (qn1 * d)
        total += w * t
    _QP_CACHE[n] = total
    return total


# Cache q-Hecke per-pair traces.
_PAIR_QH_CACHE = {}


def qhecke_pair_tr(Zsub, Nsub):
    if (Zsub, Nsub) not in _PAIR_QH_CACHE:
        v, _ = markov_trace_q_hecke_atomic(
            Zsub, Nsub, include_inter=True, dim_cap=5000)
        _PAIR_QH_CACHE[(Zsub, Nsub)] = abs(v)
    return _PAIR_QH_CACHE[(Zsub, Nsub)]


def per_braid_mass_jet(Z: int, N: int, *, N_jet: int = 1,
                         lift: str = "qplancherel",
                         include_tail: bool = True) -> dict:
    """Sum jet levels 0..N_jet of the per-braid mass tower + tail R_N.

    Per framework: m^(n) is the level-n contribution with sub-braid
    traces lifted by the chosen prolongation rule.

    Tail bound from prop:jet-tower-convergence:
      |R_N| ≤ Δ_max · ℏ_q^{2(N+1)} / (1 - ℏ_q²)
    where ℏ_q = (q-1)/q. We estimate Δ_max = level-0 mass.

    lift options:
      - 'qplancherel': V^(n) = T_q(strands)^n · V^(0)
      - 'markov':     V^(n) = z^n · V^(0)
    """
    A = Z + N
    base = per_braid_mass_hybrid(Z, N)

    # Level-0 contributions (already in base)
    desc = base["desc_q_hecke"]
    single0 = base["single"]
    cross0 = base["cross"]

    # Level-0 trace values (need for lifting)
    tr_p = _cached_sub_braid_trace(1, 0, False) if Z > 0 else mpmath.mpf(0)
    tr_n = _cached_sub_braid_trace(0, 1, False) if N > 0 else mpmath.mpf(0)
    tr_pp = qhecke_pair_tr(2, 0) if Z >= 2 else mpmath.mpf(0)
    tr_nn = qhecke_pair_tr(0, 2) if N >= 2 else mpmath.mpf(0)
    tr_pn = qhecke_pair_tr(1, 1) if Z >= 1 and N >= 1 else mpmath.mpf(0)

    # Strand counts for each sub-braid
    strands_single = 3
    strands_pair = 6

    # Level-n contributions for n = 1..N_jet
    n_pp = Z * (Z - 1) // 2
    n_nn = N * (N - 1) // 2
    n_pn = Z * N
    levels = [{"n": 0, "single": float(single0), "cross": float(cross0),
                "m_n": float(single0 + cross0)}]

    total_jet = mpmath.mpf(0)
    for n in range(1, N_jet + 1):
        if lift == "qplancherel":
            f_single = T_q_plancherel(strands_single) ** n
            f_pair = T_q_plancherel(strands_pair) ** n
        elif lift == "markov":
            f_single = z_mark ** n
            f_pair = z_mark ** n
        else:
            raise ValueError(f"unknown lift: {lift}")

        # Lift traces
        tr_p_n = tr_p * f_single
        tr_n_n = tr_n * f_single
        tr_pp_n = tr_pp * f_pair
        tr_nn_n = tr_nn * f_pair
        tr_pn_n = tr_pn * f_pair

        # Compute level-n contribution as Σ Φ_q(lifted trace)
        single_n = mpmath.mpf(0)
        if Z > 0 and tr_p_n > 0:
            single_n += Z * _safe_phi(tr_p_n)
        if N > 0 and tr_n_n > 0:
            single_n += N * _safe_phi(tr_n_n)
        cross_n = mpmath.mpf(0)
        if n_pp > 0 and tr_pp_n > 0:
            cross_n += n_pp * _safe_phi(tr_pp_n)
        if n_nn > 0 and tr_nn_n > 0:
            cross_n += n_nn * _safe_phi(tr_nn_n)
        if n_pn > 0 and tr_pn_n > 0:
            cross_n += n_pn * _safe_phi(tr_pn_n)
        cross_n *= z_mark ** 2

        m_n = single_n + cross_n
        total_jet += m_n
        levels.append({"n": n, "single": float(single_n),
                       "cross": float(cross_n), "m_n": float(m_n)})

    # Tail bound R_N per prop:jet-tower-convergence
    hbar_q_sq = ((q0 - 1) / q0) ** 2  # ≈ 0.0098
    tail = mpmath.mpf(0)
    if include_tail:
        delta_max = abs(single0 + cross0)  # estimate Δ_max as level-0 magnitude
        tail = delta_max * (hbar_q_sq ** (N_jet + 1)) / (1 - hbar_q_sq)

    total = desc + single0 + cross0 + total_jet + tail

    return {
        "Z": Z, "N": N, "A": A, "lift": lift, "N_jet": N_jet,
        "level_0_total": float(single0 + cross0),
        "jet_total": float(total_jet),
        "tail_R_N": float(tail),
        "total": float(total),
        "levels": levels,
    }


if __name__ == "__main__":
    print("=" * 100)
    print("Per-braid mass tower — jet-level sum (framework formula)")
    print("=" * 100)
    print(f"q_0 = {q0}")
    print(f"z = {float(z_mark):.4f}")
    print(f"T_q(3 strands)  = {float(T_q_plancherel(3)):.4f}  (single-nucleon)")
    print(f"T_q(6 strands)  = {float(T_q_plancherel(6)):.4f}  (pair)")
    print()

    ATOMS = [
        ("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2),
        ("6Li", 3, 3), ("7Li", 3, 4), ("9Be", 4, 5),
        ("12C", 6, 6), ("16O", 8, 8), ("40Ca", 20, 20),
    ]

    # Test both lifts at N_jet = 1, 2
    for lift_name in ["qplancherel", "markov"]:
        print()
        print("─" * 100)
        print(f"Lift: {lift_name}")
        print("─" * 100)
        for N_jet in [0, 1, 2, 5, 10]:
            print()
            print(f"  N_jet = {N_jet}")
            print(f"  {'atom':>5} {'A':>3} {'level0':>12} {'jet':>12} "
                  f"{'tail R_N':>10} {'total':>14} {'AME':>12} {'cal/m_e':>10}")
            ratios = []
            for name, Z, N in ATOMS:
                out = per_braid_mass_jet(Z, N, N_jet=N_jet, lift=lift_name)
                ame = AME_MASS_MEV[name]
                total = out["total"]
                cal = (ame / total) / M_E_MEV
                ratios.append(cal)
                print(f"  {name:>5} {Z+N:>3} {out['level_0_total']:>12.4e} "
                      f"{out['jet_total']:>12.4e} {out['tail_R_N']:>10.4e} "
                      f"{total:>14.4e} {ame:>12.4f} {cal:>10.6f}")
            mean = sum(ratios) / len(ratios)
            spread = (max(ratios) - min(ratios)) / mean * 100
            print(f"    mean cal/m_e = {mean:.6f}, spread = {spread:.4f}%")
