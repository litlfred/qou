"""
closed_form_tau_M.py — Phase 5q canonical closed form for tr_M(𝓑_K).

Combines the Phase 5c.1 + Phase 5l results into one shared utility:

  tr_M(𝓑_K)
  ──────────  =  ∏_{interface i ∈ ⋈_K} f_i(q)
  tr_M(𝓑_K^vac)

where each interface contributes a Markov-axiom factor f_i(q):

  - **positive** (σ_g, from p-p or simplified p-n):  f = z(q)
  - **negative** (σ_g^{-1}, from n-n):               f = z(q) - h(q)
  - **averaged** (σ_g - (h/2)·I, the canonical p-n
    form in `mass_at_3A_proper.atom_braid_word_3A`): f = z(q) - h(q)/2

with `z(q) = 1/(q^{1/2} + q^{-1/2})` (Markov parameter) and
`h(q) = q - q^{-1}` (Hecke skein parameter).

Combined with Phase 5l (`prop:constit-factor-tau-M-proton-identity`)
  tr_M(𝓑_K^vac) = tr_M^3(𝓑_p)^Z · tr_M^3(𝓑_n)^N

gives the full closed form

  tr_M(𝓑_K) = tr_M^3(𝓑_p)^Z · tr_M^3(𝓑_n)^N · ∏_i f_i(q).

This module exposes:
  - `markov_z(q)`, `hecke_h(q)` — primary parameters
  - `interface_factors(Z, N)` — symbolic per-interface factor list
  - `closed_form_ratio(Z, N, q)` — the ⋈_K-only ratio
  - `closed_form_tau_M(Z, N, q, tau_p, tau_n)` — full tr_M from
    the two H_3 building blocks

Ref: prop:interface-knot-markov-z.md (Phase 5c.1 interface identity)
Ref: prop:constit-factor-tau-M-proton-identity.md (Phase 5l constit identity)
Ref: docs/canonical-derivation-cheat-sheet.md §5 action #4
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Literal

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

InterfaceKind = Literal["positive", "negative", "averaged"]


def markov_z(q: mp.mpf) -> mp.mpf:
    """Markov parameter z(q) = 1 / (q^{1/2} + q^{-1/2})."""
    q = mp.mpf(q)
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def hecke_h(q: mp.mpf) -> mp.mpf:
    """Hecke skein parameter h(q) = q - q^{-1}."""
    q = mp.mpf(q)
    return q - 1 / q


def interface_factor(kind: InterfaceKind, q: mp.mpf) -> mp.mpf:
    """Per-interface Markov-axiom factor.

    kind ∈ {"positive", "negative", "averaged"}:
      positive : σ_g                  → z
      negative : σ_g^{-1}             → z - h
      averaged : σ_g - (h/2)·I        → z - h/2
    """
    z = markov_z(q)
    h = hecke_h(q)
    if kind == "positive":
        return z
    if kind == "negative":
        return z - h
    if kind == "averaged":
        return z - h / 2
    raise ValueError(f"unknown interface kind: {kind!r}")


def canonical_interface_kinds(Z: int, N: int) -> list[InterfaceKind]:
    """Interface kinds for the canonical atomic braid 𝓑_K.

    Mirrors `mass_at_3A_proper.atom_braid_word_3A`:
      - p-p boundary → positive (σ_g)
      - n-n boundary → negative (σ_g^{-1}, via skein)
      - p-n boundary → averaged (σ_g - (h/2)·I, the canonical
        Hecke-averaged choice for matter-antimatter symmetry)

    The ordering is protons-first then neutrons: K = p^Z n^N.
    """
    A = Z + N
    if A < 2:
        return []
    ordering: list[str] = ["p"] * Z + ["n"] * N
    kinds: list[InterfaceKind] = []
    for k in range(A - 1):
        nuc, next_nuc = ordering[k], ordering[k + 1]
        if nuc == "p" and next_nuc == "p":
            kinds.append("positive")
        elif nuc == "n" and next_nuc == "n":
            kinds.append("negative")
        else:
            kinds.append("averaged")
    return kinds


def closed_form_ratio(Z: int, N: int, q: mp.mpf) -> mp.mpf:
    """tr_M(𝓑_K) / tr_M(𝓑_K^vac) as a closed-form product.

    Iterates over the canonical interface kinds for atom (Z, N)
    and multiplies the Markov-axiom factors.
    """
    kinds = canonical_interface_kinds(Z, N)
    product = mp.mpf(1)
    for kind in kinds:
        product *= interface_factor(kind, q)
    return product


def closed_form_tau_M(
    Z: int, N: int, q: mp.mpf,
    tau_M_proton_H3: mp.mpf, tau_M_neutron_H3: mp.mpf,
) -> mp.mpf:
    """Full closed-form tr_M(𝓑_K) at q.

    Inputs are the two H_3 Markov-trace building blocks:
      - tr_M^3(𝓑_p, q) — the proton's H_3 trace
      - tr_M^3(𝓑_n, q) — the neutron's H_3 trace

    Output:
      tr_M(𝓑_K) = tr_M^3(𝓑_p)^Z · tr_M^3(𝓑_n)^N · ∏_i f_i(q).
    """
    constit_part = (mp.mpf(tau_M_proton_H3) ** Z
                    * mp.mpf(tau_M_neutron_H3) ** N)
    interface_part = closed_form_ratio(Z, N, q)
    return constit_part * interface_part


def interface_census(Z: int, N: int) -> dict[str, int]:
    """Counts of each interface kind in 𝓑_K."""
    kinds = canonical_interface_kinds(Z, N)
    return {
        "positive": sum(1 for k in kinds if k == "positive"),
        "negative": sum(1 for k in kinds if k == "negative"),
        "averaged": sum(1 for k in kinds if k == "averaged"),
        "total": len(kinds),
    }
