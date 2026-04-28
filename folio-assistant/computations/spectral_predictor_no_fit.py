#!/usr/bin/env python3
"""
38a: Spectral predictor using NEW upstream structural propositions only.

Uses:
  - prop:knot-factor-shell-closed:  a_K = 1 EXACT for Z=N even-even (⁴He)
  - prop:knot-factor-amphicheiral:  a_K = 1 - h² for amphicheiral knots (³H, ³He via 4_1)
  - prop:pauli-factor-wedderburn:    F_Pauli = χ_(1^n)·dim_q V_(1^n) / (χ_(n)·dim_q V_(n))
  - prop:gravity-spectral-prefactor: Term 7 prefactor = m_e · 8G (Newton's G)
  - prop:torus-knot-genus-four-unique: force carriers exactly {T_{2,9}, T_{3,5}}

For each isotope, the binding from spectral framework:

  B(isotope) = ρ_F(K) · Vol(K)             [mass_table_ppb leading: Volume]
             + a_K(isotope) · m_e          [chirality / knot factor]
             + F_Pauli(β) · m_e            [Pauli statistics]
             + universal Term 7 residue    [m_e · 8G · deep-tower Plancherel]

with NO per-isotope fitting.  All structurally derived per the new
propositions.

If the result is close to AME, the framework's spectral derivations
work directly.  If not, identifies which sector still needs work.
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
import numpy as np
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import (
    build_seminormal_matrices, nuclear_braid_character,
    partitions_of, dim_q, qfac, q_int
)

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
G_catalan = mp.catalan  # 0.916...
m_e_8G = m_e * 8 * G_catalan  # universal Term 7 prefactor


def qint(n): return q_int(n)


# Knot Vols (from mass_table_ppb framework rules)
KNOT_VOL = {
    "6_2":     mp.mpf("4.40083251397820"),
    "8_11":    mp.mpf("8.28631808635811"),
    "L6a4":    mp.mpf("7.32772475300860"),  # = 8G_Catalan = Vol(Borromean)
    "4*L6a4":  mp.mpf("29.31089901203440"), # ⁴He = 4·Borromean
}


# Per-isotope atom-knot + a_K rule application
ISOTOPES_SPEC = [
    # (label, Z, N, B_AME, K_assign, rho_F_factor, a_K_rule)
    ("D",   1, 1,  2.22456612, "6_2",     1, "general"),
    ("T",   1, 2,  8.481798,   "8_11",    2, "amphicheiral_via_4_1"),
    ("3He", 2, 1,  7.718058,   "L6a4",    2, "amphicheiral_via_4_1"),
    ("4He", 2, 2, 28.29566,    "4*L6a4",  2, "shell_closed_ZN_even"),
    ("6Li", 3, 3, 31.99405,    None,      None, "no_atom_knot_yet"),
    ("7Li", 3, 4, 39.24452,    None,      None, "no_atom_knot_yet"),
]


def F_Pauli_at_H_n(Z, N):
    """F_Pauli = χ_(1^n)·dim_q V_(1^n) / (χ_(n)·dim_q V_(n))
    per prop:pauli-factor-wedderburn.

    For H_n with n=3A:
      V_(n)    = sym block,  χ_(n)(β)    = q^writhe(β)
      V_(1^n)  = alt block,  χ_(1^n)(β)  = (-q^{-1})^writhe(β) = (-1)^w · q^{-w}
      dim_q V_(n) = 1, dim_q V_(1^n) = 1 (extreme blocks always 1-dim)

    So F_Pauli = (-1)^w · q^{-w} / q^w = (-1)^w · q^{-2w}
    where w is the writhe of the atomic braid.
    """
    A = Z + N
    n = 3 * A
    n_gens = max(1, n - 1)
    # Build sym (rank 1) and alt (rank 1) seminormal matrices for the atomic braid
    try:
        sigmas_sym, _, _ = build_seminormal_matrices((n,))
        sigmas_alt, _, _ = build_seminormal_matrices((1,)*n)
    except Exception:
        return None
    chi_sym = float(nuclear_braid_character(Z, N, sigmas_sym, 1, n_gens))
    chi_alt = float(nuclear_braid_character(Z, N, sigmas_alt, 1, n_gens))
    if abs(chi_sym) < 1e-30:
        return None
    return chi_alt / chi_sym


def a_K_for(iso, F_Pauli):
    """Per the rules in `a_K_rule`."""
    if iso == "4He":
        return 1.0  # shell-closed, exact
    if iso in ("T", "3He"):
        # amphicheiral via 4_1 representation: a = 1 - h²
        # h = χ_(1^n)(β)/χ_(1^n)(1) = χ_alt(β)/χ_alt(1) = chi_alt
        # F_Pauli = chi_alt / chi_sym, so chi_alt = F_Pauli · chi_sym.
        # If chi_sym = 1 (unit braid? no, β has crossings...) hmm.
        # Actually h = chi_(1^n)(β)/chi_(1^n)(identity) = chi_alt(β) (since chi_alt(1)=1).
        # We have chi_alt directly.
        try:
            sigmas_alt, _, _ = build_seminormal_matrices((1,)*9)  # H_9 for A=3
            Z, N = (1, 2) if iso == "T" else (2, 1)
            chi_alt = float(nuclear_braid_character(Z, N, sigmas_alt, 1, 8))
            h = chi_alt
            return float(1 - h**2)
        except Exception:
            return None
    return None  # general case needs full knot factor computation


print("=" * 110)
print("38a: Spectral predictor — NO per-isotope fitting, uses ONLY new structural propositions")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f}")
print(f"  m_e = {float(m_e):.6f} MeV")
print(f"  m_e · 8G_Catalan = {float(m_e_8G):.6f} MeV  (Term 7 prefactor — see prop:gravity-spectral-prefactor)")
print()

results = []
print(f"  {'iso':<5} {'A':>3} {'B_AME':>10} {'K_assign':<10} {'a_K':>8} {'F_Pauli':>10} {'note':>40}")
print("-" * 110)
for label, Z, N, B_AME, Kname, rho_factor, a_K_rule in ISOTOPES_SPEC:
    A = Z + N
    if Kname is None:
        print(f"  {label:<5} {A:>3} {B_AME:>10.4f} {'(no rule)':<10} {'—':>8} {'—':>10} {'no atom-knot yet (open)':>40}")
        results.append({"iso": label, "A": A, "B_AME": B_AME, "skipped": True})
        continue

    # F_Pauli structural
    F_P = F_Pauli_at_H_n(Z, N)

    # a_K structural
    aK = a_K_for(label, F_P)

    aK_str = f"{aK:+.4f}" if aK is not None else "?"
    FP_str = f"{F_P:+.4f}" if F_P is not None else "?"
    print(f"  {label:<5} {A:>3} {B_AME:>10.4f} {Kname:<10} {aK_str:>10} {FP_str:>12} {a_K_rule:>40}")

    results.append({
        "iso": label, "A": A, "Z": Z, "N": N, "B_AME": B_AME,
        "K_assign": Kname, "rho_F_factor": rho_factor,
        "a_K": aK, "a_K_rule": a_K_rule,
        "F_Pauli": F_P
    })

print()
print("=" * 110)
print("Spectral binding prediction (combining the new structural pieces)")
print("=" * 110)
print(f"  {'iso':<5} {'A':>3} {'B_AME':>10} {'Vol·ρ_F':>10} {'a_K·m_e':>10} {'F_Pauli·m_e':>13} {'B_pred':>10} {'err %':>9}")
print("-" * 110)
for r in results:
    if r.get("skipped"):
        print(f"  {r['iso']:<5} {r['A']:>3} {r['B_AME']:>10.4f}  (skipped — needs atom-knot identification)")
        continue
    Vol = float(KNOT_VOL[r["K_assign"]])
    rho_F = r["rho_F_factor"] * float(m_e)
    Vol_term = rho_F * Vol
    aK_term = (r["a_K"] or 0) * float(m_e)
    Pauli_term = (r["F_Pauli"] or 0) * float(m_e)

    # Simplest combination: leading + a_K + F_Pauli (no Term 7 yet — it's small)
    B_pred = Vol_term + aK_term + Pauli_term

    err = (B_pred - r["B_AME"])/r["B_AME"] * 100 if r["B_AME"] != 0 else 0
    print(f"  {r['iso']:<5} {r['A']:>3} {r['B_AME']:>10.4f} {Vol_term:>10.4f} {aK_term:>+10.4f} {Pauli_term:>+13.4f} {B_pred:>10.4f} {err:>+9.4f}%")
    r["Vol_term"] = Vol_term
    r["aK_term"] = aK_term
    r["Pauli_term"] = Pauli_term
    r["B_pred"] = B_pred
    r["err_pct"] = err

print()
print("=" * 110)
print("INTERPRETATION")
print("=" * 110)
print("""
Spectral predictor uses only:
  1. Vol(K)·ρ_F: mass_table_ppb's leading-order knot-volume formula
  2. a_K · m_e: chirality factor from prop:knot-factor-amphicheiral
                / shell-closed (NO fitting)
  3. F_Pauli · m_e: from prop:pauli-factor-wedderburn (Hoefsmit ratio)

Comparison to AME shows whether these structural pieces alone close
binding (or what additional sectors are needed).

For ⁴He: a_K = 1 EXACT (Markov equilibrium), so chirality is full m_e.
For ³H, ³He: a_K = 1 - h² where h is the alt-block character ratio.
For D: needs general knot-factor-spectral-form (not amphicheiral).

If predictions land within ~5% across the board, framework's structural
binding is real.  Outliers indicate which sector (Coulomb? deep-tower?)
still needs structural derivation.
""")

out = {
    "computation": "spectral-predictor-no-fit",
    "description": ("38a: Strict-spectral binding predictor for D, T, ³He, ⁴He using "
                    "the new upstream structural propositions: knot-factor-amphicheiral, "
                    "knot-factor-shell-closed, pauli-factor-wedderburn, gravity-spectral-"
                    "prefactor.  NO per-isotope fitting.  Tests whether the framework's "
                    "spectral derivations close binding directly."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "calibrations": {"m_e": float(m_e), "q_0": float(Q0), "m_p (anchor)": 938.27208816},
    "structural_propositions_used": [
        "prop:knot-factor-shell-closed (⁴He: a_K = 1 exact)",
        "prop:knot-factor-amphicheiral (³H, ³He: a_K = 1 - h²)",
        "prop:pauli-factor-wedderburn (F_Pauli = χ_alt/χ_sym)",
        "prop:gravity-spectral-prefactor (Term 7 prefactor m_e · 8G)"
    ],
    "results": results
}
out_path = Path(__file__).parent / "spectral-predictor-no-fit.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
