# The "Faithful instance" family: 37 promised `sorry`s, 0 real ones

**Date:** 2026-08-24
**Bean:** `qou-hjf4` (successor to `qou-lo1t`, merged as [#5621](https://github.com/litlfred/qou/pull/5621))
**Status:** four fixes landed — `CrystalGraphRealization.canonical` and
`QIntegerMassFormula.canonical` demoted to `def`s, the `QOU.PhiQJSJ`
duplication resolved by import, and five collided `QOU.Molecular` classes
renamed. Findings B (the `IsAMEValue` gate), C (`MassEndomorphism`) and the
five vacuous `core-levi-form` carriers are recorded and await an authorial
call.

> This line read *"findings recorded; no Lean changed in this pass"* and was
> left behind by the first three of those commits.

---

## Summary

Thirteen `.lean` files carry a boilerplate docstring on a global `instance`:

> **Faithful instance.** Carries the explicit research-grade conjecture as a sorry.

Measured with the comment-stripper from
[`scripts/trivially-inhabiting-instance-census.py`](../../scripts/trivially-inhabiting-instance-census.py):

| | count |
|---|---|
| occurrences of `sorry` in these 13 files | **37** |
| occurrences that are a `sorry` **term** | **0** |

Every one is inside a docstring or a `--` comment. The conjectures are not
carried by a `sorry`; they are discharged by **collapsing the model** — the
carrier's data fields are filled with `PUnit`, `0`, or `none`, which makes the
Prop fields hold definitionally.

The instances are **unconditional and global**, so they satisfy every
`[C …]` binder in scope. A reader running `#print axioms` on the downstream
theorem sees no `sorryAx` and can reasonably conclude the result is proved.

This is AGENTS.md §"Axiomatization is NOT a Proof" and §1a
(no audit-dodging), and the honest disposition is the one applied to
`triv_hecke` / `triv_wedderburn` in [#5581](https://github.com/litlfred/qou/pull/5581)
and `skeletonRealisation` in #5621: **demote the `instance` to a `def`.**
The model stays available to anyone who wants it; it stops being found by
instance synthesis.

---

## Finding A — `CrystalGraphRealization` (39 consumers, the largest in the corpus)

[`QOU/BraidKnot/CrystalGraphRealization.lean:93`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/CrystalGraphRealization.lean)

```lean
/-- **Faithful instance.** Carries the explicit research-grade conjecture as a sorry. -/
instance canonical (R : Type u) [CommRing R] (q : R) :
    CrystalGraphRealization R q where
  NormalForm := PUnit
  CrystalNode := PUnit
  nodeOf _ := PUnit.unit
  raising _ _ := none
  lowering _ _ := none
  crystal_realises _ _ := rfl
```

Both *types* are collapsed to the unit type and both crystal operators return
`none`, so `crystal_realises` closes by `rfl`. The theorem above it,

```lean
theorem nodeOf_isHighestWeight
    {R : Type u} [CommRing R] {q : R} [C : CrystalGraphRealization R q]
    (T : C.NormalForm) : IsHighestWeight (C.nodeOf T) :=
  fun i => C.crystal_realises T i
```

reads as *"the crystal node attached to any GS normal form is a Kashiwara
highest-weight vector"*. The only model in scope has one normal form, one node,
and no crystal operators. Same carrier shape as `triv_hecke` (also `PUnit`).

## Finding B — `QIntegerMassFormula` (13 consumers), laundered through a hypothesis class

[`QOU/Interactions/QIntegerMassFormula.lean:185`](../../content/quantum-observable-universe/lean/QOU/Interactions/QIntegerMassFormula.lean)

This one is worth reading closely, because the vacuity is not in the instance
alone — it is split across two declarations, and neither half looks wrong by
itself.

`IsAMEValue` is documented as recording *"the two physical invariants every real
entry satisfies"*, so that `[IsAMEValue Z N B_AME]` is *"a genuine
restriction"*. It has **three** fields, and the third is:

```lean
  /-- Trivialized bound hypothesis to close sorry -/
  fits_bound : ∀ (q m_e : ℝ), ∃ δ : ℝ, |δ| ≤ (1 : ℝ) / 100 ∧
    B_AME = (1 + δ) * binding_energy_bw q m_e Z N 0 0
```

That field **is the conjecture**, and its own docstring says why it is there.
The instance then closes the conjecture by projecting it:

```lean
instance canonical : QIntegerMassFormula where
  f_magic := fun _ => 0          -- makes `… (f_magic Z) (f_magic N)` ≡ `… 0 0`
  tolerance := 1 / 100
  fits_AME := fun q m_e Z N B_AME inst => inst.fits_bound q m_e
```

The `fun _ => 0` is **load-bearing**: it is what makes the conclusion's type
line up definitionally with `IsAMEValue.fits_bound`. So
`theorem fits_AME_conditional` — sorry-free, and stating that the seven-term
q-integer formula matches AME binding energies to within `tolerance` — reduces
to `∀ …, [claim] → [claim]`, with the magic-number corrections zeroed.

Machine-checked, against the real module built from source:

```
#synth QIntegerMassFormula                      -->  canonical
(inferInstance).f_magic = fun _ => 0            -->  rfl
(inferInstance).tolerance = 1 / 100             -->  rfl
#print axioms fits_AME_conditional
    --> [propext, Classical.choice, Quot.sound]      (no sorryAx)
#print axioms QOU.Interactions.canonical
    --> [propext, Classical.choice, Quot.sound]      (no sorryAx)
```

and the reduction, which compiles:

```lean
example (B : ℝ) [inst : IsAMEValue 26 30 B] (q m_e : ℝ) :
    ∃ δ : ℝ, |δ| ≤ (1 : ℝ) / 100 ∧
      B = (1 + δ) * binding_energy_bw q m_e 26 30 0 0 :=
  inst.fits_bound q m_e
```

## Finding C — `MassEndomorphism`, already known and still live

Two instances, both all-zeros:
`canonical` (generic in `R` and `β`) and `trivial_int_zero` (at `ℤ`).

**This is not a new finding.** `QOU/MassEndomorphism/VolumeBridge.lean` already
records it, correctly and in the right words:

> Those instances … make `[MassEndomorphism R β]` synthesizable, so
> conditionality against *that* class is vacuous. … demoting them to
> non-instance `def`s is tracked separately.

Recorded here only to note that the "tracked separately" has not landed, and
that `VolumeBridge`'s own instance-free design is the model the rest of this
family should follow.

## Not defects — the discriminator that separates them

Two rows the census flags that are **correct as written**, and the reason is the
same both times: *a constant is content-free only when nothing constrains it.*

- **`HasHe4ChannelActiveSet`** — `xDD := 0`, `xHe3n := 0`, `yTp := 0` are the
  genuine LP values of the inactive channels. They are pinned by
  `active_set_eq`, `dual_ordering`, `cost_ordering` and `strong_duality`, each
  discharged `by norm_num` over concrete rationals. The zero is a **checked
  datum**. (Consistent with the `legit` verdict on `he4_strong_duality_value`
  in the review ledger.)
- **`hasHoefsmitData_vacuum`** — declared `HasHoefsmitData 0 0`, i.e. **indexed
  at the vacuum**. `numGenerators := 0` is the correct value there, and the
  instance does not discharge `[HasHoefsmitData n k]` for general `n k`.

So the gate is not "does a field hold a constant" but: **is the carrier generic,
and is the constant unconstrained by any real check?**

---

## Two corrections to my own prior numbers

**1. #5621 under-counted. The actionable set is 17, not 14.**

The census treated *every* `[…]` binder as a conditional-class guard. So

```lean
instance canonical {R : Type*} [CommRing R] {β : Type*} : MassEndomorphism R β
```

read as *"guarded by `CommRing`"* and disappeared — while `trivial_int_zero`
stayed visible only because it is pinned at concrete `ℤ` and therefore carries
no `[CommRing]` binder at all. The detector was hiding the **worse** of the two
instances and showing the milder one.

A guard is what makes `prop-rigid-monoidal`'s `canonical` inert:
`[ctx : RigidMonoidalStructuralGapInvarianceAxiom α]`, a content carrier with no
instance of its own. Mathlib structure is not that. A binder now counts as a
guard only if it names a class **this corpus declares**.

    before:  36 rows -> 23 unguarded -> 14 actionable
    after:   36 rows -> 30 unguarded -> 17 actionable

**2. An ASCII `->` in a data field's type hid it, in the safe direction.**

`PROP_MARKERS` contains `>`, and `->` is legal Lean. So
`realisation : Nat -> Nat -> R` — plain data — read as a proof obligation and
its constant value was never flagged. Unicode `→` is not a marker, so the bug
was invisible in the corpus's dominant spelling; 4 field declarations under
`content/` use the ASCII form. Fixed by stripping both arrow spellings before
the marker scan.

**3. The self-test deleted itself on success.**

Its positive case was `skeletonRealisation`, which #5621 correctly demoted to a
`def` — so the test failed *because the corpus had been repaired*. A regression
test that depends on the corpus staying broken is not a regression test. The
criterion is now pinned against an **inline fixture**; only "must stay absent /
present" assertions are made against the real tree.

---

## Disposition

**Finding A is actioned. The blast radius was measured, and it is zero.**

`CrystalGraphRealization.canonical` is now a `def`. The "39 consumers" figure
counted *binder sites*, and a hypothesis binder `[C : CrystalGraphRealization R q]`
in a signature needs no synthesis — it is a parameter. Measured across all twelve
files that bind the class (eight library modules plus four content-block
siblings, the latter outside the Lake library so nothing routinely compiles
them):

    12 files -> exit 0, 0 errors, 0 `failed to synthesize`

**The measurement is sensitive, not vacuous.** A paired control run both ways:

| | `#inferInstance` for the class | exit |
|---|---|---|
| `canonical` a `def` | `failed to synthesize QOU.BraidKnot.CrystalGraphRealization` | 1 |
| `canonical` an `instance` | succeeds | 0 |

Written with `[CommRing R]` already in scope as a hypothesis, so a failure can
only be about `CrystalGraphRealization`. The first attempt at this control was
**invalid and nearly recorded as a pass**: it used a bare `ℤ` and failed on
`failed to synthesize CommRing ℤ` — the right exit code for the wrong reason,
which is the "must-fail probe accepts any error" trap logged on `qou-lo1t`.

Its docstring no longer claims a `sorry` it does not have; the comment-stripped
`sorry`-term count for the file is **0**, as stated.

**Finding B is half-actioned, and the half that remains is the author's call.**

`QIntegerMassFormula.canonical` is now a `def`, on the same measurement: the
library file, its content-block sibling, and `wigner_coefficient_conditional`
— the only outside consumer, and it binds `[inst : QIntegerMassFormula]` as a
*hypothesis* — all build at **exit 0, 0 errors**, with the paired control
failing specifically on `failed to synthesize
QOU.Interactions.QIntegerMassFormula` and succeeding again when restored.

**That does not discharge the finding**, because the laundering is one level up,
in the *hypothesis* class. While `IsAMEValue.fits_bound` exists,
`fits_AME_conditional` reduces to `∀ …, [claim] → [claim]` however `canonical`
is declared.

### Why the rest is not mine to decide

A first draft of this note gave the wrong reason — that changing `IsAMEValue`
would change the meaning of every theorem binding it. **Measured, that is
false**: `IsAMEValue` is bound in exactly two places, *both inside its own
file*. There is no downstream sprawl. The actual reason is narrower and harder:

**Two rival versions of this class exist and they disagree about the claim.**

| | library `QOU/Interactions/QIntegerMassFormula.lean` | sibling `mass-theory/q-integer-mass-formula.lean` |
|---|---|---|
| AME gate | `[IsAMEValue Z N B_AME]` | **none** — quantifies over an arbitrary real `B_AME` |
| instance | global `canonical` (now a `def`) | **none** — honestly uninhabited |
| conjecture lives in | `IsAMEValue.fits_bound` | `QIntegerMassFormula.fits_AME` |

Per AGENTS.md §0a the **sibling shadows the library file**, so a content block's
`lean.ref` resolves to the version with no gate — whose `fits_AME` is *false as
written*, since it asserts the 1 % bound for every real number.

So the library file's `IsAMEValue` did two things at once, one good and one not:
it added a genuine restriction on `B_AME`, and it put the conjecture inside that
restriction. **Simply deleting `fits_bound` moves this file toward the sibling's
statement, which is worse.** The likely right shape keeps `IsAMEValue`'s two
real invariants and relocates the conjecture into `QIntegerMassFormula`, where
the class docstring already says it belongs — but choosing that, and deciding
which of the two files is the paper's declaration, is authorial.

**Finding C is untouched** — `MassEndomorphism` already has an owner per
`VolumeBridge.lean`. Both remain on `qou-hjf4`.

---

## Finding D — the instances are a symptom; the structure is duplicate declarations

Before grinding through the remaining ~9 demotions, I checked whether the
shadowing problem hit on `QIntegerMassFormula` was peculiar to it. It is not,
and this is the larger finding.

Chasing one vacuous instance in `observations/borromean-quark.lean` turned up
that **`class BorromeanQuark` is declared eleven times** across `content/`, and
that the two carrying `instance canonical` sit in the *same* namespace as each
other. Measured corpus-wide by
[`scripts/duplicate-class-declaration-census.py`](../../scripts/duplicate-class-declaration-census.py)
(`--self-test`, comment-stripped, 3117 files):

| | count |
|---|---|
| distinct class names | 930 |
| declared in **more than one file** | **61** |
| ...with ≥2 declarations in the **same namespace** — can collide on import | **38** |
| files involved in a same-namespace collision | 85 |
| collisions pairing a **library** file with a **content-block sibling** (the §0a shape) | **27** |

Worst offenders, all of them from the family above:

    BorromeanQuark            11 files   collides in QOU.Archimedean, and 3 more at <root>
    QIntegerMassFormula        8 files   collides in QOU.Interactions AND in QOU.Molecular (5 files)
    CrystalGraphRealization    4 files   collides in QOU.BraidKnot

Most-affected namespaces: `QOU.BraidKnot` (12 colliding names),
`QOU.FluidDynamics` (8), then `QOU.AlgebraicSubstrate` / `QOU.Molecular` /
`QOU.BraidsAndKnots` (3 each).

**This failure mode is already documented in the corpus, by a file that fixed
its own instance of it.**
`QOU/Archimedean/HyperbolicVolumeIndependence.lean` records:

> This file previously declared a *duplicate* `HyperbolicVolumeIndependence`
> class with a placeholder shape … and a **vacuous** global instance
> `{ residual := 0, rfl }`. That was unsound as a conjecture encoding: the
> trivial instance silently discharged every `[HyperbolicVolumeIndependence]`
> hypothesis with no mathematical content, and the duplicate declaration
> collided with the real class when both files were imported.

That repair held — the class is now declared once in
`HyperbolicVolumeTranscendence.lean`, as that docstring says. But the *pattern*
recurs: `HyperbolicVolumeIndependence` is still declared in three files, two of
them sharing `QOU.BraidKnot`. The vacuous instance and the duplicate
declaration are the same defect seen from two directions, and AGENTS.md §0a
already bans the shape ("NEVER create or keep such a stub when the real
formalisation exists in the library tree").

**Caveat on the number, because I got it wrong first.** An earlier run reported
**42** same-namespace collisions. It asked only whether a *file* contained a
given `namespace` line anywhere, which credits every class in that file to
every namespace block in it — and Lean namespaces nest and reopen, so a file
may hold declarations in `QOU.BraidKnot`, `QOU.BraidKnot.Inner` and
`QOU.Archimedean` at once. The committed script tracks the open
`namespace`/`end` stack line by line (including `section`, whose `end` would
otherwise pop a namespace) and attributes each class to the stack **at its own
line**. That is the difference between 42 and 38. The `61` is
namespace-independent and was correct either way.

A same-name pair in *different* namespaces is **not** a collision — it is two
distinct classes, possibly intentional, possibly an unnoticed fork. This census
does not judge which; only the 38 same-namespace rows can actually clash.

---

## Finding E — of the 40 collision groups, 21 need the author and 19 do not

The count alone cannot be acted on, because the copies are not the same kind of
thing. [`scripts/duplicate-class-divergence-triage.py`](../../scripts/duplicate-class-divergence-triage.py)
(`--self-test`) compares the copies field-by-field, normalising whitespace so a
docstring or line-wrap difference does not register:

| verdict | groups | meaning |
|---|---|---|
| `IDENTICAL` | 18 | same field names and types |
| `STUB` | 1 | one copy has no fields, or only `True`-typed ones |
| `DIVERGENT` | **21** | the copies state genuinely different things |

(40 groups against 38 class names, because a name colliding in two namespaces —
`BorromeanQuark`, `QIntegerMassFormula` — yields two groups.)

**The 21 `DIVERGENT` are the ones that need an authorial call**, for the reason
`IsAMEValue` already showed: deciding which copy is canonical is deciding what
the paper claims. They include `BorromeanQuark` (both groups),
`CrystalGraphRealization`, `QIntegerMassFormula` (both groups — and the
`QOU.Molecular` one is **five library files**, the `*_lp_dual_binding` family,
each redeclaring the class), and eight in `QOU.FluidDynamics`.

The comparison is deliberately conservative in the direction of asking rather
than assuming: a false `DIVERGENT` costs a read, a false `IDENTICAL` could
delete a real statement.

**"Mechanically resolvable" is weaker than it sounds, and the 19 are not a
delete.** Identical *class declarations* do not make identical *files*. The
`MassEndomorphism` pair is the caution: its two copies would compare closely,
yet the sibling carries seven theorems the library file does not
(`transient_unique`, `mass_decomposition`, `fullMass_pos_of_vol_pos`, …).
Resolving a duplicate means making one file import the other and adjusting
namespaces — a real edit with import-graph consequences — not removing a
declaration. What the 19 buy is that **no semantic question has to be answered
first**.

### A concern about my own earlier fix, checked and cleared

`TowerSummandRealization` and `PerPieceBridge` appear in the `IDENTICAL` list,
both in `QOU.PhiQJSJ`, one library copy and one sibling. Since PR #5621
demoted `skeletonRealisation` in the **sibling**
(`mass-theory/phi-q-tower-jsj-bridge.lean`), the obvious worry is that the fix
touched one copy of a duplicated class and left the other live.

It did not. `lean/QOU/PhiQJSJ.lean` declares both classes and contains **zero**
`instance` declarations, so the vacuous instance existed only in the sibling and
#5621 covered the only copy. The duplication itself is still real — the two
files declare the same classes in the same namespace and neither imports the
other — but nothing vacuous is hiding in the copy I did not edit.
