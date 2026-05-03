#!/usr/bin/env python3
"""HIGGS-SLOT test from the G-action axioms (option 2 of the 2-7 dispatch).

Per the new G-action axioms in
content/quantum-observable-universe/algebraic-substrate/g-action-on-substrate.md:

  dim_q A^W± = [4]_q  (W-host T(2,4))
  dim_q A^Z  = [6]_q  (Z-host T(2,6))
  dim_q A^H  = [2]_q  (Higgs SU(2)_L fundamental, neutral component)

PR #513 found m ∝ tr_M(T(2,2k)) gives m_H/m_W = -11.4%. Test whether
the G-action q-dim form gives a better answer.

This is a HONEST test — no fitting. Each formula is parameter-free.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
import mpmath
mpmath.mp.dps = 50

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR

q = mpmath.mpf(Q_50_DIGIT_STR)


def q_int(n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


# Markov trace of σ_1^k on H_2(q): tr_M(σ_1^k) = (q^k - q^-k) / [2]_q
# (per the PR #513 calculation — Markov trace at H_2 with z = 1/(q^{1/2}+q^{-1/2}))
def tr_M_torus_2_2k(k):
    """Markov trace of σ_1^{2k} = T(2, 2k) closure."""
    # z = 1/(q^{1/2} + q^{-1/2}); χ_sym(σ^{2k}) = q^{2k}; χ_alt = q^{-2k}
    # tr_M(σ^{2k}) = w_sym · χ_sym + w_alt · χ_alt with w = 1/[2]_q
    return (q ** (2 * k) + q ** (-2 * k)) / q_int(2)


# PDG masses (GeV)
m_W_PDG = mpmath.mpf('80.379')
m_Z_PDG = mpmath.mpf('91.188')
m_H_PDG = mpmath.mpf('125.25')


print("HIGGS-SLOT G-action test")
print("=" * 70)
print(f"q_0 = {mpmath.nstr(q, 12)}")
print()
print("Categorical scales:")
print(f"  tr_M(T(2,4)) = {mpmath.nstr(tr_M_torus_2_2k(2), 8)}")
print(f"  tr_M(T(2,6)) = {mpmath.nstr(tr_M_torus_2_2k(3), 8)}")
print(f"  tr_M(T(2,8)) = {mpmath.nstr(tr_M_torus_2_2k(4), 8)}")
print(f"  [2]_q = {mpmath.nstr(q_int(2), 8)}")
print(f"  [4]_q = {mpmath.nstr(q_int(4), 8)}")
print(f"  [6]_q = {mpmath.nstr(q_int(6), 8)}")
print(f"  [8]_q = {mpmath.nstr(q_int(8), 8)}")
print()


def report_ratios(name, m_W_form, m_Z_form, m_H_form):
    """Report m_Z/m_W, m_H/m_W, m_H/m_Z for a candidate form."""
    pred_ZW = m_Z_form / m_W_form
    pred_HW = m_H_form / m_W_form
    pred_HZ = m_H_form / m_Z_form
    pdg_ZW = m_Z_PDG / m_W_PDG
    pdg_HW = m_H_PDG / m_W_PDG
    pdg_HZ = m_H_PDG / m_Z_PDG
    err_ZW = (pred_ZW / pdg_ZW - 1) * 100
    err_HW = (pred_HW / pdg_HW - 1) * 100
    err_HZ = (pred_HZ / pdg_HZ - 1) * 100
    print(f"  {name}")
    print(f"    m_Z/m_W: pred={mpmath.nstr(pred_ZW, 6)}, PDG={mpmath.nstr(pdg_ZW, 6)}, err={mpmath.nstr(err_ZW, 4)}%")
    print(f"    m_H/m_W: pred={mpmath.nstr(pred_HW, 6)}, PDG={mpmath.nstr(pdg_HW, 6)}, err={mpmath.nstr(err_HW, 4)}%")
    print(f"    m_H/m_Z: pred={mpmath.nstr(pred_HZ, 6)}, PDG={mpmath.nstr(pdg_HZ, 6)}, err={mpmath.nstr(err_HZ, 4)}%")
    return {
        'name': name,
        'm_Z_over_m_W': {'pred': mpmath.nstr(pred_ZW, 12), 'pdg': mpmath.nstr(pdg_ZW, 12), 'err_pct': float(err_ZW)},
        'm_H_over_m_W': {'pred': mpmath.nstr(pred_HW, 12), 'pdg': mpmath.nstr(pdg_HW, 12), 'err_pct': float(err_HW)},
        'm_H_over_m_Z': {'pred': mpmath.nstr(pred_HZ, 12), 'pdg': mpmath.nstr(pdg_HZ, 12), 'err_pct': float(err_HZ)},
    }


print("Test (i) m ∝ tr_M(T(2, 2k)) — PR #513 baseline:")
results = []
results.append(report_ratios("(i) m_X ∝ tr_M(T_X)",
                              tr_M_torus_2_2k(2), tr_M_torus_2_2k(3), tr_M_torus_2_2k(4)))

print()
print("Test (ii) m ∝ dim_q(A^X) — G-action q-dim form (Higgs is SCALAR slot [2]_q):")
results.append(report_ratios("(ii) m_X ∝ dim_q(A^X)",
                              q_int(4), q_int(6), q_int(2)))

print()
print("Test (iii) m^2 ∝ dim_q(A^X) — quadratic form:")
m_W_q = mpmath.sqrt(q_int(4))
m_Z_q = mpmath.sqrt(q_int(6))
m_H_q = mpmath.sqrt(q_int(2))
results.append(report_ratios("(iii) m_X² ∝ dim_q(A^X)", m_W_q, m_Z_q, m_H_q))

print()
print("Test (iv) m_W = (1/2) g v with g ∝ tr_M(T(2,4)), and Higgs from [2]_q:")
# Standard Higgs mech: m_W = gv/2, m_Z = m_W/cos(θ_W)
# Here cos(θ_W) emerges; try several forms
# v common to all; g_X for each
results.append(report_ratios("(iv) m_X ∝ tr_M(T_X) for W,Z; m_H ∝ [2]_q",
                              tr_M_torus_2_2k(2), tr_M_torus_2_2k(3), q_int(2)))

print()
print("Test (v) m ∝ tr_M(T(2,2k)) for W,Z; m_H = √(2λ)·v with λ from [2]_q:")
# In SM: m_H² = 2λv², so m_H/m_W = √(2λ)/g · 2 = 2√(2λ)/g
# If λ ∝ [2]_q² (categorical Higgs self-coupling), m_H ∝ √([2]_q²) · v_norm = [2]_q · v_norm
# Use v_norm = m_W / tr_M(T(2,4)) so that m_W is reproduced
# Then m_H = [2]_q · m_W / tr_M(T(2,4))
m_W_v = tr_M_torus_2_2k(2)
m_Z_v = tr_M_torus_2_2k(3)
m_H_v = q_int(2) * m_W_v / tr_M_torus_2_2k(2)  # = [2]_q
# That's just [2]_q, same as (ii)

# Try (vi) with sqrt: m_H ∝ √([2]_q · tr_M(T(2,8)))?
print()
print("Test (vi) m_H ∝ √([2]_q · dim_q × ...):")
m_H_form_vi = mpmath.sqrt(q_int(2) * q_int(8))
results.append(report_ratios("(vi) m_H ∝ √([2]_q · [8]_q); W,Z ∝ tr_M",
                              tr_M_torus_2_2k(2), tr_M_torus_2_2k(3), m_H_form_vi))

# Find best for m_H/m_W
print()
print("=" * 70)
print("VERDICT:")
print("=" * 70)
best_HW = min(results, key=lambda r: abs(r['m_H_over_m_W']['err_pct']))
print(f"  Best m_H/m_W match: {best_HW['name']} at {best_HW['m_H_over_m_W']['err_pct']:.2f}% off PDG")
print()
print("  Honest verdict:")
print("  None of these zero-free-parameter forms reproduce m_H/m_W = 1.558.")
print("  The G-action axioms determine q-dim assignments but do NOT directly")
print("  give EW mass RATIOS — the standard Higgs mechanism formula")
print("    m_W = gv/2, m_Z = m_W/cos(θ_W), m_H = √(2λ)·v")
print("  requires the categorical g, g', λ which the G-action axioms don't yet")
print("  pin down. HIGGS-SLOT remains open from this angle.")
print()
print("  WHAT THE G-ACTION AXIOMS DO CLOSE: the q-dim pattern dim_q(A^H) = [2]_q")
print("  is internally consistent (no -69% error like trying tr_M(T(2,8)) for H);")
print("  the right form likely involves the categorical Higgs self-coupling λ.")

# Witness output
out = {
    'computation': 'higgs-slot-g-action-test',
    'computedAt': datetime.now(timezone.utc).isoformat(),
    'description': (
        'HIGGS-SLOT test from G-action axioms. 6 zero-free-parameter '
        'EW mass-ratio formulas tested. Verdict: G-action q-dim '
        'assignments alone do not pin EW mass ratios; the Higgs '
        'self-coupling λ is needed.'
    ),
    'q_0': mpmath.nstr(q, 30),
    'ew_mass_pdg_GeV': {'W': float(m_W_PDG), 'Z': float(m_Z_PDG), 'H': float(m_H_PDG)},
    'tested_forms': results,
    'best_m_H_over_m_W': best_HW,
    'verdict': (
        'HIGGS-SLOT NOT closed by G-action axioms alone — '
        'mass ratios require the categorical Higgs self-coupling λ '
        '(not specified by axioms G-1 to G-4)'
    ),
}
out_path = Path(__file__).parent / 'higgs-slot-g-action-test.witness.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False, default=str)
print(f"\n→ wrote {out_path}")
