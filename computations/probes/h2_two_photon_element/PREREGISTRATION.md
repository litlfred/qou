# Pre-registration: the H₂ bond as a two-photon element

Written 2026-11-21, before any number in this directory was computed. Issue #8879.
Route 4 of the options put to the owner on the `prop:ilp-covalent-bond` thread (owner chose
"1 then 4").

## Why

`computations/probes/h2_ruled_electron` tested the bond one **monomial** at a time: each
non-identity term of the photon `γ_s(φ) = 1 + φ₀σ_s + φ₁σ_{s+1} + φ₀₁·V_s`, `V_s = σ_sσ_{s+1}⁻¹`,
on its own, so that no `φ` was chosen. Reading 3 then passes for 37 (`pe`) / 32 (`ep`) of 155
bonds, and does not select one.

An absorbed photon is not a monomial; it is the element `γ_s(φ)`. The corpus fixes some of its
coefficients by a proved identity, the factorisation of the Borromean core

    V³ = γ(0, 0, qh) · γ(0, 0, −q⁻¹h),     h = q − q⁻¹

(`borromeanV3A_eq_switched_photon_product` and its `B` twin, sorry-free). Those theorems are
proved on the `(2,1)` weight spaces; the identity is `V³ = 1 + h²V − h²V²`, which also holds on
the two one-dimensional blocks (`V ↦ 1` there), so it holds in `H₃(q)` and in every `H_n(q)`
through the windows. Check C1 tests it numerically in `H₁₂`. This probe tests reading 3 on the
**elements** built from photons whose coefficients are fixed that way, and on nothing else.

## What is fixed (taken from the corpus, not chosen)

- Everything in `h2_ruled_electron/PREREGISTRATION.md` that is not about the bond: nucleon `V^m`,
  `m ∈ {3, 6}`; electron `σ₀σ₁σ₀`; six-strand atoms with no p–e or junction letter; atom 1 `pe`,
  atom 2 `pe` or `ep`; reading 3 under convention D at the proton pin `q₀`, every level 1…12;
  mpmath 40 dps, `TOL = 1e-25`; the code of `h2_one_rule` / `h2_gg_atom` reused unchanged.
- **Photon coefficients.** Only `φ₀ = φ₁ = 0`, `φ₀₁ ∈ {qh, −q⁻¹h}`: the two photons of the
  factorisation. `φ₀` and `φ₁` are fixed by nothing in the corpus, so elements with `σ` terms
  are not tested; that is reported as a gap, not filled.

## The elements (10 per cell)

Write `γ_s^a = γ_s(0, 0, a) = 1 + a·V_s`, `a ∈ {qh, −q⁻¹h}`, `s ∈ {4, 5}`.

1. **One photon** `γ_s^a`: 4 elements.
2. **Two photons, one window** `γ_s^{qh}·γ_s^{−q⁻¹h}`, `s ∈ {4, 5}`: 2 elements. By the
   factorisation each equals `V_s³`. This is the calibration (check C1).
3. **Two photons, two windows** `γ_s^a·γ_{s'}^b`, `s ≠ s'`, `(a, b) ∈ {(qh, −q⁻¹h), (−q⁻¹h, qh)}`,
   both orders: 4 elements, `= 1 + aV_s + bV_{s'} + ab·V_sV_{s'}`.

Characters are linear, so each element's level characters are the same linear combination of
the monomial characters `χ(x)`, `χ(xV_s)`, `χ(xV_sV_{s'})`, `χ(xV_s³)`, each computed by the
existing engine.

## Checks

- **C1.** The one-window element's characters equal those of `V_s³` (max difference `< 1e-30`
  relative to the largest character), at every level, every cell.
- **C2.** The monomial `V_s³` rows agree with `h2-ruled-electron.witness.json` to its printed
  20 digits.

## Reported for each (cell, element)

Reading 3 at every level, the failing levels, the negative characters, and the trace ratio
`tr(x·E)/tr(x)` (reported, never used to select).

## Outcomes, fixed before computing

- **(i)** Only the one-window two-photon elements pass (equivalently `V_s³`). The two-photon
  element then selects `V³`, at either site.
- **(ii)** A two-window two-photon element also passes. The element test does not select a
  single site pattern; the passing set is reported.
- **(iii)** A one-photon element passes. Reported in full; a single absorbed photon then
  bonds, which the monomial test did not find.

## Priors (stated before computing)

- **P1 (99 %).** C1 holds and the one-window elements pass (they are `V³`).
- **P2 (60 %).** No one-photon element passes (no single cut-crossing monomial passed).
- **P3 (45 %).** No two-window element passes.
- So outcome (i) at about 30 %.

## Not done here

Elements with `σ` terms (needs `φ₀, φ₁`, which nothing fixes); three or more photons; other `q`;
the trefoil backup electron. Nothing is wired into the content block.
