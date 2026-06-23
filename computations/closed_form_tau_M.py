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

**At the substrate H_{3A} level (where this module operates)**: the
substrate quark-flavor split δ = (m_n − m_p) / M_N is available via
`flavor_split_subleading(q)` (PR #690, prop:flavor-split-substrate).
The `pn_convention` choices are:

  - "bring_color_weighted" (DEFAULT, 2026-06-01): quaternionic
    color-tube weighting of the p-n interface using the substrate-
    derived δ.  This IS the categorically-canonical convention
    (Bring's 3-color-tube structure on the modular Belyi cover)
    and IS derived (uses PR #690 substrate split, no fitted
    quark masses).  Net interface factor:
      f_pn = z − h · (1/2 − δ/4)
    vs the uniform (strict-averaged): f_pn = z − h/2.
    Effect at q₀: per-interface correction ≈ 7e-5; small but
    categorical (substrate-pure).
  - "chi_lambda_braid": matches the OLD production marshalling
    which drops the averaging entirely, treating p-n as positive σ.
    Retained for backward compatibility with pre-2026-06-01 scripts.
  - "strict_averaged": uses σ - (h/2)·I, the uniform bar-invariant
    projection (no flavor split — abelian (ℤ/2)³ approximation).

History: the default switched 2026-06-01 from "chi_lambda_braid" to
"bring_color_weighted" per the owner directive "when canonical /
derived, bring should be default across the compute".  The
bring_color_weighted convention was previously documented as
"queued research task; not implemented in Phase 5q" — that
docstring is now obsolete (the convention is implemented and IS
the canonical/derived choice).

Ref: prop:interface-knot-markov-z.md (Phase 5c.1 interface identity)
Ref: prop:constit-factor-tau-M-proton-identity.md (Phase 5l constit identity)
Ref: prop:averaging-resonance-rule.md (categorical σ_avg = σ - h/2 definition)
Ref: probe_pn_flavor_asymmetry.py (Bring-surface flavor-weighted averaging)
Ref: probe_per_sheet_flavor_nonin.py (per-sheet Picard-Lefschetz integration)
Ref: docs/canonical-derivation-cheat-sheet.md §5 action #4
Ref: docs/audits/2026-06-01-bring-color-weighted-implementation-and-compute-audit.md

## Derivation of the per-interface factors (categorical, 0 free params)

The three factors below are NOT independent heuristics: positive=z is the
Markov axiom tr(alpha sigma)=z tr(alpha); negative=z-h and averaged=z-h/2
follow by trace-linearity from that SINGLE Markov move plus the Hecke skein
sigma^{-1}=sigma-h.  The averaged (bar-invariant p-n) factor's division-free
form tr(alpha (sigma+sigma^{-1}))=(2z-h) tr(alpha) is Lean-proved sorry-free as
`QOU.BraidKnot.interface_knot_markov_z_bar_symmetric`
(content/quantum-observable-universe/mass-theory/interface-knot-markov-z.lean),
and `interface_factor()` below is cross-checked against the derived z, z-h,
z-h/2 by
`computations/probes/interface_factor_categorical_derivation_probe.py`.

Ref: QOU.BraidKnot.interface_knot_markov_z_bar_symmetric (Lean: averaged pn factor derived)
Ref: prop:interface-knot-markov-z §"Averaged (bar-invariant) interface"
Ref: computations/probes/interface_factor_categorical_derivation_probe.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
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
    pn_convention: PnConvention = "bring_color_weighted",
) -> list[InterfaceKind]:
    """Interface kinds for the canonical atomic braid 𝓑_K.

    Three conventions for the p-n boundary:

      - "bring_color_weighted" (DEFAULT, 2026-06-01 — canonical/derived):
          Quaternionic color-tube weighting using the substrate-derived
          δ = (m_n − m_p) / M_N from `flavor_split_subleading(q)`
          (PR #690, prop:flavor-split-substrate — substrate-pure,
          no fitted quark masses).  Net p-n interface factor (applied
          downstream in `closed_form_ratio` / `closed_form_tau_M`):
            f_pn = z − h·(1/2 − δ/4)
          For LABEL purposes returned here, the p-n kind is `"averaged"`
          (same as strict_averaged); the δ-aware factor is applied at
          the value-computation layer, not in the labels.

      - "chi_lambda_braid" (legacy production marshalling):
          p-n is marshalled as positive σ in the chi_lambda_braid
          pipeline.  `chi_lambda_braid` itself only takes
          `(sign, gen)` pairs; the averaged → σ simplification lives
          in the marshalling layer
          (`canonical_braid_marshalling.marshal_to_chi_lambda_braid`,
          which maps `(c=1, d=-h/2)` → `(sign=+1, gen)` and silently
          drops the -h/2 coefficient).  This is what the 4 production
          tr_M scripts compute prior to migration.  **Phase 5q witness
          validates the closed form against the empirical slow path
          to 1e-49 at all four anchor atoms (D, T, ³He, ⁴He) under
          this convention — `closed-form-tau-M-verification-phase5q.witness.json`.**

      - "strict_averaged" (math-correct, audit only — δ-degenerate):
          p-n uses (σ_g - (h/2)·I) which gives factor (z - h/2).
          Same as bring_color_weighted with δ = 0 (no flavor split).
          Phase 5q confirmed this **alternative** convention disagrees
          with the legacy chi_lambda_braid production marshalling by
          ~21% relative for atoms with at least one p-n interface —
          i.e. this is the gap between the literal averaging generator
          and what production marshalling actually computes, NOT a
          gap between the closed form and production.  Use this only
          when probing the marshalling-bug audit trail; the
          bring_color_weighted convention adds δ on top.

          See `docs/audits/2026-05-25-phase5q-closed-form-reconciliation.md`
          for the full convention map.

    Mirrors `mass_at_3A_proper.atom_braid_word_3A` interface logic:
      - p-p boundary → positive (σ_g)
      - n-n boundary → negative (σ_g^{-1}, via Hecke skein)
      - p-n boundary → depends on convention (see above)

    The ordering is protons-first then neutrons: K = p^Z n^N.
    """
    if pn_convention == "bring_color_weighted":
        # Quaternionic color-tube-weighted averaging at p-n interfaces.
        #
        # The interface KIND labels alone cannot encode the δ-weighted
        # asymmetric factor — the full δ-aware computation lives in
        # `closed_form_ratio` and `closed_form_tau_M` below, which
        # take q and apply z - h·(1/2 - δ/4) for the p-n interface.
        # Here we return the same label list as "strict_averaged"
        # (kinds = "averaged" for p-n) so downstream label-only
        # consumers (witness metadata, symbolic Habiro extraction
        # using chi_lambda_braid marshalling) do not crash on the
        # new default.
        A = Z + N
        if A < 2:
            return []
        ordering_list: list[str] = ["p"] * Z + ["n"] * N
        kinds_weighted: list[InterfaceKind] = []
        for k_idx in range(A - 1):
            nuc, next_nuc = ordering_list[k_idx], ordering_list[k_idx + 1]
            if nuc == "p" and next_nuc == "p":
                kinds_weighted.append("positive")
            elif nuc == "n" and next_nuc == "n":
                kinds_weighted.append("negative")
            else:  # p-n: asymmetric averaging (δ-aware factor applied in closed_form_ratio)
                kinds_weighted.append("averaged")
        return kinds_weighted
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
    pn_convention: PnConvention = "bring_color_weighted",
) -> mp.mpf:
    """tr_M(𝓑_K) / tr_M(𝓑_K^vac) as a closed-form product.

    Iterates over the canonical interface kinds for atom (Z, N)
    and multiplies the Markov-axiom factors.

    For pn_convention="bring_color_weighted": the p-n interface
    factor is z - h·(1/2 - δ/4) where δ = Δm/M_N (substrate-pure
    from flavor_split_subleading). This replaces the uniform
    z - h/2 with a quaternionically-weighted per-color-tube
    asymmetry.
    """
    if pn_convention == "bring_color_weighted":
        from _li_2_q_util import flavor_split_subleading
        z = markov_z(q)
        h = hecke_h(q)
        delta_m_over_M = flavor_split_subleading(q)
        A = Z + N
        if A < 2:
            return mp.mpf(1)
        ordering_list: list[str] = ["p"] * Z + ["n"] * N
        product = mp.mpf(1)
        for k_idx in range(A - 1):
            nuc, next_nuc = ordering_list[k_idx], ordering_list[k_idx + 1]
            if nuc == "p" and next_nuc == "p":
                product *= z
            elif nuc == "n" and next_nuc == "n":
                product *= z - h
            else:
                # Q₈-weighted p-n: asymmetric 50/50 ± δ/4
                product *= z - h * (mp.mpf(1) / 2 - delta_m_over_M / 4)
        return product

    kinds = canonical_interface_kinds(Z, N, pn_convention=pn_convention)
    product = mp.mpf(1)
    for kind in kinds:
        product *= interface_factor(kind, q)
    return product


def closed_form_tau_M(
    Z: int, N: int, q: mp.mpf,
    tau_M_proton_H3: mp.mpf, tau_M_neutron_H3: mp.mpf,
    pn_convention: PnConvention = "bring_color_weighted",
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


def compute_tau_M_nucleon_H3(
    nucleon: Literal["p", "n"],
    q_val: mp.mpf,
    dps: int = 50,
) -> mp.mpf:
    """tr_M^3(𝓑_nucleon, q) — H_3 Markov trace of the canonical
    proton or neutron braid via the y_λ · χ_λ pipeline.

    Centralised helper for the H_3 building blocks consumed by
    `closed_form_tau_M(Z, N, q, tau_p, tau_n)`.  Replaces three
    near-identical inline definitions across
      - `closed_form_tau_M_verification_phase5q.py`
      - `rho_constit_equals_tau_M_proton_phase5l.py`
      - `tau_M_proton_closed_form_phase5l1.py`
    (last two via thin wrappers; the verification script now imports).

    Compute path:
      1. Marshal _PROTON_G0/G1 (or _NEUTRON_G0/G1) chain to (sign, gen)
         via the standard `canonical_braid_marshalling` helper.
      2. Sum y_λ(q) · χ_λ(word) over partitions of 3 (= 3 partitions).

    At mpfr-50-dps this is cheap (sub-second per nucleon, no H_n>3
    machinery involved).
    """
    import mpmath as mp_local  # noqa: F401 (already imported above)
    # Imports kept local to avoid top-level cycle if a consumer of
    # closed_form_tau_M is itself imported by hecke_characters.
    from hecke_characters import chi_lambda_braid, partitions_of
    from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric
    from canonical_braid_marshalling import marshal_to_chi_lambda_braid
    from hecke_core import (
        _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    )
    from q_parameter import Q as Q0

    if nucleon == "p":
        g0, g1 = _PROTON_G0, _PROTON_G1
    elif nucleon == "n":
        g0, g1 = _NEUTRON_G0, _NEUTRON_G1
    else:
        raise ValueError(f"nucleon must be 'p' or 'n', got {nucleon!r}")

    h_val = float(Q0 - 1 / Q0)  # noqa: I8 — sign-classification param for marshal_to_chi_lambda_braid (matched vs d within eps=1e-10), not a precision coefficient
    chain_with_gens = (
        [(c, d, 0) for c, d in g0]
        + [(c, d, 1) for c, d in g1]
    )
    word = marshal_to_chi_lambda_braid(chain_with_gens, h_val)
    q_str = mp.nstr(q_val, dps, strip_zeros=False)
    # Per Copilot PR #1080 review: dps is authoritative — derive the
    # chi_lambda_braid precision tag from it instead of hardcoding
    # "mpfr_50dps", so a caller requesting (say) dps=100 gets a fully
    # 100-dps pipeline.  chi_lambda_braid requires dps >= 50 in mpfr
    # mode; enforce that bound here.
    if dps < 50:
        raise ValueError(
            f"compute_tau_M_nucleon_H3 requires dps >= 50 (got {dps}); "
            f"chi_lambda_braid mpfr mode is calibrated at 50+ dps."
        )
    precision_tag = f"mpfr_{dps}dps"
    total = mp.mpf(0)
    for lam in partitions_of(3):
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        chi = chi_lambda_braid(lam, word, q_value=q_str,
                                precision=precision_tag)
        total += y * mp.mpf(str(chi))
    return total


def interface_census(
    Z: int, N: int,
    pn_convention: PnConvention = "bring_color_weighted",
) -> dict[str, int]:
    """Counts of each interface kind in 𝓑_K."""
    kinds = canonical_interface_kinds(Z, N, pn_convention=pn_convention)
    return {
        "positive": sum(1 for k in kinds if k == "positive"),
        "negative": sum(1 for k in kinds if k == "negative"),
        "averaged": sum(1 for k in kinds if k == "averaged"),
        "total": len(kinds),
    }
