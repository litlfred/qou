#!/usr/bin/env python3
"""
Partition cancellation diagnostic for atom Markov trace.

The atom tr_M is a NEAR-CANCELLATION sum:

    tr_M(atom) = Σ_λ w_λ · χ_λ(W_atom) / d_λ  ≈  10^{-4}

while each individual term is ~10^{-2}.  This diagnostic exposes
the cancellation STRUCTURE — which partitions contribute positive,
which negative, and how they pair up — without any truncation.

Outputs per atom:

  1. Ranked list of per-partition contributions (positive + negative,
     sorted by magnitude).
  2. Cumulative sum by rank — shows how the near-zero total is
     assembled.
  3. Sign-conjugate pairing: if λ and λ' (transpose) have opposite-
     sign contributions of similar magnitude, it's evidence for a
     symmetric/antisymmetric cancellation structure.
  4. Same for χ_λ(atom) − χ_λ(free): per-partition contribution to
     BINDING (= tr_M(free) − tr_M(atom)).  Partitions where the two
     characters agree cancel from binding; partitions where they
     disagree ARE the binding physics.
"""
from __future__ import annotations

import sys
import json
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A


def _chi_lambda(shape, word):
    """χ_λ(W) = tr(Π_k (c σ_g + d I)) seminormal."""
    from scipy.sparse import issparse, eye as speye
    sigmas, dim, _ = _cached_seminormal(shape)
    if dim == 0:
        return 0.0, dim
    sparse = bool(sigmas) and issparse(sigmas[0])
    if sparse:
        prod = speye(dim, format='csr')
        I = speye(dim, format='csr')
    else:
        prod = np.eye(dim)
        I = np.eye(dim)
    for (c, d, g) in word:
        if g < len(sigmas):
            prod = prod @ (c * sigmas[g] + d * I)
    chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
    return chi, dim


def transpose_partition(shape):
    """Return the conjugate (transposed) partition."""
    if not shape:
        return ()
    max_row = shape[0]
    return tuple(sum(1 for r in shape if r > c) for c in range(max_row))


def diagnose_atom(Z: int, N: int) -> dict:
    A = Z + N
    n = 3 * A
    nfac = qfac(n)
    word_atom = atom_braid_word_3A(Z, N, m_pp=1, m_pn=1, m_nn=1,
                                      include_inter=True)
    word_free = atom_braid_word_3A(Z, N, m_pp=1, m_pn=1, m_nn=1,
                                      include_inter=False)

    rows = []
    for shape in partitions_of(n):
        chi_a, dim = _chi_lambda(shape, word_atom)
        if dim == 0:
            continue
        chi_f, _ = _chi_lambda(shape, word_free)
        dq = dim_q(shape)
        if dq == 0:
            continue
        w_l = (dq * dq) / nfac
        contrib_atom = w_l * chi_a / dim
        contrib_free = w_l * chi_f / dim
        contrib_binding = w_l * (chi_f - chi_a) / dim
        rows.append({
            "shape": tuple(shape), "shape_str": str(tuple(shape)),
            "dim": dim, "w_lambda": w_l,
            "chi_atom": chi_a, "chi_free": chi_f,
            "contrib_atom": contrib_atom,
            "contrib_free": contrib_free,
            "contrib_binding": contrib_binding,
            "sign_atom": "+" if contrib_atom >= 0 else "-",
            "sign_free": "+" if contrib_free >= 0 else "-",
        })

    tot_atom = sum(r["contrib_atom"] for r in rows)
    tot_free = sum(r["contrib_free"] for r in rows)
    tot_binding = sum(r["contrib_binding"] for r in rows)

    # Rank by |contrib_atom|.
    rows.sort(key=lambda r: abs(r["contrib_atom"]), reverse=True)

    # Sign split
    pos_atom = [r for r in rows if r["contrib_atom"] > 0]
    neg_atom = [r for r in rows if r["contrib_atom"] < 0]
    sum_pos = sum(r["contrib_atom"] for r in pos_atom)
    sum_neg = sum(r["contrib_atom"] for r in neg_atom)

    # Conjugate pairing: find λ' = transpose(λ) pairs and compare.
    by_shape = {r["shape"]: r for r in rows}
    pairings = []
    seen = set()
    for shape, r in by_shape.items():
        if shape in seen:
            continue
        conj = transpose_partition(shape)
        if conj != shape and conj in by_shape:
            r2 = by_shape[conj]
            pairings.append({
                "shape_a": str(shape), "shape_b": str(conj),
                "contrib_a": r["contrib_atom"],
                "contrib_b": r2["contrib_atom"],
                "sum": r["contrib_atom"] + r2["contrib_atom"],
            })
            seen.add(shape); seen.add(conj)
        else:
            seen.add(shape)

    return {
        "atom": f"Z={Z}N={N}", "Z": Z, "N": N, "A": A, "n": n,
        "n_partitions": len(rows),
        "tr_M_atom": tot_atom, "tr_M_free": tot_free,
        "tr_M_binding_diff": tot_binding,
        "sum_positive_atom": sum_pos, "sum_negative_atom": sum_neg,
        "net_atom_via_positive_negative": sum_pos + sum_neg,
        "n_positive": len(pos_atom), "n_negative": len(neg_atom),
        "top5_by_magnitude": rows[:5],
        "bottom5_by_magnitude": rows[-5:],
        "conjugate_pairings": pairings,
    }


def print_summary(d: dict):
    print(f"\n═══ {d['atom']}  A={d['A']}  n={d['n']}  "
          f"{d['n_partitions']} partitions ═══")
    print(f"  tr_M_atom       = {d['tr_M_atom']:+.6e}")
    print(f"  tr_M_free       = {d['tr_M_free']:+.6e}")
    print(f"  tr_M_free − atom = {d['tr_M_binding_diff']:+.6e}")
    print(f"  Σ(positive atom terms) = {d['sum_positive_atom']:+.6e}  "
          f"({d['n_positive']} partitions)")
    print(f"  Σ(negative atom terms) = {d['sum_negative_atom']:+.6e}  "
          f"({d['n_negative']} partitions)")
    sum_magnitudes = d['sum_positive_atom'] - d['sum_negative_atom']
    cancel_ratio = abs(d['tr_M_atom']) / sum_magnitudes if sum_magnitudes > 0 else 0
    print(f"  cancellation ratio     = "
          f"|tr_M| / Σ|terms| = {cancel_ratio:.2e}")
    print(f"\n  Top-5 partitions by |contrib_atom|:")
    for r in d['top5_by_magnitude']:
        print(f"    {r['shape_str']:28s} dim={r['dim']:4d}  "
              f"w={r['w_lambda']:.3e}  χ_atom={r['chi_atom']:+.3e}  "
              f"contrib_atom={r['contrib_atom']:+.3e}")
    print(f"\n  Conjugate pairings (λ vs λ'):")
    # Rank pairings by |sum|
    pairs = sorted(d['conjugate_pairings'], key=lambda p: abs(p['sum']))
    for p in pairs[:5]:
        tied = "✓ CANCEL" if abs(p['sum']) < 0.1 * max(abs(p['contrib_a']),
                                                             abs(p['contrib_b']))\
            else ""
        print(f"    {p['shape_a']:18s} ({p['contrib_a']:+.3e}) "
              f"↔ {p['shape_b']:18s} ({p['contrib_b']:+.3e})  "
              f"sum = {p['sum']:+.3e}  {tied}")


if __name__ == "__main__":
    ATOMS = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]

    print("=" * 110)
    print("PARTITION CANCELLATION DIAGNOSTIC")
    print(f"q0 = {Q0}")
    print("=" * 110)

    results = []
    for name, Z, N in ATOMS:
        d = diagnose_atom(Z, N)
        d["atom"] = name
        print_summary(d)
        results.append(d)

    witness = {
        "computation": "partition-cancellation-diagnostic",
        "description": (
            "Diagnostic for the near-cancellation structure of the "
            "atom Markov trace.  Ranks per-partition contributions, "
            "splits positive vs negative, and examines conjugate "
            "(transpose) pairing: λ ↔ λ' contributions that sum to "
            "~0 are evidence for sym/antisym cancellation.  Non-zero "
            "pair sums identify the partitions where binding "
            "physics lives."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0},
        "results": results,
    }
    out = Path(__file__).parent / "partition-cancellation-diagnostic.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
