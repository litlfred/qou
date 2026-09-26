/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.DisjointBlockTraceLaw

/-!
# The radical of a Markov trace, and what faithfulness means

`OcneanuTrace.MarkovTrace` axiomatises a trace on a tower but says nothing about
whether that trace *sees* the algebra.  This file supplies the missing notion and
its elementary theory, so that "is the Ocneanu trace faithful?" becomes a
statement one can prove or refute rather than a phrase.

## The definition, and why this one

For a trace `tr` on `A` the associated bilinear form is `⟨a, b⟩ = tr (a * b)`, and
its **radical**

  `rad T = {a | ∀ b, tr (a * b) = 0}`

is what faithfulness is about: `tr` is faithful exactly when `rad T = ⊥`.  Note
what is *not* meant — `tr` is a functional into `R`, so it is never injective on
an algebra of dimension `> 1`, and "faithful" never refers to injectivity of
`tr` itself.

## What is proved

* `rad` is a **two-sided ideal** — `mul_mem_rad_left` needs the trace property
  `tr (x * y) = tr (y * x)` and associativity, nothing else.
* `one_notMem_rad` — the radical is proper, from normalisation `tr 1 = 1`.  So
  the question is never vacuous in the degenerate direction.
* `tr_mul_gen_sub_z_of_mem` — **the Markov axiom is an orthogonality
  statement**: `g n - z • 1` is orthogonal to the whole of `H n`.  This is (T3)
  read as a fact about the form rather than about stabilisation, and it is the
  reason the radical is the natural object here: each new generator arrives with
  a prescribed component orthogonal to everything below it.
* `rad_mono_of_towerSpan_step` — the level-wise radicals **increase**: an
  element of `H n` orthogonal to a subalgebra `B ⊆ H n` stays orthogonal when
  `B` is extended by sandwiches `v * g n * w`.  Cyclicity turns the sandwich
  inside out, Markov strips the generator, and the result lands back in `B`.
  This is what makes a single low-level computation decide faithfulness at every
  level, and it is used in `OcneanuTraceNotFaithful`.

## What is NOT proved here

Nothing about any particular trace.  Whether `rad` is zero depends on the Markov
parameter `z`, and that computation is `OcneanuTraceNotFaithful`.  Nothing here
asserts or assumes faithfulness either way.
-/

namespace QOU.MathlibExt.MarkovTraceRadical

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.DisjointBlockTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
  (T : MarkovTrace R A)

/-- **The radical of the trace form** `⟨a, b⟩ = tr (a * b)`: the elements the
form cannot see. -/
def rad : Submodule R A where
  carrier := {a | ∀ b : A, T.tr (a * b) = 0}
  add_mem' {x y} hx hy := by
    intro b; rw [add_mul, map_add, hx b, hy b, add_zero]
  zero_mem' := by intro b; rw [zero_mul, map_zero]
  smul_mem' c x hx := by
    intro b; rw [smul_mul_assoc, map_smul, hx b, smul_zero]

@[simp] theorem mem_rad_iff {a : A} : a ∈ rad T ↔ ∀ b : A, T.tr (a * b) = 0 := Iff.rfl

/-- `rad` is a **right** ideal — by associativity alone. -/
theorem mul_mem_rad_right {a : A} (ha : a ∈ rad T) (c : A) : a * c ∈ rad T := by
  intro b; rw [mul_assoc]; exact ha _

/-- `rad` is a **left** ideal — this is where the trace property is used. -/
theorem mul_mem_rad_left {a : A} (ha : a ∈ rad T) (c : A) : c * a ∈ rad T := by
  intro b
  have h : T.tr (c * a * b) = T.tr (a * (b * c)) := by
    rw [mul_assoc c a b, T.tr_mul_comm c (a * b), mul_assoc]
  rw [h]; exact ha _

/-- **Faithfulness**: the trace form is nondegenerate. -/
def IsFaithful : Prop := rad T = ⊥

theorem isFaithful_iff :
    IsFaithful T ↔ ∀ a : A, (∀ b : A, T.tr (a * b) = 0) → a = 0 := by
  rw [IsFaithful, Submodule.eq_bot_iff]
  exact ⟨fun h a ha => h a ha, fun h a ha => h a ha⟩

/-- A nonzero radical element **refutes** faithfulness. -/
theorem not_isFaithful {a : A} (ha : a ∈ rad T) (ha0 : a ≠ 0) : ¬ IsFaithful T :=
  fun h => ha0 ((isFaithful_iff T).mp h a ha)

/-- The radical is **proper**: normalisation `tr 1 = 1` keeps `1` out of it, so
the trace is never degenerate in the trivial direction. -/
theorem one_notMem_rad [Nontrivial R] : (1 : A) ∉ rad T := by
  intro h
  have h1 := h 1
  rw [mul_one, T.tr_one] at h1
  exact one_ne_zero h1

/-- **The Markov axiom, read as orthogonality.**  The new generator arrives with
a prescribed component `z • 1`, and what is left over is orthogonal to the whole
of the level below. -/
theorem tr_mul_gen_sub_z_of_mem (n : ℕ) (a : A) (ha : a ∈ T.H n) :
    T.tr ((T.g n - T.z • (1 : A)) * a) = 0 := by
  have hcyc : T.tr (T.g n * a) = T.z * T.tr a := by
    rw [T.tr_mul_comm (T.g n) a]; exact T.markov n a ha
  rw [sub_mul, map_sub, hcyc, smul_mul_assoc, one_mul, map_smul, smul_eq_mul, sub_self]

/-- **The lifting step, and the reusable content of this file.**

If `a ∈ H n` is orthogonal to every element of a subalgebra `B ⊆ H n`, then it is
orthogonal to every sandwich `v * g n * w` with `v, w ∈ B` as well.

Cyclicity moves `w` to the front, Markov strips `g n`, and `v * w` is back in
`B`. So the radical relative to a stage of the filtration only ever grows — one
computation at one level settles every level above it. -/
theorem tr_mul_sandwich_of_orthogonal (n : ℕ) (B : Subalgebra R A) (hB : B ≤ T.H n)
    (a : A) (ha : a ∈ T.H n) (horth : ∀ b ∈ B, T.tr (a * b) = 0)
    (v : A) (hv : v ∈ B) (w : A) (hw : w ∈ B) :
    T.tr (a * (v * T.g n * w)) = 0 := by
  have hav : a * v ∈ T.H n := (T.H n).mul_mem ha (hB hv)
  have hw' : w ∈ T.H n := hB hw
  have e1 : T.tr (a * (v * T.g n * w)) = T.z * T.tr (a * v * w) := by
    rw [show a * (v * T.g n * w) = a * v * T.g n * w by simp only [mul_assoc]]
    exact markov₂_of_markov T n _ hav w hw'
  rw [e1, mul_assoc, horth _ (B.mul_mem hv hw), mul_zero]

end QOU.MathlibExt.MarkovTraceRadical
