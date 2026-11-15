/-
# Which binding functional can carry a pair term at Vassiliev type two

Bean `qou-zlra` (sign convention of the graded binding), closing the sign-dependent
half of `qou-oooq`'s type-two result.

`the_asymmetry_term_lives_at_vassiliev_type_two_probe` (bean `qou-oooq`) found that
for the chain trace written as a product of bond factors
`P(h) = ∏ᵢ fᵢ(h)`, `fᵢ = z₀ + bᵢ h + cᵢ h² + …`, the type-two coefficient carries a
**pair convolution** `Σ_{i<j} bᵢ bⱼ` — quadratic in the bond counts, hence in
`N − Z` — while `−log P` does not.  The bean asked whether the framework reads
binding as `+c₂`, `−c₂`, or as a logarithm, because the probe's sign was chosen
rather than derived.

This file proves that the question of the **sign** is empty for every
**product-additive** functional (any `F` with `F (f·g) = F f + F g`: `log`, `−log`,
`α·log` for any `α`), and that the pair term is present in the **bare** coefficient
of the product for every sign.  Concretely, on the ring `R[h]/(h³)` of 2-jets:

* `prod_c2` — the `h²` coefficient of a product of jets with unit constant term is
  `Σᵢ cᵢ + e₂(b)`, where `e₂(b) = Σ_{i<j} bᵢ bⱼ` is the second elementary
  symmetric function of the `h¹` coefficients;
* `e2_append` — `e₂` of a concatenation carries the **cross term**
  `(Σ l₁)(Σ l₂)`, so splitting the bonds by type gives a product of two counts;
* `additive_prod` — any product-additive `F` satisfies `F (∏ fᵢ) = Σᵢ F fᵢ`, so its
  `h²` coefficient is a sum of per-factor terms and carries **no** pair term; the
  sign and scale of `F` never enter;
* `logJet_mul` / `logJet_c2_prod` — the formal logarithm is such an `F`, and
  its `h²` coefficient is exactly `Σᵢ (cᵢ − bᵢ²/2)`: the identity
  `(Σb)² = Σb² + 2e₂(b)` (`sq_sum_eq`) is what removes the pair term;
* `neg_additive` / `smul_additive` — `−F` and `α • F` are additive whenever `F` is, so `+log`
  and `−log` are the same case.

Base ring (§7c): the jet ring and the pair-term identities need only
`[CommRing R]`; the formal logarithm needs `1/2` and lives over a `[Field K]`
with `[NeZero (2 : K)]`.  Nothing here is archimedean.  The corpus's functional
choice itself is stated in `QOU.Mass.MarkovBondRuleForcesPairwise.bindingOfTrace`
(`B = −α · ln (tr_atom / tr_free)`) and in `QOU.Mass.ChainTraceFactor.L_pp/L_nn/L_pn`;
this file says what that choice does to the type-two shape.

Ref: [leitner2026] docs/audits/2026-09-12-graded-binding-sign-convention.md
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

namespace QOU.Mass.GradedBindingFunctionalPairTerm

/-! ## The ring of 2-jets `R[h]/(h³)` -/

/-- A 2-jet `c0 + c1·h + c2·h²` modulo `h³`. -/
@[ext]
structure Jet2 (R : Type*) where
  c0 : R
  c1 : R
  c2 : R

namespace Jet2

variable {R : Type*} [CommRing R]

/-- Truncated product: coefficients of `(f·g) mod h³`. -/
instance : Mul (Jet2 R) where
  mul f g := ⟨f.c0 * g.c0, f.c0 * g.c1 + f.c1 * g.c0,
    f.c0 * g.c2 + f.c1 * g.c1 + f.c2 * g.c0⟩

instance : One (Jet2 R) where
  one := ⟨1, 0, 0⟩

instance : Add (Jet2 R) where
  add f g := ⟨f.c0 + g.c0, f.c1 + g.c1, f.c2 + g.c2⟩

instance : Zero (Jet2 R) where
  zero := ⟨0, 0, 0⟩

instance : Neg (Jet2 R) where
  neg f := ⟨-f.c0, -f.c1, -f.c2⟩

@[simp] theorem mul_c0 (f g : Jet2 R) : (f * g).c0 = f.c0 * g.c0 := rfl
@[simp] theorem mul_c1 (f g : Jet2 R) : (f * g).c1 = f.c0 * g.c1 + f.c1 * g.c0 := rfl
@[simp] theorem mul_c2 (f g : Jet2 R) :
    (f * g).c2 = f.c0 * g.c2 + f.c1 * g.c1 + f.c2 * g.c0 := rfl
@[simp] theorem one_c0 : (1 : Jet2 R).c0 = 1 := rfl
@[simp] theorem one_c1 : (1 : Jet2 R).c1 = 0 := rfl
@[simp] theorem one_c2 : (1 : Jet2 R).c2 = 0 := rfl
@[simp] theorem add_c0 (f g : Jet2 R) : (f + g).c0 = f.c0 + g.c0 := rfl
@[simp] theorem add_c1 (f g : Jet2 R) : (f + g).c1 = f.c1 + g.c1 := rfl
@[simp] theorem add_c2 (f g : Jet2 R) : (f + g).c2 = f.c2 + g.c2 := rfl
@[simp] theorem zero_c0 : (0 : Jet2 R).c0 = 0 := rfl
@[simp] theorem zero_c1 : (0 : Jet2 R).c1 = 0 := rfl
@[simp] theorem zero_c2 : (0 : Jet2 R).c2 = 0 := rfl
@[simp] theorem neg_c0 (f : Jet2 R) : (-f).c0 = -f.c0 := rfl
@[simp] theorem neg_c1 (f : Jet2 R) : (-f).c1 = -f.c1 := rfl
@[simp] theorem neg_c2 (f : Jet2 R) : (-f).c2 = -f.c2 := rfl

instance : CommMonoid (Jet2 R) where
  mul_assoc f g k := by ext <;> simp <;> ring
  one_mul f := by ext <;> simp
  mul_one f := by ext <;> simp
  mul_comm f g := by ext <;> simp <;> ring

instance : AddCommMonoid (Jet2 R) where
  add_assoc f g k := by ext <;> simp <;> ring
  zero_add f := by ext <;> simp
  add_zero f := by ext <;> simp
  add_comm f g := by ext <;> simp <;> ring
  nsmul := nsmulRec

/-- The jets with unit constant term — the normalised factors `fᵢ/z₀`, i.e. the
objects whose `h²` coefficient is the probe's `c₂/c₀`. -/
def IsUnital (f : Jet2 R) : Prop := f.c0 = 1

theorem IsUnital.mul {f g : Jet2 R} (hf : f.IsUnital) (hg : g.IsUnital) :
    (f * g).IsUnital := by
  unfold IsUnital at *
  simp [hf, hg]

theorem IsUnital.one : (1 : Jet2 R).IsUnital := rfl

theorem isUnital_prod (l : List (Jet2 R)) (h : ∀ f ∈ l, f.IsUnital) :
    l.prod.IsUnital := by
  induction l with
  | nil => exact IsUnital.one
  | cons f l ih =>
    rw [List.prod_cons]
    exact (h f (List.mem_cons_self ..)).mul
      (ih fun g hg => h g (List.mem_cons_of_mem _ hg))

end Jet2

/-! ## The second elementary symmetric function -/

variable {R : Type*} [CommRing R]

/-- `e₂ [b₁, …, bₙ] = Σ_{i<j} bᵢ bⱼ`, the pair convolution. -/
def e2 : List R → R
  | [] => 0
  | b :: bs => b * bs.sum + e2 bs

@[simp] theorem e2_nil : e2 ([] : List R) = 0 := rfl
@[simp] theorem e2_cons (b : R) (bs : List R) : e2 (b :: bs) = b * bs.sum + e2 bs := rfl

/-- **The cross term.** Splitting the factors into two classes (say the `pp` bonds
and the `nn` bonds), `e₂` picks up the product of the two class sums — a product
of two bond **counts** once each class is a repeated factor. -/
theorem e2_append (l₁ l₂ : List R) :
    e2 (l₁ ++ l₂) = e2 l₁ + e2 l₂ + l₁.sum * l₂.sum := by
  induction l₁ with
  | nil => simp
  | cons b bs ih =>
    simp only [List.cons_append, e2_cons, List.sum_append, List.sum_cons, ih]
    ring

/-- `e₂` of `n` copies of `b`: `2·e₂ = n(n−1)·b²` — quadratic in the count. -/
theorem two_mul_e2_replicate (n : ℕ) (b : R) :
    2 * e2 (List.replicate n b) = (n : R) * ((n : R) - 1) * b ^ 2 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [List.replicate_succ, e2_cons, List.sum_replicate, nsmul_eq_mul]
    push_cast
    linear_combination ih

/-- `(Σ b)² = Σ b² + 2 e₂(b)`. This identity is what the logarithm uses to
remove the pair term. -/
theorem sq_sum_eq (l : List R) :
    l.sum ^ 2 = (l.map fun b => b ^ 2).sum + 2 * e2 l := by
  induction l with
  | nil => simp
  | cons b bs ih =>
    simp only [List.sum_cons, List.map_cons, e2_cons]
    linear_combination ih

/-! ## The bare coefficient of a product carries the pair term -/

open Jet2

theorem prod_c0 (l : List (Jet2 R)) (h : ∀ f ∈ l, f.IsUnital) : l.prod.c0 = 1 :=
  isUnital_prod l h

theorem prod_c1 (l : List (Jet2 R)) (h : ∀ f ∈ l, f.IsUnital) :
    l.prod.c1 = (l.map Jet2.c1).sum := by
  induction l with
  | nil => simp
  | cons f l ih =>
    have hf : f.c0 = 1 := h f (List.mem_cons_self ..)
    have hl : ∀ g ∈ l, g.IsUnital := fun g hg => h g (List.mem_cons_of_mem _ hg)
    rw [List.prod_cons, mul_c1, hf, prod_c0 l hl, ih hl]
    simp [add_comm]

/-- **The pair term.** For factors with unit constant term,
`[h²] ∏ fᵢ = Σᵢ cᵢ + Σ_{i<j} bᵢ bⱼ`: the bare type-two coefficient is the sum of
the per-factor type-two coefficients **plus the pair convolution of the type-one
ones**. This holds for `+∏` and, by negation, for `−∏`; the sign does not remove it. -/
theorem prod_c2 (l : List (Jet2 R)) (h : ∀ f ∈ l, f.IsUnital) :
    l.prod.c2 = (l.map Jet2.c2).sum + e2 (l.map Jet2.c1) := by
  induction l with
  | nil => simp
  | cons f l ih =>
    have hf : f.c0 = 1 := h f (List.mem_cons_self ..)
    have hl : ∀ g ∈ l, g.IsUnital := fun g hg => h g (List.mem_cons_of_mem _ hg)
    rw [List.prod_cons, mul_c2, hf, prod_c0 l hl, prod_c1 l hl, ih hl]
    simp only [List.map_cons, List.sum_cons, e2_cons]
    ring

/-- The pair term of the negated product is minus the pair term: flipping the
sign convention (`+c₂` versus `−c₂`) does not remove the quadratic, it flips it. -/
theorem neg_prod_c2 (l : List (Jet2 R)) (h : ∀ f ∈ l, f.IsUnital) :
    (-l.prod).c2 = -((l.map Jet2.c2).sum + e2 (l.map Jet2.c1)) := by
  rw [neg_c2, prod_c2 l h]

/-- The chain census: `n_pp` copies of the `pp` factor, `n_pn` of `pn`, `n_nn` of
`nn`. The pair term is a **quadratic form in the three counts** with cross terms
`n_pp n_pn b_pp b_pn`, `n_pp n_nn b_pp b_nn`, `n_pn n_nn b_pn b_nn`. Stated with the
factor `2` to stay over a ring (`C(n,2)` needs division). -/
theorem two_mul_e2_census (npp npn nnn : ℕ) (bpp bpn bnn : R) :
    2 * e2 (List.replicate npp bpp ++ List.replicate npn bpn ++ List.replicate nnn bnn)
      = (npp : R) * ((npp : R) - 1) * bpp ^ 2
        + (npn : R) * ((npn : R) - 1) * bpn ^ 2
        + (nnn : R) * ((nnn : R) - 1) * bnn ^ 2
        + 2 * ((npp : R) * bpp) * ((npn : R) * bpn)
        + 2 * ((npp : R) * bpp + (npn : R) * bpn) * ((nnn : R) * bnn) := by
  rw [e2_append, e2_append, List.sum_append, List.sum_replicate, List.sum_replicate,
    List.sum_replicate, nsmul_eq_mul, nsmul_eq_mul, nsmul_eq_mul]
  have h1 := two_mul_e2_replicate npp bpp
  have h2 := two_mul_e2_replicate npn bpn
  have h3 := two_mul_e2_replicate nnn bnn
  linear_combination h1 + h2 + h3

/-! ## Any product-additive functional carries no pair term -/

/-- `F` carries products to sums — the Cauchy condition, and nothing more (the same
hypothesis as `QOU.Mass.MarkovBondRuleForcesPairwise.IsAdditiveOnProducts`). -/
def IsAdditiveOnProducts {S : Type*} [AddCommMonoid S] (F : Jet2 R → S) : Prop :=
  ∀ f g : Jet2 R, F (f * g) = F f + F g

/-- Under the Cauchy condition `F (∏ fᵢ) = Σᵢ F fᵢ` **provided** `F 1 = 0`. Every
coefficient of the image is then a sum of per-factor terms: there is no pair
term, whatever `F` is and whatever its sign. -/
theorem additive_prod {S : Type*} [AddCommMonoid S] (F : Jet2 R → S)
    (hF : IsAdditiveOnProducts F) (h1 : F 1 = 0) (l : List (Jet2 R)) :
    F l.prod = (l.map F).sum := by
  induction l with
  | nil => simpa using h1
  | cons f l ih => rw [List.prod_cons, hF, ih, List.map_cons, List.sum_cons]

/-- The census form of `additive_prod`: an additive functional of the chain product
is **linear** in the three bond counts. Contrast `two_mul_e2_census`. -/
theorem additive_census {S : Type*} [AddCommMonoid S] (F : Jet2 R → S)
    (hF : IsAdditiveOnProducts F) (h1 : F 1 = 0) (npp npn nnn : ℕ)
    (fpp fpn fnn : Jet2 R) :
    F (List.replicate npp fpp ++ List.replicate npn fpn ++ List.replicate nnn fnn).prod
      = npp • F fpp + npn • F fpn + nnn • F fnn := by
  rw [additive_prod F hF h1, List.map_append, List.map_append, List.sum_append,
    List.sum_append, List.map_replicate, List.map_replicate, List.map_replicate,
    List.sum_replicate, List.sum_replicate, List.sum_replicate]

/-- Negation preserves the Cauchy condition: `−F` is additive when `F` is. So the
`+log` and `−log` readings are one case. -/
theorem neg_additive {S : Type*} [AddCommGroup S] (F : Jet2 R → S)
    (hF : IsAdditiveOnProducts F) : IsAdditiveOnProducts (fun f => -F f) := by
  intro f g
  show -F (f * g) = -F f + -F g
  rw [hF, neg_add]

/-- Scaling preserves the Cauchy condition: `α • F` is additive when `F` is. So the
overall energy scale (`E₀`, `α`, `m_e H_q(λ) u_λ`) never enters the shape question. -/
theorem smul_additive {S : Type*} [AddCommMonoid S] {A : Type*} [Monoid A]
    [DistribMulAction A S] (α : A) (F : Jet2 R → S)
    (hF : IsAdditiveOnProducts F) : IsAdditiveOnProducts (fun f => α • F f) := by
  intro f g
  show α • F (f * g) = α • F f + α • F g
  rw [hF, smul_add]

/-! ## The formal logarithm is such a functional -/

section Log

variable {K : Type*} [Field K]

/-- The formal logarithm of a unital 2-jet, `log (1 + b h + c h²) = b h + (c − b²/2) h²`. -/
def logJet (f : Jet2 K) : Jet2 K := ⟨0, f.c1, f.c2 - f.c1 ^ 2 / 2⟩

@[simp] theorem logJet_c0 (f : Jet2 K) : (logJet f).c0 = 0 := rfl
@[simp] theorem logJet_c1 (f : Jet2 K) : (logJet f).c1 = f.c1 := rfl
@[simp] theorem logJet_c2 (f : Jet2 K) : (logJet f).c2 = f.c2 - f.c1 ^ 2 / 2 := rfl

theorem logJet_one : logJet (1 : Jet2 K) = 0 := by
  ext <;> simp

/-- `log (f·g) = log f + log g` on unital jets: the cross term `b b'` produced by
the product is cancelled exactly by `−(b + b')²/2`. -/
theorem logJet_mul [NeZero (2 : K)] {f g : Jet2 K} (hf : f.IsUnital) (hg : g.IsUnital) :
    logJet (f * g) = logJet f + logJet g := by
  unfold IsUnital at hf hg
  ext
  · simp
  · simp [hf, hg, add_comm]
  · simp only [logJet_c2, mul_c2, mul_c1, hf, hg, add_c2]
    have h2 : (2 : K) ≠ 0 := NeZero.ne _
    field_simp
    ring

/-- `log` of a product of unital jets is the sum of the logs. -/
theorem logJet_prod [NeZero (2 : K)] (l : List (Jet2 K)) (h : ∀ f ∈ l, f.IsUnital) :
    logJet l.prod = (l.map logJet).sum := by
  induction l with
  | nil => simpa using logJet_one
  | cons f l ih =>
    have hf := h f (List.mem_cons_self ..)
    have hl : ∀ g ∈ l, g.IsUnital := fun g hg => h g (List.mem_cons_of_mem _ hg)
    rw [List.prod_cons, logJet_mul hf (isUnital_prod l hl), ih hl, List.map_cons,
      List.sum_cons]

/-- **The `h²` coefficient of `log ∏ fᵢ` is `Σᵢ (cᵢ − bᵢ²/2)`** — per-factor, no pair
term. Compare `prod_c2`: the difference between the two is exactly `e₂(b)`, and the
identity that removes it is `sq_sum_eq`. -/
theorem logJet_c2_prod [NeZero (2 : K)] (l : List (Jet2 K)) (h : ∀ f ∈ l, f.IsUnital) :
    (logJet l.prod).c2 = (l.map fun f => f.c2 - f.c1 ^ 2 / 2).sum := by
  rw [logJet_c2, prod_c2 l h, prod_c1 l h, sq_sum_eq]
  have h2 : (2 : K) ≠ 0 := NeZero.ne _
  have hsum : ∀ (m : List (Jet2 K)),
      (m.map fun f => f.c2 - f.c1 ^ 2 / 2).sum
        = (m.map Jet2.c2).sum - ((m.map Jet2.c1).map fun b => b ^ 2).sum / 2 := by
    intro m
    induction m with
    | nil => simp
    | cons f m ih =>
      simp only [List.map_cons, List.sum_cons, ih]
      ring
  rw [hsum]
  field_simp
  ring

/-- The census form: the type-two piece of `log` of the chain product is **linear**
in `(n_pp, n_pn, n_nn)`, with no cross term — for `+log` (this statement) and,
by `neg_c2`, for `−log`. -/
theorem logJet_c2_census [NeZero (2 : K)] (npp npn nnn : ℕ) (fpp fpn fnn : Jet2 K)
    (hpp : fpp.IsUnital) (hpn : fpn.IsUnital) (hnn : fnn.IsUnital) :
    (logJet (List.replicate npp fpp ++ List.replicate npn fpn
        ++ List.replicate nnn fnn).prod).c2
      = (npp : K) * (fpp.c2 - fpp.c1 ^ 2 / 2) + (npn : K) * (fpn.c2 - fpn.c1 ^ 2 / 2)
        + (nnn : K) * (fnn.c2 - fnn.c1 ^ 2 / 2) := by
  have hall : ∀ f ∈ List.replicate npp fpp ++ List.replicate npn fpn
      ++ List.replicate nnn fnn, f.IsUnital := by
    intro f hf
    simp only [List.mem_append, List.mem_replicate] at hf
    rcases hf with (⟨_, rfl⟩ | ⟨_, rfl⟩) | ⟨_, rfl⟩ <;> assumption
  rw [logJet_c2_prod _ hall, List.map_append, List.map_append, List.sum_append,
    List.sum_append, List.map_replicate, List.map_replicate, List.map_replicate,
    List.sum_replicate, List.sum_replicate, List.sum_replicate, nsmul_eq_mul,
    nsmul_eq_mul, nsmul_eq_mul]

/-- The same for `−log`: still linear in the counts. The sign convention the bean
asks about changes the sign of every term and creates no cross term. -/
theorem neg_logJet_c2_census [NeZero (2 : K)] (npp npn nnn : ℕ) (fpp fpn fnn : Jet2 K)
    (hpp : fpp.IsUnital) (hpn : fpn.IsUnital) (hnn : fnn.IsUnital) :
    (-logJet (List.replicate npp fpp ++ List.replicate npn fpn
        ++ List.replicate nnn fnn).prod).c2
      = -((npp : K) * (fpp.c2 - fpp.c1 ^ 2 / 2) + (npn : K) * (fpn.c2 - fpn.c1 ^ 2 / 2)
        + (nnn : K) * (fnn.c2 - fnn.c1 ^ 2 / 2)) := by
  rw [neg_c2, logJet_c2_census npp npn nnn fpp fpn fnn hpp hpn hnn]

end Log

#print axioms prod_c2
#print axioms two_mul_e2_census
#print axioms additive_census
#print axioms logJet_mul
#print axioms logJet_c2_prod
#print axioms logJet_c2_census
#print axioms neg_logJet_c2_census

end QOU.Mass.GradedBindingFunctionalPairTerm
