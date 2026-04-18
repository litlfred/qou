#!/usr/bin/env python3
"""
Task-1 FIX:  Proper H_{3A} Wedderburn character-theoretic binding.

Replaces the per-generator H_3 Wedderburn weighting inside
atom_per_generator_volumes (which pretends each generator sits in its
own H_3(q)) with the full character sum at H_{3A}(q), evaluated on
the actual 3A-strand braid word — using build_seminormal_matrices for
each λ ⊢ 3A.

Key design decisions:

1. Calibration: E_0 = 0.782 MeV (free-neutron β-decay Q-value),
   per prop:categorical-mass-markov.  NO Catalan / ALPHA.

2. Braid word: uses the same walk as atom_per_generator_volumes —
     for each nucleon k (proton or neutron):
       intra g₀ pass: (c, d) from _PROTON_G0 or _NEUTRON_G0, at gen 3k
       intra g₁ pass: (c, d) from _PROTON_G1 or _NEUTRON_G1, at gen 3k+1
       inter  pass:  pp / nn / pn from Hecke relation, at gen 3k+2
                     (only if include_inter = True)
   → A word on 3A − 1 generators of H_{3A}.

3. Per partition λ ⊢ 3A, compute
       M_λ = Π_k (c_k · σ_{g_k}^λ + d_k · I)
       χ_λ(W) = tr(M_λ).
   Markov trace:
       tr_M(W) = Σ_λ w_λ · χ_λ(W) / d_λ,    w_λ = d_q(λ)² / [3A]_q!.
   Binding: B = E_0 · ( |tr_M(W_free)| − |tr_M(W_atom)| ).

4. Heavy atoms: full p(3A) enumeration fails for 3A ≳ 35 (p(36) ≈
   17 000, dim-sum ≈ 3 × 10⁷).  Any truncation is an audit option,
   never the default.
"""
from __future__ import annotations

import sys
import math
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, Q_INV as QI, HA as HA_VAL
from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
                         E_0_CALIBRATION_MEV)
from hecke_characters import (partitions_of, build_seminormal_matrices,
                                dim_q, qfac)

h = HA_VAL


# In-memory cache: binding_3A calls markov_trace_3A twice (atom, free)
# so at minimum this saves one re-build per run.
_SEMINORMAL_CACHE: dict[tuple[int, tuple[int, ...]], tuple] = {}

# Disk cache for seminormal matrices: standard_young_tableaux is slow
# (multi-second for dim > 5000 partitions at n=12), so we persist the
# built matrices.  Keyed by (n, shape, q0).
_SEMINORMAL_DISK = Path(__file__).parent / ".cache" / "seminormal"


def _cached_seminormal(shape: tuple[int, ...]):
    import pickle
    n = sum(shape)
    key = (n, shape)
    if key in _SEMINORMAL_CACHE:
        return _SEMINORMAL_CACHE[key]
    # Disk lookup (shape-specific file; Q0 in name avoids stale)
    _SEMINORMAL_DISK.mkdir(parents=True, exist_ok=True)
    fname = (_SEMINORMAL_DISK /
              f"n{n}_q{Q0:.10f}_shape{'-'.join(map(str, shape))}.pkl")
    if fname.exists():
        try:
            with fname.open('rb') as f:
                data = pickle.load(f)
            _SEMINORMAL_CACHE[key] = data
            return data
        except Exception:
            pass
    data = build_seminormal_matrices(shape)
    _SEMINORMAL_CACHE[key] = data
    try:
        with fname.open('wb') as f:
            pickle.dump(data, f)
    except Exception:
        pass
    return data


def atom_braid_word_3A(Z: int, N: int, *, m_pp: int = 1, m_pn: int = 1,
                         m_nn: int = 1, include_inter: bool = True):
    """Full 3A-strand braid word as a list of (c, d, gen_idx) triples.

    Matches the chain-walk convention of
    hecke_core.atom_per_generator_volumes (lines 3029–3079):
    for each nucleon k, apply intra g₀, intra g₁, then (if
    include_inter) the appropriate pp/nn/pn crossing at gen 3k+2.

    gen_idx is 0-based (σ_0 = sigmas[0] in build_seminormal_matrices).
    """
    A = Z + N
    word: list[tuple[float, float, int]] = []
    ordering = ['p'] * Z + ['n'] * N
    for k, nuc in enumerate(ordering):
        intra = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        base_g0 = 3 * k
        base_g1 = 3 * k + 1
        for c, d in intra:
            word.append((float(c), float(d), base_g0))
        for c, d in intra_g1:
            word.append((float(c), float(d), base_g1))
        if include_inter and k < A - 1:
            i_inter = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = (1.0, 0.0)
                m_this = m_pp
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (1.0, -h)
                m_this = m_nn
            else:
                base_cross = (1.0, -h / 2)
                m_this = m_pn
            c, d = base_cross
            for _ in range(m_this):
                word.append((c, d, i_inter))
    return word


def chi_lambda_of_word(sigmas, dim, word, n_gens_required: int) -> float:
    """Character χ_λ(W) = tr(Π_k (c_k · σ_{g_k} + d_k · I)) in the λ-irrep.

    ``sigmas`` is the list from build_seminormal_matrices.
    ``word`` is the list of (c, d, gen_idx) triples from
    atom_braid_word_3A.
    """
    if dim == 0:
        return 0.0
    try:
        from scipy import sparse as sp_sparse
        is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    except ImportError:
        is_sparse = False
    if is_sparse:
        from scipy import sparse as sp_sparse
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)
    for (c, d, g) in word:
        if g >= len(sigmas):
            raise IndexError(
                f"word uses generator σ_{g} but only {len(sigmas)} "
                f"seminormal matrices were provided (partition too small)")
        M = c * sigmas[g] + d * I
        product = product @ M
    if is_sparse:
        return float(product.diagonal().sum())
    return float(np.trace(product))


def markov_trace_3A(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                      include_inter: bool = True,
                      verbose: bool = False) -> dict:
    """Full H_{3A} Markov trace of the atom (or free) braid word.

    Returns dict with keys
      ``total``         : tr_M(W) = Σ_λ w_λ · χ_λ(W) / d_λ
      ``per_partition`` : per-λ record {partition, dim, w, chi, contrib}
      ``n_partitions``  : p(3A)
      ``n_gens``        : 3A − 1
    """
    A = Z + N
    if A < 1:
        return {"total": 1.0, "per_partition": [],
                "n_partitions": 0, "n_gens": 0}
    n_strands = 3 * A
    n_gens = n_strands - 1

    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)

    nfac = qfac(n_strands)
    total = 0.0
    per_partition = []
    for shape in partitions_of(n_strands):
        sigmas, dim, _syts = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        w = (dq * dq) / nfac
        chi = chi_lambda_of_word(sigmas, dim, word, n_gens)
        contrib = w * chi / dim
        total += contrib
        per_partition.append({
            "partition": shape, "dim": dim, "w": w,
            "chi": chi, "contrib": contrib,
        })
        if verbose:
            print(f"  {str(shape):>24} dim={dim:>4} w={w:+.4e} "
                  f"χ={chi:+.4e} contrib={contrib:+.4e}")
    return {
        "total": total,
        "per_partition": per_partition,
        "n_partitions": len(per_partition),
        "n_gens": n_gens,
    }


def binding_3A(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                E_0: float = E_0_CALIBRATION_MEV,
                verbose: bool = False) -> dict:
    """Binding via H_{3A} character-theoretic Markov trace.

    B = E_0 · ( |tr_M(W_free)| − |tr_M(W_atom)| )
    with W_free (include_inter=False) and W_atom (include_inter=True)
    on the same 3A-strand Iwahori–Hecke algebra.
    """
    tr_atom = markov_trace_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=True, verbose=verbose)
    tr_free = markov_trace_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=False, verbose=verbose)
    B = E_0 * (abs(tr_free["total"]) - abs(tr_atom["total"]))
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_pp": m_pp, "m_pn": m_pn, "m_nn": m_nn,
        "tr_M_atom": tr_atom["total"],
        "tr_M_free": tr_free["total"],
        "abs_diff": abs(tr_free["total"]) - abs(tr_atom["total"]),
        "E_0_MeV": E_0,
        "B_MeV": B,
        "n_partitions": tr_atom["n_partitions"],
    }


# ── CLI ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(
        description="H_{3A} Wedderburn-character binding (task-1 fix)")
    ap.add_argument("--max-A", type=int, default=6,
                    help="Max A to evaluate (p(3A) cost grows fast)")
    ap.add_argument("--E0", type=float, default=E_0_CALIBRATION_MEV,
                    help="Calibration E_0 in MeV "
                         "(default = β-decay Q = 0.782)")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
        ("6Li",  3, 3, 32.0),
        ("7Li",  3, 4, 39.244529),
        ("9Be",  4, 5, 58.1650),
        ("10B",  5, 5, 64.750),
        ("12C",  6, 6, 92.161728),
    ]

    print("=" * 110)
    print("H_{3A} WEDDERBURN-CHARACTER BINDING — task-1 fix")
    print(f"q₀ = {Q0}")
    print(f"E_0 = {args.E0:.4f} MeV  (free-neutron β-decay Q, "
          f"hecke_core.E_0_CALIBRATION_MEV)")
    print(f"No ALPHA · Catalan anywhere.")
    print("=" * 110)

    results = []
    print(f"  {'Atom':>6} {'A':>3} {'3A':>3} {'p(3A)':>6} "
          f"{'|tr_M_atom|':>14} {'|tr_M_free|':>14} "
          f"{'B_pred':>10} {'B_AME':>9} {'|Δm/m|%':>9} {'time':>8}")
    print("  " + "-" * 108)
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        if A > args.max_A:
            continue
        t0 = time.time()
        try:
            r = binding_3A(Z, N, E_0=args.E0, verbose=args.verbose)
        except Exception as e:
            print(f"  {name:>6} {A:>3} {3*A:>3} ERR: {e}")
            continue
        dt = time.time() - t0
        M_total = A * 938.272
        dm = abs(r["B_MeV"] - B_AME) / M_total * 100
        print(f"  {name:>6} {A:>3} {3*A:>3} {r['n_partitions']:>6} "
              f"{abs(r['tr_M_atom']):>14.6e} "
              f"{abs(r['tr_M_free']):>14.6e} "
              f"{r['B_MeV']:>+10.4f} {B_AME:>9.3f} "
              f"{dm:>8.4f}% {dt:>7.2f}s")
        results.append({**r, "atom": name, "B_AME_MeV": B_AME,
                         "delta_m_over_m_pct": dm, "time_sec": dt})

    if results:
        dms = [r["delta_m_over_m_pct"] for r in results]
        print(f"\n|Δm/m|% summary:  min={min(dms):.4f}%, "
              f"max={max(dms):.4f}%, mean={sum(dms)/len(dms):.4f}%")

    witness = {
        "computation": "mass-at-3A-proper",
        "description": (
            "Task-1 fix: H_{3A} Wedderburn-character binding.  For "
            "each (Z, N), builds the full 3A-strand braid word and "
            "evaluates χ_λ(W) in the Hoefsmit seminormal basis for "
            "every λ ⊢ 3A.  Markov trace = Σ_λ w_λ · χ_λ / d_λ.  "
            "Binding = E_0 · (|tr_M_free| − |tr_M_atom|) with "
            "E_0 = 0.782 MeV (free-neutron β-decay Q).  NO "
            "ALPHA · Catalan anywhere.  p(3A) grows quickly; this "
            "module tops out near A = 10-12 via full enumeration."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "E_0_MeV": args.E0,
                        "max_A": args.max_A},
        "results": results,
    }
    out = Path(__file__).parent / "mass-at-3A-proper.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
