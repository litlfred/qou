import Mathlib.Tactic
import QOU.StandardModel.ChiralityPolarizationHopf

/-!
# An SU(2) action on polarizations, and whether it reaches the Hecke letters

Bean `qou-qs2u`, owner ruling D1 (2026-11-15): *do not identify; derive*. Build an
`SU(2)` action on the polarization fibre, find an action on `H₃(q)` compatible with it,
and test whether it carries the letter pair `(σ₀, σ₁)` to every orthogonal pair
`(v, v⊥)`.

## Proved here

1. **The action on polarizations, transitive on orthogonal pairs** (model cone,
   generic `[CommRing R]`). Left multiplication by a unit quaternion `g` preserves
   Hermitian orthogonality (`leftMul_preserves_orth`). Every orthogonal unit pair
   `(p₁, p₂)` is the image of the standard pair `(1, c j + d k)` under `L_{p₁}`
   (`orth_pair_eq_leftMul_std`). So `SU(2) = Sp(1)` acts transitively on orthogonal
   pairs, through `hopf_leftMul` on the points of `S²`.
2. **Generators for an orthogonal pair commute** (`eigenAxis_commute`). For any
   idempotent `P` in any `R`-algebra, `a•P + b•(1−P)` and `c•P + d•(1−P)` commute.
   A Hecke element "attached to" the pair `(v, v⊥)` (eigenvalue `q` on one line,
   `−q⁻¹` on the other) has this shape, with `P` the projector onto `v`; so does the
   element attached to `(v⊥, v)`.
3. **The letters do not commute, and no homomorphism makes them** (`no_hom_to_axis_pair`).
   An injective ring homomorphism cannot send a non-commuting pair to a pair sharing an
   eigenprojector. In the two-dimensional block of `H₃` the letters
   `σ₀ = diag(q, −q⁻¹)` and `σ₁` below satisfy the Hecke and braid relations
   (`s0_hecke`, `s1_hecke`, `braid_s`) and do not commute unless `q² = −1` (`s_noncomm`).
4. **So no algebra automorphism of `H₃`, inner or outer, carries `(σ₀, σ₁)` to the
   generators of an orthogonal pair `(v, v⊥)`** (`no_automorphism_to_orthogonal_pair`).
   This is scope (b): the invariant is non-commutativity, which every injective
   homomorphism preserves. It rests on one modelling step, stated above: "the generator
   of the pair `(v, v⊥)`" means a Hecke element whose two eigenlines are `v` and `v⊥`.

## What does carry over (positive)

Conjugation by an invertible `g` in the `(2,1)` block is an inner automorphism of `H₃`
(trivial on the two one-dimensional blocks). It preserves the Hecke and braid relations
(`conj_hecke`, `conj_braid`). Since `GL₂` (and `U(2)`, for Hermitian-orthogonal
pairs) acts transitively on ordered pairs of distinct lines, it carries `σ₀`, whose
eigenlines are the `q`/`−q⁻¹` pair, to an element with any prescribed pair of
eigenlines. That transitivity is standard linear algebra and is not formalised here.

**Why the block statement covers `H₃`.** For generic `q`, `H₃ ≅ K ⊕ K ⊕ M₂(K)`, and
the `(2,1)` block is the only two-dimensional block, so every automorphism of `H₃`
maps it to itself and restricts to an injective endomorphism of `M₂(K)`. A pair of
targets attached to `(v, v⊥)` commutes in that block. That is the setting of
`no_automorphism_to_orthogonal_pair`; the decomposition of `H₃` is cited, not proved
here. So the `U(2)` action
reaches the **eigenline pair of a single letter**: the `+q` / `−q⁻¹` pair that the
Breit–Wheeler block calls left and right circular. It does not reach the pair of two
letters that the block calls horizontal and vertical.

Exact computation (`computations/probes/polarization_axes_h3_probe.py`): in the
symmetric form of the block, the `q`-lines of `σ₀` and `σ₁` sit at Bloch angle
`cos θ = −(q⁴ + 1)/(q² + 1)²` (`120°` at `q = 1`), never `90°` or `180°` for real `q`.

No `sorry`, no axiom, no `native_decide`, no class.
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-! ## 1. The polarization action is transitive on orthogonal pairs -/

/-- Left multiplication by a unit preserves `p̄₁ p₂`, hence Hermitian orthogonality. -/
theorem leftMul_preserves_orth {g : BringCone R} (hg : Quaternion.normSq g = 1)
    (p₁ p₂ : BringCone R) : star (g * p₁) * (g * p₂) = star p₁ * p₂ := by
  have hsg := star_mul_self_of_normSq hg
  rw [star_mul]
  calc star p₁ * star g * (g * p₂) = star p₁ * (star g * g) * p₂ := by
        simp only [mul_assoc]
    _ = star p₁ * p₂ := by rw [hsg, mul_one]

/-- **Every orthogonal unit pair is `L_{p₁}` of the standard pair `(1, c j + d k)`.** -/
theorem orth_pair_eq_leftMul_std {p₁ p₂ : BringCone R} (hp₁ : Quaternion.normSq p₁ = 1)
    (hre : (star p₁ * p₂).re = 0) (hi : (star p₁ * p₂).imI = 0) :
    p₁ * 1 = p₁ ∧
      p₁ * orthW (star p₁ * p₂).imJ (star p₁ * p₂).imK = p₂ := by
  have hps := mul_star_self_of_normSq hp₁
  refine ⟨mul_one _, ?_⟩
  have hw : orthW (star p₁ * p₂).imJ (star p₁ * p₂).imK = star p₁ * p₂ := by
    ext <;> simp [orthW, hre, hi]
  rw [hw, ← mul_assoc, hps, one_mul]

end QOU.Tetraplectic

namespace QOU.StandardModel.PolarizationHecke

/-! ## 2. Generators attached to one orthogonal pair commute -/

/-- **Two elements diagonal in the same idempotent commute.** -/
theorem eigenAxis_commute {K A : Type*} [CommRing K] [Ring A] [Algebra K A]
    (P : A) (hP : P * P = P) (a b c d : K) :
    (a • P + b • (1 - P)) * (c • P + d • (1 - P))
      = (c • P + d • (1 - P)) * (a • P + b • (1 - P)) := by
  have h1 : P * (1 - P) = 0 := by rw [mul_sub, mul_one, hP, sub_self]
  have h2 : (1 - P) * P = 0 := by rw [sub_mul, one_mul, hP, sub_self]
  have h3 : (1 - P) * (1 - P) = 1 - P := by
    rw [sub_mul, one_mul, mul_sub, mul_one, hP, sub_self, sub_zero]
  simp only [add_mul, mul_add, smul_mul_smul_comm, hP, h1, h2, h3, smul_zero, add_zero,
    zero_add, mul_comm a c, mul_comm b d]

/-- **No injective homomorphism sends a non-commuting pair to a pair sharing an
eigenprojector.** -/
theorem no_hom_to_axis_pair {K A B : Type*} [CommRing K] [Ring A] [Ring B] [Algebra K B]
    (f : A →+* B) (hf : Function.Injective f) {x y : A} (hxy : x * y ≠ y * x)
    (P : B) (hP : P * P = P) (a b c d : K) :
    ¬ (f x = a • P + b • (1 - P) ∧ f y = c • P + d • (1 - P)) := by
  rintro ⟨hx, hy⟩
  apply hxy
  apply hf
  rw [map_mul, map_mul, hx, hy]
  exact eigenAxis_commute P hP a b c d

/-! ## 3. The two-dimensional block of `H₃`

A faithful model of the `(2,1)` block with rational entries: `σ₀ = diag(q, −q⁻¹)` and
`σ₁` the conjugate (by a diagonal matrix) of the symmetric seminormal form. -/

variable {K : Type*} [Field K]

/-- `σ₀ = diag(q, −q⁻¹)`. -/
def s0 (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 0; 0, -q⁻¹]

/-- `σ₁`, with off-diagonal product `(q⁴ + q² + 1)/(q² + 1)²`. -/
def s1 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  !![-1 / (q ^ 3 + q), 1; (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2, q ^ 3 / (q ^ 2 + 1)]

/-- The Hecke quadratic `(x − q)(x + q⁻¹) = 0`, in any `K`-algebra. -/
def hecke {A : Type*} [Ring A] [Algebra K A] (q : K) (x : A) : Prop :=
  (x - q • 1) * (x + q⁻¹ • 1) = 0

theorem s0_hecke (q : K) : hecke q (s0 q) := by
  unfold hecke s0
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two]

theorem s1_hecke (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : hecke q (s1 q) := by
  have hq3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq hq2
  unfold hecke s1
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem braid_s (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    s0 q * s1 q * s0 q = s1 q * s0 q * s1 q := by
  have hq3 : q ^ 3 + q ≠ 0 := by
    have : q ^ 3 + q = q * (q ^ 2 + 1) := by ring
    rw [this]; exact mul_ne_zero hq hq2
  unfold s0 s1
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- **The letters do not commute** unless `q² = −1`. -/
theorem s_noncomm (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    s0 q * s1 q ≠ s1 q * s0 q := by
  intro h
  have h01 := congrFun (congrFun h 0) 1
  simp [s0, s1, Matrix.mul_apply, Fin.sum_univ_two] at h01
  apply hq2
  field_simp at h01
  linear_combination h01

/-- **No algebra automorphism carries `(σ₀, σ₁)` to the generators of an orthogonal
pair.** Here an automorphism of the block is any injective ring endomorphism, and "the
generators of `(v, v⊥)`" are two elements diagonal in the projector `P` onto `v`. -/
theorem no_automorphism_to_orthogonal_pair (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (f : Matrix (Fin 2) (Fin 2) K →+* Matrix (Fin 2) (Fin 2) K)
    (hf : Function.Injective f) (P : Matrix (Fin 2) (Fin 2) K) (hP : P * P = P)
    (a b c d : K) :
    ¬ (f (s0 q) = a • P + b • (1 - P) ∧ f (s1 q) = c • P + d • (1 - P)) :=
  no_hom_to_axis_pair f hf (s_noncomm q hq hq2) P hP a b c d

/-! ## 4. Conjugation preserves the relations (the positive half)

Stated for any `K`-algebra `A` and any pair `u, v` with `u v = v u = 1`; the `(2,1)` block
is the case `A = Matrix (Fin 2) (Fin 2) K`. -/

theorem conj_add_smul {A : Type*} [Ring A] [Algebra K A] {u v : A} (huv : u * v = 1)
    (x : A) (s : K) : u * x * v + s • (1 : A) = u * (x + s • 1) * v := by
  rw [mul_add, add_mul, mul_smul_comm, mul_one, smul_mul_assoc, huv]

theorem conj_hecke {A : Type*} [Ring A] [Algebra K A] (q : K) {x u v : A}
    (huv : u * v = 1) (hvu : v * u = 1) (hx : hecke q x) : hecke q (u * x * v) := by
  unfold hecke at *
  have hs : ∀ y : A, y - q • (1 : A) = y + (-q) • 1 := by
    intro y; rw [neg_smul, sub_eq_add_neg]
  rw [hs x] at hx
  rw [hs, conj_add_smul huv x (-q), conj_add_smul huv x q⁻¹]
  calc u * (x + (-q) • 1) * v * (u * (x + q⁻¹ • 1) * v)
      = u * ((x + (-q) • 1) * (v * u) * (x + q⁻¹ • 1)) * v := by simp only [mul_assoc]
    _ = 0 := by rw [hvu, mul_one, hx, mul_zero, zero_mul]

theorem conj_braid {A : Type*} [Ring A] {x y u v : A} (hvu : v * u = 1)
    (h : x * y * x = y * x * y) :
    (u * x * v) * (u * y * v) * (u * x * v) = (u * y * v) * (u * x * v) * (u * y * v) := by
  have key : ∀ a b c : A, (u * a * v) * (u * b * v) * (u * c * v) = u * (a * b * c) * v := by
    intro a b c
    calc (u * a * v) * (u * b * v) * (u * c * v)
        = u * (a * (v * u) * b * (v * u) * c) * v := by simp only [mul_assoc]
      _ = u * (a * b * c) * v := by rw [hvu, mul_one, mul_one]
  rw [key, key, h]

end QOU.StandardModel.PolarizationHecke
