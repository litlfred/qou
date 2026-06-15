#!/usr/bin/env python3
"""
Per-braid HYBRID jet-level extension — A.3 of the truncation-audit
workplan ([2026-05-02-truncation-audit.md](../../docs/audits/2026-05-02-truncation-audit.md)).

Extends `per_braid_tower_hybrid.py` from level-0-only to a sum
over jet levels n = 0..N_jet plus a geometric-series tail bound.
The full mass-tower jet form per
[`rem:mass-endomorphism-jet-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-jet-tower.md)
is

    m = |tr_M(W)| + Σ_{n=0}^{N} (Σ_{ξ∈S_1^(n)} Φ_q(|tr_M(ξ)|)
                                 + z² Σ_{(ξ,ξ')∈S_2^(n)} Φ_q(|tr_M(ξξ')|))
        + R_N

where R_N is the geometric-series tail bound from
[`prop:jet-tower-convergence`](../../content/quantum-observable-universe/braids-and-knots/jet-tower-convergence.md).

## Jet lift used here

This module is a **scaffold** — the true jet lift requires the
explicit Kähler-differential action on H_n(q), which is open
([`prop:jet-stratified-reduction`](../../content/quantum-observable-universe/braids-and-knots/jet-stratified-reduction.md)).
We use the q-Plancherel-descent lift from
[`jet_lifted_hecke.qplancherel_avg_T`](jet_lifted_hecke.py): at
strand count n, the level-1 trace transitions to level 0 with
factor T_q(n).

For the per-braid hybrid, the analogous scaffold is to scale
each sub-braid trace at level n by T_q(strand_count)^n. This is
**atom-dependent** (T depends on the sub-braid strand count),
unlike a universal geometric series — so it can in principle
tighten the per-atom spread, not just shift the mean.

## What this scaffold does NOT do

It does **not** compute genuinely new tr_M values at level n via
the jet-prolonged Hecke algebra. The level-n contributions are
the level-0 traces scaled multiplicatively. This is a known
approximation; if it narrows the spread, deeper jet-prolongation
work is justified.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from per_braid_tower_hybrid import per_braid_mass_hybrid, _safe_phi
from q_parameter import Q as Q0_FLOAT

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(Q0_FLOAT))
qi0 = 1 / q0
hbar_q = (q0 - 1) / q0  # standard ℏ_q
hbar_q_sq = hbar_q ** 2
z_mark = 1 / (q0 ** mpmath.mpf("0.5") + qi0 ** mpmath.mpf("0.5"))

M_E_MEV = 0.51099895000


# ── q-Plancherel transition factor (inlined from jet_lifted_hecke; ──
# that module has a hard pyhecke dep that's awkward in this scaffold).
_QPLANCH_CACHE: dict[int, float] = {}


def _q_int(n, q):
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def _q_fact(n, q):
    p = mpmath.mpf(1)
    for k in range(1, n + 1):
        p *= _q_int(k, q)
    return p


def _q_dim(lam, q):
    """q-dimension via hook lengths."""
    if not lam or sum(lam) == 0:
        return mpmath.mpf(1)
    n = sum(lam)
    nfac = _q_fact(n, q)
    hook_prod = mpmath.mpf(1)
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hook = arm + leg + 1
            hook_prod *= _q_int(hook, q)
    return nfac / hook_prod


def _partitions_of(n):
    if n == 0:
        return [()]
    out = []
    def gen(remaining, cap, prefix):
        if remaining == 0:
            out.append(tuple(prefix))
            return
        for k in range(min(cap, remaining), 0, -1):
            gen(remaining - k, k, prefix + [k])
    gen(n, n, [])
    return out


def _removable_corners(lam):
    corners = []
    for i in range(len(lam)):
        if i == len(lam) - 1 or lam[i] > lam[i + 1]:
            corners.append(i)
    return corners


def qplancherel_avg_T(n: int) -> mpmath.mpf:
    """Plancherel-averaged box-addition transition factor n → n+1.
    Inlined from jet_lifted_hecke. Asymptote 1/[n+1]_q for large n."""
    if n in _QPLANCH_CACHE:
        return _QPLANCH_CACHE[n]
    LARGE_N = 14
    if n + 1 > LARGE_N:
        bracket = _q_int(n + 1, q0)
        T = max(mpmath.mpf("1e-9"), min(z_mark, 1 / bracket))
        _QPLANCH_CACHE[n] = T
        return T
    parts = _partitions_of(n + 1)
    nfac = _q_fact(n + 1, q0)
    q_nplus1 = _q_int(n + 1, q0)
    total = mpmath.mpf(0)
    for lam in parts:
        dq_lam = _q_dim(lam, q0)
        if dq_lam == 0:
            continue
        w_lam = (dq_lam ** 2) / nfac
        t_lam = mpmath.mpf(0)
        for ci in _removable_corners(lam):
            lam_list = list(lam)
            lam_list[ci] -= 1
            if lam_list[ci] == 0:
                lam_list = lam_list[:ci]
            lam_prime = tuple(lam_list)
            dq_prime = _q_dim(lam_prime, q0)
            if dq_prime == 0:
                continue
            t_lam += dq_prime / (q_nplus1 * dq_lam)
        total += w_lam * t_lam
    _QPLANCH_CACHE[n] = total
    return total


AME_MASS_MEV = {
    "D":    1875.61294257,
    "3He":  2808.39148127,
    "3H":   2808.92113298,
    "4He":  3727.37909409,
    "6Li":  5603.05182,
    "7Li":  6535.36573,
    "9Be":  8392.74912,
    "12C": 11177.9292,
    "16O": 14899.16828,
    "40Ca": 37224.9202,
}


def _T_at(n_strands: int, *, default_floor: float = 1e-6) -> mpmath.mpf:
    """Per-level multiplicative factor at given sub-braid strand count.

    Uses q-Plancherel-averaged T from jet_lifted_hecke. Clamped
    to the Markov stabilization floor (z) to avoid runaway.
    """
    T = qplancherel_avg_T(max(1, n_strands))
    T_mp = mpmath.mpf(str(T))
    T_mp = min(T_mp, z_mark)
    return T_mp


def per_braid_mass_hybrid_jet(Z: int, N: int, N_jet: int = 1,
                                include_tail: bool = True) -> dict:
    """Per-braid HYBRID with jet-level sum n=0..N_jet + tail bound.

    Args
    ----
    Z, N : int
        Proton / neutron counts.
    N_jet : int, default 1
        Highest jet level summed (0 = level-0-only, reproduces
        per_braid_mass_hybrid).
    include_tail : bool, default True
        If True, add the geometric tail bound R_N.

    Returns
    -------
    dict with keys: Z, N, A, level_0_total, jet_corrections,
    tail_bound, total_with_jet, level_per_n.
    """
    A = Z + N

    # ── Level 0: existing hybrid (q-Hecke descended + q=1 MN tower) ──
    level0 = per_braid_mass_hybrid(Z, N)
    m_level0 = level0["total"]

    # ── Compute level-n contributions via T-scaled sub-braid traces ──
    # Three q-Plancherel transition factors:
    #   T_3A : descended (3A-strand braid)
    #   T_1  : per-nucleon (1-strand sub-braid; T(1) ≈ 1, trivial)
    #   T_2  : per-pair (2-strand sub-braid)
    T_3A = _T_at(3 * A)
    T_pair = _T_at(2)

    level_per_n = [{
        "n": 0,
        "desc": float(level0["desc_q_hecke"]),
        "single": float(level0["single"]) if not mpmath.isinf(level0["single"]) else float("inf"),
        "cross": float(level0["cross"]) if not mpmath.isinf(level0["cross"]) else float("inf"),
        "m_n": float(m_level0),
    }]

    jet_total = mpmath.mpf(0)
    for n in range(1, N_jet + 1):
        # Descended at level n: scaled by (z·T_3A)^n (Markov stabilization
        # with q-Plancherel descent on the 3A-strand braid).
        scale_desc = (z_mark * T_3A) ** n
        desc_n = level0["desc_q_hecke"] * scale_desc

        # Per-nucleon at level n: scaled by T_1^n (≈ 1, so per-nucleon
        # contributes weakly to jet spread). We keep the trace value
        # the same (T_1=1) but the Φ_q is recomputed at the scaled
        # value.
        # Per-pair at level n: scaled by T_pair^n.
        # tr_pp/nn/pn^(n) = T_pair^n · tr_pp/nn/pn^(0)
        # The level-n single/cross terms apply Φ_q to the SCALED traces.
        scale_pair = T_pair ** n
        # Reconstruct sub-braid traces from level0
        # We don't keep them separately on level0; recompute.
        from per_braid_tower_hybrid import _cached_sub_braid_trace
        tr_p = _cached_sub_braid_trace(1, 0, False) if Z > 0 else mpmath.mpf(0)
        tr_n = _cached_sub_braid_trace(0, 1, False) if N > 0 else mpmath.mpf(0)
        tr_pp = _cached_sub_braid_trace(2, 0, True) if Z >= 2 else mpmath.mpf(0)
        tr_nn = _cached_sub_braid_trace(0, 2, True) if N >= 2 else mpmath.mpf(0)
        tr_pn = _cached_sub_braid_trace(1, 1, True) if Z >= 1 and N >= 1 else mpmath.mpf(0)

        single_n = mpmath.mpf(0)
        if Z > 0 and tr_p > 0:
            single_n += Z * _safe_phi(tr_p * (T_pair ** 0))  # T_1 ≈ 1
        if N > 0 and tr_n > 0:
            single_n += N * _safe_phi(tr_n * (T_pair ** 0))

        cross_n = mpmath.mpf(0)
        n_pp = Z * (Z - 1) // 2
        n_nn = N * (N - 1) // 2
        n_pn = Z * N
        if n_pp > 0 and tr_pp > 0:
            cross_n += n_pp * _safe_phi(tr_pp * scale_pair)
        if n_nn > 0 and tr_nn > 0:
            cross_n += n_nn * _safe_phi(tr_nn * scale_pair)
        if n_pn > 0 and tr_pn > 0:
            cross_n += n_pn * _safe_phi(tr_pn * scale_pair)
        cross_n *= z_mark ** 2

        # Level-n contribution: subtract level-0 (since the level-0
        # sums above used unscaled traces). Actually, the jet remark
        # ADDS m^(n) to m^(0); each m^(n) is its own quadratic form.
        # For n ≥ 1, the "single" piece is unchanged (T_1=1), so it
        # would re-add the per-nucleon contribution. To avoid double-
        # counting, we report the DELTA from level 0 for the cross
        # piece, and 0 for the single piece (since T_1=1 makes them
        # identical to level 0).
        # The descended-at-level-n is purely additive (it's a new term
        # at level n, not present at level 0 in the same form).
        m_n = abs(desc_n) + cross_n - level0["cross"]  # delta vs level 0
        jet_total += m_n
        level_per_n.append({
            "n": n,
            "desc": float(desc_n) if not mpmath.isinf(desc_n) else float("inf"),
            "single": float(single_n) if not mpmath.isinf(single_n) else float("inf"),
            "cross": float(cross_n) if not mpmath.isinf(cross_n) else float("inf"),
            "m_n": float(m_n) if not mpmath.isinf(m_n) else float("inf"),
        })

    # ── Tail bound via prop:jet-tower-convergence ──
    # |R_N| ≤ Δ_max · ℏ_q^{2(N+1)} / (1 − ℏ_q²)
    # Estimate Δ_max ≈ |level-0 mass| (most pessimistic).
    tail = mpmath.mpf(0)
    if include_tail and N_jet < 10:
        Delta_max = abs(m_level0)
        tail = Delta_max * (hbar_q_sq ** (N_jet + 1)) / (1 - hbar_q_sq)

    total_with_jet = m_level0 + jet_total + (tail if include_tail else mpmath.mpf(0))

    return {
        "Z": Z, "N": N, "A": A,
        "level_0_total": float(m_level0),
        "jet_corrections": float(jet_total),
        "tail_bound": float(tail),
        "total_with_jet": float(total_with_jet),
        "level_per_n": level_per_n,
        "T_3A": float(T_3A),
        "T_pair": float(T_pair),
        "scale_desc_per_level": float(z_mark * T_3A),
    }


if __name__ == "__main__":
    print("=" * 100)
    print("Per-braid HYBRID jet-level extension (A.3) — N_jet = 1")
    print("=" * 100)
    print(f"q_0 = {q0}")
    print(f"ℏ_q²  = {float(hbar_q_sq):.6f}")
    print(f"z     = {float(z_mark):.6f}")
    print(f"m_e   = {M_E_MEV} MeV")
    print()

    ATOMS = [
        ("D", 1, 1),
        ("3He", 2, 1),
        ("3H", 1, 2),
        ("4He", 2, 2),
        ("6Li", 3, 3),
        ("7Li", 3, 4),
        ("9Be", 4, 5),
        ("12C", 6, 6),
        ("16O", 8, 8),
        ("40Ca", 20, 20),
    ]

    N_JET_VALUES = [0, 1, 2]

    all_results = {}
    for N_jet in N_JET_VALUES:
        print()
        print("─" * 100)
        print(f"  N_jet = {N_jet}")
        print("─" * 100)
        print(f"  {'Atom':>5} {'A':>3} {'level0':>14} {'jet_corr':>14} "
              f"{'tail':>10} {'total':>14} {'AME':>12} {'cal/m_e':>12}")
        print("  " + "-" * 95)
        atom_rows = []
        ratios = []
        for name, Z, N in ATOMS:
            t0 = time.time()
            out = per_braid_mass_hybrid_jet(Z, N, N_jet=N_jet)
            t = time.time() - t0
            ame = AME_MASS_MEV[name]
            total_f = out["total_with_jet"]
            cal_constant = ame / total_f if total_f != 0 else float("nan")
            cal_over_me = cal_constant / M_E_MEV
            ratios.append(cal_over_me)
            print(f"  {name:>5} {Z+N:>3} {out['level_0_total']:>14.6e} "
                  f"{out['jet_corrections']:>14.6e} "
                  f"{out['tail_bound']:>10.4e} "
                  f"{total_f:>14.4e} {ame:>12.4f} {cal_over_me:>12.8f}  "
                  f"({t:.1f}s)")
            atom_rows.append({
                "atom": name, "Z": Z, "N": N, "A": Z + N,
                "level_0_total": out["level_0_total"],
                "jet_corrections": out["jet_corrections"],
                "tail_bound": out["tail_bound"],
                "total_with_jet": total_f,
                "ame_mass_mev": ame,
                "cal_over_me": cal_over_me,
                "T_3A": out["T_3A"],
                "scale_desc_per_level": out["scale_desc_per_level"],
            })
        mean_ratio = sum(ratios) / len(ratios)
        spread = (max(ratios) - min(ratios)) / mean_ratio * 100
        print()
        print(f"  Mean cal/m_e = {mean_ratio:.6f}, spread = {spread:.4f}%")
        all_results[N_jet] = {
            "atoms": atom_rows,
            "mean_cal_over_me": mean_ratio,
            "spread_percent": spread,
        }

    # Compare spreads across N_jet
    print()
    print("=" * 100)
    print("Spread comparison across N_jet (does jet truncation close cal/m_e spread?)")
    print("=" * 100)
    print(f"  {'N_jet':>8} {'mean cal/m_e':>14} {'spread %':>12}")
    for N_jet in N_JET_VALUES:
        r = all_results[N_jet]
        print(f"  {N_jet:>8} {r['mean_cal_over_me']:>14.6f} "
              f"{r['spread_percent']:>12.4f}")

    out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-02-per-braid-hybrid-jet.witness.json"
    out_path.write_text(json.dumps({
        "audit": "Per-braid HYBRID jet-level extension (A.3 of truncation audit)",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(q0),
        "hbar_q_sq": float(hbar_q_sq),
        "z_mark": float(z_mark),
        "m_e_mev": M_E_MEV,
        "n_jet_values": N_JET_VALUES,
        "results_by_n_jet": all_results,
        "interpretation": (
            "A.3 scaffold — uses q-Plancherel-descent lift on sub-braid "
            "traces to estimate jet-level n contributions. NOT a true "
            "jet-prolonged Hecke algebra computation. Tests whether "
            "atom-dependent jet corrections (T depends on strand count) "
            "tighten the cal/m_e spread relative to N_jet=0."
        ),
    }, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
