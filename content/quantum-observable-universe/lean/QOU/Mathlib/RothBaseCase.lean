/-
  **The `m = 1` case of Roth's lemma, in terms of `index`.**

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/RothIndex.lean` and
  `QOU/Mathlib/RothHeightBound.lean`.  Both are Mathlib-only, so the three lift together.

  ═══ ⚠ WHAT WAS ACTUALLY MISSING ═══

  Bean `qou-4lbh` recorded the `m = 1` base case as **complete**, citing
  `pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero`, and added:

  > With Roth's hypothesis `H(P) ≤ q^{εd}` this gives `q^{θd} ≤ q^{εd}`, i.e. the index `θ ≤ ε`.

  That last step was **prose, not Lean.**  What was proved is a statement about *Taylor
  coefficients*: "if every coefficient of the translate below `k` vanishes, then `q^k ≤ |lead P|`."
  The induction does not consume that — it consumes a bound on `index`.  Nothing anywhere
  connected the two, because `index` lives on `MvPolynomial` and the height bound lives on
  `Polynomial`.

  This module is that connection, ending in `index_le_of_abs_leadingCoeff_le`:

      |lead P| ≤ q^e,  q ≥ 2,  gcd(p,q) = 1,  P ≠ 0,  d ≠ 0
        ⟹  index_d(P; p/q)  ≤  e/d

  With `e = εd` that reads `index ≤ ε`, which *is* the base case.  The gap was narrow but
  real: an arc can accumulate a correct height statement and a correct index calculus and
  still have no theorem relating them.

  ═══ THE TRANSFER ═══

  One variable is `MvPolynomial Unit`, and `MvPolynomial.pUnitAlgEquiv` carries it to `R[X]`.
  Two facts make the dictionary work: coefficients correspond along `n ↦ Finsupp.single () n`,
  and `translate` corresponds to `Polynomial.taylor`.  Everything else is bookkeeping.

  ⚠ **Universe trap.**  `pUnitAlgEquiv` is stated for `PUnit.{u+1}`, so a statement written
  with an unannotated `PUnit` gets an auto-bound universe and will not unify with `index`
  elsewhere — the error is an inscrutable `index.{u_2, 0}` vs `index.{0, 0}` mismatch.  Every
  statement below pins `Unit`.
-/
import QOU.Mathlib.RothIndex
import QOU.Mathlib.RothHeightBound

open Polynomial

namespace MvPolynomial

variable {R : Type*} [CommRing R]

/-! ### The one-variable dictionary -/

/-- Coefficients correspond along `n ↦ Finsupp.single () n`. -/
theorem coeff_pUnitAlgEquiv (Q : MvPolynomial Unit R) (n : ℕ) :
    (pUnitAlgEquiv R Q).coeff n = MvPolynomial.coeff (Finsupp.single () n) Q := by
  classical
  induction Q using MvPolynomial.induction_on' with
  | monomial s r =>
      rw [pUnitAlgEquiv_monomial, Polynomial.coeff_monomial, MvPolynomial.coeff_monomial]
      by_cases h : s () = n
      · have hs : s = Finsupp.single () n := by
          refine Finsupp.ext fun u => ?_
          cases u
          rw [Finsupp.single_eq_same, h]
        rw [if_pos h, if_pos hs]
      · have hs : ¬ (s = Finsupp.single () n) := by
          intro hcon
          exact h (by rw [hcon, Finsupp.single_eq_same])
        rw [if_neg h, if_neg hs]
  | add p q hp hq => rw [map_add, Polynomial.coeff_add, MvPolynomial.coeff_add, hp, hq]

/-- **`translate` is `Polynomial.taylor`** under the one-variable dictionary.  Both are
"substitute `X + α` for `X`", so this is really a naturality statement. -/
theorem pUnitAlgEquiv_translate (α : R) (Q : MvPolynomial Unit R) :
    pUnitAlgEquiv R (translate (fun _ => α) Q) = taylor α (pUnitAlgEquiv R Q) := by
  induction Q using MvPolynomial.induction_on with
  | C a => simp [translate, taylor_apply]
  | add p q hp hq => simp only [translate_add, map_add, hp, hq]
  | mul_X p i hp =>
      rw [translate_mul, translate_X, map_mul, hp, map_mul, taylor_mul]
      cases i
      simp [taylor_apply]

/-! ### From a lower bound on the index to vanishing Taylor coefficients -/

/-- A lower bound `k/d` on the index kills every Taylor coefficient below `k` — the hypothesis
`pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero` asks for.

In one variable every multi-index is `Finsupp.single () n`, so `idxWeight` is just `n/d`, and
`index ≥ k/d` says exactly that no `n < k` occurs in the support of the translate. -/
theorem taylor_coeff_eq_zero_of_le_index {d : ℕ} (hd : d ≠ 0) (α : R)
    (Q : MvPolynomial Unit R) (k n : ℕ)
    (h : (((k : ℚ) / (d : ℚ) : ℚ) : WithTop ℚ) ≤ index (fun _ => d) (fun _ => α) Q)
    (hn : n < k) :
    (taylor α (pUnitAlgEquiv R Q)).coeff n = 0 := by
  classical
  by_contra hne
  rw [← pUnitAlgEquiv_translate, coeff_pUnitAlgEquiv] at hne
  have hmem : Finsupp.single () n ∈ (translate (fun _ => α) Q).support :=
    mem_support_iff.mpr hne
  have hw := (le_index_iff _ _ _ _).mp h _ hmem
  rw [idxWeight_single] at hw
  have hdQ : (0 : ℚ) < (d : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hd
  have hw' : (k : ℚ) / (d : ℚ) ≤ (n : ℚ) / (d : ℚ) := by exact_mod_cast hw
  have hkn : (k : ℚ) ≤ (n : ℚ) := by
    have h2 := mul_le_mul_of_nonneg_right hw' hdQ.le
    rwa [div_mul_cancel₀ _ hdQ.ne', div_mul_cancel₀ _ hdQ.ne'] at h2
  have : k ≤ n := by exact_mod_cast hkn
  omega

/-- The height bound of `RothHeightBound.lean`, restated against `index`. -/
theorem pow_le_abs_leadingCoeff_of_le_index {p q : ℤ} (hq : 0 < q) (hco : IsCoprime p q)
    {d : ℕ} (hd : d ≠ 0) {P : ℤ[X]} (hP : P ≠ 0) (k : ℕ)
    (h : (((k : ℚ) / (d : ℚ) : ℚ) : WithTop ℚ)
        ≤ index (fun _ : Unit => d) (fun _ : Unit => ((p : ℚ) / (q : ℚ)))
            (((pUnitAlgEquiv ℚ).symm (P.map (algebraMap ℤ ℚ))) : MvPolynomial Unit ℚ)) :
    q ^ k ≤ |P.leadingCoeff| := by
  refine pow_le_abs_leadingCoeff_of_taylor_coeff_eq_zero hq hco hP k ?_
  intro n hn
  have := taylor_coeff_eq_zero_of_le_index hd ((p : ℚ) / (q : ℚ))
    (((pUnitAlgEquiv ℚ).symm (P.map (algebraMap ℤ ℚ))) : MvPolynomial Unit ℚ) k n h hn
  rwa [AlgEquiv.apply_symm_apply] at this

/-! ### The base case -/

/-- **The `m = 1` case of Roth's lemma.**

    `|lead P| ≤ q^e`,  `q ≥ 2`,  `gcd(p,q) = 1`,  `P ≠ 0`,  `d ≠ 0`
      ⟹  `index_d(P; p/q) ≤ e/d`.

With Roth's hypothesis `H(P) ≤ q^{εd}` — so `e = εd` — this reads `index ≤ ε`, which is what
the induction on the number of variables consumes.

The proof is by contradiction on the *realised* index.  Because `index` is an infimum over a
finite support, and in one variable every support element is `Finsupp.single () n`, the index
is literally `n₀/d` for some natural `n₀`.  So `e/d < index` forces `e < n₀`, hence
`(e+1)/d ≤ index`, hence `q^{e+1} ≤ |lead P| ≤ q^e` — impossible for `q ≥ 2`.

⚠ That integrality step is why `q ≥ 2` rather than `q > 0`: with `q = 1` the powers do not
separate and the argument gives nothing. -/
theorem index_le_of_abs_leadingCoeff_le {p q : ℤ} (hq : 2 ≤ q) (hco : IsCoprime p q)
    {d : ℕ} (hd : d ≠ 0) {P : ℤ[X]} (hP : P ≠ 0) (e : ℕ)
    (hB : |P.leadingCoeff| ≤ q ^ e) :
    index (fun _ : Unit => d) (fun _ : Unit => ((p : ℚ) / (q : ℚ)))
        (((pUnitAlgEquiv ℚ).symm (P.map (algebraMap ℤ ℚ))) : MvPolynomial Unit ℚ)
      ≤ (((e : ℚ) / (d : ℚ) : ℚ) : WithTop ℚ) := by
  classical
  set Q : MvPolynomial Unit ℚ := (pUnitAlgEquiv ℚ).symm (P.map (algebraMap ℤ ℚ)) with hQdef
  set α : ℚ := (p : ℚ) / (q : ℚ) with hαdef
  have hq0 : (0 : ℤ) < q := by omega
  have hdQ : (0 : ℚ) < (d : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hd
  have hPQ : P.map (algebraMap ℤ ℚ) ≠ 0 :=
    Polynomial.map_ne_zero_iff (algebraMap ℤ ℚ).injective_int |>.mpr hP
  have hQ0 : Q ≠ 0 := fun h =>
    hPQ ((pUnitAlgEquiv ℚ).symm.injective (h.trans (map_zero _).symm))
  -- `translate` is invertible, so a non-zero polynomial has a non-zero translate.
  have htr : translate (fun _ : Unit => α) Q ≠ 0 := by
    intro h0
    apply hQ0
    have hpt := pUnitAlgEquiv_translate α Q
    rw [h0, map_zero] at hpt
    have h2 := congrArg (taylor (-α)) hpt.symm
    rw [taylor_taylor, neg_add_cancel, taylor_zero, map_zero] at h2
    have h3 := congrArg (pUnitAlgEquiv ℚ).symm h2
    rwa [AlgEquiv.symm_apply_apply, map_zero] at h3
  -- the infimum is attained, and in one variable it is literally `n₀ / d`
  obtain ⟨i₀, hi₀, hieq⟩ := Finset.exists_mem_eq_inf _ (support_nonempty.mpr htr)
    (fun i => (idxWeight (fun _ : Unit => d) i : WithTop ℚ))
  set n₀ : ℕ := i₀ () with hn₀
  have hsingle : i₀ = Finsupp.single () n₀ := by
    refine Finsupp.ext fun u => ?_
    cases u
    rw [Finsupp.single_eq_same]
  have hidx : index (fun _ : Unit => d) (fun _ : Unit => α) Q
      = (((n₀ : ℚ) / (d : ℚ) : ℚ) : WithTop ℚ) := by
    unfold index
    rw [hieq, hsingle, idxWeight_single]
  by_contra hcon
  push_neg at hcon
  rw [hidx] at hcon
  have hlt : (e : ℚ) / (d : ℚ) < (n₀ : ℚ) / (d : ℚ) := by exact_mod_cast hcon
  have hen : e < n₀ := by
    have h2 := mul_lt_mul_of_pos_right hlt hdQ
    rw [div_mul_cancel₀ _ hdQ.ne', div_mul_cancel₀ _ hdQ.ne'] at h2
    exact_mod_cast h2
  have hk : ((((e + 1 : ℕ) : ℚ) / (d : ℚ) : ℚ) : WithTop ℚ)
      ≤ index (fun _ : Unit => d) (fun _ : Unit => α) Q := by
    rw [hidx, WithTop.coe_le_coe]
    have hle : ((e + 1 : ℕ) : ℚ) ≤ (n₀ : ℚ) := by exact_mod_cast hen
    gcongr
  have hpow := pow_le_abs_leadingCoeff_of_le_index hq0 hco hd hP (e + 1) hk
  have hchain : q ^ (e + 1) ≤ q ^ e := le_trans hpow hB
  have hqe : (0 : ℤ) < q ^ e := pow_pos hq0 e
  rw [pow_succ] at hchain
  nlinarith

/-! ### Validation

The theorem has six hypotheses; this instantiates all of them and extracts a non-trivial
conclusion rather than merely showing they are satisfiable.

Take `P = 1`, `p/q = 1/2`, `d = 1`, `e = 0`: then `|lead P| = 1 ≤ 2⁰`, and the theorem gives
`index ≤ 0`.  With `index_nonneg` that pins the index of a non-zero constant to exactly `0` —
the right answer, since a non-zero constant vanishes to order zero everywhere. -/
example :
    index (fun _ : Unit => 1) (fun _ : Unit => ((1 : ℤ) : ℚ) / ((2 : ℤ) : ℚ))
        (((pUnitAlgEquiv ℚ).symm ((1 : ℤ[X]).map (algebraMap ℤ ℚ))) : MvPolynomial Unit ℚ)
      = 0 := by
  refine le_antisymm ?_ (index_nonneg _ _ _)
  have h := index_le_of_abs_leadingCoeff_le (p := 1) (q := 2) (by norm_num)
    isCoprime_one_left (d := 1) (by norm_num) (P := 1) one_ne_zero 0 (by norm_num)
  simpa using h

/-! ### Next

⚠ This is the base case only.  What remains for Roth's lemma is the **induction on the number
of variables**: the parameter conditions (`dⱼ/dⱼ₊₁` growth, `ε`, the `qⱼ` hypotheses) and the
step that feeds this theorem and the `m−1` case back into the `m` case.

Everything that step needs from the index and height calculus is now proved —
`index_separated` and `abs_coeff_le_of_mul_separated` split the separated Wronskian,
`abs_coeff_mvGenWronskian_le` and `sum_index_le_index_mvGenWronskian_add` bound it, and this
theorem terminates the recursion.  What is not written is the recursion itself.

⚠ An earlier version of this paragraph named `index_det_ge` as the index bound.  **That was
false when written:** `index_det_ge` bounds a determinant by the indices of its *entries*, and
for a Wronskian the entries are `pderivList (D i) (f j)`, which nothing related back to
`index (f j)`.  The composite that actually does is
`sum_index_le_index_mvGenWronskian_add` in `QOU/Mathlib/WronskianIndex.lean`, written after
this module and because of this error. -/

end MvPolynomial
