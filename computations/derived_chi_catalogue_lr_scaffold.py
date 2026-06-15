#!/usr/bin/env python3
"""derived_chi_catalogue_lr_scaffold.py — Tier 1 LR factorisation scaffold.

Provides the data structures, cross-validation harness, and a stub
implementation of the LR / parabolic factorisation described in
`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`.

## What this is

A SCAFFOLD — not a working LR implementation. The harness here:

  - parses an atomic braid `atom_braid_word_3A(Z, N)` into
    (intra-nucleon factors β_k, bridge generators b_k)
  - exposes the LR multi-coefficient `c^λ_{μ_1, ..., μ_A}` via
    `pyhecke_native.lr_coefficient`
  - provides a `chi_via_lr_factorisation(λ, factors, bridges, q)` stub
    that currently raises NotImplementedError
  - provides `cross_validate_lr_against_direct(λ, β, q)` that compares
    LR-output to direct `chi_q_via_gp`

This is the substrate for Phase 1.1 (deuteron base case): once the
bridge factor `ω_{μ_p, μ_n, λ}(q)` is rigorously derived (see audit
doc §5), drop it into the `_bridge_factor_omega` stub below and the
full pipeline lights up.

## How to extend

To implement Phase 1.1 (deuteron, A=2, n=6):

  1. Derive `ω_{μ_p, μ_n, λ}(q)` for all (μ_p, μ_n ⊢ 3, λ ⊢ 6).
     Per the audit doc, this is the trace of `ρ^λ(T_{b_0})` on the
     (μ_p, μ_n) LR bi-block weighted by LR multiplicity.

  2. Implement `_bridge_factor_omega(mu_left, mu_right, lam, q)` to
     return the precomputed ω as a q-Laurent.

  3. Implement `chi_via_lr_factorisation` for A=2 using the formula
     in audit §5.

  4. Run `cross_validate_lr_against_direct(λ, β_D, q)` for all 11
     partitions of 6. All must match → Phase 1.1 done.

  5. Extend recursively to A ≥ 3 per audit §6.2.

## Cross-validation harness

The harness compares LR-output to direct compute exactly. Both sides
use Rust pyhecke_native — no float drift to worry about. Either every
partition matches (Phase 1.1 success) or the discrepancy localises
the bridge-factor bug.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import pyhecke_native as ph  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


# ── Atomic-braid structural parse ──────────────────────────────────


@dataclass
class AtomicBraidDecomposition:
    """Parsed `atom_braid_word_3A(Z, N)` into per-nucleon factors +
    bridge generators per the LR factorisation roadmap.

    Per the audit doc §1: β_atom = β_0 · b_0 · β_1 · b_1 · ... · β_{A-1}
    where each β_k touches only strands {3k, 3k+1, 3k+2} and each
    b_k = σ_{3k+2} is a single bridge between adjacent nucleon blocks.
    """

    Z: int
    N: int
    A: int
    n_strands: int
    intra_words: list[list[tuple[int, int]]] = field(default_factory=list)
    """Per-nucleon intra-words, each in (sign, gen_1based) Rust format,
    indexed relative to the 3 strands of that nucleon (gen_1based ∈ {1, 2})."""
    bridge_generators: list[int] = field(default_factory=list)
    """Bridge crossing signs (±1) at positions b_k = σ_{3k+2}."""


def parse_atomic_braid(Z: int, N: int) -> AtomicBraidDecomposition:
    """Walk through `atom_braid_word_3A(Z, N)` and split the word into
    intra-nucleon factors + bridge generators.

    A crossing at gen_idx (0-based) belongs to:
      - intra nucleon k = gen_idx // 3, IF (gen_idx % 3) ∈ {0, 1}
      - bridge between k and k+1, IF (gen_idx % 3) == 2

    Per `mass_at_3A_proper.atom_braid_word_3A` source convention.
    """
    A = Z + N
    decomp = AtomicBraidDecomposition(
        Z=Z, N=N, A=A, n_strands=3 * A,
        intra_words=[[] for _ in range(A)],
        bridge_generators=[],
    )
    word_triples = atom_braid_word_3A(Z, N)
    for (c, _d, gen_0based) in word_triples:
        sign = 1 if c >= 0 else -1
        nucleon_idx = gen_0based // 3
        gen_in_nucleon = (gen_0based % 3) + 1  # 1-based: σ_1 or σ_2 within H_3
        if (gen_0based % 3) == 2 and nucleon_idx < A - 1:
            # Bridge between nucleon k and k+1
            decomp.bridge_generators.append(sign)
        else:
            # Intra-nucleon crossing on strands 3k, 3k+1, 3k+2 → σ_{gen_in_nucleon}
            # within the per-nucleon H_3.
            decomp.intra_words[nucleon_idx].append((sign, gen_in_nucleon))
    return decomp


# ── LR multi-coefficient via pyhecke_native ────────────────────────


def multi_lr_coefficient(
    lam: tuple[int, ...],
    mu_tuple: tuple[tuple[int, ...], ...],
) -> int:
    """Multi-LR coefficient `c^λ_{μ_1, ..., μ_A}` via iterated
    `pyhecke_native.lr_coefficient`.

    For A = 1: returns 1 iff lam == mu_tuple[0], 0 otherwise.
    For A = 2: returns lr_coefficient(lam, mu_tuple[0], mu_tuple[1]).
    For A ≥ 3: iterates by combining the last two μ's into all possible
    ν's via LR, then recurse on (lam, μ_1, ..., μ_{A-2}, ν).

    Returns an integer (the multiplicity).
    """
    if len(mu_tuple) == 1:
        return 1 if tuple(lam) == tuple(mu_tuple[0]) else 0
    if len(mu_tuple) == 2:
        return ph.lr_coefficient(list(lam), list(mu_tuple[0]), list(mu_tuple[1]))
    # Recurse: combine last two μ's via LR to get intermediate ν, sum over ν
    mu_last = mu_tuple[-1]
    mu_second_last = mu_tuple[-2]
    sub_lam_size = sum(mu_second_last) + sum(mu_last)
    nus = ph.partitions_of(sub_lam_size)
    total = 0
    for nu in nus:
        nu_tuple = tuple(nu)
        c_join = ph.lr_coefficient(list(nu), list(mu_second_last), list(mu_last))
        if c_join == 0:
            continue
        new_mu_tuple = (*mu_tuple[:-2], nu_tuple)
        c_rest = multi_lr_coefficient(lam, new_mu_tuple)
        total += c_join * c_rest
    return total


# ── Bridge factor ω — STUB ────────────────────────────────────────


def _bridge_factor_omega(
    mu_left: tuple[int, ...],
    mu_right: tuple[int, ...],
    lam: tuple[int, ...],
    q_value: object,
) -> list[tuple[int, str]]:
    """Bridge factor `ω_{μ_left, μ_right, λ}(q)`.

    STUB — derivation pending (audit doc Phase 1.1).

    The honest implementation: trace of `ρ^λ(T_b)` on the
    `(μ_left, μ_right)` LR bi-block, weighted by LR multiplicity.
    Derived from the Hecke quadratic relation acting on the boundary-
    strand pair.

    Returns: the q-Laurent representation as list of (q_degree, coeff_str).
    """
    raise NotImplementedError(
        "bridge factor ω derivation pending — see "
        "`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md` "
        "§5 (deuteron base case)."
    )


def chi_via_lr_factorisation(
    lam: tuple[int, ...],
    decomp: AtomicBraidDecomposition,
    q_value: object,
) -> list[tuple[int, str]]:
    """LR / parabolic factorisation entry point. Currently raises until
    Phase 1.1 lands.

    Per audit §5 (deuteron):

      χ^λ(T_β) = Σ_{μ_p, μ_n ⊢ 3} c^λ_{μ_p, μ_n}
                 · χ^{μ_p}(T_{β_p}) · χ^{μ_n}(T_{β_n})
                 · ω_{μ_p, μ_n, λ}(q)

    Per audit §6.2 (recursive A ≥ 3): same shape, applied recursively.
    """
    raise NotImplementedError(
        "LR factorisation Phase 1.1 (deuteron base case) implementation "
        "pending; bridge factor ω derivation is the gating step."
    )


# ── Cross-validation harness ───────────────────────────────────────


def cross_validate_lr_against_direct(
    lam: tuple[int, ...],
    Z: int, N: int,
    q_value: object,
) -> dict[str, object]:
    """Compute χ^λ both via direct `chi_q_via_gp` and via the
    LR-factorisation stub. Returns a dict for inspection."""
    decomp = parse_atomic_braid(Z, N)
    # Build the full rust_word and call chi_q_via_gp.
    from derived_chi_catalogue_sweep import production_braid_word_to_rust
    rust_word, _ = production_braid_word_to_rust(Z, N)
    direct_raw = ph.chi_q_via_gp(list(lam), decomp.n_strands, rust_word)
    direct = sorted((int(d), str(c)) for (d, c) in direct_raw)

    try:
        lr_result = chi_via_lr_factorisation(lam, decomp, q_value)
        lr_sorted = sorted(lr_result)
        match = lr_sorted == direct
    except NotImplementedError as exc:
        lr_sorted = None
        match = None
        return {
            "partition": lam,
            "Z": Z, "N": N, "A": decomp.A, "n_strands": decomp.n_strands,
            "direct_first3": direct[:3],
            "lr_first3": None,
            "match": None,
            "stub_status": str(exc),
        }
    return {
        "partition": lam,
        "Z": Z, "N": N, "A": decomp.A, "n_strands": decomp.n_strands,
        "direct_first3": direct[:3],
        "lr_first3": lr_sorted[:3],
        "match": match,
    }


# ── Smoke test on import ───────────────────────────────────────────


if __name__ == "__main__":
    # Verify the atomic-braid parse on Tritium.
    decomp = parse_atomic_braid(1, 2)
    print(f"Tritium parse:")
    print(f"  A = {decomp.A}, n_strands = {decomp.n_strands}")
    print(f"  intra_words per nucleon:")
    for k, w in enumerate(decomp.intra_words):
        print(f"    nucleon {k}: {len(w)} crossings, {w[:3]}...")
    print(f"  bridges: {decomp.bridge_generators}")

    # Multi-LR coefficient for trivial decomposition λ=(3) into ((3),):
    c1 = multi_lr_coefficient((3,), ((3,),))
    print(f"\n  c^(3)_{{(3)}} = {c1}  (expected: 1)")

    # Multi-LR for λ=(2,1) into ((2,), (1,)) — non-trivial LR.
    c2 = ph.lr_coefficient([2, 1], [2], [1])
    print(f"  c^(2,1)_{{(2), (1)}} = {c2}  (LR coefficient via Rust)")

    # Cross-validate ON DEUTERON λ=(2,1,1,1,1).
    result = cross_validate_lr_against_direct((2, 1, 1, 1, 1), 1, 1, None)
    print(f"\n  deuteron λ=(2,1,1,1,1) cross-validate: {result['stub_status'][:60]}...")
    print(f"  (direct chi_q_via_gp first 3 terms: {result['direct_first3']})")
