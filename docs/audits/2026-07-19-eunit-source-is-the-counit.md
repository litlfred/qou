# `E_unit`'s source is the counit — resolving the "external/scale-free" over-claim

**Date:** 2026-07-19 · **Branch:** `claude/counit-mu0-nastokes-eunit-2026-07-19` (PR #4102) ·
**Axis:** Δ_λ binding magnitude — the `E_unit` dimensional anchor · **Owner steer:**
*"E_unit — go back to the canonical cheat sheet. Where does it come from? co-unit? Follow
(co)units through NA-Stokes in cat action. μ₀ first order only? Resolve the 'external' issues."*
**Tier:** structural tracing (scope-(a); no fit; nothing wired).

## 0. The question

Merged #4093/#4101 isolated `E_unit ≈ 0.996 MeV` (the deuteron `B = √5·E_unit·ladder` unit) as the
one remaining dimensional open, and the reeb provenance §2h.2 labelled it **"external / scale-free —
no internal QOU scale matches to better than ~2.6%."** The owner's steer: that verdict missed the
counit.

## 1. The counit *is* proved and in the paper

The per-crossing weight `(q − q⁻¹)` is the **antisymmetric Hecke-generator eigenvalue difference =
skein `L₊ − L₋` = counit-character difference** — and it is corpus-canonical, not new:

- `climax-volume-mass/crossing-energy-categorical-origin.md`: `(q, −q⁻¹)` are the two Hecke
  generator eigenvalues on `S²V ⊕ Λ²V`, **forced** by the rigid monoidal structure.
- `crossing-energy-intro.md`: `𝔈_cross = strong baseline + Q·(q − q⁻¹)`, `Q = ½(n₊ − n₋)` the
  Coulomb charge; `def:coulomb-charge` introduces `h = q − q⁻¹`.
- `commutative-crossing-energy.md`: at `q = 1`, `q − q⁻¹` vanishes; the categorical `√λ_₋ = i`
  structure is the same square-root that gives the `√5` ceiling.
- `categorical-action.lean`: the categorical action carries `matter = unit ≫ counit`.

So the *q-structure* of the energy — the counit `(q − q⁻¹)` — is proved and in the paper.

## 2. The counit **does** supply a derived MeV scale — `μ₀` (which §2h.2 omitted)

The dimensional bridge divides the τ-functor scale `m_e` by the deuteron pn-pair's **3-crossing net
counit energy** `3(q − q⁻¹)` (`observations/crossing-energy-interpretation.md`: `3(q−q⁻¹) = 0.630`
skein units):

  **`μ₀ = m_e / (3(q − q⁻¹)/2) ≈ 1.6295 MeV`**  — cheat-sheet line 237, **derived, 0 free params**,

and the deuteron rotational energy `E_rot = μ₀·ℏ_q·J_q²(3) = 2.020 MeV` (AME `2.2246`, **−9.2%**).
The §2h.2 candidate sweep (`2m_e`, `m_e[2]_v`, `E_0/[2]_v²`, `Q_β`) **did not include `μ₀`** —
that is the omission. `E_unit`'s **source is internal (the counit), not external.**

## 3. Resolving "external" (the re-scope)

§2h.2's route (i) — *"an external ~1 MeV scale the framework does not canonically contain"* — is
**withdrawn** (annotated in place, original retained): the framework *does* contain a counit-derived
per-crossing scale (`μ₀`), and route (ii) (the "A-flattened counit variant" of §2f) **is this same
object**. The exchange sector *in isolation* is scale-free — that part stands — but the counit
sector (equally internal) carries the dimension via `m_e`.

**What is actually open** is not the *existence* of an internal scale but its **accuracy**:

- **`μ₀` is first-order in `(q − q⁻¹)`** (the owner's "μ₀ first order only?" — yes). It uses the
  leading antisymmetric counit combination; the full crossing energy is
  `𝔈 = baseline + Q·(q − q⁻¹) + …` (higher holonomy orders). The deuteron **−9.2%** is the size of
  the missing higher-order (co)unit terms.
- The two deuteron forms — `μ₀`-rotational (derived, −9%) and `5g·E_unit` (+0.4%,
  `E_unit = 0.611·μ₀`) — use the **same** counit `(q − q⁻¹)` structure at different dimensional
  realizations and have **never been unified**.

## 4. The route (owner steer: follow (co)units through NA-Stokes)

Closing the derived-scale form to the 5g-form's +0.4% is a **higher-order (co)unit expansion**: trace
the counit through Step 3 of the canonical chain — `𝐂 categorical action → Yekutieli non-abelian
Stokes → 𝐇_n(q)` — where the first-order holonomy gives `μ₀·(q−q⁻¹)` and the surface-ordered
(NA-Stokes) higher orders give the `−9% → +0.4%` correction. This audit does **not** perform that
expansion; it **relocates the open** from "find an external ~1 MeV unit" (a scan, forbidden by the
§2e entropy bound) to "derive the higher-order counit/NA-Stokes terms of an internal, first-order
scale `μ₀`" — a formalize-first target, not a search. `E_unit` is **not** closed; the anti-laundering
rule stands (no axiom/class carrying it counts as a derivation).

Refs: probe [`eunit_counit_mu0_tracing_probe.py`](../../computations/deltalambda/eunit_counit_mu0_tracing_probe.py); cheat sheet lines 213/237;
`climax-volume-mass/crossing-energy-*`; `observations/crossing-energy-interpretation.md`;
`categorical-action.lean`; reeb provenance §2f/§2h.2 (scope-corrected); merged #4101 cluster-expansion
§4.
