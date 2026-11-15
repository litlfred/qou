import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.SpinFromSo3Fiber — the D10 conjecture carrier

**Sibling-resolution carrier** for content block
[`conj:spin-from-so3-fiber`](spin-from-so3-fiber.md): *D10 spin SU(2)_S*.

**No instance is provided** — the honest open state for a conjecture (AGENTS.md §3b).

## 2026-09-04 — this carrier used to assert nothing

It read, in full:

```lean
class SpinFromSo3Fiber where
  holds : Prop
```

A field typed `: Prop` has the *universe* of propositions as its type, so an instance
supplies a proposition rather than a proof of one: `⟨True⟩` discharges the class, and
every `[SpinFromSo3Fiber]`-conditional theorem was conditional on nothing.

**The defect class is known, and this is not a new finding.** Bean `qou-tsnp` —
*"GAP: 12 conjecture carriers axiomatised as `holds : Prop` assert nothing"* — lists
this very carrier among its twelve, and
[`docs/audits/2026-08-23-free-prop-field-census.md`](../../../docs/audits/2026-08-23-free-prop-field-census.md)
(PR #5562) is the corpus-wide census, with a re-runnable detector at
[`scripts/free-prop-field-audit.py`](../../../scripts/free-prop-field-audit.py). What is
new here is the **repair**, following that bean's own prescription: *"replace `holds :
Prop` with fields that encode the conjecture's content — parameter-quantified statements
in the shape of the claim."* D9 (`IsospinFromCanonicalBowtie`) was closed the same way;
this is the second of the twelve.

## What is encoded, and why this shape

The block names its own missing object in one sentence:

> The missing object is a functor from the `S₅`/`SO(3)` level `ℓ` to a Wedderburn
> coefficient of the 3-strand `H₃` trace.

The carrier therefore takes that map as a **parameter** — `levelCoeff : ℕ → R`, sending a
spherical-harmonic level to the coefficient it contributes — and constrains it at the two
places the block gives values. Following the design rule recorded in
`QOU/AlgebraicSubstrate/ConditionalClasses.lean` after its own retraction — an `∃` over a
quantity the class itself chooses cannot be false, whereas a `∀` about a quantity the
caller supplies can be — the map is supplied by the caller, so the class **is refutable**: the constant-zero
map falsifies it, and that is discharged below rather than asserted.

Indexing: `levelCoeff n` is the coefficient of `h^(2n)`, so `levelCoeff 1` is the `h²`
coefficient and `levelCoeff 2` the `h⁴` one. The block's two values:

* the Borromean Markov trace's exact closed form has **`h² = 0`**;
* its first non-trivial coefficient is **`h⁴ = −3/4`**, the load-bearing gap.

## What is NOT encoded

**The construction of the functor itself.** The block asserts spin `SU(2)_S` *arises as*
the continuous lift of `SO(3)` via `S₅ → A₅ ≅ I ⊂ SO(3)`, and that extending to continuous
`SO(3)` is what populates `ℓ = 2, 3, 4, …`. Stating that needs a spherical-harmonic-level
type and an `H₃` Wedderburn-coefficient type related by an actual functor; the corpus
carries the *fibre map* (`BringFiberAction`, inhabited by `bringFiberAction_icosahedral`
with the icosahedral Reeb map) but not the level → coefficient bridge. Inventing those
types here would encode a different claim than the block makes.

This is exactly the case `qou-tsnp`'s guard describes — *"if a conjecture's claim cannot
yet be stated against existing types … the honest outcome is to say so and leave the
carrier, noting what type must grow first."* The claim is **partly** statable, so the
statable part is stated and the rest is named: **what must grow first is a type for the
`S₅`/`SO(3)` level indexed against `H₃`'s Wedderburn blocks.**

**NOT claimed:** that `h⁴ = −3/4` is derived here. It is the block's stated structural
value of the Borromean Markov trace; carrying it as a class field is the §3b conjecture
pattern, not a derivation (AGENTS.md §"Axiomatization is NOT a Proof").

## Base ring — generic, corrected 2026-09-05

This file first read *"Stated over `ℝ`: the coefficients are real and the block sits on the
archimedean side of the wall, so §7c's generic-`R` default does not apply."* That reasoning
was wrong, and a `wall-side-correct` sweep flagged it **critical**. Nothing here is
archimedean: there is no ordering, no `Real.sqrt`, no `Real.log`, no `Real.exp` — the
content is one rational-function identity and two equations, and `field_simp; ring`
discharges the identity over any field.

Both the class and the identity are therefore generic over `{R : Type*} [Field R]`, which
is strictly more general and clears the wall. The identity additionally needs
`[CharZero R]`, and that requirement is real rather than incidental: `field_simp` cannot
clear the `4⁻¹` without knowing `4 ≠ 0`, so the closed form is false in characteristic 2.
That is a genuine mathematical hypothesis the `ℝ` statement was hiding. The refutability witness instantiates at `ℚ`.

**The flag had been invisible, which is the part worth recording.** It did not appear when
this carrier was merged; it appeared when the sidecar was refreshed. The earlier verdict
was a `pass` recorded against a *previous version of this file*, and a stale sidecar is
indistinguishable from a clean one.

-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/spin-from-so3-fiber.ts
-/

namespace QOU.BraidsAndKnots

/-- **The Family A linking weight, in closed form.** The block states
`(3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h²` with `h = q - q⁻¹`, and that it *terminates* at `h²`.

This is an identity, not a conjecture, so it is a **theorem** rather than a class field —
the part of the block that can be discharged is discharged. It is what makes "Family A
terminates at `h²`" a statement about the truncation rather than about the algebra. -/
theorem familyA_linking_weight_closed_form {R : Type*} [Field R] [CharZero R]
    (q : R) (hq : q ≠ 0) :
    (3 * q ^ 2 + 4 + 3 * q⁻¹ ^ 2) / 4
      = 5 / 2 + (3 / 4) * (q - q⁻¹) ^ 2 := by
  field_simp
  ring

/-- **CONJECTURE (D10).** Spin `SU(2)_S` as the continuous `SO(3)` lift on the three colour
sheets, via the `S₅ → A₅ ≅ I ⊂ SO(3)` icosahedral embedding on Bring's quintic.

`levelCoeff` is the block's own named missing object — the map from spherical-harmonic
level to the Wedderburn coefficient it contributes to the 3-strand `H₃` trace, with
`levelCoeff n` the coefficient of `h^(2n)`. It is supplied by the **caller**, so the class
is false for maps that do not take the block's values (see the refutability theorem below).

**No instance is provided.** Downstream results consume this as `[SpinFromSo3Fiber f]` and
are genuinely conditional on it.

-- Ref: [leitner2026] conj:spin-from-so3-fiber -/
class SpinFromSo3Fiber {R : Type*} [Field R] (levelCoeff : ℕ → R) : Prop where
  /-- The Borromean Markov trace's exact closed form has **`h² = 0`** — the `ℓ = 1` level
  contributes nothing, which is why the `S₃`-truncated Family A weight (ending at `h²`)
  cannot see the structure. -/
  h_squared_vanishes : levelCoeff 1 = 0
  /-- The **first non-trivial** coefficient is `h⁴ = −3/4`, supplied by `ℓ = 2`. This is the
  load-bearing `h⁴` closure gap the block names. -/
  h_fourth_eq : levelCoeff 2 = -3 / 4

/-- The class is **refutable**, which the previous `holds : Prop` carrier was not: the
constant-zero map satisfies `h_squared_vanishes` and fails `h_fourth_eq`.

Stated as a theorem rather than left to the docstring because "the carrier asserts
something" is precisely the property that was missing, and a reader should see it
discharged rather than take the prose's word. -/
theorem spinFromSo3Fiber_refutable :
    ¬ SpinFromSo3Fiber (R := ℚ) (fun _ => 0) := by
  intro hc
  have h := hc.h_fourth_eq
  norm_num at h

end QOU.BraidsAndKnots
