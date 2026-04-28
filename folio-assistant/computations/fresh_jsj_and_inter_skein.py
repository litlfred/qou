#!/usr/bin/env python3
"""
Two fresh attempts at closing the neutron-tower gap:

  (A) JSJ decomposition of neutron vs proton braid closures.
      Check if neutron closure has a hyperbolic piece the proton
      doesn't, which could account for mass difference.

  (B) Derive inter-nucleon Skein masses S_pp, S_pn, S_nn by analogy
      with the paper's intra-nucleon S_uu, S_ud, S_dd formulas, but
      applied at the NUCLEON level (one meta-step up).  Test whether
      these can give B(D), B(T), etc.

Paper's intra-nucleon Skein:
  S_uu(q, μ_u) = (q+q⁻¹) μ_u / (q^½+q⁻^½)
  S_ud(q, μ_u, μ_d) = (q μ_u + q⁻¹ μ_d) / (q^½+q⁻^½)

Claim to test: for composite nucleons, inter-nucleon Skein has same
FORM with μ_p, μ_n replacing μ_u, μ_d.  Binding contribution per
inter-nucleon pair derived from Skein differences.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 40
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
me = mp.mpf(str(M_E_MEV))
m_p = mp.mpf(str(M_P_MEV))
m_n = mp.mpf(str(M_N_MEV))
h = Q0 - QI

# ── (A) JSJ decomposition check ────────────────────────────────
print("=" * 100)
print("(A) JSJ decomposition of proton/neutron branch closures")
print("=" * 100)

try:
    import snappy

    # Proton branches (from earlier analysis)
    test_braids = [
        ('p_b0_σ0^7·σ1⁻⁴', [1,1,1,1,1,1,1,-2,-2,-2,-2]),
        ('p_b1_σ0^7·σ1⁻²', [1,1,1,1,1,1,1,-2,-2]),
        ('p_b2_σ0^5·σ1⁻⁴', [1,1,1,1,-1,1,1,-2,-2,-2,-2]),
        ('p_b3_σ0^5·σ1⁻²', [1,1,1,1,-1,1,1,-2,-2]),
        ('n_b0_σ0^7·σ1⁻⁴', [1,1,1,1,1,1,1,-2,-2,-2,-2]),
        ('n_b1_σ0^5·σ1⁻⁴', [1,1,1,1,-1,1,1,-2,-2,-2,-2]),
        ('n_b2_σ0^3σ0·σ1⁻⁴', [1,1,1,-1,1,1,1,-2,-2,-2,-2]),
        ('n_b3_σ0^3σ0⁻²·σ1⁻⁴', [1,1,1,-1,-1,1,1,-2,-2,-2,-2]),
    ]

    jsj_results = []
    for name, word in test_braids:
        try:
            L = snappy.Link(braid_closure=word)
            M = L.exterior()
            # Try JSJ
            M.randomize()
            try:
                v = float(M.volume().real if hasattr(M.volume(), 'real') else M.volume())
            except Exception:
                v = 0.0
            sol_type = M.solution_type()
            # Try cusp count + triangulation info
            n_cusps = M.num_cusps()
            try:
                hom = str(M.homology())
            except Exception:
                hom = "n/a"
            print(f"  {name:<25} vol={v:+.6f} sol={sol_type:<30} "
                  f"n_cusps={n_cusps} H_1={hom}")
            jsj_results.append({
                'name': name, 'braid_word': word,
                'volume': v, 'solution_type': sol_type,
                'n_cusps': n_cusps, 'h1': hom,
            })
        except Exception as e:
            print(f"  {name:<25} ERR: {type(e).__name__}: {str(e)[:60]}")
except ImportError:
    print("  SnapPy not available")
    jsj_results = []

print()

# ── (B) Inter-nucleon Skein derivation ─────────────────────────
print("=" * 100)
print("(B) Inter-nucleon Skein masses — S_pp, S_pn, S_nn")
print("=" * 100)

K = (Q0 + QI) / (mp.sqrt(Q0) + mp.sqrt(QI))   # (q+q⁻¹)/(q^½+q⁻^½)
Kp = mp.sqrt(Q0) + mp.sqrt(QI)   # denominator q^½+q⁻^½

# Test: same-form Skein at nucleon level with μ_p = m_p, μ_n = m_n
S_pp = K * m_p
S_nn = K * m_n
S_pn = (Q0 * m_p + QI * m_n) / Kp

print(f"  K(q) = (q+q⁻¹)/(q^½+q⁻^½) = {float(K):.8f}")
print(f"  Using μ_p = m_p = {float(m_p)} MeV, μ_n = m_n = {float(m_n)} MeV:")
print(f"    S_pp = {float(S_pp):.4f} MeV")
print(f"    S_pn = {float(S_pn):.4f} MeV")
print(f"    S_nn = {float(S_nn):.4f} MeV")
print()

# Binding hypotheses:
print("  Binding hypotheses:")
# H1: B(D) = S_pn (single pn pair contribution)
print(f"    H1: B(D) = S_pn = {float(S_pn):.4f}  vs CODATA 2.225 → err {float((S_pn-2.225)/2.225*100):+.1f}%")
# H2: B(D) = S_pn − (S_pp + S_nn)/2 (deviation from symmetric)
dev = S_pn - (S_pp + S_nn)/2
print(f"    H2: B(D) = S_pn − (S_pp+S_nn)/2 = {float(dev):.6f}")
# H3: B(D) = |S_pp − S_pn| (asymmetry)
asym = mp.fabs(S_pp - S_pn)
print(f"    H3: B(D) = |S_pp − S_pn| = {float(asym):.4f}  vs 2.225 → err {float((asym-2.225)/2.225*100):+.1f}%")
# H4: B(D) = (K−1)·(m_p + m_n)
H4 = (K - 1) * (m_p + m_n)
print(f"    H4: B(D) = (K−1)·(m_p+m_n) = {float(H4):.4f}  vs 2.225 → err {float((H4-2.225)/2.225*100):+.1f}%")
# H5: B(D) = (K·(m_p+m_n)/2) − (m_p+m_n)/2
H5 = (K - 1) * (m_p + m_n) / 2
print(f"    H5: B(D) = (K−1)·(m_p+m_n)/2 = {float(H5):.4f}  vs 2.225 → err {float((H5-2.225)/2.225*100):+.1f}%")
# H6: Jones-polynomial style B = sum |S_xy − (m_x + m_y)/2|
# For D: only pn pair
pn_defect = S_pn - (m_p + m_n) / 2
print(f"    H6: B(D) = S_pn − avg(m_p, m_n) = {float(pn_defect):.6f}")

print()
print("  For T (Z=1, N=2 — inter-nucleon pairs: 2 pn + 1 nn):")
# Multiple pair contributions
B_T_h1 = 2*S_pn + S_nn   # sum of inter pairs
print(f"    H1_T: 2·S_pn + S_nn = {float(B_T_h1):.4f}  (nonsense — too big)")
B_T_h4 = (K - 1) * (2*m_p + 3*m_n)   # with Z+N nucleon mass sum scaled
B_T_h4_alt = (K-1)*(1*m_p + 2*m_n)
print(f"    H4_T: (K−1)·(Σ m_nuc) = {float(B_T_h4_alt):.4f}  vs 8.482 → err {float((B_T_h4_alt-8.482)/8.482*100):+.1f}%")

# Save
witness = {
    "computation": "fresh-jsj-and-inter-skein",
    "description": (
        "(A) JSJ decomposition of proton/neutron branch closures. "
        "(B) Inter-nucleon Skein mass derivations at nucleon level."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q_0": Q0_FLOAT,
    "jsj_results": jsj_results,
    "K_prefactor": float(K),
    "S_pp": float(S_pp),
    "S_pn": float(S_pn),
    "S_nn": float(S_nn),
}
out = Path(__file__).parent / "fresh-jsj-and-inter-skein.witness.json"
out.write_text(json.dumps(witness, indent=2, default=str))
print(f"\n  Witness: {out}")
