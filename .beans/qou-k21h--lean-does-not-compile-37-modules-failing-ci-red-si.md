---
# qou-k21h
title: 'Lean does not compile: 37 modules failing, CI red since 2026-04-25'
status: in-progress
type: bug
priority: high
created_at: 2026-08-07T20:43:08Z
updated_at: 2026-08-07T20:43:08Z
---

A complete `lake build` of the QOU package — the first in months — fails on
**37 modules**. `lean_ci.yml` last ran **2026-04-25** and failed on `main`;
nothing has run a full Lean build since, so this accumulated unseen.

Found while reseeding the Lean olean cache (folio-assistant side). Bean
`5d7z` there recorded the symptom — "16 of 28 blocks failed to elaborate" —
and attributed it entirely to a cache missing own-package oleans. That was
only half of it: the code also does not build.

Build outcome: **4026 targets OK, 37 modules failing**, plus 9 `sorry`
warnings. The whole Mathlib closure (3214 oleans) built clean, so this is
QOU's own code, not a dependency problem.

## Error classes

**1. Declaration outside the namespace its dot-notation needs — dominant.**
A `def`/`theorem` meant to be `Type.member` is declared at namespace top
level, so it becomes `Namespace.member`. Call sites using `x.member` then
fail; because the carrier is often a `def ... : Prop`, Lean unfolds the type
and reports the confusing `Function.<member>` instead. Affects at least:
QCharacter (`IsQChar.mul`), TorusKnot (`TorusKnotLabel.seifertRank`,
`.embeddableOn`), DeltaLambdaSignRule (`Partition.dimIrrep` ×9, `.nStat`,
`.conjugate`, `.armLength`, `.legLength`, `.hookLength`, `.hookProduct`),
TypeBFoldedCrystalCombinatorics, LightNucleus, KnotRegistry, Brunnian,
EigenbasisStructuralLemmas, JointGaloisBraidFigure8, PathIntegrals,
PhysicalIntractability, LRFusion, BringShellBinding, Wedderburn.

**2. Parse errors — these files have NEVER compiled.** 5 sites:
ConfinementLevel (`exists` used as an identifier — reserved keyword),
MarkovAxiomsPrimitive, HoefsmitV21CosSymmetrization (×3),
BraidGroupNStrand.

**3. References to Mathlib constants that do not exist** in the pinned
revision (verified absent by grepping Mathlib): `List.foldl_mul_eq_mul_prod`,
`Real.rpow_half_eq_sqrt`, `Matrix.frobeniusInner`,
`Matrix.PosSemidef.entry_sq_le_diag_mul`,
`Matrix.PosSemidef.entry_zero_of_diag_zero`. These need real replacements,
not renames.

**4. Duplicate / clashing declarations.** `QOU.IsSelfDual` and
`TypeBCrystal.transpose` declared twice; AppendixSurreals/Basic declares
`SurrealField.neg/add/mul/sub` colliding with structure fields of the same
name (7 sites).

**5. Tactic failures** downstream of the above (`rewrite` pattern not found,
`decide` failed, `introN`, `cases` eliminating into non-`Prop`).

## Plan

- [ ] Class 1 (mechanical, unambiguous — intended name is stated in each file)
- [ ] Class 2 parse errors
- [ ] Class 4 duplicate/clashing declarations
- [ ] Class 3 nonexistent Mathlib constants — needs real substitutions
- [ ] Class 5 residual tactic failures
- [ ] Full `lake build` green
- [ ] Re-enable / verify `lean_ci.yml`

Classes 3 and 5 may need decisions about the mathematics; those get raised
rather than guessed.
