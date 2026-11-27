import Mathlib.Data.Matrix.Mul
import Mathlib.Data.Fintype.Pi
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

/-!
# n − p vanishes at q = 1 for every number of strands

At `q = 1` the Hecke R-matrix `Rc` is the swap and `σ⁻¹ = σ`, so every braid word acts on
`(C²)^{⊗n}` as a strand-permutation matrix, and the weight term of the jet derivative
`𝒟 = (hol − 1)/q + (1 − q⁻¹)·T³` has coefficient `0`. (That identification is the input; it is
stated here, not proved in this file.)

This file proves the combinatorial core over any commutative ring `R`:

* the global flip (complement every bit) commutes with every strand-permutation matrix;
* matrices commuting with the flip are closed under `+`, `-`, `*`, powers and contain `1`;
* for such a matrix, the trace over states with `w` false bits equals the trace over states with
  `n − w` false bits.

Corollary `blockTr_hol_sub_one_pow`: for `hol` any product of strand permutations, every
`tr_w((hol − 1)^k)` equals `tr_{n−w}((hol − 1)^k)`. With `false` read as `u`, block `w` and block
`n − w` are mirror nucleons, so every n − p term of this kind is `0` at `q = 1`, for all `n`, `k`.
-/

namespace QOU.MassTheory.FlipSymmetryAtOne

open Matrix

variable {n : ℕ} {R : Type*} [CommRing R]

/-- A basis state of `(C²)^{⊗n}`: one bit per strand. -/
abbrev St (n : ℕ) := Fin n → Bool

/-- The global flip: complement every bit. -/
def flip (s : St n) : St n := fun i => !(s i)

@[simp] lemma flip_flip (s : St n) : flip (flip s) = s := by
  funext i; simp [flip]

/-- The flip as an equivalence. -/
def flipEquiv : St n ≃ St n := ⟨flip, flip, flip_flip, flip_flip⟩

/-- Number of `false` (u) bits. -/
def uCount (s : St n) : ℕ := (Finset.univ.filter (fun i => s i = false)).card

lemma uCount_flip (s : St n) : uCount (flip s) = n - uCount s := by
  unfold uCount
  have h1 : (Finset.univ.filter (fun i => flip s i = false))
      = Finset.univ.filter (fun i => ¬ (s i = false)) := by
    ext i; simp [flip]
  rw [h1]
  have h2 := Finset.filter_card_add_filter_neg_card_eq_card
    (s := (Finset.univ : Finset (Fin n))) (fun i => s i = false)
  simp only [Finset.card_univ, Fintype.card_fin] at h2
  omega

lemma uCount_le (s : St n) : uCount s ≤ n := by
  unfold uCount
  calc _ ≤ (Finset.univ : Finset (Fin n)).card := Finset.card_filter_le _ _
    _ = n := by simp

/-- `M` commutes with the flip. -/
def FlipInv (M : Matrix (St n) (St n) R) : Prop := ∀ s t, M (flip s) (flip t) = M s t

lemma flipInv_one : FlipInv (1 : Matrix (St n) (St n) R) := by
  intro s t
  by_cases h : s = t
  · subst h; simp
  · have h' : flip s ≠ flip t := fun e => h (by simpa using congrArg flip e)
    simp [h, h']

lemma FlipInv.add {M N : Matrix (St n) (St n) R} (hM : FlipInv M) (hN : FlipInv N) :
    FlipInv (M + N) := by
  intro s t; simp [hM s t, hN s t]

lemma FlipInv.sub {M N : Matrix (St n) (St n) R} (hM : FlipInv M) (hN : FlipInv N) :
    FlipInv (M - N) := by
  intro s t; simp [hM s t, hN s t]

lemma FlipInv.mul {M N : Matrix (St n) (St n) R} (hM : FlipInv M) (hN : FlipInv N) :
    FlipInv (M * N) := by
  intro s t
  simp only [Matrix.mul_apply]
  rw [← Equiv.sum_comp (flipEquiv (n := n))]
  refine Finset.sum_congr rfl (fun u _ => ?_)
  show M (flip s) (flip u) * N (flip u) (flip t) = M s u * N u t
  rw [hM, hN]

lemma FlipInv.pow {M : Matrix (St n) (St n) R} (hM : FlipInv M) (k : ℕ) : FlipInv (M ^ k) := by
  induction k with
  | zero => simpa using (flipInv_one (n := n) (R := R))
  | succ k ih => rw [pow_succ]; exact ih.mul hM

/-- The matrix of a strand permutation `π`: `P s t = 1` iff `s = t ∘ π`. -/
def permMat (π : Equiv.Perm (Fin n)) : Matrix (St n) (St n) R :=
  fun s t => if s = t ∘ π then 1 else 0

lemma flipInv_permMat (π : Equiv.Perm (Fin n)) : FlipInv (permMat (R := R) π) := by
  intro s t
  have : (flip s = flip t ∘ π) ↔ (s = t ∘ π) := by
    constructor
    · intro h; funext i; have := congrFun h i; simpa [flip] using this
    · intro h; funext i; simp [flip, h]
  simp only [permMat, this]

lemma flipInv_prod (l : List (Equiv.Perm (Fin n))) :
    FlipInv ((l.map (permMat (R := R))).prod) := by
  induction l with
  | nil => simpa using (flipInv_one (n := n) (R := R))
  | cons π l ih => simpa using (flipInv_permMat (R := R) π).mul ih

/-- Trace over the states with exactly `w` false bits. -/
def blockTr (M : Matrix (St n) (St n) R) (w : ℕ) : R :=
  ∑ s ∈ Finset.univ.filter (fun s : St n => uCount s = w), M s s

/-- Mirror blocks have equal trace for a flip-invariant matrix. -/
theorem blockTr_mirror {M : Matrix (St n) (St n) R} (hM : FlipInv M) {w : ℕ} (hw : w ≤ n) :
    blockTr M w = blockTr M (n - w) := by
  unfold blockTr
  refine Finset.sum_nbij' flip flip ?_ ?_ ?_ ?_ ?_
  · intro s hs
    have hs' : uCount s = w := by simpa using hs
    simp [uCount_flip, hs']
  · intro s hs
    have hs' : uCount s = n - w := by simpa using hs
    simp [uCount_flip, hs', Nat.sub_sub_self hw]
  · intro s _; simp
  · intro s _; simp
  · intro s _; exact (hM s s).symm

/-- **n − p = 0 at q = 1, every `n`, every `k`.** For `hol` a product of strand permutations,
the mirror blocks of `(hol − 1)^k` have equal trace. -/
theorem blockTr_hol_sub_one_pow (l : List (Equiv.Perm (Fin n))) (k : ℕ) {w : ℕ} (hw : w ≤ n) :
    blockTr (((l.map (permMat (R := R))).prod - 1) ^ k) w
      = blockTr (((l.map (permMat (R := R))).prod - 1) ^ k) (n - w) :=
  blockTr_mirror (((flipInv_prod l).sub flipInv_one).pow k) hw

end QOU.MassTheory.FlipSymmetryAtOne
