#!/usr/bin/env python3
"""
Kähler Padé resummation — numeric (finite-difference) approach.

Previous attempt (`kahler_expansion_variants.py`) was blocked on
sympy.simplify bottleneck inside build_V_hat_symbolic (8.5s per
call, 16 calls per order per atom).

This version:

1. Precompute V̂(q) numerically at a small set of q-values near q₀
   via kahler_lift.build_V_hat_symbolic + .subs — one symbolic
   build, multiple numeric substitutions.
2. Finite-difference derivatives from the value samples.
3. Build the Kähler Taylor series coefficients up to order N.
4. Apply scipy.interpolate.pade for [N/2, N/2] Padé approximant.
5. Evaluate the Padé rational at ℏ_q; compare to direct Taylor
   truncation at the same order.

Purpose: test whether Padé resolves the T/3He Kähler divergence
(session finding: Taylor at order 1+ blows up on T/3He).
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from canonical_plus_multibrane import (HBAR_Q, HBAR_Q_SQ,
                                          E_0_BETA_DECAY_MEV,
                                          tower_mass_level)
from kahler_lift import build_V_hat_symbolic, q as q_sym
from ocneanu_weights import tr_M_via_ocneanu_word


def _numeric_V_hat_at_q(V_hat_sym, q_val: float) -> list[float]:
    """Evaluate each generator's symbolic V̂(q) at a numeric q."""
    return [float(V.subs(q_sym, q_val)) for V in V_hat_sym]


def _finite_diff_coeffs(f_vals: list[float], step: float,
                          order: int) -> list[float]:
    """From 2·order+1 values of a function at q₀ + k·step for
    k = -order..order, extract the Taylor coefficients at q₀ up to
    order (central differences).

    Returns [c_0, c_1, ..., c_order] where f(q₀ + δ) ≈ Σ c_k · δ^k.
    """
    n = len(f_vals)
    mid = n // 2
    # Fit a polynomial of degree `order` through the samples
    xs = np.array([(k - mid) * step for k in range(n)], dtype=float)
    ys = np.array(f_vals, dtype=float)
    # np.polyfit gives highest-order first; we want lowest-order first
    coeffs_high_first = np.polyfit(xs, ys, order)
    coeffs_low_first = coeffs_high_first[::-1]
    return [float(c) for c in coeffs_low_first]


def _build_z_V(V_hat_sym, q_val: float) -> list[float]:
    """z·V̂ evaluated at q_val, per generator.  Matches the
    unified_lift convention."""
    z_val = 1.0 / (np.sqrt(q_val) + 1.0 / np.sqrt(q_val))
    V_vals = _numeric_V_hat_at_q(V_hat_sym, q_val)
    return [z_val * v for v in V_vals]


def compute_kahler_series_and_pade(
        Z: int, N: int, order: int = 6, delta_rel: float = 0.005
        ) -> dict:
    """Compute the Kähler Taylor series z·V̂(q) + ℏ_q · θ(z·V̂) + ...
    at q₀ numerically, plus Padé approximant.

    Uses finite differences in the LOG-q variable (which is the
    Euler-operator's natural coordinate).  Samples V̂(q) at
    q₀ · exp(k · δ) for k = -order..order with δ = delta_rel.
    """
    # One symbolic build per path
    V_sym_atom = build_V_hat_symbolic(Z, N, include_inter=True)
    V_sym_free = build_V_hat_symbolic(Z, N, include_inter=False)
    n_gens = len(V_sym_atom)

    # Sample z·V̂ at q₀·exp(k·δ) for each generator
    ks = list(range(-order, order + 1))
    q_samples = [Q0 * np.exp(k * delta_rel) for k in ks]

    zV_atom_samples = [_build_z_V(V_sym_atom, q) for q in q_samples]
    zV_free_samples = [_build_z_V(V_sym_free, q) for q in q_samples]

    result = {"order": order, "delta_rel": delta_rel, "ks": ks,
                "generators": [], "free_generators": []}

    for i in range(n_gens):
        atom_vals = [zV_atom_samples[j][i] for j in range(len(ks))]
        free_vals = [zV_free_samples[j][i] for j in range(len(ks))]
        # Taylor coefficients in the log-q variable (step = delta_rel)
        a_atom = _finite_diff_coeffs(atom_vals, delta_rel, order)
        a_free = _finite_diff_coeffs(free_vals, delta_rel, order)
        # Direct Taylor evaluation at log-step = ℏ_q
        taylor_atom = sum(a_atom[k] * HBAR_Q**k for k in range(order + 1))
        taylor_free = sum(a_free[k] * HBAR_Q**k for k in range(order + 1))
        # Padé [m/m] from these Taylor coefficients — try multiple
        # numerator/denominator splits; NaN on [3/3] doesn't mean
        # NaN on [2/4] or [4/2].
        pade_results = {}
        try:
            import scipy.interpolate as si
            for split in ((2, 4), (3, 3), (4, 2)):
                m, n_d = split
                if m + n_d > order:
                    continue
                try:
                    p_atom, q_atom = si.pade(a_atom, m)
                    p_free, q_free = si.pade(a_free, m)
                    pa = float(p_atom(HBAR_Q) / q_atom(HBAR_Q))
                    pf = float(p_free(HBAR_Q) / q_free(HBAR_Q))
                    if np.isfinite(pa) and np.isfinite(pf):
                        pade_results[f"pade_{m}_{n_d}"] = {
                            "atom": pa, "free": pf}
                except Exception:
                    pass
        except Exception:
            pass
        pade_atom = (pade_results.get("pade_3_3", {}).get("atom")
                      or pade_results.get("pade_2_4", {}).get("atom")
                      or pade_results.get("pade_4_2", {}).get("atom")
                      or float('nan'))
        pade_free = (pade_results.get("pade_3_3", {}).get("free")
                      or pade_results.get("pade_2_4", {}).get("free")
                      or pade_results.get("pade_4_2", {}).get("free")
                      or float('nan'))
        # Direct eval (Borel-sum): V̂(q₀·exp(ℏ_q))
        direct_atom = float(V_sym_atom[i].subs(q_sym, Q0 * np.exp(HBAR_Q)))
        direct_free = float(V_sym_free[i].subs(q_sym, Q0 * np.exp(HBAR_Q)))
        # (z·V̂)(shifted q)
        q_shift = Q0 * np.exp(HBAR_Q)
        z_shift = 1.0 / (np.sqrt(q_shift) + 1.0 / np.sqrt(q_shift))
        direct_zV_atom = z_shift * direct_atom
        direct_zV_free = z_shift * direct_free
        result["generators"].append({
            "i": i,
            "taylor_coeffs_log_q": a_atom,
            "taylor_at_hbar_q": taylor_atom,
            "pade_at_hbar_q": pade_atom,
            "direct_zV_shifted_q": direct_zV_atom,
        })
        result["free_generators"].append({
            "i": i,
            "taylor_coeffs_log_q": a_free,
            "taylor_at_hbar_q": taylor_free,
            "pade_at_hbar_q": pade_free,
            "direct_zV_shifted_q": direct_zV_free,
        })

    return result


def binding_from_vhat(V_atom_1: list[float], V_free_1: list[float],
                        E_0: float = E_0_BETA_DECAY_MEV) -> float:
    """Binding via the single-level ℏ_q² tower formula."""
    m_a = tower_mass_level(V_atom_1, pair_mode="full")
    m_f = tower_mass_level(V_free_1, pair_mode="full")
    return E_0 * HBAR_Q_SQ * (m_f - m_a)


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1,  2.22452),
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
    ]

    print("=" * 110)
    print("KÄHLER PADÉ PROBE (numeric, no sympy per-order build)")
    print(f"q0 = {Q0}, ℏ_q = {HBAR_Q:.4f}")
    print("=" * 110)

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        print(f"\n{name} (Z={Z}, N={N}, A={A})")
        t0 = time.time()
        try:
            r = compute_kahler_series_and_pade(Z, N, order=6)
            dt = time.time() - t0
            V_taylor_atom = [g["taylor_at_hbar_q"] for g in r["generators"]]
            V_taylor_free = [g["taylor_at_hbar_q"] for g in r["free_generators"]]
            V_pade_atom = [g["pade_at_hbar_q"] for g in r["generators"]]
            V_pade_free = [g["pade_at_hbar_q"] for g in r["free_generators"]]
            V_direct_atom = [g["direct_zV_shifted_q"] for g in r["generators"]]
            V_direct_free = [g["direct_zV_shifted_q"] for g in r["free_generators"]]
            # Canonical trace
            tr_a = abs(tr_M_via_ocneanu_word(Z, N, include_inter=True))
            tr_f = abs(tr_M_via_ocneanu_word(Z, N, include_inter=False))
            canon = E_0_BETA_DECAY_MEV * (tr_f - tr_a)
            # Three tower values under three expansions
            B_taylor = canon + binding_from_vhat(V_taylor_atom, V_taylor_free)
            B_pade = canon + binding_from_vhat(V_pade_atom, V_pade_free)
            B_direct = canon + binding_from_vhat(V_direct_atom, V_direct_free)
            err_t = abs(B_taylor - B_AME) / Mtot * 100
            err_p = abs(B_pade - B_AME) / Mtot * 100
            err_d = abs(B_direct - B_AME) / Mtot * 100
            print(f"  canonical:       {canon:+.4f} MeV")
            print(f"  Taylor order 6:  B = {B_taylor:+.4f}  err = {err_t:.4f}%  ({dt:.1f}s)")
            print(f"  Padé [3/3]:      B = {B_pade:+.4f}    err = {err_p:.4f}%")
            print(f"  direct Borel:    B = {B_direct:+.4f}  err = {err_d:.4f}%")
            results.append({
                "atom": name, "Z": Z, "N": N, "A": A, "B_AME": B_AME,
                "canonical_MeV": canon,
                "taylor": {"B_MeV": B_taylor, "err_pct": err_t},
                "pade":   {"B_MeV": B_pade,   "err_pct": err_p},
                "direct": {"B_MeV": B_direct, "err_pct": err_d},
                "time_sec": dt, "series": r,
            })
        except Exception as e:
            import traceback
            print(f"  ERR: {type(e).__name__}: {e}")
            traceback.print_exc()

    witness = {
        "computation": "kahler-pade-probe",
        "description": (
            "Kähler Padé resummation via numeric finite-difference "
            "derivatives.  Avoids the sympy.simplify bottleneck "
            "(build_V_hat_symbolic is called twice per atom, once "
            "per include_inter flag; results are reused across "
            "order / Padé / direct-eval branches).  Compares "
            "Taylor vs Padé vs direct-Borel evaluation of the "
            "Kähler-lifted V̂ at q₀ · exp(ℏ_q) = 1.225."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "hbar_q": HBAR_Q,
                          "E_0_MeV": E_0_BETA_DECAY_MEV},
        "results": results,
    }
    out = Path(__file__).parent / "kahler-pade-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
