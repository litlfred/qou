#!/usr/bin/env python3
"""
Full tower binding from the isotope's NF (with electrons).

Per user (2026-04-19):
  "B should use NF of isotopes with electrons"
  "Use the full tower for calculating B"
  "When calculating the full Tower you start with a normal form
   just as you do with the mass"

Pipeline (mirrors the single-vortex mass calculation):

  1.  Build atom braid with electrons via hecke_core.build_atom_nf,
      reducing to the 6-D H_3(q) normal form.
  2.  Project the NF onto the 3 Wedderburn channels:
        V^sym = |c_γ|
        V^std = |(c_σ₀, c_σ₁, c_L+, c_L-)|   (L²-norm of the std block)
        V^alt = |c_{e⁻}|
  3.  Apply the **full** single-vortex tower formula
      ([prop:mass-endomorphism-tower](#prop:mass-endomorphism-tower))
      treating the 3 channels as the "generators":

        T(V^sym, V^std, V^alt)
          = |V^sym · V^std · V^alt|
          + Σ_λ Φ_q(V^λ)
          + Σ_{λ < μ} z² · Φ_q(V^λ · V^μ)

     (The ∏ term here is over 3 channels, not A-1 nucleons, so it
      stays bounded.)
  4.  Weight each channel by the Wedderburn weight w_λ and scale by
      m_e:

        B(Z, N) = w_sym · m_e · ln|Φ_q(V^sym)|
                + w_std · m_e · ln|Φ_q(V^std)|
                + w_alt · m_e · ln|Φ_q(V^alt)|
                + [pair-blow-up and product terms, if applicable]

Witness stores both the NF (per isotope) AND the derived B.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV
from hecke_core import build_atom_nf


NF_NAMES = ["gamma", "sigma_0", "sigma_1", "L_plus", "L_minus", "e_minus"]

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
W_SYM = 1.0 / (qint2**2 + 2)
W_STD = qint2**2 / (qint2**2 + 2)
W_ALT = W_SYM

Z_MARK = 1.0 / (math.sqrt(q0) + 1.0 / math.sqrt(q0))


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


def phi_q(v, max_k=500):
    return math.exp(ln_phi_q(v, max_k))


def project_channels(nf: list[float]) -> tuple[float, float, float]:
    """3-channel Wedderburn projection magnitudes."""
    V_sym = abs(nf[0])
    V_std = math.sqrt(nf[1]**2 + nf[2]**2 + nf[3]**2 + nf[4]**2)
    V_alt = abs(nf[5])
    return V_sym, V_std, V_alt


def binding_single_vortex(V_sym, V_std, V_alt):
    """Full single-vortex tower applied to 3 channels as generators.

    m = |prod V^lambda|
      + Sum_lambda Phi_q(V^lambda)
      + Sum_{lambda<mu} z^2 · Phi_q(V^lambda · V^mu)

    Weighted by Wedderburn weights times m_e for binding.
    """
    V = [V_sym, V_std, V_alt]
    w = [W_SYM, W_STD, W_ALT]
    # Descended term
    desc = abs(V[0] * V[1] * V[2])
    # Single terms (weighted sum of Φ_q per channel)
    singles = [phi_q(abs(v)) for v in V]
    # Pair terms
    pairs = []
    for i in range(3):
        for j in range(i + 1, 3):
            pairs.append(Z_MARK**2 * phi_q(abs(V[i] * V[j])))
    m_atom = desc + sum(singles) + sum(pairs)
    return {
        "desc": desc,
        "singles": singles,
        "pairs": pairs,
        "m_atom": m_atom,
    }


def binding_log_channels(V_sym, V_std, V_alt):
    """Simpler channel-log variant — the prop:tower-binding-energy form.

    B = Sum_lambda w_lambda · m_e · ln|Phi_q(V^lambda)|

    (Same formula as full-tower-mass.py but with V^lambda from the
    isotope NF instead of per-generator symbolic computation.)
    """
    Bs = ln_phi_q(V_sym)
    Bd = ln_phi_q(V_std)
    Ba = ln_phi_q(V_alt)
    return {
        "ln_Phi_sym": Bs, "ln_Phi_std": Bd, "ln_Phi_alt": Ba,
        "B_MeV": (W_SYM * M_E_MEV * Bs
                    + W_STD * M_E_MEV * Bd
                    + W_ALT * M_E_MEV * Ba),
    }


AME2020 = {
    "D":   2.224566, "T":   8.481798, "3He": 7.718058,
    "4He": 28.295674, "6Li": 31.994571, "7Li": 39.244529,
    "9Be": 58.164980, "10B": 64.750861, "12C": 92.161728,
}


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1),   ("T",   1, 2),   ("3He", 2, 1),
        ("4He", 2, 2),   ("6Li", 3, 3),   ("7Li", 3, 4),
        ("9Be", 4, 5),   ("12C", 6, 6),
    ]

    print("=" * 124)
    print("FULL TOWER FROM ISOTOPE NF (with electrons)")
    print(f"q₀ = {q0},  m_e = {M_E_MEV} MeV,  z_Markov = {Z_MARK:.6f}")
    print(f"w_sym={W_SYM:.6f}  w_std={W_STD:.6f}  w_alt={W_ALT:.6f}")
    print("=" * 124)

    print(f"\n  {'atom':>6} {'Z':>2} {'N':>2}  "
          f"{'V_sym':>8} {'V_std':>8} {'V_alt':>8}  "
          f"{'B_log':>10} {'B_SV':>10}  {'B_AME':>10}  "
          f"{'err_log':>9} {'err_SV':>9}")
    print("  " + "-" * 108)

    results = []
    for name, Z, N in ATOMS:
        A = Z + N
        Mtot = A * 938.272
        B_AME = AME2020[name]

        nf = build_atom_nf(Z, N)
        V_sym, V_std, V_alt = project_channels(nf)

        B_log = binding_log_channels(V_sym, V_std, V_alt)
        B_sv = binding_single_vortex(V_sym, V_std, V_alt)

        # Single-vortex binding: B_MeV form — interpret m_atom as mass
        # defect/binding contribution; scale by W_λ·m_e similarly.
        # Simpler: use m_atom directly as B_MeV (m_e units).
        B_sv_MeV = (W_SYM + W_STD + W_ALT) * M_E_MEV * math.log(
            abs(B_sv["m_atom"]) + 1e-30)

        err_log = abs(B_log["B_MeV"] - B_AME) / Mtot * 100
        err_sv = abs(B_sv_MeV - B_AME) / Mtot * 100

        print(f"  {name:>6} {Z:>2} {N:>2}  "
              f"{V_sym:>8.4f} {V_std:>8.4f} {V_alt:>8.4f}  "
              f"{B_log['B_MeV']:>+10.4f} {B_sv_MeV:>+10.4f}  "
              f"{B_AME:>+10.4f}  "
              f"{err_log:>8.4f}% {err_sv:>8.4f}%")

        results.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B_AME,
            "nf": [float(x) for x in nf],
            "nf_basis": NF_NAMES,
            "V_sym": V_sym, "V_std": V_std, "V_alt": V_alt,
            "binding_log_channels": B_log,
            "binding_single_vortex": B_sv,
            "B_single_vortex_MeV": B_sv_MeV,
            "err_log_pct": err_log,
            "err_sv_pct": err_sv,
        })

    out = (Path(__file__).parent
             / "isotope-nf-full-tower.witness.json")
    out.write_text(json.dumps({
        "computation": "isotope-nf-full-tower",
        "description": (
            "B derived from the isotope's H_3 normal form "
            "(with electrons). Two variants: (a) log-channel "
            "B = Sum_lambda w_lambda m_e ln|Phi_q(V^lambda)|, "
            "(b) single-vortex full tower applied to the 3 channel "
            "projections as generators."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV,
                          "W_sym": W_SYM, "W_std": W_STD, "W_alt": W_ALT,
                          "z_markov": Z_MARK},
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
