---
# qou-3thc
title: 'SphericalCategory: the braiding-free spherical class, and sphericalOfRibbon'
status: completed
type: task
priority: normal
created_at: 2026-08-30T07:03:25Z
updated_at: 2026-08-30T07:24:39Z
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


## CLOSED 2026-08-30 — all of it proved, sorry-free

Commit `eb94a71fce` on `claude/spherical-category-ribbon-2026-08-30`, PR #6117.
New module `QOU/MathlibExt/SphericalCategory.lean`, registered in `QOU.lean`.

`qDimPivotalRight`, `qDimPivotalLeft`, `SphericalCategory`, both bridges, and
`sphericalOfRibbon` — every ribbon right-rigid category is spherical. The instance
**derives** the field (`qDimTwistedLeftWith_eq` discharges it); it does not carry its own
conclusion.

### The planned route held — with one piece that was not in the plan

The bean predicted `qDimPivotalRight = qDimTwistedWith X Xᘁ` via `rightDualIso_hom_evaluation`,
and that half went through in **three lines**. The *left* half did not: the evaluation form is
structurally unable to reach it, because there the pivotor appears **whiskered on the left against
a coevaluation**, not whiskered right against an evaluation. The missing lemma is

    coev_comp_rightDualIso : η_{p₁} ≫ A ◁ (rightDualIso p₁ p₂).hom = η_{p₂}

the coevaluation counterpart of `rightDualIso_hom_evaluation`, which the corpus did not have and
Mathlib does not have either (Mathlib carries `rightDualIso` and `rightDualIso_id` and nothing
else). So the tranche's real content is one new general rigid-category lemma plus the assembly.

**The p₁-vs-p₂ choice inside it is not cosmetic**, and this is the part worth carrying forward.
Transporting the goal through `tensorLeftHomEquiv` for **p₂** leaves a mixed `η_{p₂}` against
`ε_{p₁}` which is no snake identity and does not close. The **p₁** equivalence reduces *both*
sides to `(ρ_ B₁).hom ≫ (rightDualIso p₁ p₂).hom` after a single use of the evaluation form. Both
were tried; only the second works.

### Measured, not assumed

- **Non-vacuity.** `qDimPivotalLeft X = qDimPivotalRight X := rfl` is **rejected** by the
  elaborator, so the class field relates two genuinely distinct morphisms. Same check `qou-djk4`
  applied to `qDimTwistedLeftWith`.
- **The `qou-l64i` lesson transferred.** Two rewrites failed against goals they visibly matched;
  both were fixed by restating the helper in **reassoc form with a trailing `k`** (`hnat`), the
  same shape that unlocked the monodromy proof. A third failure was an over-eager `congr 2` that
  produced an object-equality goal `Xᘁ ⊗ X = X ⊗ Xᘁ`; replacing it with a named rewrite fixed it.
- **Instance coherence.** `sphericalOfRibbon` had to move out of the `[BalancedCategory C]`
  section: with both that variable and `[RibbonCategory C]` in scope, `RibbonCategory.toBalancedCategory`
  and the section variable are *different* instances and the final `exact` fails on it.

### Verification (CI is `workflow_dispatch`-only; agent verification is the gate)

- `lean`-direct exit 0, no warnings, on the new module and on the edited `PivotalCategory.lean`.
- `#print axioms` on `coev_comp_rightDualIso`, both bridges and `sphericalOfRibbon`:
  `[propext, Classical.choice, Quot.sound]` — **no `sorryAx`**.
- `scripts/check-sidecars.sh` clean; no §7c flags (generic over `C`, no `ℝ`).

### Left deliberately undone

- `coev_comp_rightDualIso` belongs in `RightDualIsoUnique.lean` beside the evaluation form. It is
  in the new file instead, because that module is imported transitively by everything this file
  uses, so adding it there invalidates each of their oleans and a `lake build` on a restored tree
  is the documented way to destroy the cache. Docstring records the intended home.
- `BraidKnot.SphericalStructure` is untouched, and should stay: it is the right object where no
  twist is available, and `qou-djk4` established it is not derivable from ribbon at any twist.
