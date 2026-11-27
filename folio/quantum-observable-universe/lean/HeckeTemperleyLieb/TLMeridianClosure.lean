import HeckeTemperleyLieb.TLHopfLinkRow

/-!
# Closing a meridian on the Temperley–Lieb tower

Bean `hkmt`. The rows `S_{b,j}` with `b ≥ 2` need the loop of a cabled strand around a
Jones–Wenzl projector to be closed off one strand at a time. This file does the single-strand
step on the corpus tower `TLFin K δ n` with the positive-loop crossings
`σᵢ = A − A⁻¹eᵢ`, `δ = A² + A⁻²` of `TLPositiveLoopCrossingTwist`.

No conditional expectation is constructed. Closing the last strand is done at the level of
elements by the cap sandwich `e·ι(x)·e = ι(x')·e` (the shape of the corpus Jones lemma
`HProp`), and at the level of traces by the Markov property.

* `cap_conj_cap`: a crossing pair `σ X σ⁻¹` under a cap closes like `e' X e'`
  (Reidemeister II through a cap).
* `omega`, `cap_hopf`: closing the loop strand of `hopfW (n+1)` (the last strand going once
  around `n + 1` others) leaves `Ω_n ∈ TL_{n+1}`, given by the recursion
  `Ω_n = (A²δ − 2)·hopfW n + A⁻²·ι(Ω_{n−1})`.
* `aug_omega`: `aug(Ω_n) = A^{2n+4} + A^{−(2n+4)}`, i.e. `q^{n+2} + q^{−(n+2)}` at `q = A²`.
* `jw_cap_hopf`: so on the Jones–Wenzl projector `p_n`, one closed loop around it is the
  scalar `q^{n+2} + q^{−(n+2)}`.
* `loop`, `cap_loop`: the last strand going around the first `n + 1` while passing on one side
  of `c` further strands (`loop n c = σ·ι(loop n (c−1))·σ⁻¹`) closes to the same `Ω_n`.
* `trace_loop`: for every Markov trace with `δε = 1`,
  `τ(ι(x)·loop n (c+1)) = ε·τ(x·ι(ι^c Ω_n))`.

This is the meridian-removal step of the cabled Hopf link. The remaining steps for `S_{b,j}`
(the cup slide `e·ι(loop_c)·loop_{c+1} = e` and naturality of the cabled loop) are not here.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] https://doi.org/10.1007/BF01389127
-/

namespace QOU.HeckeTemperleyLieb.TLMeridian

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLPositiveLoop QOU.HeckeTemperleyLieb.TLHopfRow

variable {K : Type*} [Field K] {δ A : K}

/-! ## Two cap identities -/

theorem sandwich {R : Type*} [Ring R] (Y g g' : R) (hY : Commute Y g) (hg : g * g' * g = g) :
    g * (Y * g') * g = Y * g := by
  rw [← mul_assoc g Y, ← hY.eq]; simp only [mul_assoc]; rw [← mul_assoc g, hg]

/-- Expansion of a cap around two same-sign crossings. With `e` the last generator and `e'`
the one below it, if `X` commutes with `e` and `e' X e' = Y e'` with `Y` commuting with `e`,
then `e σ' X σ' e = ((A²δ − 2)·X + A⁻²·Y)·e`. -/
theorem cap_sq {m : ℕ} (X Y : TLFin K δ (m + 2))
    (hX : Commute X (e K δ adjFin (Fin.last (m + 1))))
    (hY : Commute Y (e K δ adjFin (Fin.last (m + 1))))
    (hXY : e K δ adjFin (Fin.castSucc (Fin.last m)) * X * e K δ adjFin (Fin.castSucc (Fin.last m))
      = Y * e K δ adjFin (Fin.castSucc (Fin.last m)))
    (hA : A ≠ 0) :
    e K δ adjFin (Fin.last (m + 1)) * (crossing δ A (Fin.castSucc (Fin.last m)) * X *
        crossing δ A (Fin.castSucc (Fin.last m))) * e K δ adjFin (Fin.last (m + 1))
      = ((A ^ 2 * δ - 2) • X + A⁻¹ ^ 2 • Y) * e K δ adjFin (Fin.last (m + 1)) := by
  set g := e K δ adjFin (Fin.last (m + 1))
  set g' := e K δ adjFin (Fin.castSucc (Fin.last m))
  have hgg : g * g' * g = g := last_adj δ m
  have h1 : g * X * g = δ • (X * g) := by rw [← hX.eq, mul_assoc, e_sq', mul_smul_comm]
  have h2 : g * (X * g') * g = X * g := by
    rw [← mul_assoc g X, ← hX.eq]; simp only [mul_assoc]; rw [← mul_assoc g, hgg]
  have h3 : g * (g' * X) * g = X * g := by
    rw [mul_assoc, mul_assoc, hX.eq]; simp only [← mul_assoc]; rw [hgg]
  have h4 : g * (g' * X * g') * g = Y * g := by
    rw [hXY, ← mul_assoc g Y, ← hY.eq]; simp only [mul_assoc]; rw [← mul_assoc g, hgg]
  have hexp : crossing δ A (Fin.castSucc (Fin.last m)) * X *
      crossing δ A (Fin.castSucc (Fin.last m))
      = A ^ 2 • X - (A * A⁻¹) • (X * g') - (A * A⁻¹) • (g' * X) + A⁻¹ ^ 2 • (g' * X * g') := by
    unfold crossing
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]
    module
  rw [hexp]
  simp only [mul_add, mul_sub, add_mul, sub_mul, mul_smul_comm, smul_mul_assoc, h1, h2, h3, h4]
  rw [mul_inv_cancel₀ hA]
  module

/-- **Reidemeister II through a cap.** If `X` commutes with the last generator `e`, then
`e σ' X σ'⁻¹ e = e e' X e' e`. -/
theorem cap_conj_cap {m : ℕ} (X : TLFin K δ (m + 2))
    (hX : Commute X (e K δ adjFin (Fin.last (m + 1)))) (hA : A ≠ 0)
    (hδ : δ = A ^ 2 + A⁻¹ ^ 2) :
    e K δ adjFin (Fin.last (m + 1)) * (crossing δ A (Fin.castSucc (Fin.last m)) * X *
        crossingInv δ A (Fin.castSucc (Fin.last m))) * e K δ adjFin (Fin.last (m + 1))
      = e K δ adjFin (Fin.last (m + 1)) * (e K δ adjFin (Fin.castSucc (Fin.last m)) * X *
        e K δ adjFin (Fin.castSucc (Fin.last m))) * e K δ adjFin (Fin.last (m + 1)) := by
  set g := e K δ adjFin (Fin.last (m + 1))
  set g' := e K δ adjFin (Fin.castSucc (Fin.last m))
  have hgg : g * g' * g = g := last_adj δ m
  have h1 : g * X * g = δ • (X * g) := by rw [← hX.eq, mul_assoc, e_sq', mul_smul_comm]
  have h2 : g * (X * g') * g = X * g := by
    rw [← mul_assoc g X, ← hX.eq]; simp only [mul_assoc]; rw [← mul_assoc g, hgg]
  have h3 : g * (g' * X) * g = X * g := by
    rw [mul_assoc, mul_assoc, hX.eq]; simp only [← mul_assoc]; rw [hgg]
  have hexp : crossing δ A (Fin.castSucc (Fin.last m)) * X *
      crossingInv δ A (Fin.castSucc (Fin.last m))
      = (A * A⁻¹) • X - A ^ 2 • (X * g') - A⁻¹ ^ 2 • (g' * X) + (A⁻¹ * A) • (g' * X * g') := by
    unfold crossing crossingInv
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]
    module
  rw [hexp]
  simp only [mul_add, mul_sub, add_mul, sub_mul, mul_smul_comm, smul_mul_assoc, h1, h2, h3]
  rw [mul_inv_cancel₀ hA, inv_mul_cancel₀ hA]
  have hd : δ • (X * g) = A ^ 2 • (X * g) + A⁻¹ ^ 2 • (X * g) := by rw [← add_smul, ← hδ]
  rw [hd]
  module

/-! ## Closing the Hopf loop -/

variable (δ A) in
/-- `Ω_n ∈ TL_{n+1}`: what is left of `hopfW (n + 1)` after its loop strand is closed. -/
noncomputable def omega : ∀ n : ℕ, TLFin K δ n
  | 0 => (A ^ 2 * δ - 2 + A⁻¹ ^ 2 * δ) • 1
  | n + 1 => (A ^ 2 * δ - 2) • hopfW δ A (n + 1) + A⁻¹ ^ 2 • incl δ n (omega n)

theorem incl_crossing' {m : ℕ} (i : Fin m) :
    incl δ m (crossing δ A i) = crossing δ A (Fin.castSucc i) := incl_crossing i

/-- **Closing the loop strand of the Hopf word.**
`e · ι(hopfW (n+1)) · e = ι(ι(Ω_n)) · e`. -/
theorem cap_hopf (hA : A ≠ 0) : ∀ n : ℕ,
    e K δ adjFin (Fin.last (n + 1)) * incl δ (n + 1) (hopfW δ A (n + 1)) *
        e K δ adjFin (Fin.last (n + 1))
      = incl δ (n + 1) (incl δ n (omega δ A n)) * e K δ adjFin (Fin.last (n + 1))
  | 0 => by
    have hw : incl δ 1 (hopfW δ A 1) = crossing δ A (Fin.castSucc (Fin.last 0)) * 1 *
        crossing δ A (Fin.castSucc (Fin.last 0)) := by
      rw [hopfW_succ, map_mul, map_mul, incl_crossing']
      simp [hopfW, hopfList]
    rw [hw, cap_sq (m := 0) 1 (δ • 1) (Commute.one_left _) (Commute.smul_left (Commute.one_left _) _)
      (by rw [mul_one, e_sq', smul_mul_assoc, one_mul]) hA]
    simp only [omega, map_smul, map_one]
    congr 1
    module
  | n + 1 => by
    have hw : incl δ (n + 2) (hopfW δ A (n + 2)) =
        crossing δ A (Fin.castSucc (Fin.last (n + 1))) *
          incl δ (n + 2) (incl δ (n + 1) (hopfW δ A (n + 1))) *
          crossing δ A (Fin.castSucc (Fin.last (n + 1))) := by
      rw [hopfW_succ, map_mul, map_mul, incl_crossing']
    have hX := incl_incl_commute δ (n + 1) (hopfW δ A (n + 1))
    have hY := incl_incl_commute δ (n + 1) (incl δ n (omega δ A n))
    have hXY : e K δ adjFin (Fin.castSucc (Fin.last (n + 1))) *
        incl δ (n + 2) (incl δ (n + 1) (hopfW δ A (n + 1))) *
        e K δ adjFin (Fin.castSucc (Fin.last (n + 1)))
        = incl δ (n + 2) (incl δ (n + 1) (incl δ n (omega δ A n))) *
          e K δ adjFin (Fin.castSucc (Fin.last (n + 1))) := by
      rw [← incl_e, ← map_mul, ← map_mul, cap_hopf hA n, map_mul]
    rw [hw, cap_sq _ _ hX hY hXY hA]
    simp only [omega, map_add, map_smul]

/-- The augmentation of a crossing is `A`. -/
theorem aug_crossing {m : ℕ} (i : Fin m) :
    augmentation K δ adjFin (crossing δ A i) = A := by
  simp [crossing]

theorem aug_hopfW (n : ℕ) : augmentation K δ adjFin (hopfW δ A n) = A ^ (2 * n) := by
  rw [hopfW, map_list_prod, List.map_map]
  have : (augmentation K δ adjFin ∘ crossing δ A) = fun _ : Fin n => A :=
    funext fun i => aug_crossing i
  rw [this, List.map_const', List.prod_replicate, hopfList_length]

/-- **The loop scalar.** `aug(Ω_n) = A^{2n+4} + A^{−(2n+4)}`. -/
theorem aug_omega (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) : ∀ n : ℕ,
    augmentation K δ adjFin (omega δ A n) = A ^ (2 * n + 4) + A⁻¹ ^ (2 * n + 4)
  | 0 => by
    have hB : A * A⁻¹ = 1 := mul_inv_cancel₀ hA
    simp only [omega, map_smul, map_one, smul_eq_mul, mul_one]
    rw [hδ]
    linear_combination 2 * (A * A⁻¹ + 1) * hB
  | n + 1 => by
    have hB : A * A⁻¹ = 1 := mul_inv_cancel₀ hA
    simp only [omega, map_add, map_smul, aug_incl, smul_eq_mul, aug_hopfW, aug_omega hA hδ n]
    rw [hδ]
    linear_combination 2 * A ^ (2 * n + 2) * (A * A⁻¹ + 1) * hB

/-- **One loop around `p_n` is a scalar.** Closing the loop strand of `hopfW (n+1)` on the
Jones–Wenzl projector `p_n` multiplies it by `A^{2n+4} + A^{−(2n+4)} = q^{n+2} + q^{−(n+2)}`. -/
theorem jw_cap_hopf (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n : ℕ) (hS : JWSpec δ n) :
    incl δ (n + 1) (incl δ n (jw δ n)) * e K δ adjFin (Fin.last (n + 1)) *
        incl δ (n + 1) (hopfW δ A (n + 1)) * e K δ adjFin (Fin.last (n + 1))
      = (A ^ (2 * n + 4) + A⁻¹ ^ (2 * n + 4)) •
        (incl δ (n + 1) (incl δ n (jw δ n)) * e K δ adjFin (Fin.last (n + 1))) := by
  have h := cap_hopf (δ := δ) hA n
  calc _ = incl δ (n + 1) (incl δ n (jw δ n)) * (e K δ adjFin (Fin.last (n + 1)) *
        incl δ (n + 1) (hopfW δ A (n + 1)) * e K δ adjFin (Fin.last (n + 1))) := by
          simp only [mul_assoc]
    _ = _ := by
      rw [h, ← mul_assoc, ← map_mul, ← map_mul, mul_eq_aug_smul hS.1, aug_omega hA hδ, map_smul,
        map_smul, smul_mul_assoc]

/-! ## A loop passing other strands -/

variable (δ A) in
/-- `loop n c ∈ TL_{n+c+2}`: the last strand goes once around the first `n + 1`, passing on one
side of the `c` strands in between. `loop n 0 = hopfW (n+1)`, and
`loop n (c+1) = σ · ι(loop n c) · σ⁻¹` with `σ` the last crossing. -/
noncomputable def loop (n : ℕ) : ∀ c : ℕ, TLFin K δ (n + c + 1)
  | 0 => hopfW δ A (n + 1)
  | c + 1 => crossing δ A (Fin.last (n + c + 1)) * incl δ (n + c + 1) (loop n c) *
      crossingInv δ A (Fin.last (n + c + 1))

variable (δ A) in
/-- `ι^c Ω_n ∈ TL_{n+c+1}`. -/
noncomputable def omegaC (n : ℕ) : ∀ c : ℕ, TLFin K δ (n + c)
  | 0 => omega δ A n
  | c + 1 => incl δ (n + c) (omegaC n c)

theorem aug_omegaC (n : ℕ) : ∀ c, augmentation K δ adjFin (omegaC δ A n c) =
    augmentation K δ adjFin (omega δ A n)
  | 0 => rfl
  | c + 1 => (aug_incl δ (n + c) (omegaC δ A n c)).trans (aug_omegaC n c)

theorem incl_crossingInv {m : ℕ} (i : Fin m) :
    incl δ m (crossingInv δ A i) = crossingInv δ A (Fin.castSucc i) := by
  simp [crossingInv, map_sub, map_smul, incl_e]

/-- **The passing loop closes to the same meridian.**
`e · ι(loop n c) · e = ι(ι(ι^c Ω_n)) · e`. -/
theorem cap_loop (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (n : ℕ) : ∀ c : ℕ,
    e K δ adjFin (Fin.last (n + c + 1)) * incl δ (n + c + 1) (loop δ A n c) *
        e K δ adjFin (Fin.last (n + c + 1))
      = incl δ (n + c + 1) (incl δ (n + c) (omegaC δ A n c)) *
        e K δ adjFin (Fin.last (n + c + 1))
  | 0 => cap_hopf hA n
  | c + 1 => by
    show e K δ adjFin (Fin.last (n + c + 2)) * incl δ (n + c + 2) (loop δ A n (c + 1)) *
        e K δ adjFin (Fin.last (n + c + 2))
      = incl δ (n + c + 2) (incl δ (n + c + 1) (incl δ (n + c) (omegaC δ A n c))) *
        e K δ adjFin (Fin.last (n + c + 2))
    have hw : incl δ (n + c + 2) (loop δ A n (c + 1)) =
        crossing δ A (Fin.castSucc (Fin.last (n + c + 1))) *
          incl δ (n + c + 2) (incl δ (n + c + 1) (loop δ A n c)) *
          crossingInv δ A (Fin.castSucc (Fin.last (n + c + 1))) := by
      rw [loop, map_mul, map_mul, incl_crossing', incl_crossingInv]
    have hX := incl_incl_commute δ (n + c + 1) (loop δ A n c)
    have hO : Commute (incl δ (n + c + 2) (incl δ (n + c + 1) (incl δ (n + c) (omegaC δ A n c))))
        (e K δ adjFin (Fin.last (n + c + 2))) :=
      incl_incl_commute δ (n + c + 1) (incl δ (n + c) (omegaC δ A n c))
    have hXY : e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1))) *
        incl δ (n + c + 2) (incl δ (n + c + 1) (loop δ A n c)) *
        e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1)))
        = incl δ (n + c + 2) (incl δ (n + c + 1) (incl δ (n + c) (omegaC δ A n c))) *
          e K δ adjFin (Fin.castSucc (Fin.last (n + c + 1))) := by
      rw [← incl_e, ← map_mul, ← map_mul, cap_loop hA hδ n c, map_mul]
    rw [hw, cap_conj_cap _ hX hA hδ, mul_assoc, mul_assoc, ← mul_assoc _ _
      (e K δ adjFin (Fin.last (n + c + 2))), hXY]
    simpa only [mul_assoc] using sandwich _ _ _ hO (last_adj δ (n + c + 1))

/-! ## The trace -/

/-- **Reidemeister II through the closure.** For a Markov trace with `δε = 1`,
`τ(ι(x)·σ·ι(w)·σ⁻¹) = τ(ι(x)·e·ι(w)·e)`. -/
theorem trace_conj {ε : K} (T : MarkovTower δ ε) (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)
    (hε : δ * ε = 1) {m : ℕ} (x w : TLFin K δ m) :
    T.τ (m + 1) (incl δ m x * (crossing δ A (Fin.last m) * incl δ m w *
        crossingInv δ A (Fin.last m)))
      = T.τ (m + 1) (incl δ m x * (e K δ adjFin (Fin.last m) * incl δ m w *
        e K δ adjFin (Fin.last m))) := by
  set g := e K δ adjFin (Fin.last m)
  have hexp : crossing δ A (Fin.last m) * incl δ m w * crossingInv δ A (Fin.last m)
      = (A * A⁻¹) • incl δ m w - A ^ 2 • (incl δ m w * g) - A⁻¹ ^ 2 • (g * incl δ m w)
        + (A⁻¹ * A) • (g * incl δ m w * g) := by
    unfold crossing crossingInv
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]
    module
  have t1 : T.τ (m + 1) (incl δ m x * incl δ m w) = T.τ m (x * w) := by
    rw [← map_mul, T.tr_incl]
  have t2 : T.τ (m + 1) (incl δ m x * (incl δ m w * g)) = ε * T.τ m (x * w) := by
    rw [← mul_assoc, ← map_mul, T.tr_markov]
  have t3 : T.τ (m + 1) (incl δ m x * (g * incl δ m w)) = ε * T.τ m (x * w) := by
    rw [← mul_assoc, T.tr_comm, ← mul_assoc, ← map_mul, T.tr_markov, T.tr_comm]
  rw [hexp]
  simp only [mul_add, mul_sub, mul_smul_comm, map_add, map_sub, map_smul, t1, t2, t3,
    smul_eq_mul]
  rw [mul_inv_cancel₀ hA, inv_mul_cancel₀ hA]
  have : T.τ m (x * w) - A ^ 2 * (ε * T.τ m (x * w)) - A⁻¹ ^ 2 * (ε * T.τ m (x * w))
      = (1 - δ * ε) * T.τ m (x * w) := by linear_combination (ε * T.τ m (x * w)) * hδ
  rw [one_mul, one_mul, this, hε, sub_self, zero_mul, zero_add]

/-- **Meridian removal.** For a Markov trace with `δε = 1`, closing the last strand of
`ι(x)·loop n (c+1)` leaves `ε` times the trace of `x·ι(ι^c Ω_n)`. -/
theorem trace_loop {ε : K} (T : MarkovTower δ ε) (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2)
    (hε : δ * ε = 1) (n c : ℕ) (x : TLFin K δ (n + c + 1)) :
    T.τ (n + c + 2) (incl δ (n + c + 1) x * loop δ A n (c + 1))
      = ε * T.τ (n + c + 1) (x * incl δ (n + c) (omegaC δ A n c)) := by
  show T.τ (n + c + 1 + 1) (incl δ (n + c + 1) x * (crossing δ A (Fin.last (n + c + 1)) *
      incl δ (n + c + 1) (loop δ A n c) * crossingInv δ A (Fin.last (n + c + 1)))) = _
  rw [trace_conj T hA hδ hε, cap_loop hA hδ n c, ← mul_assoc, ← map_mul, T.tr_markov]

end QOU.HeckeTemperleyLieb.TLMeridian
