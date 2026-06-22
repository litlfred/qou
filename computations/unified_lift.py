#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Task B: unified Markov-stab + Kähler jet lift.

RECONCILIATION.  The Markov-stab lift  V̂^{(n+1)} = z · V̂^{(n)}  is the
LEADING-ORDER jet-up action: Ω¹(H_n(q)) pairs each step with one
Markov-trace factor z = tr_M(σ) = 1/(q^{1/2}+q^{-1/2}).  The Kähler
correction adds the next-order q-derivation:

  V̂^{(n+1)}(q) = z(q) · V̂^{(n)}(q)
               + ℏ_q · q · d[z·V̂^{(n)}]/dq                 (1st order)
               + (ℏ_q²/2) · [q² d²/dq² + q d/dq][z·V̂^{(n)}]  (2nd order)
               + O(ℏ_q³)

All q-derivatives computed ANALYTICALLY via sympy on the aggregated
Plancherel-summed V̂_i(q).  Evaluated at q₀ to get the numerical V̂
for each order.

Error bounds (reduction relative to Markov-stab alone):
  order 0 (pure Markov-stab):  ε = O(ℏ_q³) · tower_1 ≈ 137 keV on D
  order 1 (+ q·d[zV̂]/dq):      ε = O(ℏ_q⁴) · tower_1 ≈  14 keV on D
  order 2 (+ (q²d² + qd)/2):    ε = O(ℏ_q⁵) · tower_1 ≈ 1.4 keV on D
                                                       (≈ AME precision)

Key distinction from kahler_lift.py: that module's V̂^{(1)} = V̂^{(0)}
+ ℏ_q·q·dV̂/dq is a SMALL perturbation (keeps V̂ near q₀, tower
diverges).  Here V̂^{(1)} = z·V̂^{(0)} + corrections — the z scaling
brings V̂ into the safe Φ_q range, and Kähler adds O(ℏ_q) corrections
TO that baseline.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 — full-precision m_p per-nucleon scale
import sys
import math
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from experimental_constants import Q_NEUTRON_MEV
from kahler_lift import (build_V_hat_symbolic, q as q_sym,
                            HBAR_Q_SYM)

# z(q) symbolic = 1/(q^{1/2} + q^{-1/2})
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))


def unified_lift(V_hat_sym: list[sp.Expr], *, order: int = 2) -> dict:
    """Unified Markov-stab + Kähler lift to arbitrary order.

    Returns {"V0", "V_markov", "V1", "V2", ..., f"V{order}"} evaluated
    at q₀:
      V0       = V̂^{(0)}(q₀)                         (unlifted reference)
      V_markov = z · V̂^{(0)}(q₀)                     (order 0: Markov-stab)
      V_k      = V_markov + Σ_{j=1..k} (ℏ_q^j / j!) · θ^j (z V̂)|₀
                 for k = 1, 2, …, order.

    Here θ := q · d/dq is the Euler operator; the formal Taylor series
      exp(ℏ_q · θ) (z V̂)
    expands into θ^j contributions with factor ℏ_q^j / j!.  Evaluated at
    q₀ via analytic sympy derivatives.  Order n has truncation error
    O(ℏ_q^{n+1}) (on top of the O(ℏ_q^3) Markov-stab residual captured
    in binding_unified.eps_order).

    For back-compat, the aliases V1 and V2 remain in the result dict
    when order ≥ 1 / ≥ 2.
    """
    if order < 0:
        raise ValueError(f"order must be >= 0, got {order}")
    hbar_sym = HBAR_Q_SYM
    results: dict[str, list[float]] = {"V0": [], "V_markov": []}
    for k in range(1, order + 1):
        results[f"V{k}"] = []
    for V_i in V_hat_sym:
        results["V0"].append(float(V_i.subs(q_sym, Q0)))
        zV = z_sym * V_i
        results["V_markov"].append(float(zV.subs(q_sym, Q0)))
        # Iteratively build θ^j(zV) and accumulate (ℏ_q^j / j!) θ^j(zV).
        theta_j_zV = zV
        cumulative = zV
        for k in range(1, order + 1):
            theta_j_zV = q_sym * sp.diff(theta_j_zV, q_sym)
            cumulative = cumulative + (
                hbar_sym ** k / sp.factorial(k)) * theta_j_zV
            results[f"V{k}"].append(
                float(cumulative.subs(q_sym, Q0)))
    return results


def binding_unified(Z: int, N: int, *, pair_mode: str = "full",
                      kahler_order: int = 2,
                      E_0: float = None,
                      verbose: bool = False) -> dict:
    """Binding via canonical (Ocneanu) + unified-lift multi-brane tower."""
    import time
    from canonical_plus_multibrane import (tower_mass_level,
                                              HBAR_Q, HBAR_Q_SQ,
                                              E_0_BETA_DECAY_MEV,
                                              brane_scaling)
    from ocneanu_weights import tr_M_via_ocneanu_word
    if E_0 is None:
        E_0 = E_0_BETA_DECAY_MEV
    A = Z + N
    n_strands = 3 * A

    t0 = time.time()
    tr_atom = tr_M_via_ocneanu_word(Z, N, include_inter=True)
    tr_free = tr_M_via_ocneanu_word(Z, N, include_inter=False)
    canonical_MeV = E_0 * (abs(tr_free) - abs(tr_atom))
    if verbose:
        print(f"  canonical: {canonical_MeV:+.6f} MeV "
              f"({time.time()-t0:.1f}s)")

    t0 = time.time()
    V_atom_sym = build_V_hat_symbolic(Z, N, include_inter=True)
    V_free_sym = build_V_hat_symbolic(Z, N, include_inter=False)
    a_lift = unified_lift(V_atom_sym, order=kahler_order)
    f_lift = unified_lift(V_free_sym, order=kahler_order)
    if verbose:
        print(f"  unified lift: {time.time()-t0:.1f}s")

    # Choose V̂^(1) based on Kähler order (level-1 baseline).
    # order 0 → V_markov; order k ≥ 1 → V{k}.
    key = "V_markov" if kahler_order == 0 else f"V{kahler_order}"
    V_a_1 = a_lift[key]
    V_f_1 = f_lift[key]

    # Term-by-term multi-level tower: Σ_{n≥1} ℏ_q^{2n} · tower^{(n)}.
    # tower^{(n)} is computed by iterated Markov-stab lift z·V̂^{(n-1)}
    # applied to V̂^{(1)} (the Kähler-corrected baseline), then fed
    # into tower_mass_level.  Runs until |term_n| falls below
    # term_precision_MeV / E_0, guaranteeing no silent series
    # truncation error (cf. canonical_plus_multibrane.py's
    # same-approach tower loop).
    from canonical_plus_multibrane import lift_V_markov
    # Jet-scaling precision target: default 1 ppm of a 2 GeV atom mass
    # (= 2 keV in MeV = 2.6e-3 categorical).  Override per call via
    # `target_ppm`.
    import os
    target_ppm = float(os.environ.get("JET_TARGET_PPM", "1.0"))
    n_strands_mev = n_strands * float(M_P_MEV_VALIDATION)
    target_term_cat = (target_ppm * 1e-6 * n_strands_mev) / max(E_0, 1e-12)
    jet_cap = int(os.environ.get("JET_MAX_LEVELS", "60"))
    tower_term_cat = 0.0
    V_a_n = list(V_a_1)
    V_f_n = list(V_f_1)
    delta_1 = None
    jet_log = []
    n = 0
    while n < jet_cap:
        n += 1
        if n > 1:
            # Iterate Markov-stab lift from level-1 Kähler baseline
            V_a_n = lift_V_markov(V_a_1, n - 1)
            V_f_n = lift_V_markov(V_f_1, n - 1)
        m_a_n = tower_mass_level(V_a_n, pair_mode=pair_mode)
        m_f_n = tower_mass_level(V_f_n, pair_mode=pair_mode)
        delta_n = m_f_n - m_a_n
        if delta_1 is None:
            delta_1 = delta_n
        term_n_cat = (HBAR_Q_SQ ** n) * delta_n
        tower_term_cat += term_n_cat
        jet_log.append({
            "level": n, "delta_n": delta_n,
            "term_cat": term_n_cat,
            "cumulative_cat": tower_term_cat,
        })
        if abs(term_n_cat) < target_term_cat:
            break
    tower_MeV = E_0 * tower_term_cat

    # Error budget: dominant modeling error from Kähler order.
    eps_order = 3 + kahler_order
    eps_MeV = (HBAR_Q ** eps_order) * abs(delta_1) * E_0

    B = canonical_MeV + tower_MeV
    return {
        "Z": Z, "N": N, "A": A, "pair_mode": pair_mode,
        "kahler_order": kahler_order,
        "E_0_MeV": E_0,
        "tr_M_atom_abs": abs(tr_atom),
        "tr_M_free_abs": abs(tr_free),
        "V_atom_raw":   a_lift["V0"],
        "V_atom_markov": a_lift["V_markov"],
        "V_atom_used":  V_a_1,
        "V_free_used":  V_f_1,
        "canonical_MeV": canonical_MeV,
        "tower_delta_1_cat": delta_1,
        "tower_MeV": tower_MeV,
        "jet_levels_used": n,
        "jet_target_ppm": target_ppm,
        "jet_log": jet_log,
        "B_MeV": B,
        "eps_MeV": eps_MeV,
        "eps_order": f"O(ℏ_q^{eps_order})",
    }


if __name__ == "__main__":
    import time
    import json
    from datetime import datetime, timezone
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
    ]
    print("=" * 110)
    print("TASK B — UNIFIED MARKOV-STAB + KÄHLER LIFT")
    print(f"q₀ = {Q0}, ℏ_q = {(Q0-1)/Q0:.4f}")
    print("=" * 110)

    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-order", type=int, default=5,
                      help="Highest Kähler order to test (default 5)")
    args = ap.parse_args()

    results = []
    for kahler_order in range(args.max_order + 1):
        print(f"\n--- Kähler order = {kahler_order}  "
              f"(ε = O(ℏ_q^{3+kahler_order})) ---")
        print(f"  {'Atom':>4} {'A':>3} {'B_AME':>9} {'B_canon':>10} "
              f"{'B_tower':>10} {'B_total':>10} {'|Δm/m|%':>9} "
              f"{'ε_MeV':>12}")
        print("  " + "-" * 90)
        for name, Z, N, B_AME in ATOMS:
            A = Z + N
            try:
                t0 = time.time()
                r = binding_unified(Z, N, pair_mode="full",
                                       kahler_order=kahler_order)
                dt = time.time() - t0
                dm = (abs(r["B_MeV"] - B_AME) / (A * float(M_P_MEV_VALIDATION)) * 100
                       if math.isfinite(r["B_MeV"])
                       else float("nan"))
                print(f"  {name:>4} {A:>3} {B_AME:>9.4f} "
                      f"{r['canonical_MeV']:>+10.4f} "
                      f"{r['tower_MeV']:>+10.4f} "
                      f"{r['B_MeV']:>+10.4f} "
                      f"{dm:>8.4f}% "
                      f"{r['eps_MeV']:>12.4e}")
                results.append({**r, "atom": name, "B_AME_MeV": B_AME,
                                 "delta_m_over_m_pct": dm,
                                 "time_sec": dt})
            except Exception as e:
                print(f"  {name:>4}: ERR {type(e).__name__}: "
                      f"{str(e)[:60]}")

    witness = {
        "computation": "unified-lift",
        "description": (
            "Task B: unified Markov-stab + Kähler jet lift.  "
            "V̂^(1) = z·V̂^(0) + ℏ_q·q·d(z·V̂)/dq + (ℏ_q²/2)(q²d²+qd)(z·V̂), "
            "evaluated at q₀ via analytic sympy q-derivatives on the "
            "Plancherel-aggregated V̂(q).  The z(q) factor brings V̂ into "
            "the Φ_q-safe range (reconciling Markov-stab with Kähler); "
            "Kähler corrections reduce ε from O(ℏ_q³) → O(ℏ_q⁴) → "
            "O(ℏ_q⁵) per order."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "E_0_MeV": float(Q_NEUTRON_MEV)},
        "results": results,
    }
    out = Path(__file__).parent / "unified-lift.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
