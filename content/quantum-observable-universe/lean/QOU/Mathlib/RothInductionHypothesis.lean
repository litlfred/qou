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
    {n : ℕ} (o' : σ ≃ Fin n) (ω ε θ : ℚ) (hIH : RothLemmaUniform σ n ω ε θ)
    {r : ℕ} (hr : r ≠ 0)
    (d₁ : σ → ℕ) (hd₁ : ∀ j, d₁ j ≠ 0)
    (κ : σ → ℚ) (Kh : σ → ℤ) (B : ℤ) (E : ℕ)
    (hheight : ∀ j, max |(κ j).num| |(((κ j).den : ℤ))| = Kh j)
    (hg : RothGamma o' ω d₁ Kh)
    (Dx : Fin r → List σ) (Dy : Fin r → List Unit)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial Unit ℚ)
    (P : MvPolynomial (σ ⊕ Unit) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) (hWy : mvGenWronskian Dy ψ ≠ 0)
    (hdeg : ∀ j k, degreeOf j (φ k) ≤ d₁ j)
    (hB : ∀ m, |coeff m (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det| ≤ B)
    (hq2 : ∀ j, 2 ≤ Kh j)
    (hBq : ∀ j, B ≤ Kh j ^ E) (hE : ∀ j, (E : ℚ) ≤ ε * ((r * d₁ j : ℕ) : ℚ)) :
    index (fun j => r * d₁ j) κ (mvGenWronskian Dx φ)
      ≤ ((θ : ℚ) : WithTop ℚ) := by
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
  have hIHapp := hIH o' (fun j => r * d₁ j) κ Kh U' B E
    (fun j => Nat.mul_ne_zero hr (hd₁ j)) hheight
    (rothGamma_scale hr hq2 hg) hU'ne hdegU hBU hq2 hBq hE
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
      ≤ ((1 : ℚ) : WithTop ℚ) := by
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
      Unit ≃ Fin 1) 1 1 1 (rothLemmaUniform_one 1 1 1 le_rfl)
    one_ne_zero (fun _ => 1) (fun _ => one_ne_zero)
    (fun _ => ((1 : ℤ) : ℚ) / ((2 : ℤ) : ℚ)) (fun _ => 2) 1 0 ?_ ?_
    (fun _ => []) (fun _ => []) (fun _ => 1) (fun _ => 1) 1
    ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro j
    norm_num
  · exact
      { growth := by
          intro j k h
          have := j.isLt
          have := k.isLt
          omega
        height := by intro j k _; exact le_rfl
        floor := by intro j _; rw [rothHeightFloor_one]; norm_num }
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
    (ε θ : ℚ) (hεθ : ε ≤ θ) {r : ℕ} (hr : r ≠ 0)
    (d₂ : Unit → ℕ) (hd₂ : ∀ j, d₂ j ≠ 0)
    (κ : Unit → ℚ) (Kh : Unit → ℤ) (B : ℤ) (E : ℕ)
    (hheight : ∀ j, max |(κ j).num| |(((κ j).den : ℤ))| = Kh j)
    (Dx : Fin r → List σ) (Dy : Fin r → List Unit)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial Unit ℚ)
    (P : MvPolynomial (σ ⊕ Unit) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) (hWy : mvGenWronskian Dy ψ ≠ 0)
    (hdeg : ∀ j k, degreeOf j (ψ k) ≤ d₂ j)
    (hB : ∀ m, |coeff m (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det| ≤ B)
    (hq2 : ∀ j, 2 ≤ Kh j)
    (hBq : ∀ j, B ≤ Kh j ^ E) (hE : ∀ j, (E : ℚ) ≤ ε * ((r * d₂ j : ℕ) : ℚ)) :
    index (fun j => r * d₂ j) κ (mvGenWronskian Dy ψ)
      ≤ ((θ : ℚ) : WithTop ℚ) := by
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
  have hIHapp := rothLemmaUniform_one 1 ε θ hεθ
    (⟨fun _ => 0, fun _ => (), fun _ => rfl, fun i => Subsingleton.elim _ _⟩ : Unit ≃ Fin 1)
    (fun j => r * d₂ j) κ Kh V' B E
    (fun j => Nat.mul_ne_zero hr (hd₂ j)) hheight
    { growth := by intro j k h; have := j.isLt; have := k.isLt; omega
      height := by intro j k _; exact le_rfl
      floor := by
        intro j _
        rw [rothHeightFloor_one]
        exact le_trans (by norm_num) (hq2 ()) }
    hV'ne hdegV hBV hq2 hBq hE
  have hmap : map (algebraMap ℤ ℚ) V' = C l⁻¹ * mvGenWronskian Dy ψ := hV'
  rwa [hmap, index_C_mul _ _ (inv_ne_zero hl)] at hIHapp


/-! ### §12's own form — `Θ` rather than the `E`-encoded schema

Correction nineteen: §12 invokes the induction hypothesis as

> `J(U; ρ₁,…,ρ_{m−1}; κ₁,…,κ_{m−1}) ≤ Θ_{m−1}(b; ρ₁,…,ρ_{m−1}; H₁,…,H_{m−1})`

which is **the definition of `Θ`** — `U ∈ R(b;ρ)` and `κ ∈ Q(H)`, nothing else.  There is no
height *exponent* at this step; `Γ` enters separately, as what bounds `Θ_{m−1}` afterwards.

The two theorems below are that step.  They consume `IsRothTheta`'s upper-bound clause
directly and are shorter than the `RothLemmaUniform` versions above, which fuse set membership
with `Γ` and share a single `E` that `Γ` cannot supply.

⚠ The `RothLemmaUniform` forms above are **superseded, not wrong**.  They are proved and their
statements are true; they simply carry a hypothesis stack the induction cannot produce.  Kept
until the recursion is written and confirms nothing needs them. -/

/-- **The `x` half of `hres`, in `Θ` form** — §12's `J(U;ρ;κ) ≤ Θ_{m−1}(b;ρ;H)`.

§6's Gauss replaces the rational Wronskian by an integral `U'` with `map U' = C l · W_x`; `U'`
then lies in `R(b; r·d₁)` by the degree and height bounds; `IsRothTheta`'s first clause applies;
and `index_C_mul` carries the bound back, the scaling being free on the index side. -/
theorem index_rescaled_wronskian_le_theta [DecidableEq σ]
    {r : ℕ} (d₁ : σ → ℕ) (b : ℤ) (H : σ → ℕ) (κ : σ → ℚ) (Θ' : ℚ)
    (hΘ' : IsRothTheta b (fun j => r * d₁ j) H Θ') (hκ : InRothFracSet H κ)
    (Dx : Fin r → List σ) (Dy : Fin r → List Unit)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial Unit ℚ)
    (P : MvPolynomial (σ ⊕ Unit) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) (hWy : mvGenWronskian Dy ψ ≠ 0)
    (hdeg : ∀ j k, degreeOf j (φ k) ≤ d₁ j)
    (hB : ∀ m, |coeff m (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det| ≤ b) :
    index (fun j => r * d₁ j) κ (mvGenWronskian Dx φ) ≤ ((Θ' : ℚ) : WithTop ℚ) := by
  classical
  obtain ⟨l, U', V', hl, hU', hV', hfact⟩ :=
    exists_integral_wronskian_factors Dx Dy φ ψ P hP hWx
  have hU'ne : U' ≠ 0 := integral_factor_ne_zero hl hWx hU'
  have hV'ne : V' ≠ 0 := integral_factor_ne_zero (inv_ne_zero hl) hWy hV'
  have hdegU : ∀ j, degreeOf j U' ≤ r * d₁ j := fun j =>
    degreeOf_integral_factor_le hU' j
      (degreeOf_mvGenWronskian_le j Dx φ (d₁ j) (fun k => hdeg j k))
  have hBU : ∀ n, |coeff n U'| ≤ b := fun n =>
    abs_coeff_integral_wronskian_factor_le hfact hV'ne hB n
  have happ := hΘ'.1 U' κ ⟨hU'ne, hdegU, hBU⟩ hκ
  have hmap : map (algebraMap ℤ ℚ) U' = C l * mvGenWronskian Dx φ := hU'
  rwa [hmap, index_C_mul _ _ hl] at happ

/-- **The `y` half of `hres`, in `Θ` form** — §12's `J(V; ρ_m; κ_m) ≤ Θ₁(b; ρ_m; H_m)`.

The mirror, and it needs no induction hypothesis: the split-off group is one variable, so the
`Θ` it is measured against is `Θ₁`, which §10 bounds outright (`isRothTheta_le_of_gamma_one`). -/
theorem index_rescaled_wronskian_le_right_theta [DecidableEq σ]
    {r : ℕ} (d₂ : Unit → ℕ) (b : ℤ) (H' : Unit → ℕ) (κ' : Unit → ℚ) (Θ₁ : ℚ)
    (hΘ₁ : IsRothTheta b (fun j => r * d₂ j) H' Θ₁) (hκ' : InRothFracSet H' κ')
    (Dx : Fin r → List σ) (Dy : Fin r → List Unit)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial Unit ℚ)
    (P : MvPolynomial (σ ⊕ Unit) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) (hWy : mvGenWronskian Dy ψ ≠ 0)
    (hdeg : ∀ j k, degreeOf j (ψ k) ≤ d₂ j)
    (hB : ∀ m, |coeff m (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det| ≤ b) :
    index (fun j => r * d₂ j) κ' (mvGenWronskian Dy ψ) ≤ ((Θ₁ : ℚ) : WithTop ℚ) := by
  classical
  obtain ⟨l, U', V', hl, hU', hV', hfact⟩ :=
    exists_integral_wronskian_factors Dx Dy φ ψ P hP hWx
  have hU'ne : U' ≠ 0 := integral_factor_ne_zero hl hWx hU'
  have hV'ne : V' ≠ 0 := integral_factor_ne_zero (inv_ne_zero hl) hWy hV'
  have hdegV : ∀ j, degreeOf j V' ≤ r * d₂ j := fun j =>
    degreeOf_integral_factor_le hV' j
      (degreeOf_mvGenWronskian_le j Dy ψ (d₂ j) (fun k => hdeg j k))
  have hBV : ∀ n, |coeff n V'| ≤ b := fun n =>
    abs_coeff_integral_wronskian_factor_le_right hfact hU'ne hB n
  have happ := hΘ₁.1 V' κ' ⟨hV'ne, hdegV, hBV⟩ hκ'
  have hmap : map (algebraMap ℤ ℚ) V' = C l⁻¹ * mvGenWronskian Dy ψ := hV'
  rwa [hmap, index_C_mul _ _ (inv_ne_zero hl)] at happ

/-! ### ⚠⚠ Correction twenty-six — the two halves above take the wrong `b`

`hB` in both is a bound on the **determinant**'s coefficients.  Correction 21 established that
§12's budget covers the **divided** Wronskian `W`, with `det = C c · W` and `c` a product of
factorials of size `2^{Θ(r² log r)}`; `WronskianHeight.exists_divided_wronskian` proves exactly
that, and §11's clause `b ≤ 2^{c'}·a^r` has no room for the extra factor.

So the two halves above and the only available height bound **do not compose**, and both were
green.  The correction landed in `WronskianHeight` and was never propagated here.

The `_div` forms below take `W` and the factorisation `det = C c · W` instead, and are
otherwise identical — `SeparatedGauss.exists_integral_wronskian_factors_div` parks the `c⁻¹` on
the `y` side, and `index_C_mul` is indifferent to which constant it divides out.

⚠ The originals are kept: they are true, and a caller who does have a determinant bound (a
small `r`, say) can still use them.  What they cannot be is the induction's `hres`. -/

/-- **The `x` half of `hres`, in `Θ` form, against the divided Wronskian** — correction 26. -/
theorem index_rescaled_wronskian_le_theta_div [DecidableEq σ]
    {r : ℕ} (d₁ : σ → ℕ) (b : ℤ) (H : σ → ℕ) (κ : σ → ℚ) (Θ' : ℚ)
    (hΘ' : IsRothTheta b (fun j => r * d₁ j) H Θ') (hκ : InRothFracSet H κ)
    (Dx : Fin r → List σ) (Dy : Fin r → List Unit)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial Unit ℚ)
    (P : MvPolynomial (σ ⊕ Unit) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) (hWy : mvGenWronskian Dy ψ ≠ 0)
    (hdeg : ∀ j k, degreeOf j (φ k) ≤ d₁ j)
    (W : MvPolynomial (σ ⊕ Unit) ℤ) {c : ℤ} (hc : c ≠ 0)
    (hdet : (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det = C c * W)
    (hB : ∀ m, |coeff m W| ≤ b) :
    index (fun j => r * d₁ j) κ (mvGenWronskian Dx φ) ≤ ((Θ' : ℚ) : WithTop ℚ) := by
  classical
  obtain ⟨l, l', U', V', hl, hl', hU', hV', hfact⟩ :=
    exists_integral_wronskian_factors_div Dx Dy φ ψ P hP hWx W hc hdet
  have hU'ne : U' ≠ 0 := integral_factor_ne_zero hl hWx hU'
  have hV'ne : V' ≠ 0 := integral_factor_ne_zero hl' hWy hV'
  have hdegU : ∀ j, degreeOf j U' ≤ r * d₁ j := fun j =>
    degreeOf_integral_factor_le hU' j
      (degreeOf_mvGenWronskian_le j Dx φ (d₁ j) (fun k => hdeg j k))
  have hBU : ∀ n, |coeff n U'| ≤ b := fun n =>
    abs_coeff_integral_wronskian_factor_le hfact hV'ne hB n
  have happ := hΘ'.1 U' κ ⟨hU'ne, hdegU, hBU⟩ hκ
  have hmap : map (algebraMap ℤ ℚ) U' = C l * mvGenWronskian Dx φ := hU'
  rwa [hmap, index_C_mul _ _ hl] at happ

/-- **The `y` half of `hres`, in `Θ` form, against the divided Wronskian** — correction 26. -/
theorem index_rescaled_wronskian_le_right_theta_div [DecidableEq σ]
    {r : ℕ} (d₂ : Unit → ℕ) (b : ℤ) (H' : Unit → ℕ) (κ' : Unit → ℚ) (Θ₁ : ℚ)
    (hΘ₁ : IsRothTheta b (fun j => r * d₂ j) H' Θ₁) (hκ' : InRothFracSet H' κ')
    (Dx : Fin r → List σ) (Dy : Fin r → List Unit)
    (φ : Fin r → MvPolynomial σ ℚ) (ψ : Fin r → MvPolynomial Unit ℚ)
    (P : MvPolynomial (σ ⊕ Unit) ℤ)
    (hP : map (Int.castRingHom ℚ) P
        = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ Unit) ℚ) * rename Sum.inr (ψ k))
    (hWx : mvGenWronskian Dx φ ≠ 0) (hWy : mvGenWronskian Dy ψ ≠ 0)
    (hdeg : ∀ j k, degreeOf j (ψ k) ≤ d₂ j)
    (W : MvPolynomial (σ ⊕ Unit) ℤ) {c : ℤ} (hc : c ≠ 0)
    (hdet : (Matrix.of fun i j =>
        pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr) P).det = C c * W)
    (hB : ∀ m, |coeff m W| ≤ b) :
    index (fun j => r * d₂ j) κ' (mvGenWronskian Dy ψ) ≤ ((Θ₁ : ℚ) : WithTop ℚ) := by
  classical
  obtain ⟨l, l', U', V', hl, hl', hU', hV', hfact⟩ :=
    exists_integral_wronskian_factors_div Dx Dy φ ψ P hP hWx W hc hdet
  have hU'ne : U' ≠ 0 := integral_factor_ne_zero hl hWx hU'
  have hV'ne : V' ≠ 0 := integral_factor_ne_zero hl' hWy hV'
  have hdegV : ∀ j, degreeOf j V' ≤ r * d₂ j := fun j =>
    degreeOf_integral_factor_le hV' j
      (degreeOf_mvGenWronskian_le j Dy ψ (d₂ j) (fun k => hdeg j k))
  have hBV : ∀ n, |coeff n V'| ≤ b := fun n =>
    abs_coeff_integral_wronskian_factor_le_right hfact hU'ne hB n
  have happ := hΘ₁.1 V' κ' ⟨hV'ne, hdegV, hBV⟩ hκ'
  have hmap : map (algebraMap ℤ ℚ) V' = C l' * mvGenWronskian Dy ψ := hV'
  rwa [hmap, index_C_mul _ _ hl'] at happ

/-- **Non-vacuity of the `Θ` form.**

Same data as `index_rescaled_wronskian_le_witness` — one variable each side, everything
constant — with `IsRothTheta` supplied by `exists_isRothTheta` and the point `κ = 1`, whose
height `max(1,1)` is exactly the required `H = 1`.

⚠ The hypothesis stack is **shorter** than the `RothLemmaUniform` version's: no `Kh`, no `E`,
no coprimality, no `2 ≤ Kh`, no `RothGamma`, and no `r ≠ 0`.  That is the practical evidence for
correction nineteen — the faithful form of §12's step asks for less because it asks for the
right thing. -/
theorem index_rescaled_wronskian_le_theta_witness :
    ∃ Θ' : ℚ, IsRothTheta (1 : ℤ) (fun _ : Unit => 1 * 1) (fun _ : Unit => 1) Θ' ∧
      index (fun _ : Unit => 1 * 1) (fun _ : Unit => (1 : ℚ))
          (mvGenWronskian (fun _ : Fin 1 => ([] : List Unit))
            (fun _ : Fin 1 => (1 : MvPolynomial Unit ℚ)))
        ≤ ((Θ' : ℚ) : WithTop ℚ) := by
  classical
  obtain ⟨Θ', hΘ'⟩ := exists_isRothTheta (1 : ℤ) (fun _ : Unit => 1 * 1) (fun _ : Unit => 1)
    le_rfl (fun _ => le_rfl)
  refine ⟨Θ', hΘ', ?_⟩
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
  refine index_rescaled_wronskian_le_theta (σ := Unit) (r := 1) (fun _ => 1) 1
    (fun _ => 1) (fun _ => (1 : ℚ)) Θ' hΘ' ?_
    (fun _ => []) (fun _ => []) (fun _ => 1) (fun _ => 1) 1 ?_ ?_ ?_ ?_ ?_
  · intro h
    norm_num [InRothFracSet]
  · simp
  · rw [hW]; exact one_ne_zero
  · rw [hW]; exact one_ne_zero
  · intro j k
    rw [show (1 : MvPolynomial Unit ℚ) = C 1 from (map_one C).symm, degreeOf_C]
    exact Nat.zero_le 1
  · intro m
    rw [hdet, coeff_one]
    split <;> simp

/-! ### Next

The `y` half of `hres` is the base case: one variable, so `RothBaseCase` applies to
`mvGenWronskian Dy ψ` directly — via the same Gauss step, since that Wronskian is rational too
and `RothBaseCase` is about integer polynomials.

With both halves, `index_le_of_rothGrowth_of_rescaled_bounds` gives §13's conclusion outright
and the induction can be written: `rothLemmaMahler_one` is the base and this is the step.

§14 has since been read from the page scans, and it corrected two things this note had wrong:
the constant is `c_m = 2^{m+1} − 3`, not `2^m − 3` (`rothConstant`), and what iterating
produces is `Θ_m ≤ c_m·t^{2^{−(m−1)}}` — an **exponent**, not a linear factor.  The bound both
halves now carry is the parameter `θ`, and the recursion's obligation is to show the assembled
`θ` satisfies `RothBound m t`.  See the eleventh correction in `RothLemmaStatement`. -/

end MvPolynomial
