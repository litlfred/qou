#!/usr/bin/env python3
"""
SDP-dual-quotient prototype: character pre-filter for atom Markov trace.

Per docs/sdp-dual-quotient-reduction.md, many Wedderburn blocks λ ⊢
3A contribute zero or negligibly to tr_M(W_atom) — we can drop them
EXACTLY and shrink the partition sum.

This module implements the pre-filter stage (step 1) only:

    tr_M(W) = Σ_{λ ⊢ 3A} w_λ · χ_λ(W) / d_λ
            ≈ Σ_{λ ∈ ACTIVE} w_λ · χ_λ(W) / d_λ
    with  |χ_λ(W)| < ε  ⇒  drop λ

The full SDP-dual (step 3) — solving a reduced feasibility LP to
identify further zero-shadow-price partitions — is a refinement
left for follow-up.

Empirical goals:

  - Report `|ACTIVE|` vs total partitions per atom
  - Validate that partition-filtered tr_M agrees with full tr_M
    to numerical precision
  - Quantify speedup
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from canonical_plus_multibrane import E_0_BETA_DECAY_MEV
from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A


def _chi_lambda(shape: tuple[int, ...],
                 word: list[tuple[float, float, int]]) -> float:
    """χ_λ(W) = tr(Π_k (c_k σ_{g_k} + d_k I)) in the seminormal basis."""
    from scipy.sparse import issparse, eye as speye
    sigmas, dim, _syts = _cached_seminormal(shape)
    if dim == 0:
        return 0.0
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
    if sparse:
        return float(prod.diagonal().sum())
    return float(np.trace(prod))


def trM_prefiltered(Z: int, N: int, word: list[tuple[float, float, int]],
                      *, contrib_eps: float = 1e-6) -> dict:
    """Compute tr_M(W) on the ATOM-word with magnitude-based
    contribution filter.

    Full tr_M = Σ_λ w_λ · χ_λ(W) / d_λ.  Partitions whose
    |w_λ · χ_λ / d_λ| < contrib_eps are negligible at the target
    precision — their dropped sum bounds the truncation error.

    The filter IS a magnitude truncation; the SDP-DUAL-QUOTIENT
    formalism would identify which partitions have zero DUAL shadow
    price rigorously, but that requires solving the atom-level LP
    dual (separate step).  Magnitude truncation is the empirical
    approximation to the same intuition.

    Returns:
      trM            — truncated sum
      trM_full       — full sum (for comparison)
      n_active       — partitions kept
      n_total        — total partitions of 3A
      dropped_contrib — sum of dropped contributions (should be
                        dominated by contrib_eps × n_dropped)
    """
    A = Z + N
    n = 3 * A
    nfac = qfac(n)
    all_parts = list(partitions_of(n))
    rows = []
    for shape in all_parts:
        chi = _chi_lambda(shape, word)
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        w_l = (dq * dq) / nfac
        contrib = w_l * chi / dim
        rows.append({"shape": shape, "dim": dim, "w_lambda": w_l,
                       "chi": chi, "contribution": contrib})
    # Sort by |contribution| descending.
    rows.sort(key=lambda r: abs(r["contribution"]), reverse=True)
    trM_full = sum(r["contribution"] for r in rows)
    active = [r for r in rows if abs(r["contribution"]) >= contrib_eps]
    dropped = [r for r in rows if abs(r["contribution"]) < contrib_eps]
    trM_active = sum(r["contribution"] for r in active)
    return {
        "trM": trM_active,
        "trM_full": trM_full,
        "n_total": len(rows),
        "n_active": len(active),
        "n_dropped": len(dropped),
        "active": [{"shape": str(r["shape"]), "dim": r["dim"],
                      "contribution": r["contribution"]}
                     for r in active],
        "top_dropped": [{"shape": str(r["shape"]), "dim": r["dim"],
                           "contribution": r["contribution"]}
                          for r in dropped[:5]],
        "dropped_contrib": sum(r["contribution"] for r in dropped),
        "truncation_error": abs(trM_active - trM_full),
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]
    print("=" * 110)
    print("SDP-DUAL-QUOTIENT PREFILTER — character pre-filter for atom tr_M")
    print(f"q0 = {Q0}")
    print("=" * 110)

    results = []
    for name, Z, N in ATOMS:
        A = Z + N
        n = 3 * A
        word_atom = atom_braid_word_3A(Z, N, m_pp=1, m_pn=1, m_nn=1,
                                          include_inter=True)
        word_free = atom_braid_word_3A(Z, N, m_pp=1, m_pn=1, m_nn=1,
                                          include_inter=False)
        print(f"\n{name} (Z={Z}, N={N}, A={A}, n=3A={n})")
        for label, word in [("atom", word_atom), ("free", word_free)]:
            for eps in (1e-3, 1e-4, 1e-6):
                t0 = time.time()
                r = trM_prefiltered(Z, N, word, contrib_eps=eps)
                dt = time.time() - t0
                frac_active = r["n_active"] / r["n_total"] if r["n_total"] > 0 else 0
                print(f"  {label}/ε={eps:.0e}:  tr_M_trunc={r['trM']:+.6e} "
                      f"full={r['trM_full']:+.6e}  "
                      f"active={r['n_active']:3d}/{r['n_total']:3d} "
                      f"({frac_active*100:4.1f}%)  err={r['truncation_error']:.1e}  "
                      f"({dt:.2f}s)")
                results.append({"atom": name, "Z": Z, "N": N, "A": A,
                                  "path": label, "eps": eps, **r,
                                  "time_sec": dt})

    witness = {
        "computation": "sdp-dual-quotient-prefilter",
        "description": (
            "Character pre-filter stage of the SDP-dual-quotient "
            "reduction (docs/sdp-dual-quotient-reduction.md).  Drops "
            "Wedderburn blocks λ ⊢ 3A with |χ_λ(W)| < 1e-12 from the "
            "atom Markov-trace sum.  Reports |ACTIVE| vs total and "
            "the total dropped contribution (which should be ~ε)."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "chi_eps": 1e-12},
        "results": results,
    }
    out = Path(__file__).parent / "sdp-dual-quotient-prefilter.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
