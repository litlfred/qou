/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Algebra.Subalgebra.Basic
import Mathlib.Algebra.Algebra.Subalgebra.Lattice
import Mathlib.Algebra.Group.Conj
import Mathlib.Algebra.Field.Rat
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# The Ocneanu / Markov trace as an abstract functional on a tower

Mathlib has no Markov trace and no Ocneanu trace.  Measured, not assumed: a
case-insensitive word-boundary grep over every `.lean` file of the vendored tree
(commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`) returns **0** hits for
`Ocneanu`, `Markov trace`, `Temperley`, `Kauffman`, `skein`, `Jones polynomial`
and `BraidGroup`, and **1** for `Hecke` — a paper title in the FLT bibliography
comment.  `find -iname '*knot*' -o -iname '*braid*' -o -iname '*hecke*'` returns
only `CategoryTheory` files about the monoidal *braiding*.  Two near-misses that
a bare grep would report: `Mathlib.CategoryTheory.MarkovCategory` is categorical
probability and `Mathlib.MeasureTheory…Markov` is Markov's inequality; neither is
this.  What Mathlib does supply, and what this file leans on, is
`Matrix.trace_mul_comm`-style cyclicity as an *idea* and the `Subalgebra` /
`LinearMap` / `IsConj` API.

This file axiomatises the trace **as a functional on a tower of subalgebras**

  `H 0 ⊆ H 1 ⊆ H 2 ⊆ ⋯ ⊆ A`,

with a distinguished new generator `g n ∈ H (n+1)` at each level, and derives the
consequences that make such a functional useful.

## What is a HYPOTHESIS here

`MarkovTrace` itself.  Its fields are the classical axioms

* `tr_mul_comm` — the trace property `tr (a * b) = tr (b * a)`;
* `tr_one` — normalisation `tr 1 = 1`;
* `markov` — **Markov stabilisation** `tr (a * g n) = z * tr a` for `a ∈ H n`;
* `markov_inv` — the inverse-generator form `tr (a * g⁻¹ n) = z' * tr a`.

**Nothing in this file constructs such a functional on the Iwahori–Hecke tower**,
and no claim is made that the Hecke tower satisfies these axioms.  That is the
standard theorem of Jones and Ocneanu, cited below and *not* formalised here.
What is supplied instead is a **non-vacuity witness** (`unitMarkovTrace`), so
that the axioms are demonstrably satisfiable and none of the theorems below is
empty.

**No topology is proved here.**  There is no braid group, no link diagram, no
Hecke algebra, no Markov theorem, no Reidemeister move and no Jones polynomial
anywhere in this file, and none is defined or imported.  The tower is purely
algebraic: a monotone family of `Subalgebra R A` with a distinguished element
adjoined at each level.  Where the names "Markov move I / II" occur below they
are *nomenclature for the algebraic statement being proved* — they record which
classical move that statement is the algebraic shadow of, and are **not** a
claim that any topological invariance has been established.

## What is a THEOREM here

* `MarkovTrace.tr_conj` — conjugation invariance from a *one-sided* inverse:
  `v * u = 1 → tr (u * x * v) = tr x`.  No unit, no group, no invertibility of
  `x`.
* `MarkovTrace.tr_eq_of_isConj` — consequently `tr` is a **class function**:
  `IsConj x y → tr x = tr y`.  This is Markov move I.
* `MarkovTrace.tr_gen`, `MarkovTrace.tr_gen_inv` — the two Markov parameters are
  the trace values of the generators: `tr (g n) = z`, `tr (g⁻¹ n) = z'`.  These
  are where `tr_one` earns its place.
* `MarkovTrace.tr_mul_stabWord` — **iterated stabilisation**: appending the `k`
  successive new generators `g n, g (n+1), …, g (n+k-1)` to an element of `H n`
  multiplies the trace by `z ^ k`.  This is Markov move II, iterated, and it is
  the statement whose specialisation at `a = 1` reads
  `tr (g n * g (n+1) * ⋯) = z ^ k`.
* `MarkovTrace.gen_inv_eq_of_quadratic`,
  `MarkovTrace.markovParam_inv_eq_sub` and
  `MarkovTrace.tr_mul_ginv_of_quadratic` — the inverse stabilisation is **not
  independent once a quadratic relation is present**: if
  `g n * g n = h • g n + 1` then `g⁻¹ n = g n - h • 1`, the parameter is forced
  to `z' = z - h`, and — the substantive form — the stabilisation identity
  `tr (a * g⁻¹ n) = (z - h) * tr a` for `a ∈ H n` follows from `tr_mul_comm`,
  `tr_one` and `markov` alone, *without* using the field `markov_inv` at all.
  In the Hecke case `h = q - q⁻¹`.  That last theorem is the precise sense in
  which the fourth Markov axiom is derived rather than assumed; `markov_inv` is
  nonetheless kept as a field because the derivation needs the quadratic
  relation, which is supplied at the call site and is not part of the tower
  data, so the structure would otherwise be unable to state T3' at all.

`stabWord` is a plain definition (a word in a family of ring elements) and
carries no trace content; `stabWord_add` is the concatenation identity for it.

## Relation to existing material in this repository

This is deliberately **self-contained and Mathlib-only**, per the convention for
`QOU.MathlibExt`.  Two neighbours are worth naming so this file is not mistaken
for either:

* `QOU.MathlibExt.MarkovUnusedGenerator.MarkovTower` axiomatises the *same*
  tower shape but for a different purpose — deriving the bond rule at an unused
  interior generator — and carries neither the normalisation `tr 1 = 1`, the
  inverse generator, nor conjugation invariance.
* `QOU.MathlibExt.MarkovTrace` is a *module namespace* about the character /
  cyclicity layer on concrete Hecke matrix representations.  The structure
  defined here is `QOU.MathlibExt.OcneanuTrace.MarkovTrace`; the two share a
  final name component and nothing else.

## Conventions

The Markov parameters `z` and `z'` are **abstract ring elements** throughout.
Nothing here fixes them, so the file is convention-neutral: it is neither a
convention-C nor a convention-D statement, and instantiating `z` at either
specialises it without reproving anything.

## Base ring

Generic `[CommRing R]` acting on a generic ring `A`.  No `ℝ`, no ordering, no
square roots, no archimedean content.  The single concrete witness
`exists_markovTrace_param_ne` is stated over `ℚ` only because it needs a ring
carrying a unit that differs from its own inverse.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01393699
-/

namespace QOU.MathlibExt.OcneanuTrace

variable {R : Type*} [CommRing R]
variable {A : Type*} [Ring A] [Algebra R A]

/-! ## The axioms -/

/-- A **Markov (Ocneanu) trace** on a tower of subalgebras of `A`.

`H n` is the `n`-th algebra of the tower and `g n` is the generator adjoined at
step `n`, so `g n ∈ H (n + 1)` but in general `g n ∉ H n`.  `ginv n` is a
two-sided inverse for it, present so that the negative-crossing stabilisation
axiom can be stated.

Every field is used by a theorem below, and no field encodes any of the
conclusions: conjugation invariance, the values `tr (g n)` and `tr (ginv n)`,
iterated stabilisation, and the relation between the two Markov parameters are
all derived. -/
structure MarkovTrace (R : Type*) [CommRing R] (A : Type*) [Ring A]
    [Algebra R A] where
  /-- The tower of subalgebras `H 0 ⊆ H 1 ⊆ ⋯`. -/
  H : ℕ → Subalgebra R A
  /-- The tower is increasing. -/
  H_mono : Monotone H
  /-- The generator adjoined at step `n`. -/
  g : ℕ → A
  /-- `g n` lives one level up. -/
  g_mem : ∀ n, g n ∈ H (n + 1)
  /-- A two-sided inverse for `g n` (the negative crossing). -/
  ginv : ℕ → A
  /-- The inverse generator also lives one level up. -/
  ginv_mem : ∀ n, ginv n ∈ H (n + 1)
  /-- `ginv n` is a left inverse of `g n`. -/
  ginv_mul : ∀ n, ginv n * g n = 1
  /-- `ginv n` is a right inverse of `g n`. -/
  mul_ginv : ∀ n, g n * ginv n = 1
  /-- The trace, as an `R`-linear functional on the whole algebra. -/
  tr : A →ₗ[R] R
  /-- **(T1)** The trace property. -/
  tr_mul_comm : ∀ a b : A, tr (a * b) = tr (b * a)
  /-- **(T2)** Normalisation. -/
  tr_one : tr 1 = 1
  /-- The Markov parameter for a positive crossing. -/
  z : R
  /-- The Markov parameter for a negative crossing. -/
  zinv : R
  /-- **(T3)** Markov stabilisation, at the top of the tower. -/
  markov : ∀ n : ℕ, ∀ a ∈ H n, tr (a * g n) = z * tr a
  /-- **(T3')** Markov stabilisation by the inverse generator. -/
  markov_inv : ∀ n : ℕ, ∀ a ∈ H n, tr (a * ginv n) = zinv * tr a

/-! ## Ascending words

`stabWord` is a word in an arbitrary family of ring elements and mentions no
trace; it is defined here so that the iterated-stabilisation theorem below can be
stated once for a general stabilising family and then instantiated at both the
positive and the inverse generators. -/

/-- The ascending word `s n * s (n+1) * ⋯ * s (n+k-1)`, associated to the
left. -/
def stabWord (s : ℕ → A) (n : ℕ) : ℕ → A
  | 0 => 1
  | k + 1 => stabWord s n k * s (n + k)

@[simp] theorem stabWord_zero (s : ℕ → A) (n : ℕ) : stabWord s n 0 = 1 := rfl

theorem stabWord_succ (s : ℕ → A) (n k : ℕ) :
    stabWord s n (k + 1) = stabWord s n k * s (n + k) := rfl

/-- Concatenation: the ascending word of length `j + k` starting at `n` splits
as the length-`j` word at `n` times the length-`k` word at `n + j`. -/
theorem stabWord_add (s : ℕ → A) (n j k : ℕ) :
    stabWord s n (j + k) = stabWord s n j * stabWord s (n + j) k := by
  induction k with
  | zero => simp
  | succ k ih =>
    have hidx : n + (j + k) = n + j + k := by omega
    rw [← Nat.add_assoc j k 1, stabWord_succ, ih, stabWord_succ, hidx, mul_assoc]

namespace MarkovTrace

variable (T : MarkovTrace R A)

/-! ## Markov move I: the trace is a class function -/

/-- **Conjugation invariance.**  Only a *one-sided* inverse is needed: if
`v * u = 1` then `tr (u * x * v) = tr x`, for every `x`.  Neither `u` nor `v`
need be a unit, and `x` is arbitrary.

This is the algebraic content of Markov move I (whose topological reading is
that conjugating a braid does not change its closure — not proved here). -/
theorem tr_conj (u x v : A) (h : v * u = 1) : T.tr (u * x * v) = T.tr x := by
  rw [T.tr_mul_comm (u * x) v, ← mul_assoc, h, one_mul]

/-- Conjugation invariance in its unit form: `tr (u * x * u⁻¹) = tr x`. -/
theorem tr_conj_units (u : Aˣ) (x : A) : T.tr (↑u * x * ↑u⁻¹) = T.tr x :=
  T.tr_conj _ x _ u.inv_mul

/-- **The trace is a class function.**  Conjugate elements have equal trace. -/
theorem tr_eq_of_isConj {x y : A} (h : IsConj x y) : T.tr x = T.tr y := by
  obtain ⟨c, hc⟩ := h
  have hc' : (↑c : A) * x = y * ↑c := hc
  have hy : (↑c : A) * x * ↑(c⁻¹) = y := by
    rw [hc', mul_assoc, c.mul_inv, mul_one]
  rw [← hy, T.tr_conj_units]

/-- Conjugating by a tower generator leaves the trace unchanged. -/
theorem tr_conj_gen (n : ℕ) (x : A) : T.tr (T.g n * x * T.ginv n) = T.tr x :=
  T.tr_conj _ x _ (T.ginv_mul n)

/-- Conjugating by the inverse of a tower generator leaves the trace
unchanged. -/
theorem tr_conj_gen_inv (n : ℕ) (x : A) : T.tr (T.ginv n * x * T.g n) = T.tr x :=
  T.tr_conj _ x _ (T.mul_ginv n)

/-! ## The Markov parameters are trace values -/

/-- The positive Markov parameter is the trace of a generator.  This is where
the normalisation axiom `tr 1 = 1` is used. -/
@[simp] theorem tr_gen (n : ℕ) : T.tr (T.g n) = T.z := by
  have h := T.markov n 1 (T.H n).one_mem
  rwa [one_mul, T.tr_one, mul_one] at h

/-- The negative Markov parameter is the trace of an inverse generator. -/
@[simp] theorem tr_gen_inv (n : ℕ) : T.tr (T.ginv n) = T.zinv := by
  have h := T.markov_inv n 1 (T.H n).one_mem
  rwa [one_mul, T.tr_one, mul_one] at h

/-! ## Markov move II, iterated -/

/-- An ascending word of length `k` starting at level `n` lies in `H (n + k)`. -/
theorem stabWord_mem (s : ℕ → A) (hs : ∀ m, s m ∈ T.H (m + 1)) (n k : ℕ) :
    stabWord s n k ∈ T.H (n + k) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have h1 : stabWord s n k ∈ T.H (n + (k + 1)) :=
      T.H_mono (by omega) ih
    have h2 : s (n + k) ∈ T.H (n + (k + 1)) :=
      T.H_mono (by omega) (hs (n + k))
    exact (T.H (n + (k + 1))).mul_mem h1 h2

/-- **Iterated Markov stabilisation.**  For any family `s` that stabilises with
constant factor `c`, appending the `k` successive stabilising elements
`s n, s (n+1), …, s (n+k-1)` to an element of `H n` multiplies the trace by
`c ^ k`.

Stated for a general `(s, c)` so that it applies verbatim to the positive
generators with `c = z` and to the inverse generators with `c = z'`. -/
theorem tr_mul_stabWord (s : ℕ → A) (c : R) (hs : ∀ m, s m ∈ T.H (m + 1))
    (hstab : ∀ m : ℕ, ∀ a ∈ T.H m, T.tr (a * s m) = c * T.tr a) (n : ℕ) :
    ∀ (k : ℕ) (a : A), a ∈ T.H n → T.tr (a * stabWord s n k) = c ^ k * T.tr a := by
  intro k
  induction k with
  | zero => intro a _; simp
  | succ k ih =>
    intro a ha
    have hmem : a * stabWord s n k ∈ T.H (n + k) :=
      (T.H (n + k)).mul_mem (T.H_mono (Nat.le_add_right n k) ha)
        (T.stabWord_mem s hs n k)
    have hsplit : a * stabWord s n (k + 1) = a * stabWord s n k * s (n + k) := by
      rw [stabWord_succ, mul_assoc]
    rw [hsplit, hstab (n + k) _ hmem, ih a ha, pow_succ]
    ring

/-- Iterated stabilisation by the positive generators. -/
theorem tr_mul_genWord (n k : ℕ) (a : A) (ha : a ∈ T.H n) :
    T.tr (a * stabWord T.g n k) = T.z ^ k * T.tr a :=
  T.tr_mul_stabWord T.g T.z T.g_mem T.markov n k a ha

/-- Iterated stabilisation by the inverse generators. -/
theorem tr_mul_genInvWord (n k : ℕ) (a : A) (ha : a ∈ T.H n) :
    T.tr (a * stabWord T.ginv n k) = T.zinv ^ k * T.tr a :=
  T.tr_mul_stabWord T.ginv T.zinv T.ginv_mem T.markov_inv n k a ha

/-- The trace of a bare ascending word of `k` positive generators is `z ^ k` —
the algebraic counterpart of the `k`-fold stabilised unknot (no link is defined
here; see the module docstring). -/
theorem tr_genWord (n k : ℕ) : T.tr (stabWord T.g n k) = T.z ^ k := by
  have h := T.tr_mul_genWord n k 1 (T.H n).one_mem
  rwa [one_mul, T.tr_one, mul_one] at h

/-- The trace of a bare ascending word of `k` inverse generators is `z' ^ k`. -/
theorem tr_genInvWord (n k : ℕ) : T.tr (stabWord T.ginv n k) = T.zinv ^ k := by
  have h := T.tr_mul_genInvWord n k 1 (T.H n).one_mem
  rwa [one_mul, T.tr_one, mul_one] at h

/-! ## The fourth axiom is derived once a quadratic relation is present -/

/-- If the generator satisfies a quadratic relation `g n * g n = h • g n + 1`
— the Hecke relation, with `h = q - q⁻¹` — then its inverse is forced:
`ginv n = g n - h • 1`. -/
theorem gen_inv_eq_of_quadratic (n : ℕ) (h : R)
    (hq : T.g n * T.g n = h • T.g n + 1) :
    T.ginv n = T.g n - h • (1 : A) := by
  have hright : T.g n * (T.g n - h • (1 : A)) = 1 := by
    rw [mul_sub, hq, mul_smul_comm, mul_one, add_sub_cancel_left]
  calc T.ginv n = T.ginv n * 1 := (mul_one _).symm
    _ = T.ginv n * (T.g n * (T.g n - h • (1 : A))) := by rw [hright]
    _ = T.ginv n * T.g n * (T.g n - h • (1 : A)) := (mul_assoc _ _ _).symm
    _ = T.g n - h • (1 : A) := by rw [T.ginv_mul n, one_mul]

/-- **The negative Markov parameter is determined by the positive one** as soon
as the generator satisfies a quadratic relation: `z' = z - h`.

For the Iwahori–Hecke relation `σ² = (q - q⁻¹) σ + 1` this reads
`z' = z - (q - q⁻¹)`, i.e. the fourth Markov axiom is a consequence of the
other three rather than an independent assumption. -/
theorem markovParam_inv_eq_sub (n : ℕ) (h : R)
    (hq : T.g n * T.g n = h • T.g n + 1) :
    T.zinv = T.z - h := by
  have hval := T.tr_gen_inv n
  rw [T.gen_inv_eq_of_quadratic n h hq, map_sub, map_smul, T.tr_gen n, T.tr_one,
    smul_eq_mul, mul_one] at hval
  exact hval.symm

/-- **The inverse-stabilisation axiom itself is derived**, not merely its
parameter.  Given the quadratic relation, `tr (a * ginv n) = (z - h) * tr a` for
every `a ∈ H n`.

The proof uses only `gen_inv_eq_of_quadratic` (hence `ginv_mul`), linearity of
`tr`, and `markov` — the field `markov_inv` is **not** used, which is what makes
this the honest form of the claim that the fourth Markov axiom is a consequence
of the other three rather than an independent assumption.  `markovParam_inv_eq_sub`
is the corresponding statement about the parameter, and does go through
`markov_inv`. -/
theorem tr_mul_ginv_of_quadratic (n : ℕ) (h : R)
    (hq : T.g n * T.g n = h • T.g n + 1) (a : A) (ha : a ∈ T.H n) :
    T.tr (a * T.ginv n) = (T.z - h) * T.tr a := by
  rw [T.gen_inv_eq_of_quadratic n h hq, mul_sub, mul_smul_comm, mul_one, map_sub,
    map_smul, T.markov n a ha, smul_eq_mul, sub_mul]

end MarkovTrace

/-! ## Non-vacuity

The axioms above are satisfiable, and they do **not** force the two Markov
parameters to coincide.  The witness is the one-dimensional tower `A = R` with
every `H n = ⊤`, the generator a fixed unit `u`, and `tr = id`.  It is
commutative and says nothing about the Hecke tower — it is an inhabitation
witness only — but it is faithful (`tr 1 = 1 ≠ 0` in a nontrivial ring), so the
axioms do not collapse the trace to zero. -/

/-- The one-dimensional tower over `R` with generator a fixed unit `u`, trace the
identity, `z = u` and `z' = u⁻¹`. -/
def unitMarkovTrace (u : Rˣ) : MarkovTrace R R where
  H := fun _ => ⊤
  H_mono := fun _ _ _ => le_rfl
  g := fun _ => (u : R)
  g_mem := fun _ => by trivial
  ginv := fun _ => ((u⁻¹ : Rˣ) : R)
  ginv_mem := fun _ => by trivial
  ginv_mul := fun _ => u.inv_mul
  mul_ginv := fun _ => u.mul_inv
  tr := LinearMap.id
  tr_mul_comm := fun a b => by simpa using mul_comm a b
  tr_one := rfl
  z := (u : R)
  zinv := ((u⁻¹ : Rˣ) : R)
  markov := fun _ a _ => by simpa using mul_comm a (u : R)
  markov_inv := fun _ a _ => by simpa using mul_comm a ((u⁻¹ : Rˣ) : R)

@[simp] theorem unitMarkovTrace_z (u : Rˣ) : (unitMarkovTrace u).z = (u : R) := rfl

@[simp] theorem unitMarkovTrace_zinv (u : Rˣ) :
    (unitMarkovTrace u).zinv = ((u⁻¹ : Rˣ) : R) := rfl

@[simp] theorem unitMarkovTrace_g (u : Rˣ) (n : ℕ) :
    (unitMarkovTrace u).g n = (u : R) := rfl

/-- The witness satisfies a quadratic relation, with `h = u - u⁻¹`.  This is what
keeps the hypothesis of `MarkovTrace.gen_inv_eq_of_quadratic` and
`MarkovTrace.markovParam_inv_eq_sub` from being empty: it is inhabited, and with
`h ≠ 0` whenever `u ≠ u⁻¹`. -/
theorem unitMarkovTrace_quadratic (u : Rˣ) (n : ℕ) :
    (unitMarkovTrace u).g n * (unitMarkovTrace u).g n
      = ((u : R) - ((u⁻¹ : Rˣ) : R)) • (unitMarkovTrace u).g n + 1 := by
  simp only [unitMarkovTrace_g, smul_eq_mul, sub_mul, u.inv_mul]
  ring

/-- **The two Markov parameters are genuinely independent**: the axioms admit a
model with `z ≠ z'`, so the inverse-stabilisation axiom `markov_inv` is not a
restatement of `markov`.  Witness: the unit `2` over `ℚ`, whose inverse is
`2⁻¹ ≠ 2`. -/
theorem exists_markovTrace_param_ne : ∃ T : MarkovTrace ℚ ℚ, T.z ≠ T.zinv := by
  refine ⟨unitMarkovTrace (Units.mk0 (2 : ℚ) (by norm_num)), ?_⟩
  simp only [unitMarkovTrace_z, unitMarkovTrace_zinv, Units.val_inv_eq_inv_val,
    Units.val_mk0]
  norm_num

end QOU.MathlibExt.OcneanuTrace
