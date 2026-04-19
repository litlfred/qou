#!/usr/bin/env python3
"""
Magic-reordered atom braid for binding — one uniform algorithm.

Per magic-unfold-peel.md's core-first-then-valence reordering, applied
to the H_A 3-channel tower.  For each atom, find the largest
doubly-magic pair (Z_c, N_c) ≤ (Z, N), reorder the nucleons with core
nucleons first and valence nucleons after, then compute B via the
standard tower formula on this reordering.

The magic peel is VACUOUS (ordering unchanged from interleaved) when
no doubly-magic pair fits under (Z, N) — so the algorithm reduces to
direct tower on sub-magic atoms with no special case.

This captures core-valence coupling via the inter-nucleon crossings
at the core-valence boundary of the reordered braid.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV

q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1 / q_sym
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
W_SYM = 1.0 / (qint2**2 + 2)
W_STD = qint2**2 / (qint2**2 + 2)
W_ALT = W_SYM

MAGIC = {2, 8, 20, 28, 50, 82, 126}


def largest_doubly_magic_core(Z, N):
    best = (0, 0)
    for zc in MAGIC:
        if zc > Z:
            continue
        for nc in MAGIC:
            if nc > N:
                continue
            if zc + nc > best[0] + best[1]:
                best = (zc, nc)
    return best


def interleaved_ordering(Z, N):
    o = []
    pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


def magic_reordered_ordering(Z, N):
    """Core-first-then-valence ordering.  When (Z_c, N_c)=(0, 0) the
    peel is vacuous and this equals `interleaved_ordering(Z, N)`."""
    Zc, Nc = largest_doubly_magic_core(Z, N)
    core = interleaved_ordering(Zc, Nc)
    valence = interleaved_ordering(Z - Zc, N - Nc)
    return core + valence, (Zc, Nc)


def ln_phi_q(v, max_k=500):
    if v == 0:
        return 0.0
    s = 0.0
    for k in range(1, max_k + 1):
        f = 1.0 - qi0**k * v
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15:
            break
    return s


def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1:
        return (sp.Integer(1), sp.Integer(0))
    elif ti == 0 and tj == 0:
        return (sp.Integer(1), -HA_sym)
    else:
        return (sp.Integer(1), -HA_sym / 2)


def per_gen_volumes(gen_idx, ordering, m_pp=1, m_pn=1, m_nn=1):
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
    gluon = [(sp.Integer(1), sp.Integer(0))] * (
        2 if ordering[gen_idx] == 1 else 4)
    for c, d in gluon:
        a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                 sp.expand(a * c + b * d))
        sp_v = sp.expand(sp_v * (c * q_sym + d))
        ap_v = sp.expand(ap_v * (-c / q_sym + d))
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        ti, tj = ordering[gen_idx], ordering[j]
        if ti == 1 and tj == 1:
            m = m_pp
        elif ti == 0 and tj == 0:
            m = m_nn
        else:
            m = m_pn
        for _ in range(m):
            a, b = (sp.expand(a * c * HA_sym + a * d + b * c),
                     sp.expand(a * c + b * d))
            sp_v = sp.expand(sp_v * (c * q_sym + d))
            ap_v = sp.expand(ap_v * (-c / q_sym + d))
    return sp_v, z_sym * a + b, ap_v


def B_on_ordering(Z, N, ordering, m_pp=1, m_pn=1, m_nn=1):
    A = len(ordering)
    if A < 2:
        return 0.0
    Bs = Bd = Ba = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen_volumes(i, ordering, m_pp, m_pn, m_nn)
        Bs += ln_phi_q(abs(float(vs.subs(q_sym, q0))))
        Bd += ln_phi_q(abs(float(vd.subs(q_sym, q0))))
        Ba += ln_phi_q(abs(float(va.subs(q_sym, q0))))
    return (W_SYM * M_E_MEV * Bs
              + W_STD * M_E_MEV * Bd
              + W_ALT * M_E_MEV * Ba)


AME = {
    "D":   2.224566, "T":   8.481798, "3He": 7.718058,
    "4He": 28.295674, "6Li": 31.994571, "7Li": 39.244529,
    "9Be": 58.164980, "12C": 92.161728,
}


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1),   ("T",   1, 2),   ("3He", 2, 1),
        ("4He", 2, 2),   ("6Li", 3, 3),   ("7Li", 3, 4),
        ("9Be", 4, 5),   ("12C", 6, 6),
    ]

    print("=" * 130)
    print("MAGIC-REORDERED BINDING — one uniform rule, core-first-then-valence")
    print(f"MAGIC = {sorted(MAGIC)}")
    print("=" * 130)
    print(f"\n  {'atom':>6} {'Z':>2} {'N':>2}  "
          f"{'core':>8} {'ordering_std':>14} {'ordering_mgc':>14}  "
          f"{'B_std':>10} {'B_mgc':>10} {'B_AME':>10} "
          f"{'err_std':>9} {'err_mgc':>9} {'delta':>10}")
    print("  " + "-" * 128)

    results = []
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        B_AME = AME[name]

        ord_std = interleaved_ordering(Z, N)
        ord_mgc, (Zc, Nc) = magic_reordered_ordering(Z, N)

        B_std = B_on_ordering(Z, N, ord_std)
        B_mgc = B_on_ordering(Z, N, ord_mgc)

        err_std = abs(B_std - B_AME) / Mtot * 100
        err_mgc = abs(B_mgc - B_AME) / Mtot * 100

        core_str = f"({Zc},{Nc})"
        ord_std_str = "".join("p" if t == 1 else "n" for t in ord_std)
        ord_mgc_str = "".join("p" if t == 1 else "n" for t in ord_mgc)

        marker = ""
        if ord_std == ord_mgc:
            marker = " (vacuous)"
        elif err_mgc < err_std:
            marker = " ✓"
        elif err_mgc > err_std * 1.5:
            marker = " ✗"

        print(f"  {name:>6} {Z:>2} {N:>2}  "
              f"{core_str:>8} {ord_std_str:>14} {ord_mgc_str:>14}  "
              f"{B_std:>+10.4f} {B_mgc:>+10.4f} {B_AME:>+10.4f} "
              f"{err_std:>8.4f}% {err_mgc:>8.4f}% "
              f"{B_mgc-B_std:>+10.4f}" + marker)

        results.append({
            "atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME,
            "core_Z": Zc, "core_N": Nc,
            "ordering_standard": ord_std_str,
            "ordering_magic_reordered": ord_mgc_str,
            "peel_vacuous": ord_std == ord_mgc,
            "B_standard_MeV": B_std, "B_magic_MeV": B_mgc,
            "delta_MeV": B_mgc - B_std,
            "err_standard_pct": err_std, "err_magic_pct": err_mgc,
        })

    # Summary
    improved = [r for r in results
                    if not r["peel_vacuous"]
                    and r["err_magic_pct"] < r["err_standard_pct"]]
    worsened = [r for r in results
                    if not r["peel_vacuous"]
                    and r["err_magic_pct"] > r["err_standard_pct"]]
    vacuous = [r for r in results if r["peel_vacuous"]]
    print(f"\n  peel vacuous: {[r['atom'] for r in vacuous]}")
    print(f"  magic reorder IMPROVES: {[r['atom'] for r in improved]}")
    print(f"  magic reorder WORSENS: {[r['atom'] for r in worsened]}")

    out = Path(__file__).parent / "magic-reordered-binding.witness.json"
    out.write_text(json.dumps({
        "computation": "magic-reordered-binding",
        "description": (
            "Uniform algorithm: for each atom, reorder nucleons to "
            "core-first-then-valence where core = largest doubly-magic "
            "pair ≤ (Z, N). Apply standard H_A 3-channel tower on this "
            "reordering. Magic peel is VACUOUS (ordering unchanged) for "
            "sub-magic atoms. Captures core-valence coupling natively "
            "via the inter-nucleon crossings at the reordered boundary."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                          "MAGIC": sorted(MAGIC),
                          "W_sym": W_SYM, "W_std": W_STD, "W_alt": W_ALT},
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
