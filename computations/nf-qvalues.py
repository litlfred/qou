#!/usr/bin/env python3
"""
NF-based Q-value computation: free neutron validation then isotope table.

Crossing convention (Hecke inverse σ⁻¹ = σ − h,  h = q − q⁻¹):
  pp → σ:          T(1,  0  ) = [[h, 1],[1,  0  ]]
  nn → σ⁻¹:        T(1, −h  ) = [[0, 1],[1, −h  ]]
  pn → ½(σ+σ⁻¹): T(1, −h/2) = [[h/2,1],[1,−h/2]]

Levels
------
  Quark (L1):   each nucleon expanded to 3 quarks (u↔p, d↔n);
                H_{3A}(q), B₃ confinement per nucleon.
                Used for FREE NEUTRON only (A=3 quarks, tractable).

  Nucleon (L0): each nucleon is one strand;
                H_A(q), no confinement braid.
                Used for all ISOTOPES (A up to 14 in Python, rest → Rust).

Free-neutron calibration
------------------------
  Parent quark ordering: neutron = [u,d,d]  → types [p,n,n]
  Daughter:              proton  = [u,u,d]  → types [p,p,n]
  net(x) = Σ_w c_w  (augmentation: eval all σᵢ → 1)
  Δ_q    = net_n − net_p   (quark-level Δ)

  The calibration defines the quark-level energy per unit net change:
    E_q = Q_NEUTRON / Δ_q
  Q_NEUTRON = m_n − m_p − m_e = 0.78233341 ± 6.1e-7 MeV
  Source: CODATA 2022, https://physics.nist.gov/cgi-bin/cuu/Value?mnmpm

Nucleon-level prediction (Stage 2)
------------------------------------
  A nucleon-level Δ_A encodes the same 1-quark flip, now surrounded
  by the full nuclear binding environment.  The ratio
    r = Δ_A / Δ₁   (Δ₁ = Δ at A=3 quark level, i.e. Δ_q)
  measures how much nuclear binding suppresses the bare quark flip.
  Q_pred = r × Q_NEUTRON = Δ_A × E_q

  When r ≈ 1 (light nuclei with little binding), Q_pred → Q_NEUTRON.
  When r ≪ 1 (heavy, tightly-bound nuclei), Q_pred ≪ Q_NEUTRON.
  ³H has r ≈ 1 (almost no suppression at nucleon level alone) — the
  binding correction is expected to enter only at quark level (L1).

Status: quark-level computation for multi-nucleon nuclei requires the
  Rust hecke-engine (A=9 → 36 crossings + B₃).  Python can handle
  A ≤ 14 at NUCLEON level; quark-level isotopes are deferred.

Usage:
    cd computations
    python3 nf-qvalues.py
Output:
    nf-qvalues.witness.json
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from hecke_division import HeckeDivision, HeckeElement
from q_parameter import Q as q0, Q_INV as qi0, HA, LN_Q
from experimental_constants import (
    M_E_MEV,
    Q_NEUTRON_MEV, Q_NEUTRON_MEV_ERR,
    Q_TRITIUM_MEV,   Q_TRITIUM_MEV_ERR,
    Q_C14_MEV,       Q_C14_MEV_ERR,
    Q_CO60_MEV,      Q_CO60_MEV_ERR,
    Q_SR90_MEV,      Q_SR90_MEV_ERR,
    Q_CS137_MEV,     Q_CS137_MEV_ERR,
    Q_BI210_MEV,     Q_BI210_MEV_ERR,
)

div = HeckeDivision(q_val=q0)

# ── Utilities ────────────────────────────────────────────────────

def nf_net(elem):
    """Augmentation: Σ_w c_w  (evaluate all generators at 1)."""
    return sum(elem.terms.values())


def build_nf(types, with_B3=False):
    """Build and Gröbner-reduce the braid for the given strand types.

    types:   list of 'p'/'n' strings.
    with_B3: prefix the 3-strand Borromean confinement braid (use for
             quark-level single-nucleon computations only).

    Crossings (i,j) for all pairs i<j, applied at generator σᵢ
    (adjacency approximation, consistent with existing QOU scripts).

    Returns (reduced_element, net_coefficient, elapsed_s).
    """
    A = len(types)
    t0 = time.time()
    if with_B3:
        elem, _ = div.borromean_B3()
    else:
        elem = HeckeElement.identity()
    for i in range(A):
        for j in range(i + 1, A):
            ti, tj = types[i], types[j]
            if ti == tj == 'p':
                cx = div.crossing_positive(i)
            elif ti == tj == 'n':
                cx = div.crossing_negative(i)
            else:
                cx = div.crossing_mixed(i)
            elem, _ = div.reduce(elem * cx)
    return elem, nf_net(elem), time.time() - t0


def nf_terms_str(elem):
    """Human-readable NF terms sorted by word length."""
    rows = []
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        label = "𝟏" if not w else "·".join(f"σ{g}" for g in w)
        rows.append((label, c))
    return rows


# ══════════════════════════════════════════════════════════════════
# ─── Stage 1: Free neutron calibration (quark level, H₃(q)+B₃) ──
# ══════════════════════════════════════════════════════════════════

SEP = "═" * 72
sep = "─" * 72

print(SEP)
print("NF Q-VALUE COMPUTATION — corrected Hecke σ⁻¹ = σ − (q−q⁻¹)")
print(SEP)
print(f"\nSubstrate:  q₀ = {q0:.10f},  h = q−q⁻¹ = {HA:.10f}")
print("\nCrossing convention:")
print(f"  pp → σ:          T(1,  0   ) = [[h, 1],[1,  0   ]]")
print(f"  nn → σ⁻¹:        T(1, −h   ) = [[0, 1],[1, −h   ]]")
print(f"  pn → ½(σ+σ⁻¹): T(1, −h/2 ) = [[h/2,1],[1,−h/2 ]]")
print()
print(sep)
print("Stage 1 — Free neutron β⁻ decay  n→p e⁻ ν̄  (quark level, H₃(q)+B₃)")
print(sep)
print()
print("  CODATA 2022 reference:")
print(f"    Q(n→p e⁻ ν̄) = m_n − m_p − m_e = {Q_NEUTRON_MEV:.8f} ± {Q_NEUTRON_MEV_ERR:.2e} MeV")
print(f"    URL  : https://physics.nist.gov/cgi-bin/cuu/Value?mnmpm")
print(f"    Cite : CODATA 2022, NIST PL Gaithersburg MD 20899 USA")
print()
print("  Quark model:  neutron = [u,d,d]  (types: p,n,n)")
print("                proton  = [u,u,d]  (types: p,p,n)")
print("  B₃ = (σ₀σ₁⁻¹)³  Borromean confinement included.")
print()

print("  Computing NF(neutron [u,d,d]) ...", end=" ", flush=True)
nf_n, net_n, t_n = build_nf(['p','n','n'], with_B3=True)
print(f"done  ({t_n:.3f}s)")
print(f"  net(n) = Σ c_w = {net_n:+.10f}")
print("  Terms:")
for lbl, c in nf_terms_str(nf_n):
    print(f"      {c:+.10f}  ·  {lbl}")

print()
print("  Computing NF(proton [u,u,d]) ...", end=" ", flush=True)
nf_p, net_p, t_p = build_nf(['p','p','n'], with_B3=True)
print(f"done  ({t_p:.3f}s)")
print(f"  net(p) = Σ c_w = {net_p:+.10f}")
print("  Terms:")
for lbl, c in nf_terms_str(nf_p):
    print(f"      {c:+.10f}  ·  {lbl}")

delta_q = net_n - net_p          # quark-level Δ(net)
E_q = Q_NEUTRON_MEV / delta_q   # quark-level energy scale

print()
print(f"  Δ_q = net(n) − net(p) = {delta_q:+.10f}")
print()
print(f"  Quark-level energy scale:")
print(f"    E_q = Q_NEUTRON / Δ_q = {Q_NEUTRON_MEV:.8f} / ({delta_q:.10f})")
print(f"    E_q = {E_q:.6f} MeV")
print(f"    E_q / m_e = {E_q/M_E_MEV:.6f}")
print(f"    m_e / E_q = {M_E_MEV/E_q:.6f}")
print()
print(f"  ✓ Free neutron validation (exact by construction):")
print(f"      Q_pred = Δ_q × E_q = {delta_q * E_q:.8f} MeV  =  Q_NEUTRON  ✓")
print()


# ══════════════════════════════════════════════════════════════════
# ─── Stage 2: Nucleon-level NF for isotopes ──────────────────────
# ══════════════════════════════════════════════════════════════════

ISOTOPES = [
    # (Z, N, name, Q_exp, Q_exp_err)
    (1,   2,  "³H→³He",     Q_TRITIUM_MEV,  Q_TRITIUM_MEV_ERR),
    (6,   8,  "¹⁴C→¹⁴N",   Q_C14_MEV,      Q_C14_MEV_ERR),
]

print(sep)
print("Stage 2 — Nucleon-level NF for isotopes  (H_A(q), no B₃)")
print(sep)
print()
print("  Applying E_q (calibrated at quark level) to nucleon-level Δ_A:")
print("    Q_pred(A) = Δ_A × E_q")
print()
print("  Physical interpretation of the ratio r = Δ_A / Δ_q:")
print("    r ≈ 1  →  nuclear binding negligible; Q_pred ≈ Q_NEUTRON")
print("    r ≪ 1  →  binding strongly suppresses the decay energy")
print()
print("  Note: the nucleon-level model encodes inter-nucleon crossings only.")
print("  Binding-energy suppression is expected to emerge at quark level (L1).")
print("  Quark-level isotope computations require the Rust hecke-engine.")
print()

iso_results = []
for Z, N, name, Q_exp, Q_exp_err in ISOTOPES:
    A = Z + N
    types_par = ['p'] * Z  + ['n'] * N
    types_dau = ['p'] * (Z + 1) + ['n'] * (N - 1)

    print(f"  {name}  (Z={Z}, N={N}, A={A})")
    print(f"    Parent  = {types_par}")
    print(f"    Daughter= {types_dau}")

    print(f"    NF(parent)  ...", end=" ", flush=True)
    _, net_par, t1 = build_nf(types_par)
    print(f"net = {net_par:+.8f}  ({t1:.3f}s)")

    print(f"    NF(daughter)...", end=" ", flush=True)
    _, net_dau, t2 = build_nf(types_dau)
    print(f"net = {net_dau:+.8f}  ({t2:.3f}s)")

    delta_A = net_par - net_dau
    r       = delta_A / delta_q          # suppression ratio
    Q_pred  = delta_A * E_q
    err_pct = (Q_pred - Q_exp) / Q_exp * 100.0

    print(f"    Δ_A   = {delta_A:+.8f}")
    print(f"    r = Δ_A/Δ_q = {r:+.6f}")
    print(f"    Q_pred = Δ_A × E_q = {Q_pred:.5f} MeV")
    print(f"    Q_obs  = {Q_exp:.5f} ± {Q_exp_err:.5f} MeV")
    print(f"    Error  = {err_pct:+.1f}%")
    print()

    iso_results.append({
        "name": name, "Z": Z, "N": N, "A": A,
        "net_parent": net_par, "net_daughter": net_dau,
        "delta_A": delta_A,
        "r_suppression": r,
        "Q_pred_MeV": Q_pred, "Q_exp_MeV": Q_exp, "Q_exp_err_MeV": Q_exp_err,
        "error_pct": err_pct,
    })


# ── Summary + diagnosis ──────────────────────────────────────────
print(sep)
print("Summary and diagnosis")
print(sep)
print()
print(f"  {'Decay':>14}  {'Q_pred':>9}  {'Q_obs':>9}  {'r=Δ_A/Δ_q':>10}  {'error':>7}")
print(f"  {'-'*14}  {'-'*9}  {'-'*9}  {'-'*10}  {'-'*7}")
for r in iso_results:
    print(f"  {r['name']:>14}  {r['Q_pred_MeV']:9.5f}  {r['Q_exp_MeV']:9.5f}"
          f"  {r['r_suppression']:10.4f}  {r['error_pct']:+6.1f}%")
print()
print("  Diagnosis:")
print(f"    • Δ_q (free neutron, quark level) = {delta_q:+.6f}")
print(f"    • For ³H:  Δ_A ≈ Δ_q → r ≈ 1 → Q_pred ≈ Q_NEUTRON = {Q_NEUTRON_MEV:.4f} MeV")
print(f"      But observed Q(³H) = {Q_TRITIUM_MEV:.5f} MeV — factor {Q_NEUTRON_MEV/Q_TRITIUM_MEV:.0f}× too large.")
print()
print("  Root cause:")
print("    The nucleon-level model captures only inter-nucleon crossing type")
print("    changes (n→p conversion).  With the correct Hecke inverse (c=1,d=−h),")
print("    the σ and σ⁻¹ matrices differ only in the constant term, so the")
print("    nucleon-level Δ_A ≈ Δ_q regardless of nuclear size.  Nuclear")
print("    binding-energy suppression only enters at quark level (L1), where")
print("    the 3A-strand computation for ³H (9 strands, 36 crossings + 3×B₃)")
print("    should show r ≪ 1.")
print()
print("  Next step required:")
print("    Quark-level (L1) computation for ³H and ¹⁴C using the Rust")
print("    hecke-engine with the corrected crossing convention.")
print("    The binding suppression factor r encodes the nuclear Q-value.")
print()
print("  Notes:")
print("    • Free-neutron Q-value is CODATA 2022 with URL provenance.")
print("    • All predictions use ≈ (not =), per notation register.")
print("    • Crossing convention: σ⁻¹ = σ − (q−q⁻¹)  (upstream Hecke fix).")


# ── Write witness JSON ────────────────────────────────────────────
witness = {
    "computation": "nf-qvalues",
    "description": (
        "NF-based Q-value computation (corrected Hecke σ⁻¹ = σ−h). "
        "Stage 1: free neutron quark-level calibration of E_q. "
        "Stage 2: nucleon-level NF for β⁻ decay isotopes."
    ),
    "timestamp":   datetime.now(timezone.utc).isoformat(),
    "q0":          q0,
    "HA":          HA,
    "crossing_convention": {
        "pp":      "sigma             c=1  d=0",
        "nn":      "sigma_inv=sigma-h  c=1  d=-h",
        "pn":      "half_sum=sigma-h/2 c=1  d=-h/2",
        "reference": "upstream Hecke-Skein fix, sigma_inv = sigma - (q - q^-1)",
    },
    "free_neutron": {
        "codata_source": {
            "Q_NEUTRON_MEV":     Q_NEUTRON_MEV,
            "Q_NEUTRON_MEV_ERR": Q_NEUTRON_MEV_ERR,
            "url":  "https://physics.nist.gov/cgi-bin/cuu/Value?mnmpm",
            "citation": (
                "CODATA 2022, NIST Physics Laboratory, Gaithersburg MD 20899 USA. "
                "Q = m_n - m_p - m_e derived from individual mass-energy equivalents; "
                "cross-checked against direct CODATA entry m_n-m_p = 1.2933321 MeV."
            ),
        },
        "model":        "quark level H3(q) with Borromean B3=(sigma0*sigma1^-1)^3",
        "neutron_types":"p,n,n  (u,d,d)",
        "proton_types": "p,p,n  (u,u,d)",
        "net_neutron":  net_n,
        "net_proton":   net_p,
        "delta_q":      delta_q,
        "E_q_MeV":      E_q,
        "E_q_over_me":  E_q / M_E_MEV,
        "Q_pred_MeV":   delta_q * E_q,
        "Q_obs_MeV":    Q_NEUTRON_MEV,
        "status":       "exact by construction (E_q is calibrated from this)",
        "neutron_nf_terms": {
            ("·".join(str(g) for g in w) if w else "1"): c
            for w, c in sorted(nf_n.terms.items(), key=lambda x: (len(x[0]), x[0]))
        },
        "proton_nf_terms": {
            ("·".join(str(g) for g in w) if w else "1"): c
            for w, c in sorted(nf_p.terms.items(), key=lambda x: (len(x[0]), x[0]))
        },
    },
    "isotopes_nucleon_level": iso_results,
    "diagnosis": {
        "observation":
            "Nucleon-level Δ_A ≈ Δ_q for all light nuclei: r ≈ 1. "
            "Q_pred(³H) ≈ Q_NEUTRON, far above observed 0.019 MeV.",
        "root_cause":
            "With corrected Hecke inverse (c=1, d=-h), the matrices "
            "T_pp and T_nn differ only in the constant term. "
            "The nucleon-level Δ_A is insensitive to nuclear binding. "
            "Binding suppression enters only at quark level (L1).",
        "next_step":
            "Quark-level (L1) computation for ³H and 14C via Rust "
            "hecke-engine with corrected crossing convention.",
    },
}

out_path = Path(__file__).resolve().parent / "nf-qvalues.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness → {out_path.name}")
