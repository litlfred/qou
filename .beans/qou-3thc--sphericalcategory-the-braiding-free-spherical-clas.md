---
# qou-3thc
title: 'SphericalCategory: the braiding-free spherical class, and sphericalOfRibbon'
status: in-progress
type: task
priority: normal
created_at: 2026-08-30T07:03:25Z
updated_at: 2026-08-30T07:04:11Z
---

## Why now

`PivotalCategory.lean` §"What is still not proved" says, verbatim: *"Sphericality — that the left
and right quantum dimensions agree — is a separate condition and is not touched here. A pivotal
structure does not imply it."* That is the last named open item of the `qou-djk4` arc; `qou-djk4`
itself is closed (its three follow-on items were each measured to need no work) and `qou-l64i`
(multiplicativity) merged on 2026-08-30 as `fba34039f2`.

## Corpus-grep (before declaring open)

- `content/**/*.lean` — **no** `SphericalCategory` class, **no** `sphericalOf*` instance,
  **no** `qDimLeft`/`qDimRight` defined from a pivotor. The single hit for `class Spherical` is
  `KeystonePivotalSpherical.lean:166`, which is `SphericalStructure` — a *different* object: it is
  stated over the **twistless braided** closure and its `leftQDim_eq` is an **asserted
  hypothesis**, not a derived condition (that is the finding `qou-djk4` recorded).
- `docs/`, `.beans/` — no hit for `SphericalCategory`.
- So this is open in the corpus. It is **not** open in the literature: sphericality of a ribbon
  category is classical (Barrett–Westbury). What is missing is the Lean.

## The target

Two definitions and one instance, all **braiding-free at the level of the statement** — which is
what makes this better than `SphericalStructure` and liftable to Mathlib:

```lean
noncomputable def qDimRight [PivotalCategory C] (X : C) : 𝟙_ C ⟶ 𝟙_ C :=
  η_ X (Xᘁ) ≫ ((pivotorApp X).hom ▷ Xᘁ) ≫ ε_ (Xᘁ) (Xᘁᘁ)

noncomputable def qDimLeft [PivotalCategory C] (X : C) : 𝟙_ C ⟶ 𝟙_ C :=
  η_ (Xᘁ) (Xᘁᘁ) ≫ (Xᘁ ◁ (pivotorApp X).inv) ≫ ε_ X (Xᘁ)

class SphericalCategory (C : Type*) [Category C] [MonoidalCategory C] [RightRigidCategory C]
    extends PivotalCategory C where
  qDimLeft_eq_qDimRight : ∀ X : C, qDimLeft X = qDimRight X
```

plus `sphericalOfRibbon [BalancedCategory C] [RibbonCategory C] : SphericalCategory C`.

## Planned route (a plan, not a finding — see the caveat)

`pivotalOfRibbon`'s pivotor is `θ_X ≫ (drinfeldIso X).hom` (`BraidedTensorDual.lean:357`), and
`drinfeldIso` is the `rightDualIso` comparing `X` and `Xᘁᘁ` as duals of `Xᘁ`, the first via
`BraidedCategory.exactPairing_swap`. So the expectation is

  `qDimRight X = qDimTwistedWith X (Xᘁ)` and `qDimLeft X = qDimTwistedLeftWith X (Xᘁ)`,

after which `qDimTwistedLeftWith_eq` (landed in #5866) closes the instance in one line. The
`rightDualIso`-against-`ε` step should be `rightDualIso_hom_unique`.

**This is a prediction and must be measured, not assumed.** In `qou-l64i` my predictions about
which rewrite would fire were wrong essentially every time while the measurements all held; and in
`qou-djk4` two rows of a summary table I wrote were wrong about facts the corpus already had. If
the bridge does not go through, the honest outcome is the two definitions plus a stated gap — not
a weakened class.

## Watch for

- **Do not restate the conclusion as a class field.** A `SphericalCategory` whose field is the
  thing to be proved is fine as a *class* (that is what a condition is), but `sphericalOfRibbon`
  must **derive** it. An instance that assumes it is the §3b-cond non-degeneracy failure.
- `qDimLeft`/`qDimRight` must not be definitionally equal, or the class is vacuous. Check with
  `rfl` being **rejected**, as `qou-djk4` did for `qDimTwistedLeftWith`.
