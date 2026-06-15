#!/usr/bin/env python3
"""
Certificate-to-mass validation: evaluate all 47 hecke-engine certificates
against AME2020 observed masses.

For each certificate, this script:
  1. Reads the certificate JSON (isotope metadata + polynomial evaluations)
  2. Computes the atomic mass M(Z,N) using two methods:
     (a) CODATA+AME2020: M = Z·m_p + N·m_n + Z·m_e − B(Z,N)
         (this is the existing topological-mass-table approach)
     (b) Certificate polynomials: evaluate f_pauli, tr_alt, net at q₀
  3. Compares against AME2020 atomic mass excess / binding energy
  4. Identifies which certificate field (if any) encodes physical mass

KEY INSIGHT: The existing mass table uses M = Z·m_p + N·m_n + Z·m_e − B(Z,N)
where m_p, m_n are CODATA inputs and B/A is AME2020 input. This is NOT a
prediction from q — it is a consistency check using observed constants.

The certificate fields (tr_alt_f64, net_f64, f_pauli_f64) are polynomial
evaluations at q₀ from the Hecke algebra transfer matrix. The question is:
can these be converted to physical mass independently of CODATA m_p, m_n?

Usage:
    python3 certificate-to-mass.py

Output:
    certificate-to-mass.witness.json
"""

import json
import math
import sys
import glob
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import (
    Q, Q_INV, HBAR_Q, HBAR_Q_SQ,
    VOL_FIGURE_EIGHT, MASS_RATIO_MU_E,
    HA, E_CROSS, Q_ERR,
)
from experimental_constants import (
    M_E_MEV, M_P_MEV, M_N_MEV,
    VOL_BORROMEAN,
)
from witness_base import WitnessBuilder

# ══════════════════════════════════════════════════════════════
# §1  AME2020 BINDING ENERGIES (per nucleon, MeV)
# ══════════════════════════════════════════════════════════════
# Source: Atomic Mass Evaluation 2020 (Huang et al.)
# https://doi.org/10.1088/1674-1137/abddb0
#
# Format: (Z, N, A, B/A [MeV], symbol, half_life_note)
# B/A = binding energy per nucleon from AME2020
# For stable isotopes, half_life_note = "stable"

AME2020_ISOTOPES = {
    # ── Hydrogen isotopes ────────────────────────────────────
    (1, 0):   (1,   0.0000,   "H",   "stable"),        # protium (no binding)
    (1, 1):   (2,   1.1121,   "H",   "stable"),        # deuterium
    (1, 2):   (3,   2.8273,   "H",   "12.32 yr"),      # tritium
    (1, 3):   (4,   1.7200,   "H",   "unbound"),       # 4H
    (1, 4):   (5,   0.5700,   "H",   "unbound"),       # 5H
    (1, 5):   (6,   0.9600,   "H",   "unbound"),       # 6H (est.)
    (1, 6):   (7,   0.5300,   "H",   "unbound"),       # 7H (est.)
    (1, 7):   (8,   0.3500,   "H",   "unbound"),       # 8H (est.)
    (1, 8):   (9,   0.2200,   "H",   "unbound"),       # 9H (est.)
    # ── Helium isotopes ──────────────────────────────────────
    (2, 1):   (3,   2.5727,   "He",  "stable"),        # 3He
    (2, 2):   (4,   7.0739,   "He",  "stable"),        # 4He (alpha)
    (2, 3):   (5,   5.4813,   "He",  "602 keV"),       # 5He
    (2, 4):   (6,   4.8782,   "He",  "806.92 ms"),     # 6He
    (2, 5):   (7,   4.1231,   "He",  "unbound"),       # 7He
    (2, 6):   (8,   3.9259,   "He",  "119.1 ms"),      # 8He
    (2, 7):   (9,   3.3490,   "He",  "unbound"),       # 9He (est.)
    (2, 8):   (10,  3.0330,   "He",  "unbound"),       # 10He (est.)
    # ── Lithium isotopes ─────────────────────────────────────
    (3, 2):   (5,   5.2667,   "Li",  "unbound"),       # 5Li
    (3, 3):   (6,   5.3326,   "Li",  "stable"),        # 6Li
    (3, 4):   (7,   5.6063,   "Li",  "stable"),        # 7Li
    (3, 5):   (8,   5.1598,   "Li",  "839.40 ms"),     # 8Li
    (3, 6):   (9,   5.0379,   "Li",  "178.3 ms"),      # 9Li
    (3, 7):   (10,  4.5311,   "Li",  "unbound"),       # 10Li
    (3, 8):   (11,  4.1544,   "Li",  "8.75 ms"),       # 11Li (halo)
    # ── Beryllium isotopes ───────────────────────────────────
    (4, 3):   (7,   5.3714,   "Be",  "53.22 d"),       # 7Be (EC)
    (4, 4):   (8,   7.0624,   "Be",  "6.7e-17 s"),     # 8Be (2α, ~0 s)
    (4, 5):   (9,   6.4628,   "Be",  "stable"),        # 9Be
    (4, 6):   (10,  6.4977,   "Be",  "1.51 Myr"),      # 10Be
    (4, 7):   (11,  5.9530,   "Be",  "13.76 s"),       # 11Be
    (4, 8):   (12,  5.7210,   "Be",  "20.20 ms"),      # 12Be
    # ── Boron isotopes ───────────────────────────────────────
    (5, 4):   (9,   6.2572,   "B",   "unbound"),       # 9B
    (5, 5):   (10,  6.4751,   "B",   "stable"),        # 10B
    (5, 6):   (11,  6.9277,   "B",   "stable"),        # 11B
    (5, 7):   (12,  6.6313,   "B",   "20.20 ms"),      # 12B
    (5, 8):   (13,  6.4956,   "B",   "17.33 ms"),      # 13B
    # ── Carbon isotopes ──────────────────────────────────────
    (6, 5):   (11,  6.6764,   "C",   "20.36 min"),     # 11C
    (6, 6):   (12,  7.6801,   "C",   "stable"),        # 12C
    (6, 7):   (13,  7.4699,   "C",   "stable"),        # 13C
    (6, 8):   (14,  7.5203,   "C",   "5730 yr"),       # 14C
    # ── Nitrogen isotopes ────────────────────────────────────
    (7, 5):   (12,  6.1703,   "N",   "11.00 ms"),      # 12N
    (7, 6):   (13,  7.2389,   "N",   "9.965 min"),     # 13N
    (7, 7):   (14,  7.4756,   "N",   "stable"),        # 14N
    # ── Oxygen isotopes ──────────────────────────────────────
    (8, 4):   (12,  5.9199,   "O",   "unbound"),       # 12O (est.)
    (8, 5):   (13,  6.8270,   "O",   "8.58 ms"),       # 13O
    (8, 8):   (16,  7.9762,   "O",   "stable"),        # 16O
    # ── Neon ─────────────────────────────────────────────────
    (10, 10): (20,  8.0325,   "Ne",  "stable"),        # 20Ne
    # ── Calcium ──────────────────────────────────────────────
    (20, 20): (40,  8.5513,   "Ca",  "stable"),        # 40Ca
    # ── Cobalt ───────────────────────────────────────────────
    (27, 33): (60,  8.7467,   "Co",  "5.271 yr"),      # 60Co
}


# ══════════════════════════════════════════════════════════════
# §2  LOAD ALL CERTIFICATES
# ══════════════════════════════════════════════════════════════

CERT_DIR = Path(__file__).parent / "../../tools/hecke-engine"

def load_certificates():
    """Load all certificate-*.json files from the hecke-engine directory."""
    certs = []
    for path in sorted(CERT_DIR.glob("certificate-*.json")):
        with open(path) as f:
            cert = json.load(f)
        cert["_path"] = str(path)
        certs.append(cert)
    return certs


# ══════════════════════════════════════════════════════════════
# §3  MASS COMPUTATION METHODS
# ══════════════════════════════════════════════════════════════

# Method A: CODATA + AME2020 (the existing approach in topological-mass-table.py)
# M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N)
# This is trivially correct — it just recombines known constants.

def mass_codata_ame(Z, N, B_per_A):
    """Atomic mass from CODATA nucleon masses + AME2020 binding energy."""
    A = Z + N
    M_free = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
    B_total = A * B_per_A
    return M_free - B_total


# Method B: Topological mass from knot volume
# 𝔪(K) = Vol(K) / ℏ_q²
# This gives mass in units of m_e. Multiply by m_e (MeV) for MeV.

def mass_topological(vol_knot):
    """Topological mass from hyperbolic knot volume."""
    return vol_knot / HBAR_Q_SQ  # in units of m_e


# Method C: From certificate polynomial evaluations
# The certificate contains tr_alt_f64, net_f64, f_pauli_f64 evaluated at q₀.
# Question: which (if any) maps to physical mass, and with what scale factor?

def mass_from_net(net_f64, scale_E0):
    """Mass from certificate net × scale factor E₀."""
    return abs(net_f64) * scale_E0


# ══════════════════════════════════════════════════════════════
# §4  EVALUATE CERTIFICATES AGAINST AME2020
# ══════════════════════════════════════════════════════════════

def evaluate_all():
    certs = load_certificates()
    
    print("=" * 120)
    print("CERTIFICATE-TO-MASS VALIDATION: 47 Hecke-Engine Certificates vs AME2020")
    print("=" * 120)
    print()
    print(f"Substrate parameter: q₀ = {Q:.15f}")
    print(f"ℏ_q = {HBAR_Q:.15f},  ℏ_q² = {HBAR_Q_SQ:.15f}")
    print(f"HA = q - q⁻¹ = {HA:.10f}")
    print(f"E_× = HA/2 = {E_CROSS:.10f}")
    print()
    
    # ── Key mass scales ──────────────────────────────────────
    m_borromean = VOL_BORROMEAN / HBAR_Q_SQ  # in m_e units
    m_borromean_MeV = m_borromean * M_E_MEV
    
    # E₀ from beta decay calibration
    E0_beta = 4.1549  # MeV (from beta-decay-energy-scale.py)
    
    print("Reference mass scales:")
    print(f"  m_e = {M_E_MEV:.11f} MeV (CODATA)")
    print(f"  m_p = {M_P_MEV:.8f} MeV (CODATA)")
    print(f"  m_n = {M_N_MEV:.8f} MeV (CODATA)")
    print(f"  𝔪(𝔅₃) = Vol(𝔅₃)/ℏ_q² = {m_borromean:.4f} m_e = {m_borromean_MeV:.3f} MeV")
    print(f"  E₀(β) = {E0_beta} MeV (calibrated from neutron β-decay)")
    print()
    
    # ── Source classification ────────────────────────────────
    # What is genuinely from q vs from CODATA/AME2020?
    print("=" * 80)
    print("SOURCE CLASSIFICATION: What comes from q vs observed data")
    print("=" * 80)
    print()
    print("FROM q ALONE (genuine predictions):")
    print(f"  • ℏ_q = {HBAR_Q:.10f}  (from Vol(4₁) and m_μ/m_e)")
    print(f"  • q₀ = {Q:.15f}")
    print(f"  • HA = {HA:.10f}")
    print(f"  • Transfer matrix T(c,d) entries")
    print(f"  • Skein polynomials P_p(q), P_n(q)")
    print(f"  • Certificate polynomial evaluations (tr_alt, net, f_pauli)")
    print(f"  • Mass RATIOS: m_μ/m_e = {MASS_RATIO_MU_E:.6f} (definitional)")
    print()
    print("FROM CODATA/AME2020 (external input, NOT predictions):")
    print(f"  • m_e = {M_E_MEV} MeV  (sets absolute MeV scale)")
    print(f"  • m_p = {M_P_MEV} MeV  (used directly in M(Z,N))")
    print(f"  • m_n = {M_N_MEV} MeV  (used directly in M(Z,N))")
    print(f"  • B/A from AME2020    (used directly in M(Z,N))")
    print()
    print("MIXED (q provides structure, CODATA sets scale):")
    print(f"  • 𝔪(𝔅₃) = Vol(𝔅₃)/ℏ_q² × m_e = topological ratio × CODATA scale")
    print(f"  • E₀ = Q_neutron/|Δnet| = CODATA Q-value / q-derived net difference")
    print()
    
    # ── Certificate evaluation ───────────────────────────────
    print("=" * 120)
    print("CERTIFICATE POLYNOMIAL VALUES vs AME2020")
    print("=" * 120)
    print()
    
    header = (
        f"{'Isotope':<8} {'Z':>3} {'N':>3} {'A':>3} "
        f"{'f_pauli':>12} {'tr_alt':>14} {'net':>14} "
        f"{'B/A(AME)':>10} {'M(CODATA)':>12} "
        f"{'Status':>10}"
    )
    print(header)
    print("-" * len(header))
    
    results = []
    matched = 0
    unmatched = 0
    
    for cert in certs:
        iso = cert["isotope"]
        Z = iso["z"]
        N = iso["n"]
        A = iso["a"]
        name = iso["name"]
        parity = iso.get("parity", "?")
        
        fp = cert.get("f_pauli_f64")
        ta = cert.get("tr_alt_f64")
        net = cert.get("net_f64")
        tm = cert.get("tr_markov_f64")
        
        # Look up AME2020 data
        key = (Z, N)
        if key in AME2020_ISOTOPES:
            A_ame, BperA, sym, half = AME2020_ISOTOPES[key]
            M_codata = mass_codata_ame(Z, N, BperA)
            status = "matched"
            matched += 1
        else:
            BperA = None
            M_codata = None
            status = "no AME"
            unmatched += 1
        
        fp_s = f"{fp:.6e}" if fp is not None else "None"
        ta_s = f"{ta:.6e}" if ta is not None else "None"
        net_s = f"{net:.6e}" if net is not None else "None"
        BperA_s = f"{BperA:.4f}" if BperA is not None else "N/A"
        M_s = f"{M_codata:.2f}" if M_codata is not None else "N/A"
        
        print(f"{name:<8} {Z:>3} {N:>3} {A:>3} {fp_s:>12} {ta_s:>14} {net_s:>14} {BperA_s:>10} {M_s:>12} {status:>10}")
        
        results.append({
            "isotope": name,
            "Z": Z,
            "N": N,
            "A": A,
            "parity": parity,
            "f_pauli_f64": fp,
            "tr_alt_f64": ta,
            "net_f64": net,
            "tr_markov_f64": tm,
            "B_per_A_AME2020": BperA,
            "M_CODATA_MeV": round(M_codata, 4) if M_codata else None,
            "status": status,
        })
    
    print()
    print(f"Matched to AME2020: {matched}/{len(certs)}")
    print(f"Without AME2020 data: {unmatched}/{len(certs)}")
    print()
    print("NOTE: 'Matched' means AME2020 has binding-energy data for this isotope.")
    print("It does NOT mean the certificate predicts the mass. There is currently")
    print("no formula mapping certificate polynomial fields → B/A in MeV.")
    
    # ── Per-isotope observed vs certificate detail ───────────
    print()
    print("=" * 120)
    print("PER-ISOTOPE DETAIL: AME2020 observed B/A vs certificate polynomial fields")
    print("=" * 120)
    print()
    print("For each isotope we show the AME2020 observed binding energy per nucleon")
    print("alongside the certificate's three polynomial evaluations at q₀.")
    print("NONE of these fields maps to B/A via a known formula — they encode")
    print("combinatorial crossing structure, not mass directly.")
    print()
    
    matched_data = [r for r in results if r["M_CODATA_MeV"] is not None and r["net_f64"] is not None]
    
    if matched_data:
        header2 = (
            f"{'Isotope':<8} {'A':>3} {'B/A(AME)':>10} {'M(AME,MeV)':>12} "
            f"{'f_pauli':>12} {'|net|':>14} {'M/|net|':>14} "
            f"{'Category':>12}"
        )
        print(header2)
        print("-" * len(header2))
        
        for r in matched_data:
            M = r["M_CODATA_MeV"]
            BperA = r["B_per_A_AME2020"]
            net = r["net_f64"]
            fp = r["f_pauli_f64"]
            abs_net = abs(net) if net else 0
            ratio = M / abs_net if abs_net > 1e-30 else float('inf')
            
            # Classify: what kind of isotope is this?
            A = r["A"]
            cat = "light" if A <= 14 else "medium" if A <= 40 else "heavy"
            
            BperA_s = f"{BperA:.4f}" if BperA is not None else "N/A"
            
            print(
                f"{r['isotope']:<8} {r['A']:>3} {BperA_s:>10} {M:>12.2f} "
                f"{fp:>12.6e} {abs_net:>14.6e} {ratio:>14.4e} "
                f"{cat:>12}"
            )
    
    # ── Analysis summary ─────────────────────────────────────
    print()
    print("=" * 80)
    print("ANALYSIS: Certificate Field → Mass Correlation")
    print("=" * 80)
    print()
    print("KEY FINDINGS:")
    print()
    print("1. The net_f64 values span ~50 orders of magnitude (1e+47 for 60Co")
    print("   down to 1e-8 for light isotopes). There is NO simple linear")
    print("   relationship net × E₀ = M(MeV) that works across all isotopes.")
    print()
    print("2. The f_pauli_f64 values are O(1) for all isotopes (~0.001 to ~2.5).")
    print("   This is the Pauli exclusion statistical factor, not a mass predictor.")
    print()
    print("3. The tr_alt_f64 and net_f64 encode the Skein polynomial P(q₀),")
    print("   which gives COMBINATORIAL structure (crossing patterns), not mass.")
    print()
    print("=" * 80)
    print("SCALING PARAMETERS")
    print("=" * 80)
    print()
    print("PARAMETER 1 (required): m_e = 0.51099895 MeV (CODATA 2022)")
    print("  This is our RULER — it converts dimensionless q-derived quantities")
    print("  to physical MeV. Without m_e, we can only predict dimensionless ratios.")
    print("  The substrate parameter q fixes mass RATIOS (m_μ/m_e = Vol(4₁)/ℏ_q²)")
    print("  but the absolute MeV scale requires one external input.")
    print()
    print("PARAMETER 2 (potential, TODO): E₀ ≈ 4.155 MeV")
    print("  Calibrated from neutron β-decay: E₀ = Q_neutron / |Δnet|.")
    print("  Currently derived FROM observed Q-value and q-computed Δnet.")
    print("  May be derivable from q alone if B/A computation is achieved.")
    print("  TODO: Determine if E₀ is independent of m_e or follows from it.")
    print()
    print("=" * 80)
    print("SOURCE CLASSIFICATION")
    print("=" * 80)
    print()
    print("CURRENT MASS COMPUTATION: M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N)")
    print("  uses CODATA m_p, m_n and AME2020 B/A. This is trivially correct")
    print("  because it recombines observed values — it is NOT a prediction.")
    print("  The 0.0000% deviations in the mass tables just confirm arithmetic.")
    print()
    print("GENUINE q-PREDICTIONS possible:")
    print("  a) Mass RATIOS between particles (e.g., m_μ/m_e = Vol(4₁)/ℏ_q²)")
    print("  b) Q-values = mass DIFFERENCES (e.g., neutron β-decay Q)")
    print("  c) Half-life RATIOS via log_q(ft) spectroscopy")
    print("  d) Binding energy per nucleon B/A from transfer matrix (NOT YET DONE)")
    print()
    print("=" * 80)
    print("THE OPEN PROBLEM: B/A from q")
    print("=" * 80)
    print()
    print("PHYSICS: The binding energy per nucleon B/A measures how tightly")
    print("nucleons are bound inside a nucleus. For stable nuclei, B/A ≈ 7-9 MeV.")
    print("This is the difference between the mass of free nucleons and the")
    print("actual nuclear mass: B = Z·m_p + N·m_n − M_nucleus.")
    print()
    print("In QOU, each nucleus has a topological structure: nucleon braids")
    print("joined by inter-nucleon crossings. The transfer matrix product")
    print("∏ᵢ V̂ᵢ(q) gives the Skein polynomial P(q), whose evaluation at q₀")
    print("encodes the crossing pattern. The OPEN QUESTION is:")
    print()
    print("  Can B/A be extracted from the certificate polynomial P(q₀)?")
    print()
    print("If yes, then M(Z,N) = Z·m_p(q) + N·m_n(q) + Z·m_e − A·(B/A)(q)")
    print("would be a GENUINE prediction from q + m_e alone.")
    print("If no, B/A remains an external input and mass tables are tautological.")
    print()
    print("The certificate fields (net, tr_alt, f_pauli) currently show no")
    print("simple mapping to B/A. This is the critical open problem.")
    
    # ── Build witness ────────────────────────────────────────
    w = WitnessBuilder("certificate-to-mass", engine="python")
    w.set_description(
        "Validation of 47 hecke-engine certificates against AME2020 atomic masses. "
        "Evaluates certificate polynomial fields (tr_alt, net, f_pauli) at q₀ and "
        "compares to observed masses. Documents which computations are genuine "
        "predictions from q vs recombinations of CODATA/AME2020 inputs."
    )
    
    w.add_parameter("q₀", Q)
    w.add_parameter("q₀_err", Q_ERR)
    w.add_parameter("ℏ_q", HBAR_Q)
    w.add_parameter("ℏ_q²", HBAR_Q_SQ)
    w.add_parameter("m_e (MeV)", M_E_MEV)
    w.add_parameter("m_p (MeV)", M_P_MEV)
    w.add_parameter("m_n (MeV)", M_N_MEV)
    w.add_parameter("certificates_count", len(certs))
    w.add_parameter("ame2020_matched", matched)
    
    # Assertions
    w.add_assertion(
        "All 47 certificates loaded",
        computed=len(certs),
        expected=47,
        tolerance=0,
        source="tools/hecke-engine/certificate-*.json",
    )
    
    w.add_assertion(
        "AME2020 lookup exists for all 47 certificates (NOT a prediction test)",
        computed=matched,
        expected=47,
        tolerance=0,
        source="AME2020 binding energy database",
    )
    
    # Note: no certificate→mass formula exists yet, so no prediction
    # assertions can be made. The "matched" count means AME2020 has
    # B/A data for these isotopes, not that any certificate field
    # reproduces the observed mass.
    
    # Record individual certificate results
    w.add_data("certificate_results", results)
    
    # Source classification
    w.add_data("source_classification", {
        "from_q_alone": [
            "ℏ_q, q₀, HA (substrate parameter chain)",
            "Transfer matrix T(c,d) entries",
            "Skein polynomials P(q)",
            "Certificate polynomial evaluations",
            "Mass ratio m_μ/m_e (definitional)",
        ],
        "from_codata_ame2020": [
            "m_e (absolute MeV scale — the RULER)",
            "m_p, m_n (nucleon masses)",
            "B/A (binding energy per nucleon)",
        ],
        "mixed": [
            "Topological mass 𝔪(K) = Vol(K)/ℏ_q² × m_e",
            "E₀ = Q_neutron / |Δnet|",
        ],
        "genuine_predictions_possible": [
            "Mass ratios between particles",
            "Q-values (mass differences) from Δnet × E₀",
            "Half-life ratios via log_q(ft)",
            "B/A from transfer matrix (NOT YET IMPLEMENTED)",
        ],
    })
    
    w.add_data("scaling_parameters", {
        "parameter_1_required": {
            "name": "m_e",
            "value_MeV": M_E_MEV,
            "source": "CODATA 2022",
            "role": "Absolute MeV scale (ruler). Converts dimensionless q-derived "
                    "quantities to physical units. Without m_e, only dimensionless "
                    "ratios (m_μ/m_e, etc.) can be predicted.",
        },
        "parameter_2_potential_TODO": {
            "name": "E₀",
            "value_MeV": E0_beta,
            "source": "Calibrated from neutron β-decay: E₀ = Q/|Δnet|",
            "role": "Energy scale for Q-value predictions from net differences. "
                    "Currently derived from observed Q and q-computed Δnet. "
                    "TODO: determine if E₀ is independently derivable from q "
                    "or if it reduces to m_e × f(q).",
        },
    })
    
    w.add_data("open_problem_B_over_A", {
        "statement": "Compute B/A purely from q without importing AME2020 values",
        "physics": "B/A measures how tightly nucleons bind. For stable nuclei, "
                   "B/A ≈ 7-9 MeV. In QOU, each nucleus has a topological "
                   "structure (nucleon braids + inter-nucleon crossings) whose "
                   "transfer matrix product gives the Skein polynomial P(q). "
                   "The question is: can B/A be extracted from P(q₀)?",
        "current_status": "No formula maps certificate fields (net, tr_alt, "
                          "f_pauli) to B/A. The net values span ~50 orders "
                          "of magnitude while B/A varies 0-9 MeV.",
        "if_solved": "M(Z,N) = Z·m_p(q) + N·m_n(q) + Z·m_e − A·(B/A)(q) "
                     "would be genuine predictions from q + m_e alone.",
    })
    
    w.save()
    print()
    print("Witness written to certificate-to-mass.witness.json")
    return results


if __name__ == "__main__":
    evaluate_all()
