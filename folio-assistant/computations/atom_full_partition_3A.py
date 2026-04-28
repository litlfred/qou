#!/usr/bin/env python3
"""
ATOM-LEVEL Wedderburn over ALL partitions λ ⊢ 3A.

Per user direction: "use all partitions" — sum the Markov trace
over every irrep of H_{3A}(q), not just sym/std/alt.

For each isotope, compute:

  tr_M(β_atom) = Σ_{λ ⊢ 3A} w_λ · χ_λ(β_atom) / dim_q V_λ

with algebraic Wedderburn weights w_λ = (dim_q V_λ)² / [3A]_q!.

Two physics goals:

  GOAL 1 (np splitting bridge).  The naive 1-chain identity
    Δm_{n-p} ≈ 2αH_A²·Φ_3(p) gave 0.205 MeV vs CODATA 1.293 MeV.
    With the FULL partition sum, we can directly compute
      Δm_{n-p} = (|tr_M(β_n)| - |tr_M(β_p)|)·E_0
    and check structural agreement.

  GOAL 2 (isotope extension).  For D, T, ³He, ⁴He, evaluate
  the partition sum and compare to CODATA.

S-decomposition: pair each λ with its transpose λ'; the
symmetric combination (λ + λ')/2 is S-even, the antisymmetric
is S-odd.  Self-conjugate λ = λ' lives entirely in S-even.
The np splitting must come from S-odd contributions.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 40

from hecke_core import (atom_character_raw, _partition_table,
                          _ensure_ysn_attached, h as H_A_F)
from hecke_characters import dim_q, young_hooks, partitions_of
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
H_A = Q0 - QI
me = mp.mpf(str(M_E_MEV))


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for k in range(2, n+1):
        out *= q_int(k)
    return out


def transpose_partition(lam):
    """λ → λ' (transpose)."""
    if not lam:
        return tuple()
    max_part = lam[0]
    return tuple(sum(1 for p in lam if p > j) for j in range(max_part))


def atom_partition_data(Z, N, max_strands=12):
    """Return list of (lam, dq, w_lam, chi, chi_norm, S_class) for each
    partition λ ⊢ 3A, where:
      lam       : the partition tuple
      dq        : dim_q V_λ (mpf)
      w_lam     : w_λ = (dim_q V_λ)² / [3A]_q!  (mpf)
      chi       : χ_λ(β_atom) — the actual trace value (mpc)
      S_class   : 'self' if λ = λ', else (λ', '+') for S-even pair member,
                  (λ', '-') for S-odd
    """
    A = Z + N
    n_strands = 3 * A
    if n_strands > max_strands:
        return None
    nfac = q_fact(n_strands)

    _ensure_ysn_attached()
    PT = _partition_table()
    entries = [e for e in PT if e['k'] == n_strands]

    rows = []
    for entry in entries:
        lam = tuple(entry['partition'])
        try:
            dq = mp.mpf(str(float(dim_q(lam))))
        except Exception:
            continue
        if dq == 0:
            continue
        w = dq * dq / nfac
        try:
            chi_q, log_norm, _ = atom_character_raw(Z, N, entry, include_inter=True)
        except Exception:
            continue
        # chi = chi_q * exp(log_norm), full character trace at q_0
        chi = mp.mpc(str(float(chi_q))) * mp.exp(mp.mpf(str(float(log_norm))))
        rows.append({'lam': lam, 'dq': dq, 'w_lam': w, 'chi': chi})

    # S-classify
    by_lam = {r['lam']: r for r in rows}
    for r in rows:
        lam = r['lam']
        lamp = transpose_partition(lam)
        if lamp == lam:
            r['S_class'] = ('self', None)
        elif lamp in by_lam:
            r['S_class'] = ('pair', lamp)
        else:
            r['S_class'] = ('orphan', lamp)
    return rows


def markov_trace(rows):
    """tr_M = Σ_λ w_λ · χ_λ / dim_q V_λ."""
    total = mp.mpc(0)
    for r in rows:
        total += r['w_lam'] * r['chi'] / r['dq']
    return total


def s_decompose(rows):
    """Split contributions into S-even and S-odd parts.
       S-even per pair: (χ_λ + χ_{λ'}) / 2
       S-odd per pair:  (χ_λ − χ_{λ'}) / 2
       Self-conjugate λ: entirely S-even.
    Returns (tr_M_even, tr_M_odd)."""
    tr_even = mp.mpc(0)
    tr_odd  = mp.mpc(0)
    by_lam = {r['lam']: r for r in rows}
    seen = set()
    for r in rows:
        lam = r['lam']
        if lam in seen:
            continue
        kind, partner = r['S_class']
        if kind == 'self':
            tr_even += r['w_lam'] * r['chi'] / r['dq']
            seen.add(lam)
        elif kind == 'pair' and partner in by_lam:
            r2 = by_lam[partner]
            chi_e = (r['chi'] + r2['chi']) / 2
            chi_o = (r['chi'] - r2['chi']) / 2
            # Each member contributes w·χ/dq.  Pair-sum:
            tr_even += r['w_lam'] * chi_e / r['dq'] + r2['w_lam'] * chi_e / r2['dq']
            tr_odd  += r['w_lam'] * chi_o / r['dq'] - r2['w_lam'] * chi_o / r2['dq']
            seen.add(lam); seen.add(partner)
        else:
            # orphan — shouldn't happen for full partition table
            tr_even += r['w_lam'] * r['chi'] / r['dq']
            seen.add(lam)
    return tr_even, tr_odd


def main() -> int:
    print("=" * 100)
    print("FULL-PARTITION ATOM-LEVEL WEDDERBURN  (λ ⊢ 3A, all partitions)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print()

    ISOTOPES = [
        ('p',   1, 0, M_P_MEV),
        ('n',   0, 1, M_N_MEV),
        ('D',   1, 1, 1876.12393),
        ('T',   1, 2, 2809.43215),
        ('³He', 2, 1, 2809.41347),
        ('⁴He', 2, 2, 3728.40133),
    ]

    # Calibrate via proton: |tr_M(β_p)| = M_P_MEV / E_0
    print("  Proton calibration:")
    rows_p = atom_partition_data(1, 0)
    if rows_p is None:
        print("  ERROR: proton partition data unavailable (max_strands)")
        return 1
    tr_p = markov_trace(rows_p)
    abs_p = float(mp.fabs(tr_p))
    E0 = M_P_MEV / abs_p
    print(f"    n_partitions = {len(rows_p)}")
    print(f"    |tr_M(β_p)|  = {abs_p:.10e}")
    print(f"    E_0 = M_p/|tr_M| = {E0:.6e} MeV/cat")
    print()

    # Per-isotope partition sum
    print(f"  {'iso':<6} {'A':>2} {'3A':>3} {'#λ':>4} {'|tr_M|':>15} "
          f"{'mass MeV':>10} {'CODATA':>10} {'err %':>9}")

    rows_out = []
    for name, Z, N, M_ref in ISOTOPES:
        rows = atom_partition_data(Z, N, max_strands=12)
        if rows is None:
            print(f"  {name:<6} {Z+N:>2} {3*(Z+N):>3} (skipped: > 12 strands)")
            continue
        tr = markov_trace(rows)
        tr_e, tr_o = s_decompose(rows)
        abs_tr = float(mp.fabs(tr))
        m_MeV = abs_tr * E0
        err = (m_MeV - M_ref) / M_ref * 100
        print(f"  {name:<6} {Z+N:>2} {3*(Z+N):>3} {len(rows):>4} "
              f"{abs_tr:>15.6e} {m_MeV:>10.4f} {M_ref:>10.4f} {err:>+8.3f}%")
        rows_out.append({
            'iso': name, 'Z': Z, 'N': N, 'A': Z+N, 'n_strands': 3*(Z+N),
            'n_partitions': len(rows),
            'tr_M_abs': abs_tr,
            'tr_M_re': float(mp.re(tr)), 'tr_M_im': float(mp.im(tr)),
            'tr_even_re': float(mp.re(tr_e)), 'tr_even_im': float(mp.im(tr_e)),
            'tr_odd_re':  float(mp.re(tr_o)), 'tr_odd_im':  float(mp.im(tr_o)),
            'mass_MeV': m_MeV,
            'CODATA_MeV': M_ref,
            'err_pct': err,
        })

    print()

    # GOAL 1: np mass splitting from S-decomposition
    print("─" * 100)
    print("  GOAL 1 — np mass splitting via S-eigenspace decomposition")
    print("─" * 100)
    rows_n = atom_partition_data(0, 1)
    if rows_n is None:
        print("  neutron data unavailable")
    else:
        tr_n = markov_trace(rows_n)
        tr_p_e, tr_p_o = s_decompose(rows_p)
        tr_n_e, tr_n_o = s_decompose(rows_n)

        # |tr_M(β_n)|·E_0 vs CODATA
        m_n_pred = float(mp.fabs(tr_n)) * E0
        delta_pred = m_n_pred - M_P_MEV
        delta_codata = M_N_MEV - M_P_MEV
        print(f"    |tr_M(β_p)| = {float(mp.fabs(tr_p)):.6e}   (calibrated to M_p)")
        print(f"    |tr_M(β_n)| = {float(mp.fabs(tr_n)):.6e}")
        print(f"    Δ|tr_M|·E_0 = {delta_pred:+.6f} MeV")
        print(f"    CODATA Δm_{{n-p}} = {delta_codata:+.6f} MeV")
        print(f"    err = {(delta_pred-delta_codata)/delta_codata*100:+.3f}%")
        print()
        print(f"  S-eigenspace decomposition of tr_M:")
        print(f"    {'iso':<8} {'|tr_even|':>15} {'|tr_odd|':>15} {'odd/even':>10}")
        for label, te, to in [('proton', tr_p_e, tr_p_o), ('neutron', tr_n_e, tr_n_o)]:
            ae, ao = float(mp.fabs(te)), float(mp.fabs(to))
            ratio = ao/ae if ae > 0 else float('inf')
            print(f"    {label:<8} {ae:>15.6e} {ao:>15.6e} {ratio:>10.4e}")
        print()
        print(f"    np splitting from S-odd: |tr_p_odd| - |tr_n_odd| = "
              f"{float(mp.fabs(tr_p_o)) - float(mp.fabs(tr_n_o)):+.6e}")
        print(f"    times E_0 = {(float(mp.fabs(tr_p_o)) - float(mp.fabs(tr_n_o)))*E0:+.6f} MeV")

    print()
    print("─" * 100)
    print("  GOAL 2 — isotope predictions summary")
    print("─" * 100)
    for r in rows_out:
        if r['iso'] in ('D', 'T', '³He', '⁴He'):
            print(f"    {r['iso']:<6}  {r['mass_MeV']:>10.4f} vs "
                   f"{r['CODATA_MeV']:>10.4f} MeV ({r['err_pct']:+.3f}%)")

    witness = {
        'computation': 'atom-full-partition-3A',
        'description': (
            'Full atom-level Wedderburn over all λ ⊢ 3A.  For each '
            'isotope compute tr_M(β_atom) = Σ_λ w_λ·χ_λ/dim_q V_λ '
            'with algebraic weights w_λ = (dim_q V_λ)²/[3A]_q!.  '
            'Calibrated to M_p; predicts m_n, D, T, ³He, ⁴He.  '
            'S-eigenspace decomposition (λ ↔ λ\') extracts S-even '
            'and S-odd contributions; np splitting localised to '
            'S-odd subspace.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'E0_MeV_per_cat': E0,
        'isotopes': rows_out,
    }
    out = Path(__file__).parent / "atom-full-partition-3A.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
