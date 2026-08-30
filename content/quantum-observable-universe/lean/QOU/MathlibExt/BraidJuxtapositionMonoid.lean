/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.FreeMonoid.Basic
import Mathlib.Algebra.Group.TypeTags.Basic
import Mathlib.Algebra.Group.Equiv.Basic
import Mathlib.Data.Sigma.Basic
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Juxtaposition of braids as a monoid

**Mathlib has no braid groups and no knot theory.** Measured against the vendored tree
(commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, 6996 modules): `find -iname '*braid*'` returns
only `CategoryTheory` files about the monoidal *braiding*; `find -iname '*Hecke*'` and
`-iname '*knot*'` return nothing; word-boundary greps for `Markov trace`, `Ocneanu`, `Temperley`,
`Kauffman`, `skein`, `Jones polynomial` and `braid closure` return zero. Two near-misses a bare grep
reports: `Mathlib.CategoryTheory.MarkovCategory` is categorical *probability* and
`Mathlib.MeasureTheory…Markov` is Markov's inequality; neither is relevant here.

This file supplies the **structural layer under trace multiplicativity**: putting two braids
side by side on disjoint strand blocks, as an algebraic operation, and the monoid it generates.

## The setting

Juxtaposition (disjoint side-by-side union, "distant union") takes a braid on `m` strands and a
braid on `n` strands to a braid on `m + n` strands. Because the index *changes*, no fixed-`n`
algebraic structure can express it: the operation lives on a family `F : ℕ → Type*` and has the
heterogeneous shape

    jux : F m → F n → F (m + n).

`Juxtaposable F` is exactly that data plus an empty braid `empty : F 0` and the three laws below.
Nothing here assumes `F n` *is* the Artin braid group, which is why the results apply verbatim to
it, to its abelianisation (the writhe), to a Hecke-type quotient, and to the word model.

## What is proved here (all theorems, no `sorry`, no axiom beyond Mathlib's)

* `instMonoidSigma` — the disjoint union `Σ n, F n` is a **monoid** under juxtaposition, with the
  empty braid as unit. This is the "juxtaposition monoid" of the title.
* `strandCount` — `Σ n, F n →* Multiplicative ℕ`, i.e. juxtaposition adds strand counts.
* `juxHom`, `juxLeft`, `juxRight` — the interchange law in `MonoidHom` form: juxtaposition is a
  monoid homomorphism `F m × F n →* F (m + n)`, and each block includes as a submonoid.
* `juxLeft_commute_juxRight` — **the two blocks do not interact**: their images commute inside
  `F (m + n)`. This is the algebraic content of far commutation `σᵢσⱼ = σⱼσᵢ` for distant `i, j`,
  and it is *derived* from the interchange law, not assumed.
* `const_interchange_iff_commutative` — the interchange law has real content: on the constant
  family it holds **iff** the fibre monoid is commutative. So `JuxtaposableMonoid` is a genuine
  restriction, not a bookkeeping tautology.
* `ofMultiplicative` / `ofMultiplicative_comp` — a functional `f` with `f (jux a b) = f a * f b`
  is **exactly** a monoid hom out of the juxtaposition monoid, and every monoid hom arises this
  way. This is the abstract home of `QOU.MathlibExt.MarkovTraceMultiplicative.markovTrace_juxtapose`
  (`tr (K₁ # K₂) = tr K₁ * tr K₂`): that file proves the hypothesis `f (jux a b) = f a * f b` for
  the matrix trace under the Kronecker model; this file says what such an `f` *is*.
  `MonoidHom.map_pow` then gives `k` disjoint copies for free.

## The index arithmetic, handled honestly

`(m + n) + k` and `m + (n + k)` are **not** definitionally equal in `ℕ` (`Nat.add` recurses on its
second argument), so `jux (jux a b) c` and `jux a (jux b c)` do not even have the same type. The
associativity axiom is therefore stated as an equality **in the sigma type** `Σ i, F i`, which
carries the index equality and the value equality together. Likewise `0 + n` does not reduce, so
the left-unit law `empty_jux` is stated in the sigma type as well.

`n + 0` *does* reduce to `n`, so the right-unit law `jux_empty` is stated directly in `F n` with no
cast. The asymmetry between `empty_jux` and `jux_empty` is not an oversight: it records exactly
where a cast is needed and where it is not.

## Non-vacuity

Two concrete models, both verified:

* `Const M` (constant family, `jux = (*)`) for a commutative monoid `M`. At `M = Multiplicative ℤ`
  this is the **writhe model** — the exponent sum of a juxtaposed braid is the sum of the exponent
  sums — and it satisfies the interchange law. `writheTotal_surjective` shows the resulting monoid
  is not degenerate.
* `WordFamily α` (words of length `n`, `jux =` concatenation) — a genuinely *dependent* family, so
  it exercises the cast the constant model does not. `wordEquiv` identifies its juxtaposition
  monoid with `FreeMonoid α`, on the nose.

`WordFamily` witnesses `Juxtaposable` only, not `JuxtaposableMonoid`, and that is not a gap in the
development: `WordFamily α n` carries no monoid structure of its own, and by
`const_interchange_iff_commutative` a free (noncommutative) multiplication could not satisfy the
interchange law in any case.

## Scope — read this before citing it

Everything below is **algebra**. That a given pair of link diagrams' connected sum is realised by
juxtaposition on disjoint strand blocks is a *modelling* statement about diagrams, not proved here
and not provable in Mathlib as it stands (there is no `Link`, no diagram, no Reidemeister move).
This file makes no topological claim.

Ground ring / typeclass: nothing stronger than `Monoid` is used; there is no ordering, no `ℝ`, and
no archimedean content.
-/

namespace QOU.MathlibExt.BraidJuxtaposition

universe u v

/-! ## The juxtaposition structure -/

/-- A **juxtaposable family**: a family of "braid-like" objects indexed by strand count, with a
side-by-side union `jux : F m → F n → F (m + n)` and an empty object on `0` strands.

The three laws are associativity, and the two unit laws. Associativity and the *left* unit law are
stated as equalities in `Σ i, F i`, because their two sides live in types indexed by
propositionally- but not definitionally-equal naturals (`(m + n) + k` vs `m + (n + k)`, and `0 + n`
vs `n`). The *right* unit law needs no such packaging, since `n + 0` reduces to `n`. -/
class Juxtaposable (F : ℕ → Type u) where
  /-- Side-by-side union of a braid on `m` strands with one on `n` strands. -/
  jux : {m n : ℕ} → F m → F n → F (m + n)
  /-- The empty braid, on zero strands. -/
  empty : F 0
  /-- Juxtaposition is associative, as an equality in `Σ i, F i` (the index equality
  `(m + n) + k = m + (n + k)` is part of the statement). -/
  jux_assoc : ∀ {m n k : ℕ} (a : F m) (b : F n) (c : F k),
    (⟨m + n + k, jux (jux a b) c⟩ : Σ i, F i) = ⟨m + (n + k), jux a (jux b c)⟩
  /-- The empty braid is a left unit, as an equality in `Σ i, F i` (`0 + n = n` is part of the
  statement, since `0 + n` does not reduce). -/
  empty_jux : ∀ {n : ℕ} (a : F n), (⟨0 + n, jux empty a⟩ : Σ i, F i) = ⟨n, a⟩
  /-- The empty braid is a right unit. No cast is needed: `n + 0` reduces to `n`. -/
  jux_empty : ∀ {n : ℕ} (a : F n), jux a empty = a

export Juxtaposable (jux empty jux_assoc empty_jux jux_empty)

variable {F : ℕ → Type u}

/-- **The juxtaposition monoid.** The disjoint union of all strand counts, `Σ n, F n`, is a monoid
under side-by-side union, with the empty braid as unit. Working on the disjoint union is what makes
juxtaposition expressible as a *homogeneous* binary operation at all. -/
instance instMonoidSigma [Juxtaposable F] : Monoid (Σ n, F n) where
  mul x y := ⟨x.1 + y.1, jux x.2 y.2⟩
  one := ⟨0, empty⟩
  mul_assoc a b c := jux_assoc a.2 b.2 c.2
  one_mul a := empty_jux a.2
  mul_one a := congrArg (Sigma.mk a.1) (jux_empty a.2)

@[simp]
theorem mk_mul_mk [Juxtaposable F] {m n : ℕ} (a : F m) (b : F n) :
    (⟨m, a⟩ : Σ i, F i) * ⟨n, b⟩ = ⟨m + n, jux a b⟩ := rfl

@[simp]
theorem one_eq_empty [Juxtaposable F] : (1 : Σ i, F i) = ⟨0, empty⟩ := rfl

/-- **Juxtaposition adds strand counts**, packaged as a monoid homomorphism to the natural numbers
under addition. This is the grading of the juxtaposition monoid. -/
def strandCount [Juxtaposable F] : (Σ n, F n) →* Multiplicative ℕ where
  toFun x := Multiplicative.ofAdd x.1
  map_one' := rfl
  map_mul' _ _ := rfl

@[simp]
theorem strandCount_mk [Juxtaposable F] {n : ℕ} (a : F n) :
    strandCount (⟨n, a⟩ : Σ i, F i) = Multiplicative.ofAdd n := rfl

/-! ## The interchange (bifunctoriality) law -/

/-- A juxtaposable family whose fibres are monoids, satisfying the **interchange law**

    jux (a * a') (b * b') = jux a b * jux a' b'.

This is the algebraic statement that the two strand blocks *do not interact*: composing inside each
block and then juxtaposing is the same as juxtaposing and then composing. For the Artin braid
groups it is the assertion that `Bₘ × Bₙ → Bₘ₊ₙ` is a group homomorphism, i.e. that the image is
the parabolic subgroup on the two blocks.

Both fields are quantified equations in the shape of the claim; see
`const_interchange_iff_commutative` for a proof that they are a genuine restriction. -/
class JuxtaposableMonoid (F : ℕ → Type u) [∀ n, Monoid (F n)] [Juxtaposable F] : Prop where
  /-- Juxtaposing the two units gives the unit. -/
  jux_one : ∀ {m n : ℕ}, jux (1 : F m) (1 : F n) = 1
  /-- The interchange law: the two blocks compose independently. -/
  jux_mul : ∀ {m n : ℕ} (a a' : F m) (b b' : F n),
    jux (a * a') (b * b') = jux a b * jux a' b'

section Interchange

variable [∀ n, Monoid (F n)] [Juxtaposable F] [JuxtaposableMonoid F] {m n : ℕ}

/-- **Juxtaposition is a monoid homomorphism out of the product of the two blocks.** This is the
interchange law repackaged; it is the precise sense in which `jux` is bifunctorial. -/
def juxHom (m n : ℕ) : F m × F n →* F (m + n) where
  toFun p := jux p.1 p.2
  map_one' := JuxtaposableMonoid.jux_one
  map_mul' p q := JuxtaposableMonoid.jux_mul p.1 q.1 p.2 q.2

@[simp]
theorem juxHom_apply (a : F m) (b : F n) : juxHom m n (a, b) = jux a b := rfl

/-- The **left block inclusion** `F m →* F (m + n)`: pad on the right with `n` trivial strands. -/
def juxLeft (m n : ℕ) : F m →* F (m + n) where
  toFun a := jux a (1 : F n)
  map_one' := JuxtaposableMonoid.jux_one
  map_mul' a a' := by
    have h := JuxtaposableMonoid.jux_mul a a' (1 : F n) 1
    rwa [one_mul] at h

/-- The **right block inclusion** `F n →* F (m + n)`: pad on the left with `m` trivial strands. -/
def juxRight (m n : ℕ) : F n →* F (m + n) where
  toFun b := jux (1 : F m) b
  map_one' := JuxtaposableMonoid.jux_one
  map_mul' b b' := by
    have h := JuxtaposableMonoid.jux_mul (1 : F m) 1 b b'
    rwa [one_mul] at h

@[simp] theorem juxLeft_apply (a : F m) : juxLeft m n a = jux a (1 : F n) := rfl

@[simp] theorem juxRight_apply (b : F n) : juxRight m n b = jux (1 : F m) b := rfl

/-- A juxtaposition factors as *left block* times *right block*. -/
theorem jux_eq_juxLeft_mul_juxRight (a : F m) (b : F n) :
    jux a b = juxLeft m n a * juxRight m n b := by
  have h := JuxtaposableMonoid.jux_mul a 1 (1 : F n) b
  rwa [mul_one, one_mul] at h

/-- The same juxtaposition factors in the *other* order too. -/
theorem jux_eq_juxRight_mul_juxLeft (a : F m) (b : F n) :
    jux a b = juxRight m n b * juxLeft m n a := by
  have h := JuxtaposableMonoid.jux_mul (1 : F m) a b (1 : F n)
  rwa [one_mul, mul_one] at h

/-- **The two blocks do not interact.** The images of the two block inclusions commute inside
`F (m + n)`. For braid groups this is far commutation, `σᵢ σⱼ = σⱼ σᵢ` when `i` and `j` lie in
different blocks — and here it is a *consequence* of the interchange law, not an extra axiom. -/
theorem juxLeft_commute_juxRight (a : F m) (b : F n) :
    Commute (juxLeft m n a) (juxRight m n b) :=
  ((jux_eq_juxLeft_mul_juxRight a b).symm.trans (jux_eq_juxRight_mul_juxLeft a b))

end Interchange

/-- **The interchange law is not automatic.** For the constant family with `jux = (*)`, the
interchange law holds if and only if the fibre monoid is commutative. So `JuxtaposableMonoid` is a
real constraint: a noncommutative fibre with `jux = (*)` refutes it. -/
theorem const_interchange_iff_commutative (M : Type u) [Monoid M] :
    (∀ a a' b b' : M, a * a' * (b * b') = a * b * (a' * b')) ↔ ∀ x y : M, x * y = y * x := by
  constructor
  · intro h x y
    have := h 1 x y 1
    simpa using this
  · intro h a a' b b'
    rw [mul_assoc, mul_assoc]
    congr 1
    rw [← mul_assoc, h a' b, mul_assoc]

/-! ## Multiplicative functionals are monoid homs on the juxtaposition monoid -/

section Functional

variable [Juxtaposable F] {M : Type v} [Monoid M]

/-- **A juxtaposition-multiplicative functional is a monoid hom out of the juxtaposition monoid.**

Given a family of functionals `f n : F n → M` that is normalised on the empty braid and turns
juxtaposition into multiplication, `ofMultiplicative` assembles it into a genuine
`(Σ n, F n) →* M`.

This is the abstract statement behind
`QOU.MathlibExt.MarkovTraceMultiplicative.markovTrace_juxtapose`: that file discharges the
hypothesis `hmul` for the matrix trace on the Kronecker model of disjoint strands; this
construction is what the hypothesis buys you. In particular `MonoidHom.map_pow` immediately gives
the value on `k` disjoint copies of one component. -/
def ofMultiplicative (f : (n : ℕ) → F n → M) (hone : f 0 empty = 1)
    (hmul : ∀ {m n : ℕ} (a : F m) (b : F n), f (m + n) (jux a b) = f m a * f n b) :
    (Σ n, F n) →* M where
  toFun x := f x.1 x.2
  map_one' := hone
  map_mul' x y := hmul x.2 y.2

@[simp]
theorem ofMultiplicative_apply (f : (n : ℕ) → F n → M) (hone : f 0 empty = 1)
    (hmul : ∀ {m n : ℕ} (a : F m) (b : F n), f (m + n) (jux a b) = f m a * f n b)
    {n : ℕ} (a : F n) :
    ofMultiplicative f hone hmul ⟨n, a⟩ = f n a := rfl

/-- **Conversely, every monoid hom out of the juxtaposition monoid is multiplicative under
juxtaposition.** Together with `ofMultiplicative_comp` this says the two notions coincide. -/
theorem map_jux (φ : (Σ n, F n) →* M) {m n : ℕ} (a : F m) (b : F n) :
    φ ⟨m + n, jux a b⟩ = φ ⟨m, a⟩ * φ ⟨n, b⟩ :=
  φ.map_mul ⟨m, a⟩ ⟨n, b⟩

/-- **`ofMultiplicative` is surjective onto the monoid homs**: every `φ : (Σ n, F n) →* M` is
`ofMultiplicative` applied to its own restriction to the fibres. With `map_jux` this makes the
correspondence between juxtaposition-multiplicative functionals and monoid homs a bijection. -/
theorem ofMultiplicative_comp (φ : (Σ n, F n) →* M) :
    ofMultiplicative (fun n a => φ ⟨n, a⟩) φ.map_one
      (fun {_m _n} a b => map_jux φ a b) = φ := by
  ext x
  rfl

end Functional

/-! ## Non-vacuity, model 1: the constant family (the writhe model) -/

/-- The constant family `n ↦ M`: every strand count carries the same object. -/
abbrev Const (M : Type u) (_ : ℕ) : Type u := M

/-- The transport lemma for a constant family: since `Const M i` does not depend on `i`, an index
equality and a value equality assemble into an equality in `Σ n, Const M n` with no `HEq`. Stated
with `i j` universally quantified precisely so that `subst` applies. -/
private theorem sigma_const_eq {M : Type u} {i j : ℕ} (h : i = j) {a b : M} (hab : a = b) :
    (⟨i, a⟩ : Σ n, Const M n) = ⟨j, b⟩ := by
  subst h; subst hab; rfl

/-- Any commutative monoid gives a juxtaposable constant family, with `jux` the multiplication.
The two sigma-level laws go through `sigma_const_eq`, since the family does not actually depend on
the index. -/
instance instJuxtaposableConst (M : Type u) [CommMonoid M] : Juxtaposable (Const M) where
  jux a b := a * b
  empty := 1
  jux_assoc a b c := sigma_const_eq (Nat.add_assoc _ _ _) (mul_assoc a b c)
  empty_jux a := sigma_const_eq (Nat.zero_add _) (one_mul a)
  jux_empty a := mul_one a

@[simp]
theorem const_jux (M : Type u) [CommMonoid M] {m n : ℕ} (a : Const M m) (b : Const M n) :
    jux a b = a * b := rfl

@[simp]
theorem const_empty (M : Type u) [CommMonoid M] : (empty : Const M 0) = 1 := rfl

/-- The constant family on a commutative monoid satisfies the interchange law. By
`const_interchange_iff_commutative` commutativity is not merely convenient here — it is exactly
what the interchange law demands of this model. -/
instance instJuxtaposableMonoidConst (M : Type u) [CommMonoid M] :
    JuxtaposableMonoid (Const M) where
  jux_one := one_mul 1
  jux_mul a a' b b' := mul_mul_mul_comm a a' b b'

/-- The **writhe model**: every strand count carries `ℤ` written multiplicatively, and juxtaposition
adds writhes. This is the abelianisation picture — the exponent sum of a braid word is additive
under disjoint union — and it is a faithful model of `JuxtaposableMonoid`. -/
abbrev WritheFamily : ℕ → Type := Const (Multiplicative ℤ)

/-- Total writhe of a juxtaposed system, as a monoid hom out of the juxtaposition monoid. -/
def writheTotal : (Σ n, WritheFamily n) →* Multiplicative ℤ :=
  ofMultiplicative (fun _ a => a) rfl (fun _ _ => rfl)

/-- **The writhe model is non-degenerate**: its juxtaposition monoid surjects onto `ℤ`, so the
model is very far from a one-point family. -/
theorem writheTotal_surjective : Function.Surjective writheTotal :=
  fun z => ⟨⟨0, z⟩, rfl⟩

/-- Every strand count is realised in the writhe model. -/
theorem writhe_strandCount_surjective :
    Function.Surjective (strandCount (F := WritheFamily)) :=
  fun k => ⟨⟨Multiplicative.toAdd k, 1⟩, rfl⟩

/-- The writhe model computes: juxtaposing a `+3` block with a `+4` block gives `+7` on the
combined strand count. -/
example : (jux (Multiplicative.ofAdd (3 : ℤ)) (Multiplicative.ofAdd (4 : ℤ)) :
    Const (Multiplicative ℤ) (1 + 2)) = Multiplicative.ofAdd (7 : ℤ) := rfl

/-! ## Non-vacuity, model 2: words (a genuinely dependent family) -/

/-- Words of length `n` in an alphabet `α`. Unlike `Const`, this family really depends on the
index, so it exercises the casts in `jux_assoc` and `empty_jux`. -/
abbrev WordFamily (α : Type u) (n : ℕ) : Type u := { l : List α // l.length = n }

/-- **Concatenation makes words juxtaposable.** The two sigma-level laws are `List.append_assoc`
and `List.nil_append` transported by `Sigma.subtype_ext`; the right-unit law is `List.append_nil`
with no transport at all, because `n + 0` reduces. -/
instance instJuxtaposableWord (α : Type u) : Juxtaposable (WordFamily α) where
  jux a b := ⟨a.1 ++ b.1, by simp [a.2, b.2]⟩
  empty := ⟨[], rfl⟩
  jux_assoc a b c := Sigma.subtype_ext (Nat.add_assoc _ _ _) (List.append_assoc a.1 b.1 c.1)
  empty_jux a := Sigma.subtype_ext (Nat.zero_add _) (List.nil_append a.1)
  jux_empty a := Subtype.ext (List.append_nil a.1)

@[simp]
theorem word_jux_val (α : Type u) {m n : ℕ} (a : WordFamily α m) (b : WordFamily α n) :
    (jux a b).1 = a.1 ++ b.1 := rfl

/-- The word model computes, and so does the monoid multiplication assembled from it: a word of
length `2` juxtaposed with a word of length `1` lands at strand count `3` with the concatenated
word. -/
example : ((⟨2, ⟨[1, 2], rfl⟩⟩ : Σ n, WordFamily ℕ n) * ⟨1, ⟨[3], rfl⟩⟩).1 = 3 := rfl

example : ((⟨2, ⟨[1, 2], rfl⟩⟩ : Σ n, WordFamily ℕ n) * ⟨1, ⟨[3], rfl⟩⟩).2.1 = [1, 2, 3] := rfl

/-- Reading off the underlying word is a monoid hom from the word model's juxtaposition monoid to
the free monoid on `α`. -/
def wordTotal (α : Type u) : (Σ n, WordFamily α n) →* FreeMonoid α :=
  ofMultiplicative (fun _ a => FreeMonoid.ofList a.1) rfl (fun _ _ => rfl)

theorem wordTotal_injective (α : Type u) : Function.Injective (wordTotal α) := by
  rintro ⟨m, a⟩ ⟨n, b⟩ h
  have hval : a.1 = b.1 := h
  have hmn : m = n := by rw [← a.2, ← b.2, hval]
  exact Sigma.subtype_ext hmn hval

theorem wordTotal_surjective (α : Type u) : Function.Surjective (wordTotal α) :=
  fun l => ⟨⟨(FreeMonoid.toList l).length, ⟨FreeMonoid.toList l, rfl⟩⟩, rfl⟩

/-- **The juxtaposition monoid of the word model is the free monoid.** This pins the abstract
construction down completely on a dependent family: `Σ n, WordFamily α n` under side-by-side union
is `FreeMonoid α`, on the nose. In particular the juxtaposition monoid is in general
noncommutative and infinite, so `Juxtaposable` is very far from vacuous. -/
noncomputable def wordEquiv (α : Type u) : (Σ n, WordFamily α n) ≃* FreeMonoid α :=
  MulEquiv.ofBijective (wordTotal α) ⟨wordTotal_injective α, wordTotal_surjective α⟩

end QOU.MathlibExt.BraidJuxtaposition
