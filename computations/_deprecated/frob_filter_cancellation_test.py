#!/usr/bin/env python3
"""FROB-FILTER cancellation-precision-budget test.

Tests the refined hypothesis from
docs/audits/2026-05-02-nv-frob-filter-conjectures.md §FROB-FILTER:
the activation A_** is determined NOT by the smallest A with
q_n > p_n (signature crossover at A=3), but by the smallest A
where summing |Σ_all| in f64 loses too much precision via
catastrophic cancellation.

Method: for each atomic mass A in {1..6}, with parent (Z, N) and
daughter (Z+1, N-1), enumerate all 4^A per-nucleon channel
configurations, compute Σ_all = Σ Δme and Σ_FP (Frobenius-
filtered, both me_par ≥ 0 AND me_dau ≥ 0). Report:

  - Σ_all magnitude vs |Σ_pos| + |Σ_neg| (cancellation depth)
  - Required relative precision = |Σ_all| / max|term|
  - f64 budget = 2^-53 ≈ 1.1e-16
  - Crossover where required precision exceeds f64 budget

Input: 4-channel symbolic data from full-derivation-verified.py
(per-nucleon channels triv, conf, unconf, sign for proton + neutron).
"""
import math
from itertools import product as cartesian
import sympy as sp

# === Reproduce the channel data (from full-derivation-verified.py) ===
VOL_41 = 2.029883212819307
MU_E = 206.7682830
M_E = 0.51099895

hbar_q = math.sqrt(VOL_41 / MU_E)
q0 = 1.0 / (1.0 - hbar_q)

q = sp.Symbol('q', positive=True)

# Channel data per per_nucleon_channels in branching-qvalues.witness.json
# (key: channel name, value: dict of proton/neutron expressions)
ch_data = {
    'triv':   {'p': (q**2 + 1)**2 / (4*q),
               'n': (q**2 + 1)**2 / (4*q**3)},
    'conf':   {'p': (3*q**2 + 1) / (4*q**3),
               'n': -(q**8 - q**6 - 2*q**4 - 5*q**2 - 1) / (4*q**3*(q**2 + 1))},
    'unconf': {'p': -q*(q**2 + 3) / 4,
               'n': -(q**8 + 5*q**6 + 2*q**4 + q**2 - 1) / (4*q**3*(q**2 + 1))},
    'sign':   {'p': -(q**2 + 1)**2 / (4*q**3),
               'n': -(q**2 + 1)**2 / (4*q)},
}
ch_names = list(ch_data.keys())

# Pre-evaluate at q0
ch_num = {ch: {tp: float(ch_data[ch][tp].subs(q, q0)) for tp in ('p', 'n')}
          for ch in ch_names}
print("Per-nucleon channel evaluations at q0 = {:.10f}:".format(q0))
print(f"  {'channel':<8s} {'p (proton)':>15s} {'n (neutron)':>15s}")
for ch in ch_names:
    print(f"  {ch:<8s} {ch_num[ch]['p']:>15.6e} {ch_num[ch]['n']:>15.6e}")
print()

def beta_chain(par, dau):
    """Enumerate all 4^A configs and compute Σ_all + Σ_FP for given
    parent / daughter nucleon strings ('pn...' chars).
    Returns dict with Σ_all, Σ_FP, n_FP, |Σ_pos|, |Σ_neg|, max|term|."""
    A = len(par)
    sigma_all = 0.0
    sigma_fp = 0.0
    sigma_pos = 0.0
    sigma_neg = 0.0
    max_term = 0.0
    n_fp = 0
    n_total = 4 ** A
    for config in cartesian(ch_names, repeat=A):
        me_p = 1.0; me_d = 1.0
        for m in range(A):
            tp = par[m]
            td = dau[m]
            me_p *= ch_num[config[m]][tp]
            me_d *= ch_num[config[m]][td]
        dme = me_d - me_p
        sigma_all += dme
        absdme = abs(dme)
        if absdme > max_term: max_term = absdme
        if dme > 0: sigma_pos += dme
        elif dme < 0: sigma_neg += dme
        if me_p >= 0 and me_d >= 0:
            sigma_fp += dme
            n_fp += 1
    return {
        'A': A,
        'n_total': n_total,
        'n_fp': n_fp,
        'sigma_all': sigma_all,
        'sigma_fp': sigma_fp,
        'sigma_pos': sigma_pos,
        'sigma_neg': sigma_neg,
        'max_term': max_term,
        'cancellation_depth': sigma_pos - sigma_neg,
        'precision_required': abs(sigma_all) / max_term if max_term > 0 else None,
    }


def run_test():
    # β-decay chains: parent (Z neutrons → Z+1 protons after one β-)
    # Schema: par[m] in {'p', 'n'}, dau[m] in {'p', 'n'} where one
    # neutron becomes a proton.
    # For consistent A coverage, use generic (one n -> one p) chains:
    chains = []
    for A in range(1, 7):
        # Simplest: A nucleons, parent = A neutrons, daughter = (A-1) neutrons + 1 proton
        # (corresponds to neutron-rich → less-neutron-rich β decay)
        if A == 1:
            par = 'n'; dau = 'p'
        elif A == 2:
            par = 'nn'; dau = 'pn'   # ²n → d (synthetic)
        elif A == 3:
            par = 'pnn'; dau = 'ppn'  # ³H → ³He (real)
        elif A == 4:
            par = 'ppnn'; dau = 'pppn'  # synthetic A=4 β
        elif A == 5:
            par = 'ppnnn'; dau = 'pppnn'  # synthetic A=5 β
        elif A == 6:
            par = 'ppnnnn'; dau = 'pppnnn'  # ⁶He → ⁶Li (real)
        chains.append((A, par, dau))

    print(f"{'A':>3} {'chain':>16} {'n_total':>9} {'n_FP':>8} "
          f"{'|Σ_all|':>11} {'|Σ_FP|':>11} "
          f"{'pos':>11} {'|neg|':>11} "
          f"{'cancel':>11} {'req prec':>11}")
    print("-" * 130)
    results = []
    for A, par, dau in chains:
        r = beta_chain(par, dau)
        chain_str = f"{par}→{dau}"
        cancel = r['cancellation_depth']  # |Σ_pos - Σ_neg| ~ |Σ_pos| + |Σ_neg|
        req_prec = r['precision_required']
        print(f"{A:>3} {chain_str:>16} {r['n_total']:>9} {r['n_fp']:>8} "
              f"{abs(r['sigma_all']):>11.4e} {abs(r['sigma_fp']):>11.4e} "
              f"{r['sigma_pos']:>11.4e} {abs(r['sigma_neg']):>11.4e} "
              f"{cancel:>11.4e} {req_prec:>11.4e}")
        results.append({**r, 'par': par, 'dau': dau, 'chain': chain_str})

    print()
    print("Refined cancellation-precision-budget hypothesis:")
    print("  required precision = |Σ_all| / max|term|")
    print("  f64 budget = 2^-53 ≈ 1.11e-16")
    print()
    print("Crossover analysis (where required precision exceeds f64):")
    f64_budget = 2.0 ** -53
    crossover_found = False
    for r in results:
        rp = r['precision_required']
        ratio = (rp / f64_budget) if rp is not None else None
        if rp is not None and rp < 100 * f64_budget:
            print(f"  A={r['A']}: required precision {rp:.3e} ~ {ratio:.2e} × f64_budget — DANGER ZONE")
            if not crossover_found:
                print(f"          ↑ first A within 2 orders of f64 budget — likely A_**")
                crossover_found = True
        else:
            print(f"  A={r['A']}: required precision {rp:.3e} — safe at f64")

    print()
    print("Σ_all vs Σ_FP magnitude:")
    print(f"  {'A':>3} {'|Σ_all|/|max|':>14} {'|Σ_FP|/|max|':>14} {'FP gives speedup':>18}")
    for r in results:
        all_norm = abs(r['sigma_all']) / r['max_term']
        fp_norm = abs(r['sigma_fp']) / r['max_term']
        gain = (all_norm / fp_norm) if fp_norm > 0 else float('inf')
        print(f"  {r['A']:>3} {all_norm:>14.3e} {fp_norm:>14.3e} {gain:>18.2e}")

    return results


if __name__ == "__main__":
    run_test()
