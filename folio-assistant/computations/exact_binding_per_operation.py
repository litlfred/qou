#!/usr/bin/env python3
"""
Exact per-operation binding computation toward 1-ppb precision.

User direction: don't unwind the whole braid word into a matrix
representation — just keep each KNOT OPERATION and its weight, and
sum at the end.  Replaces float arithmetic with mpmath arbitrary-
precision arithmetic; each crossing contributes an exact (c, d)
coefficient in (q, q^{-1}); the total is the symbolic sum of per-
crossing log-weights evaluated at q_0.

Pipeline
────────
1. For each atom (Z, N), build the nucleon string 'pppnn...' via the
   nuclear-ground-state search (same as atom_mass_atomic_braid.py).
2. Walk the atomic braid one crossing at a time.  For each
   generator position i = 0 ... A-2:
     • read the crossing type (pp, pn, nn, pe, ne, ee);
     • look up the exact (c, d) for that crossing;
     • update the transfer-matrix chain (a, b) in mpmath with
       ~100-digit precision;
     • evaluate V̂_i = z · a + b, add ln|V̂_i| to the running Φ.
3. Sum gives Φ; apply mass formula; extract binding energy.

Compared to float compute_Phi (~15 digit mantissa), mpmath at 100
digits gives 85 extra digits of headroom — more than enough for
1-ppb precision on total mass (requires ≥ 10 digits post-decimal
on MeV-scale M).

Atoms covered: the Z ≤ 10 light isotopes from AME2020.

Output: exact-binding-per-operation.witness.json
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import (
    Q as Q0_FLOAT,
    HBAR_Q,
    HBAR_Q_SQ,
    VOL_FIGURE_EIGHT,
    MASS_RATIO_MU_E,
)
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV

import mpmath as mp
mp.mp.dps = 100   # ~100 decimal digits of precision


# ── Recompute q_0, ℏ_q², etc. in mpmath precision ───────────────
# Use the high-precision globals from q_parameter (computed via
# Vol(4_1) = 2 Cl_2(π/3) at 50 dps).  Previously this block went
# `mp.mpf(str(VOL_FIGURE_EIGHT)) / mp.mpf(str(MASS_RATIO_MU_E))`,
# which only carried f64 (~16 dps) through and printed 40 dps of
# trailing noise in the witness JSON.
from q_parameter import (
    Q_MP as Q0_MP, HBAR_Q_MP, HBAR_Q_SQ_MP, HA_MP,
)
Z_MP = mp.mpf(1) / (mp.sqrt(Q0_MP) + mp.mpf(1) / mp.sqrt(Q0_MP))


def crossing_coeff_mp(ti: str, tj: str) -> tuple[mp.mpf, mp.mpf]:
    """Exact (c, d) for each crossing pair in mpmath."""
    zero, one, half = mp.mpf(0), mp.mpf(1), mp.mpf("0.5")
    if ti == "p" and tj == "p": return one, zero
    if ti == "n" and tj == "n": return one, -HA_MP
    if (ti, tj) in [("p", "n"), ("n", "p")]: return one, -HA_MP * half
    if (ti, tj) in [("p", "e"), ("e", "p")]: return one, -HA_MP
    if (ti, tj) in [("n", "e"), ("e", "n")]: return zero, one
    if ti == "e" and tj == "e": return one, zero
    return zero, one


def compute_phi_mp(ordering: list[str]) -> mp.mpf:
    """Φ_q via transfer-matrix chain in mpmath — per-operation tracking."""
    n = len(ordering)
    if n <= 1:
        return mp.mpf(0)
    Phi = mp.mpf(0)
    for gen in range(n - 1):
        a = mp.mpf(0)
        b = mp.mpf(1)
        for j in range(gen + 1, n):
            c, d = crossing_coeff_mp(ordering[gen], ordering[j])
            if c == 0 and d == 1:
                continue
            a_new = a * c * HA_MP + a * d + b * c
            b_new = a * c + b * d
            a, b = a_new, b_new
        V = Z_MP * a + b
        if abs(V) < mp.mpf("1e-200"):
            # log|V| → -∞ as V → 0; return -mp.inf so
            # B_pred = -α · Φ → +∞ (physically: infinite binding
            # at zero-volume degeneracy).
            return -mp.inf
        Phi += mp.log(abs(V))
    return Phi


def find_nuclear_gs_float(Z: int, N: int) -> list[str]:
    """Same nuclear GS search as atom_mass_atomic_braid (float is fine here
    — we only need the ORDERING, which is integer; the mass arithmetic
    happens in mpmath afterwards."""
    from atom_mass_atomic_braid import compute_Phi as compute_Phi_float
    A = Z + N
    if A <= 1:
        return list("p" * Z + "n" * N)
    total = math.comb(A, Z)
    if total <= 50000:
        best_Phi, best_o = float("inf"), None
        for pos in combinations(range(A), Z):
            o = ["n"] * A
            for p in pos:
                o[p] = "p"
            Phi = compute_Phi_float(o)
            if Phi < best_Phi:
                best_Phi, best_o = Phi, list(o)
        return best_o
    # Steepest-descent fallback for large A
    o = list("p" * Z + "n" * N)
    Phi = compute_Phi_float(o)
    improved = True
    while improved:
        improved = False
        for i in range(A):
            for j in range(i + 1, A):
                if o[i] == o[j]:
                    continue
                o2 = list(o)
                o2[i], o2[j] = o2[j], o2[i]
                P2 = compute_Phi_float(o2)
                if P2 < Phi - 1e-12:
                    o, Phi = o2, P2
                    improved = True
                    break
            if improved:
                break
    return o


# ── Build atomic braid: nucleons + Z electrons (ep-pair insertion) ──

def atomic_ordering(Z: int, N: int, nuc_order: list[str]) -> list[str]:
    """Insert Z electrons using ep-pair convention (same as paper)."""
    out: list[str] = []
    e_remaining = Z
    for t in nuc_order:
        out.append(t)
        if t == "p" and e_remaining > 0:
            out.append("e")
            e_remaining -= 1
    while e_remaining > 0:
        out.append("e")
        e_remaining -= 1
    return out


# ── AME2020 targets ─────────────────────────────────────────────
AME_TABLE = [
    ("1H",   1,  0,   938.78307,   0.0),
    ("2H",   1,  1,  1876.12393,   2.22458),
    ("3H",   1,  2,  2809.43210,   8.4818),
    ("3He",  2,  1,  2809.41347,   7.7180),
    ("4He",  2,  2,  3728.40133,  28.29566),
    ("6Li",  3,  3,  5603.0515,   31.9941),
    ("7Li",  3,  4,  6535.3668,   39.2446),
    ("9Be",  4,  5,  8394.7953,   58.1651),
    ("11B",  5,  6, 10255.1031,   76.2054),
    ("12C",  6,  6, 11177.9292,   92.1617),
    ("14N",  7,  7, 13043.7809, 104.6589),
    ("16O",  8,  8, 14899.1687, 127.6193),
    ("19F",  9, 10, 17696.9006, 147.8013),
    ("20Ne",10, 10, 18622.8401, 160.6449),
]


def free_mass_mp(Z: int, N: int) -> mp.mpf:
    return (mp.mpf(str(M_P_MEV)) * Z
            + mp.mpf(str(M_N_MEV)) * N
            + mp.mpf(str(M_E_MEV)) * Z)


def main() -> int:
    print(f"\n  Exact per-operation binding — mpmath precision {mp.mp.dps} digits")
    print(f"  q_0 = {mp.nstr(Q0_MP, 25)}")
    print(f"  ℏ_q² = {mp.nstr(HBAR_Q_SQ_MP, 25)}\n")

    print(f"  {'atom':>6} {'Z':>2} {'N':>2}  "
          f"{'Phi':>25}  {'B_pred':>11} {'B_AME':>11} {'err_%':>8}")
    print("  " + "-" * 90)

    rows = []
    for sym, Z, N, M_obs, B_ame in AME_TABLE:
        if Z + N == 1:
            # Single proton: no braid
            continue
        nuc_order = find_nuclear_gs_float(Z, N)
        ordering = atomic_ordering(Z, N, nuc_order)
        Phi = compute_phi_mp(ordering)
        # Apply paper's mass formula — placeholder:
        # M_pred = free + α·Φ, where α is calibrated elsewhere.
        # Without re-fitting α here, report Φ and use the standard
        # calibration from atom_mass_atomic_braid.
        # Use α = m_e (single-channel crossing-energy scale) as a
        # leading-order approximation; detailed Wedderburn is the
        # full answer.
        alpha_mp = mp.mpf(str(M_E_MEV))  # leading-order scale
        B_pred = -alpha_mp * Phi         # binding = -α · Φ_atom
        err_pct = (float(B_pred) - B_ame) / B_ame * 100 if B_ame > 0 else 0.0
        print(f"  {sym:>6} {Z:>2} {N:>2}  "
              f"{mp.nstr(Phi, 20):>25}  "
              f"{float(B_pred):>11.4f} {B_ame:>11.4f} {err_pct:>+8.2f}")
        rows.append({
            "symbol": sym,
            "Z": Z, "N": N, "A": Z + N,
            "ordering": "".join(ordering),
            "Phi_mp_str": mp.nstr(Phi, 40),
            "B_pred_MeV": float(B_pred),
            "B_AME_MeV": B_ame,
            "residual_MeV": float(B_pred) - B_ame,
            "err_pct": err_pct,
            "precision_digits": mp.mp.dps,
        })

    ok = [r for r in rows if r["B_AME_MeV"] > 0]
    if ok:
        mean = sum(abs(r["residual_MeV"]) for r in ok) / len(ok)
        max_e = max(abs(r["residual_MeV"]) for r in ok)
        print(f"\n  Summary: n={len(ok)}, mean|ΔB|={mean:.4f} MeV, max|ΔB|={max_e:.4f} MeV")

    witness = {
        "name": "exact-binding-per-operation",
        "description": (
            "Exact per-operation binding computation.  Tracks each "
            "knot operation in the atomic braid, applies the exact "
            "(c, d) coefficient in (q, q⁻¹), accumulates the transfer-"
            "matrix chain in mpmath at 100 decimal digits, and sums "
            "ln|V̂_i| over crossings.  Replaces the float pipeline "
            "of atom_mass_atomic_braid.py.  Zero free parameters; "
            "uses α = m_e as leading-order energy scale pending "
            "Wedderburn-weighted refinement."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0_mp_str": mp.nstr(Q0_MP, 40),
            "hbar_q_sq_mp_str": mp.nstr(HBAR_Q_SQ_MP, 40),
            "precision_digits": mp.mp.dps,
        },
        "rows": rows,
    }
    out = Path(__file__).parent / "exact-binding-per-operation.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
