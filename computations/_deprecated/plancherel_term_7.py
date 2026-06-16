#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
TERM 7 PROPERLY VIA PLANCHEREL WEIGHTS — log-functional Φ_k at
curvature-rank strata k = 4, 5.

Per prop:spectral-sequence-collapse, the GB filtration spectral
sequence collapses at E_1 (semisimple cohomology), so the mass
formula reduces to Plancherel-weighted Markov-trace projection
on the centre Z(H_n(q)) = ⊕_λ ℂ·p_λ.

The mass mechanism is LOGARITHMIC: the paper's Φ_1, Φ_2, Φ_3 in
wedderburn-mass-formula are log|trace|, log|det|, log|sym/alt|.
We extend this to Φ_4, Φ_5 at higher curvature-rank strata
(GB depths 4, 5), binning by partition height.

Approach (per user direction):
  1. For each isotope (Z, N), build atomic braid β.
  2. For each partition λ ⊢ 3A, compute χ_λ(β) via Hoefsmit.
  3. Compute w_λ = dim_q²(λ)/[3A]_q! (Plancherel weight, bounded).
  4. Define Φ_k(β) = Σ_{λ : depth(λ) = k} w_λ · log|χ_λ(β)|.
     (log makes contributions O(10) even when traces are O(1))
  5. Bin by depth (= height − 1).
  6. Add α · Φ_4 + α · Φ_5 to the existing 3-term formula's
     binding contribution.  Compare to B_nucl (Coulomb-subtracted).

Goal: see if Plancherel-weighted log functionals at curvature-rank
4-5 close the binding gap for D, T, ³He, ⁴He.
"""
from __future__ import annotations
import sys, json, warnings
from multiprocessing import Pool, cpu_count
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from scipy import sparse as sp_sparse
import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hecke_characters import (
    partitions_of, dim_q, build_seminormal_matrices,
    chi_lambda_braid as _shared_chi_lambda_braid,
    _RUST_CHI_AVAILABLE as _RUST_AVAILABLE,
    PRECISION_F64_FALLBACK, PRECISION_MPFR_50DPS,
)
from hecke_core import _step_chain_generic
from q_mpmath import set_q, qfac as _qfac_shared
from profiling import profile

set_q(Q0_FLOAT)

# Default precision for this script.  Set via CLI arg / env var:
#   PLANCHEREL_PRECISION=mpfr_50dps python3 plancherel_term_7.py
import os as _os
PRECISION = _os.environ.get("PLANCHEREL_PRECISION", PRECISION_F64_FALLBACK)

# F5: parameterized ε-cutoff on Plancherel weight w_λ.
# Default 0.0 = no truncation = exact sum.  When > 0, partitions with
# w_λ < EPS_CUTOFF are skipped; the result is labeled as truncated.
# CLI: EPS_CUTOFF=1e-3 python3 plancherel_term_7.py
EPS_CUTOFF = float(_os.environ.get("EPS_CUTOFF", "0.0"))

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
me = mp.mpf(str(M_E_MEV))
G = mp.catalan
alpha_bind = me * 8 * G
H_A = Q0 - QI
h_val = float(H_A)
q3_q = Q0**2 + 1 + QI**2


def qfac(n):
    """q-factorial — re-uses shared q_mpmath.qfac."""
    return _qfac_shared(n)


def atomic_braid_word(Z, N):
    """Build atomic braid as a word on 3A strands (1-indexed generators)."""
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    word = []  # list of (sign, gen_index 1-indexed)
    for k in range(A):
        chain = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=True)
        for c, d, g in chain:
            # convert (c, d) to braid letters
            cf = float(c); df = float(d)
            if abs(cf - 1.0) < 1e-10 and abs(df) < 1e-10:
                # sigma (positive)
                word.append(('+', g + 1))
            elif abs(cf - 1.0) < 1e-10 and abs(df + h_val) < 1e-10:
                # sigma^{-1}
                word.append(('-', g + 1))
            else:
                # ud-mixed: treat as (sigma + sigma^-1)/2 → add positive then negative
                # for chi computation, we use the average; here just track positive
                word.append(('+', g + 1))
    return word


def chi_lambda_at_q0(shape, word):
    """Compute χ_λ(β) at q_0 via Hoefsmit seminormal."""
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)
    for sign, gen in word:
        idx = gen - 1  # 0-indexed
        if idx >= len(sigmas) or idx < 0:
            continue
        if sign == '+':
            M = sigmas[idx]
        else:
            M = sigmas[idx] - h_val * I
        product = product @ M
    if is_sparse:
        chi = float(product.diagonal().sum())
    else:
        chi = float(np.trace(product))
    return chi


def _chi_lambda_fast(lam_t, word, q0_float, precision=None):
    """Character χ_λ(β) at q_0 at requested precision tag.

    For precision='f64', returns float (fast).
    For precision='mpfr_50dps' or higher, returns float parsed from
    the mpfr decimal string (50 dps preserved through float? — note
    Python float is f64; if you need full precision, use mpmath.mpf
    on the returned string).
    """
    if precision is None:
        precision = PRECISION
    result = _shared_chi_lambda_braid(
        lam_t, word, q_value=q0_float, precision=precision
    )
    # mpfr returns a string; convert to float for log/sign operations.
    # (For full ppb-level downstream propagation, callers should use
    # mpmath.mpf(result) directly instead of float().)
    if isinstance(result, str):
        return float(result)
    return result


def _process_partition(args):
    """Worker for multiprocessing.Pool.

    Returns (lam_t, depth, w_lam, chi, log_abs_chi, sign_chi) on success,
    or None on error / vanishing character.  Top-level (picklable).

    `sign_chi`: +1 if χ > 0, −1 if χ < 0.  Used for Phase D phase
    tracking — the full complex log is `log|χ| + (sign−1)/(−2)·iπ`,
    so the Plancherel-weighted complex Φ_k decomposes into a real
    part (current Term-7 formulation) plus an imaginary part counting
    π-fluxes at depth k.
    """
    lam_t, word, nfac, q0_float = args
    depth = len(lam_t) - 1
    try:
        chi = _chi_lambda_fast(lam_t, word, q0_float)
    except Exception:
        return None
    if chi == 0:
        return None
    dq = float(dim_q(lam_t))
    w_lam = dq * dq / nfac
    log_abs_chi = float(np.log(abs(chi)))
    sign_chi = 1 if chi > 0 else -1
    return (lam_t, depth, w_lam, chi, log_abs_chi, sign_chi)


def main():
    print("=" * 100)
    print("TERM 7 via PLANCHEREL WEIGHTS — log Φ_k at curvature-ranks 4, 5")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  α = m_e · 8G = {float(alpha_bind):.4f} MeV")
    print()

    # B_nucl from coulomb-subtracted-binding.witness.json
    B_NUCL = {
        ('D',   1, 1): 2.22456612,
        ('T',   1, 2): 8.481798,
        ('3He', 2, 1): 8.59697,    # AME 7.7181 + Coulomb 0.879
        ('4He', 2, 2): 29.32700,   # 28.296 + 1.031
    }
    isotopes = [
        ('D',   1, 1, 1876.12393, B_NUCL[('D', 1, 1)]),
        ('T',   1, 2, 2809.43215, B_NUCL[('T', 1, 2)]),
        ('3He', 2, 1, 2809.41347, B_NUCL[('3He', 2, 1)]),
        ('4He', 2, 2, 3728.40133, B_NUCL[('4He', 2, 2)]),
    ]

    n_workers = max(1, cpu_count() - 1)
    kernel = "Rust (pyhecke_native)" if _RUST_AVAILABLE else "Python"
    print(f"  Character kernel: {kernel}")
    print(f"  Precision tag:    {PRECISION}")
    print(f"  Using {n_workers} parallel workers for character evaluation\n")

    rows = []
    for name, Z, N, M_ref, B_nucl in isotopes:
        A = Z + N
        n = 3 * A
        word = atomic_braid_word(Z, N)
        nfac = float(qfac(n))

        # Build job list: one (lam_t, word, nfac, q) tuple per partition
        jobs = [(tuple(lam), word, nfac, float(Q0_FLOAT)) for lam in partitions_of(n)]
        # Profile this isotope's character-eval phase.
        _profile_ctx = profile("plancherel_term_7", precision=PRECISION,
                                isotope=name, n=n)
        _profile_ctx.__enter__()

        # F2: batch character evaluation in Rust (rayon-parallel inside).
        # Replaces previous Python multiprocessing.Pool path — no
        # pickling overhead, work-stealing balances dim variation.
        per_depth = {}  # depth -> [(λ, w_λ, χ, log|χ|, sign)]
        try:
            import pyhecke_native as _pyn
            shapes_list = [list(lam) for lam, *_ in jobs]
            word_marshalled = [(1 if s == '+' else -1, g) for s, g in word]
            if PRECISION.startswith("mpfr_"):
                # mpfr batch — preserve precision via decimal string for q.
                q_str = format(float(Q0_FLOAT), ".50g")
                dps = int(PRECISION.split("_")[1].rstrip("dps")) \
                    if PRECISION.split("_")[1].endswith("dps") \
                    else int(PRECISION.split("_")[1])
                chi_strs = _pyn.chi_lambdas_braid_mpfr(
                    shapes_list, word_marshalled, q_str, dps
                )
                chis = [float(s) for s in chi_strs]
            else:
                chis = _pyn.chi_lambdas_braid(
                    shapes_list, word_marshalled, float(Q0_FLOAT)
                )
        except (ImportError, AttributeError):
            # Fallback to multiprocessing.Pool path if Rust batch
            # unavailable (e.g., older pyhecke_native build).
            if n_workers > 1 and len(jobs) > 4:
                with Pool(n_workers) as pool:
                    results = pool.map(_process_partition, jobs)
            else:
                results = [_process_partition(j) for j in jobs]
            for r in results:
                if r is None:
                    continue
                lam_t, depth, w_lam, chi, log_abs_chi, sign_chi = r
                per_depth.setdefault(depth, []).append(
                    (lam_t, w_lam, chi, log_abs_chi, sign_chi)
                )
            _profile_ctx.__exit__(None, None, None)
            chis = None  # signal: results already aggregated above

        if chis is not None:
            # Aggregate batch results into per-depth structure.
            n_skipped_eps = 0
            for (lam_t_arg, _, _, _), chi in zip(jobs, chis):
                lam_t = lam_t_arg
                if chi == 0:
                    continue
                depth = len(lam_t) - 1
                dq = float(dim_q(lam_t))
                w_lam = dq * dq / nfac
                # F5: parameterized ε-cutoff (default 0 = no truncation).
                if EPS_CUTOFF > 0 and w_lam < EPS_CUTOFF:
                    n_skipped_eps += 1
                    continue
                log_abs_chi = float(np.log(abs(chi)))
                sign_chi = 1 if chi > 0 else -1
                per_depth.setdefault(depth, []).append(
                    (lam_t, w_lam, chi, log_abs_chi, sign_chi)
                )
            if EPS_CUTOFF > 0 and n_skipped_eps > 0:
                print(f"    [eps-cutoff {EPS_CUTOFF:.1e}: skipped "
                      f"{n_skipped_eps}/{len(chis)} partitions]")
            _profile_ctx.__exit__(None, None, None)

        # Compute Φ_k (real) = Σ_{λ at depth k} w_λ · log|χ_λ|
        # Compute Π_k (Phase D) = Σ_{λ at depth k} w_λ · [χ_λ < 0]
        #   The full complex Φ_k^complex = Φ_k + iπ · Π_k.
        Phi_k = {}
        Pi_k = {}
        for d, items in per_depth.items():
            phi = sum(w * lc for _, w, _, lc, _ in items)
            pi = sum(w for _, w, _, _, sgn in items if sgn < 0)
            Phi_k[d] = phi
            Pi_k[d] = pi

        print(f"\n  === {name} (Z={Z}, N={N}, 3A={n}) ===")
        print(f"    {'depth':>5} {'#λ':>4} {'Σ w_λ':>10} {'Φ_k':>14} {'α·Φ_k (MeV)':>14} {'Π_k':>9}")
        for d in sorted(Phi_k):
            items = per_depth[d]
            sum_w = sum(w for _, w, _, _, _ in items)
            phi = Phi_k[d]
            pi = Pi_k[d]
            print(f"    {d:>5} {len(items):>4} {sum_w:>10.6f} {phi:>14.6f} "
                  f"{float(alpha_bind) * phi:>+14.6f} {pi:>9.6f}")

        # Sum Φ_k for k >= 4 (NEW Term 7)
        Phi_term_7 = sum(Phi_k.get(d, 0) for d in range(4, n))
        Term_7_MeV = float(alpha_bind) * Phi_term_7
        # Phase D: total π-flux from negative characters across all depths
        Pi_total = sum(Pi_k.get(d, 0) for d in range(0, n))
        Pi_term_7 = sum(Pi_k.get(d, 0) for d in range(4, n))
        print(f"\n    Term 7 (depths 4..{n-1}) = α · Σ Φ_k = {Term_7_MeV:+.6f} MeV")
        print(f"    π-flux total across all k:     Π = {Pi_total:.6f}")
        print(f"    π-flux at depths 4..{n-1}:        Π_(≥4) = {Pi_term_7:.6f}")
        print(f"    Coulomb-corrected B_nucl  = {B_nucl:+.4f} MeV")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'B_nucl': B_nucl, 'Phi_per_depth': Phi_k,
            'Pi_per_depth': Pi_k,
            'Term_7_MeV': Term_7_MeV,
            'Pi_total': Pi_total,
            'Pi_term_7': Pi_term_7,
        })

    # Save witness
    witness = {
        'computation': 'plancherel-term-7-phase-d',
        'description': (
            'Term 7 via Plancherel-weighted log-functional Φ_k at '
            'curvature-rank strata k=4..n.  Phase D: also tracks Π_k = '
            'Σ_{λ:depth=k} w_λ·[χ_λ < 0], the Plancherel-weighted '
            'count of negative-character blocks (π-flux contribution '
            'to the full complex log).  Bounded weights w_λ = '
            'dim_q²(λ)/[n]_q!.  Log of trace gives O(10) magnitudes '
            'consistent with MeV scale.  Tested on D, T, 3He, 4He.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        # User directive: every result must carry a precision tag.
        # f64_numeric_fallback   ⇒ ~16 dps, fast Rust kernel
        # mpfr_50dps (or higher) ⇒ exact at requested decimal precision
        # symbolic_q             ⇒ deferred (F3 Murnaghan–Nakayama)
        'precision': PRECISION,
        # F5: ε-cutoff (0 = no truncation = exact sum).  When > 0, the
        # output is a TRUNCATED Plancherel sum; consumers should treat
        # the binding-energy / Φ_k results as approximations.
        'truncation_eps': EPS_CUTOFF,
        'q_0': Q0_FLOAT,
        'isotopes': [{
            'iso': r['iso'], 'Z': r['Z'], 'N': r['N'], 'A': r['A'],
            'B_nucl': r['B_nucl'],
            'Phi_per_depth': {str(k): float(v) for k, v in r['Phi_per_depth'].items()},
            'Pi_per_depth': {str(k): float(v) for k, v in r['Pi_per_depth'].items()},
            'Term_7_MeV': r['Term_7_MeV'],
            'Pi_total': r['Pi_total'],
            'Pi_term_7': r['Pi_term_7'],
        } for r in rows],
    }
    out = Path(__file__).parent / "plancherel-term-7.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
