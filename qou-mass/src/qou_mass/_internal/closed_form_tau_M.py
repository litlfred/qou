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

with `z(q) = q^3 / (q^2 + 1)` (Markov parameter, registry convention **D**)
and `h(q) = q - q^{-1}` (Hecke skein parameter).

OWNER RULING 2026-08-09 excised convention **C**, `z = 1/(q^{1/2} +
q^{-1/2})`, which this header documented until 2026-08-15. Reading C off
this docstring rather than off `markov_z` below is a **23% error**
(0.4993203 vs 0.6126880 at q_0). `markov_z`'s own docstring carries the
forcing argument and the registry pointers — it is authoritative; this
header is a summary of it.

Combined with Phase 5l (`constit-factor-tau-M-proton-identity`)
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
`flavor_split_leading(q)` (PR #690, prop:flavor-split-substrate; the
2026-06-29 de-wire moved this off the POSITED subleading form).
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
Ref: `constit-factor-tau-M-proton-identity` (Phase 5l constit identity)
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
(folio/quantum-observable-universe/mass-theory/interface-knot-markov-z.lean),
and `interface_factor()` below is cross-checked against the derived z, z-h,
z-h/2 by
`computations/probes/interface_factor_categorical_derivation_probe.py`.

Ref: QOU.BraidKnot.interface_knot_markov_z_bar_symmetric (Lean: averaged pn factor derived)
Ref: prop:interface-knot-markov-z §"Averaged (bar-invariant) interface"
Ref: computations/probes/interface_factor_categorical_derivation_probe.py

Retired-label note: a block named above with a backticked stem and no
`prop:`/`conj:` prefix has NO carrier in folio/ — it was demoted to
_deprecated/ and is recorded in docs/audits/2026-10-11-retired-label-records.md §A,
with the statement it carried and the command to recover its content.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Literal

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

InterfaceKind = Literal["positive", "negative", "averaged", "averaged_weighted"]
PnConvention = Literal["chi_lambda_braid", "strict_averaged", "bring_color_weighted"]


def markov_z(q: mp.mpf) -> mp.mpf:
    """Markov parameter z(q) = q^3 / (q^2 + 1) — registry convention **D**.

    OWNER RULING 2026-08-09: convention C excised. This returned C's
    `1/(q^{1/2} + q^{-1/2}) = 0.4993203` until then; it now returns D's
    `q^3/(q^2+1) = 0.6126880`.

    The selection is FORCED, not stipulated. `lem:feynman-eigenbasis-
    decomposition` puts the row cap `ell(lambda) <= 2` in the mass channel's own
    decomposition (V = the fundamental of SU_q(2)), so `y_(1^3) = 0`; given that,
    `QOU.BraidsAndKnots.MarkovTraceTLUniqueness.
    markovWeights_eq_jones_of_threeRow_eq_zero` (sorry-free) makes the faithful
    normalised Markov trace unique and equal to `q^3/(q^2+1)`. The competing root
    `z = q` is degenerate (`y_(2,1) = 0`, not faithful on TL_3).

    NOT decided by which value matches experiment. For the record it does NOT
    flatter the binding table: mean |err| over {2H,3H,3He,4He,6Li,7Li} moves
    37.39% -> 43.85%. It does fix 2H (+74.85% -> +27.36%) and, structurally, the
    deuteron stops being unreachable — under C, AME sits 30.4% below the whole
    admissible band; under D it is inside it.

    Registry: docs/coordination/trace-convention-registry.md.
    Forcing: docs/audits/2026-08-08-mass-fibre-dimension-forces-convention-d.md.
    """
    q = mp.mpf(q)
    return q ** 3 / (q ** 2 + 1)


def hecke_h(q: mp.mpf) -> mp.mpf:
    """Hecke skein parameter h(q) = q - q^{-1}."""
    q = mp.mpf(q)
    return q - 1 / q


def trM_sigma1_sq(q: mp.mpf) -> mp.mpf:
    """tr_M(sigma_1^2) = h*z + 1, for any n >= 2.

    Follows from the Hecke quadratic sigma^2 = h*sigma + 1 and tr_M(sigma) = z;
    it holds for ANY Markov parameter, which is exactly why it belongs here in
    terms of `markov_z` rather than being written out.

    ## Why this function exists

    This identity was copy-pasted, specialised to convention C, into at least
    five places:

        knot_operator_census_group_actions.trM_sigma1_sq   1 + (q-1)/sqrt(q)
        c_3_categorical_derivation_attempt.trM_hopf        1 + (q-1)/sqrt(q)
        lepton_t2n_torus_tower.trM_hopf_census_form        1 + (q-1)/sqrt(q)
        inter_nucleon_linked_channel.census_hopf           1 + (Q0-1)/sqrt(Q0)
        tools/sage-examples/.../hecke_surface.trace_weights (via a local z)

    `1 + (q-1)/q^{1/2}` IS `h*z + 1` evaluated at z_C -- the square root is
    z_C's, not the identity's. So when z moved to D every copy silently went on
    describing the excised convention, and the sage example's guard
    (`assert abs(TR_M[1] - z) < 1e-9`) started failing while the rest just
    returned wrong numbers quietly.

    A local copy of a library value is the whole defect class. One definition,
    gated by R11 in the trace-convention registry, is the fix.
    """
    q = mp.mpf(q)
    return hecke_h(q) * markov_z(q) + 1


def wenzl_weights_h2(q: mp.mpf) -> tuple:
    """H_2(q) Wedderburn weights (y_(2), y_(1,1)), solved from the axioms.

    tr_M(1) = y_(2) + y_(1,1) = 1 and tr_M(sigma_1) = y_(2)*q - y_(1,1)/q = z
    give y_(2) = (q*z + 1)/(q^2 + 1) and y_(1,1) = 1 - y_(2), for any z.

    The convention-C specialisation of this is
    `(q^{3/2} + q + 1)/(q^3 + q^2 + q + 1)`, which is what
    `lepton_t2n_torus_tower.wenzl_weights` hardcoded (twice -- once numerically
    and once in sympy, and the two were migrated separately, so for one commit
    they disagreed and the file's own symbolic-vs-numeric assertion caught it).
    The q^{3/2} is z_C's square root showing through a formula that has none of
    its own.
    """
    q = mp.mpf(q)
    y2 = (q * markov_z(q) + 1) / (q ** 2 + 1)
    return y2, 1 - y2


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
    *,
    weighted_labels: bool = False,
) -> list[InterfaceKind]:
    """Interface kinds for the canonical atomic braid 𝓑_K.

    Three conventions for the p-n boundary:

      - "bring_color_weighted" (DEFAULT, 2026-06-01 — canonical/derived):
          Quaternionic color-tube weighting using the substrate-derived
          δ = (m_n − m_p) / M_N from `flavor_split_leading(q)`
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
        #
        # THAT DEFAULT IS A TRAP FOR ANY CONSUMER THAT APPLIES ITS OWN
        # FACTOR. Asking for the canonical convention and then mapping the
        # returned labels through a three-kind {positive, negative,
        # averaged} dispatch yields z - h/2 — the colour-BLIND factor —
        # while the caller believes it is canonical. It cannot be caught by
        # an equality test against "averaged_weighted", because that label
        # is never emitted; it fails by returning a slightly smaller number
        # rather than by raising. Measured live in
        # `probes/binding_closed_form_C_vs_D_probe.py::interface_factor`.
        #
        # `weighted_labels=True` opts into the full vocabulary, emitting
        # "averaged_weighted" for the p-n interface so such a consumer either
        # handles the weighting or raises on an unknown kind. It is opt-in
        # precisely so the label-only consumers above keep working.
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
                kinds_weighted.append(
                    "averaged_weighted" if weighted_labels else "averaged")
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
    from flavor_split_leading). This replaces the uniform
    z - h/2 with a quaternionically-weighted per-color-tube
    asymmetry.
    """
    if pn_convention == "bring_color_weighted":
        # DE-WIRED 2026-06-29 (owner directive): canonical color-weighting δ
        # uses the PROVEN leading flavor split, not the posited (1+ℏ_q³)-
        # corrected subleading (unproven, 76%-insufficient — see audit
        # 2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md).
        from _li_2_q_util import flavor_split_leading
        z = markov_z(q)
        h = hecke_h(q)
        delta_m_over_M = flavor_split_leading(q)
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

    TRACE CONVENTION: **convention D** — SU(2)/Temperley-Lieb (Jones),
    z = q^3/(q^2+1) (`markov_z` above), weights from
    `y_lambda_wenzl_bridge_numeric`, y_(1^3) = 0. Both the binding and the
    mass channel are now D; convention C (the full-Hecke Ocneanu / Wenzl
    z-trace, z = 1/(q^{1/2}+q^{-1/2}), y_(1^3) != 0) was excised by owner
    ruling 2026-08-09. Registry:
    docs/coordination/trace-convention-registry.md.

    This docstring said **C** until 2026-08-09 while `markov_z` had already
    returned D since 33a6c7aa, and `y_lambda_wenzl_bridge_numeric` was still
    C until bean qou-wgta item 3 — so the declaration, the interface and the
    constituent were three different answers. All three are D now.

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
    *,
    intra_order: Literal["borromean", "grouped"] = "borromean",
) -> mp.mpf:
    """tr_M^3(𝓑_nucleon, q) — H_3 Markov trace of the canonical
    proton or neutron braid via the y_λ · χ_λ pipeline.

    ⚠ **ORDERING CORRECTED 2026-09-06** (bean `qou-y2o7`, owner decision).
    Until now this built its own nucleon word as *all gen 0, then all gen 1* —
    the **grouped** ordering — and it did so because it used
    `chi_monotone_transfer.chi_all_lambda`, the monotone-ONLY kernel. The
    2026-09-05 ruling (`qou-hu1f`) makes the canonical intra-nucleon core
    **borromean**, `(σ₀σ₁⁻¹)³`, which is non-monotone by construction:

        grouped   gen sequence [0,0,0,0,0,0,0,1,1,1,1]   τ_p 1.1457596924573009
        canonical gen sequence [0,1,0,1,0,1,0,0,1,0,0]   τ_p 0.6293284022029219

    So this was not a stale value a re-run would fix — the function *could not
    express* the canonical word while it used that kernel. It satisfied the
    kernel's precondition by building the wrong braid, and therefore never
    raised: it returned a plausible 50-dps number in the superseded ordering.
    That silence is why three separate sweeps missed it (the `qou-hu1f` witness
    sweep, `binding_canonical`, and `qou-cvky`'s population of files that raise
    on a non-monotone word).

    `intra_order="grouped"` reproduces the old word exactly, for producers that
    must reproduce a grouped-era artifact. It is a **historical escape hatch,
    not a choice**: the default is the ruling, and a caller passing `grouped`
    should say why at its call site.

    Compute path:
      1. Take the canonical word from `mass_at_3A_proper.atom_braid_word_3A`
         (or, under `intra_order="grouped"`, rebuild the legacy
         `_PROTON_G0/G1` chain), carrying `d` through unchanged.
      2. Sum y_λ(q) · χ_λ(word) over partitions of 3 (= 3 partitions),
         with χ via `chi_general_word.chi_all_lambda_any`.

    At mpfr-50-dps this is cheap (sub-second per nucleon, no H_n>3
    machinery involved).

    Centralised helper for the H_3 building blocks consumed by
    `closed_form_tau_M(Z, N, q, tau_p, tau_n)`.  Replaces three
    near-identical inline definitions across
      - `closed_form_tau_M_verification_phase5q.py`
      - `rho_constit_equals_tau_M_proton_phase5l.py`
      - `tau_M_proton_closed_form_phase5l1.py`
    (last two via thin wrappers; the verification script now imports).

    (The compute path is stated above, under the ordering correction.)

    🛑 **This used to marshal through `marshal_to_chi_lambda_braid` and was
    WRONG by 15.3 % (proton) / 27.3 % (neutron)** — fixed 2026-08-26, bean
    `qou-qu2w`. That marshaller "emits signs and drops `d` entirely" (its own
    docstring) and maps `averaged → sign=+1`. Each nucleon chain carries TWO
    `averaged` crossings — intra-nucleon, nothing to do with a p-n interface.
    Censused with `canonical_braid_crossings.classify_crossing`, which is the
    module that owns the ctype vocabulary (this file deliberately does not
    re-list it; its own `InterfaceKind` is a separate, interface-level
    vocabulary — see `interface_factor`):

        proton   6 positive, 2 averaged, 3 inverse
        neutron  5 positive, 2 averaged, 4 inverse

    so the flattening replaced that crossing's Markov factor `z − h/2` by `z`
    at two sites per nucleon. The marshaller's defence — "equally lossy for
    both variants, which is why the collapse is correct *here*" — is about
    `averaged` vs `averaged_weighted` and does not license `averaged → sigma`.

    **This was not a convention question, which is why it survived every
    convention audit.** Both paths are convention D, and A=1 has no p-n
    interface, so no `pn_convention` argument reaches this site — this
    function correctly takes none. Anything keyed on `pn_convention` is
    structurally blind here.

    The fixed values reproduce `habiro-coefficients-atomic.witness.json`
    (τ_p = 1.14575969245730087, τ_n = 0.987743688115809572) to ~1e-50; the
    old ones missed it by the factors above, and squared into the 2.157×
    disagreement between `habiro-coefficients-helium-4` and
    `atomic-tr-m-helium4-canonical`. Measured in
    `probes/nucleon_h3_marshalling_divergence_probe.py`.
    """
    # Imports kept local to avoid top-level cycle if a consumer of
    # closed_form_tau_M is itself imported by hecke_characters.
    from hecke_characters import partitions_of
    from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric
    from chi_general_word import chi_all_lambda_any

    if nucleon not in ("p", "n"):
        raise ValueError(f"nucleon must be 'p' or 'n', got {nucleon!r}")
    if intra_order not in ("borromean", "grouped"):
        raise ValueError(
            f"intra_order must be 'borromean' (canonical) or 'grouped' "
            f"(historical), got {intra_order!r}")

    if dps < 50:
        raise ValueError(
            f"compute_tau_M_nucleon_H3 requires dps >= 50 (got {dps}); "
            f"the character path is calibrated at 50+ dps."
        )

    q_mp = mp.mpf(q_val)
    if intra_order == "borromean":
        # The word comes FROM ITS PRODUCER. That is the substance of this fix:
        # a future ordering ruling now reaches this function by changing one
        # default in `atom_braid_word_3A`, instead of silently not reaching it.
        from mass_at_3A_proper import atom_braid_word_3A
        word = atom_braid_word_3A(*((1, 0) if nucleon == "p" else (0, 1)),
                                  q=q_mp)
    else:
        # HISTORICAL. The pre-2026-09-05 word, rebuilt from the hecke_core
        # chains exactly as this function used to build it unconditionally:
        # (c, d, gen) with all gen 0 then all gen 1. `d` is carried through as
        # mpf — it IS the crossing, and dropping it is the defect this
        # function used to have (see the marshalling note above).
        from hecke_core import (
            _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
        )
        g0, g1 = ((_PROTON_G0, _PROTON_G1) if nucleon == "p"
                  else (_NEUTRON_G0, _NEUTRON_G1))
        # Via the named helper rather than the concatenation written out. This
        # branch was ALREADY correct — opt-in, defaulted off, documented above
        # — but it was spelled exactly like the sixteen sites that are not, so
        # `intra_ordering_structural_assembly_audit` could only list it beside
        # them. Calling `grouped_word_from_chains` states in code what the
        # docstring states in prose. Output identical: the helper IS this
        # concatenation, and the mpf conversion is preserved per chain.
        from pyhecke.atom import grouped_word_from_chains
        word = grouped_word_from_chains(
            [(mp.mpf(str(c)), mp.mpf(str(d))) for c, d in g0],
            [(mp.mpf(str(c)), mp.mpf(str(d))) for c, d in g1],
        )

    # `chi_all_lambda_any`, not `chi_monotone_transfer.chi_all_lambda`: the
    # canonical word is NON-MONOTONE and the monotone transfer cannot accept
    # it. Same signature; dispatches on the word's own generator sequence, so
    # the grouped branch above still takes the monotone route. At H_3 the
    # general path costs nothing (d_λ ≤ 2) and is in fact ~290x FASTER here —
    # 0.0023 s against 0.669 s — because it needs no transfer set-up at this
    # size. Same routing `qou-cvky` applied to its 11 monotone-kernel callers.
    #
    # `q=q_val` explicitly: the trace and the representation are then built
    # at ONE q. The previous implementation classified crossing signs against
    # the module-level `q_parameter.Q` while tracing at the caller's `q_val`
    # — a pin straddle that was harmless only because every caller happened
    # to pass the same value.
    chi = chi_all_lambda_any(word, 3, dps=dps, q=q_mp)
    total = mp.mpf(0)
    for lam in partitions_of(3):
        y = y_lambda_wenzl_bridge_numeric(lam, q_val, dps=dps)
        total += y * chi.get(tuple(lam), mp.mpf(0))
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
