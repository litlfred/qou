#!/usr/bin/env python3
"""
Isotope NF witness with electrons — one per isotope, saved.

Per user (2026-04-19) "B should use NF of isotopes with electrons;
isotopes NF should be witnessed":

For each isotope (Z, N), build the atom braid word including Z
electrons (σ₁⁻¹ at gen 1 per legacy hecke_core convention, revisit
under SDP later), reduce to H_3(q) NF via `hecke_core.build_atom_nf`
(6-D Gröbner normal form: {γ, σ₀, σ₁, L₊, L₋, e⁻}), and save the
coefficient vector as a witness.

From the NF vector `c = [c_γ, c_σ₀, c_σ₁, c_{L+}, c_{L-}, c_{e⁻}]`,
derive the 3-channel Wedderburn projection per
[prop:tower-binding-energy](#prop:tower-binding-energy):

  K^sym = c_γ · γ                       (sym / trivial irrep, 1-D)
  K^std = c_σ₀·σ₀ + c_σ₁·σ₁
           + c_{L+}·L₊ + c_{L-}·L₋       (std irrep, 2-D projection)
  K^alt = c_{e⁻} · e⁻                    (alt irrep, 1-D)

And the Markov trace per channel (using trace weights):

  tr_M^λ(K) = <K^λ, tr_M_weights>

Binding proposed for each isotope:

  B(Z, N) = w_sym · m_e · ln|Φ_q(V̂^sym)|
          + w_std · m_e · ln|Φ_q(V̂^std)|
          + w_alt · m_e · ln|Φ_q(V̂^alt)|

where V̂^λ is the per-channel projection magnitude.

This is an H_3-level evaluation (post-Gröbner reduction) of the
content-block formula. NF reduction collapses the 3A-strand detail
into a 6-D vector, then Wedderburn splits that vector over sym/std/
alt.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0, HA as h
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hecke_core import build_atom_nf


# NF basis names in H_3(q) (6-D).
NF_NAMES = ["gamma", "sigma_0", "sigma_1", "L_plus", "L_minus", "e_minus"]

# Channel projectors onto the 6-D NF basis:
#   sym  = {γ}                index 0
#   std  = {σ₀, σ₁, L₊, L₋}   indices 1..4
#   alt  = {e⁻}               index 5
CHANNEL_SYM = np.array([1, 0, 0, 0, 0, 0], dtype=float)
CHANNEL_STD = np.array([0, 1, 1, 1, 1, 0], dtype=float)
CHANNEL_ALT = np.array([0, 0, 0, 0, 0, 1], dtype=float)

# Wedderburn weights at q₀ (same as full-tower-mass.py).
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


def project_channels(nf: list[float]) -> dict:
    """Project a 6-D NF vector onto the 3 Wedderburn channels."""
    arr = np.asarray(nf, dtype=float)
    # Per-channel MAGNITUDE of the projected vector component, summed.
    sym_mag = abs(arr[0])
    std_mag = float(np.sqrt(np.sum(arr[1:5]**2)))
    alt_mag = abs(arr[5])
    return {
        "sym": {"proj_nf": (arr * CHANNEL_SYM).tolist(),
                 "magnitude": sym_mag},
        "std": {"proj_nf": (arr * CHANNEL_STD).tolist(),
                 "magnitude": std_mag},
        "alt": {"proj_nf": (arr * CHANNEL_ALT).tolist(),
                 "magnitude": alt_mag},
    }


def binding_from_nf(Z: int, N: int, nf: list[float]) -> dict:
    """Compute B(Z, N) via the 3-channel V̂^λ = per-channel projection
    magnitude, fed into Σ w_λ m_e ln|Φ_q(V̂^λ)|."""
    proj = project_channels(nf)
    B_sym = ln_phi_q(proj["sym"]["magnitude"])
    B_std = ln_phi_q(proj["std"]["magnitude"])
    B_alt = ln_phi_q(proj["alt"]["magnitude"])
    B = (W_SYM * M_E_MEV * B_sym
           + W_STD * M_E_MEV * B_std
           + W_ALT * M_E_MEV * B_alt)
    return {
        "ln_Phi_sym": B_sym, "ln_Phi_std": B_std, "ln_Phi_alt": B_alt,
        "V_sym": proj["sym"]["magnitude"],
        "V_std": proj["std"]["magnitude"],
        "V_alt": proj["alt"]["magnitude"],
        "B_MeV": B,
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",    1,  1,  2.22452),
        ("T",    1,  2,  8.481821),
        ("3He",  2,  1,  7.71804),
        ("4He",  2,  2, 28.295674),
        ("6Li",  3,  3, 32.00),
        ("7Li",  3,  4, 39.244529),
        ("9Be",  4,  5, 58.1650),
        ("12C",  6,  6, 92.161728),
    ]

    print("=" * 120)
    print("ISOTOPE NF WITNESS — H_3(q) NF with electrons")
    print(f"q0 = {q0},  W_sym = {W_SYM:.6f},  W_std = {W_STD:.6f},  "
          f"W_alt = {W_ALT:.6f}")
    print("=" * 120)

    print(f"\n  {'atom':>6} {'Z':>2} {'N':>2}   {'gamma':>10} "
          f"{'sigma_0':>10} {'sigma_1':>10} {'L_+':>10} {'L_-':>10} "
          f"{'e_-':>10}   {'V_sym':>8} {'V_std':>8} {'V_alt':>8}")
    print("  " + "-" * 112)

    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        # Build H_3 NF with electrons (legacy: Z copies of σ_1^-1)
        nf = build_atom_nf(Z, N)
        proj = project_channels(nf)
        binding = binding_from_nf(Z, N, nf)
        err = abs(binding["B_MeV"] - B_AME) / Mtot * 100
        print(f"  {name:>6} {Z:>2} {N:>2}  "
              f"{nf[0]:>+10.3e} {nf[1]:>+10.3e} {nf[2]:>+10.3e} "
              f"{nf[3]:>+10.3e} {nf[4]:>+10.3e} {nf[5]:>+10.3e}   "
              f"{proj['sym']['magnitude']:>8.4f} "
              f"{proj['std']['magnitude']:>8.4f} "
              f"{proj['alt']['magnitude']:>8.4f}")
        results.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B_AME,
            "nf_basis_names": NF_NAMES,
            "nf_coefficients": [float(x) for x in nf],
            "channel_projections": proj,
            "binding": binding,
            "err_mass_pct": err,
        })

    print()
    print("  --- Binding energies from NF projection ---")
    print(f"  {'atom':>6}  {'B_pred':>10} {'B_AME':>10} {'gap':>10} "
          f"{'err':>10}")
    print("  " + "-" * 55)
    for r in results:
        print(f"  {r['atom']:>6}  "
              f"{r['binding']['B_MeV']:>+10.4f} {r['B_AME_MeV']:>+10.4f} "
              f"{r['binding']['B_MeV']-r['B_AME_MeV']:>+10.4f} "
              f"{r['err_mass_pct']:>9.4f}%")

    out = (Path(__file__).parent
             / "isotope-nf-witness.witness.json")
    out.write_text(json.dumps({
        "computation": "isotope-nf-witness",
        "description": (
            "H_3(q) normal forms of isotopes (with electrons "
            "appended as Z·σ₁⁻¹ per hecke_core convention), "
            "projected onto the 3 Wedderburn channels (sym/std/alt) "
            "and used to compute B(Z,N) per "
            "prop:tower-binding-energy."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "q_inv": qi0, "M_E_MEV": M_E_MEV,
            "W_sym": W_SYM, "W_std": W_STD, "W_alt": W_ALT,
            "NF_basis": NF_NAMES,
            "channel_sym_mask": CHANNEL_SYM.tolist(),
            "channel_std_mask": CHANNEL_STD.tolist(),
            "channel_alt_mask": CHANNEL_ALT.tolist(),
        },
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
