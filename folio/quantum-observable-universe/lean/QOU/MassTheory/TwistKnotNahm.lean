import QOU.MassTheory.PreArchimedeanBloch

/-!
# The twist-knot state sum and its Nahm datum: `5₂`

`NahmBlochBridge` reads the figure-eight datum `A = (−1)` off the `q → 1` shift
ratio of Habiro's `4₁` summand. This file does the same for the twist knots
`K_p`, whose cyclotomic expansion is Masbaum's double sum, and so for `5₂ = K_2`
(bean `qou-35a8`).

**The summand.** At a Kashaev point (`q^N = 1`) the twist-knot sum is
`∑_{n ≥ k ≥ 0} S(n, k)` with, writing `(q)_m = ∏_{j=1}^m (1 − q^j)` and `n = a + k`,

    S(a, k) = (−1)^k q^{p·k(k+1) + C(k,2)} (1 − q^{2k+1}) q^n (q)_n³ / ((q)_{n+k+1} (q)_{n−k}).

`masbaumTerm` is this summand. `masbaumTerm_shift_n` and `masbaumTerm_shift_k`
are its two exact shift ratios, for every `q` that is not a root of unity.

**The saddle equations.** Put `X = q^n` and `Y = q^k` in the shift ratios and set
`q = 1`. Both ratios equal `1` exactly when (`TwistSaddle`)

    (1 − X)³ = (1 − XY)(1 − X/Y),        −Y^{2p+1} (1 − X/Y) = 1 − XY.

So the datum is read off the sum, not chosen: the Pochhammers give the shapes
`X`, `XY`, `X/Y` with multiplicities `3, −1, −1`, and the Gaussian
`q^{p·k(k+1) + C(k,2)}` gives the quadratic form `diag(0, −(2p+1))`. In the
convention `∏_ℓ (1 − z_ℓ)^{m_ℓ L_ℓi} = ε_i ∏_j x_j^{A_ij}` the datum is

    x = (X, Y),   L = [[1, 0], [1, 1], [1, −1]],   m = (3, −1, −1),
    A = diag(0, −(2p+1)),   ε = (1, −1).

`A` is symmetric, so the class `twistClass = 3[X] − [XY] − [X/Y]` is a Bloch class
up to the sign `ε`: Suslin's symbol of the class is `(−1) ∧ Y` for every `p`
(`deltaP_twistClass`). Hence

* `two_smul_twistClass_mem_blochGroup`: `2 · twistClass ∈ B(F)` over every field;
* `twistClass_mem_blochGroup_of_sq`: `twistClass ∈ B(F)` when `Y` is a square,
  in particular over any algebraically closed field
  (`twistClass_mem_blochGroup_isAlgClosed`).

**`5₂`.** For `p = 2` the system has the solutions `(X, Y) = (1 + t, t)` with
`t³ − t² + 2t − 1 = 0` (`fiveTwo_saddle_of_cubic`). With `y = 1 − t` this cubic is
`y³ − 2y² + 3y − 1 = 0`, the 5₂ saddle cubic already in the corpus
(`MathlibExt/FiveTwoSaddleSumRule.lean`). Its field has discriminant `−23`, the
trace field of `5₂`. Nothing here uses a measured value or a volume.

## Scope

Pre-Archimedean only: no `ℝ`, `ℂ`, limit or regulator. That the Bloch–Wigner
regulator of `twistClass` at the geometric root is `Vol(5₂)` is a separate,
Archimedean statement and is not claimed here. Masbaum's formula itself (that this
double sum is the coloured Jones / Kashaev invariant of `K_p`) is cited, not
proved; what is proved is everything from the summand down. Whether the sign `ε`
can be removed, so that `twistClass ∈ B(F)` over every field, is open here.

-- Ref: [masbaum2003] Masbaum, Skein-theoretical derivation of some formulas of Habiro, Algebr. Geom. Topol. 3 (2003) 537-556, Thm 3.2.
-- Ref: [nahm2007] Nahm, Conformal field theory and torsion elements of the Bloch group, in Frontiers in Number Theory, Physics and Geometry II (2007) 67-132.
-- Ref: [suslin1991] Suslin, K_3 of a field, and the Bloch group, Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-/

namespace QOU.Archimedean.TwistKnotNahm

open QOU.Archimedean.PreArchimedeanBloch

set_option linter.unusedSectionVars false

noncomputable section

variable {F : Type*} [Field F] [DecidableEq F]

/-! ## The summand and its exact shift ratios -/

/-- The `q`-Pochhammer `(q)_m = ∏_{j=1}^m (1 − q^j)`. -/
def poch (q : F) (m : ℕ) : F :=
  ∏ j ∈ Finset.range m, (1 - q ^ (j + 1))

theorem poch_succ (q : F) (m : ℕ) : poch q (m + 1) = poch q m * (1 - q ^ (m + 1)) := by
  simp [poch, Finset.prod_range_succ]

theorem poch_ne_zero {q : F} (hq : ∀ j : ℕ, 0 < j → q ^ j ≠ 1) (m : ℕ) : poch q m ≠ 0 := by
  rw [poch, Finset.prod_ne_zero_iff]
  intro j _
  exact sub_ne_zero.2 (hq (j + 1) (Nat.succ_pos j)).symm

/-- The Gaussian exponent `p·k(k+1) + C(k,2)`. -/
def gaussExp (p : ℤ) (k : ℕ) : ℤ := p * (k * (k + 1)) + (k.choose 2 : ℕ)

theorem gaussExp_succ (p : ℤ) (k : ℕ) :
    gaussExp p (k + 1) = gaussExp p k + (2 * p * (k + 1) + k) := by
  simp only [gaussExp, Nat.choose_succ_succ', Nat.choose_one_right]
  push_cast
  ring

/-- Masbaum's twist-knot summand at `n = a + k`. -/
def masbaumTerm (q : F) (p : ℤ) (a k : ℕ) : F :=
  (-1) ^ k * q ^ gaussExp p k * (1 - q ^ (2 * k + 1)) * q ^ (a + k) * poch q (a + k) ^ 3 /
    (poch q (a + 2 * k + 1) * poch q a)

/-- **Shift in `n` at fixed `k`.** Writing `X = q^n` (`n = a + k`) and `Y = q^k`,
the factors are `q^{n+1} = qX`, `q^{n+k+2} = q²XY`, `q^{n−k+1} = qX/Y`
(`shift_monomials`), so the ratio is
`S(n+1, k) / S(n, k) = q (1 − qX)³ / ((1 − q²XY)(1 − qX/Y))`. -/
theorem masbaumTerm_shift_n {q : F} (hq : ∀ j : ℕ, 0 < j → q ^ j ≠ 1) (p : ℤ) (a k : ℕ) :
    masbaumTerm q p (a + 1) k * ((1 - q ^ (a + 2 * k + 2)) * (1 - q ^ (a + 1)))
      = masbaumTerm q p a k * (q * (1 - q ^ (a + k + 1)) ^ 3) := by
  have hP := poch_ne_zero hq
  have h1 : (1 - q ^ (a + 2 * k + 2)) ≠ 0 := sub_ne_zero.2 (hq _ (by omega)).symm
  have h2 : (1 - q ^ (a + 1)) ≠ 0 := sub_ne_zero.2 (hq _ (by omega)).symm
  have e1 : a + 1 + k = (a + k) + 1 := by ring
  have e2 : a + 1 + 2 * k + 1 = (a + 2 * k + 1) + 1 := by ring
  have e3 : a + 2 * k + 1 + 1 = a + 2 * k + 2 := by ring
  unfold masbaumTerm
  rw [e1, e2, poch_succ q (a + k), poch_succ q (a + 2 * k + 1), poch_succ q a, e3,
    div_mul_eq_mul_div, div_mul_eq_mul_div,
    div_eq_div_iff (mul_ne_zero (mul_ne_zero (hP _) h1) (mul_ne_zero (hP _) h2))
      (mul_ne_zero (hP _) (hP _))]
  ring

/-- **Shift in `k` at fixed `n`.** Here `n = a + k + 1`; with `X = q^n`, `Y = q^k`
the factors are `q^{a+2k+3} = q²XY` and `q^{a+1} = X/Y`, so
`S(k+1) / S(k) = −q^{2p(k+1)+k} · (1 − q^{2k+3})/(1 − q^{2k+1}) · (1 − X/Y)/(1 − q²XY)`. -/
theorem masbaumTerm_shift_k {q : F} (h0 : q ≠ 0) (hq : ∀ j : ℕ, 0 < j → q ^ j ≠ 1)
    (p : ℤ) (a k : ℕ) :
    masbaumTerm q p a (k + 1) * ((1 - q ^ (2 * k + 1)) * (1 - q ^ (a + 2 * k + 3)))
      = masbaumTerm q p (a + 1) k *
          (-(q ^ (2 * p * ((k : ℤ) + 1) + (k : ℤ))) * (1 - q ^ (2 * k + 3)) * (1 - q ^ (a + 1))) := by
  have hP := poch_ne_zero hq
  have h1 : (1 - q ^ (a + 2 * k + 3)) ≠ 0 := sub_ne_zero.2 (hq _ (by omega)).symm
  have h2 : (1 - q ^ (a + 1)) ≠ 0 := sub_ne_zero.2 (hq _ (by omega)).symm
  have e1 : a + (k + 1) = a + k + 1 := by ring
  have e1' : a + 1 + k = a + k + 1 := by ring
  have e2 : a + 2 * (k + 1) + 1 = (a + 2 * k + 2) + 1 := by ring
  have e2' : a + 1 + 2 * k + 1 = a + 2 * k + 2 := by ring
  have e3 : 2 * (k + 1) + 1 = 2 * k + 3 := by ring
  have e4 : a + 2 * k + 2 + 1 = a + 2 * k + 3 := by ring
  have g : gaussExp p (k + 1) = gaussExp p k + (2 * p * ((k : ℤ) + 1) + (k : ℤ)) := by
    rw [gaussExp_succ]
  unfold masbaumTerm
  rw [e1, e1', e2, e2', e3, poch_succ q (a + 2 * k + 2), poch_succ q a, e4, g, zpow_add₀ h0,
    div_mul_eq_mul_div, div_mul_eq_mul_div,
    div_eq_div_iff (mul_ne_zero (mul_ne_zero (hP _) h1) (hP _))
      (mul_ne_zero (hP _) (mul_ne_zero (hP _) h2))]
  ring

/-- The monomials in the shift ratios, in terms of `X = q^n` and `Y = q^k`. -/
theorem shift_monomials {q : F} (h0 : q ≠ 0) (a k : ℕ) :
    q ^ (a + 2 * k + 2) = q ^ 2 * (q ^ (a + k) * q ^ k) ∧
      q ^ (a + 1) = q * (q ^ (a + k) / q ^ k) ∧
      q ^ (a + 2 * k + 3) = q ^ 2 * (q ^ (a + k + 1) * q ^ k) ∧
      q ^ (a + 1) = q ^ (a + k + 1) / q ^ k := by
  have hk : q ^ k ≠ 0 := pow_ne_zero _ h0
  refine ⟨by ring, ?_, by ring, ?_⟩
  · rw [mul_div_assoc', eq_div_iff hk]; ring
  · rw [eq_div_iff hk]; ring

/-! ## The saddle equations at `q = 1` -/

/-- The `q = 1` values of the two shift ratios equal `1`. -/
structure TwistSaddle (p : ℤ) (X Y : F) : Prop where
  X_ne_zero : X ≠ 0
  Y_ne_zero : Y ≠ 0
  XY_ne_one : X * Y ≠ 1
  X_ne_Y : X ≠ Y
  /-- `n`-ratio at `q = 1`. -/
  eq_n : (1 - X) ^ 3 = (1 - X * Y) * (1 - X / Y)
  /-- `k`-ratio at `q = 1`. -/
  eq_k : -(Y ^ (2 * p + 1)) * (1 - X / Y) = 1 - X * Y

/-- The twist-knot class `3[X] − [XY] − [X/Y] ∈ P(F)`. -/
def twistClass (X Y : F) : PreBloch F :=
  QuotientAddGroup.mk (3 • gen X - gen (X * Y) - gen (X / Y))

theorem u_pow {a : F} (ha : a ≠ 0) (m : ℕ) : u (a ^ m) = m • u a := by
  have h : a ^ m ≠ 0 := pow_ne_zero m ha
  simp only [u, ha, h, ne_eq, not_false_eq_true, dite_true]
  rw [← ofMul_pow]
  congr 1
  ext
  simp

theorem u_zpow {a : F} (ha : a ≠ 0) (m : ℤ) : u (a ^ m) = m • u a := by
  have h : a ^ m ≠ 0 := zpow_ne_zero m ha
  simp only [u, ha, h, ne_eq, not_false_eq_true, dite_true]
  rw [← ofMul_zpow]
  congr 1
  ext
  simp

theorem u_one : u (1 : F) = 0 := by
  simp only [u, ne_eq, one_ne_zero, not_false_eq_true, dite_true]
  rw [← ofMul_one]
  congr 1
  ext
  simp

/-- **Suslin's symbol of the twist-knot class is `(−1) ∧ Y`**, for every `p` and
every solution, and for every alternating pairing `β`. -/
theorem delta_twistClass {G : Type*} [AddCommGroup G]
    (β : Additive Fˣ →+ Additive Fˣ →+ G) (hβ : ∀ a, β a a = 0)
    (hanti : ∀ a b, β b a = - β a b) {p : ℤ} {X Y : F} (s : TwistSaddle p X Y) :
    delta β (3 • gen X - gen (X * Y) - gen (X / Y)) = β (u (-1)) (u Y) := by
  obtain ⟨hX, hY, hXY, hXneY, en, ek⟩ := s
  have hXY0 : X * Y ≠ 0 := mul_ne_zero hX hY
  have hXdY0 : X / Y ≠ 0 := div_ne_zero hX hY
  have hXdY1 : X / Y ≠ 1 := fun h => hXneY ((div_eq_one_iff_eq hY).1 h)
  have hA : (1 - X * Y) ≠ 0 := sub_ne_zero.2 (Ne.symm hXY)
  have hB : (1 - X / Y) ≠ 0 := sub_ne_zero.2 (Ne.symm hXdY1)
  have hX1 : X ≠ 1 := by
    intro h
    have h' : (1 - X * Y) * (1 - X / Y) = 0 := by rw [← en, h]; ring
    exact mul_ne_zero hA hB h'
  have hC : (1 - X) ≠ 0 := sub_ne_zero.2 (Ne.symm hX1)
  have hYp : Y ^ (2 * p + 1) ≠ 0 := zpow_ne_zero _ hY
  -- the two equations, additively
  have un : 3 • u (1 - X) = u (1 - X * Y) + u (1 - X / Y) := by
    rw [← u_mul hA hB, ← en, u_pow hC]
  have uk : u (1 - X * Y) = u (-1) + (2 * p + 1) • u Y + u (1 - X / Y) := by
    rw [← ek, neg_mul, neg_eq_neg_one_mul,
      u_mul (by norm_num) (mul_ne_zero hYp hB), u_mul hYp hB, u_zpow hY, add_assoc]
  rw [map_sub, map_sub, map_nsmul, delta_gen β hX hX1, delta_gen β hXY0 hXY,
    delta_gen β hXdY0 hXdY1, u_mul hX hY, u_div hX hY]
  have h3 : 3 • β (u X) (u (1 - X)) = β (u X) (3 • u (1 - X)) := (map_nsmul _ _ _).symm
  rw [h3, un, uk]
  simp only [map_add, map_sub, AddMonoidHom.add_apply, AddMonoidHom.sub_apply, map_zsmul,
    hβ]
  rw [hanti (u Y) (u (-1))]
  abel_nf

/-- Suslin's symbol of `twistClass` in `Λ²_ℤ F^×` is `(−1) ∧ Y`. -/
theorem deltaP_twistClass {p : ℤ} {X Y : F} (s : TwistSaddle p X Y) :
    deltaP (wedge F) (wedge_antisymm (F := F)) (twistClass X Y) = wedge F (u (-1)) (u Y) := by
  rw [twistClass, deltaP_mk]
  exact delta_twistClass (wedge F) wedge_self wedge_antisymm s

/-- `(−1) ∧ z` is killed by `2`. -/
theorem two_smul_wedge_neg_one (z : Additive Fˣ) : 2 • wedge F (u (-1)) z = 0 := by
  have h : (2 : ℕ) • u (-1 : F) = 0 := by
    rw [← u_pow (by norm_num), neg_one_sq, u_one]
  rw [← AddMonoidHom.nsmul_apply, ← map_nsmul, h, map_zero, AddMonoidHom.zero_apply]

/-- **Twice the twist-knot class is a Bloch class, over every field.** -/
theorem two_smul_twistClass_mem_blochGroup {p : ℤ} {X Y : F} (s : TwistSaddle p X Y) :
    2 • twistClass X Y ∈ BlochGroup F := by
  simp only [BlochGroup, AddMonoidHom.mem_ker, map_nsmul, deltaP_twistClass s]
  exact two_smul_wedge_neg_one _

/-- **The twist-knot class is a Bloch class when `Y` is a square.** -/
theorem twistClass_mem_blochGroup_of_sq {p : ℤ} {X Y W : F} (s : TwistSaddle p X Y)
    (hW : Y = W ^ 2) : twistClass X Y ∈ BlochGroup F := by
  have hW0 : W ≠ 0 := by
    rintro rfl
    exact s.Y_ne_zero (by simp [hW])
  simp only [BlochGroup, AddMonoidHom.mem_ker]
  rw [deltaP_twistClass s, hW, u_pow hW0, map_nsmul]
  exact two_smul_wedge_neg_one _

/-- Over an algebraically closed field every twist-knot class is a Bloch class. -/
theorem twistClass_mem_blochGroup_isAlgClosed [IsAlgClosed F] {p : ℤ} {X Y : F}
    (s : TwistSaddle p X Y) : twistClass X Y ∈ BlochGroup F := by
  obtain ⟨W, hW⟩ := IsAlgClosed.exists_pow_nat_eq Y (by norm_num : 0 < 2)
  exact twistClass_mem_blochGroup_of_sq s hW.symm

/-! ## `5₂ = K_2` -/

/-- **The `5₂` saddle solutions.** If `t³ − t² + 2t − 1 = 0` and `5 ≠ 0` in `F`,
then `(X, Y) = (1 + t, t)` solves the `p = 2` system. -/
theorem fiveTwo_saddle_of_cubic {t : F} (ht : t ^ 3 - t ^ 2 + 2 * t - 1 = 0)
    (h5 : (5 : F) ≠ 0) : TwistSaddle 2 (1 + t) t := by
  have ht0 : t ≠ 0 := by
    rintro rfl
    norm_num at ht
  have hX0 : 1 + t ≠ 0 := by
    intro h
    have : t = -1 := by linear_combination h
    subst this
    apply h5
    linear_combination -ht
  have hq : 1 - (1 + t) / t = -1 / t := by field_simp; ring
  refine ⟨hX0, ht0, ?_, ?_, ?_, ?_⟩
  · intro h
    -- `t² + t = 1` and the cubic force `5t = 3`, then `−1 = 0`
    have h53 : 5 * t - 3 = 0 := by linear_combination ht - (t - 2) * h
    have : (-1 : F) = 0 := by linear_combination (25 : F) * h - (5 * t + 8) * h53
    norm_num at this
  · intro h
    have : (1 : F) = 0 := by linear_combination h
    exact one_ne_zero this
  · rw [hq, mul_div_assoc', eq_div_iff ht0]
    linear_combination (-(t + 1)) * ht
  · have e : (t : F) ^ (2 * (2 : ℤ) + 1) = t ^ 5 := by norm_cast
    rw [e, hq, mul_div_assoc', div_eq_iff ht0]
    linear_combination (t * (t + 1)) * ht

/-- `5₂`: the class `3[1 + t] − [t(1 + t)] − [(1 + t)/t]` is a Bloch class up to `2`. -/
theorem fiveTwo_two_smul_mem_blochGroup {t : F} (ht : t ^ 3 - t ^ 2 + 2 * t - 1 = 0)
    (h5 : (5 : F) ≠ 0) : 2 • twistClass (1 + t) t ∈ BlochGroup F :=
  two_smul_twistClass_mem_blochGroup (fiveTwo_saddle_of_cubic ht h5)

/-- The cubic is the corpus's `5₂` saddle cubic `y³ − 2y² + 3y − 1` at `y = 1 − t`. -/
theorem fiveTwo_cubic_iff (t : F) :
    t ^ 3 - t ^ 2 + 2 * t - 1 = 0 ↔ (1 - t) ^ 3 - 2 * (1 - t) ^ 2 + 3 * (1 - t) - 1 = 0 := by
  constructor <;> intro h <;> linear_combination -h

end

end QOU.Archimedean.TwistKnotNahm
