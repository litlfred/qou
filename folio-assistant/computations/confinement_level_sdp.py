#!/usr/bin/env python3
"""
Infrastructure: level-agnostic SDP over the knot-operator basis.

Standard procedure when working across any confinement level
(quark → hadron → nuclear → atomic):

  1. Each "strand" (quark, nucleon, atom, etc.) carries a
     torus-knot operator T_{r,s} chosen from a finite canonical basis.
  2. Inter-strand interactions are flavor-dependent Hecke crossings
     (c, d, gen) tuples.
  3. SDP picks the per-strand operator tuple that minimizes |tr_M|
     (least-action / ground-state configuration), subject to the
     Frobenius demand-supply constraint (automatic for real Hecke
     words by prop:frobenius-auto-feasibility).

This module exports:
  KNOT_OPERATORS      — canonical ordered list
  knot_operator_word(op, base_gen) — exact Hecke braid word
  build_level_word(ops, flavors, crossing_fn, gluon_base_gens)
                      — compose full braid from per-strand ops
  level_sdp(n_strands, flavors, crossing_fn, label)
                      — run SDP over all operator tuples, return
                        (optimal, dual_gaps, per-candidate tr_M).

The pattern is reused by:
  electron_knot_operator_sdp.py — atomic level (electrons in Z-atom)
  m_proton_knot_sdp.py          — quark level (quarks in proton)
  [future] hadron_bond_sdp.py   — hadron level (hadron bonds in nucleus)
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path
from typing import Callable, Sequence

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
from mass_at_3A_proper import _cached_seminormal
from hecke_characters import partitions_of, dim_q, qfac
from sdp_decision import sdp_decide, SdpDecisionReport

HA = q0 - qi0  # h = q - q^{-1}


# ── Canonical knot-operator basis ──────────────────────────────────────────
KNOT_OPERATORS = ["T_1_0", "T_2_1", "T_2_2", "T_2_3", "T_2_5"]
"""Torus-knot operators T_{r,s} as Hecke braid words.

    T_{1,0}  empty word         — identity (no interaction)
    T_{2,1}  σ_j                — single crossing
    T_{2,2}  σ_j²               — Hopf link / gluon
    T_{2,3}  σ_j σ_{j+1} σ_j    — trefoil / electron
    T_{2,5}  (σ_j σ_{j+1})² σ_j — cinquefoil / muon

Each operator is a bounded Jones polynomial value on every irrep,
so χ_λ(T)/dim_λ stays in a compact set — unlike arbitrary σ^n
powers which amplify χ outside the convergence radius of Φ_q.
"""


def knot_operator_word(op: str, base_gen: int) -> list[tuple[float, float, int]]:
    """Exact Hecke braid word (c, d, gen) for a torus-knot operator."""
    if op == "T_1_0":
        return []
    if op == "T_2_1":
        return [(1.0, 0.0, base_gen)]
    if op == "T_2_2":
        return [(1.0, 0.0, base_gen), (1.0, 0.0, base_gen)]
    if op == "T_2_3":
        return [(1.0, 0.0, base_gen),
                (1.0, 0.0, base_gen + 1),
                (1.0, 0.0, base_gen)]
    if op == "T_2_5":
        return [(1.0, 0.0, base_gen), (1.0, 0.0, base_gen + 1),
                (1.0, 0.0, base_gen), (1.0, 0.0, base_gen + 1),
                (1.0, 0.0, base_gen)]
    raise ValueError(f"unknown knot operator: {op}")


def knot_op_strands_needed(op: str) -> int:
    """Number of strands the operator occupies (for base_gen placement)."""
    return {"T_1_0": 1, "T_2_1": 2, "T_2_2": 2, "T_2_3": 3, "T_2_5": 3}[op]


# ── Level-agnostic braid composition ──────────────────────────────────────
def build_level_word(per_strand_ops: Sequence[str],
                     flavors: Sequence[int],
                     crossing_fn: Callable[[int, int], tuple[float, float]],
                     strand_anchors: Sequence[int] | None = None
                     ) -> list[tuple[float, float, int]]:
    """Compose braid word for one confinement level.

    per_strand_ops : e.g. ["T_2_2", "T_2_2", "T_2_3"] for uud quark level
    flavors        : flavor id per strand (e.g. [U, U, D])
    crossing_fn    : (flavor_i, flavor_j) → (c, d) for the σ_i generator
                     in the inter-strand crossing
    strand_anchors : base_gen for each strand's operator (default:
                     auto-place with room for largest T_{r,s})

    Returns flat list of (c, d, gen) tuples forming the full braid.
    """
    n = len(per_strand_ops)
    if strand_anchors is None:
        # Linear layout: strand s at gen s * 2 (leaves room for T_{2,3})
        strand_anchors = [2 * s for s in range(n)]

    word: list[tuple[float, float, int]] = []
    # 1) Per-strand operator segments
    for s, op in enumerate(per_strand_ops):
        word.extend(knot_operator_word(op, strand_anchors[s]))
    # 2) Inter-strand flavor crossings
    for i in range(n):
        for j in range(i + 1, n):
            c, d = crossing_fn(flavors[i], flavors[j])
            # Place crossing at the boundary gen between strand i and j
            boundary = max(strand_anchors[i], 0) + 1  # simple heuristic
            if i + 1 == j:
                boundary = strand_anchors[j] - 1
                if boundary < 0: boundary = 0
            word.append((c, d, boundary))
    return word


def tr_M_plancherel(word: list[tuple[float, float, int]], n_strands: int) -> float:
    """Plancherel-weighted Markov trace of a Hecke word at H_{n_strands}(q).

    tr_M(w) = Σ_λ (d_q(λ)² / [n]_q!) · χ_λ(w) / dim_V_λ
    """
    from scipy.sparse import issparse, eye as speye
    nfac = qfac(n_strands)
    tr = 0.0
    for shape in partitions_of(n_strands):
        sigmas, dim_irrep, _ = _cached_seminormal(shape)
        if dim_irrep == 0:
            continue
        dq = dim_q(shape)
        if dq == 0:
            continue
        sparse = bool(sigmas) and issparse(sigmas[0])
        if sparse:
            prod = speye(dim_irrep, format='csr')
            I = speye(dim_irrep, format='csr')
        else:
            prod = np.eye(dim_irrep)
            I = np.eye(dim_irrep)
        for (c, d, g) in word:
            if g < len(sigmas):
                prod = prod @ (c * sigmas[g] + d * I)
        chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
        w = (dq * dq) / nfac
        tr += w * chi / dim_irrep
    return tr


# ── Level-agnostic SDP ─────────────────────────────────────────────────────
def level_sdp(n_strands: int,
              flavors: Sequence[int],
              crossing_fn: Callable[[int, int], tuple[float, float]],
              label: str = "",
              candidate_ops: list[str] | None = None,
              strand_anchors: Sequence[int] | None = None,
              objective: str = "min_abs_trM",
              ) -> tuple[tuple[str, ...], SdpDecisionReport]:
    """Run SDP over all per-strand knot-operator assignments.

    objective:
      "min_trM"       — minimize signed tr_M (sdp_decide default)
      "min_abs_trM"   — minimize |tr_M|, the on-shell / ground-state
                         configuration (physical default)

    Returns the optimal operator tuple + full SDP report with dual gaps.
    """
    n_particles = len(flavors)
    ops = candidate_ops or KNOT_OPERATORS

    # Enumerate all tuples (|ops|^n_particles candidates)
    candidates = []
    for assignment in itertools.product(ops, repeat=n_particles):
        word = build_level_word(list(assignment), flavors, crossing_fn,
                                strand_anchors)
        name = "+".join(assignment)
        candidates.append((name, word))

    if objective == "min_abs_trM":
        # On-shell / ground-state candidate
        def compute_trM(w, n):
            return abs(tr_M_plancherel(w, n))
    elif objective == "max_abs_trM":
        # Mass-carrying excited configuration (sdp_decide argmin → negate)
        def compute_trM(w, n):
            return -abs(tr_M_plancherel(w, n))
    else:
        def compute_trM(w, n):
            return tr_M_plancherel(w, n)

    rep = sdp_decide(candidates=candidates, n_strands=n_strands,
                     compute_trM=compute_trM, label=label)
    optimal_tuple = tuple(rep.optimal_name.split("+"))
    return optimal_tuple, rep


if __name__ == "__main__":
    # Self-test: proton at quark level (uud)
    U, D = 1, 0
    def flavor_crossing(fi, fj):
        if fi == U and fj == U: return (1.0, 0.0)
        if fi == D and fj == D: return (1.0, -HA)
        return (1.0, -HA/2.0)

    print("="*80)
    print("SELF-TEST: Proton (uud) at quark level via knot-operator SDP")
    print("="*80)
    optimal, rep = level_sdp(
        n_strands=6,   # 3 quarks × 2 strands per op
        flavors=[U, U, D],
        crossing_fn=flavor_crossing,
        label="proton-uud-quark-level"
    )
    print(f"Optimal operator tuple: {optimal}")
    print(f"Optimal tr_M           : {rep.optimal_trM:+.6e}")
    print(f"Number of candidates   : {rep.n_candidates}")
    print(f"LP status              : {rep.lp_status}")
    print(f"\nTop-5 candidates by tr_M:")
    sorted_trM = sorted(rep.trM_by_candidate.items(), key=lambda x: abs(x[1]))
    for name, t in sorted_trM[:5]:
        print(f"  {name:<40}  tr_M={t:+.6e}  gap={rep.dual_gaps[name]:+.6e}")
