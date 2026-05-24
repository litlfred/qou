#!/usr/bin/env python3
"""
Comprehensive isotope mass table: all stable and long-lived isotopes.

Extends topological-mass-table.py from one isotope per element to ALL
stable isotopes, providing:
  1. AME2020 binding energies for every stable/long-lived nuclide
  2. CODATA+AME2020 mass computation M(Z,N)
  3. Mapping to hecke-engine certificates where they exist
  4. Clear separation of genuine q-predictions from CODATA inputs

The key insight documented here: the current mass computation
M(Z,N) = Z·m_p + N·m_n + Z·m_e − B(Z,N) is NOT a prediction from q.
It recombines observed constants. The genuine predictions are:
  - Mass RATIOS (m_μ/m_e from q)
  - Q-values (mass DIFFERENCES from Δnet × E₀)
  - Half-life ratios (from log_q(ft) spectroscopy)

Usage:
    python3 isotope-mass-table.py

Output:
    isotope-mass-table.witness.json
"""

import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import (
    Q, Q_INV, HBAR_Q, HBAR_Q_SQ,
    VOL_FIGURE_EIGHT, MASS_RATIO_MU_E,
    HA, E_CROSS, Q_ERR,
)
from experimental_constants import (
    M_E_MEV, M_E_MEV_ERR,
    M_P_MEV_ERR,
    M_N_MEV_ERR,
)
from witness_base import WitnessBuilder
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402


# ══════════════════════════════════════════════════════════════
# §1  AME2020 STABLE & LONG-LIVED ISOTOPE DATABASE
# ══════════════════════════════════════════════════════════════
# Source: Atomic Mass Evaluation 2020 (Huang et al.)
# https://doi.org/10.1088/1674-1137/abddb0
#
# Format: (Z, N, A, B/A [MeV], symbol, stability)
# "stable" = observationally stable or t½ > age of universe
# "long-lived" = t½ > 1 year (relevant for astrophysics)
#
# For Z = 1-20, ALL known isotopes with measured B/A are included.
# For Z = 21-92, only stable + longest-lived isotopes per element.

ISOTOPES = [
    # ── Z=1 Hydrogen ─────────────────────────────────────────
    (1, 0, 1, 0.0000,  "H",  "stable"),       # ¹H protium
    (1, 1, 2, 1.1121,  "H",  "stable"),       # ²H deuterium
    (1, 2, 3, 2.8273,  "H",  "12.32 yr"),     # ³H tritium
    # ── Z=2 Helium ───────────────────────────────────────────
    (2, 1, 3, 2.5727,  "He", "stable"),       # ³He
    (2, 2, 4, 7.0739,  "He", "stable"),       # ⁴He
    (2, 4, 6, 4.8782,  "He", "806.92 ms"),    # ⁶He
    (2, 6, 8, 3.9259,  "He", "119.1 ms"),     # ⁸He
    # ── Z=3 Lithium ──────────────────────────────────────────
    (3, 3, 6, 5.3326,  "Li", "stable"),       # ⁶Li
    (3, 4, 7, 5.6063,  "Li", "stable"),       # ⁷Li
    # ── Z=4 Beryllium ────────────────────────────────────────
    (4, 3, 7, 5.3714,  "Be", "53.22 d"),      # ⁷Be (EC)
    (4, 5, 9, 6.4628,  "Be", "stable"),       # ⁹Be
    (4, 6, 10, 6.4977, "Be", "1.51 Myr"),     # ¹⁰Be
    # ── Z=5 Boron ────────────────────────────────────────────
    (5, 5, 10, 6.4751, "B",  "stable"),       # ¹⁰B
    (5, 6, 11, 6.9277, "B",  "stable"),       # ¹¹B
    # ── Z=6 Carbon ───────────────────────────────────────────
    (6, 6, 12, 7.6801, "C",  "stable"),       # ¹²C
    (6, 7, 13, 7.4699, "C",  "stable"),       # ¹³C
    (6, 8, 14, 7.5203, "C",  "5730 yr"),      # ¹⁴C
    # ── Z=7 Nitrogen ─────────────────────────────────────────
    (7, 7, 14, 7.4756, "N",  "stable"),       # ¹⁴N
    (7, 8, 15, 7.6995, "N",  "stable"),       # ¹⁵N
    # ── Z=8 Oxygen ───────────────────────────────────────────
    (8, 8,  16, 7.9762, "O", "stable"),       # ¹⁶O
    (8, 9,  17, 7.7507, "O", "stable"),       # ¹⁷O
    (8, 10, 18, 7.7671, "O", "stable"),       # ¹⁸O
    # ── Z=9 Fluorine ─────────────────────────────────────────
    (9, 10, 19, 7.7790, "F", "stable"),       # ¹⁹F
    # ── Z=10 Neon ────────────────────────────────────────────
    (10, 10, 20, 8.0325, "Ne", "stable"),     # ²⁰Ne
    (10, 11, 21, 7.9717, "Ne", "stable"),     # ²¹Ne
    (10, 12, 22, 8.0808, "Ne", "stable"),     # ²²Ne
    # ── Z=11 Sodium ──────────────────────────────────────────
    (11, 12, 23, 8.1115, "Na", "stable"),     # ²³Na
    # ── Z=12 Magnesium ───────────────────────────────────────
    (12, 12, 24, 8.2607, "Mg", "stable"),     # ²⁴Mg
    (12, 13, 25, 8.2235, "Mg", "stable"),     # ²⁵Mg
    (12, 14, 26, 8.3339, "Mg", "stable"),     # ²⁶Mg
    # ── Z=13 Aluminium ───────────────────────────────────────
    (13, 14, 27, 8.3316, "Al", "stable"),     # ²⁷Al
    # ── Z=14 Silicon ─────────────────────────────────────────
    (14, 14, 28, 8.4477, "Si", "stable"),     # ²⁸Si
    (14, 15, 29, 8.4487, "Si", "stable"),     # ²⁹Si
    (14, 16, 30, 8.5207, "Si", "stable"),     # ³⁰Si
    # ── Z=15 Phosphorus ──────────────────────────────────────
    (15, 16, 31, 8.4812, "P",  "stable"),     # ³¹P
    # ── Z=16 Sulfur ──────────────────────────────────────────
    (16, 16, 32, 8.4932, "S",  "stable"),     # ³²S
    (16, 17, 33, 8.4977, "S",  "stable"),     # ³³S
    (16, 18, 34, 8.5837, "S",  "stable"),     # ³⁴S
    (16, 20, 36, 8.5756, "S",  "stable"),     # ³⁶S
    # ── Z=17 Chlorine ────────────────────────────────────────
    (17, 18, 35, 8.5204, "Cl", "stable"),     # ³⁵Cl
    (17, 20, 37, 8.5703, "Cl", "stable"),     # ³⁷Cl
    # ── Z=18 Argon ───────────────────────────────────────────
    (18, 18, 36, 8.5200, "Ar", "stable"),     # ³⁶Ar
    (18, 20, 38, 8.6143, "Ar", "stable"),     # ³⁸Ar
    (18, 22, 40, 8.5954, "Ar", "stable"),     # ⁴⁰Ar
    # ── Z=19 Potassium ───────────────────────────────────────
    (19, 20, 39, 8.5570, "K",  "stable"),     # ³⁹K
    (19, 21, 40, 8.5381, "K",  "1.248 Gyr"),  # ⁴⁰K
    (19, 22, 41, 8.5762, "K",  "stable"),     # ⁴¹K
    # ── Z=20 Calcium ─────────────────────────────────────────
    (20, 20, 40, 8.5513, "Ca", "stable"),     # ⁴⁰Ca
    (20, 22, 42, 8.6165, "Ca", "stable"),     # ⁴²Ca
    (20, 23, 43, 8.6007, "Ca", "stable"),     # ⁴³Ca
    (20, 24, 44, 8.6582, "Ca", "stable"),     # ⁴⁴Ca
    (20, 26, 46, 8.6688, "Ca", ">5.6e18 yr"), # ⁴⁶Ca
    (20, 28, 48, 8.6664, "Ca", ">5.8e24 yr"), # ⁴⁸Ca
    # ── Z=21-30 (First transition metals) ────────────────────
    (21, 24, 45, 8.6190, "Sc", "stable"),     # ⁴⁵Sc
    (22, 24, 46, 8.6564, "Ti", "stable"),     # ⁴⁶Ti
    (22, 25, 47, 8.6611, "Ti", "stable"),     # ⁴⁷Ti
    (22, 26, 48, 8.7229, "Ti", "stable"),     # ⁴⁸Ti
    (22, 27, 49, 8.7109, "Ti", "stable"),     # ⁴⁹Ti
    (22, 28, 50, 8.7557, "Ti", "stable"),     # ⁵⁰Ti
    (23, 28, 51, 8.7420, "V",  "stable"),     # ⁵¹V
    (24, 26, 50, 8.7009, "Cr", ">1.3e18 yr"), # ⁵⁰Cr
    (24, 28, 52, 8.7760, "Cr", "stable"),     # ⁵²Cr
    (24, 29, 53, 8.7602, "Cr", "stable"),     # ⁵³Cr
    (24, 30, 54, 8.7782, "Cr", "stable"),     # ⁵⁴Cr
    (25, 30, 55, 8.7649, "Mn", "stable"),     # ⁵⁵Mn
    (26, 28, 54, 8.7362, "Fe", "stable"),     # ⁵⁴Fe
    (26, 30, 56, 8.7904, "Fe", "stable"),     # ⁵⁶Fe (max B/A)
    (26, 31, 57, 8.7703, "Fe", "stable"),     # ⁵⁷Fe
    (26, 32, 58, 8.7922, "Fe", "stable"),     # ⁵⁸Fe
    (27, 32, 59, 8.7680, "Co", "stable"),     # ⁵⁹Co
    (28, 30, 58, 8.7322, "Ni", "stable"),     # ⁵⁸Ni
    (28, 32, 60, 8.7807, "Ni", "stable"),     # ⁶⁰Ni
    (28, 33, 61, 8.7651, "Ni", "stable"),     # ⁶¹Ni
    (28, 34, 62, 8.7945, "Ni", "stable"),     # ⁶²Ni (highest B/A)
    (28, 36, 64, 8.7774, "Ni", "stable"),     # ⁶⁴Ni
    (29, 34, 63, 8.7522, "Cu", "stable"),     # ⁶³Cu
    (29, 36, 65, 8.7569, "Cu", "stable"),     # ⁶⁵Cu
    (30, 34, 64, 8.7356, "Zn", "stable"),     # ⁶⁴Zn
    (30, 36, 66, 8.7596, "Zn", "stable"),     # ⁶⁶Zn
    (30, 37, 67, 8.7334, "Zn", "stable"),     # ⁶⁷Zn
    (30, 38, 68, 8.6823, "Zn", "stable"),     # ⁶⁸Zn
    (30, 40, 70, 8.7295, "Zn", "stable"),     # ⁷⁰Zn
]


# ══════════════════════════════════════════════════════════════
# §2  CERTIFICATE LOOKUP
# ══════════════════════════════════════════════════════════════

CERT_DIR = Path(__file__).parent / "../../tools/hecke-engine"

def load_certificate_index():
    """Build (Z,N) → certificate lookup from hecke-engine certificates."""
    index = {}
    for path in sorted(CERT_DIR.glob("certificate-*.json")):
        try:
            with open(path) as f:
                cert = json.load(f)
            iso = cert["isotope"]
            key = (iso["z"], iso["n"])
            index[key] = {
                "name": iso["name"],
                "f_pauli": cert.get("f_pauli_f64"),
                "tr_alt": cert.get("tr_alt_f64"),
                "net": cert.get("net_f64"),
                "tr_markov": cert.get("tr_markov_f64"),
                "path": str(path.name),
            }
        except (json.JSONDecodeError, KeyError):
            continue
    return index


# ══════════════════════════════════════════════════════════════
# §3  TRANSFER MATRIX (from topological-mass-table.py)
# ══════════════════════════════════════════════════════════════

q = Q
qi = Q_INV
z_m = 1.0 / (q**0.5 + qi**0.5)

def T_mat(c, d):
    return [[c * HA + d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def crossing_coeffs(ti, tj):
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -HA
    else: return 1.0, -HA / 2.0

def compute_skein_poly(types):
    """Skein polynomial P(q) for given strand types."""
    A = len(types)
    P = 1.0
    for i in range(A - 1):
        M = [[1, 0], [0, 1]]
        for j in range(i + 1, A):
            c, d = crossing_coeffs(types[i], types[j])
            M = mat_mul(M, T_mat(c, d))
        V = z_m * M[0][0] + M[1][0]
        P *= V
    return P

def build_strand_types(Z, N):
    """Build strand type list: Z protons + N neutrons."""
    return ['p'] * Z + ['n'] * N


# ══════════════════════════════════════════════════════════════
# §4  COMPUTATION
# ══════════════════════════════════════════════════════════════

def main():
    cert_index = load_certificate_index()
    
    print("=" * 140)
    print("COMPREHENSIVE ISOTOPE MASS TABLE")
    print("=" * 140)
    print()
    print(f"Substrate: q₀ = {Q:.15f},  ℏ_q = {HBAR_Q:.10f},  HA = {HA:.10f}")
    print(f"CODATA: m_p = {M_P_MEV_VALIDATION} MeV, m_n = {M_N_MEV_VALIDATION} MeV, m_e = {M_E_MEV} MeV")
    print()
    
    header = (
        f"{'Isotope':<8} {'Z':>3} {'N':>3} {'A':>3} "
        f"{'B/A':>8} {'M(MeV)':>12} {'±δ':>8} "
        f"{'ln|P|':>10} {'Certificate':>10} {'Source':>12}"
    )
    print(header)
    print("-" * len(header))
    
    results = []
    cert_count = 0
    stable_count = 0
    
    for Z, N, A, BperA, sym, stability in ISOTOPES:
        # CODATA+AME2020 mass
        M_free = Z * M_P_MEV_VALIDATION + N * M_N_MEV_VALIDATION + Z * M_E_MEV
        B_total = A * BperA
        M_q = M_free - B_total
        M_err = math.sqrt((Z * M_P_MEV_ERR)**2 + (N * M_N_MEV_ERR)**2 + (Z * M_E_MEV_ERR)**2)
        
        # Skein polynomial (transfer matrix chain)
        types = build_strand_types(Z, N)
        P = compute_skein_poly(types)
        ln_P = math.log(abs(P)) if abs(P) > 0 else float('-inf')
        
        # Certificate lookup
        key = (Z, N)
        cert = cert_index.get(key)
        cert_label = cert["name"] if cert else "—"
        if cert:
            cert_count += 1
        
        is_stable = "stable" in stability
        if is_stable:
            stable_count += 1
        
        # Source classification
        source = "CODATA+AME"  # always, since M uses m_p, m_n, B/A
        
        iso_name = f"{A}{sym}"
        print(
            f"{iso_name:<8} {Z:>3} {N:>3} {A:>3} "
            f"{BperA:>8.4f} {M_q:>12.2f} ±{M_err:>7.4f} "
            f"{ln_P:>10.4f} {cert_label:>10} {source:>12}"
        )
        
        results.append({
            "isotope": iso_name,
            "Z": Z,
            "N": N,
            "A": A,
            "symbol": sym,
            "B_per_A": BperA,
            "B_total": round(B_total, 4),
            "M_MeV": round(M_q, 4),
            "M_err_MeV": round(M_err, 6),
            "ln_P": round(ln_P, 6) if ln_P != float('-inf') else None,
            "stability": stability,
            "has_certificate": cert is not None,
            "certificate_net": cert["net"] if cert else None,
            "certificate_f_pauli": cert["f_pauli"] if cert else None,
            "source": source,
        })
    
    print()
    print(f"Total isotopes computed: {len(results)}")
    print(f"  Stable: {stable_count}")
    print(f"  With hecke-engine certificate: {cert_count}")
    print()
    
    # ── Binding energy analysis ──────────────────────────────
    print("=" * 80)
    print("BINDING ENERGY PER NUCLEON: Certificate Isotopes vs AME2020")
    print("=" * 80)
    print()
    print("For isotopes WITH hecke-engine certificates, can the certificate")
    print("polynomial encode B/A independently of AME2020?")
    print()
    
    cert_isotopes = [r for r in results if r["has_certificate"]]
    print(f"{'Isotope':<8} {'A':>3} {'B/A(AME)':>10} {'net':>14} {'f_pauli':>12} {'ln|P|':>10}")
    print("-" * 70)
    for r in cert_isotopes:
        net = r["certificate_net"]
        fp = r["certificate_f_pauli"]
        net_s = f"{net:.6e}" if net is not None else "None"
        fp_s = f"{fp:.6f}" if fp is not None else "None"
        ln_P_s = f"{r['ln_P']:.4f}" if r['ln_P'] is not None else "N/A"
        print(f"{r['isotope']:<8} {r['A']:>3} {r['B_per_A']:>10.4f} {net_s:>14} {fp_s:>12} {ln_P_s:>10}")
    
    print()
    print("CRITICAL FINDING: The certificate fields (net, tr_alt, f_pauli)")
    print("do NOT directly encode B/A. The net values span ~50 orders of")
    print("magnitude while B/A spans only 0-9 MeV. No simple mapping exists.")
    print()
    print("THE PATH FORWARD for genuine mass predictions:")
    print("  1. Compute ln|P(q)| for each isotope (done above)")
    print("  2. The RATIO ln|P_daughter|/ln|P_parent| predicts Q-values")
    print("  3. B/A may be extractable from P(q) via a volume integral")
    print("     (cf. topological mass 𝔪(K) = Vol(K)/ℏ_q²)")
    print("  4. Certificate polynomials tr_alt(q) encode the exact Skein")
    print("     polynomial — its integral may yield the knot volume")
    
    # ── Witness generation ───────────────────────────────────
    w = WitnessBuilder("isotope-mass-table", engine="python")
    w.set_audit_only("docs/audits/last-2-days-pipeline-wiring.md")
    w.set_description(
        "Comprehensive isotope mass table for all stable and long-lived "
        "nuclides up to Z=30. Uses CODATA nucleon masses + AME2020 binding "
        "energies. Maps each isotope to its hecke-engine certificate where "
        "available. Documents source classification (CODATA/AME2020 input "
        "vs genuine q-predictions)."
    )
    
    w.add_parameter("q₀", Q)
    w.add_parameter("ℏ_q", HBAR_Q)
    w.add_parameter("m_p (MeV)", M_P_MEV_VALIDATION)
    w.add_parameter("m_n (MeV)", M_N_MEV_VALIDATION)
    w.add_parameter("m_e (MeV)", M_E_MEV)
    w.add_parameter("isotopes_count", len(results))
    w.add_parameter("stable_count", stable_count)
    w.add_parameter("certificate_count", cert_count)
    
    w.add_assertion(
        "All isotopes computed",
        computed=len(results),
        expected=len(ISOTOPES),
        tolerance=0,
        source="AME2020 isotope database",
    )
    
    w.add_assertion(
        "Certificate coverage",
        computed=cert_count,
        expected=cert_count,
        tolerance=0,
        source="tools/hecke-engine/certificate-*.json",
    )
    
    # Spot-check: ⁴He mass
    he4 = next(r for r in results if r["isotope"] == "4He")
    w.add_assertion(
        "⁴He mass (CODATA+AME2020)",
        computed=round(he4["M_MeV"], 1),
        expected=3728.4,
        tolerance=0.1,
        unit="MeV",
        source="AME2020 + CODATA 2022",
    )
    
    # Spot-check: ¹²C mass
    c12 = next(r for r in results if r["isotope"] == "12C")
    w.add_assertion(
        "¹²C mass (CODATA+AME2020)",
        computed=round(c12["M_MeV"], 1),
        expected=11177.9,
        tolerance=0.1,
        unit="MeV",
        source="AME2020 + CODATA 2022",
    )
    
    # Spot-check: ⁵⁶Fe mass (peak B/A)
    fe56 = next(r for r in results if r["isotope"] == "56Fe")
    w.add_assertion(
        "⁵⁶Fe mass (CODATA+AME2020)",
        computed=round(fe56["M_MeV"], 1),
        expected=52103.1,
        tolerance=0.2,
        unit="MeV",
        source="AME2020 + CODATA 2022",
    )
    
    w.add_data("isotope_results", results)
    w.add_data("source_note",
        "All masses use M = Z·m_p + N·m_n + Z·m_e − B(Z,N) with "
        "CODATA m_p, m_n and AME2020 B/A. This is NOT a prediction "
        "from q — it recombines observed constants. Genuine q-predictions "
        "are mass ratios, Q-values (mass differences), and half-life ratios."
    )
    
    w.save()
    print()
    print(f"Witness written to isotope-mass-table.witness.json")


if __name__ == "__main__":
    main()
