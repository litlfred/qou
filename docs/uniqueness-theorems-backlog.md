# Uniqueness theorems backlog — pre-publication

> Queued per owner direction (2026-05-29, #1422 thread): every "canonical X"
> claim in the QOU framework must be backed by a *proved uniqueness theorem*
> before publication / production. This document is the tracked backlog.

The QOU mass derivation chain (see [`canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md))
asserts that several constructions are "canonical" — meaning *uniquely
determined* by the framework axioms. For each, a Lean uniqueness theorem
must accompany the construction before the framework can claim derivation
without external choice.

## Status table

| # | Construction | Cheat-sheet line | Current status | Uniqueness theorem needed |
|---|---|---|---|---|
| 1 | **τ_M Markov trace** on H_n(R, q) | line 234 (`[jones1987]` cited) | Lean theorem currently selection-by-contrast with τ_SW; SW purge in flight (this PR) | `tau_M_unique_nondegenerate` — *any* non-degenerate Frobenius form on H_n(R, q) equals τ_M. Axiom class: `MarkovTraceUniqueness` citing [wenzl1990] / [jones1987]. **In progress (#1422).** |
| 2 | **T_w SDP-canonical knot operator** | line 69, 95 | Explicitly `conj:canonical-knot-id-sdp` (a conjecture) | `T_w_unique_sdp` — the joint mass-tower SDP has a unique optimum; the active set + dual variables identify a unique T_w. Likely requires Slater's condition + strict complementarity + a strong-duality + unique-optimum proof for the SDP class. |
| 3 | **Canonical p-n averaging form** | line 124, 128 | "Open audit finding" — current production uses uniform bar-invariant; owner intuition is Bring color-tube weighted | `pn_averaging_unique` — any p-n averaging satisfying (a) bar-invariance, (b) color-flavor compatibility (Bring color-tube symmetry), (c) standard normalisation, is unique. Open math + Lean. |
| 4 | **Geom_full(K) per-knot** | line 175, 185 | Cheat sheet: refining Geom_full is "open R&D"; Family-A linking-weight currently selected | `geom_full_unique` — any per-knot evaluation satisfying the universality axiom (`prop:geom-universality`) + categorical functoriality (`prop:hoefsmit-scattering-pipeline`) on a specified knot/link class is unique. Hardest of the four; couples knot invariants + categorical universality. |
| 5 | **Archimedean realization functor** at q₀ | implicit (Step 8 of chain) | Cheat sheet treats Archimedean realisation as well-defined; uniqueness modulo gauge implicit | `archimedean_functor_unique` — the realisation functor `R = ℚ(q) → ℝ` at `q = q₀` is unique up to the gauge of the substrate symmetry. Lower priority; standard categorical-realisation result, but should be formalized for completeness. |

## Notes

- **q₀ is NOT a uniqueness item** — q₀ is a *calibration choice* (pinned from CODATA m_p/m_e per #1422), not a mathematically unique value. The framework is parametric in q₀; the uniqueness items above hold for every q in the appropriate generic locus.
- **The Wedderburn decomposition + Hecke algebra** uniqueness are standard
  theorems (Mathlib / Drinfeld–Jimbo) — assumed without re-proof.
- **Class-axiomatisation pattern** (CLAUDE.md §3b-cond): when the cited
  uniqueness is an established external theorem (Wenzl, Jones), the Lean
  proof axiomatizes it as a `class` with the `-- Ref:` citation, and
  downstream results are proved sorry-free *conditional on the class
  instance*. The Mathlib pattern for citing established uniqueness
  results.

## Workflow

For each item:

1. **Authoring**: add a `theorem <X>_unique` in the relevant `.lean` file,
   axiom-classed where appropriate.
2. **Narrative**: add a paired remark/proposition block in `.md` describing
   the uniqueness statement + its physical content.
3. **Compute consequence**: identify any production script that previously
   chose between candidates and prove it now picks the unique canonical
   form.
4. **Audit**: add the uniqueness theorem to the cheat sheet's reference
   column.

## See also

- [`canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md)
- [`audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md`](audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md) §"Resolution 2026-05-29"
- `content/quantum-observable-universe/mass-theory/markov-trace-frobenius-selection.lean`
