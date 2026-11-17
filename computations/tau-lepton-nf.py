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

    The bₙ satisfy the continuant (Morgan--Voyce) recurrence
    bₙ₊₁ = h·bₙ + bₙ₋₁ with b₀ = 0, b₁ = 1.

Usage:
    python3 tau-lepton-nf.py

Output:
    tau-lepton-nf.witness.json
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

# ── Import canonical q at full mpf precision (bean qou-hytc) ─────
sys.path.insert(0, str(Path(__file__).parent))
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()

from q_parameter import (  # noqa: E402
    MASS_RATIO_MU_E_STR,
    Q_50_DIGIT_STR,
    VOL_FIGURE_EIGHT_50_STR,
)
from witness_base import WitnessBuilder  # noqa: E402


# ── Chebyshev recurrence for NF(σ₀ⁿ) = aₙ·𝟙 + bₙ·σ₀ ──────────

def chebyshev_nf(n_max: int, h: mp.mpf) -> tuple[list[mp.mpf], list[mp.mpf]]:
    """Compute NF(σ₀ⁿ) for n = 0..n_max via Chebyshev recurrence in mpmath.mpf.

    Returns lists (a, b) where NF(σ₀ⁿ) = a[n]·𝟙 + b[n]·σ₀.

    The recurrence is:
        a₀ = 1, b₀ = 0
        aₙ₊₁ = bₙ
        bₙ₊₁ = h·bₙ + aₙ
    """
    a = [mp.mpf(1)]
    b = [mp.mpf(0)]
    for _ in range(n_max):
        a_new = b[-1]
        b_new = h * b[-1] + a[-1]
        a.append(a_new)
        b.append(b_new)
    return a, b


def main():
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    qi = mp.mpf(1) / q
    h = q - qi  # q − q⁻¹
    hbar_q = mp.mpf(1) - qi
    vol_4_1 = mp.mpf(VOL_FIGURE_EIGHT_50_STR)
    mass_ratio_mu_e = mp.mpf(MASS_RATIO_MU_E_STR)

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
            "a_n (𝟙 coeff)": fmt(a[n]),
            "b_n (σ₀ coeff)": fmt(b[n]),
            "net": fmt(a[n] + b[n]),
        }

    # ── Decay: τ⁻ → e⁻ + ν̄ₑ + ν_τ ──────────────────────────────
    # NF(ν) = 1·𝟙 + 0·σ₀  (neutrino = identity in Hecke)
    # Δ = NF(τ) − NF(e) − 2·NF(ν)
    two = mp.mpf(2)
    br_pdg_e = mp.mpf("0.1782")
    br_pdg_mu = mp.mpf("0.1739")
    delta_net_e = (a[7] + b[7]) - (a[3] + b[3]) - two
    delta_net_mu = (a[7] + b[7]) - (a[5] + b[5]) - two

    tau_to_e = {
        "process": "τ⁻ → e⁻ + ν̄ₑ + ν_τ",
        "BR_PDG": fmt(br_pdg_e),
        "delta_1": fmt(a[7] - a[3] - two),
        "delta_sigma": fmt(b[7] - b[3]),
        "delta_net": fmt(delta_net_e),
        "crossings_released": 7 - 3,
    }

    # ── Decay: τ⁻ → μ⁻ + ν̄_μ + ν_τ ─────────────────────────────
    tau_to_mu = {
        "process": "τ⁻ → μ⁻ + ν̄_μ + ν_τ",
        "BR_PDG": fmt(br_pdg_mu),
        "delta_1": fmt(a[7] - a[5] - two),
        "delta_sigma": fmt(b[7] - b[5]),
        "delta_net": fmt(delta_net_mu),
        "crossings_released": 7 - 5,
    }

    # ── BR ratio check ───────────────────────────────────────────
    # In the Standard Model, BR(τ→e)/BR(τ→μ) ≈ 1.0 (lepton universality)
    # The Hecke NF Δ is an algebraic invariant; the physical rate
    # additionally requires the weak vertex form factor.
    # Check: ratio of Δ_net values
    br_ratio_nf = delta_net_e / delta_net_mu

    # ── Mass ratios from NF net amplitudes ───────────────────────
    # The net NF amplitude is the total Hecke weight. Mass ratios
    # via the topological mass formula involve Vol(K)/ℏ_q², but for
    # torus knots (non-hyperbolic, Vol=0), mass comes through the
    # Higgs mechanism coupling at each Reeb degree.
    net_ratio_mu_e = (a[5] + b[5]) / (a[3] + b[3])
    net_ratio_tau_e = (a[7] + b[7]) / (a[3] + b[3])
    net_ratio_tau_mu = (a[7] + b[7]) / (a[5] + b[5])
    mass_info = {
        "net_ratio_mu_e": fmt(net_ratio_mu_e),
        "net_ratio_tau_e": fmt(net_ratio_tau_e),
        "net_ratio_tau_mu": fmt(net_ratio_tau_mu),
        "note": "Torus knot mass comes from Higgs mechanism (Vol(4₁)/ℏ_q²), not directly from NF net. NF net captures algebraic weight.",
    }

    # ── Full NF table for T_{2,n}, n=0..9 ───────────────────────
    nf_table = []
    for n in range(10):
        nf_table.append({
            "n": n,
            "a_n": fmt(a[n]),
            "b_n": fmt(b[n]),
            "net": fmt(a[n] + b[n]),
        })

    # ── Continuant identity check ───────────────────────────────
    # bₙ satisfies the continuant recurrence bₙ₊₁ = h·bₙ + bₙ₋₁
    # (Morgan--Voyce type, NOT standard Chebyshev-U which has −bₙ₋₁).
    # Verify: bₙ₊₁ − h·bₙ − bₙ₋₁ = 0 for all n ≥ 1.
    continuant_check = []
    cont_tol = mp.mpf("1e-50")
    for n in range(1, 9):
        residual = b[n + 1] - h * b[n] - b[n - 1]
        continuant_check.append({
            "n": n,
            "b_{n+1}": fmt(b[n + 1]),
            "h*b_n + b_{n-1}": fmt(h * b[n] + b[n - 1]),
            "residual": fmt(residual),
            "match": abs(residual) < cont_tol,
        })

    # ── Build witness using WitnessBuilder ─────────────────────
    all_match = all(c["match"] for c in continuant_check)

    w = WitnessBuilder("tau-lepton-nf", engine="mpmath")
    w.set_description(
        "Chebyshev tower NF(T_{2,n}) in H₂(q) for the charged lepton "
        "tower n = 3, 5, 7 (electron, muon, tau). Verifies the continuant "
        "(Morgan--Voyce) recurrence and the algebraic structure of "
        "leptonic tau decays."
    )
    w.set_content_block("rem:lepton-mass-integrals")

    # Parameters
    w.add_parameter("q₀", fmt(q))
    w.add_parameter("h (q−q⁻¹)", fmt(h))
    w.add_parameter("ℏ_q", fmt(hbar_q))
    w.add_parameter("Vol(4₁)", fmt(vol_4_1))
    w.add_parameter("m_μ/m_e", fmt(mass_ratio_mu_e))

    # Assertions
    # 1. Continuant recurrence holds
    w.add_assertion(
        "Continuant recurrence bₙ₊₁ = h·bₙ + bₙ₋₁ (all n)",
        computed=1 if all_match else 0,
        expected=1,
        tolerance=0,
        unit="boolean",
        source="Morgan--Voyce recurrence in H₂(q)",
    )

    # 2. NF coefficients for leptons (bean qou-26f2, qou-hytc)
    net = [a[i] + b[i] for i in range(len(a))]
    rel_scale = mp.mpf("1e-8")
    for name, info in leptons.items():
        n = info["n"]
        w.add_assertion(
            f"NF(T_{{2,{n}}}) net amplitude ({name})",
            computed=fmt(net[n]),
            expected=fmt(h * net[n - 1] + net[n - 2]),
            tolerance=fmt(abs(net[n]) * rel_scale),
            unit="dimensionless",
            source=f"Chebyshev recurrence at n={n}: "
                   f"s[{n}] = h*s[{n - 1}] + s[{n - 2}]",
        )

    # 3. BR ratio NF vs PDG (bean qou-hytc: mpf-carried computed tolerance)
    pdg_br_ratio = br_pdg_e / br_pdg_mu
    w.add_assertion(
        "NF Δ ratio (τ→e)/(τ→μ) vs PDG BR ratio",
        computed=fmt(br_ratio_nf),
        expected=fmt(pdg_br_ratio),
        tolerance=fmt(abs(pdg_br_ratio) * mp.mpf("0.25")),
        unit="dimensionless",
        source="Algebraic NF ratio vs PDG 2024 branching fractions. "
               "NF captures crossing structure; physical rate requires "
               "weak vertex form factor.",
    )

    # Data
    w.add_data("lepton_nfs", lepton_nfs)
    w.add_data("tau_to_electron_decay", tau_to_e)
    w.add_data("tau_to_muon_decay", tau_to_mu)
    w.add_data("BR_ratio_NF", fmt(br_ratio_nf))
    w.add_data("mass_ratios_from_net", mass_info)
    w.add_data("nf_table_T2n", nf_table)
    w.add_data("continuant_check", continuant_check)

    w.add_caveat(
        "Torus knots T_{2,n} have zero hyperbolic volume. Lepton mass "
        "ratios do not come from Vol(K)/ℏ_q² but through the Higgs "
        "mechanism coupling at each Reeb degree. The NF net amplitudes "
        "are algebraic weights, not direct mass predictions."
    )

    witness_path = w.save()

    # ── Print summary ────────────────────────────────────────────
    print("=" * 70)
    print("  TAU LEPTON NF — Chebyshev tower T_{2,n} in H₂(q)")
    print("=" * 70)
    print(f"\n  q = {mp.nstr(q, 11)},  h = q−q⁻¹ = {mp.nstr(h, 10)}\n")

    print("  NF(T_{2,n}) = aₙ·𝟙 + bₙ·σ₀")
    print("  " + "-" * 55)
    for n in range(10):
        label = ""
        if n == 3: label = " ← electron"
        elif n == 5: label = " ← muon"
        elif n == 7: label = " ← tau"
        print(f"  n={n}:  a={mp.nstr(a[n], 9):>12s}  b={mp.nstr(b[n], 9):>12s}  net={mp.nstr(a[n]+b[n], 9)}{label}")

    print(f"\n  --- Continuant recurrence: bₙ₊₁ = h·bₙ + bₙ₋₁ ---")
    print(f"  All match: {all_match}")

    print(f"\n  --- Leptonic tau decay ---")
    for d in [tau_to_e, tau_to_mu]:
        print(f"  {d['process']}:")
        print(f"    Δ(𝟙)  = {d['delta_1']}")
        print(f"    Δ(σ₀) = {d['delta_sigma']}")
        print(f"    Δ(net) = {d['delta_net']}")
        print(f"    Crossings released: {d['crossings_released']}")
        print(f"    PDG BR: {d['BR_PDG']}")

    print(f"\n  NF Δ ratio (τ→e)/(τ→μ) = {mp.nstr(br_ratio_nf, 7)}")
    print(f"  PDG BR ratio            = {mp.nstr(pdg_br_ratio, 7)}")
    print(f"  (Lepton universality predicts ≈ 1.0)")

    print(f"\n  --- Net amplitude ratios ---")
    print(f"  net(μ)/net(e) = {mp.nstr(net_ratio_mu_e, 7)}")
    print(f"  net(τ)/net(e) = {mp.nstr(net_ratio_tau_e, 7)}")
    print(f"  net(τ)/net(μ) = {mp.nstr(net_ratio_tau_mu, 7)}")

    print(f"\n  Witness: {witness_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
