import QOU.BraidsAndKnots.TFromTraceCyclicity
import HeckeTemperleyLieb.MarkovTraceSymmetries

/-!
# QOU.BraidsAndKnots.TFromTraceCyclicityH3 — the T conjecture for every 3-strand representation

`QOU.BraidsAndKnots.TFromTraceCyclicity` carries `conj:t-from-trace-cyclicity` as a class
whose one field says: for every matrix representation `ρ : HeckeRep n d` and every signed
braid word `w`, the character of `w` and of its reversal agree. This file provides the
instance for `n = 3` and every `d` by an elementary argument. The general case (every `n`)
is `QOU.BraidsAndKnots.TFromTraceCyclicityAll`.

## The argument

The statement is about an arbitrary *cyclic* functional, not a Markov trace, so the
uniqueness route of `QOU.IwahoriHecke.MarkovTraceSymmetries.markov_reverse` is not available.
For three strands a direct argument works. Let `t` be any `R`-linear functional with
`t (x y) = t (y x)` on an algebra with a Hecke family `s₀, s₁`. Pull it back to the presented
algebra `Pres 2 a b` along `lift`, and also along `lift` into the opposite algebra followed
by `unop`. The second pull-back is "evaluate the reversed word". The presented algebra is
spanned by the six Jones normal-form words `1, s₀, s₁, s₁s₀, s₀s₁, s₀s₁s₀`
(`JonesNormalForm.adjoin_eq_level`). Five of them are palindromes, and the sixth pair
`s₀s₁ ↔ s₁s₀` is a cyclic rotation, so the two pull-backs agree on every spanning word,
hence everywhere (`cyclic_reverse_two`).

For `n ≥ 4` the normal-form words are no longer palindromes or rotations of each other; the
general argument is the induction along the parabolic chain in
`QOU.IwahoriHecke.HeckeTraceReversal`.

-- Ref: [leitner2026] conj:t-from-trace-cyclicity
-- Ref: [jones1987] Jones, Hecke algebra representations of braid groups (1987), §4.
-/

namespace QOU.BraidsAndKnots

open QOU.IwahoriHecke.JonesNormalForm QOU.IwahoriHecke.MarkovTraceSymmetries MulOpposite

section TwoGenerators

variable {R : Type*} [CommRing R] {a b : R}
variable {A : Type*} [Ring A] [Algebra R A] {s : ℕ → A}

/-- **Reversal invariance of every cyclic functional on a two-generator Hecke family.** -/
theorem cyclic_reverse_two (hs : HeckeFamily 2 a b s) (t : A →ₗ[R] R)
    (hcyc : ∀ x y : A, t (x * y) = t (y * x)) (α β : Bool → R)
    (w : List (Fin 2 × Bool)) :
    t (evalWord α β s w.reverse) = t (evalWord α β s w) := by
  have hop := heckeFamily_op hs
  -- the two pull-backs to the presented algebra
  let T : Pres 2 a b →ₗ[R] R := t ∘ₗ (lift hs).toLinearMap
  let T' : Pres 2 a b →ₗ[R] R := opTrace t ∘ₗ (lift hop).toLinearMap
  have hTT : ∀ x, T x = T' x := by
    intro x
    have hx : x ∈ Algebra.adjoin R (pgen 2 a b '' Set.Iio 2) := by
      rw [adjoin_pgen_eq_top]; trivial
    rw [← Subalgebra.mem_toSubmodule, adjoin_eq_level (pres_heckeFamily 2 a b) le_rfl] at hx
    induction hx using Submodule.span_induction with
    | mem y hy =>
      classical
      simp only [words, Finset.coe_image₂, Set.mem_image2, Finset.mem_coe,
        Finset.mem_image, Finset.mem_range, Finset.mem_singleton] at hy
      obtain ⟨y', ⟨_, rfl, d', ⟨j', hj', rfl⟩, rfl⟩, d, ⟨j, hj, rfl⟩, rfl⟩ := hy
      have h0 : lift hs (pgen 2 a b 0) = s 0 := lift_pgen hs (by norm_num)
      have h1 : lift hs (pgen 2 a b 1) = s 1 := lift_pgen hs (by norm_num)
      have h0' : lift hop (pgen 2 a b 0) = op (s 0) := lift_pgen hop (by norm_num)
      have h1' : lift hop (pgen 2 a b 1) = op (s 1) := lift_pgen hop (by norm_num)
      interval_cases j' <;> interval_cases j <;>
        simp [T, T', dprod, h0, h1, h0', h1', mul_assoc] <;>
        first
        | rfl
        | exact hcyc _ _
    | zero => simp
    | add x y _ _ hx hy => rw [map_add, map_add, hx, hy]
    | smul c x _ hx => rw [map_smul, map_smul, hx]
  have h := hTT (evalWord α β (pgen 2 a b) w)
  simp only [T, T', LinearMap.coe_comp, Function.comp_apply, AlgHom.toLinearMap_apply] at h
  rw [map_evalWord (lift hs) α β _ s (fun i hi => lift_pgen hs hi),
    map_evalWord (lift hop) α β _ _ (fun i hi => lift_pgen hop hi), evalWord_op,
    opTrace_apply, unop_op] at h
  exact h.symm

end TwoGenerators

section ThreeStrands

open QOU.Archimedean Matrix

variable {d : ℕ}

/-- The generators of a 3-strand representation as an `ℕ`-indexed family. -/
noncomputable def genFamily3 (ρ : HeckeRep 3 d) : ℕ → Matrix (Fin d) (Fin d) R_t :=
  fun i => if h : i < 2 then ρ.gen ⟨i, h⟩ else 0

theorem genFamily3_of_lt (ρ : HeckeRep 3 d) {i : ℕ} (h : i < 2) :
    genFamily3 ρ i = ρ.gen ⟨i, h⟩ := dif_pos h

theorem genFamily3_hecke (ρ : HeckeRep 3 d) : HeckeFamily 2 HA_t (1 : R_t) (genFamily3 ρ) where
  quad i hi := by
    rw [genFamily3_of_lt ρ hi, ρ.hecke_rel, one_smul]
  braid i hi := by
    have hi0 : i = 0 := by omega
    subst hi0
    rw [genFamily3_of_lt ρ (by norm_num), genFamily3_of_lt ρ (by norm_num)]
    exact ρ.braid_adj 0 (by norm_num) (by norm_num)
  comm i j hij hj := by omega

/-- `HeckeRep.eval` is `evalWord` in the standard convention. -/
theorem eval_eq_evalWord (ρ : HeckeRep 3 d) (w : Archimedean.BraidWord 3) :
    ρ.eval w = evalWord (stdα HA_t) stdβ (genFamily3 ρ) (N := 2) w := by
  induction w with
  | nil => rfl
  | cons p w ih =>
    obtain ⟨i, e⟩ := p
    have hi : (i : ℕ) < 2 := i.isLt
    cases e
    · show ρ.genInv i * ρ.eval w = _
      rw [evalWord_cons, ← ih]
      congr 1
      simp only [letter, stdα, stdβ, HeckeRep.genInv, genFamily3_of_lt ρ hi]
      simp [neg_smul, sub_eq_add_neg, add_comm]
    · show ρ.gen i * ρ.eval w = _
      rw [evalWord_cons, ← ih]
      congr 1
      simp [letter, stdα, stdβ, genFamily3_of_lt ρ hi]

/-- **`conj:t-from-trace-cyclicity` for three strands, unconditionally.** Every character of
every 3-strand Hecke representation is invariant under braid-word reversal. -/
theorem markovTrace_timeReversal_three (ρ : HeckeRep 3 d) (w : Archimedean.BraidWord 3) :
    MathlibExt.MarkovTrace.markovTrace ρ (timeReversal w)
      = MathlibExt.MarkovTrace.markovTrace ρ w := by
  simp only [MathlibExt.MarkovTrace.markovTrace, HeckeRep.character, timeReversal,
    eval_eq_evalWord]
  exact cyclic_reverse_two (genFamily3_hecke ρ) (Matrix.traceLinearMap (Fin d) R_t R_t)
    (fun x y => Matrix.trace_mul_comm x y) _ _ w

/-- `TFromTraceCyclicity 3 d` from the elementary three-strand argument. Not an instance: the
general instance for every `n` is `TFromTraceCyclicityAll.tFromTraceCyclicity`. -/
def tFromTraceCyclicity_three : TFromTraceCyclicity 3 d where
  trace_reversal_invariant := markovTrace_timeReversal_three

end ThreeStrands

end QOU.BraidsAndKnots
