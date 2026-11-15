---
# qou-rdg8
title: 'gb-residue-spectral-sum: make mass a definition and the spectral decomposition a lemma (3-block change)'
status: todo
type: task
priority: normal
created_at: 2026-09-04T23:34:22Z
updated_at: 2026-09-04T23:34:51Z
---

Scoped out of `qou-tmmt` on 2026-09-04 (PR #6681), deliberately.

## The defect

`class GBResidueSpectralSum` carries `mass : R` as a **free field** and
`spectral_decomposition : mass = |descended| + ∑ ℓ, residue ℓ` as its only Prop
field. The class's own docstring states the consequence: *"any tuple inhabits
the class: choose the six data fields freely, set `mass := |descended| + ∑
residue ℓ`, and discharge this by `rfl`. So it fixes one field relative to the
others rather than constraining anything outside the class."*

That Prop field IS `prop:gb-residue-spectral-sum`, the block's own claim, and it
is satisfied by construction. It is a §3b-cond item-5 defect one level up from
the usual one — the projection is not in a theorem body (both consuming theorems
genuinely derive), so no body-shape detector can see it.

## The fix

- `mass` becomes `def spectralMass (S) : R := |S.descended| + ∑ ℓ, S.residue ℓ`.
- `spectral_decomposition` becomes a proved lemma (`rfl`), which is honest:
  it *is* true by construction, and saying so removes an axiom rather than
  dressing one up.
- The conjectural content then has to move to what the docstring says is
  genuinely unencoded: that `residue ℓ` is the cyclotomic projection of
  `Φ_q · gradedTrace ℓ`, and that `gradedTrace` is `tr_M` descended along
  `J^ℓ/J^{ℓ+1}`. Both need the Habiro-ring / GS-filtration infrastructure the
  module header defers, so the honest interim is a class field relating
  `residue` to `gradedTrace` at all — today nothing does, and the docstring
  says so.

## Why it is a three-block change, not a one-file one

Three siblings reference the class's fields by `lean.ref`:

- `gs-spectral-decomposition-existence.ts` → `qou:QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition`
  (it exists *only* to point at that field);
- `habiro-residue-sum-equivalence.lean` references `GBResidueSpectralSum.mass`;
- `gs-spectral-sum-finite.ts` → `qou:QOU.BraidKnot.spectral_sum_finite`.

There is also a **library twin**,
`content/quantum-observable-universe/lean/QOU/BraidKnot/GBResidueSpectralSum.lean`,
which defines the same class and a `spectral_sum_finite` **of a different
statement** under the same name in the same namespace. It is imported by
`QOU.BraidKnot`, so changing it needs an olean rebuild (`lean -o`, never
`lake build` — the restore carries `RESTORED-NO-TRACES`).

**Decide the sibling-vs-library duplication first.** Two definitions of one
class, drifting (the sibling had `ℝ` hardcoded where the library is generic;
that direction was already corrected once), is the actual root problem here, and
fixing `mass` in only one of them would widen the drift rather than close it.
