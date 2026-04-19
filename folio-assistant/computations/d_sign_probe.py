#!/usr/bin/env python3
"""
Probe subtractive mechanisms for D's over-prediction.

Per user (2026-04-19):
  "1. Probe formula sign conventions on D (what if B = |tr_atom|
      − |tr_free| for small A)?"
  "2. Look for subtractive terms (negative-weight channels,
      complementary irreps)?"

Two variants:

A. Sign flip: standard B = Σ_λ w_λ m_e Σ_i ln|Φ_q(V^λ)| with the
   sign of each channel tied to the sign of V^λ (not |V^λ|).  This
   allows negative per-channel contributions.

B. Negative alt-channel weight: w_alt → −w_alt (partition-conjugate
   of sym is alt; treating them as +/− pair models particle/antiparticle).
   Keeps w_sym > 0, w_std > 0, w_alt < 0.

Test on D, T, 3He, 4He, 6Li, 7Li.  Record which over-predicting
atoms benefit, whether 4He (which was already close) gets hurt.
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


def ground_state(Z, N):
    o = []
    pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


def compute_B_variants(Z, N):
    A = Z + N
    if A < 2:
        return None
    ordering = ground_state(Z, N)
    # Accumulate per-channel sums WITH SIGN of V
    Bs_abs = Bd_abs = Ba_abs = 0.0
    Bs_sgn = Bd_sgn = Ba_sgn = 0.0
    for i in range(A - 1):
        vs, vd, va = per_gen_volumes(i, ordering)
        vs_q = float(vs.subs(q_sym, q0))
        vd_q = float(vd.subs(q_sym, q0))
        va_q = float(va.subs(q_sym, q0))
        ls = ln_phi_q(abs(vs_q))
        ld = ln_phi_q(abs(vd_q))
        la = ln_phi_q(abs(va_q))
        Bs_abs += ls
        Bd_abs += ld
        Ba_abs += la
        # Signed variant: sign(V) × ln|Φ_q(|V|)|
        Bs_sgn += (1 if vs_q >= 0 else -1) * ls
        Bd_sgn += (1 if vd_q >= 0 else -1) * ld
        Ba_sgn += (1 if va_q >= 0 else -1) * la

    # Default (all |V|)
    B_default = (W_SYM * M_E_MEV * Bs_abs
                   + W_STD * M_E_MEV * Bd_abs
                   + W_ALT * M_E_MEV * Ba_abs)
    # Variant A: use sign(V) per channel
    B_signed = (W_SYM * M_E_MEV * Bs_sgn
                  + W_STD * M_E_MEV * Bd_sgn
                  + W_ALT * M_E_MEV * Ba_sgn)
    # Variant B: negative alt-channel weight
    B_neg_alt = (W_SYM * M_E_MEV * Bs_abs
                   + W_STD * M_E_MEV * Bd_abs
                   - W_ALT * M_E_MEV * Ba_abs)
    # Variant C: negative alt + signed (both)
    B_signed_neg_alt = (W_SYM * M_E_MEV * Bs_sgn
                          + W_STD * M_E_MEV * Bd_sgn
                          - W_ALT * M_E_MEV * Ba_sgn)
    return {
        "B_default": B_default,
        "B_signed": B_signed,           # sign(V) · ln|Φ_q|
        "B_neg_alt": B_neg_alt,          # w_alt → −w_alt
        "B_signed_neg_alt": B_signed_neg_alt,
        "per_channel": {
            "V_sym_at_q0": float(per_gen_volumes(0, ordering)[0].subs(q_sym, q0)),
            "V_std_at_q0": float(per_gen_volumes(0, ordering)[1].subs(q_sym, q0)),
            "V_alt_at_q0": float(per_gen_volumes(0, ordering)[2].subs(q_sym, q0)),
            "Bs_abs": Bs_abs, "Bd_abs": Bd_abs, "Ba_abs": Ba_abs,
            "Bs_sgn": Bs_sgn, "Bd_sgn": Bd_sgn, "Ba_sgn": Ba_sgn,
        },
    }


AME = {
    "D":   2.224566, "T":   8.481798, "3He": 7.718058,
    "4He": 28.295674, "6Li": 31.994571, "7Li": 39.244529,
}


if __name__ == "__main__":
    ATOMS = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1),
                ("4He", 2, 2), ("6Li", 3, 3), ("7Li", 3, 4)]

    print("=" * 130)
    print("D SIGN PROBE — sign-flipped / negative-alt variants")
    print(f"q0 = {q0}  w_sym={W_SYM:.4f}  w_std={W_STD:.4f}  w_alt={W_ALT:.4f}")
    print("=" * 130)
    print(f"\n  {'atom':>6} {'Z':>2} {'N':>2}  "
          f"{'default':>10} {'signed':>10} {'neg_alt':>10} {'signed_neg_alt':>15}  "
          f"{'B_AME':>10}  "
          f"{'err_def':>8} {'err_sgn':>8} {'err_na':>8} {'err_sna':>8}")
    print("  " + "-" * 120)

    results = []
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        B_AME = AME[name]
        v = compute_B_variants(Z, N)

        err_def = abs(v["B_default"] - B_AME) / Mtot * 100
        err_sgn = abs(v["B_signed"] - B_AME) / Mtot * 100
        err_na = abs(v["B_neg_alt"] - B_AME) / Mtot * 100
        err_sna = abs(v["B_signed_neg_alt"] - B_AME) / Mtot * 100

        # Highlight best
        min_err = min(err_def, err_sgn, err_na, err_sna)

        def mark(e):
            return " *" if abs(e - min_err) < 1e-6 else "  "

        print(f"  {name:>6} {Z:>2} {N:>2}  "
              f"{v['B_default']:>+10.4f} {v['B_signed']:>+10.4f} "
              f"{v['B_neg_alt']:>+10.4f} {v['B_signed_neg_alt']:>+15.4f}  "
              f"{B_AME:>+10.4f}  "
              f"{err_def:>7.4f}%{mark(err_def)} {err_sgn:>6.4f}%{mark(err_sgn)} "
              f"{err_na:>6.4f}%{mark(err_na)} {err_sna:>6.4f}%{mark(err_sna)}")

        results.append({
            "atom": name, "Z": Z, "N": N, "B_AME": B_AME,
            **v,
            "err_default_pct": err_def,
            "err_signed_pct": err_sgn,
            "err_neg_alt_pct": err_na,
            "err_signed_neg_alt_pct": err_sna,
        })

    # Count which variant wins per atom
    winners = {"default": 0, "signed": 0, "neg_alt": 0, "signed_neg_alt": 0}
    for r in results:
        errs = [("default", r["err_default_pct"]),
                  ("signed", r["err_signed_pct"]),
                  ("neg_alt", r["err_neg_alt_pct"]),
                  ("signed_neg_alt", r["err_signed_neg_alt_pct"])]
        winner = min(errs, key=lambda x: x[1])[0]
        winners[winner] += 1
    print(f"\n  Wins per variant: {winners}")

    out = Path(__file__).parent / "d-sign-probe.witness.json"
    out.write_text(json.dumps({
        "computation": "d-sign-probe",
        "description": (
            "Probe subtractive mechanisms: (signed) use sign(V) in "
            "each channel instead of |V|; (neg_alt) flip w_alt sign; "
            "(signed_neg_alt) both. Tests whether any variant can "
            "reduce D's over-prediction via native subtraction."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                          "W_sym": W_SYM, "W_std": W_STD, "W_alt": W_ALT},
        "winners_per_variant": winners,
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
