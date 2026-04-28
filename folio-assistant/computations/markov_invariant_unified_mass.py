#!/usr/bin/env python3
"""
30a: Markov-invariant unified mass formula assembly.

Refactor the 6-term mass formula to use ONLY Markov-invariant
ingredients (no per-generator-volume proxies):

  M(β) = Z·m_p + N·m_n + Z·m_e − α_M · log|tr_M_canonical(β)|
                              − α_F · Σ_λ 1/dim_q(V_λ) · m_e
                              − α_T7 · m_e · 8G · B_shadow(β)

where:
  - tr_M_canonical(β) from pyhecke (already Markov-invariant)
  - Σ_λ 1/dim_q(V_λ) = Frobenius co-Casimir at H_{3A} (universal)
  - B_shadow(β) = Plancherel-weighted shadow-price sum (Term 7)
  - α_M, α_F, α_T7 are STRUCTURAL prefactors (per term, NOT per isotope)

Calibration:
  α_M  from D binding (single nucleus, single number)
  α_F  from T binding
  α_T7 from ³He binding (or fix to m_e·8G universal per Term 7 prop)

Then PREDICT ⁴He binding without further fitting.  If close, the
framework is universal at single-prefactor level.  ⁶Li, ⁷Li extend
the same structure (need pyhecke at H_18, H_21 — next step).

30b (built into this script): for each isotope, quantify the gap
between Markov-invariant prediction and AME, vs the gap with the
existing non-Markov-invariant 6-term.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
m_p = mp.mpf("938.27208816")
m_n = mp.mpf("939.56542052")
G = mp.catalan


def qint(n): return (Q0**n - QI**n)/(Q0 - QI)
def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n+1): p *= qint(k)
    return p

def hook_lengths(shape):
    rows = len(shape); out = []
    for i in range(rows):
        for j in range(shape[i]):
            arm = shape[i] - j - 1
            leg = sum(1 for r in range(i+1, rows) if shape[r] > j)
            out.append(arm + leg + 1)
    return out

def dim_q_partition(shape, n):
    h_prod = mp.mpf(1)
    for hk in hook_lengths(shape): h_prod *= qint(hk)
    return qfac(n) / h_prod

def partitions_of(n):
    if n == 0:
        yield (); return
    def gen(rem, mxp):
        if rem == 0: yield (); return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem-p, p):
                yield (p,) + rest
    yield from gen(n, n)

def Sigma_n(n, height_cap=8):
    """Σ_n = Σ_λ 1/dim_q(V_λ) — Frobenius co-Casimir at H_n (height-capped)."""
    total = mp.mpf(0)
    for shape in partitions_of(n):
        if len(shape) > height_cap: continue
        d = dim_q_partition(shape, n)
        if abs(d) > mp.mpf("1e-30"):
            total += 1/d
    return total


# Canonical Markov traces from pyhecke (already on branch)
canon = json.load(open(Path(__file__).parent / "canonical-isospin-pyhecke.witness.json"))
canon_results = canon["results"]

# Map isotope label to canon key
def get_canon_tr(iso):
    sup = {"3He": "³He", "4He": "⁴He", "6Li": "⁶Li", "7Li": "⁷Li"}
    target = sup.get(iso, iso)
    for k in canon_results:
        if k.startswith(target + " ") or k == target:
            return mp.mpf(str(canon_results[k]["tr_M_q0"]))
    return None


# Term 7 shadow-price (already on branch)
try:
    t7 = json.load(open(Path(__file__).parent / "paper-six-term-shadow-price-sweep.witness.json"))
    t7_results = t7["results"]
except Exception:
    t7_results = {}

def get_B_shadow(iso):
    sup = {"3He": "³He", "4He": "⁴He"}
    target = sup.get(iso, iso)
    for k in t7_results:
        if k.startswith(target + " ") or k == target:
            return mp.mpf(str(t7_results[k]["B_shadow"]))
    return mp.mpf(0)


# AME 2020 reference
AME = {
    "p":   ( 1, 0,   938.78308711,    0.0),
    "n":   ( 0, 1,   939.56542052,    0.0),
    "D":   ( 1, 1,  1876.12393,       2.22456612),
    "T":   ( 1, 2,  2809.43215,       8.481798),
    "3He": ( 2, 1,  2809.41347,       7.718058),
    "4He": ( 2, 2,  3728.40133,      28.29566),
}


print("=" * 110)
print("30a: Markov-invariant unified mass formula")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f}")
print(f"  m_e = {float(m_e):.6f} MeV,  m_p = {float(m_p):.6f},  m_n = {float(m_n):.6f}")
print()

# Compute structural ingredients per isotope
print(f"  {'iso':<5} {'A':>3} {'tr_M':>12} {'log|tr_M|':>12} {'Σ_n co-Cas':>12} {'B_shadow':>12}")
print("-" * 80)
isotope_data = {}
for iso in ["p", "n", "D", "T", "3He", "4He"]:
    Z, N, M_AME, B_AME = AME[iso]
    A = Z + N
    n = 3 * A
    tr_M = get_canon_tr(iso)
    log_tr = mp.log(abs(tr_M)) if tr_M is not None and tr_M != 0 else None
    Sn = Sigma_n(n)
    Bsh = get_B_shadow(iso)
    isotope_data[iso] = {
        "Z": Z, "N": N, "A": A, "n": n,
        "tr_M": tr_M, "log_tr_M": log_tr,
        "Sigma_n": Sn, "B_shadow": Bsh,
        "M_AME": M_AME, "B_AME": B_AME
    }
    print(f"  {iso:<5} {A:>3} {float(tr_M):>+12.6f} {float(log_tr):>+12.6f} {float(Sn):>12.6f} {float(Bsh):>12.6f}")
print()

# ── Markov-invariant unified mass formula ──────────────────────────
# M_pred = Z·m_p + N·m_n + Z·m_e − binding
# binding = α_M · log|tr_M| + α_F · m_e · Σ_n + α_T7 · m_e·8G · B_shadow
#
# Universal α_T7 = 1 (per Term 7 prop: α = m_e·8G in front, no extra factor).
# Calibrate (α_M, α_F) from {D, T} bindings.
# Predict ³He, ⁴He.

m_e_8G = m_e * 8 * G  # ≈ 3.745 MeV

# Set up linear system from D, T:
#   B(D) = α_M · log|tr_M(D)| + α_F · m_e · Σ_6(D) + 1 · m_e_8G · B_shadow(D)
#   B(T) = α_M · log|tr_M(T)| + α_F · m_e · Σ_9(T) + 1 · m_e_8G · B_shadow(T)
B_D_AME = mp.mpf(str(AME["D"][3]))
B_T_AME = mp.mpf(str(AME["T"][3]))
log_trM_D = isotope_data["D"]["log_tr_M"]
log_trM_T = isotope_data["T"]["log_tr_M"]
S6 = isotope_data["D"]["Sigma_n"]
S9 = isotope_data["T"]["Sigma_n"]
Bsh_D = isotope_data["D"]["B_shadow"]
Bsh_T = isotope_data["T"]["B_shadow"]

# B = α_M · log_tr + α_F · m_e · Σ_n + m_e_8G · Bsh
# residual = B - m_e_8G · Bsh  =  α_M·log_tr + α_F · m_e · Σ_n
res_D = B_D_AME - m_e_8G * Bsh_D
res_T = B_T_AME - m_e_8G * Bsh_T

# Solve linear system  (log_tr_D, m_e·S6) (α_M)    (res_D)
#                       (log_tr_T, m_e·S9) (α_F) = (res_T)
A11 = log_trM_D; A12 = m_e * S6
A21 = log_trM_T; A22 = m_e * S9
det_A = A11 * A22 - A12 * A21
alpha_M = (res_D * A22 - res_T * A12) / det_A
alpha_F = (A11 * res_T - A21 * res_D) / det_A

print(f"  Calibrated structural prefactors (from D, T binding):")
print(f"    α_M (Markov coefficient)         = {float(alpha_M):.6f} MeV")
print(f"    α_F (Frobenius co-Casimir coeff) = {float(alpha_F):.6f}  (dimensionless × m_e)")
print(f"    α_T7 (Term 7 universal)           = 1.0  (= m_e·8G implicit prefactor)")
print()

# ── Predict ³He, ⁴He ──────────────────────────────────────────────
print("=" * 110)
print(f"  {'iso':<5} {'A':>3} {'B_AME':>10} {'α_M·log|tr|':>14} {'α_F·m_e·Σ_n':>14} {'m_e·8G·B_sh':>14} {'B_pred':>12} {'err %':>9}")
print("-" * 110)
results = []
for iso in ["D", "T", "3He", "4He"]:
    d = isotope_data[iso]
    M_term = alpha_M * d["log_tr_M"]
    F_term = alpha_F * m_e * d["Sigma_n"]
    T7_term = m_e_8G * d["B_shadow"]
    B_pred = M_term + F_term + T7_term
    B_AME = mp.mpf(str(d["B_AME"]))
    err = (B_pred - B_AME) / B_AME * 100 if B_AME != 0 else mp.mpf(0)
    M_pred = d["Z"] * m_p + d["N"] * m_n + d["Z"] * m_e - B_pred
    M_AME = mp.mpf(str(d["M_AME"]))
    err_M = (M_pred - M_AME)/M_AME * 100
    is_calib = "(calibration anchor)" if iso in ("D", "T") else ""
    print(f"  {iso:<5} {d['A']:>3} {float(B_AME):>10.4f} {float(M_term):>+14.6f} {float(F_term):>+14.6f} {float(T7_term):>+14.6f} {float(B_pred):>+12.6f} {float(err):>+9.4f}% {is_calib}")
    results.append({
        "iso": iso, "A": d["A"], "Z": d["Z"], "N": d["N"],
        "M_AME_MeV": float(M_AME), "B_AME_MeV": float(B_AME),
        "M_term": float(M_term), "F_term": float(F_term), "T7_term": float(T7_term),
        "B_pred_MeV": float(B_pred), "M_pred_MeV": float(M_pred),
        "err_B_pct": float(err), "err_M_pct": float(err_M),
        "is_calibration": iso in ("D", "T")
    })

print()
print("=" * 110)
print("OBSERVATIONS / 30b GAP ANALYSIS")
print("=" * 110)
print("""
Markov-invariant unified formula (3 structural prefactors):
  α_M, α_F calibrated from {D, T} bindings.
  α_T7 = 1 (universal per Term 7 prop).

  iso   B_AME   B_pred (Markov-inv)   err
  D     2.225   (calibrated)         0%
  T     8.482   (calibrated)         0%
  ³He   7.718   PREDICTION           ?
  ⁴He  28.30   PREDICTION            ?

The PREDICTION rows show whether the Markov-invariant unified
formula generalises with a single set of structural prefactors, or
whether per-isotope refinement is still needed.

Compared to existing non-Markov-invariant 6-term:
  (per paper-six-term-isotope-sweep.witness.json)
  D: -21.05%   T: -25.68%   ³He: +0.58%   ⁴He: -4.42%

The Markov-invariant formula's prediction precision on ³He, ⁴He
indicates whether the 'iterative tower' principle works in practice.
""")

out = {
    "computation": "markov-invariant-unified-mass",
    "description": ("30a: Markov-invariant unified mass formula assembly. "
                    "Replaces non-Markov-invariant proxies in the 6-term "
                    "with pyhecke canonical Markov trace, Frobenius co-Casimir "
                    "Σ_n, and universal Term 7 (m_e·8G·B_shadow).  Calibrates "
                    "α_M, α_F from {D, T} binding to test universality on "
                    "³He, ⁴He.  Built into the same script: 30b gap analysis "
                    "between Markov-invariant predictions and AME."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "structural_prefactors": {
        "alpha_M_MeV": float(alpha_M),
        "alpha_F": float(alpha_F),
        "alpha_T7_universal": 1.0,
        "m_e_8G_MeV": float(m_e_8G)
    },
    "isotopes": results
}
out_path = Path(__file__).parent / "markov-invariant-unified-mass.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
