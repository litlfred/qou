import QOU.Mathlib.SDPDuality
import Mathlib.Analysis.NormedSpace.HahnBanach.Separation
import Mathlib.Topology.Instances.Matrix
import Mathlib.Data.Real.StarOrdered
import Mathlib.Topology.Algebra.Module.FiniteDimension

/-!
# SDP strong duality under (dual) Slater

Real SDPs in standard form, with the trace pairing `⟨X, Y⟩ = tr(XY)`
(`QOU.Mathlib.SDPDuality.traceInner`):

* primal `(P)`: minimise `⟨C, X⟩` subject to `⟨Aᵢ, X⟩ = bᵢ` (`i : Fin m`) and `X ⪰ 0`;
* dual `(D)`: maximise `Σᵢ bᵢ yᵢ` subject to `C - Σᵢ yᵢ Aᵢ ⪰ 0`.

## What is proved (sorry-free, no new axioms)

* `posSemidef_iff_traceInner_nonneg` — self-duality of the PSD cone under the trace
  pairing: a Hermitian `M` is PSD iff `⟨M, X⟩ ≥ 0` for every PSD `X`.
* `isClosed_posSemidef`, `convex_posSemidef` — the PSD cone is closed and convex.
* `exists_sub_smul_one_posSemidef` — a positive-definite `S` dominates `ε • 1` for some
  `ε > 0`; `isCompact_psd_sublevel` — hence `{X ⪰ 0 : ⟨S, X⟩ ≤ R}` is compact.
* `isClosed_image_psd` — if some `C - Σ ȳᵢ Aᵢ` is positive definite (dual Slater), the
  image of the PSD cone under `X ↦ ((⟨Aᵢ, X⟩)ᵢ, ⟨C, X⟩)` is closed.  This is the step
  where Slater is used; without it the image cone need not be closed.
* `exists_primal_optimum` — under dual Slater and primal feasibility the primal minimum is
  attained.
* `strong_duality_of_dual_slater` — **main theorem**: if `Aᵢ`, `C` are symmetric, the
  primal is feasible and the dual is strictly feasible, then there is a primal optimum
  `X⋆` and, for every `ε > 0`, a dual-feasible `y` with `Σ bᵢ yᵢ > ⟨C, X⋆⟩ - ε`.
  The proof separates `(b, ⟨C, X⋆⟩ - ε)` from the closed convex image cone by
  `geometric_hahn_banach_closed_point`, reads off the coefficients of the separating
  functional, and converts its nonpositivity on the cone into dual feasibility via
  PSD self-duality.
* `no_duality_gap` — the same result as `IsLeast` (primal) / `IsLUB` (dual) of one common
  value `p`, combining the main theorem with `SDPDuality.weak_duality`.

## What is NOT proved here

* **Dual attainment.** Under dual Slater the dual supremum need not be attained, and it is
  not claimed.  The symmetric statement (primal Slater ⇒ dual attained, zero gap) is
  not proved in this file.
* The symmetry hypotheses `(Aᵢ).IsHermitian`, `C.IsHermitian` are genuinely used (PSD
  self-duality only sees the symmetric part); the non-symmetric case is not treated.
* Nothing here discharges `QOU.Interactions.ConfinementSDP`'s `strong_duality` field or
  `QOU.MathlibExt.SDP.HasStrongDuality` (which is stated for the *primal*-Slater direction
  over a general ring); wiring this theorem to those carriers is separate work.
-/
-- Ref: [leitner2026] Boyd–Vandenberghe, Convex Optimization, §5.9; Ben-Tal–Nemirovski, Lectures on Modern Convex Optimization, Thm 1.4.2

open Matrix Finset

namespace QOU.Mathlib.SDPStrongDuality
open QOU.Mathlib.SDPDuality

variable {n m : ℕ}

lemma traceInner_add_right (A X Y : Matrix (Fin n) (Fin n) ℝ) :
    traceInner A (X + Y) = traceInner A X + traceInner A Y := by
  simp only [traceInner, Matrix.mul_add, trace_add]

lemma traceInner_smul_right (c : ℝ) (A X : Matrix (Fin n) (Fin n) ℝ) :
    traceInner A (c • X) = c * traceInner A X := by
  simp only [traceInner, Matrix.mul_smul, trace_smul, smul_eq_mul]

/-- `⟨M, v vᵀ⟩ = vᵀ M v`. -/
lemma traceInner_vecMulVec (M : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) :
    traceInner M (vecMulVec v v) = v ⬝ᵥ (M *ᵥ v) := by
  simp only [traceInner, Matrix.trace, Matrix.diag, Matrix.mul_apply, vecMulVec_apply,
    dotProduct, mulVec, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun k _ => ?_
  ring

/-- A Hermitian matrix pairing nonnegatively with every PSD matrix is PSD. -/
theorem posSemidef_of_traceInner_nonneg {M : Matrix (Fin n) (Fin n) ℝ} (hM : M.IsHermitian)
    (h : ∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → 0 ≤ traceInner M X) :
    M.PosSemidef := by
  refine ⟨hM, fun v => ?_⟩
  have hv := h _ (posSemidef_vecMulVec_self_star v)
  simp only [star_trivial] at hv ⊢
  rwa [traceInner_vecMulVec] at hv

/-- **Self-duality of the PSD cone** under the trace pairing. -/
theorem posSemidef_iff_traceInner_nonneg {M : Matrix (Fin n) (Fin n) ℝ} (hM : M.IsHermitian) :
    M.PosSemidef ↔
      ∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → 0 ≤ traceInner M X :=
  ⟨fun hMp X hX => traceInner_nonneg_of_posSemidef M X hMp hX,
    posSemidef_of_traceInner_nonneg hM⟩

lemma continuous_traceInner (A : Matrix (Fin n) (Fin n) ℝ) :
    Continuous fun X : Matrix (Fin n) (Fin n) ℝ => traceInner A X :=
  (continuous_const.matrix_mul continuous_id).matrix_trace

/-- The PSD cone is closed. -/
lemma isClosed_posSemidef : IsClosed {X : Matrix (Fin n) (Fin n) ℝ | X.PosSemidef} := by
  have h1 : IsClosed {X : Matrix (Fin n) (Fin n) ℝ | X.IsHermitian} :=
    isClosed_eq continuous_id.matrix_conjTranspose continuous_id
  have h2 : IsClosed {X : Matrix (Fin n) (Fin n) ℝ |
      ∀ x : Fin n → ℝ, 0 ≤ star x ⬝ᵥ (X *ᵥ x)} := by
    simp only [Set.setOf_forall]
    exact isClosed_iInter fun x => isClosed_le continuous_const
      (continuous_const.dotProduct (continuous_id.matrix_mulVec continuous_const))
  exact h1.inter h2

/-- The PSD cone is convex. -/
lemma convex_posSemidef : Convex ℝ {X : Matrix (Fin n) (Fin n) ℝ | X.PosSemidef} := by
  intro X hX Y hY a b ha hb _
  exact (hX.smul ha).add (hY.smul hb)

lemma quad_single (X : Matrix (Fin n) (Fin n) ℝ) (i j : Fin n) :
    Pi.single i (1:ℝ) ⬝ᵥ (X *ᵥ Pi.single j 1) = X i j := by
  simp [mulVec_single, single_dotProduct]

lemma diag_nonneg {X : Matrix (Fin n) (Fin n) ℝ} (hX : X.PosSemidef) (i : Fin n) :
    0 ≤ X i i := by
  have := hX.2 (Pi.single i 1)
  simpa [star_trivial, quad_single] using this

lemma diag_le_trace {X : Matrix (Fin n) (Fin n) ℝ} (hX : X.PosSemidef) (i : Fin n) :
    X i i ≤ X.trace :=
  Finset.single_le_sum (f := fun k => X k k) (fun k _ => diag_nonneg hX k) (Finset.mem_univ i)

/-- Entries of a PSD matrix are bounded by its trace. -/
lemma abs_entry_le_trace {X : Matrix (Fin n) (Fin n) ℝ} (hX : X.PosSemidef) (i j : Fin n) :
    |X i j| ≤ X.trace := by
  have hsym : X j i = X i j := by
    have := congrFun (congrFun hX.1 i) j
    simpa [conjTranspose_apply, star_trivial] using this
  have hp := hX.2 (Pi.single i 1 + Pi.single j 1)
  have hm := hX.2 (Pi.single i 1 - Pi.single j 1)
  simp only [star_trivial, mulVec_add, mulVec_sub, dotProduct_add, add_dotProduct,
    dotProduct_sub, sub_dotProduct, quad_single, hsym] at hp hm
  have hi := diag_le_trace hX i
  have hj := diag_le_trace hX j
  rw [abs_le]; constructor <;> linarith


/-- A positive-definite `S` satisfies `S - ε • 1 ⪰ 0` for some `ε > 0`
(take `ε = 1 / (1 + Σ 1/λᵢ)` over the eigenvalues `λᵢ > 0`). -/
lemma exists_sub_smul_one_posSemidef {S : Matrix (Fin n) (Fin n) ℝ} (hS : S.PosDef) :
    ∃ ε : ℝ, 0 < ε ∧ (S - ε • (1 : Matrix (Fin n) (Fin n) ℝ)).PosSemidef := by
  classical
  set ev := hS.1.eigenvalues with hev
  have hpos : ∀ i, 0 < ev i := hS.eigenvalues_pos
  set T : ℝ := ∑ i, 1 / ev i with hT
  have hT0 : 0 ≤ T := Finset.sum_nonneg fun i _ => (one_div_pos.2 (hpos i)).le
  refine ⟨1 / (1 + T), by positivity, ?_⟩
  set ε : ℝ := 1 / (1 + T) with hε
  let U : Matrix (Fin n) (Fin n) ℝ := hS.1.eigenvectorUnitary
  have hspec : S = U * diagonal ev * star U := by
    have := hS.1.spectral_theorem
    rw [show RCLike.ofReal ∘ ev = ev from funext fun _ => rfl] at this
    exact this
  have hU : U * star U = 1 := unitary.mul_star_self_of_mem hS.1.eigenvectorUnitary.2
  have hle : ∀ i, ε ≤ ev i := by
    intro i
    have h1 : 1 / ev i ≤ T :=
      Finset.single_le_sum (f := fun j => 1 / ev j)
        (fun j _ => (one_div_pos.2 (hpos j)).le) (Finset.mem_univ i)
    rw [hε, div_le_iff₀ (by positivity)]
    have h2 : ev i * (1 / ev i) = 1 := mul_one_div_cancel (hpos i).ne'
    nlinarith [hpos i]
  have hD : (diagonal fun i => ev i - ε).PosSemidef :=
    PosSemidef.diagonal fun i => sub_nonneg.2 (hle i)
  have hdiag : (diagonal fun i => ev i - ε) = diagonal ev - ε • (1 : Matrix (Fin n) (Fin n) ℝ) := by
    ext a c
    by_cases h : a = c
    · subst h; simp
    · simp [diagonal_apply_ne _ h, one_apply_ne h]
  have key : S - ε • (1 : Matrix (Fin n) (Fin n) ℝ) = U * (diagonal fun i => ev i - ε) * Uᴴ := by
    rw [hdiag, ← star_eq_conjTranspose, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_smul,
      Matrix.mul_one, Matrix.smul_mul, hU, ← hspec]
  rw [key]
  exact hD.mul_mul_conjTranspose_same U

/-- The sublevel set `{X ⪰ 0 : ⟨S, X⟩ ≤ R}` of a positive-definite `S` is compact. -/
lemma isCompact_psd_sublevel {S : Matrix (Fin n) (Fin n) ℝ} (hS : S.PosDef) (R : ℝ) :
    IsCompact {X : Matrix (Fin n) (Fin n) ℝ | X.PosSemidef ∧ traceInner S X ≤ R} := by
  obtain ⟨ε, hε, hSε⟩ := exists_sub_smul_one_posSemidef hS
  have hbox : IsCompact (Set.pi Set.univ fun _ : Fin n =>
      Set.pi Set.univ fun _ : Fin n => Set.Icc (-(R / ε)) (R / ε) :
        Set (Fin n → Fin n → ℝ)) :=
    isCompact_univ_pi fun _ => isCompact_univ_pi fun _ => isCompact_Icc
  refine hbox.of_isClosed_subset
    (isClosed_posSemidef.inter (isClosed_le (continuous_traceInner S) continuous_const)) ?_
  rintro (X : Matrix (Fin n) (Fin n) ℝ) ⟨hX, hXR⟩
  have h0 := traceInner_nonneg_of_posSemidef _ X hSε hX
  rw [traceInner_sub_left, traceInner_smul_left] at h0
  have htr : traceInner 1 X = X.trace := by simp [traceInner]
  rw [htr] at h0
  have htrle : X.trace ≤ R / ε := by
    rw [le_div_iff₀ hε]; nlinarith
  intro i _ j _
  have := abs_entry_le_trace hX i j
  exact abs_le.1 (this.trans htrle)


/-- The constraint-and-objective map `X ↦ ((⟨A_i, X⟩)_i, ⟨C, X⟩)`. -/
noncomputable def constraintMap (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) :
    Matrix (Fin n) (Fin n) ℝ →ₗ[ℝ] (Fin m → ℝ) × ℝ where
  toFun X := (fun i => traceInner (A i) X, traceInner C X)
  map_add' X Y := by
    ext <;> simp [traceInner_add_right]
  map_smul' c X := by
    ext <;> simp [traceInner_smul_right]

@[simp] lemma constraintMap_apply (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (C X : Matrix (Fin n) (Fin n) ℝ) :
    constraintMap A C X = (fun i => traceInner (A i) X, traceInner C X) := rfl

lemma traceInner_slack (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (C : Matrix (Fin n) (Fin n) ℝ)
    (y : Fin m → ℝ) (X : Matrix (Fin n) (Fin n) ℝ) :
    traceInner (C - ∑ i, y i • A i) X = traceInner C X - ∑ i, y i * traceInner (A i) X := by
  rw [traceInner_sub_left, traceInner_finset_sum_left]
  simp only [traceInner_smul_left]

/-- **Closedness of the image cone under dual Slater.** If some `C - Σ ȳ_i A_i` is positive
definite, the image of the PSD cone under `constraintMap A C` is closed. -/
theorem isClosed_image_psd (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (C : Matrix (Fin n) (Fin n) ℝ)
    (ybar : Fin m → ℝ) (hslater : (C - ∑ i, ybar i • A i).PosDef) :
    IsClosed (constraintMap A C '' {X | X.PosSemidef}) := by
  set Sb := C - ∑ i, ybar i • A i with hSb
  set L := constraintMap A C with hL
  let ell : (Fin m → ℝ) × ℝ → ℝ := fun w => w.2 - ∑ i, ybar i * w.1 i
  have hell : Continuous ell :=
    continuous_snd.sub (continuous_finset_sum _ fun i _ =>
      continuous_const.mul ((continuous_apply i).comp continuous_fst))
  have hellL : ∀ X, ell (L X) = traceInner Sb X := fun X => by
    simp [ell, L, Sb, traceInner_slack]
  have hLc : Continuous L := LinearMap.continuous_of_finiteDimensional L
  refine isClosed_of_closure_subset fun w hw => ?_
  set R := ell w + 1
  have hK := isCompact_psd_sublevel hslater R
  have hKc : IsClosed (L '' {X | X.PosSemidef ∧ traceInner Sb X ≤ R}) :=
    (hK.image hLc).isClosed
  have hwK : w ∈ closure (L '' {X | X.PosSemidef ∧ traceInner Sb X ≤ R}) := by
    rw [mem_closure_iff]
    intro o ho hwo
    have hU : IsOpen {w' | ell w' < R} := isOpen_lt hell continuous_const
    have hwU : w ∈ {w' | ell w' < R} := by simp [R]
    obtain ⟨_, ⟨hxo, hxU⟩, ⟨X, hX, rfl⟩⟩ :=
      (mem_closure_iff.1 hw) _ (ho.inter hU) ⟨hwo, hwU⟩
    refine ⟨L X, hxo, X, ⟨hX, ?_⟩, rfl⟩
    have : ell (L X) < R := hxU
    rw [hellL] at this
    exact this.le
  rw [hKc.closure_eq] at hwK
  obtain ⟨X, ⟨hX, _⟩, hXw⟩ := hwK
  exact ⟨X, hX, hXw⟩


/-- The dual slack `C - Σ yᵢ Aᵢ` of symmetric data is symmetric. -/
lemma isHermitian_slack {A : Fin m → Matrix (Fin n) (Fin n) ℝ} {C : Matrix (Fin n) (Fin n) ℝ}
    (hA : ∀ i, (A i).IsHermitian) (hC : C.IsHermitian) (y : Fin m → ℝ) :
    (C - ∑ i, y i • A i).IsHermitian := by
  unfold Matrix.IsHermitian
  rw [conjTranspose_sub, conjTranspose_sum, hC.eq]
  congr 1
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [conjTranspose_smul, (hA i).eq, star_trivial]

/-- **Primal attainment under dual Slater.** If the primal is feasible and some
`C - Σ ȳᵢ Aᵢ` is positive definite, the primal minimum is attained. -/
theorem exists_primal_optimum (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (b : Fin m → ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ)
    (hprimal : ∃ X₀ : Matrix (Fin n) (Fin n) ℝ, X₀.PosSemidef ∧ ∀ i, traceInner (A i) X₀ = b i)
    (hslater : ∃ ybar : Fin m → ℝ, (C - ∑ i, ybar i • A i).PosDef) :
    ∃ Xs : Matrix (Fin n) (Fin n) ℝ, Xs.PosSemidef ∧ (∀ i, traceInner (A i) Xs = b i) ∧
      ∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → (∀ i, traceInner (A i) X = b i) →
        traceInner C Xs ≤ traceInner C X := by
  obtain ⟨X₀, hX₀, hX₀f⟩ := hprimal
  obtain ⟨ybar, hyb⟩ := hslater
  set Sb := C - ∑ i, ybar i • A i
  have hfeas : ∀ X, (∀ i, traceInner (A i) X = b i) →
      traceInner Sb X = traceInner C X - ∑ i, ybar i * b i := fun X hX => by
    simp only [Sb, traceInner_slack, hX]
  set R := traceInner Sb X₀
  let F := {X : Matrix (Fin n) (Fin n) ℝ | X.PosSemidef ∧ traceInner Sb X ≤ R} ∩
    {X | ∀ i, traceInner (A i) X = b i}
  have hFc : IsCompact F := by
    refine (isCompact_psd_sublevel hyb R).inter_right ?_
    simp only [Set.setOf_forall]
    exact isClosed_iInter fun i => isClosed_eq (continuous_traceInner _) continuous_const
  have hX₀F : X₀ ∈ F := ⟨⟨hX₀, le_rfl⟩, hX₀f⟩
  obtain ⟨Xs, ⟨⟨hXs, _⟩, hXsf⟩, hmin⟩ :=
    hFc.exists_isMinOn ⟨X₀, hX₀F⟩ (continuous_traceInner C).continuousOn
  refine ⟨Xs, hXs, hXsf, fun X hX hXf => ?_⟩
  by_cases hle : traceInner C X ≤ traceInner C X₀
  · refine hmin ⟨⟨hX, ?_⟩, hXf⟩
    simp only [R, hfeas X hXf, hfeas X₀ hX₀f]
    linarith
  · have := hmin hX₀F
    simp only [Set.mem_setOf_eq] at this
    linarith

/-- **SDP strong duality under dual Slater.** For symmetric data, if the primal is
feasible and the dual is strictly feasible (`C - Σ ȳᵢ Aᵢ` positive definite), then the
primal minimum is attained at some `Xs`, and the dual supremum equals `⟨C, Xs⟩`: every
`ε > 0` admits a dual-feasible `y` with `Σ bᵢ yᵢ > ⟨C, Xs⟩ - ε` (the reverse inequality is
`SDPDuality.weak_duality`). -/
theorem strong_duality_of_dual_slater (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (b : Fin m → ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i, (A i).IsHermitian) (hC : C.IsHermitian)
    (hprimal : ∃ X₀ : Matrix (Fin n) (Fin n) ℝ, X₀.PosSemidef ∧ ∀ i, traceInner (A i) X₀ = b i)
    (hslater : ∃ ybar : Fin m → ℝ, (C - ∑ i, ybar i • A i).PosDef) :
    ∃ Xs : Matrix (Fin n) (Fin n) ℝ, Xs.PosSemidef ∧ (∀ i, traceInner (A i) Xs = b i) ∧
      (∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → (∀ i, traceInner (A i) X = b i) →
        traceInner C Xs ≤ traceInner C X) ∧
      ∀ ε : ℝ, 0 < ε → ∃ y : Fin m → ℝ, (C - ∑ i, y i • A i).PosSemidef ∧
        traceInner C Xs - ε < ∑ i, b i * y i := by
  obtain ⟨Xs, hXs, hXsf, hopt⟩ := exists_primal_optimum A b C hprimal hslater
  refine ⟨Xs, hXs, hXsf, hopt, fun ε hε => ?_⟩
  obtain ⟨ybar, hyb⟩ := hslater
  set L := constraintMap A C
  set K := L '' {X : Matrix (Fin n) (Fin n) ℝ | X.PosSemidef}
  set t := traceInner C Xs - ε
  have hKcl : IsClosed K := isClosed_image_psd A C ybar hyb
  have hKcv : Convex ℝ K := convex_posSemidef.linear_image L
  have hnot : (b, t) ∉ K := by
    rintro ⟨X, hX, hXe⟩
    have h1 : ∀ i, traceInner (A i) X = b i := fun i =>
      congrFun (congrArg Prod.fst hXe) i
    have h2 : traceInner C X = t := congrArg Prod.snd hXe
    have := hopt X hX h1
    linarith
  obtain ⟨f, u, hfu, hu⟩ := geometric_hahn_banach_closed_point hKcv hKcl hnot
  have hu0 : 0 < u := by
    have := hfu 0 ⟨0, PosSemidef.zero, by simp⟩
    simpa using this
  have hfK : ∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → f (L X) ≤ 0 := by
    intro X hX
    by_contra hpos
    push_neg at hpos
    have hc : 0 < u / f (L X) := div_pos hu0 hpos
    have := hfu (L ((u / f (L X)) • X)) ⟨_, hX.smul hc.le, rfl⟩
    rw [map_smul, map_smul, smul_eq_mul, div_mul_cancel₀ _ hpos.ne'] at this
    exact lt_irrefl _ this
  -- coefficients of the separating functional
  let z : Fin m → ℝ := fun i => f ((fun j => if i = j then 1 else 0), 0)
  let σ : ℝ := f (0, 1)
  have hfrep : ∀ (v : Fin m → ℝ) (s : ℝ), f (v, s) = ∑ i, v i * z i + s * σ := by
    intro v s
    have hsplit : (v, s) = (v, (0:ℝ)) + s • ((0 : Fin m → ℝ), (1:ℝ)) := by
      ext <;> simp
    rw [hsplit, map_add, map_smul, smul_eq_mul]
    congr 1
    have := LinearMap.pi_apply_eq_sum_univ
      ((f : (Fin m → ℝ) × ℝ →L[ℝ] ℝ).toLinearMap.comp (LinearMap.inl ℝ (Fin m → ℝ) ℝ)) v
    simpa [z, smul_eq_mul] using this
  have hσ : σ < 0 := by
    have h1 := hfK Xs hXs
    have h2 := hu
    simp only [L, constraintMap_apply, hfrep] at h1
    rw [hfrep] at h2
    simp only [hXsf] at h1
    have : 0 < -ε * σ := by simp only [t] at h2; nlinarith
    nlinarith
  refine ⟨fun i => -z i / σ, ?_, ?_⟩
  · refine posSemidef_of_traceInner_nonneg (isHermitian_slack hA hC _) fun X hX => ?_
    have h1 := hfK X hX
    simp only [L, constraintMap_apply, hfrep] at h1
    rw [traceInner_slack]
    have hsum : ∑ i, -z i / σ * traceInner (A i) X = -(∑ i, traceInner (A i) X * z i) / σ := by
      rw [← Finset.sum_neg_distrib, Finset.sum_div]
      refine Finset.sum_congr rfl fun i _ => ?_
      ring
    rw [hsum, neg_div, sub_neg_eq_add]
    have : 0 ≤ (∑ i, traceInner (A i) X * z i + traceInner C X * σ) / σ :=
      div_nonneg_of_nonpos h1 hσ.le
    have hrw : (∑ i, traceInner (A i) X * z i + traceInner C X * σ) / σ =
        traceInner C X + (∑ i, traceInner (A i) X * z i) / σ := by
      rw [add_div, mul_div_cancel_right₀ _ hσ.ne, add_comm]
    linarith
  · have h2 := hu
    rw [hfrep] at h2
    have hsum : ∑ i, b i * (-z i / σ) = -(∑ i, b i * z i) / σ := by
      rw [← Finset.sum_neg_distrib, Finset.sum_div]
      refine Finset.sum_congr rfl fun i _ => ?_
      ring
    rw [hsum, lt_div_iff_of_neg hσ]
    linarith


/-- **No duality gap**: under the hypotheses of `strong_duality_of_dual_slater`, one value
`p` is the least primal objective value and the least upper bound of the dual objective
values. -/
theorem no_duality_gap (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (b : Fin m → ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i, (A i).IsHermitian) (hC : C.IsHermitian)
    (hprimal : ∃ X₀ : Matrix (Fin n) (Fin n) ℝ, X₀.PosSemidef ∧ ∀ i, traceInner (A i) X₀ = b i)
    (hslater : ∃ ybar : Fin m → ℝ, (C - ∑ i, ybar i • A i).PosDef) :
    ∃ p : ℝ,
      IsLeast {v | ∃ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef ∧
        (∀ i, traceInner (A i) X = b i) ∧ v = traceInner C X} p ∧
      IsLUB {d | ∃ y : Fin m → ℝ, (C - ∑ i, y i • A i).PosSemidef ∧
        d = ∑ i, b i * y i} p := by
  obtain ⟨Xs, hXs, hXsf, hopt, hgap⟩ :=
    strong_duality_of_dual_slater A b C hA hC hprimal hslater
  refine ⟨traceInner C Xs, ⟨⟨Xs, hXs, hXsf, rfl⟩, ?_⟩, ⟨?_, ?_⟩⟩
  · rintro v ⟨X, hX, hXf, rfl⟩
    exact hopt X hX hXf
  · rintro d ⟨y, hy, rfl⟩
    exact weak_duality A b C Xs y hXs hXsf _ hy (add_sub_cancel _ _)
  · intro B hB
    by_contra hlt
    push_neg at hlt
    obtain ⟨y, hy, hyv⟩ := hgap (traceInner C Xs - B) (sub_pos.2 hlt)
    have := hB ⟨y, hy, rfl⟩
    linarith

end QOU.Mathlib.SDPStrongDuality
