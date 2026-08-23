/-
  **Applying the induction hypothesis to the `x`-factor** — the `hres` the induction step
  needs, discharged from `RothLemmaUniform` at `m − 1`.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/SeparatedGauss.lean`,
  `QOU/Mathlib/RothLemmaStatement.lean` and `QOU/Mathlib/WronskianHeight.lean`.

  ═══ WHAT THIS IS ═══

  `index_le_of_rothGrowth_of_rescaled_bounds` (`QOU/Mathlib/RothOperatorFamily.lean`) takes
  `hres`: a bound on the two Wronskians' indices at the **rescaled** degrees.  Everything above
  `hres` is proved; this discharges its `x` half.

  The chain is entirely composition, and the only step with content is one that costs nothing:

  * §6's Gauss (`exists_integral_wronskian_factors`) replaces the rational Wronskian
    `Wx = mvGenWronskian Dx φ` by an **integral** `U'` with `map U' = C l · Wx`;
  * `RothLemmaUniform` at `m − 1` applies to `U'`, because `U'` is an integer polynomial;
  * `index_C_mul` says the scaling `l` **does not move the index**, so the bound transfers
    back to `Wx` unchanged.

  ⚠ That last point is the arc's recurring theme in its final form.  The scaling is free on
  the index side (`index_C_mul`), free on the degree side (`degreeOf_C_mul_le`), free for
  non-vanishing — and costs something on exactly one side, the height, which is why §6 does
  Gauss at all and why §7's argument is where integrality is load-bearing.
-/
import QOU.Mathlib.SeparatedGauss
import QOU.Mathlib.RothLemmaStatement
import QOU.Mathlib.WronskianHeight

namespace MvPolynomial

variable {σ : Type*}

/-- **The `x` half of `hres`, from the induction hypothesis.**

Read the hypotheses as the induction step supplies them: `φ`, `ψ` are a separated
representation of the (integer) auxiliary polynomial `P`, `Dx`, `Dy` a bounded-order operator
family with both Wronskians non-zero, and `B` a height bound on the determinant those
operators form over `ℤ`.

⚠ `hWy` — the `y`-Wronskian being non-zero — is needed for the **height** step and nothing
else: `abs_coeff_le_of_mul_separated` picks a non-zero coefficient of the other factor. It is
exactly what `BoundedOrderWronskian` supplies, and it is the same hypothesis §7 leans on. -/
theorem index_rescaled_wronskian_le [DecidableEq σ]
    {n : ℕ} (o' : σ ≃ Fin n) (ω ε : ℚ) (hIH : RothLemmaUniform σ n ω ε)
    {r : ℕ} (hr : r ≠ 0)
    (d₁ : σ → ℕ) (hd₁ : ∀ j, d₁ j ≠ 0) (hg : RothGrowth o' ω d₁)
    (pn qd : σ → ℤ) (B : ℤ) (E : ℕ)
    (Dx : Fin r → List σ) (Dy : Fin r → List Unit)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial Unit ℚ)
    (P : MvPolynomial (σ ⊕ Unit) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) (hWy : mvGenWronskian Dy ψ ≠ 0)
    (hdeg : ∀ j k, degreeOf j (φ k) ≤ d₁ j)
    (hB : ∀ m, |coeff m (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det| ≤ B)
    (hq2 : ∀ j, 2 ≤ qd j) (hco : ∀ j, IsCoprime (pn j) (qd j))
    (hBq : ∀ j, B ≤ qd j ^ E) (hE : ∀ j, (E : ℚ) ≤ ε * ((r * d₁ j : ℕ) : ℚ)) :
    index (fun j => r * d₁ j) (fun j => (pn j : ℚ) / (qd j : ℚ)) (mvGenWronskian Dx φ)
      ≤ ((((n : ℚ) * ε : ℚ)) : WithTop ℚ) := by
  classical
  obtain ⟨l, U', V', hl, hU', hV', hfact⟩ :=
    exists_integral_wronskian_factors Dx Dy φ ψ P hP hWx
  have hU'ne : U' ≠ 0 := integral_factor_ne_zero hl hWx hU'
  have hV'ne : V' ≠ 0 := integral_factor_ne_zero (inv_ne_zero hl) hWy hV'
  have hdegU : ∀ j, degreeOf j U' ≤ r * d₁ j := fun j =>
    degreeOf_integral_factor_le hU' j
      (degreeOf_mvGenWronskian_le j Dx φ (d₁ j) (fun k => hdeg j k))
  have hBU : ∀ m, |coeff m U'| ≤ B := fun m =>
    abs_coeff_integral_wronskian_factor_le hfact hV'ne hB m
  have hIHapp := hIH o' (fun j => r * d₁ j) pn qd U' B E
    (fun j => Nat.mul_ne_zero hr (hd₁ j))
    (rothGrowth_scale hr hg) hU'ne hdegU hBU hq2 hco hBq hE
  have hmap : map (algebraMap ℤ ℚ) U' = C l * mvGenWronskian Dx φ := hU'
  rwa [hmap, index_C_mul _ _ hl] at hIHapp

/-- **Non-vacuity.**  The largest hypothesis stack in this arc, shown jointly satisfiable.

One variable on each side, everything constant: `n = r = 1`, `d₁ ≡ 1`, `P = 1`, `φ = ψ ≡ 1`,
`p/q = 1/2`, `B = 1`, `E = 0`.  Then the auxiliary polynomial's determinant is `1`, whose
coefficients are `0` and `1`, so `B = 1` works; `E = 0` makes `B ≤ q^E` read `1 ≤ 1`; and the
induction hypothesis is `rothLemmaUniform_one`, which is **proved**.

⚠ This certifies joint satisfiability and nothing more — and the arc has been explicit that
finite witnesses test vacuity, not usefulness (correction 9). What it rules out is the failure
mode that a stack this large invites: two side conditions that quietly contradict each other,
leaving a theorem that is true because it is empty. -/
theorem index_rescaled_wronskian_le_witness :
    index (fun _ : Unit => 1 * 1) (fun _ : Unit => ((1 : ℤ) : ℚ) / ((2 : ℤ) : ℚ))
        (mvGenWronskian (fun _ : Fin 1 => ([] : List Unit))
          (fun _ : Fin 1 => (1 : MvPolynomial Unit ℚ)))
      ≤ ((((1 : ℕ) : ℚ) * 1 : ℚ) : WithTop ℚ) := by
  classical
  have hW : ∀ {α : Type} [DecidableEq α],
      mvGenWronskian (fun _ : Fin 1 => ([] : List α))
        (fun _ : Fin 1 => (1 : MvPolynomial α ℚ)) = 1 := by
    intro α _
    rw [mvGenWronskian, Matrix.det_fin_one, mvWronskianMatrix_apply]
    simp
  have hdet : (Matrix.of fun _ _ : Fin 1 =>
      pderivList (([] : List Unit).map Sum.inl ++ ([] : List Unit).map Sum.inr)
        (1 : MvPolynomial (Unit ⊕ Unit) ℤ)).det = 1 := by
    rw [Matrix.det_fin_one]
    simp
  refine index_rescaled_wronskian_le (σ := Unit) (n := 1) (r := 1)
    (⟨fun _ => 0, fun _ => (), fun _ => rfl, fun i => Subsingleton.elim _ _⟩ :
      Unit ≃ Fin 1) 1 1 (rothLemmaUniform_one 1 1)
    one_ne_zero (fun _ => 1) (fun _ => one_ne_zero) ?_
    (fun _ => 1) (fun _ => 2) 1 0
    (fun _ => []) (fun _ => []) (fun _ => 1) (fun _ => 1) 1
    ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro j k h
    have := j.isLt
    have := k.isLt
    omega
  · simp
  · rw [hW]; exact one_ne_zero
  · rw [hW]; exact one_ne_zero
  · intro j k
    rw [show (1 : MvPolynomial Unit ℚ) = C 1 from (map_one C).symm, degreeOf_C]
    exact Nat.zero_le 1
  · intro m
    rw [hdet, coeff_one]
    split <;> simp
  · intro j; norm_num
  · intro j; exact isCoprime_one_left
  · intro j; norm_num
  · intro j; norm_num

/-- **The `y` half of `hres`** — and it needs **no induction hypothesis at all**.

The split-off group is a single variable, so the relevant instance of `RothLemmaUniform` is
the `m = 1` case, which is `rothLemmaUniform_one` and is **proved**.  So where the `x` half
consumes the induction hypothesis, this half consumes the base case, and the recursion's two
inputs turn out to be the same theorem at two different arities.

The growth condition does not appear: at one variable there is no consecutive pair, so
`RothGrowth` is vacuous — which is also why `rothLemmaUniform_one` holds for every `ω`. -/
theorem index_rescaled_wronskian_le_right [DecidableEq σ]
    (ε : ℚ) {r : ℕ} (hr : r ≠ 0)
    (d₂ : Unit → ℕ) (hd₂ : ∀ j, d₂ j ≠ 0)
    (pn qd : Unit → ℤ) (B : ℤ) (E : ℕ)
    (Dx : Fin r → List σ) (Dy : Fin r → List Unit)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial Unit ℚ)
    (P : MvPolynomial (σ ⊕ Unit) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) (hWy : mvGenWronskian Dy ψ ≠ 0)
    (hdeg : ∀ j k, degreeOf j (ψ k) ≤ d₂ j)
    (hB : ∀ m, |coeff m (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det| ≤ B)
    (hq2 : ∀ j, 2 ≤ qd j) (hco : ∀ j, IsCoprime (pn j) (qd j))
    (hBq : ∀ j, B ≤ qd j ^ E) (hE : ∀ j, (E : ℚ) ≤ ε * ((r * d₂ j : ℕ) : ℚ)) :
    index (fun j => r * d₂ j) (fun j => (pn j : ℚ) / (qd j : ℚ)) (mvGenWronskian Dy ψ)
      ≤ ((((1 : ℕ) : ℚ) * ε : ℚ) : WithTop ℚ) := by
  classical
  obtain ⟨l, U', V', hl, hU', hV', hfact⟩ :=
    exists_integral_wronskian_factors Dx Dy φ ψ P hP hWx
  have hU'ne : U' ≠ 0 := integral_factor_ne_zero hl hWx hU'
  have hV'ne : V' ≠ 0 := integral_factor_ne_zero (inv_ne_zero hl) hWy hV'
  have hdegV : ∀ j, degreeOf j V' ≤ r * d₂ j := fun j =>
    degreeOf_integral_factor_le hV' j
      (degreeOf_mvGenWronskian_le j Dy ψ (d₂ j) (fun k => hdeg j k))
  have hBV : ∀ m, |coeff m V'| ≤ B := fun m =>
    abs_coeff_integral_wronskian_factor_le_right hfact hU'ne hB m
  have hIHapp := rothLemmaUniform_one 1 ε
    (⟨fun _ => 0, fun _ => (), fun _ => rfl, fun i => Subsingleton.elim _ _⟩ : Unit ≃ Fin 1)
    (fun j => r * d₂ j) pn qd V' B E
    (fun j => Nat.mul_ne_zero hr (hd₂ j))
    (by intro j k h; have := j.isLt; have := k.isLt; omega)
    hV'ne hdegV hBV hq2 hco hBq hE
  have hmap : map (algebraMap ℤ ℚ) V' = C l⁻¹ * mvGenWronskian Dy ψ := hV'
  rwa [hmap, index_C_mul _ _ (inv_ne_zero hl)] at hIHapp


/-! ### Next

The `y` half of `hres` is the base case: one variable, so `RothBaseCase` applies to
`mvGenWronskian Dy ψ` directly — via the same Gauss step, since that Wronskian is rational too
and `RothBaseCase` is about integer polynomials.

With both halves, `index_le_of_rothGrowth_of_rescaled_bounds` gives §13's conclusion outright
and the induction can be written: `rothLemmaUniform_one` is the base, this is the step, and
`c_m = 2^m − 3` is what iterating produces.

⚠ Provenance: §14 has **not** been read, so `c_m = 2^m − 3` stays unasserted. -/

end MvPolynomial
