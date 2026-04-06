#!/usr/bin/env python3
"""
Tau lepton normal form and leptonic decay witness.

Computes the Hecke-algebra normal forms NF(T_{2,n}) for the charged
lepton tower n = 3, 5, 7 (electron, muon, tau) via the Chebyshev
recurrence in H₂(q), and verifies the algebraic structure of the
leptonic tau decay τ⁻ → e⁻ + ν̄ₑ + ν_τ.

Theory:
    T_{2,n} = σ₀ⁿ in B₂, which maps to H₂(q) with basis {𝟙, σ₀}.
    The Hecke relation σ₀² = (q − q⁻¹)σ₀ + 1 gives a continuant
    recurrence: if NF(σ₀ⁿ) = aₙ·𝟙 + bₙ·σ₀, then
        aₙ₊₁ = bₙ
        bₙ₊₁ = h·bₙ + aₙ      where h = q − q⁻¹.

    The bₙ satisfy the continuant (Morgan-Voyce) recurrence
    bₙ₊₁ = h·bₙ + bₙ₋₁ with b₀ = 0, b₁ = 1.

Usage:
    python3 tau-lepton-nf.py

Output:
    tau-lepton-nf.witness.json
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── Import canonical q ───────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import (
    Q, Q_INV, Q_ERR, HBAR_Q, HBAR_Q_SQ,
    VOL_FIGURE_EIGHT, MASS_RATIO_MU_E,
    HA, E_CROSS,
)

# ── Chebyshev recurrence for NF(σ₀ⁿ) = aₙ·𝟙 + bₙ·σ₀ ──────────

def chebyshev_nf(n_max, h):
    """Compute NF(σ₀ⁿ) for n = 0..n_max via Chebyshev recurrence.

    Returns lists (a, b) where NF(σ₀ⁿ) = a[n]·𝟙 + b[n]·σ₀.

    The recurrence is:
        a₀ = 1, b₀ = 0
        aₙ₊₁ = bₙ
        bₙ₊₁ = h·bₙ + aₙ
    """
    a = [1.0]
    b = [0.0]
    for _ in range(n_max):
        a_new = b[-1]
        b_new = h * b[-1] + a[-1]
        a.append(a_new)
        b.append(b_new)
    return a, b


def main():
    h = HA  # q − q⁻¹

    # Compute NF for T_{2,n} = σ₀ⁿ, n = 0..9
    a, b = chebyshev_nf(9, h)

    # ── Lepton tower ─────────────────────────────────────────────
    leptons = {
        "electron": {"n": 3, "knot": "T_{2,3}", "symbol": "e⁻"},
        "muon":     {"n": 5, "knot": "T_{2,5}", "symbol": "μ⁻"},
        "tau":      {"n": 7, "knot": "T_{2,7}", "symbol": "τ⁻"},
    }

    lepton_nfs = {}
    for name, info in leptons.items():
        n = info["n"]
        lepton_nfs[name] = {
            "n": n,
            "knot": info["knot"],
            "symbol": info["symbol"],
            "a_n (𝟙 coeff)": a[n],
            "b_n (σ₀ coeff)": b[n],
            "net": a[n] + b[n],
        }

    # ── Decay: τ⁻ → e⁻ + ν̄ₑ + ν_τ ──────────────────────────────
    # NF(ν) = 1·𝟙 + 0·σ₀  (neutrino = identity in Hecke)
    # Δ = NF(τ) − NF(e) − 2·NF(ν)
    tau_to_e = {
        "process": "τ⁻ → e⁻ + ν̄ₑ + ν_τ",
        "BR_PDG": 0.1782,
        "delta_1": a[7] - a[3] - 2.0,
        "delta_sigma": b[7] - b[3],
        "delta_net": (a[7] + b[7]) - (a[3] + b[3]) - 2.0,
        "crossings_released": 7 - 3,
    }

    # ── Decay: τ⁻ → μ⁻ + ν̄_μ + ν_τ ─────────────────────────────
    tau_to_mu = {
        "process": "τ⁻ → μ⁻ + ν̄_μ + ν_τ",
        "BR_PDG": 0.1739,
        "delta_1": a[7] - a[5] - 2.0,
        "delta_sigma": b[7] - b[5],
        "delta_net": (a[7] + b[7]) - (a[5] + b[5]) - 2.0,
        "crossings_released": 7 - 5,
    }

    # ── BR ratio check ───────────────────────────────────────────
    # In the Standard Model, BR(τ→e)/BR(τ→μ) ≈ 1.0 (lepton universality)
    # The Hecke NF Δ is an algebraic invariant; the physical rate
    # additionally requires the weak vertex form factor.
    # Check: ratio of Δ_net values
    br_ratio_nf = tau_to_e["delta_net"] / tau_to_mu["delta_net"]

    # ── Mass ratios from NF net amplitudes ───────────────────────
    # The net NF amplitude is the total Hecke weight. Mass ratios
    # via the topological mass formula involve Vol(K)/ℏ_q², but for
    # torus knots (non-hyperbolic, Vol=0), mass comes through the
    # Higgs mechanism coupling at each Reeb degree.
    mass_info = {
        "net_ratio_mu_e": (a[5] + b[5]) / (a[3] + b[3]),
        "net_ratio_tau_e": (a[7] + b[7]) / (a[3] + b[3]),
        "net_ratio_tau_mu": (a[7] + b[7]) / (a[5] + b[5]),
        "note": "Torus knot mass comes from Higgs mechanism (Vol(4₁)/ℏ_q²), not directly from NF net. NF net captures algebraic weight.",
    }

    # ── Full NF table for T_{2,n}, n=0..9 ───────────────────────
    nf_table = []
    for n in range(10):
        nf_table.append({
            "n": n,
            "a_n": a[n],
            "b_n": b[n],
            "net": a[n] + b[n],
        })

    # ── Continuant identity check ───────────────────────────────
    # bₙ satisfies the continuant recurrence bₙ₊₁ = h·bₙ + bₙ₋₁
    # (Morgan-Voyce type, NOT standard Chebyshev-U which has −bₙ₋₁).
    # Verify: bₙ₊₁ − h·bₙ − bₙ₋₁ = 0 for all n ≥ 1.
    continuant_check = []
    for n in range(1, 9):
        residual = b[n + 1] - h * b[n] - b[n - 1]
        continuant_check.append({
            "n": n,
            "b_{n+1}": b[n + 1],
            "h*b_n + b_{n-1}": h * b[n] + b[n - 1],
            "residual": residual,
            "match": abs(residual) < 1e-12,
        })

    # ── Build witness ────────────────────────────────────────────
    witness = {
        "title": "Tau lepton NF and leptonic decay — T_{2,n} Chebyshev tower",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": Q,
            "q_err": Q_ERR,
            "h (q−q⁻¹)": h,
            "hbar_q": HBAR_Q,
            "hbar_q_sq": HBAR_Q_SQ,
            "Vol(4_1)": VOL_FIGURE_EIGHT,
            "m_μ/m_e": MASS_RATIO_MU_E,
        },
        "lepton_nfs": lepton_nfs,
        "tau_to_electron_decay": tau_to_e,
        "tau_to_muon_decay": tau_to_mu,
        "BR_ratio_NF (tau→e / tau→μ)": br_ratio_nf,
        "mass_ratios_from_net": mass_info,
        "nf_table_T2n": nf_table,
        "continuant_recurrence_check": continuant_check,
    }

    # ── Print summary ────────────────────────────────────────────
    print("=" * 70)
    print("  TAU LEPTON NF — Chebyshev tower T_{2,n} in H₂(q)")
    print("=" * 70)
    print(f"\n  q = {Q:.10f},  h = q−q⁻¹ = {h:.10f}\n")

    print("  NF(T_{2,n}) = aₙ·𝟙 + bₙ·σ₀")
    print("  " + "-" * 55)
    for n in range(10):
        label = ""
        if n == 3: label = " ← electron"
        elif n == 5: label = " ← muon"
        elif n == 7: label = " ← tau"
        print(f"  n={n}:  a={a[n]:12.8f}  b={b[n]:12.8f}  net={a[n]+b[n]:.8f}{label}")

    print(f"\n  --- Continuant recurrence: bₙ₊₁ = h·bₙ + bₙ₋₁ ---")
    all_match = all(c["match"] for c in continuant_check)
    print(f"  All match: {all_match}")

    print(f"\n  --- Leptonic tau decay ---")
    for d in [tau_to_e, tau_to_mu]:
        print(f"  {d['process']}:")
        print(f"    Δ(𝟙)  = {d['delta_1']:+.8f}")
        print(f"    Δ(σ₀) = {d['delta_sigma']:+.8f}")
        print(f"    Δ(net) = {d['delta_net']:+.8f}")
        print(f"    Crossings released: {d['crossings_released']}")
        print(f"    PDG BR: {d['BR_PDG']}")

    print(f"\n  NF Δ ratio (τ→e)/(τ→μ) = {br_ratio_nf:.6f}")
    print(f"  PDG BR ratio            = {0.1782/0.1739:.6f}")
    print(f"  (Lepton universality predicts ≈ 1.0)")

    print(f"\n  --- Net amplitude ratios ---")
    print(f"  net(μ)/net(e) = {mass_info['net_ratio_mu_e']:.6f}")
    print(f"  net(τ)/net(e) = {mass_info['net_ratio_tau_e']:.6f}")
    print(f"  net(τ)/net(μ) = {mass_info['net_ratio_tau_mu']:.6f}")

    # ── Write witness ────────────────────────────────────────────
    witness_path = Path(__file__).with_suffix(".witness.json")
    with open(witness_path, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"\n  Witness written to {witness_path.name}")
    print("=" * 70)


if __name__ == "__main__":
    main()
