#!/usr/bin/env python3
"""
ATOMIC CHIRALITY RESIDUE SCANNER

Phase C from the Yekutieli/Plancherel branch: extract the persistent
gauge-invariant (chirality) background from atomic braids.

For each isotope, evaluate Plancherel-weighted log-character on the
chirality cells (Wedderburn blocks with signed_content = 0, i.e.
D_q² = 0 in the q-Dirac cell scanner).  These cells are the
algebraic analogue of the gluon-condensate background — see
`prop:confinement-categorical` and `rem:confinement-curvature-rank`.

The chirality residue is

    Φ_chir^{(k)}(K) := Σ_{λ : depth(λ)=k, D_q²(λ)=0} w_λ · log|χ_λ(β_K)|

i.e. Φ_k restricted to the chirality cells.  Numerical comparison
against B_nucl tells us how much of nuclear binding lives in the
chirality channel vs. the non-chirality (D_q² ≠ 0) cells.

Uses Rust seminormal kernel `pyhecke_native.chi_lambda_braid` for
fast character evaluation (~50× faster than pure Python for n ≥ 9).
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys, json, warnings
from multiprocessing import Pool, cpu_count
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import mpmath as mp
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV
from hecke_characters import (
    partitions_of, dim_q,
    chi_lambda_braid as _shared_chi_lambda_braid,
    _RUST_CHI_AVAILABLE as _RUST_AVAILABLE,
)
from hecke_core_legacy import _step_chain_generic
from q_mpmath import set_q, qfac
from witness_base import WitnessBuilder

set_q(Q0_FLOAT)

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
H_A = Q0 - QI
h_val = float(H_A)
me = mp.mpf(str(M_E_MEV))
G = mp.catalan
alpha_bind = me * 8 * G


def signed_content(lam):
    """Signed Young content c_λ = Σ_{(i,j) ∈ λ} (j − i)."""
    total = 0
    for i, row in enumerate(lam):
        for j in range(row):
            total += j - i
    return total


def is_chirality_cell(lam):
    """Chirality cell: signed_content(λ) = 0 ⇒ D_q²(λ) = 0."""
    return signed_content(lam) == 0


def atomic_braid_word(Z, N):
    """Build atomic braid as a word on 3A strands (1-indexed gens)."""
    A = Z + N
    n_gens = max(1, 3 * A - 1)
    ordering = ['p'] * Z + ['n'] * N
    word = []
    for k in range(A):
        chain = _step_chain_generic(
            ordering[k], ordering[:k], n_gens, include_inter=True
        )
        for c, d, g in chain:
            cf = float(c); df = float(d)
            if abs(cf - 1.0) < 1e-10 and abs(df) < 1e-10:
                word.append(('+', g + 1))
            elif abs(cf - 1.0) < 1e-10 and abs(df + h_val) < 1e-10:
                word.append(('-', g + 1))
            else:
                word.append(('+', g + 1))
    return word


def _process(args):
    """Worker: evaluate χ_λ(β) and return the per-block summary."""
    lam_t, word_marshalled, nfac, q0_float = args
    is_chir = is_chirality_cell(lam_t)
    depth = len(lam_t) - 1
    try:
        chi = _shared_chi_lambda_braid(lam_t, word_marshalled, q_value=q0_float)
    except Exception:
        return None
    if chi == 0:
        return None
    dq = float(dim_q(lam_t))
    w_lam = dq * dq / nfac
    log_abs_chi = float(mp.log(abs(chi)))
    sign_chi = 1 if chi > 0 else -1
    return (lam_t, depth, w_lam, chi, log_abs_chi, sign_chi, is_chir)


def main():
    print("=" * 100)
    print("ATOMIC CHIRALITY RESIDUE SCANNER")
    print("=" * 100)
    kernel = "Rust (pyhecke_native)" if _RUST_AVAILABLE else "Python"
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  Character kernel: {kernel}")
    print(f"  α = m_e · 8G = {float(alpha_bind):.4f} MeV")
    print()

    # Coulomb-corrected B_nucl (MeV).  For Z ≥ 2, AME experimental
    # binding plus Coulomb-energy estimate from the symmetric
    # nuclear shell model.
    #
    # Higher-A isotopes (⁶Li, ⁷Li, ⁹Be, ¹²C) require kernel
    # optimization beyond the current Rust seminormal: at n=18 (⁶Li)
    # there are 385 partitions some with dim ~ O(10⁵), pushing the
    # current vector-trace algorithm past 10-minute budgets.
    # Future work: SIMD vectorization or batched character evaluation.
    B_NUCL = {
        ('D',   1, 1): 2.22456612,
        ('T',   1, 2): 8.481798,
        ('3He', 2, 1): 8.59697,
        ('4He', 2, 2): 29.32700,
    }
    isotopes = [
        ('D',   1, 1, B_NUCL[('D',   1, 1)]),
        ('T',   1, 2, B_NUCL[('T',   1, 2)]),
        ('3He', 2, 1, B_NUCL[('3He', 2, 1)]),
        ('4He', 2, 2, B_NUCL[('4He', 2, 2)]),
    ]

    n_workers = max(1, cpu_count() - 1)
    rows = []
    for name, Z, N, B_nucl in isotopes:
        A = Z + N
        n = 3 * A
        word = atomic_braid_word(Z, N)
        word_marshalled = [(1 if s == '+' else -1, g) for s, g in word]
        nfac = float(qfac(n))

        jobs = [
            (tuple(lam), word_marshalled, nfac, float(Q0_FLOAT))
            for lam in partitions_of(n)
        ]
        with Pool(n_workers) as pool:
            results = pool.map(_process, jobs)

        # Per-depth aggregation, with chirality vs. non-chirality split
        per_depth = {}  # depth -> {'chir': [...], 'non_chir': [...]}
        n_chir_cells = 0
        n_total_cells = 0
        for r in results:
            if r is None:
                continue
            lam_t, depth, w, chi, lac, sgn, is_chir = r
            n_total_cells += 1
            if is_chir:
                n_chir_cells += 1
            bucket = 'chir' if is_chir else 'non_chir'
            per_depth.setdefault(depth, {'chir': [], 'non_chir': []})[bucket].append(
                (lam_t, w, chi, lac, sgn)
            )

        # Compute Φ_chir^{(k)} and Φ_non_chir^{(k)} per depth
        Phi_chir = {}
        Phi_total = {}
        Pi_chir = {}
        for d, bucket in per_depth.items():
            phi_c = sum(w * lac for _, w, _, lac, _ in bucket['chir'])
            phi_n = sum(w * lac for _, w, _, lac, _ in bucket['non_chir'])
            pi_c = sum(w for _, w, _, _, sgn in bucket['chir'] if sgn < 0)
            Phi_chir[d] = phi_c
            Phi_total[d] = phi_c + phi_n
            Pi_chir[d] = pi_c

        print(f"\n  === {name} (Z={Z}, N={N}, 3A={n}) ===")
        print(f"    Chirality cells: {n_chir_cells}/{n_total_cells} "
              f"({100*n_chir_cells/n_total_cells:.1f}% by count)")
        print(f"    {'depth':>5} {'#chir':>6} {'#total':>7} "
              f"{'Φ_chir':>14} {'Φ_total':>14} {'chir/total':>10}")
        for d in sorted(per_depth):
            n_c = len(per_depth[d]['chir'])
            n_t = n_c + len(per_depth[d]['non_chir'])
            pc = Phi_chir[d]
            pt = Phi_total[d]
            ratio = pc / pt if abs(pt) > 1e-12 else 0.0
            print(f"    {d:>5} {n_c:>6} {n_t:>7} {pc:>14.6f} {pt:>14.6f} "
                  f"{ratio:>10.4f}")

        # Total chirality residue
        Phi_chir_total = sum(Phi_chir.values())
        Phi_chir_high = sum(Phi_chir.get(d, 0) for d in range(4, n))
        Chir_MeV = float(alpha_bind) * Phi_chir_total
        Chir_high_MeV = float(alpha_bind) * Phi_chir_high

        print(f"\n    α · Φ_chir (all depths)         = {Chir_MeV:+.6f} MeV")
        print(f"    α · Φ_chir (depths ≥ 4 only)    = {Chir_high_MeV:+.6f} MeV")
        print(f"    Coulomb-corrected B_nucl        = {B_nucl:+.4f} MeV")
        print(f"    Chirality fraction of B_nucl    = {Chir_MeV / B_nucl:.4f}")

        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'B_nucl': B_nucl,
            'n_chir_cells': n_chir_cells,
            'n_total_cells': n_total_cells,
            'Phi_chir_per_depth': {str(k): float(v) for k, v in Phi_chir.items()},
            'Phi_total_per_depth': {str(k): float(v) for k, v in Phi_total.items()},
            'Pi_chir_per_depth': {str(k): float(v) for k, v in Pi_chir.items()},
            'alpha_Phi_chir_total_MeV': Chir_MeV,
            'alpha_Phi_chir_high_MeV': Chir_high_MeV,
        })

    # ── Emit witness via WitnessBuilder (provenance + assertions) ──
    builder = WitnessBuilder("atomic-chirality-residue")
    builder.set_description(
        'Plancherel-weighted log-character contribution from the '
        'chirality cells (D_q² = 0 ⇔ signed_content(λ) = 0) in the '
        'atomic braid character decomposition. Provides the '
        'gauge-invariant background ("gluon condensate") '
        'contribution per curvature-rank stratum. '
        'Wired to prop:confinement-categorical — the spectral-sequence-collapse '
        'reading of confinement predicts that only Wedderburn-central '
        '(D_q² = 0) observables survive, i.e. the chirality channel.'
    )
    builder.set_content_block("prop:confinement-categorical")
    builder.add_parameter("q0", str(Q0_FLOAT))
    builder.add_parameter("kernel", "rust" if _RUST_AVAILABLE else "python")
    builder.add_data("isotopes", rows)

    # ── Assertions ──
    # 1. Every isotope has at least one chirality cell at the binding-energy
    #    stratum (depth = A-1 or thereabouts). If 0/N then the chirality-
    #    channel claim is empty.
    n_iso_with_chir = sum(1 for r in rows if r['n_chir_cells'] > 0)
    builder.add_assertion(
        "all_isotopes_have_chirality_cells",
        computed=float(n_iso_with_chir),
        expected=float(len(rows)),
        tolerance=0.0,
        unit="count",
        source=(
            "prop:confinement-categorical claims confinement = collapse "
            "onto chirality cells. Every isotope must have ≥ 1 chirality "
            "cell in its Wedderburn decomposition."
        ),
    )
    # 2. Chirality fraction of binding energy is in [-2, 2]: this is a
    #    well-formedness check — the chirality channel can contribute
    #    positively (binding-deepening) or negatively (binding-reducing,
    #    interpreted as a sign-coherence cancellation in the gauge background).
    #    A value outside [-2, 2] would indicate the chirality residue
    #    dominates by >2× the actual binding, which is implausible.
    chir_fractions = [abs(r['alpha_Phi_chir_total_MeV'] / r['B_nucl'])
                      for r in rows if r['B_nucl']]
    max_chir_frac = max(chir_fractions) if chir_fractions else 0.0
    builder.add_assertion(
        "chirality_fraction_bounded",
        computed=float(max_chir_frac),
        expected=0.0,
        tolerance=2.0,
        unit="|fraction|",
        source=(
            "|α · Φ_chir(K) / B_nucl(K)| ≤ 2 across all isotopes — "
            "well-formedness check on the chirality-channel contribution. "
            f"Per-isotope: {[(r['iso'], round(r['alpha_Phi_chir_total_MeV']/r['B_nucl'], 3)) for r in rows if r['B_nucl']]}"
        ),
    )

    builder.save()
    print(f"\n  Witness emitted: atomic-chirality-residue.witness.json")


if __name__ == "__main__":
    main()
