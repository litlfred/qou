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

## Open: Bring color-tube weighted averaging (Phase 5q audit)

The "averaged" interface factor here is the BAR-INVARIANT PROJECTION
  σ_avg = (σ + σ^{-1})/2 = σ - (h/2)·I
i.e. a UNIFORM 50/50 average of σ and σ^{-1}.  This is the convention
documented in
  - `mass_at_3A_proper.atom_braid_word_3A` (the canonical builder)
  - `averaging-resonance-rule.md` (the categorical definition)
  - `bar-involution.md` (the bar-symmetric structure)

Per the **owner's intuition** (recorded in
`probe_pn_flavor_asymmetry.py` and `probe_per_sheet_flavor_nonin.py`
docstrings — "we are missing some asymmetry in proton, neutron... color
tubes are different for each so averaging / integration along Bring's
surface not the same"), the truly canonical averaging at the p-n
interface should reflect the **3-color-tube structure** of each nucleon
on Bring's surface:

  - proton (uud) carries color tubes (μ_u, μ_u, μ_d) on sheets c_1,c_2,c_3
  - neutron (udd) carries (μ_u, μ_d, μ_d)
  - the p-n boundary averages over the 3·3 = 9 color-pair assignments,
    weighted by quark content — NOT a uniform σ-vs-σ^{-1} 50/50.

The empirical probe (`probe_pn_flavor_asymmetry.py` Scheme 4) confirms
the sum-weighted per-quark average reproduces Δm_{n-p} to ~0.14% of
CODATA via the Bring-surface integration.  This is at the MASS level
(downstream of tr_M).

**At the substrate H_{3A} level (where this module operates)**: quark
mass μ_u, μ_d info is NOT present, so the Bring color-tube weighting
cannot be applied algebraically here without an upstream input.
The current `pn_convention` choices are:

  - "chi_lambda_braid" (DEFAULT): matches production marshalling
    which drops the averaging entirely, treating p-n as positive σ.
  - "strict_averaged": uses σ - (h/2)·I, the uniform bar-invariant
    projection.

A future `pn_convention="bring_color_weighted"` would require the
extension of the closed form to take quark-mass inputs and apply the
sum-weighted average derived in `probe_per_sheet_flavor_nonin.py`.
**This is a queued research task; not implemented in Phase 5q.**

For the production-tr_M-migration (Action 4), the chi_lambda_braid
default is correct because production scripts use the simplified σ
marshalling.  Any future migration to a quark-mass-aware tr_M would
need to extend BOTH this module and the production pipelines.

Ref: prop:interface-knot-markov-z.md (Phase 5c.1 interface identity)
Ref: prop:constit-factor-tau-M-proton-identity.md (Phase 5l constit identity)
Ref: prop:averaging-resonance-rule.md (categorical σ_avg = σ - h/2 definition)
Ref: probe_pn_flavor_asymmetry.py (Bring-surface flavor-weighted averaging)
Ref: probe_per_sheet_flavor_nonin.py (per-sheet Picard-Lefschetz integration)
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
PnConvention = Literal["chi_lambda_braid", "strict_averaged", "bring_color_weighted"]


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


def canonical_interface_kinds(
    Z: int, N: int,
    pn_convention: PnConvention = "chi_lambda_braid",
) -> list[InterfaceKind]:
    """Interface kinds for the canonical atomic braid 𝓑_K.

    Two conventions for the p-n boundary:

      - "chi_lambda_braid" (DEFAULT, matches production):
          p-n is marshalled as positive σ in the chi_lambda_braid
          pipeline.  `chi_lambda_braid` itself only takes
          `(sign, gen)` pairs; the averaged → σ simplification lives
          in the marshalling layer
          (`canonical_braid_marshalling.marshal_to_chi_lambda_braid`,
          which maps `(c=1, d=-h/2)` → `(sign=+1, gen)` and silently
          drops the -h/2 coefficient).  This is what the 4 production
          tr_M scripts compute.

      - "strict_averaged" (math-correct, audit only):
          p-n uses (σ_g - (h/2)·I) which gives factor (z - h/2).
          Phase 5q confirmed this convention disagrees with the
          production pipeline by ~21% relative for atoms with at
          least one p-n interface.  Use this only when probing the
          marshalling-bug audit trail; do NOT use it for the closed
          form that production scripts validate against.

    Mirrors `mass_at_3A_proper.atom_braid_word_3A` interface logic:
      - p-p boundary → positive (σ_g)
      - n-n boundary → negative (σ_g^{-1}, via Hecke skein)
      - p-n boundary → depends on convention (see above)

    The ordering is protons-first then neutrons: K = p^Z n^N.
    """
    if pn_convention == "bring_color_weighted":
        raise NotImplementedError(
            "Bring color-tube weighted averaging at the p-n interface "
            "requires quark-mass inputs (μ_u, μ_d) per nucleon and a "
            "per-sheet color assignment.  See `probe_per_sheet_flavor_nonin.py` "
            "and `probe_pn_flavor_asymmetry.py` for the empirical "
            "derivation at the mass level (sum-weighted scheme matches "
            "CODATA Δm to ~0.14%).  Implementing this at the substrate "
            "H_{3A} level — where this module operates — requires extending "
            "the closed form to accept quark-mass inputs and apply the "
            "9-way color-pair-weighted average at p-n boundaries.  "
            "Tracked as a Phase 5q open R&D item per the cheat sheet."
        )
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
        else:  # p-n
            if pn_convention == "strict_averaged":
                kinds.append("averaged")
            else:
                kinds.append("positive")
    return kinds


def closed_form_ratio(
    Z: int, N: int, q: mp.mpf,
    pn_convention: PnConvention = "chi_lambda_braid",
) -> mp.mpf:
    """tr_M(𝓑_K) / tr_M(𝓑_K^vac) as a closed-form product.

    Iterates over the canonical interface kinds for atom (Z, N)
    and multiplies the Markov-axiom factors.
    """
    kinds = canonical_interface_kinds(Z, N, pn_convention=pn_convention)
    product = mp.mpf(1)
    for kind in kinds:
        product *= interface_factor(kind, q)
    return product


def closed_form_tau_M(
    Z: int, N: int, q: mp.mpf,
    tau_M_proton_H3: mp.mpf, tau_M_neutron_H3: mp.mpf,
    pn_convention: PnConvention = "chi_lambda_braid",
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
    interface_part = closed_form_ratio(
        Z, N, q, pn_convention=pn_convention
    )
    return constit_part * interface_part


def interface_census(
    Z: int, N: int,
    pn_convention: PnConvention = "chi_lambda_braid",
) -> dict[str, int]:
    """Counts of each interface kind in 𝓑_K."""
    kinds = canonical_interface_kinds(Z, N, pn_convention=pn_convention)
    return {
        "positive": sum(1 for k in kinds if k == "positive"),
        "negative": sum(1 for k in kinds if k == "negative"),
        "averaged": sum(1 for k in kinds if k == "averaged"),
        "total": len(kinds),
    }
