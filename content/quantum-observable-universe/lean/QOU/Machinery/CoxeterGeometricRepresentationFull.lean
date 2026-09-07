/-
# The geometric representation, tier 2 — general bond orders and FULL simple-injectivity

The Chebyshev leg, closing the last stated-open piece of the tier-1
geometric representation (#4308): the Coxeter relations hold in the
reflection representation at EVERY bond order, so the Tits residue
`σᵢ ≠ σⱼ` is discharged for EVERY Coxeter system — no simply-laced
hypothesis, no per-system decidability, nothing:

* **`reflEnd_pair_apply` / `formLin_i_pair` / `formLin_j_pair`** — the
  composite `g = fᵢfⱼ` acts by an affine correction supported on the two
  roots, and the scalar pair `(⟨αᵢ,·⟩, ⟨αⱼ,·⟩)` transforms by the
  explicit 2×2 recursion with `c = B(αᵢ, αⱼ)`.
* **`periodic_of_two_step`** — the trig engine: any real sequence
  satisfying `u(k+2) = 2cos φ · u(k+1) − u(k)` agrees with
  `α sin(kφ) + β cos(kφ)` (two-step induction), hence returns to its
  initial value when `mφ = 2π`. The only trigonometry is the angle
  -addition recursion and `sin 2π = 0, cos 2π = 1`.
* **`reflEnd_pair_pow_eq_one`** — `(fᵢfⱼ)^m = 1` at every `m ≥ 3`:
  the scalar sequences are `m`-periodic with `φ = 2π/m` (the composite
  trace identity `4c² − 2 = 2cos φ` is the double-angle formula), and
  periodicity alone forces both accumulated root-coefficient sums to
  vanish (`2Sx = 2c·Sy` and `(2c² − 2)Sy = 0` with `c² < 1`) — no
  closed-form summation is ever computed.
* **`reflEnd_isLiftable`** — the Coxeter relations for EVERY matrix
  (m = 0 free by `pow_zero`, m = 1 impossible off-diagonal, m = 2 the
  tier-1 commutation, m ≥ 3 above).
* **`geomRepFull` / `simple_injective`** — THE PAYOFF: the simple map
  of EVERY Coxeter system is injective. Tits faithfulness at the level
  the transversal program needs, with no residue anywhere.
* **`isReduced_iji_unconditional` / `braid_at_pair_unconditional` /
  `far_commute_at_pair_unconditional`** — cell faithfulness and the
  presentation laws on the length-rule module at every applicable pair
  of every Coxeter system, hypothesis-free. Supersedes the simply-laced
  tier-1 wrappers and the A₃ instantiation.

HONESTY (STRICT): sorry-free, hypothesis-free. What this does NOT
prove: full Tits faithfulness (`ℓ` of arbitrary words / the order of
`σᵢσⱼ` being exactly `mᵢⱼ`) — only simple-injectivity, which is all the
transversal program consumes.

✅ UPDATE (2026-09-07): the second of those two — **the order of `σᵢσⱼ`
being exactly `mᵢⱼ`** — is now proved, in
`QOU.Machinery.CoxeterDihedralOrder.dihedralExact_full`, off the scalar
recursion in this file. It needs *less* than `reflEnd_pair_pow_eq_one`
does, not more: tracking `⟨αᵢ, (fᵢfⱼ)^k αᵢ⟩` alone gives `cos (k·2π/m)`
with no sine and no invertibility, so `m ≥ 2` suffices where the forward
direction needs `m ≥ 3`. The FIRST half — `ℓ` of arbitrary words — is
still not proved here. Pair-canonicity of the τ-assignment
functor remains the one open item of the program. Base ring: `ℝ` by
necessity (§7c); the module payoffs stay generic `[CommRing R]`.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterGeometricRepresentation

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List
open QOU.Machinery.HeckeGeneral
open scoped Classical

variable {B : Type*} {M : CoxeterMatrix B}

/-! ## The composite action and the scalar recursion, general form -/

lemma reflEnd_pair_apply (M : CoxeterMatrix B) (i j : B) (w : B →₀ ℝ) :
    (reflEnd M i * reflEnd M j) w
      = w - Finsupp.single j (2 * formLin M j w)
          - Finsupp.single i
            (2 * (formLin M i w
              - 2 * bilinCoeff M i j * formLin M j w)) := by
  show reflEnd M i (reflEnd M j w) = _
  rw [reflEnd_apply M j w, reflEnd_apply M i (w - _), map_sub,
    formLin_single]
  congr 2
  ring

lemma formLin_i_pair (M : CoxeterMatrix B) (i j : B) (w : B →₀ ℝ) :
    formLin M i ((reflEnd M i * reflEnd M j) w)
      = -(formLin M i w) + 2 * bilinCoeff M i j * formLin M j w := by
  rw [reflEnd_pair_apply, map_sub, map_sub, formLin_single, formLin_single,
    bilinCoeff_diag]
  ring

lemma formLin_j_pair (M : CoxeterMatrix B) (i j : B) (w : B →₀ ℝ) :
    formLin M j ((reflEnd M i * reflEnd M j) w)
      = -(2 * bilinCoeff M i j) * formLin M i w
        + (4 * bilinCoeff M i j ^ 2 - 1) * formLin M j w := by
  rw [reflEnd_pair_apply, map_sub, map_sub, formLin_single, formLin_single,
    bilinCoeff_diag, bilinCoeff_symm M j i]
  ring

/-! ## The trig engine -/

private lemma sin_two_step (a f : ℝ) :
    Real.sin (a + 2 * f)
      = 2 * Real.cos f * Real.sin (a + f) - Real.sin a := by
  rw [show a + 2 * f = a + f + f from by ring, Real.sin_add (a + f) f,
    Real.sin_add a f, Real.cos_add a f]
  linear_combination (-Real.sin a) * Real.sin_sq_add_cos_sq f

private lemma cos_two_step (a f : ℝ) :
    Real.cos (a + 2 * f)
      = 2 * Real.cos f * Real.cos (a + f) - Real.cos a := by
  rw [show a + 2 * f = a + f + f from by ring, Real.cos_add (a + f) f,
    Real.cos_add a f, Real.sin_add a f]
  linear_combination (-Real.cos a) * Real.sin_sq_add_cos_sq f

private lemma two_step_eq (T : ℝ) (u v : ℕ → ℝ)
    (hu : ∀ k, u (k + 2) = T * u (k + 1) - u k)
    (hv : ∀ k, v (k + 2) = T * v (k + 1) - v k)
    (h0 : u 0 = v 0) (h1 : u 1 = v 1) : ∀ k, u k = v k := by
  intro k
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    match k with
    | 0 => exact h0
    | 1 => exact h1
    | (k + 2) => rw [hu, hv, ih (k + 1) (by omega), ih k (by omega)]

/-- **The periodicity engine**: a sequence obeying the Chebyshev
recursion at angle `φ` returns to its initial value after `m` steps
whenever `mφ` is a full turn. -/
private lemma periodic_of_two_step (φ : ℝ) (hs : Real.sin φ ≠ 0) (m : ℕ)
    (hsin : Real.sin (m * φ) = 0) (hcos : Real.cos (m * φ) = 1)
    (u : ℕ → ℝ)
    (hu : ∀ k, u (k + 2) = 2 * Real.cos φ * u (k + 1) - u k) :
    u m = u 0 := by
  set α := (u 1 - u 0 * Real.cos φ) / Real.sin φ with hα
  set v : ℕ → ℝ :=
    fun k => α * Real.sin (k * φ) + u 0 * Real.cos (k * φ) with hv
  have hvrec : ∀ k, v (k + 2) = 2 * Real.cos φ * v (k + 1) - v k := by
    intro k
    show α * Real.sin ((↑(k + 2) : ℝ) * φ)
        + u 0 * Real.cos ((↑(k + 2) : ℝ) * φ) = _
    push_cast
    rw [show ((k : ℝ) + 2) * φ = k * φ + 2 * φ from by ring,
      sin_two_step, cos_two_step,
      show (k : ℝ) * φ + φ = ((k : ℝ) + 1) * φ from by ring]
    show _ = 2 * Real.cos φ
        * (α * Real.sin ((↑(k + 1) : ℝ) * φ)
          + u 0 * Real.cos ((↑(k + 1) : ℝ) * φ))
      - (α * Real.sin ((k : ℝ) * φ) + u 0 * Real.cos ((k : ℝ) * φ))
    push_cast
    ring
  have h0 : u 0 = v 0 := by
    show u 0 = α * Real.sin ((0 : ℕ) * φ) + u 0 * Real.cos ((0 : ℕ) * φ)
    simp
  have h1 : u 1 = v 1 := by
    show u 1 = α * Real.sin ((1 : ℕ) * φ) + u 0 * Real.cos ((1 : ℕ) * φ)
    push_cast
    rw [one_mul, hα, div_mul_cancel₀ _ hs]
    ring
  have hall := two_step_eq (2 * Real.cos φ) u v hu hvrec h0 h1
  rw [hall m]
  show α * Real.sin ((m : ℝ) * φ) + u 0 * Real.cos ((m : ℝ) * φ) = u 0
  rw [hsin, hcos]
  ring

/-! ## The order-`m` relation at every `m ≥ 3` -/

/-- **`(fᵢfⱼ)^m = 1` at every bond order `m ≥ 3`.** The scalar pair is
`m`-periodic at angle `φ = 2π/m`, and periodicity alone forces the
accumulated root-coefficient sums to vanish. -/
theorem reflEnd_pair_pow_eq_one {i j : B} (hij : i ≠ j) {m : ℕ}
    (hm : M i j = m) (hm3 : 3 ≤ m) :
    (reflEnd M i * reflEnd M j) ^ m = 1 := by
  have hc : bilinCoeff M i j = -Real.cos (Real.pi / m) := by
    unfold bilinCoeff
    rw [if_neg hij, hm]
  set c := bilinCoeff M i j with hcdef
  set φ := 2 * Real.pi / m with hφ
  have hm0 : (m : ℝ) ≠ 0 := by
    have : (3 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hm3
    linarith
  have hφpos : 0 < φ := by
    rw [hφ]
    positivity
  have hφlt : φ < Real.pi := by
    rw [hφ, div_lt_iff₀ (by positivity)]
    have h3 : (3 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hm3
    nlinarith [Real.pi_pos]
  have hs : Real.sin φ ≠ 0 :=
    ne_of_gt (Real.sin_pos_of_pos_of_lt_pi hφpos hφlt)
  have hT : 4 * c ^ 2 - 2 = 2 * Real.cos φ := by
    rw [hc, hφ]
    have : 2 * Real.pi / m = 2 * (Real.pi / m) := by ring
    rw [this, Real.cos_two_mul]
    ring
  have hsq : c ^ 2 < 1 := by
    have hpyth := Real.sin_sq_add_cos_sq (Real.pi / m)
    have hsinpos : 0 < Real.sin (Real.pi / m) := by
      apply Real.sin_pos_of_pos_of_lt_pi
      · positivity
      · rw [div_lt_iff₀ (by positivity)]
        have h3 : (3 : ℝ) ≤ (m : ℝ) := by exact_mod_cast hm3
        nlinarith [Real.pi_pos]
    rw [hc]
    nlinarith [hsinpos]
  have hsinm : Real.sin ((m : ℝ) * φ) = 0 := by
    rw [hφ, show (m : ℝ) * (2 * Real.pi / m) = 2 * Real.pi from by
      rw [mul_comm, div_mul_cancel₀ _ hm0]]
    exact Real.sin_two_pi
  have hcosm : Real.cos ((m : ℝ) * φ) = 1 := by
    rw [hφ, show (m : ℝ) * (2 * Real.pi / m) = 2 * Real.pi from by
      rw [mul_comm, div_mul_cancel₀ _ hm0]]
    exact Real.cos_two_pi
  set g := reflEnd M i * reflEnd M j with hg
  apply LinearMap.ext
  intro w
  show (g ^ m) w = (1 : Module.End ℝ (B →₀ ℝ)) w
  set X : ℕ → ℝ := fun k => formLin M i ((g ^ k) w) with hX
  set Y : ℕ → ℝ := fun k => formLin M j ((g ^ k) w) with hY
  have hpow : ∀ k, (g ^ (k + 1)) w = g ((g ^ k) w) := by
    intro k
    rw [pow_succ']
    rfl
  have hXrec : ∀ k, X (k + 1) = -(X k) + 2 * c * Y k := by
    intro k
    show formLin M i ((g ^ (k + 1)) w) = _
    rw [hpow, hg]
    exact formLin_i_pair M i j _
  have hYrec : ∀ k, Y (k + 1) = -(2 * c) * X k + (4 * c ^ 2 - 1) * Y k := by
    intro k
    show formLin M j ((g ^ (k + 1)) w) = _
    rw [hpow, hg]
    exact formLin_j_pair M i j _
  have hX2 : ∀ k, X (k + 2) = 2 * Real.cos φ * X (k + 1) - X k := by
    intro k
    have e1 : X (k + 2) = -(X (k + 1)) + 2 * c * Y (k + 1) := hXrec (k + 1)
    have e2 : Y (k + 1) = -(2 * c) * X k + (4 * c ^ 2 - 1) * Y k := hYrec k
    have e3 : X (k + 1) = -(X k) + 2 * c * Y k := hXrec k
    rw [← hT, e1, e2, e3]
    ring
  have hY2 : ∀ k, Y (k + 2) = 2 * Real.cos φ * Y (k + 1) - Y k := by
    intro k
    have e1 : Y (k + 2) = -(2 * c) * X (k + 1) + (4 * c ^ 2 - 1) * Y (k + 1) :=
      hYrec (k + 1)
    have e2 : Y (k + 1) = -(2 * c) * X k + (4 * c ^ 2 - 1) * Y k := hYrec k
    have e3 : X (k + 1) = -(X k) + 2 * c * Y k := hXrec k
    rw [← hT, e1, e2, e3]
    ring
  have hXper : X m = X 0 := periodic_of_two_step φ hs m hsinm hcosm X hX2
  have hYper : Y m = Y 0 := periodic_of_two_step φ hs m hsinm hcosm Y hY2
  -- the accumulated sums vanish
  set Sx := ∑ k ∈ Finset.range m, X k with hSx
  set Sy := ∑ k ∈ Finset.range m, Y k with hSy
  have hshiftX : ∑ k ∈ Finset.range m, X (k + 1) = Sx + X m - X 0 := by
    have h1 := Finset.sum_range_succ' X m
    have h2 := Finset.sum_range_succ X m
    rw [h2] at h1
    linarith [h1]
  have hshiftY : ∑ k ∈ Finset.range m, Y (k + 1) = Sy + Y m - Y 0 := by
    have h1 := Finset.sum_range_succ' Y m
    have h2 := Finset.sum_range_succ Y m
    rw [h2] at h1
    linarith [h1]
  have hsumX : ∑ k ∈ Finset.range m, X (k + 1) = -Sx + 2 * c * Sy := by
    rw [Finset.sum_congr rfl (fun k _ => hXrec k), Finset.sum_add_distrib,
      Finset.sum_neg_distrib, ← Finset.mul_sum]
  have hsumY : ∑ k ∈ Finset.range m, Y (k + 1)
      = -(2 * c) * Sx + (4 * c ^ 2 - 1) * Sy := by
    rw [Finset.sum_congr rfl (fun k _ => hYrec k), Finset.sum_add_distrib,
      ← Finset.mul_sum, ← Finset.mul_sum]
  have E1 : 2 * Sx - 2 * c * Sy = 0 := by
    have h := hsumX
    rw [hshiftX, hXper] at h
    linear_combination h
  have E2 : (2 - 4 * c ^ 2) * Sy + 2 * c * Sx = 0 := by
    have h := hsumY
    rw [hshiftY, hYper] at h
    linear_combination h
  have hSy0 : Sy = 0 := by
    have hfinal : (2 - 2 * c ^ 2) * Sy = 0 := by
      linear_combination E2 - c * E1
    rcases mul_eq_zero.mp hfinal with h | h
    · exact absurd h (ne_of_gt (by nlinarith [hsq]))
    · exact h
  have hSx0 : Sx = 0 := by
    linear_combination (1 / 2 : ℝ) * E1 + c * hSy0
  -- the accumulated action formula
  have hform : ∀ k, (g ^ k) w
      = w - Finsupp.single j (2 * ∑ r ∈ Finset.range k, Y r)
          - Finsupp.single i
            (2 * ∑ r ∈ Finset.range k, (X r - 2 * c * Y r)) := by
    intro k
    induction k with
    | zero => simp
    | succ k ih =>
      have hstep : (g ^ (k + 1)) w = g ((g ^ k) w) := hpow k
      have happ : g ((g ^ k) w)
          = (g ^ k) w - Finsupp.single j (2 * Y k)
              - Finsupp.single i (2 * (X k - 2 * c * Y k)) := by
        have h := reflEnd_pair_apply M i j ((g ^ k) w)
        rw [← hg] at h
        exact h
      rw [hstep, happ, ih, Finset.sum_range_succ, Finset.sum_range_succ,
        mul_add, mul_add, Finsupp.single_add, Finsupp.single_add]
      abel
  rw [hform m]
  rw [show ∑ r ∈ Finset.range m, (X r - 2 * c * Y r)
      = Sx - 2 * c * Sy from by
    rw [Finset.sum_sub_distrib, ← Finset.mul_sum]]
  rw [← hSy, hSx0, hSy0]
  simp

/-! ## Full liftability and the payoff -/

/-- **The Coxeter relations hold in the geometric representation of
EVERY Coxeter matrix.** -/
theorem reflEnd_isLiftable (M : CoxeterMatrix B) :
    M.IsLiftable (reflEnd M) := by
  intro i j
  by_cases hij : i = j
  · subst hij
    rw [M.diagonal, pow_one, reflEnd_mul_self]
  · rcases Nat.lt_or_ge (M i j) 3 with h3 | h3
    · have h1 := M.off_diagonal i j hij
      rcases (show M i j = 0 ∨ M i j = 2 from by omega) with h | h
      · rw [h, pow_zero]
      · rw [h]
        have hcomm : Commute (reflEnd M i) (reflEnd M j) :=
          reflEnd_comm_of_eq_two hij h
        rw [hcomm.mul_pow, pow_two, pow_two, reflEnd_mul_self,
          reflEnd_mul_self, one_mul]
    · exact reflEnd_pair_pow_eq_one hij rfl h3

variable {W : Type*} [Group W]

/-- The geometric representation of an arbitrary Coxeter system. -/
noncomputable def geomRepFull (cs : CoxeterSystem M W) :
    W →* Module.End ℝ (B →₀ ℝ) :=
  cs.lift ⟨reflEnd M, reflEnd_isLiftable M⟩

@[simp] lemma geomRepFull_simple (cs : CoxeterSystem M W) (i : B) :
    geomRepFull cs (cs.simple i) = reflEnd M i :=
  cs.lift_apply_simple (reflEnd_isLiftable M) i

/-- **THE TITS RESIDUE, DISCHARGED IN FULL**: the simple map of every
Coxeter system is injective. -/
theorem simple_injective (cs : CoxeterSystem M W) :
    Function.Injective cs.simple := by
  intro i j h
  by_contra hij
  have happ := congrArg (geomRepFull cs) h
  rw [geomRepFull_simple, geomRepFull_simple] at happ
  have hv := congrArg
    (fun F : Module.End ℝ (B →₀ ℝ) => (F (Finsupp.single i 1)) i) happ
  simp only [reflEnd_apply, formLin_single, bilinCoeff_diag,
    Finsupp.sub_apply, Finsupp.single_eq_same] at hv
  rw [Finsupp.single_eq_of_ne hij] at hv
  norm_num at hv

theorem simple_ne_full (cs : CoxeterSystem M W) {i j : B} (hij : i ≠ j) :
    cs.simple i ≠ cs.simple j :=
  fun h => hij (simple_injective cs h)

/-- Cell faithfulness at every `M i j = 3` pair, unconditionally. -/
theorem isReduced_iji_unconditional (cs : CoxeterSystem M W) {i j : B}
    (hm : M i j = 3) : cs.IsReduced [i, j, i] :=
  isReduced_iji_of_simple_ne cs i j hm
    (simple_ne_full cs
      (fun he => by subst he; exact absurd (M.diagonal i ▸ hm) (by norm_num)))

/-- Cell faithfulness at every `M i j = 2` pair, unconditionally. -/
theorem isReduced_ij_unconditional (cs : CoxeterSystem M W) {i j : B}
    (hm : M i j = 2) : cs.IsReduced [i, j] :=
  isReduced_ij_of_simple_ne cs i j hm
    (simple_ne_full cs
      (fun he => by subst he; exact absurd (M.diagonal i ▸ hm) (by norm_num)))

/-- **Braid on the length-rule module at every `M i j = 3` pair of every
Coxeter system — NO hypothesis.** -/
theorem braid_at_pair_unconditional {R : Type*} [CommRing R]
    (cs : CoxeterSystem M W) {i j : B} (hm : M i j = 3) (h : R)
    (v : W → R) :
    letI S := dihedralTransversal cs i j hm (isReduced_iji_unconditional cs hm)
    mulStep S.Di h (mulStep S.Dj h (mulStep S.Di h v))
      = mulStep S.Dj h (mulStep S.Di h (mulStep S.Dj h v)) :=
  DihedralCosetStructure.braid_of_dihedral _ h v

/-- **Far commutation at every `M i j = 2` pair of every Coxeter system —
NO hypothesis.** -/
theorem far_commute_at_pair_unconditional {R : Type*} [CommRing R]
    (cs : CoxeterSystem M W) {i j : B} (hm : M i j = 2) (h : R)
    (v : W → R) :
    letI S := commutingTransversal cs i j hm (isReduced_ij_unconditional cs hm)
    mulStep S.Di h (mulStep S.Dj h v)
      = mulStep S.Dj h (mulStep S.Di h v) :=
  CommutingCosetStructure.far_commute_of_commuting _ h v

end QOU.Machinery.CoxeterParabolic
