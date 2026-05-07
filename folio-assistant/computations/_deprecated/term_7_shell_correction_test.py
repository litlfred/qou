#!/usr/bin/env python3
"""
TERM 7 SHELL CORRECTION TEST against Coulomb-corrected nuclear binding.

Per conj:shell-correction-term-seven, the proposed Term 7 has the form

    Term_7 = m_e · Σ_{λ ⊢ 3A,  height(λ) = 6}  H_q(λ) · w(Z, N, λ)

where the sum runs over height-6 partitions of 3A (with self-conjugate
restriction λ = λ' optionally applied per task spec).  H_q(λ) is the
q-hook product (related to dim_q via [n]_q!/H_q(λ) = dim_q(λ)).  We
combine Term 7 with the atomic Frobenius co-Casimir baseline

    B_pred = m_e · Σ_{λ ⊢ 3A} 1/dim_q(λ)  +  Term_7

and compare to the *Coulomb-corrected* nuclear binding values
B_nucl from `coulomb-subtracted-binding.witness.json`.

Question to answer: does any candidate occupancy w(Z, N, λ) close
the A ≥ 3 binding gap?  In particular, can ⁴He (gap ≈ 27 MeV after
the chirality-residue framework gives ~1.15 MeV) be accommodated
by 3 height-6 self-conjugate partitions of 3A=12?

Witness: term-7-shell-correction-test.witness.json
"""
from __future__ import annotations
import sys
import json
import warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from hecke_characters import partitions_of, dim_q, young_hooks
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
me = mp.mpf(str(M_E_MEV))


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for k in range(2, n + 1):
        out *= q_int(k)
    return out


def hook_product_q(lam):
    """H_q(λ) = Π_{x∈λ} [h_x]_q, the q-hook product."""
    out = mp.mpf(1)
    for h in young_hooks(lam):
        out *= q_int(int(h))
    return out


def dim_q_lam(lam):
    return q_fact(sum(lam)) / hook_product_q(lam)


def conjugate_partition(lam):
    """λ' = (#{i: λ_i ≥ j})_j."""
    if not lam:
        return ()
    max_part = lam[0]
    return tuple(sum(1 for li in lam if li >= j + 1) for j in range(max_part))


def height(lam):
    return len(lam)


def width(lam):
    return lam[0] if lam else 0


def height6_self_conjugate_partitions_of(n):
    """Self-conjugate partitions of n with exactly height 6 (and width 6)."""
    out = []
    for lam in partitions_of(n):
        if height(lam) != 6:
            continue
        if width(lam) != 6:
            continue
        if conjugate_partition(lam) != lam:
            continue
        out.append(lam)
    return out


def height6_partitions_of(n):
    """All partitions of n with exactly height 6 (no self-conjugate filter)."""
    return [lam for lam in partitions_of(n) if height(lam) == 6]


def frobenius_codim_atom(n_strands):
    """Σ_{λ⊢n} 1/dim_q(λ) — atomic Frobenius co-Casimir baseline."""
    return sum(mp.mpf(1) / dim_q_lam(tuple(lam))
               for lam in partitions_of(n_strands))


# ──────────────────────────────────────────────────────────────
# Occupancy formulas to try
# ──────────────────────────────────────────────────────────────

def occ_unit(Z, N, A, lam):
    return 1.0


def occ_min_zn_per_a(Z, N, A, lam):
    # (Z+N)/A · min(Z,N) = min(Z,N)
    return float(min(Z, N))


def occ_zn_over_a2(Z, N, A, lam):
    return (Z * N) / (A * A) if A > 0 else 0.0


def occ_pp_nn_over_a(Z, N, A, lam):
    n_pp = Z * (Z - 1) // 2
    n_nn = N * (N - 1) // 2
    return (n_pp + n_nn) / A if A > 0 else 0.0


OCCUPANCY = {
    "w=1":           occ_unit,
    "min(Z,N)":      occ_min_zn_per_a,
    "(Z·N)/A²":      occ_zn_over_a2,
    "(n_pp+n_nn)/A": occ_pp_nn_over_a,
}


# ──────────────────────────────────────────────────────────────
# Term-7 evaluator
# ──────────────────────────────────────────────────────────────

def term7_value(Z, N, lams_set, occ_fn):
    """Term_7 = m_e · Σ_{λ in lams_set} H_q(λ) · w(Z, N, A, λ)."""
    A = Z + N
    if A < 1 or not lams_set:
        return mp.mpf(0)
    total = mp.mpf(0)
    for lam in lams_set:
        H_q = hook_product_q(lam)
        w_zn = mp.mpf(str(occ_fn(Z, N, A, lam)))
        total += H_q * w_zn
    return me * total


# ──────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────

def load_b_nucl():
    p = Path(__file__).parent / "coulomb-subtracted-binding.witness.json"
    data = json.loads(p.read_text())
    out = {}
    for entry in data['isotopes']:
        out[entry['iso']] = {
            'Z': entry['Z'], 'N': entry['N'], 'A': entry['A'],
            'B_AME': entry['B_AME_MeV'],
            'B_nucl': entry['B_nucl_MeV'],
            'E_Coul': entry['E_Coul_MeV'],
        }
    return out


def main():
    print("=" * 100)
    print("TERM 7 SHELL CORRECTION TEST — height-6 partitions of 3A")
    print("vs. Coulomb-corrected nuclear binding B_nucl")
    print("=" * 100)
    print(f"  q_0      = {Q0_FLOAT}")
    print(f"  m_e      = {float(me)} MeV")
    print()

    b_data = load_b_nucl()

    # Restrict to the requested 6 isotopes
    requested = ["D", "T", "3He", "4He", "6Li", "7Li"]
    isotopes = [(iso, b_data[iso]['Z'], b_data[iso]['N']) for iso in requested]

    # Pre-compute height-6 partitions and the atomic Frobenius co-Casimir
    print("  Height-6 partition inventory at 3A:")
    print(f"  {'A':>3} {'3A':>3} {'#parts':>8} {'#h=6':>6} "
          f"{'#h=6 ∧ self-conj':>18}")
    h6_full = {}
    h6_sc = {}
    fc_codim = {}
    for iso, Z, N in isotopes:
        A = Z + N
        n = 3 * A
        full = list(partitions_of(n))
        h6 = height6_partitions_of(n)
        sc = height6_self_conjugate_partitions_of(n)
        h6_full[A] = h6
        h6_sc[A] = sc
        fc_codim[A] = frobenius_codim_atom(n)
        print(f"  {A:>3} {n:>3} {len(full):>8} {len(h6):>6} {len(sc):>18}")
    print()

    # Show the 4He height-6 self-conjugate partitions explicitly
    print(f"  Explicit 4He (3A=12) height-6 self-conjugate partitions:")
    for lam in h6_sc[4]:
        Hq = float(hook_product_q(lam))
        d = float(dim_q_lam(lam))
        print(f"    {lam}  H_q(λ) = {Hq:.6e}   dim_q(λ) = {d:.6e}   "
              f"m_e·H_q(λ) = {float(me) * Hq:.4e} MeV")
    print()

    # Compute Σ_3A baseline and Term 7 across occupancy choices
    rows = []
    for iso, Z, N in isotopes:
        A = Z + N
        sigma_3A = float(me) * float(fc_codim[A])
        b_nucl = b_data[iso]['B_nucl']
        b_ame = b_data[iso]['B_AME']
        gap_baseline = b_nucl - sigma_3A   # baseline under-binding gap
        rows.append({
            'iso': iso, 'Z': Z, 'N': N, 'A': A,
            'sigma_3A_MeV': sigma_3A,
            'B_nucl_MeV': b_nucl, 'B_AME_MeV': b_ame,
            'gap_after_baseline_MeV': gap_baseline,
            'h6_count': len(h6_full[A]),
            'h6_sc_count': len(h6_sc[A]),
            'h6_sc_partitions': [list(l) for l in h6_sc[A]],
            'term7': {},
        })

    print("  Baseline (atomic Frobenius co-Casimir = m_e · Σ_{λ⊢3A} 1/dim_q):")
    print(f"  {'iso':<6} {'A':>2} {'B_nucl':>10} {'B_AME':>10} "
          f"{'σ_3A':>10} {'gap':>10}")
    for r in rows:
        print(f"  {r['iso']:<6} {r['A']:>2} "
              f"{r['B_nucl_MeV']:>10.3f} {r['B_AME_MeV']:>10.3f} "
              f"{r['sigma_3A_MeV']:>10.3f} {r['gap_after_baseline_MeV']:>10.3f}")
    print()

    # Apply Term 7 — both with and without self-conjugate restriction
    for sc_only_label, lams_for_A in [
            ("self-conjugate height-6 only", h6_sc),
            ("all height-6", h6_full)]:
        print("=" * 100)
        print(f"  Term 7 over {sc_only_label}:")
        print("=" * 100)
        for occ_name, occ_fn in OCCUPANCY.items():
            print(f"\n  Occupancy: w = {occ_name}")
            print(f"  {'iso':<6} {'A':>2} {'σ_3A':>10} {'Term_7':>14} "
                  f"{'B_pred':>10} {'B_nucl':>10} {'err %':>10}")
            for r in rows:
                A = r['A']
                Z = r['Z']; N = r['N']
                lams = lams_for_A[A]
                t7 = float(term7_value(Z, N, lams, occ_fn))
                b_pred = r['sigma_3A_MeV'] + t7
                b_nucl = r['B_nucl_MeV']
                err = (b_pred - b_nucl) / b_nucl * 100 if b_nucl else 0.0
                key = f"{sc_only_label}::{occ_name}"
                r['term7'][key] = {
                    'term7_MeV': t7,
                    'B_pred_MeV': b_pred,
                    'err_pct': err,
                }
                print(f"  {r['iso']:<6} {A:>2} {r['sigma_3A_MeV']:>10.3f} "
                      f"{t7:>+14.3e} {b_pred:>+10.3f} {b_nucl:>+10.3f} "
                      f"{err:>+9.2f}%")
    print()

    # Specifically inspect 4He: gap is ~27 MeV; can H_q values cover it?
    print("=" * 100)
    print("  ⁴He drill-down — can 3 self-conjugate height-6 partitions of 12 cover ~27 MeV?")
    print("=" * 100)
    he4 = next(r for r in rows if r['iso'] == '4He')
    target_gap = he4['B_nucl_MeV'] - he4['sigma_3A_MeV']
    print(f"  Target gap (B_nucl − σ_3A): {target_gap:.3f} MeV")
    print(f"  Target / m_e:               {target_gap / float(me):.3e}")
    print()
    sum_Hq_sc = sum(float(hook_product_q(lam)) for lam in h6_sc[4])
    sum_Hq_full = sum(float(hook_product_q(lam)) for lam in h6_full[4])
    print(f"  Σ H_q(λ)  over self-conj h=6 of 12: {sum_Hq_sc:.4e}")
    print(f"  m_e · ΣH_q (sc):                    {float(me) * sum_Hq_sc:.4e} MeV")
    print(f"  Σ H_q(λ)  over all h=6 of 12:       {sum_Hq_full:.4e}")
    print(f"  m_e · ΣH_q (all):                   {float(me) * sum_Hq_full:.4e} MeV")
    print()

    # Required occupancy magnitude to reach target_gap
    print(f"  Required avg occupancy to bridge gap (sc): "
          f"{target_gap / (float(me) * sum_Hq_sc):.4e}")
    print(f"  Required avg occupancy to bridge gap (all):"
          f"{target_gap / (float(me) * sum_Hq_full):.4e}")
    print()

    # Save witness
    witness = {
        'computation': 'term-7-shell-correction-test',
        'description': (
            'Numerical test of conj:shell-correction-term-seven using '
            'height-6 (and self-conjugate height-6) partitions of 3A '
            'against Coulomb-corrected nuclear binding B_nucl from '
            'coulomb-subtracted-binding.witness.json.  Tries four '
            'occupancy formulas: w=1, min(Z,N), (Z·N)/A², '
            '(n_pp+n_nn)/A.  Compares to baseline B_pred = '
            'm_e·Σ_{λ⊢3A} 1/dim_q(λ) + Term_7.'
        ),
        'reference_blocks': [
            'conj:shell-correction-term-seven',
            'rem:higher-a-shell-diagnostic',
            'prop:bw-coefficient-shadow-price',
        ],
        'inputs': [
            'coulomb-subtracted-binding.witness.json',
        ],
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'm_e_MeV': float(me),
        'occupancies_tested': list(OCCUPANCY.keys()),
        'partition_filters': [
            'self-conjugate height-6',
            'all height-6',
        ],
        'isotopes': rows,
        '4He_drilldown': {
            'target_gap_MeV': target_gap,
            'sum_Hq_self_conj': sum_Hq_sc,
            'sum_Hq_all_h6': sum_Hq_full,
            'm_e_sum_Hq_sc_MeV': float(me) * sum_Hq_sc,
            'm_e_sum_Hq_all_MeV': float(me) * sum_Hq_full,
            'required_avg_occupancy_sc': target_gap / (float(me) * sum_Hq_sc),
            'required_avg_occupancy_all': target_gap / (float(me) * sum_Hq_full),
        },
    }
    out = Path(__file__).parent / "term-7-shell-correction-test.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"  Witness: {out}")


if __name__ == "__main__":
    main()
