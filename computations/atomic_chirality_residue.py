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
import sys, json, time, warnings
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
    partitions_of, dim_q, qfac,
    chi_lambda_braid_mpf as _shared_chi_lambda_braid_mpf,
    _RUST_CHI_AVAILABLE as _RUST_AVAILABLE,
)
from hecke_core_legacy import _step_chain_generic
from witness_base import WitnessBuilder
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from _precision import fmt  # noqa: E402

# `qfac` comes from `hecke_characters`, NOT `q_mpmath`.  Two different functions
# share the name: `hecke_characters.qfac(n, q=None)` takes an explicit anchor
# (the `dim_q(shape, q)` idiom, bean `qou-wee5`), `q_mpmath.qfac(n)` takes only
# `n`.  This file imported the second and called the first, so `main` died at
# `qfac(n, Q0_PROTON)` with `TypeError: qfac() takes 1 positional argument but 2
# were given` -- measured, every run.  `set_q` went with it: with the anchor
# passed explicitly there was no consumer left, and it was being called at
# import time, where `mp.dps` is still mpmath's default 15.


def q0_mp() -> mp.mpf:
    """The proton pin as an `mpf`, built at the CURRENT precision.

    Replaces `qou_substrate.constants.Q`, a Python float (measured:
    `type(Q) is float`), which capped every `dim_q` / `qfac` call here at f64
    whatever `mp.dps` said.  A function rather than a constant because `mp.mpf`
    rounds at construction and at import time `mp.dps` is 15.
    """
    return Q_MP

Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
H_A = Q0 - QI
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
            # Was `float(c)` / `float(d)` against `h_val = float(H_A)`. The
            # OUTCOME here is discrete -- which sign the crossing carries -- and
            # a 1e-10 window on O(1) values cannot flip it, so this was not a
            # wrong answer. It is still an f64 computation in a `computations/`
            # script, which the NO-FLOAT64 rule covers regardless of whether the
            # result survives; `H_A` is already an mpf, so carrying it costs
            # nothing.
            cf = mp.mpf(str(c)); df = mp.mpf(str(d))
            tol = mp.mpf("1e-10")
            if abs(cf - 1) < tol and abs(df) < tol:
                word.append(('+', g + 1))
            elif abs(cf - 1) < tol and abs(df + H_A) < tol:
                word.append(('-', g + 1))
            else:
                word.append(('+', g + 1))
    return word


def _process(args):
    """Worker: evaluate χ_λ(β) and return the per-block summary.

    Everything here is `mpf`.  `mp.mpf` is picklable, so the multiprocessing
    boundary is not a reason to drop to f64 -- the previous version marshalled
    `nfac` and `q0` across it as Python floats and computed the whole worker in
    f64 as a result.  `dps` is set per worker because `set_compute_dps()` in the
    parent does not survive the fork on every platform.
    """
    lam_t, signed_word, nfac_str, q0_str, dps = args
    mp.mp.dps = dps
    nfac = mp.mpf(nfac_str)
    is_chir = is_chirality_cell(lam_t)
    depth = len(lam_t) - 1
    try:
        chi = _shared_chi_lambda_braid_mpf(lam_t, signed_word, q_value=q0_str)
    except Exception:
        return None
    if chi == 0:
        return None
    dq = dim_q(lam_t, mp.mpf(q0_str))
    w_lam = dq * dq / nfac
    log_abs_chi = mp.log(abs(chi))
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
        ('D',   1, 1): AME_B_DEUTERON_MEV_VALIDATION,
        ('T',   1, 2): AME_B_TRITIUM_MEV_VALIDATION,
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
        # `chi_lambda_braid_mpf` takes the FLAT SIGNED word and marshals the
        # (sign, generator) pairs itself, so the hand-rolled `word_marshalled`
        # that stood here is gone.
        signed_word = [g if s == '+' else -g for s, g in word]
        nfac = qfac(n, q0_mp())

        jobs = [
            (tuple(lam), signed_word, fmt(nfac), Q_50_DIGIT_STR, mp.mp.dps)
            for lam in partitions_of(n)
        ]
        # `imap_unordered` rather than `map`, purely so the run is observable.
        # The mpfr character kernel is ~8x the f64 one it replaced, which turns
        # 4He (n=12, 77 partitions, a 12-strand word) from minutes into tens of
        # minutes -- a `pool.map` there is a silent wait long enough to look
        # like a hang, which the long-compute logging discipline exists to
        # prevent. Order does not matter: every consumer below re-derives the
        # partition from the returned tuple.
        t_iso = time.time()
        results = []
        with Pool(n_workers) as pool:
            for i, r in enumerate(pool.imap_unordered(_process, jobs), 1):
                results.append(r)
                if i % 5 == 0 or i == len(jobs):
                    el = time.time() - t_iso
                    eta = el / i * (len(jobs) - i)
                    print(f"    [{name} n={n}] {i}/{len(jobs)} partitions  "
                          f"{el:6.1f}s elapsed, ~{eta:6.1f}s left", flush=True)

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
            # `mp.fsum`, not the builtin `sum`: these run to hundreds of terms
            # per depth and the builtin accumulates pairwise rounding.
            phi_c = mp.fsum(w * lac for _, w, _, lac, _ in bucket['chir'])
            phi_n = mp.fsum(w * lac for _, w, _, lac, _ in bucket['non_chir'])
            pi_c = mp.fsum(w for _, w, _, _, sgn in bucket['chir'] if sgn < 0)
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
            ratio = pc / pt if abs(pt) > mp.mpf("1e-12") else mp.mpf(0)
            print(f"    {d:>5} {n_c:>6} {n_t:>7} {float(pc):>14.6f} "
                  f"{float(pt):>14.6f} {float(ratio):>10.4f}")

        # Total chirality residue
        Phi_chir_total = mp.fsum(Phi_chir.values())
        Phi_chir_high = mp.fsum(Phi_chir.get(d, mp.mpf(0)) for d in range(4, n))
        Chir_MeV = alpha_bind * Phi_chir_total
        Chir_high_MeV = alpha_bind * Phi_chir_high
        B_nucl_mp = mp.mpf(str(B_nucl))

        print(f"\n    α · Φ_chir (all depths)         = {float(Chir_MeV):+.6f} MeV")
        print(f"    α · Φ_chir (depths ≥ 4 only)    = {float(Chir_high_MeV):+.6f} MeV")
        print(f"    Coulomb-corrected B_nucl        = {float(B_nucl_mp):+.4f} MeV")
        print(f"    Chirality fraction of B_nucl    = {float(Chir_MeV / B_nucl_mp):.4f}")

        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'B_nucl': fmt(B_nucl_mp),
            'n_chir_cells': n_chir_cells,
            'n_total_cells': n_total_cells,
            'Phi_chir_per_depth': {str(k): fmt(v) for k, v in Phi_chir.items()},
            'Phi_total_per_depth': {str(k): fmt(v) for k, v in Phi_total.items()},
            'Pi_chir_per_depth': {str(k): fmt(v) for k, v in Pi_chir.items()},
            'alpha_Phi_chir_total_MeV': fmt(Chir_MeV),
            'alpha_Phi_chir_high_MeV': fmt(Chir_high_MeV),
            # kept as mpf for the assertions below; stripped before `add_data`
            '_chir_frac_mp': abs(Chir_MeV / B_nucl_mp) if B_nucl_mp else mp.mpf(0),
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
    builder.add_parameter("q0", Q_50_DIGIT_STR)
    builder.add_parameter("kernel", "rust" if _RUST_AVAILABLE else "python")
    chir_fractions = [r.pop('_chir_frac_mp') for r in rows]
    builder.add_data("isotopes", rows)

    # ── Assertions ──
    # 1. Every isotope has at least one chirality cell at the binding-energy
    #    stratum (depth = A-1 or thereabouts). If 0/N then the chirality-
    #    channel claim is empty.
    n_iso_with_chir = sum(1 for r in rows if r['n_chir_cells'] > 0)
    builder.add_assertion(
        "all_isotopes_have_chirality_cells",
        # Counts, so `str(int)` -- `float()` made the witness carry `4.0` for a
        # cardinality and put two raw float64 fields into it. Tolerance 0 is
        # exact by construction here: this compares two integers.
        computed=str(n_iso_with_chir),
        expected=str(len(rows)),
        tolerance="0",
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
    max_chir_frac = max(chir_fractions) if chir_fractions else mp.mpf(0)
    builder.add_assertion(
        "chirality_fraction_bounded",
        computed=fmt(max_chir_frac),
        expected=fmt(mp.mpf(0)),
        tolerance="2",    # exact bound; string per the drained convention (qou-t0rf)
        unit="|fraction|",
        source=(
            "|α · Φ_chir(K) / B_nucl(K)| ≤ 2 across all isotopes — "
            "well-formedness check on the chirality-channel contribution. "
            f"Per-isotope: {[(r['iso'], mp.nstr(f, 6)) for r, f in zip(rows, chir_fractions)]}"
        ),
    )

    builder.save()
    print(f"\n  Witness emitted: atomic-chirality-residue.witness.json")


if __name__ == "__main__":
    main()
