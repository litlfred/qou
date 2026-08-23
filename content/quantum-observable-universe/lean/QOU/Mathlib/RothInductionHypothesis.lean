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

/-! ### Next

The `y` half of `hres` is the base case: one variable, so `RothBaseCase` applies to
`mvGenWronskian Dy ψ` directly — via the same Gauss step, since that Wronskian is rational too
and `RothBaseCase` is about integer polynomials.

With both halves, `index_le_of_rothGrowth_of_rescaled_bounds` gives §13's conclusion outright
and the induction can be written: `rothLemmaUniform_one` is the base, this is the step, and
`c_m = 2^m − 3` is what iterating produces.

⚠ Provenance: §14 has **not** been read, so `c_m = 2^m − 3` stays unasserted. -/

end MvPolynomial
