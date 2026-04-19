#!/usr/bin/env python3
"""
Full-tower binding with intra-nucleon gluons REMOVED from the
per-generator vertex volumes.

Per session deuteron audit (2026-04-19):
  "Gluons live INSIDE the nucleon, not at the inter-nucleon
  junction. For D (A=2), the single generator is the pn
  inter-nucleon bond; counting proton's intranucleon gluons at
  that generator over-weights the proton side and breaks
  reflection symmetry."

Hypothesis: nucleon-internal structure (gluons, B_3 Borromean,
quark confinement) is ALREADY accounted for in the proton and
neutron rest masses m_p = 938.272 MeV and m_n = 939.565 MeV.
Including them in the per-generator V_hat at the inter-nucleon
slot is DOUBLE-COUNTING.

Refactor: per_gen_volumes_no_intra computes V_hat_i^lambda using
ONLY inter-nucleon crossings to later nucleons.  Each generator
represents the inter-nucleon coupling between nucleons i and
[i+1, ..., A-1], no intra-nucleon components.

Compare B_pred with vs without intra-gluon across atoms.
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


def per_gen_volumes_no_intra(gen_idx, ordering, m_pp=1, m_pn=1, m_nn=1):
    """Per-gen per-channel V_hat with ONLY inter-nucleon crossings.

    No gluon, no intra-nucleon B_3, no quark crossings. Those are
    assumed absorbed into the proton/neutron rest masses.
    """
    a, b = sp.Integer(0), sp.Integer(1)
    sp_v, ap_v = sp.Integer(1), sp.Integer(1)
    A = len(ordering)
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


def per_gen_volumes_default(gen_idx, ordering, m_pp=1, m_pn=1, m_nn=1):
    """Default: gluon-included (matches full-tower-mass.py)."""
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


def ground_state(Z, N):
    o = []
    pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


def B_atom(Z, N, per_gen_fn, m_pp=1, m_pn=1, m_nn=1):
    A = Z + N
    if A < 2:
        return 0.0
    ordering = ground_state(Z, N)
    Bs = Bd = Ba = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen_fn(i, ordering, m_pp, m_pn, m_nn)
        Bs += ln_phi_q(abs(float(vs.subs(q_sym, q0))))
        Bd += ln_phi_q(abs(float(vd.subs(q_sym, q0))))
        Ba += ln_phi_q(abs(float(va.subs(q_sym, q0))))
    return (W_SYM * M_E_MEV * Bs
              + W_STD * M_E_MEV * Bd
              + W_ALT * M_E_MEV * Ba)


if __name__ == "__main__":
    ATOMS = [
        ("D",   1,  1,  2.224566),
        ("T",   1,  2,  8.481798),
        ("3He", 2,  1,  7.718058),
        ("4He", 2,  2, 28.295674),
        ("6Li", 3,  3, 31.994571),
        ("7Li", 3,  4, 39.244529),
        ("9Be", 4,  5, 58.164980),
        ("12C", 6,  6, 92.161728),
    ]

    print("=" * 125)
    print("FULL TOWER — INTRA-NUCLEON GLUONS REMOVED from per-gen V_hat")
    print("(gluons assumed absorbed into proton/neutron rest mass)")
    print("=" * 125)
    print(f"\n  {'atom':>6} {'Z':>2} {'N':>2}  "
          f"{'B_default':>10} {'err_def':>9}  "
          f"{'B_no_intra':>11} {'err_no_intra':>12}  "
          f"{'Delta B':>10} {'B_AME':>10}")
    print("  " + "-" * 100)

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272

        B_default = B_atom(Z, N, per_gen_volumes_default)
        B_no_intra = B_atom(Z, N, per_gen_volumes_no_intra)

        err_def = abs(B_default - B_AME) / Mtot * 100
        err_no_intra = abs(B_no_intra - B_AME) / Mtot * 100
        delta_B = B_no_intra - B_default

        marker = "  "
        if err_no_intra < err_def:
            marker = " ✓"  # intra-gluon removal helps
        elif err_no_intra > err_def * 2:
            marker = " ✗"  # intra-gluon removal hurts

        print(f"  {name:>6} {Z:>2} {N:>2}  "
              f"{B_default:>+10.4f} {err_def:>8.4f}%  "
              f"{B_no_intra:>+11.4f} {err_no_intra:>11.4f}%{marker} "
              f"{delta_B:>+10.4f} {B_AME:>+10.4f}")

        results.append({
            "atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME,
            "B_default_MeV": B_default, "err_default_pct": err_def,
            "B_no_intra_MeV": B_no_intra, "err_no_intra_pct": err_no_intra,
            "delta_B_MeV": delta_B,
        })

    # Summary
    helped = [r for r in results
                if r["err_no_intra_pct"] < r["err_default_pct"]]
    hurt = [r for r in results
              if r["err_no_intra_pct"] > r["err_default_pct"]]
    print(f"\n  intra-gluon removal HELPS: {[r['atom'] for r in helped]}")
    print(f"  intra-gluon removal HURTS: {[r['atom'] for r in hurt]}")

    out = Path(__file__).parent / "full-tower-no-intra-gluon.witness.json"
    out.write_text(json.dumps({
        "computation": "full-tower-no-intra-gluon",
        "description": (
            "Comparison: per_gen_volumes with vs without intra-nucleon "
            "gluons. Default includes gluons (2sigma_0 proton / "
            "4sigma_0 neutron); refactored variant removes them, "
            "leaving only inter-nucleon crossings. Hypothesis: "
            "nucleon-internal gluons are absorbed into m_p, m_n "
            "rest masses and should NOT appear in per-generator "
            "V_hat at the inter-nucleon generator."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                          "W_sym": W_SYM, "W_std": W_STD, "W_alt": W_ALT},
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
