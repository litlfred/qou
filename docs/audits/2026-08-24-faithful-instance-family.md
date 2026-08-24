# The "Faithful instance" family: 34 promised `sorry`s, 0 real ones

**Date:** 2026-08-24
**Bean:** `qou-hjf4` (successor to `qou-lo1t`, merged as [#5621](https://github.com/litlfred/qou/pull/5621))
**Status:** findings recorded; no Lean changed in this pass.

---

## Summary

Thirteen `.lean` files carry a boilerplate docstring on a global `instance`:

> **Faithful instance.** Carries the explicit research-grade conjecture as a sorry.

Measured with the comment-stripper from
[`scripts/trivially-inhabiting-instance-census.py`](../../scripts/trivially-inhabiting-instance-census.py):

| | count |
|---|---|
| occurrences of `sorry` in these 13 files | **34** |
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
