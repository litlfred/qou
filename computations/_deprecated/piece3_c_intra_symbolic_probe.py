#!/usr/bin/env python3
"""
Symbolic investigation of c_intra ≈ -0.114·α at q_0.

The empirical per-nucleon intra log-sum is c_intra/α ≈ -0.114
(see piece3-interface-vs-intra.witness.json). For a single nucleon
in isolation (Z=1, N=0 OR Z=0, N=1), the intra log-sum is the
per-generator ln|V_i^full| over the 2 H_3 generators.

This probe:
  1. Computes ln|V_i^full| symbolically (high-precision mpmath) for
     proton and neutron in H_3, isolated.
  2. Tries to express the resulting numbers as combinations of
     {q_0, ℏ_q, c_q, [n]_q, ln q_0, …}.
  3. Reports any matches within 0.01%.

Output: piece3-c-intra-symbolic.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_MP  # noqa: E402
from hecke_core import atom_per_generator_volumes  # noqa: E402

q = Q_MP

# Categorical constants
h_bar_q = (q - 1) / q
c_q     = 1 / (q - 1)
z_mark  = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
n2_q    = q + 1 / q
n3_q    = (q ** 3 - q ** -3) / (q - 1 / q)
ln_q    = mp.log(q)
G_CATALAN = mp.catalan


def per_nucleon_intra_log_sum(Z: int, N: int) -> dict:
    """Per-nucleon intra log-sum at high precision."""
    vols = atom_per_generator_volumes(Z, N, include_inter=False)
    log_sum = mp.mpf(0)
    log_terms = []
    for v in vols:
        x = mp.mpf(v["full"])
        log_v = mp.log(abs(x)) if abs(x) > mp.mpf("1e-30") else mp.mpf(0)
        log_sum += log_v
        log_terms.append(float(log_v))
    return {
        "Z": Z, "N": N,
        "n_gens": len(vols),
        "log_terms": log_terms,
        "log_sum": float(log_sum),
        "log_sum_mpf": str(log_sum),
    }


def main() -> int:
    print("=" * 96)
    print(f"  Symbolic investigation of c_intra at q_0 = {float(q):.10f}")
    print("=" * 96)

    # Isolated proton, neutron
    p = per_nucleon_intra_log_sum(1, 0)
    n = per_nucleon_intra_log_sum(0, 1)

    print(f"\n  Isolated proton (Z=1, N=0, include_inter=False):")
    print(f"    n_generators = {p['n_gens']}")
    for i, t in enumerate(p["log_terms"]):
        print(f"    ln|V_{i}^full| = {t:>+12.8f}")
    print(f"    intra Σ      = {p['log_sum']:>+12.8f}")

    print(f"\n  Isolated neutron (Z=0, N=1, include_inter=False):")
    print(f"    n_generators = {n['n_gens']}")
    for i, t in enumerate(n["log_terms"]):
        print(f"    ln|V_{i}^full| = {t:>+12.8f}")
    print(f"    intra Σ      = {n['log_sum']:>+12.8f}")

    # Categorical-constant candidates
    p_target = abs(mp.mpf(p["log_sum"]))
    n_target = abs(mp.mpf(n["log_sum"]))
    print(f"\n  Categorical constants at q_0 = {float(q):.10f}:")
    constants = {
        "ln q":          float(ln_q),
        "ln (1/q)":      float(-ln_q),
        "ℏ_q":           float(h_bar_q),
        "ℏ_q²":          float(h_bar_q ** 2),
        "z²":            float(z_mark ** 2),
        "[2]_q":         float(n2_q),
        "[3]_q":         float(n3_q),
        "c_q":           float(c_q),
        "8G":            float(8 * G_CATALAN),
        "1/c_q":         float(1 / c_q),
        "1/[3]_q":       float(1 / n3_q),
        "1/[3]_q!":      float(1 / (n2_q * n3_q)),
    }
    for k, v in constants.items():
        print(f"    {k:<10} = {v:+.6f}")

    print(f"\n  Closed-form candidates for intra Σ_p = {float(p['log_sum']):+.8f}:")
    candidates_p = {
        "−ln q":           float(-ln_q),
        "−ℏ_q":            float(-h_bar_q),
        "−ℏ_q²":           float(-h_bar_q ** 2),
        "−12·ℏ_q²":         float(-12 * h_bar_q ** 2),
        "−2·ln q":         float(-2 * ln_q),
        "ln(q^{-1.07})":    float(-1.07 * ln_q),
        "−z² · ½":         float(-z_mark ** 2 / 2),
        "−1/[3]_q · ½":     float(-1 / n3_q / 2),
        "−ℏ_q · 1.124":     float(-h_bar_q * 1.124),
        "−2·ℏ_q² · [2]_q":  float(-2 * h_bar_q ** 2 * n2_q),
        "−6·ℏ_q²·[2]_q":   float(-6 * h_bar_q ** 2 * n2_q),
        "−ℏ_q²·[3]_q!·z⁻²": float(-h_bar_q ** 2 * n2_q * n3_q / z_mark ** 2),
        "−(q−1)·z²·½":     float(-(q - 1) * z_mark ** 2 / 2),
        "−ln([3]_q)·1/[3]_q": float(-mp.log(n3_q) / n3_q),
        "−ln(q)·z²·½":     float(-ln_q * z_mark ** 2 / 2),
        "−ln(q)·[2]_q · z²": float(-ln_q * n2_q * z_mark ** 2),
    }
    p_target_f = float(p["log_sum"])
    for name, val in sorted(candidates_p.items(), key=lambda x: abs(x[1] - p_target_f)):
        err = abs(val - p_target_f) / abs(p_target_f) * 100 if p_target_f != 0 else 0
        marker = " ★" if err < 0.1 else (" ◦" if err < 5 else "")
        print(f"    {name:<28} {val:>+12.6f}  Δ = {(val - p_target_f):>+10.6f}  err = {err:>7.3f}%{marker}")

    print(f"\n  Closed-form candidates for intra Σ_n = {float(n['log_sum']):+.8f}:")
    n_target_f = float(n["log_sum"])
    for name, val in sorted(candidates_p.items(), key=lambda x: abs(x[1] - n_target_f)):
        err = abs(val - n_target_f) / abs(n_target_f) * 100 if n_target_f != 0 else 0
        marker = " ★" if err < 0.1 else (" ◦" if err < 5 else "")
        print(f"    {name:<28} {val:>+12.6f}  Δ = {(val - n_target_f):>+10.6f}  err = {err:>7.3f}%{marker}")

    # Average across nucleon types
    average = (p_target_f + n_target_f) / 2
    print(f"\n  Average (p+n)/2 intra Σ = {average:+.8f}")
    print(f"  Bonus structural identities to test:")
    print(f"    diff (n − p) = {n_target_f - p_target_f:+.8f}")
    print(f"    relative ratio n/p = {n_target_f / p_target_f if p_target_f != 0 else 0:.4f}")

    witness = {
        "computation": "piece3-c-intra-symbolic",
        "description": (
            "Symbolic investigation of c_intra ≈ -0.114·α at q_0. "
            "Tries to express the per-nucleon intra log-sum as a "
            "combination of categorical constants {ln q, ℏ_q, [n]_q, "
            "c_q, z, 8G}. Reports closest matches within 5%."
        ),
        "reference_blocks": [
            "prop:rho-k-graded-expansion",
            "prop:atomic-mass-gb-nf",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(q),
            "ln_q": float(ln_q),
            "h_bar_q": float(h_bar_q),
        },
        "isolated_proton": p,
        "isolated_neutron": n,
        "candidate_formulas": candidates_p,
        "p_target": p_target_f,
        "n_target": n_target_f,
    }
    out = HERE / "piece3-c-intra-symbolic.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
