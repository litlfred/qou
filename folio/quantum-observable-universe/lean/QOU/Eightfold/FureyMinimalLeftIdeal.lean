import QOU.MathlibExt.OctonionComplexStructure
import QOU.MathlibExt.OctonionDerivationProperties

set_option maxHeartbeats 8000000

/-!
# QOU.Eightfold.FureyMinimalLeftIdeal — Furey's minimal left ideals of `ℂ ⊗ 𝕆`

Bean `qou-s4xb` (epic `qou-8lxd`), stream 15. Formalises, sorry-free, the construction of
Furey's thesis §6.6 (`furey2016`, arXiv:1611.09182, held at
`library/arxiv-1611.09182v1/sections/sec-048-66-minimal-left-ideals.md`): the Witt
nilpotents `αⱼ`, the primitive idempotent `ωω† = α₁α₂α₃α₃†α₂†α₁†`, and the minimal left ideal
`S_u = (ℂ⊗𝕆)_L · ωω†` of the algebra of octonionic left-multiplication operators.

## Conventions

* The octonion table is the corpus's (`OctonionDerivations.octMul`, Baez: `eₐeₐ₊₁ = eₐ₊₃`
  mod 7), copied here over a generic commutative ring as `omul` and shown to BE the corpus
  table (`omul_map`).
* The special imaginary unit is the corpus colour unit `e₁` (`stdIm`), so that the `su(3)`
  below is literally the corpus `su3 stdIm ⊂ Der𝕆`. Furey uses `e₇`; the index shift
  `k ↦ k + 1` (mod 7 on `1..7`) is an automorphism of the Baez table carrying `e₇ ↦ e₁`, and
  carries Furey's `α₁ = ½(−e₅ + i e₄)`, `α₂ = ½(−e₃ + i e₁)`, `α₃ = ½(−e₆ + i e₂)` to the
  `α₁ = ½(−e₆ + i e₅)`, `α₂ = ½(−e₄ + i e₂)`, `α₃ = ½(−e₇ + i e₃)` used here.
* "Products of octonions act from the left" (Furey): `α β f := α(β f)`, i.e. composition of
  left-multiplication operators. We work with `βⱼ := 2αⱼ` (`Bm`) and `βⱼ† := 2αⱼ†` (`Bd`) so
  that the Clifford relations hold over ANY commutative ring containing a square root `i` of
  `−1`; the factor `1/2` enters only where the ideal is built (field, `2 ≠ 0`).

## Base ring (§7c)

Nothing here needs `ℂ`. The Witt decomposition needs exactly a square root of `−1`, so the
algebra is over a generic `[CommRing R]` with `i : R`, `i * i = −1`; the ideal and its
dimension are over a generic `[Field K] [CharZero K]` with such an `i` (minimal instance
`ℚ(i)`; char 0 is used only to base-change the corpus's ℚ-derivations). The second root `−i`
is the Galois conjugate; Furey's particle ↔ antiparticle map `i ↦ −i` (thesis §6.6, after
(6.21)) is the substitution `i ↦ −i` throughout (`Bd_eq_neg_Bm_neg`, `vacD_eq`).
-/

namespace QOU.Eightfold.FureyIdeal

open QOU.MathlibExt.OctonionDerivations

/-! ## 1. The octonion product over a generic commutative ring -/

section Generic

variable {R : Type*} [CommRing R]

/-- The corpus octonion product (Baez convention), over a generic commutative ring. -/
def omul (u v : Fin 8 → R) : Fin 8 → R :=
  ![u 0 * v 0 - u 1 * v 1 - u 2 * v 2 - u 3 * v 3 - u 4 * v 4 - u 5 * v 5 - u 6 * v 6 - u 7 * v 7, u 0 * v 1 + u 1 * v 0 + u 2 * v 4 + u 3 * v 7 - u 4 * v 2 + u 5 * v 6 - u 6 * v 5 - u 7 * v 3, u 0 * v 2 - u 1 * v 4 + u 2 * v 0 + u 3 * v 5 + u 4 * v 1 - u 5 * v 3 + u 6 * v 7 - u 7 * v 6, u 0 * v 3 - u 1 * v 7 - u 2 * v 5 + u 3 * v 0 + u 4 * v 6 + u 5 * v 2 - u 6 * v 4 + u 7 * v 1, u 0 * v 4 + u 1 * v 2 - u 2 * v 1 - u 3 * v 6 + u 4 * v 0 + u 5 * v 7 + u 6 * v 3 - u 7 * v 5, u 0 * v 5 - u 1 * v 6 + u 2 * v 3 - u 3 * v 2 - u 4 * v 7 + u 5 * v 0 + u 6 * v 1 + u 7 * v 4, u 0 * v 6 + u 1 * v 5 - u 2 * v 7 + u 3 * v 4 - u 4 * v 3 - u 5 * v 1 + u 6 * v 0 + u 7 * v 2, u 0 * v 7 + u 1 * v 3 + u 2 * v 6 - u 3 * v 1 + u 4 * v 5 - u 5 * v 4 - u 6 * v 2 + u 7 * v 0]

/-- **`omul` is the corpus table**: base change of `octMul` along any ring map `ℚ → R`. -/
theorem omul_map (f : ℚ →+* R) (u v : Fin 8 → ℚ) :
    omul (f ∘ u) (f ∘ v) = f ∘ octMul u v := by
  funext k
  fin_cases k <;> simp [omul, octMul]

/-- Left multiplication is additive and homogeneous in the right argument. -/
theorem omul_add_right (u v w : Fin 8 → R) : omul u (v + w) = omul u v + omul u w := by
  funext k; fin_cases k <;> simp [omul] <;> ring

theorem omul_smul_right (u : Fin 8 → R) (c : R) (v : Fin 8 → R) :
    omul u (c • v) = c • omul u v := by
  funext k; fin_cases k <;> simp [omul] <;> ring

theorem omul_add_left (u v w : Fin 8 → R) : omul (u + v) w = omul u w + omul v w := by
  funext k; fin_cases k <;> simp [omul] <;> ring

theorem omul_smul_left (c : R) (u v : Fin 8 → R) :
    omul (c • u) v = c • omul u v := by
  funext k; fin_cases k <;> simp [omul] <;> ring

/-- The octonion conjugate `x₀ − Σ xₖ eₖ`. -/
def oconj (u : Fin 8 → R) : Fin 8 → R := ![u 0, -u 1, -u 2, -u 3, -u 4, -u 5, -u 6, -u 7]

variable (i : R)

/-- `βⱼ = 2αⱼ`: `β₀ = −e₆ + i e₅`, `β₁ = −e₄ + i e₂`, `β₂ = −e₇ + i e₃`. -/
def beta : Fin 3 → Fin 8 → R
  | 0 => ![0, 0, 0, 0, 0, i, -1, 0]
  | 1 => ![0, 0, i, 0, -1, 0, 0, 0]
  | 2 => ![0, 0, 0, i, 0, 0, 0, -1]

/-- `βⱼ† = 2αⱼ†`, the Furey hermitian conjugate (`i ↦ −i` together with octonion
conjugation): `betaD i j = oconj (beta (−i) j)` (`betaD_eq`). -/
def betaD : Fin 3 → Fin 8 → R
  | 0 => ![0, 0, 0, 0, 0, i, 1, 0]
  | 1 => ![0, 0, i, 0, 1, 0, 0, 0]
  | 2 => ![0, 0, 0, i, 0, 0, 0, 1]

theorem betaD_eq (j : Fin 3) : betaD i j = oconj (beta (-i) j) := by
  funext k; fin_cases j <;> fin_cases k <;> simp [betaD, beta, oconj]

/-- `Bm i j x = βⱼ x` written out (each component has two terms). -/
def Bm : Fin 3 → (Fin 8 → R) → (Fin 8 → R)
  | 0 => fun x => ![-(i * x 5) + x 6, x 5 + i * x 6, -(i * x 3) + -(x 7), i * x 2 + x 4, -(x 3) + i * x 7, i * x 0 + -(x 1), -(x 0) + -(i * x 1), x 2 + -(i * x 4)]
  | 1 => fun x => ![-(i * x 2) + x 4, x 2 + i * x 4, i * x 0 + -(x 1), -(i * x 5) + -(x 6), -(x 0) + -(i * x 1), i * x 3 + x 7, x 3 + -(i * x 7), -(x 5) + i * x 6]
  | 2 => fun x => ![-(i * x 3) + x 7, x 3 + i * x 7, i * x 5 + x 6, i * x 0 + -(x 1), x 5 + -(i * x 6), -(i * x 2) + -(x 4), -(x 2) + i * x 4, -(x 0) + -(i * x 1)]

/-- `Bd i j x = βⱼ† x` written out. -/
def Bd : Fin 3 → (Fin 8 → R) → (Fin 8 → R)
  | 0 => fun x => ![-(i * x 5) + -(x 6), -(x 5) + i * x 6, -(i * x 3) + x 7, i * x 2 + -(x 4), x 3 + i * x 7, i * x 0 + x 1, x 0 + -(i * x 1), -(x 2) + -(i * x 4)]
  | 1 => fun x => ![-(i * x 2) + -(x 4), -(x 2) + i * x 4, i * x 0 + x 1, -(i * x 5) + x 6, x 0 + -(i * x 1), i * x 3 + -(x 7), -(x 3) + -(i * x 7), x 5 + i * x 6]
  | 2 => fun x => ![-(i * x 3) + -(x 7), -(x 3) + i * x 7, i * x 5 + -(x 6), i * x 0 + x 1, -(x 5) + -(i * x 6), -(i * x 2) + x 4, x 2 + i * x 4, x 0 + -(i * x 1)]

/-- **`Bm` is left multiplication by `βⱼ`** in the corpus table. -/
theorem Bm_eq (j : Fin 3) (x : Fin 8 → R) : Bm i j x = omul (beta i j) x := by
  funext k; fin_cases j <;> fin_cases k <;> simp [Bm, beta, omul] <;> ring

/-- **`Bd` is left multiplication by `βⱼ†`.** -/
theorem Bd_eq (j : Fin 3) (x : Fin 8 → R) : Bd i j x = omul (betaD i j) x := by
  funext k; fin_cases j <;> fin_cases k <;> simp [Bd, betaD, omul] <;> ring

/-- **Galois form of the dagger**: `βⱼ†` at root `i` is `−βⱼ` at the conjugate root `−i`. -/
theorem Bd_eq_neg_Bm_neg (j : Fin 3) (x : Fin 8 → R) : Bd i j x = -Bm (-i) j x := by
  funext k; fin_cases j <;> fin_cases k <;> simp [Bd, Bm] <;> ring

/-! ## 2. The Clifford (CAR) relations — `Cl(6)` from left multiplication -/

variable {i}

/-- `{βₐ, β_b†} = 4 δₐ_b` (i.e. `{αₐ, α_b†} = δₐ_b`). -/
theorem car_Bm_Bd (hi : i * i = -1) (a b : Fin 3) (x : Fin 8 → R) :
    Bm i a (Bd i b x) + Bd i b (Bm i a x) = if a = b then (4 : R) • x else 0 := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  funext k
  fin_cases a <;> fin_cases b <;> fin_cases k <;>
    simp [Bm, Bd] <;> ring_nf <;> simp only [h2] <;> ring_nf

/-- `{βₐ, β_b} = 0`. -/
theorem car_Bm_Bm (hi : i * i = -1) (a b : Fin 3) (x : Fin 8 → R) :
    Bm i a (Bm i b x) + Bm i b (Bm i a x) = 0 := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  funext k
  fin_cases a <;> fin_cases b <;> fin_cases k <;>
    simp [Bm] <;> ring_nf <;> simp only [h2] <;> ring_nf

/-- `{βₐ†, β_b†} = 0`. -/
theorem car_Bd_Bd (hi : i * i = -1) (a b : Fin 3) (x : Fin 8 → R) :
    Bd i a (Bd i b x) + Bd i b (Bd i a x) = 0 := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  funext k
  fin_cases a <;> fin_cases b <;> fin_cases k <;>
    simp [Bd] <;> ring_nf <;> simp only [h2] <;> ring_nf

/-! ## 3. The vacuum and the idempotent `ωω†` -/

variable (i) in
/-- The `S_u` vacuum vector `Ω = 1 + i e₁` (the image of `ωω†`). -/
def vac : Fin 8 → R := ![1, i, 0, 0, 0, 0, 0, 0]

/-- The annihilators kill the vacuum: `αⱼ Ω = 0` (Furey (6.20)). -/
theorem Bm_vac (hi : i * i = -1) (j : Fin 3) : Bm i j (vac i) = 0 := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  funext k; fin_cases j <;> fin_cases k <;> simp [Bm, vac] <;> ring_nf <;> simp only [h2] <;>
    ring_nf

/-- **The idempotent, scaled.** `β₀β₁β₂β₂†β₁†β₀† x = 32 (x₀ − i x₁) Ω`, i.e.
`ωω† x = ½(x₀ − i x₁) · Ω`: a rank-one operator onto the vacuum line. -/
theorem omega_omegaD_apply (hi : i * i = -1) (x : Fin 8 → R) :
    Bm i 0 (Bm i 1 (Bm i 2 (Bd i 2 (Bd i 1 (Bd i 0 x))))) =
      (32 * (x 0 - i * x 1)) • vac i := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  have h3 : i ^ 3 = -i := by rw [pow_succ, h2]; ring
  have h4 : i ^ 4 = 1 := by rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, h2]; ring
  have h5 : i ^ 5 = i := by rw [pow_succ, h4]; ring
  have h6 : i ^ 6 = -1 := by rw [show (6 : ℕ) = 2 * 3 from rfl, pow_mul, h2]; ring
  funext k
  fin_cases k <;> simp [Bm, Bd, vac] <;> ring_nf <;> simp only [h2, h3, h4, h5, h6] <;> ring_nf

variable (i) in
/-- The `S_d` vacuum vector `Ω' = 1 − i e₁ = vac (−i)`. -/
def vacD : Fin 8 → R := vac (-i)

/-- **The conjugate idempotent `ω†ω`** (Furey (6.21)) is rank one onto `Ω' = vac (−i)`: the
`S_d` vacuum is the Galois conjugate of the `S_u` vacuum. -/
theorem omegaD_omega_apply (hi : i * i = -1) (x : Fin 8 → R) :
    Bd i 0 (Bd i 1 (Bd i 2 (Bm i 2 (Bm i 1 (Bm i 0 x))))) =
      (32 * (x 0 + i * x 1)) • vacD i := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  have h3 : i ^ 3 = -i := by rw [pow_succ, h2]; ring
  have h4 : i ^ 4 = 1 := by rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, h2]; ring
  have h5 : i ^ 5 = i := by rw [pow_succ, h4]; ring
  have h6 : i ^ 6 = -1 := by rw [show (6 : ℕ) = 2 * 3 from rfl, pow_mul, h2]; ring
  funext k
  fin_cases k <;> simp [Bm, Bd, vacD, vac] <;> ring_nf <;> simp only [h2, h3, h4, h5, h6] <;>
    ring_nf

/-! ## 4. The Fock ladder: Furey's eight states (6.19) -/

variable (i) in
/-- The eight Fock vectors (scaled by `2^level`), in Furey's order (6.19):
`0 : ν = Ω`, `1,2,3 : d̄ʳᵍᵇ = αⱼ†Ω`, `4 : uʳ = α₃†α₂†Ω`, `5 : uᵍ = α₁†α₃†Ω`,
`6 : uᵇ = α₂†α₁†Ω`, `7 : e⁺ = α₃†α₂†α₁†Ω`. -/
def fock : Fin 8 → Fin 8 → R
  | 0 => ![1, i, 0, 0, 0, 0, 0, 0]
  | 1 => ![0, 0, 0, 0, 0, 2 * i, 2, 0]
  | 2 => ![0, 0, 2 * i, 0, 2, 0, 0, 0]
  | 3 => ![0, 0, 0, 2 * i, 0, 0, 0, 2]
  | 4 => ![0, 0, 0, 0, 0, 4, 4 * i, 0]
  | 5 => ![0, 0, 4, 0, 4 * i, 0, 0, 0]
  | 6 => ![0, 0, 0, 4, 0, 0, 0, 4 * i]
  | 7 => ![-8 * i, -8, 0, 0, 0, 0, 0, 0]

/-- The fermion level (number of `α†`'s) of each Fock vector. -/
def level : Fin 8 → ℕ
  | 0 => 0 | 1 => 1 | 2 => 1 | 3 => 1 | 4 => 2 | 5 => 2 | 6 => 2 | 7 => 3

theorem fock_zero : fock i 0 = vac i := rfl

/-- **The ladder**: each Fock vector is the stated chain of raising operators on `Ω`. -/
theorem fock_chain (hi : i * i = -1) :
    fock i 1 = Bd i 0 (vac i) ∧ fock i 2 = Bd i 1 (vac i) ∧ fock i 3 = Bd i 2 (vac i) ∧
    fock i 4 = Bd i 2 (Bd i 1 (vac i)) ∧ fock i 5 = Bd i 0 (Bd i 2 (vac i)) ∧
    fock i 6 = Bd i 1 (Bd i 0 (vac i)) ∧ fock i 7 = Bd i 2 (Bd i 1 (Bd i 0 (vac i))) := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  have h3 : i ^ 3 = -i := by rw [pow_succ, h2]; ring
  have h4 : i ^ 4 = 1 := by rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, h2]; ring
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> funext k <;> fin_cases k <;>
    simp [fock, Bd, vac] <;> ring_nf <;> simp only [h2, h3, h4] <;> ring_nf

/-- The top state is killed by every raising operator (the ladder terminates). -/
theorem Bd_top (hi : i * i = -1) (j : Fin 3) : Bd i j (fock i 7) = 0 := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  funext k; fin_cases j <;> fin_cases k <;> simp [Bd, fock] <;> ring_nf <;> simp only [h2] <;>
    ring_nf

variable (i) in
/-- The (scaled) number operator `4N = Σⱼ βⱼ†βⱼ`. -/
def numOp (x : Fin 8 → R) : Fin 8 → R := Bd i 0 (Bm i 0 x) + Bd i 1 (Bm i 1 x) + Bd i 2 (Bm i 2 x)

/-- **Number grading**: `N (fock k) = level k · fock k`; levels `0,1,1,1,2,2,2,3`. -/
theorem numOp_fock (hi : i * i = -1) (k : Fin 8) :
    numOp i (fock i k) = (4 * (level k : R)) • fock i k := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  have h3 : i ^ 3 = -i := by rw [pow_succ, h2]; ring
  funext m
  fin_cases k <;> fin_cases m <;> simp [numOp, Bd, Bm, fock, level] <;> ring_nf <;>
    simp only [h2, h3] <;> ring_nf

/-- The unit `e₁` over `R`. -/
def eOne : Fin 8 → R := ![0, 1, 0, 0, 0, 0, 0, 0]

/-- **The `e₁`-complex structure is `−i (−1)^N`** on the Fock basis: `L(e₁)` acts by `−i`
on levels 0, 2 and by `+i` on levels 1, 3. -/
theorem Le_fock (hi : i * i = -1) (k : Fin 8) :
    omul eOne (fock i k) = ((-1) ^ (level k + 1) * i) • fock i k := by
  have h2 : i ^ 2 = -1 := by rw [sq]; exact hi
  funext m
  fin_cases k <;> fin_cases m <;> simp [omul, eOne, fock, level] <;> ring_nf <;>
    simp only [h2] <;> ring_nf

end Generic

end QOU.Eightfold.FureyIdeal
