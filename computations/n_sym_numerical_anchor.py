#!/usr/bin/env python3
"""N_sym numerical anchor — pin the value of the symmetric-channel
Plancherel normalization at q_0, test ansatze, run PSLQ.

Per `n-sym-symmetric-channel-normalization`, the closed-form
expression for N_v factors as

  N_v = (∏_{k=2,3,4} [2k]_q² / [2]_q) · N_sym(q)

with N_sym(q_0) ≈ 213.11 fixed by CODATA G_F.

This script:
  1. Computes N_sym(q_0) at 200 dps
  2. Tests 25+ q-arithmetic ansatze; ranks by relative error
  3. Runs PSLQ on log(N_sym) over the standard basis
  4. Computes a candidate Gram-determinant value (candidate (a))
     for comparison
  5. Emits witness JSON

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
from datetime import datetime, timezone
from pathlib import Path
import time
import sys as _sys
import mpmath
mpmath.mp.dps = 200

# Centralized constants (per Gemini review on PR #515).
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, G_F_MEV

# Ref: [leitner2026] conj:g-action-on-substrate (the anchor and why it is not a host trace)

q = mpmath.mpf(Q_50_DIGIT_STR)


def q_int(n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def q_factorial(n):
    p = mpmath.mpf(1)
    for k in range(1, n + 1):
        p *= q_int(k)
    return p


# CODATA-derived N_v (from centralized experimental_constants)
G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))
v_weak = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
E_cross = (q - 1 / q) / 2
mu_0 = m_e / (3 * E_cross)
N_v = v_weak / (E_cross * mu_0)

# Conjectured product factor
prod_pl = (q_int(4) ** 2 / q_int(2)) * (q_int(6) ** 2 / q_int(2)) * (q_int(8) ** 2 / q_int(2))
N_sym_target = N_v / prod_pl


def main():
    print("N_sym numerical anchor (200 dps)")
    print("=" * 70)
    print(f"q_0    = {mpmath.nstr(q, 30)}")
    print(f"N_v    = {mpmath.nstr(N_v, 25)}")
    print(f"prod   = {mpmath.nstr(prod_pl, 25)}")
    print(f"N_sym  = N_v / prod = {mpmath.nstr(N_sym_target, 25)}")
    print()

    # Ansatz tests
    candidates = {
        "[7]_q · [8]_q · [3]_q":      q_int(7) * q_int(8) * q_int(3),
        "[6]_q² · [7]_q · [8]_q / [10]_q":
                                       q_int(6) ** 2 * q_int(7) * q_int(8) / q_int(10),
        "45 · [5]_q":                 45 * q_int(5),
        "[5]_q!":                     q_factorial(5),
        "[6]_q · [7]_q · 5":          q_int(6) * q_int(7) * 5,
        "[10]_q² / [2]_q² · 8":       q_int(10) ** 2 / q_int(2) ** 2 * 8,
        "[10]_q² · 2":                q_int(10) ** 2 * 2,
        "[5]_q! · 5 / [2]_q":         q_factorial(5) * 5 / q_int(2),
        "[3]_q^4 · [4]_q":            q_int(3) ** 4 * q_int(4),
        "5! · [3]_q":                 120 * q_int(3),
        "6! · [3]_q / 5":             720 * q_int(3) / 5,
        "[6]_q!":                     q_factorial(6),
        "32 · [7]_q · [3]_q²":        32 * q_int(7) * q_int(3) ** 2,
        "12 · [5]_q · [7]_q² / [3]_q":
                                       12 * q_int(5) * q_int(7) ** 2 / q_int(3),
        "[10]_q · [9]_q²":            q_int(10) * q_int(9) ** 2,
        "[3]_q!":                     q_factorial(3),
        "3 · [5]_q · [7]_q · [3]_q":  3 * q_int(5) * q_int(7) * q_int(3),
        "[2]_q · [3]_q · [4]_q · [5]_q · [6]_q":
                                       q_int(2)*q_int(3)*q_int(4)*q_int(5)*q_int(6),
        # Catalan-numbers-weighted forms (parallels [3]_q^4 in 1/α):
        "C_3 · [5]_q · [4]_q":        5 * q_int(5) * q_int(4),  # C_3 = 5
        "C_4 · [6]_q · [5]_q":        14 * q_int(6) * q_int(5),  # C_4 = 14
        # Exterior-square Plancherel forms (parallels 45 in 1/α):
        "binom(10,2) · [5]_q":        45 * q_int(5),
        "binom(8,2) · [6]_q":         28 * q_int(6),
        # Direct "leading" forms:
        "[8]_q · [7]_q · 3":          q_int(8) * q_int(7) * 3,
        "[8]_q · [7]_q · [3]_q":      q_int(8) * q_int(7) * q_int(3),  # same as best?
        "[9]_q · [10]_q · 2":         q_int(9) * q_int(10) * 2,
    }
    ranked = sorted(
        candidates.items(),
        key=lambda kv: abs(kv[1] - N_sym_target) / N_sym_target,
    )
    print(f"{'ansatz':<42} {'value':>14} {'rel err %':>14}")
    print('-' * 75)
    rows = []
    for name, val in ranked:
        rel_err = abs(val - N_sym_target) / N_sym_target
        flag = ' *** clean' if abs(rel_err) < 1e-3 else (' * close' if abs(rel_err) < 0.05 else '')
        print(f"  {name:<40} {mpmath.nstr(val, 8):>14} {mpmath.nstr(rel_err*100, 6):>13}%{flag}")
        rows.append({
            'ansatz': name,
            'value_at_q0': mpmath.nstr(val, 30),
            'rel_err_pct': mpmath.nstr(rel_err * 100, 25),
        })

    # PSLQ search on log(N_sym)
    print()
    print("PSLQ on log(N_sym) over q-arithmetic + small primes basis:")
    basis = [
        ('log(N_sym)', mpmath.log(N_sym_target)),
        ('log(q)',     mpmath.log(q)),
    ]
    for k in range(2, 11):
        basis.append((f'log[{k}]_q', mpmath.log(q_int(k))))
    for p in (2, 3, 5, 7):
        basis.append((f'log({p})', mpmath.log(p)))

    names = [n for n, _ in basis]
    vec = [v for _, v in basis]
    pslq_results = []
    for tol_str, mc in [('1e-100', 10**6), ('1e-50', 10**8),
                         ('1e-12', 10**10), ('1e-7', 10**12)]:
        t0 = time.time()
        rel = mpmath.pslq(vec, tol=mpmath.mpf(tol_str), maxcoeff=mc)
        elapsed = time.time() - t0
        if rel is None:
            print(f"  tol={tol_str:>8} maxc={mc:>14}: no relation ({elapsed:.2f}s)")
            pslq_results.append({'tol': tol_str, 'maxcoeff': mc, 'relation': None})
        else:
            has_n_sym = rel[0] != 0
            terms = {n: int(r) for n, r in zip(names, rel) if r != 0}
            check = sum(r * v for r, v in zip(rel, vec))
            print(f"  tol={tol_str:>8}: relation found, has_N_sym={has_n_sym}: {terms}  "
                  f"(residual {mpmath.nstr(check, 4)})")
            pslq_results.append({
                'tol': tol_str, 'maxcoeff': mc,
                'relation': terms,
                'has_log_N_sym_coeff': has_n_sym,
                'residual_str': mpmath.nstr(check, 8),
            })

    # Candidate (a) — Gram determinant of the EW Wedderburn block
    # The EW block has 3 hosts, each contributing a 2-dim H_2 with
    # symmetric/alternating split. The naive Gram det of this 6-dim
    # symmetric-block bilinear form: g_{ii} = q^{2k_i} (sym eig²) + q^{-2k_i} (alt eig²)
    # for k_i ∈ {2, 3, 4}. Det = ∏ (q^{2k}+q^{-2k}) · (cross terms 0 for orthogonal hosts)
    print()
    print("Candidate (a) — naive Gram determinant of the EW symmetric-block:")
    gram_det_naive = mpmath.mpf(1)
    for k in (2, 3, 4):
        # symmetric block contributes q^{2k}, alt contributes q^{-2k}
        # Gram diagonal element ~ q^{2k} · q^{-2k} = 1 — too symmetric
        # Try ∏ (q^{4k} - q^{-4k})/(q²-q^-²) = ∏ [2k]_q
        gram_det_naive *= q_int(2 * k)
    print(f"  ∏ [2k]_q (k=2,3,4) = [4]_q · [6]_q · [8]_q = {mpmath.nstr(gram_det_naive, 12)}")
    rel_a = abs(gram_det_naive - N_sym_target) / N_sym_target
    print(f"  rel err vs N_sym = {mpmath.nstr(rel_a*100, 5)}%")

    # write witness
    out = {
        'computation': 'n-sym-numerical-anchor',
        'computedAt': datetime.now(timezone.utc).isoformat(),
        'description': (
            'Numerical anchor for conj:n-sym-symmetric-channel-normalization. '
            'Computes N_sym(q_0) = N_v / ∏_{k=2,3,4} [2k]_q²/[2]_q ≈ 213.11 '
            'and tests 25+ q-arithmetic ansatze plus PSLQ. No clean closed '
            'form found; candidate (a) Gram determinant naive = [4]_q[6]_q[8]_q '
            'evaluated for comparison.'
        ),
        'q_0_dps': mpmath.mp.dps,
        'q_0': mpmath.nstr(q, 50),
        'N_v': mpmath.nstr(N_v, 25),
        'prod_factor': mpmath.nstr(prod_pl, 25),
        'N_sym_target': mpmath.nstr(N_sym_target, 25),
        'ansatz_tests': rows,
        'pslq_runs': pslq_results,
        'candidate_a_gram_det_naive': mpmath.nstr(gram_det_naive, 25),
        'candidate_a_rel_err_pct': mpmath.nstr(rel_a * 100, 25),
        'closes_audit_flag_partially': 'NV-1 (closure path identified)',
        'next_step': (
            'Discharge candidate (a) Gram determinant by computing the '
            'EW Wedderburn-block Gram matrix categorically, OR discharge '
            'candidate (b) Higgs-eaten Goldstone phase space via U2/U4 '
            'conjectures from PR #511.'
        ),
    }
    out_path = WitnessBuilder.wrap_legacy("n-sym-numerical-anchor", out, script_path=__file__, engine="python").save()
    print(f"\n→ wrote {out_path}")


if __name__ == '__main__':
    main()
