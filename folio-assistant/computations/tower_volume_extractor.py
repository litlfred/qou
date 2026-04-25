#!/usr/bin/env python3
"""
Tower volume extractor — test the density-volume hypothesis.

HYPOTHESIS.  The paper's topological mass formula says
    𝔪(K) = Vol(K) / ℏ_q²
which can be rewritten as the classical mass–density–volume equation
    𝔪 = ρ · Vol,   ρ = 1/ℏ_q² = q²/(q-1)²   ≈ 101.8 at q₀.

If this is literal, then each jet level n should contribute a mass
    𝔪^(n) = ℏ_q^(2n) · V_n
where V_n is a level-n "categorical volume" that stays ROUGHLY
CONSTANT in n (or matches a smooth geometric quantity like
hyperbolic volume).

PROBE.  Run binding_canonical_plus_multibrane at
n_brane_levels = 1, 2, 3, ... and extract the per-level delta:

    Δ^(n) := 𝔪_free^(n) - 𝔪_atom^(n)      (categorical units)
    V_n   := Δ^(n) / ℏ_q^{2(n-1)}          (density-normalised volume)

Note: Δ^(n) already carries a ℏ_q^(2n) scaling inside tower_term, but
we want RAW per-level values so we undo one factor of ℏ_q^{2(n-1)}
to see if V_n converges.  Actually the cleanest extraction:

    V_n_raw := Δ^(n)_unscaled    (i.e. tower_mass_level output before
                                    multiplying by brane_scaling)

If V_n stabilises as n grows → density interpretation holds.
If V_n grows or decays → density is level-dependent.

Compares D, T, ³He and reports per-level V_n.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0
from canonical_plus_multibrane import (tower_mass_level, lift_V_markov,
                                           HBAR_Q, HBAR_Q_SQ,
                                           per_gen_V_hat_aggregated)
from mass_endomorphism import z_mark
from mass_at_3A_proper import phi_q_safe


def tower_transient_only(V, *, pair_mode="full", cap_frac=0.98):
    """Paper-correct level-n contribution: singletons + pairs only.

    Per updated rem:mass-endomorphism-jet-tower, the descended product
    |Π V̂| is level-0 only; levels n ≥ 1 contribute just:
        Σ_i Φ_q(|V̂_i|) + z² Σ_{i<j} Φ_q(|V̂_i V̂_j|).
    """
    n = len(V)
    if n == 0:
        return 0.0
    single = sum(phi_q_safe(abs(v), cap_frac=cap_frac) for v in V)
    cross = 0.0
    if pair_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                cross += z_mark ** 2 * phi_q_safe(
                    abs(V[i] * V[j]), cap_frac=cap_frac)
    elif pair_mode == "adjacent":
        for i in range(n - 1):
            cross += z_mark ** 2 * phi_q_safe(
                abs(V[i] * V[i + 1]), cap_frac=cap_frac)
    return single + cross


def per_level_delta_raw(Z: int, N: int, *, n_levels: int = 8,
                           pair_mode: str = "full") -> dict:
    """Return raw per-level Δ^(n) = m_free^(n) − m_atom^(n) (cat units),
    BEFORE ℏ_q^{2n} brane scaling.

    Also returns density-interpreted V_n = Δ^(n) / ℏ_q^{2n} which
    should be ≈ constant if q²/(q-1)² is the effective density.
    """
    V_atom_0 = per_gen_V_hat_aggregated(Z, N, include_inter=True)
    V_free_0 = per_gen_V_hat_aggregated(Z, N, include_inter=False)
    per_level = []
    for n in range(0, n_levels + 1):
        V_a = lift_V_markov(V_atom_0, n)
        V_f = lift_V_markov(V_free_0, n)
        m_a = tower_mass_level(V_a, pair_mode=pair_mode)
        m_f = tower_mass_level(V_f, pair_mode=pair_mode)
        delta = m_f - m_a
        # Density-normalised "volume" at level n
        V_n_density = delta * (HBAR_Q_SQ ** n) if n > 0 else delta
        # Alternative: V_n_raw (without brane scaling)
        per_level.append({
            "n": n,
            "m_atom_n": m_a,
            "m_free_n": m_f,
            "delta_n_raw": delta,
            "hbar_q_2n": HBAR_Q_SQ ** n,
            "mass_contribution_scaled": (HBAR_Q_SQ ** n) * delta,
            "V_n_if_density_ρ": delta / (1.0 / HBAR_Q_SQ) if n == 0
                else delta * (HBAR_Q_SQ ** (n - 1)),
        })
    return {"Z": Z, "N": N, "A": Z + N,
             "pair_mode": pair_mode, "n_levels": n_levels,
             "rho_q": 1.0 / HBAR_Q_SQ,
             "per_level": per_level}


if __name__ == "__main__":
    print("=" * 100)
    print("TOWER VOLUME EXTRACTOR — test ρ = 1/ℏ_q² hypothesis")
    print(f"  q₀ = {q0:.6f}")
    print(f"  ℏ_q = {HBAR_Q:.6f},  ℏ_q² = {HBAR_Q_SQ:.6e}")
    print(f"  proposed density ρ = 1/ℏ_q² = {1.0/HBAR_Q_SQ:.4f}")
    print("=" * 100)

    ATOMS = [
        ("D",    1, 1),
        ("T",    1, 2),
        ("3He",  2, 1),
    ]

    results = []
    for name, Z, N in ATOMS:
        print(f"\n{'=' * 80}")
        print(f"Atom: {name}  (Z={Z}, N={N}, A={Z+N})")
        print("=" * 80)
        r = per_level_delta_raw(Z, N, n_levels=8)
        r["atom"] = name
        results.append(r)
        print(f"  {'n':>3} {'Δ_n (raw)':>16} {'ℏ_q^(2n)':>14} "
              f"{'m^(n) (scaled)':>18} {'V_n = Δ·ℏ_q^(2(n-1))':>24}")
        for p in r["per_level"]:
            print(f"  {p['n']:>3} {p['delta_n_raw']:>+16.4e} "
                  f"{p['hbar_q_2n']:>14.4e} "
                  f"{p['mass_contribution_scaled']:>+18.4e} "
                  f"{p['V_n_if_density_ρ']:>+24.4e}")

    # Analysis: is V_n roughly constant?
    print(f"\n{'=' * 80}")
    print("DENSITY HYPOTHESIS TEST — is V_n roughly level-independent?")
    print("=" * 80)
    print("(If 𝔪 = ρ·V literally, then V_n = Δ^(n) · ℏ_q^{2(n-1)} "
          "should be constant in n)")
    print()
    for r in results:
        V_list = [p["V_n_if_density_ρ"]
                   for p in r["per_level"] if p["n"] >= 1]
        V_vals = [v for v in V_list if math.isfinite(v)]
        if not V_vals:
            continue
        V_mean = sum(V_vals) / len(V_vals)
        V_std = (sum((v - V_mean) ** 2 for v in V_vals) / len(V_vals)) ** 0.5
        V_min, V_max = min(V_vals), max(V_vals)
        print(f"  {r['atom']:>4}: V_n range = [{V_min:+.4e}, {V_max:+.4e}]")
        print(f"         mean = {V_mean:+.4e}, std = {V_std:.4e}")
        print(f"         std/|mean| = {V_std/abs(V_mean) if V_mean else float('nan'):.4f}  "
              f"(ideally ≪ 1 if density hypothesis holds)")
        # Also report the ratio V_{n+1}/V_n
        ratios = []
        for a, b in zip(V_vals[:-1], V_vals[1:]):
            if a != 0:
                ratios.append(b / a)
        if ratios:
            rmean = sum(ratios) / len(ratios)
            print(f"         V_{'{n+1}'}/V_n ratios: "
                  f"{[f'{x:+.3f}' for x in ratios[:6]]}")
            print(f"         mean ratio = {rmean:+.4f}  "
                  f"(1.0 = constant, z² = {z_mark**2:.4f} = "
                  f"Markov-stab decay)")

    # Also note Markov-stab geometric prediction: under V̂^(n) = z^n V̂^(0),
    # the ratio V_{n+1}/V_n approaches z² · (something) in the limit.
    # If instead ratio = 1, density is truly constant.

    witness = {
        "computation": "tower-volume-extractor",
        "description": (
            "Test the density-volume hypothesis: if 𝔪 = ρ·V with "
            "ρ = 1/ℏ_q² (from topological-mass-formula), then the "
            "per-level mass contribution 𝔪^(n) = ℏ_q^{2n}·Δ^(n) "
            "should factor into a constant density times a level-n "
            "volume.  Extract V_n = Δ^(n)·ℏ_q^{2(n-1)} and check "
            "whether it stabilises with n.  If constant, q effectively "
            "plays the role of density in the categorical mass formula.  "
            "If V_n decays geometrically, the density is level-dependent."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "hbar_q": HBAR_Q, "hbar_q_sq": HBAR_Q_SQ,
            "rho_q_proposed": 1.0 / HBAR_Q_SQ,
            "pair_mode": "full",
        },
        "atoms": results,
    }
    out = Path(__file__).parent / "tower-volume-extractor.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
