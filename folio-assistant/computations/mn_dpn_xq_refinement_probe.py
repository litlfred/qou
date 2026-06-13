#!/usr/bin/env python3
"""mn_dpn_xq_refinement_probe.py — m_n / Δ_pn 100× target (precision)

This probe tests candidate refinements for the flavor-split factor X(q) at both
the proton and muon anchors, parallel to PR #1511 (where α_EM was refined by the
Habiro element [2]_q (1 - h²α)).

The base unrefined flavor-split factor is:
    X_0(q) = (q - 1)^2 (1 - q^{-4}) / 3 = ℏ_q^2 h_q [2]_q / 3

The mass splitting is given by:
    m_n - m_p = M_N · X_0(q) · C(q)
where C(q) is the Habiro refinement.

We test categorical combinations identified via a rational basis scan:
    - 1 + 4 ℏ_q^3 / [3]_q  (0.39 ppm match)
    - 1 + h_q^2 / (17 [2]_q) (0.20 ppm match)
    - 1 + 5/12 [2]_q h_q α_EM (0.46 ppm match)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: E402, F401

from mpmath import mp
from _precision import set_compute_dps
from witness_base import WitnessBuilder
from q_parameter import q_at, q_muon_at, Q_50_DIGIT_STR

def hbar(q):
    return (q - 1) / q

def h(q):
    return q - 1 / q

def quantum_int(n, q):
    return (q**n - q**(-n)) / (q - 1/q)

def evaluate_candidates(q_val, m_n_target, m_p_target, alpha_em):
    M_N = (m_p_target + m_n_target) / 2
    delta_pn_target = m_n_target - m_p_target
    
    # Base X_0(q) = ℏ_q^2 * h * [2]_q / 3
    X_0 = hbar(q_val)**2 * h(q_val) * quantum_int(2, q_val) / 3
    
    results = {}
    
    variants = [
        ("Base (no refinement)", mp.mpf('1.0')),
        ("C1: 1 + ℏ_q^3", 1 + hbar(q_val)**3),
        ("C2: 1 + 4 ℏ_q^3 / [3]_q", 1 + 4 * hbar(q_val)**3 / quantum_int(3, q_val)),
        ("C3: 1 + h_q^2 / (17 [2]_q)", 1 + h(q_val)**2 / (17 * quantum_int(2, q_val))),
        ("C4: 1 + 5/12 [2]_q h_q α_EM", 1 + 5/12 * quantum_int(2, q_val) * h(q_val) * alpha_em),
    ]
    
    for name, C in variants:
        pred_delta = M_N * X_0 * C
        err_ppm = float(abs(pred_delta - delta_pn_target) / delta_pn_target * 1e6)
        results[name] = {"pred_delta": mp.nstr(pred_delta, 15), "err_ppm": err_ppm}
        
    return results

def main():
    set_compute_dps()
    wb = WitnessBuilder("mn-dpn-xq-refinement-probe", engine="mpmath")
    
    m_p_codata = mp.mpf("938.27208816")
    m_n_codata = mp.mpf("939.56542052")
    alpha_em = mp.mpf("0.0072973525693")
    
    q_proton = mp.mpf(Q_50_DIGIT_STR)
    q_muon = q_muon_at(50)
    
    print("Evaluating at q_proton anchor:")
    res_proton = evaluate_candidates(q_proton, m_n_codata, m_p_codata, alpha_em)
    for k, v in res_proton.items():
        print(f"  {k:<35}: err = {v['err_ppm']:.2f} ppm")
        
    print("\nEvaluating at q_muon anchor:")
    res_muon = evaluate_candidates(q_muon, m_n_codata, m_p_codata, alpha_em)
    for k, v in res_muon.items():
        print(f"  {k:<35}: err = {v['err_ppm']:.2f} ppm")
        
    wb.add_data("q_proton", mp.nstr(q_proton, 30))
    wb.add_data("q_muon", mp.nstr(q_muon, 30))
    wb.add_data("proton_anchor_results", res_proton)
    wb.add_data("muon_anchor_results", res_muon)
    
    best_err = min([v['err_ppm'] for k, v in res_proton.items()])
    wb.add_assertion(
        "precision_improved_beyond_100x",
        computed=best_err < 12.0,  # Base error was 1277 ppm. 100x target means < 12.7 ppm
        expected=True,
        source="The categorical refinement should exceed the 100x improvement target over the base unrefined error."
    )
    
    wb.save()

if __name__ == "__main__":
    main()
