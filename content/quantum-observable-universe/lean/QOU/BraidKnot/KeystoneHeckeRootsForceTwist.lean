import QOU.BraidKnot.KeystoneModularTwist

/-!
# The Hecke relation's two roots FORCE the twist on the 1-dimensional blocks

`KeystoneModularTwist.lean` builds the modular `T`-matrix `θ_λ := q^{c(λ)}` and proves its
transpose law, but its header hedges: *"for the Hecke MTC the exponent is **(up to convention)**
the content sum"*. Nothing in the corpus discharged that hedge — the exponent was **defined**,
not derived, so `θ` was a definition wearing a physical name.

This file discharges the hedge **for the two one-dimensional blocks**, from the corpus's own
Hecke convention `(σᵢ − q)(σᵢ + q⁻¹) = 0` and nothing else.

## The argument

A one-dimensional representation sends every `σᵢ` to a scalar `s` satisfying the Hecke relation.
Over a field that relation has **exactly two** roots — `isHeckeRoot_iff` — namely `q` (trivial)
and `−q⁻¹` (sign). There is no third choice and no free parameter.

The full twist `Δ² = (σ₁σ₂⋯σ_{n−1})^n` is a **positive** braid word of length `n(n−1)`, so on a
one-dimensional rep it acts by `s^{n(n−1)}`. Then:

* trivial root: `q^{n(n−1)}`;
* sign root: `(−q⁻¹)^{n(n−1)} = q^{−n(n−1)}` — the minus sign cancels **because the word length
  is even** (`fullTwistLength_even`), which is why the sign block gets a genuine inverse power of
  `q` rather than a sign.

Against these, `2·c([n]) = n(n−1)` — which the corpus **already proves**
(`two_mul_contentSum_single_row`) — gives `θ_{[n]}² = q^{n(n−1)}`, and the transpose law
`c(λ') = −c(λ)` (`contentSum_conj`) gives the column block its inverse. So the content-sum
exponent is not a convention on these blocks: it is the Hecke root, squared.

## Honest scope

**This is a scope-(a) result, not the general theorem.** It covers `λ = [n]` and `λ = (1ⁿ)` — the
one-dimensional blocks — because those are the ones a *character* argument can reach. It does
**not** derive `θ_λ = q^{c(λ)}` for general `λ`; that needs the Jucys–Murphy elements acting on
the seminormal basis with eigenvalue `q^{2·content}`, which the corpus does not yet carry in Lean.
The hedge in `KeystoneModularTwist.lean` therefore stands for `dim V_λ > 1` and is **not** edited
by this file.

The covered case is nonetheless the one the mass path uses: at `n = 3` the column block gives
`θ_{(1³)} = q^{−3}`, the `/q³` appearing in `F_Bor` (beans `qou-w1j9`, `qou-gzs0`).

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1 (content, conjugate).
- [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (`S`, `T` modular data).
-/

namespace QOU.BraidKnot.Keystone

open Finset QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.IdentityI

variable {R : Type*} [Field R]

/-! ## The Hecke relation and its two roots -/

/-- **The corpus's Hecke convention**, as a predicate on a scalar: `s` is a root of
`(σ − q)(σ + q⁻¹) = 0`.  A one-dimensional representation sends every generator to such an `s`. -/
def IsHeckeRoot (q s : R) : Prop := (s - q) * (s + q⁻¹) = 0

/-- The trivial root `s = q` (the symmetric / one-row channel). -/
theorem isHeckeRoot_triv (q : R) : IsHeckeRoot q q := by
  unfold IsHeckeRoot; simp

/-- The sign root `s = −q⁻¹` (the antisymmetric / one-column channel). -/
theorem isHeckeRoot_sign (q : R) : IsHeckeRoot q (-q⁻¹) := by
  unfold IsHeckeRoot; simp

/-- **There are exactly two roots.**  Over a field the Hecke relation has no third solution, so a
one-dimensional block has no freedom in its twist beyond the binary trivial-vs-sign choice. -/
theorem isHeckeRoot_iff (q s : R) : IsHeckeRoot q s ↔ s = q ∨ s = -q⁻¹ := by
  unfold IsHeckeRoot
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h1 | h2
    · exact Or.inl (sub_eq_zero.mp h1)
    · exact Or.inr (add_eq_zero_iff_eq_neg.mp h2)
  · rintro (rfl | rfl)
    · simp
    · simp

/-! ## The full twist is a positive word of even length -/

/-- Word length of the full twist `Δ² = (σ₁⋯σ_{n−1})^n` in `B_n`: `n(n−1)` positive letters. -/
def fullTwistLength (n : ℕ) : ℕ := n * (n - 1)

/-- **The full twist has even length** — a product of consecutive naturals.  This is the load-bearing
fact for the sign block: it is what cancels the minus sign in `(−q⁻¹)^{n(n−1)}`. -/
theorem fullTwistLength_even (n : ℕ) : Even (fullTwistLength n) := by
  unfold fullTwistLength
  rcases n with _ | m
  · simp
  · simpa [Nat.succ_sub_one, Nat.mul_comm] using Nat.even_mul_succ_self m

/-- On an even power the sign root's minus sign cancels, leaving an inverse power of `q`.
Note this needs **no** `q ≠ 0` hypothesis. -/
theorem neg_inv_pow_even (q : R) {k : ℕ} (hk : Even k) : (-q⁻¹) ^ k = (q ^ k)⁻¹ := by
  rw [hk.neg_pow, inv_pow]

/-! ## The twist on a one-dimensional block -/

/-- The full twist `Δ²` evaluated on the one-dimensional rep sending each `σᵢ ↦ s`. -/
def oneDimFullTwist (s : R) (n : ℕ) : R := s ^ fullTwistLength n

@[simp] theorem oneDimFullTwist_triv (q : R) (n : ℕ) :
    oneDimFullTwist q n = q ^ fullTwistLength n := rfl

/-- **The sign block's full twist is a negative power of `q`**, with the sign gone. -/
theorem oneDimFullTwist_sign (q : R) (n : ℕ) :
    oneDimFullTwist (-q⁻¹) n = (q ^ fullTwistLength n)⁻¹ :=
  neg_inv_pow_even q (fullTwistLength_even n)

/-! ## Matching `θ` — the exponent is the root, not a convention -/

/-- `θ_{[n]}² = q^{n(n−1)}`: the square of the one-row twist is the trivial root's full twist.
Uses the corpus's already-proved `2·c([n]) = n(n−1)`. -/
theorem contentSum_single_row_mul_two (n : ℕ) :
    contentSum [n] * ((2 : ℕ) : ℤ) = ((fullTwistLength n : ℕ) : ℤ) := by
  push_cast
  rw [mul_comm, show (2 : ℤ) * contentSum [n] = 2 * contentSum [n] from rfl,
    two_mul_contentSum_single_row]
  unfold fullTwistLength
  rcases n with _ | m
  · simp
  · push_cast [Nat.succ_sub_one]; ring

theorem theta_single_row_sq (q : R) (n : ℕ) :
    (theta q [n]) ^ 2 = q ^ fullTwistLength n := by
  unfold theta
  rw [← zpow_natCast (q ^ contentSum [n]) 2, ← zpow_mul, contentSum_single_row_mul_two,
    zpow_natCast]

/-- `θ_{[n]'}² = (q^{n(n−1)})⁻¹`: the transpose (one-column) block's twist squared is the **sign**
root's full twist.  Uses the transpose law `c(λ') = −c(λ)`. -/
theorem theta_single_col_sq (q : R) (n : ℕ) :
    (theta q (conj [n])) ^ 2 = (q ^ fullTwistLength n)⁻¹ := by
  have hs : ([n] : List ℕ).Sorted (· ≥ ·) := List.sorted_singleton _
  have hcs : contentSum (conj [n]) = - contentSum [n] := contentSum_conj [n] hs
  unfold theta
  rw [hcs, ← zpow_natCast (q ^ (-contentSum [n])) 2, ← zpow_mul, neg_mul,
    contentSum_single_row_mul_two, zpow_neg, zpow_natCast]

/-- **Main result — the Hecke root determines the one-dimensional twist.**

Whichever of the two roots a one-dimensional block takes, its full twist `Δ²` is `θ²` at the
corresponding partition: the one-row `[n]` for the trivial root, the one-column `[n]'` for the
sign root.  The content-sum exponent is therefore **derived** on these blocks rather than chosen,
which is what the `KeystoneModularTwist` header's *"(up to convention)"* left open.

Scope: one-dimensional blocks only — see the module docstring. -/
theorem oneDim_twist_forced_by_hecke_root (q s : R) (n : ℕ) (hs : IsHeckeRoot q s) :
    (s = q ∧ oneDimFullTwist s n = (theta q [n]) ^ 2) ∨
    (s = -q⁻¹ ∧ oneDimFullTwist s n = (theta q (conj [n])) ^ 2) := by
  rcases (isHeckeRoot_iff q s).mp hs with rfl | rfl
  · exact Or.inl ⟨rfl, by rw [oneDimFullTwist_triv, theta_single_row_sq]⟩
  · exact Or.inr ⟨rfl, by rw [oneDimFullTwist_sign, theta_single_col_sq]⟩

/-- **The mass path's `/q³`, machine-checked.**  At `n = 3` the full twist has length `3·2 = 6`, so
the sign block satisfies `θ² = q^{−6}`, i.e. `θ_{(1³)} = q^{−3}`.

This is the factor appearing in `F_Bor = |tr_M(β_Bor)| · [3]_q! / q³` (beans `qou-gzs0`,
`qou-w1j9`).  What this file adds is that the exponent is **forced by the sign root of the Hecke
relation**, not chosen: `gzs0` had the arithmetic right but could only observe that `q^{−3}` was
*of framing shape*. -/
theorem theta_single_col_sq_three (q : R) : (theta q (conj [3])) ^ 2 = (q ^ 6)⁻¹ := by
  simpa [fullTwistLength] using theta_single_col_sq (R := R) q 3

end QOU.BraidKnot.Keystone
