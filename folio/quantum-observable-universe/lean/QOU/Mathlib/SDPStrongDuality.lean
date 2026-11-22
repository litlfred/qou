import QOU.Mathlib.SDPDuality
import Mathlib.Analysis.NormedSpace.HahnBanach.Separation
import Mathlib.Topology.Instances.Matrix
import Mathlib.Data.Real.StarOrdered
import Mathlib.Topology.Algebra.Module.FiniteDimension
import Mathlib.Analysis.Convex.Topology
import Mathlib.LinearAlgebra.Dual.Lemmas
import QOU.MathlibExt.SDP

/-!
# SDP strong duality under dual Slater and under primal Slater

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

### Primal-Slater direction

* `exists_smul_one_add_smul_posSemidef` — for symmetric `E`, `L • 1 + c • E ⪰ 0` for all
  `|c| ≤ 1` (some `L ≥ 0`); with `exists_sub_smul_one_posSemidef` this gives
  `exists_psd_preimage_near_of_linearMap`: under primal Slater, for any linear `Q` with range
  inside `range 𝒜`, every right-hand side `b + Q u` with `u` small is attained by a PSD matrix
  with bounded objective (`exists_psd_preimage_near` is the case `Q = id`, onto `𝒜`).
* `surjective_of_linearIndependent` — linearly independent `Aᵢ` make
  `X ↦ (⟨Aᵢ, X⟩)ᵢ` onto.
* `strong_duality_of_primal_slater'` — **second main theorem**, with **no rank hypothesis**
  on the `Aᵢ`: symmetric data, a positive-definite primal-feasible `X̄`, and a dual-feasible
  point ⇒ the **dual optimum is attained** at some `ys` and every `ε > 0` admits a
  primal-feasible `X` with `⟨C, X⟩ < Σ bᵢ ysᵢ + ε` (no gap).  Proof: with `V = range 𝒜` and
  `U` a linear complement of `V`, separate `(0,0)` from the interior of
  `G = {(𝒜X - b + v, t) : X ⪰ 0, v ∈ U, t > ⟨C, X⟩ - inf (P)}`
  (`geometric_hahn_banach_open_point`); `(0,0) ∉ G` because `b ∈ V` and `V ∩ U = 0`, and the
  thickening by `U` gives `G` interior even when `𝒜` is not onto.  Extend to `G` by
  `closure (interior G) = closure G`, use Slater to make the `t`-coefficient negative, and
  read off a dual point by PSD self-duality.  `strong_duality_of_primal_slater` is the older
  signature with an (unused) onto hypothesis, derived from it.
* `exists_optimal_pair'` — under two-sided Slater (no rank hypothesis): a primal optimum and a
  dual optimum with equal objectives, and complementary slackness `⟨C - Σ ysᵢ Aᵢ, Xs⟩ = 0`.
  `exists_optimal_pair` is the older signature with an (unused) onto hypothesis.

### The `QOU.MathlibExt.SDP.HasStrongDuality` carrier

* `not_hasStrongDuality_unboundedSDP`, `not_forall_hasStrongDuality` — **the class is false
  as stated**: it asks for a primal-dual optimal pair from primal strict feasibility alone,
  and the `1 × 1` SDP "minimise `-x` over `x ⪰ 0`" is strictly feasible, unbounded below
  (`unboundedSDP_unbounded`) and has no dual-feasible point.
* `hasStrongDuality_of_slater'` — the class does hold for real SDPs with symmetric data and
  a positive-definite dual slack, with no rank condition on the constraints (a theorem, not
  an `instance`, since these hypotheses are not classes).  `hasStrongDuality_of_slater` is
  the older signature with an (unused) linear-independence hypothesis.

## What is NOT proved here

* **Dual attainment under dual Slater alone** and **primal attainment under primal Slater
  alone** are not claimed (both can fail).
* The symmetry hypotheses `(Aᵢ).IsHermitian`, `C.IsHermitian` are genuinely used (PSD
  self-duality only sees the symmetric part); the non-symmetric case is not treated.
* Nothing here discharges `QOU.Interactions.ConfinementSDP`'s `strong_duality` field.
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

/-- For a symmetric `E` there is `L ≥ 0` with `L • 1 + c • E ⪰ 0` whenever `|c| ≤ 1`
(take `L = Σ |λᵢ|` over the eigenvalues of `E`). -/
lemma exists_smul_one_add_smul_posSemidef {E : Matrix (Fin n) (Fin n) ℝ} (hE : E.IsHermitian) :
    ∃ L : ℝ, 0 ≤ L ∧ ∀ c : ℝ, |c| ≤ 1 →
      (L • (1 : Matrix (Fin n) (Fin n) ℝ) + c • E).PosSemidef := by
  classical
  set ev := hE.eigenvalues with hev
  set L : ℝ := ∑ i, |ev i| with hL
  have hL0 : 0 ≤ L := Finset.sum_nonneg fun i _ => abs_nonneg _
  refine ⟨L, hL0, fun c hc => ?_⟩
  let U : Matrix (Fin n) (Fin n) ℝ := hE.eigenvectorUnitary
  have hspec : E = U * diagonal ev * star U := by
    have := hE.spectral_theorem
    rw [show RCLike.ofReal ∘ ev = ev from funext fun _ => rfl] at this
    exact this
  have hU : U * star U = 1 := unitary.mul_star_self_of_mem hE.eigenvectorUnitary.2
  have hle : ∀ i, 0 ≤ L + c * ev i := by
    intro i
    have h1 : |ev i| ≤ L :=
      Finset.single_le_sum (f := fun j => |ev j|) (fun j _ => abs_nonneg _) (Finset.mem_univ i)
    have h2 : |c * ev i| ≤ |ev i| := by
      rw [abs_mul]; exact mul_le_of_le_one_left (abs_nonneg _) hc
    have h3 := neg_abs_le (c * ev i)
    linarith
  have hD : (diagonal fun i => L + c * ev i).PosSemidef := PosSemidef.diagonal hle
  have hdiag : (diagonal fun i => L + c * ev i) =
      L • (1 : Matrix (Fin n) (Fin n) ℝ) + c • diagonal ev := by
    ext a d
    by_cases h : a = d
    · subst h; simp
    · simp [diagonal_apply_ne _ h, one_apply_ne h]
  have key : L • (1 : Matrix (Fin n) (Fin n) ℝ) + c • E =
      U * (diagonal fun i => L + c * ev i) * Uᴴ := by
    rw [hdiag, ← star_eq_conjTranspose, Matrix.mul_add, Matrix.add_mul, Matrix.mul_smul,
      Matrix.mul_smul, Matrix.mul_one, Matrix.smul_mul, Matrix.smul_mul, hU, ← hspec]
  rw [key]
  exact hD.mul_mul_conjTranspose_same U

lemma traceInner_sum_right {ι : Type*} (s : Finset ι) (A : Matrix (Fin n) (Fin n) ℝ)
    (f : ι → Matrix (Fin n) (Fin n) ℝ) :
    traceInner A (∑ k ∈ s, f k) = ∑ k ∈ s, traceInner A (f k) := by
  simp only [traceInner, Matrix.mul_sum, trace_sum]

/-- For symmetric `A`, `⟨A, Xᵀ⟩ = ⟨A, X⟩`. -/
lemma traceInner_transpose_right {A : Matrix (Fin n) (Fin n) ℝ} (hA : A.IsHermitian)
    (X : Matrix (Fin n) (Fin n) ℝ) : traceInner A Xᵀ = traceInner A X := by
  have hAT : Aᵀ = A := by
    have := hA.eq
    rwa [conjTranspose_eq_transpose_of_trivial] at this
  unfold traceInner
  rw [← trace_transpose, transpose_mul, transpose_transpose, hAT, trace_mul_comm]

/-- If the constraint map is onto, each coordinate vector has a *symmetric* preimage. -/
lemma exists_symm_dual_basis (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (hA : ∀ i, (A i).IsHermitian)
    (hsurj : ∀ v : Fin m → ℝ, ∃ X : Matrix (Fin n) (Fin n) ℝ, ∀ i, traceInner (A i) X = v i)
    (k : Fin m) :
    ∃ E : Matrix (Fin n) (Fin n) ℝ, E.IsHermitian ∧
      ∀ i, traceInner (A i) E = if i = k then 1 else 0 := by
  obtain ⟨E', hE'⟩ := hsurj fun i => if i = k then 1 else 0
  refine ⟨(1/2 : ℝ) • (E' + E'ᵀ), ?_, fun i => ?_⟩
  · unfold Matrix.IsHermitian
    rw [conjTranspose_eq_transpose_of_trivial, transpose_smul, transpose_add,
      transpose_transpose, add_comm]
  · rw [traceInner_smul_right, traceInner_add_right, traceInner_transpose_right (hA i), hE' i]
    ring

/-- A vector in the range of the constraint map has a *symmetric* preimage. -/
lemma exists_symm_preimage (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (hA : ∀ i, (A i).IsHermitian) (d : Fin m → ℝ)
    (hd : ∃ X : Matrix (Fin n) (Fin n) ℝ, ∀ i, traceInner (A i) X = d i) :
    ∃ E : Matrix (Fin n) (Fin n) ℝ, E.IsHermitian ∧ ∀ i, traceInner (A i) E = d i := by
  obtain ⟨E', hE'⟩ := hd
  refine ⟨(1/2 : ℝ) • (E' + E'ᵀ), ?_, fun i => ?_⟩
  · unfold Matrix.IsHermitian
    rw [conjTranspose_eq_transpose_of_trivial, transpose_smul, transpose_add,
      transpose_transpose, add_comm]
  · rw [traceInner_smul_right, traceInner_add_right, traceInner_transpose_right (hA i), hE' i]
    ring

/-- **Primal Slater gives an interior point, relative to a linear map `Q`.** Let
`Q : ℝ^m → ℝ^m` be linear with range inside the range of the constraint map
`X ↦ (⟨Aᵢ, X⟩)ᵢ`.  If some `X̄` is positive definite, then for every `u` within `r` of `0`
(sup norm) the right-hand side `𝒜(X̄) + Q u` is attained by a PSD matrix whose objective value
is at most `M`.  With `Q = id` this needs an onto constraint map
(`exists_psd_preimage_near`); with `Q` a projection onto the range it needs nothing. -/
lemma exists_psd_preimage_near_of_linearMap (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i, (A i).IsHermitian)
    (Q : (Fin m → ℝ) →ₗ[ℝ] (Fin m → ℝ))
    (hQ : ∀ v : Fin m → ℝ, ∃ X : Matrix (Fin n) (Fin n) ℝ, ∀ i, traceInner (A i) X = Q v i)
    {Xbar : Matrix (Fin n) (Fin n) ℝ} (hXbar : Xbar.PosDef) :
    ∃ r : ℝ, 0 < r ∧ ∃ M : ℝ, ∀ u : Fin m → ℝ, ‖u‖ < r →
      ∃ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef ∧
        (∀ i, traceInner (A i) X = traceInner (A i) Xbar + Q u i) ∧ traceInner C X ≤ M := by
  classical
  choose E hEh hEA using fun k : Fin m =>
    exists_symm_preimage A hA (Q fun j => if k = j then 1 else 0) (hQ _)
  choose L hL0 hLpsd using fun k => exists_smul_one_add_smul_posSemidef (hEh k)
  obtain ⟨ε, hε, hXε⟩ := exists_sub_smul_one_posSemidef hXbar
  set w : ℝ := ε / (m + 1) with hw
  have hw0 : 0 < w := by positivity
  set SL : ℝ := ∑ k, L k with hSL
  have hSL0 : 0 ≤ SL := Finset.sum_nonneg fun k _ => hL0 k
  set ρ : ℝ := w / (1 + SL) with hρ
  have hρ0 : 0 < ρ := by positivity
  have hρL : ∀ k, ρ * L k ≤ w := by
    intro k
    have h1 : L k ≤ SL := Finset.single_le_sum (f := L) (fun j _ => hL0 j) (Finset.mem_univ k)
    have h2 : ρ * (1 + SL) = w := by rw [hρ]; field_simp
    nlinarith
  refine ⟨ρ, hρ0, traceInner C Xbar + ρ * ∑ k, |traceInner C (E k)|, fun u hu => ?_⟩
  have hu' : ∀ k, |u k| < ρ := fun k =>
    lt_of_le_of_lt (by simpa [Real.norm_eq_abs] using norm_le_pi_norm u k) hu
  refine ⟨Xbar + ∑ k, u k • E k, ?_, fun i => ?_, ?_⟩
  · -- PSD: split into `(X̄ - ε 1) + Σ_k (w 1 + u_k E_k) + (ε - m w) 1`
    have hk : ∀ k, (w • (1 : Matrix (Fin n) (Fin n) ℝ) + u k • E k).PosSemidef := by
      intro k
      have hc : |u k / ρ| ≤ 1 := by
        rw [abs_div, abs_of_pos hρ0, div_le_one hρ0]; exact (hu' k).le
      have h1 := (hLpsd k (u k / ρ) hc).smul hρ0.le
      have heq : w • (1 : Matrix (Fin n) (Fin n) ℝ) + u k • E k =
          ρ • (L k • (1 : Matrix (Fin n) (Fin n) ℝ) + (u k / ρ) • E k) +
            (w - ρ * L k) • (1 : Matrix (Fin n) (Fin n) ℝ) := by
        rw [smul_add, smul_smul, smul_smul, mul_div_cancel₀ _ hρ0.ne', sub_smul]
        abel
      rw [heq]
      exact h1.add (PosSemidef.one.smul (sub_nonneg.2 (hρL k)))
    have hsum : (∑ k, (w • (1 : Matrix (Fin n) (Fin n) ℝ) + u k • E k)).PosSemidef := by
      refine Finset.sum_induction _ (fun M : Matrix (Fin n) (Fin n) ℝ => M.PosSemidef)
        (fun a b ha hb => ha.add hb) PosSemidef.zero fun k _ => hk k
    have hmw : (0 : ℝ) ≤ ε - m * w := by
      rw [hw, mul_div_assoc', sub_nonneg, div_le_iff₀ (by positivity)]
      nlinarith
    have heq : Xbar + ∑ k, u k • E k =
        (Xbar - ε • (1 : Matrix (Fin n) (Fin n) ℝ)) +
          (∑ k, (w • (1 : Matrix (Fin n) (Fin n) ℝ) + u k • E k)) +
          (ε - m * w) • (1 : Matrix (Fin n) (Fin n) ℝ) := by
      rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
        ← Nat.cast_smul_eq_nsmul ℝ, smul_smul, sub_smul]
      abel
    rw [heq]
    exact (hXε.add hsum).add (PosSemidef.one.smul hmw)
  · rw [traceInner_add_right, traceInner_sum_right, LinearMap.pi_apply_eq_sum_univ Q u]
    simp only [traceInner_smul_right, hEA, Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
  · rw [traceInner_add_right, traceInner_sum_right, Finset.mul_sum]
    gcongr with k
    rw [traceInner_smul_right]
    calc u k * traceInner C (E k) ≤ |u k * traceInner C (E k)| := le_abs_self _
      _ = |u k| * |traceInner C (E k)| := abs_mul _ _
      _ ≤ ρ * |traceInner C (E k)| :=
          mul_le_mul_of_nonneg_right (hu' k).le (abs_nonneg _)

/-- **Primal Slater gives an interior point.** If the constraint map is onto and some
feasible `X̄` is positive definite, then every right-hand side within `r` of `b = 𝒜(X̄)`
(sup norm) is attained by a PSD matrix whose objective value is at most `M`. -/
lemma exists_psd_preimage_near (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i, (A i).IsHermitian)
    (hsurj : ∀ v : Fin m → ℝ, ∃ X : Matrix (Fin n) (Fin n) ℝ, ∀ i, traceInner (A i) X = v i)
    {Xbar : Matrix (Fin n) (Fin n) ℝ} (hXbar : Xbar.PosDef) :
    ∃ r : ℝ, 0 < r ∧ ∃ M : ℝ, ∀ u : Fin m → ℝ, ‖u‖ < r →
      ∃ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef ∧
        (∀ i, traceInner (A i) X = traceInner (A i) Xbar + u i) ∧ traceInner C X ≤ M :=
  exists_psd_preimage_near_of_linearMap A C hA LinearMap.id (fun v => hsurj v) hXbar

/-- **SDP strong duality under primal Slater (no rank hypothesis).** For symmetric data, if
some primal-feasible `X̄` is positive definite and the dual is feasible, then the **dual
optimum is attained** at some `ys` and there is **no duality gap**: every `ε > 0` admits a
primal-feasible `X` with `⟨C, X⟩ < Σ bᵢ ysᵢ + ε`.  No linear independence of the `Aᵢ` and
no surjectivity of `𝒜 : X ↦ (⟨Aᵢ, X⟩)ᵢ` is assumed.

Proof: with `p = inf (P)` (finite by weak duality), let `V = range 𝒜` and `U` any linear
complement of `V` in `ℝ^m`.  The convex set
`G = {(𝒜X - b + v, t) : X ⪰ 0, v ∈ U, t > ⟨C, X⟩ - p}` misses `(0, 0)` (since `b = 𝒜X̄ ∈ V`
and `V ∩ U = 0`) and, by primal Slater applied along the projection onto `V` along `U`, has
nonempty interior.  Separating `(0,0)` from `interior G` and passing to
`closure (interior G) = closure G` gives `f ≤ 0` on `G`; Slater forces the `t`-coefficient
`σ` of `f` to be negative, and `ys = -z / σ` is dual feasible (PSD self-duality) with
`Σ bᵢ ysᵢ ≥ p`.  The thickening by `U` replaces the earlier onto-hypothesis: when `𝒜` is onto,
`U = 0` and `G` is the set used before. -/
theorem strong_duality_of_primal_slater' (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (b : Fin m → ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i, (A i).IsHermitian) (hC : C.IsHermitian)
    (hslater : ∃ Xbar : Matrix (Fin n) (Fin n) ℝ, Xbar.PosDef ∧ ∀ i, traceInner (A i) Xbar = b i)
    (hdual : ∃ y₀ : Fin m → ℝ, (C - ∑ i, y₀ i • A i).PosSemidef) :
    ∃ ys : Fin m → ℝ, (C - ∑ i, ys i • A i).PosSemidef ∧
      (∀ y : Fin m → ℝ, (C - ∑ i, y i • A i).PosSemidef → ∑ i, b i * y i ≤ ∑ i, b i * ys i) ∧
      ∀ ε : ℝ, 0 < ε → ∃ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef ∧
        (∀ i, traceInner (A i) X = b i) ∧ traceInner C X < ∑ i, b i * ys i + ε := by
  obtain ⟨Xbar, hXbar, hXbarf⟩ := hslater
  obtain ⟨y₀, hy₀⟩ := hdual
  -- the primal value `p`
  set P := {v : ℝ | ∃ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef ∧
    (∀ i, traceInner (A i) X = b i) ∧ v = traceInner C X} with hP
  have hPne : P.Nonempty := ⟨_, Xbar, hXbar.posSemidef, hXbarf, rfl⟩
  have hPbdd : BddBelow P := by
    refine ⟨∑ i, b i * y₀ i, ?_⟩
    rintro v ⟨X, hX, hXf, rfl⟩
    exact weak_duality A b C X y₀ hX hXf _ hy₀ (add_sub_cancel _ _)
  set p := sInf P with hp
  have hple : ∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → (∀ i, traceInner (A i) X = b i) →
      p ≤ traceInner C X := fun X hX hXf => csInf_le hPbdd ⟨X, hX, hXf, rfl⟩
  -- the range `V` of the constraint map, and a complement `U` of it
  let T : Matrix (Fin n) (Fin n) ℝ →ₗ[ℝ] (Fin m → ℝ) :=
    LinearMap.fst ℝ (Fin m → ℝ) ℝ ∘ₗ constraintMap A 0
  have hT : ∀ X i, T X i = traceInner (A i) X := fun X i => rfl
  set V := LinearMap.range T with hV
  obtain ⟨U, hVU⟩ := Submodule.exists_isCompl V
  -- the convex set `G`, thickened by `U` so that it has interior even when `V ≠ ⊤`
  set G : Set ((Fin m → ℝ) × ℝ) := {w | ∃ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef ∧
    ∃ v ∈ U, (∀ i, w.1 i = traceInner (A i) X - b i + v i) ∧ traceInner C X - p < w.2}
    with hG
  have hGcv : Convex ℝ G := by
    rintro w₁ ⟨X₁, hX₁, v₁, hv₁, hu₁, ht₁⟩ w₂ ⟨X₂, hX₂, v₂, hv₂, hu₂, ht₂⟩ a c ha hc hac
    refine ⟨a • X₁ + c • X₂, (hX₁.smul ha).add (hX₂.smul hc), a • v₁ + c • v₂,
      U.add_mem (U.smul_mem a hv₁) (U.smul_mem c hv₂), fun i => ?_, ?_⟩
    · simp only [Prod.fst_add, Prod.smul_fst, Pi.add_apply, Pi.smul_apply, smul_eq_mul, hu₁,
        hu₂, traceInner_add_right, traceInner_smul_right]
      have : b i = (a + c) * b i := by rw [hac, one_mul]
      linarith
    · simp only [Prod.snd_add, Prod.smul_snd, smul_eq_mul, traceInner_add_right,
        traceInner_smul_right]
      have hpos : 0 < a * (w₁.2 - (traceInner C X₁ - p)) + c * (w₂.2 - (traceInner C X₂ - p)) := by
        rcases ha.lt_or_eq with ha' | ha'
        · have := mul_pos ha' (sub_pos.2 ht₁)
          have := mul_nonneg hc (sub_pos.2 ht₂).le
          linarith
        · subst ha'
          have hc1 : c = 1 := by linarith
          subst hc1
          simpa using sub_pos.2 ht₂
      have hp' : p = (a + c) * p := by rw [hac, one_mul]
      nlinarith
  have hnot0 : ((0 : Fin m → ℝ), (0 : ℝ)) ∉ G := by
    rintro ⟨X, hX, v, hv, hu, ht⟩
    have hdiff : (fun i => traceInner (A i) X - b i) ∈ V := by
      refine ⟨X - Xbar, ?_⟩
      rw [map_sub]
      funext i
      show T X i - T Xbar i = _
      rw [hT, hT, hXbarf]
    have hneg : (fun i => traceInner (A i) X - b i) = -v := by
      funext i
      have := hu i
      simp only [Pi.zero_apply, Pi.neg_apply] at this ⊢
      linarith
    have hzero := Submodule.disjoint_def.1 hVU.disjoint _ hdiff (hneg ▸ U.neg_mem hv)
    have hXf : ∀ i, traceInner (A i) X = b i := fun i => by
      have := congrFun hzero i; simp only [Pi.zero_apply] at this; linarith
    have := hple X hX hXf
    simp at ht
    linarith
  -- interior point from primal Slater
  -- (the projection onto `V` along `U` has range in `V`, so no surjectivity is needed)
  obtain ⟨r, hr, M, hM⟩ := exists_psd_preimage_near_of_linearMap A C hA
    (Submodule.IsCompl.projection hVU) (fun v => by
      obtain ⟨X, hX⟩ := (V.linearProjOfIsCompl U hVU v).2
      exact ⟨X, fun i => congrFun hX i⟩) hXbar
  have hball : ∀ u : Fin m → ℝ, ‖u‖ < r → ∀ t : ℝ, M - p < t → (u, t) ∈ G := by
    intro u hu t ht
    obtain ⟨X, hX, hXc, hXo⟩ := hM u hu
    have hsplit := Submodule.IsCompl.projection_add_projection_eq_self hVU u
    refine ⟨X, hX, Submodule.IsCompl.projection hVU.symm u,
      (U.linearProjOfIsCompl V hVU.symm u).2, fun i => ?_, by simp only; linarith⟩
    have := congrFun hsplit i
    simp only [Pi.add_apply] at this
    simp only [hXc, hXbarf]; linarith
  have hOsub : Metric.ball (0 : Fin m → ℝ) r ×ˢ Set.Ioi (M - p) ⊆ interior G :=
    interior_maximal (fun w ⟨h1, h2⟩ => hball w.1 (mem_ball_zero_iff.1 h1) w.2 h2)
      (Metric.isOpen_ball.prod isOpen_Ioi)
  have hint : ((0 : Fin m → ℝ), M - p + 1) ∈ interior G :=
    hOsub ⟨Metric.mem_ball_self hr, by simp⟩
  -- separation
  obtain ⟨f, hf⟩ := geometric_hahn_banach_open_point (hGcv.interior) isOpen_interior
    (fun h => hnot0 (interior_subset h))
  have hf0 : f ((0 : Fin m → ℝ), (0 : ℝ)) = 0 := by
    rw [show ((0 : Fin m → ℝ), (0 : ℝ)) = (0 : (Fin m → ℝ) × ℝ) from rfl, map_zero]
  have hfG : ∀ w ∈ G, f w ≤ 0 := by
    intro w hw
    have hcl : w ∈ closure (interior G) := by
      rw [hGcv.closure_interior_eq_closure_of_nonempty_interior ⟨_, hint⟩]
      exact subset_closure hw
    have : closure (interior G) ⊆ {x | f x ≤ 0} :=
      closure_minimal (fun x hx => by have := hf x hx; rw [hf0] at this; exact this.le)
        (isClosed_le f.continuous continuous_const)
    exact this hcl
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
  -- the key inequality on `G`
  have hkey : ∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → ∀ δ : ℝ, 0 < δ →
      ∑ i, (traceInner (A i) X - b i) * z i + (traceInner C X - p + δ) * σ ≤ 0 := by
    intro X hX δ hδ
    have := hfG ((fun i => traceInner (A i) X - b i), traceInner C X - p + δ)
      ⟨X, hX, 0, U.zero_mem, fun i => by simp, by simp only; linarith⟩
    rwa [hfrep] at this
  have hσle : σ ≤ 0 := by
    have h := hkey Xbar hXbar.posSemidef 1 one_pos
    simp only [hXbarf, sub_self, zero_mul, Finset.sum_const_zero, zero_add] at h
    have := hple Xbar hXbar.posSemidef hXbarf
    by_contra hσ
    push_neg at hσ
    have : 0 < (traceInner C Xbar - p + 1) * σ := mul_pos (by linarith) hσ
    linarith
  have hσ : σ < 0 := by
    refine lt_of_le_of_ne hσle fun hσ0 => ?_
    have hz : ∀ u : Fin m → ℝ, ‖u‖ < r → ∑ i, u i * z i ≤ 0 := by
      intro u hu
      have := hfG _ (hball u hu (M - p + 1) (by linarith))
      rwa [hfrep, hσ0, mul_zero, add_zero] at this
    set s : ℝ := r / (2 * (‖z‖ + 1)) with hs
    have hs0 : 0 < s := by positivity
    have hsz : ‖s • z‖ < r := by
      rw [norm_smul, Real.norm_eq_abs, abs_of_pos hs0, hs]
      rw [div_mul_eq_mul_div, div_lt_iff₀ (by positivity)]
      nlinarith [norm_nonneg z]
    have h1 := hz _ hsz
    simp only [Pi.smul_apply, smul_eq_mul, mul_assoc, ← Finset.mul_sum] at h1
    have h2 : ∑ i, z i * z i ≤ 0 := by
      by_contra h; push_neg at h; nlinarith [mul_pos hs0 h]
    have hzz : ∀ i, z i = 0 := by
      intro i
      have h3 : ∑ j, z j * z j = 0 :=
        le_antisymm h2 (Finset.sum_nonneg fun j _ => mul_self_nonneg _)
      have := (Finset.sum_eq_zero_iff_of_nonneg fun j _ => mul_self_nonneg (z j)).1 h3 i
        (Finset.mem_univ i)
      exact mul_self_eq_zero.1 this
    have := hf _ hint
    rw [hf0, hfrep, hσ0] at this
    simp [hzz] at this
  -- the dual point
  set ys : Fin m → ℝ := fun i => -z i / σ with hys
  have hysum : ∀ v : Fin m → ℝ, ∑ i, v i * ys i = -(∑ i, v i * z i) / σ := by
    intro v
    rw [← Finset.sum_neg_distrib, Finset.sum_div]
    refine Finset.sum_congr rfl fun i _ => ?_
    simp only [hys]; ring
  have hineq : ∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef →
      p - ∑ i, b i * ys i ≤ traceInner (C - ∑ i, ys i • A i) X := by
    intro X hX
    set a := ∑ i, traceInner (A i) X * z i
    set β := ∑ i, b i * z i
    have hsplit : ∑ i, (traceInner (A i) X - b i) * z i = a - β := by
      simp only [a, β, sub_mul, Finset.sum_sub_distrib]
    have hQ : a - β + (traceInner C X - p) * σ ≤ 0 := by
      by_contra hQ
      push_neg at hQ
      have hδ : 0 < (a - β + (traceInner C X - p) * σ) / (-2 * σ) :=
        div_pos hQ (by linarith)
      have := hkey X hX _ hδ
      rw [hsplit] at this
      have hσne : σ ≠ 0 := hσ.ne
      have e : (a - β + (traceInner C X - p) * σ) / (-2 * σ) * σ =
          -(a - β + (traceInner C X - p) * σ) / 2 := by
        field_simp
      rw [add_mul, e] at this
      linarith
    have h0 : 0 ≤ (a - β + (traceInner C X - p) * σ) / σ := div_nonneg_of_nonpos hQ hσ.le
    rw [add_div, mul_div_cancel_right₀ _ hσ.ne, sub_div] at h0
    rw [traceInner_slack]
    have e1 : ∑ i, ys i * traceInner (A i) X = -a / σ := by
      have := hysum fun i => traceInner (A i) X
      rw [show -a / σ = ∑ i, traceInner (A i) X * ys i from this.symm]
      exact Finset.sum_congr rfl fun i _ => mul_comm _ _
    have e2 : ∑ i, b i * ys i = -β / σ := by rw [hysum, neg_div]
    rw [e1, e2, neg_div, neg_div]
    linarith
  have hpys : p ≤ ∑ i, b i * ys i := by
    have := hineq 0 PosSemidef.zero
    simp [traceInner] at this
    linarith
  have hysfeas : (C - ∑ i, ys i • A i).PosSemidef := by
    refine posSemidef_of_traceInner_nonneg (isHermitian_slack hA hC ys) fun X hX => ?_
    by_contra hneg
    push_neg at hneg
    set d := p - ∑ i, b i * ys i
    set sX := traceInner (C - ∑ i, ys i • A i) X
    have hc : 0 < (|d| + 1) / (-sX) := div_pos (by positivity) (by linarith)
    have := hineq _ (hX.smul hc.le)
    rw [traceInner_smul_right] at this
    have e : (|d| + 1) / (-sX) * sX = -(|d| + 1) := by
      field_simp [hneg.ne]
    rw [e] at this
    have := neg_abs_le d
    linarith
  have hgap : ∀ ε : ℝ, 0 < ε → ∃ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef ∧
      (∀ i, traceInner (A i) X = b i) ∧ traceInner C X < ∑ i, b i * ys i + ε := by
    intro ε hε
    obtain ⟨v, ⟨X, hX, hXf, rfl⟩, hv⟩ := exists_lt_of_csInf_lt hPne (lt_add_of_pos_right p hε)
    exact ⟨X, hX, hXf, by linarith⟩
  refine ⟨ys, hysfeas, fun y hy => ?_, hgap⟩
  by_contra hlt
  push_neg at hlt
  obtain ⟨X, hX, hXf, hXv⟩ := hgap _ (sub_pos.2 hlt)
  have := weak_duality A b C X y hX hXf _ hy (add_sub_cancel _ _)
  linarith

/-- **SDP strong duality under primal Slater**, the form with an onto constraint map
`X ↦ (⟨Aᵢ, X⟩)ᵢ` (equivalently, linearly independent `Aᵢ` — see
`surjective_of_linearIndependent`).  The hypothesis `hsurj` is not needed: this is
`strong_duality_of_primal_slater'`, kept for its existing signature. -/
theorem strong_duality_of_primal_slater (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (b : Fin m → ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i, (A i).IsHermitian) (hC : C.IsHermitian)
    (_hsurj : ∀ v : Fin m → ℝ, ∃ X : Matrix (Fin n) (Fin n) ℝ, ∀ i, traceInner (A i) X = v i)
    (hslater : ∃ Xbar : Matrix (Fin n) (Fin n) ℝ, Xbar.PosDef ∧ ∀ i, traceInner (A i) Xbar = b i)
    (hdual : ∃ y₀ : Fin m → ℝ, (C - ∑ i, y₀ i • A i).PosSemidef) :
    ∃ ys : Fin m → ℝ, (C - ∑ i, ys i • A i).PosSemidef ∧
      (∀ y : Fin m → ℝ, (C - ∑ i, y i • A i).PosSemidef → ∑ i, b i * y i ≤ ∑ i, b i * ys i) ∧
      ∀ ε : ℝ, 0 < ε → ∃ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef ∧
        (∀ i, traceInner (A i) X = b i) ∧ traceInner C X < ∑ i, b i * ys i + ε :=
  strong_duality_of_primal_slater' A b C hA hC hslater hdual

/-- **Linear independence gives surjectivity of the constraint map.** If the `Aᵢ` are linearly
independent, every `v : Fin m → ℝ` is `(⟨Aᵢ, X⟩)ᵢ` for some `X`.  (A nonzero functional
`z` killing the range would give `⟨Σ zᵢ Aᵢ, X⟩ = 0` for all `X`; taking `X = (Σ zᵢ Aᵢ)ᵀ`
forces `Σ zᵢ Aᵢ = 0`, hence `z = 0`.) -/
theorem surjective_of_linearIndependent (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (hli : LinearIndependent ℝ A) :
    ∀ v : Fin m → ℝ, ∃ X : Matrix (Fin n) (Fin n) ℝ, ∀ i, traceInner (A i) X = v i := by
  let T : Matrix (Fin n) (Fin n) ℝ →ₗ[ℝ] (Fin m → ℝ) :=
    LinearMap.fst ℝ (Fin m → ℝ) ℝ ∘ₗ constraintMap A 0
  have htop : LinearMap.range T = ⊤ := by
    by_contra hne
    obtain ⟨f, hf0, hf⟩ :=
      Submodule.exists_dual_map_eq_bot_of_lt_top (lt_top_iff_ne_top.2 hne) inferInstance
    let z : Fin m → ℝ := fun i => f (fun j => if i = j then 1 else 0)
    have hfrep : ∀ v : Fin m → ℝ, f v = ∑ i, v i * z i := by
      intro v
      simpa [z, smul_eq_mul] using LinearMap.pi_apply_eq_sum_univ f v
    have hzero : ∀ X : Matrix (Fin n) (Fin n) ℝ, ∑ i, traceInner (A i) X * z i = 0 := by
      intro X
      have hmem : f (T X) ∈ (LinearMap.range T).map f := ⟨T X, ⟨X, rfl⟩, rfl⟩
      rw [hf, Submodule.mem_bot, hfrep] at hmem
      exact hmem
    set N := ∑ i, z i • A i with hNdef
    have hN : (N * Nᴴ).trace = 0 := by
      have h1 : traceInner N Nᵀ = 0 := by
        rw [hNdef, traceInner_finset_sum_left]
        simp only [traceInner_smul_left]
        rw [← hzero (∑ i, z i • A i)ᵀ]
        exact Finset.sum_congr rfl fun i _ => mul_comm _ _
      simpa [traceInner, conjTranspose_eq_transpose_of_trivial] using h1
    have hN0 : N = 0 := trace_mul_conjTranspose_self_eq_zero_iff.1 hN
    have hz := Fintype.linearIndependent_iff.1 hli z hN0
    apply hf0
    refine LinearMap.ext fun v => ?_
    rw [hfrep]
    simp [hz]
  intro v
  obtain ⟨X, hX⟩ := (LinearMap.range_eq_top.1 htop) v
  exact ⟨X, fun i => congrFun hX i⟩

/-- **Primal-dual optimal pair under two-sided Slater.** For symmetric data, a
positive-definite primal-feasible point and a positive-definite dual slack, there are a primal
optimum `Xs` and a dual optimum `ys` with equal objective values; complementary slackness
`⟨C - Σ ysᵢ Aᵢ, Xs⟩ = 0` follows.  No linear independence of the `Aᵢ` is assumed. -/
theorem exists_optimal_pair' (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (b : Fin m → ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i, (A i).IsHermitian) (hC : C.IsHermitian)
    (hpslater : ∃ Xbar : Matrix (Fin n) (Fin n) ℝ, Xbar.PosDef ∧ ∀ i, traceInner (A i) Xbar = b i)
    (hdslater : ∃ ybar : Fin m → ℝ, (C - ∑ i, ybar i • A i).PosDef) :
    ∃ (Xs : Matrix (Fin n) (Fin n) ℝ) (ys : Fin m → ℝ),
      Xs.PosSemidef ∧ (∀ i, traceInner (A i) Xs = b i) ∧
      (C - ∑ i, ys i • A i).PosSemidef ∧
      traceInner C Xs = ∑ i, b i * ys i ∧
      traceInner (C - ∑ i, ys i • A i) Xs = 0 ∧
      (∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → (∀ i, traceInner (A i) X = b i) →
        traceInner C Xs ≤ traceInner C X) ∧
      (∀ y : Fin m → ℝ, (C - ∑ i, y i • A i).PosSemidef → ∑ i, b i * y i ≤ ∑ i, b i * ys i) := by
  obtain ⟨Xbar, hXbar, hXbarf⟩ := hpslater
  obtain ⟨ybar, hyb⟩ := hdslater
  obtain ⟨Xs, hXs, hXsf, hopt⟩ :=
    exists_primal_optimum A b C ⟨Xbar, hXbar.posSemidef, hXbarf⟩ ⟨ybar, hyb⟩
  obtain ⟨ys, hys, hysopt, hgap⟩ := strong_duality_of_primal_slater' A b C hA hC
    ⟨Xbar, hXbar, hXbarf⟩ ⟨ybar, hyb.posSemidef⟩
  have heq : traceInner C Xs = ∑ i, b i * ys i := by
    refine le_antisymm ?_ (weak_duality A b C Xs ys hXs hXsf _ hys (add_sub_cancel _ _))
    by_contra h
    push_neg at h
    obtain ⟨X, hX, hXf, hXv⟩ := hgap _ (sub_pos.2 h)
    have := hopt X hX hXf
    linarith
  refine ⟨Xs, ys, hXs, hXsf, hys, heq, ?_, hopt, hysopt⟩
  rw [traceInner_slack, heq]
  simp only [hXsf, sub_eq_zero]
  exact Finset.sum_congr rfl fun i _ => mul_comm _ _

/-- **Primal-dual optimal pair under two-sided Slater**, the form with an onto constraint map.
The hypothesis `hsurj` is not needed: this is `exists_optimal_pair'`, kept for its existing
signature. -/
theorem exists_optimal_pair (A : Fin m → Matrix (Fin n) (Fin n) ℝ) (b : Fin m → ℝ)
    (C : Matrix (Fin n) (Fin n) ℝ) (hA : ∀ i, (A i).IsHermitian) (hC : C.IsHermitian)
    (_hsurj : ∀ v : Fin m → ℝ, ∃ X : Matrix (Fin n) (Fin n) ℝ, ∀ i, traceInner (A i) X = v i)
    (hpslater : ∃ Xbar : Matrix (Fin n) (Fin n) ℝ, Xbar.PosDef ∧ ∀ i, traceInner (A i) Xbar = b i)
    (hdslater : ∃ ybar : Fin m → ℝ, (C - ∑ i, ybar i • A i).PosDef) :
    ∃ (Xs : Matrix (Fin n) (Fin n) ℝ) (ys : Fin m → ℝ),
      Xs.PosSemidef ∧ (∀ i, traceInner (A i) Xs = b i) ∧
      (C - ∑ i, ys i • A i).PosSemidef ∧
      traceInner C Xs = ∑ i, b i * ys i ∧
      traceInner (C - ∑ i, ys i • A i) Xs = 0 ∧
      (∀ X : Matrix (Fin n) (Fin n) ℝ, X.PosSemidef → (∀ i, traceInner (A i) X = b i) →
        traceInner C Xs ≤ traceInner C X) ∧
      (∀ y : Fin m → ℝ, (C - ∑ i, y i • A i).PosSemidef → ∑ i, b i * y i ≤ ∑ i, b i * ys i) :=
  exists_optimal_pair' A b C hA hC hpslater hdslater

/-! ## The `HasStrongDuality` carrier of `QOU.MathlibExt.SDP`

`QOU.MathlibExt.SDP.HasStrongDuality sdp h` asks for a primal-dual optimal pair from
primal strict feasibility `h` **alone**.  That is false in general, already at `R = ℝ`:
`unboundedSDP` below (minimise `-x` over `x ⪰ 0`, `1 × 1`, no constraints) is primally
strictly feasible, unbounded below, and has no dual-feasible point, so it admits no
`StrongDualityPair` (`not_hasStrongDuality_unboundedSDP`).  The missing hypothesis is
(at least) dual feasibility; and with dual feasibility but no dual Slater point the primal
optimum may fail to be attained, so the honest sufficient condition proved here is
two-sided Slater (`hasStrongDuality_of_slater'`; no rank condition on the constraints). -/

section MathlibExtBridge
open QOU.MathlibExt.SDP

/-- **`HasStrongDuality` from two-sided Slater.** For a real SDP with symmetric cost and
constraints, a positive-definite feasible point `h`, and a positive-definite dual slack, the
class `HasStrongDuality sdp h` holds.  No linear independence of the constraints is assumed.
(Not an `instance`: its extra hypotheses are not classes.) -/
theorem hasStrongDuality_of_slater' (sdp : SDPPrimal n ℝ (Fin m)) (h : sdp.IsStrictlyFeasible)
    (hA : ∀ i, (sdp.constraint i).IsHermitian) (hC : sdp.cost.IsHermitian)
    (hdslater : ∃ ybar : Fin m → ℝ, (sdp.dualSlack ybar).PosDef) :
    HasStrongDuality sdp h := by
  obtain ⟨Xbar, hXbar, hXbarf⟩ := id h
  obtain ⟨Xs, ys, hXs, hXsf, hys, heq, -, -, -⟩ :=
    exists_optimal_pair' sdp.constraint sdp.rhs sdp.cost hA hC ⟨Xbar, hXbar, hXbarf⟩ hdslater
  refine ⟨⟨StrongDualityPair.mk Xs ys (And.intro hXs hXsf) hys ?_⟩⟩
  show traceInner sdp.cost Xs = ∑ i, ys i * sdp.rhs i
  rw [heq]
  exact Finset.sum_congr rfl fun i _ => mul_comm _ _

/-- **`HasStrongDuality` from two-sided Slater**, the form with linearly independent
constraints.  The hypothesis `hli` is not needed: this is `hasStrongDuality_of_slater'`, kept
for its existing signature. -/
theorem hasStrongDuality_of_slater (sdp : SDPPrimal n ℝ (Fin m)) (h : sdp.IsStrictlyFeasible)
    (hA : ∀ i, (sdp.constraint i).IsHermitian) (hC : sdp.cost.IsHermitian)
    (_hli : LinearIndependent ℝ sdp.constraint)
    (hdslater : ∃ ybar : Fin m → ℝ, (sdp.dualSlack ybar).PosDef) :
    HasStrongDuality sdp h :=
  hasStrongDuality_of_slater' sdp h hA hC hdslater

/-- Minimise `⟨-1, X⟩ = -x` over `1 × 1` PSD `X = (x)`, with no equality constraints. -/
def unboundedSDP : SDPPrimal 1 ℝ (Fin 0) where
  cost := -1
  constraint := fun i => i.elim0
  rhs := fun i => i.elim0

theorem unboundedSDP_strictlyFeasible : unboundedSDP.IsStrictlyFeasible :=
  ⟨1, PosDef.one, fun i => i.elim0⟩

/-- `unboundedSDP` is unbounded below. -/
theorem unboundedSDP_unbounded (t : ℝ) :
    ∃ Φ : Matrix (Fin 1) (Fin 1) ℝ, unboundedSDP.IsFeasible Φ ∧ unboundedSDP.objAt Φ < t := by
  refine ⟨(|t| + 1) • (1 : Matrix (Fin 1) (Fin 1) ℝ),
    ⟨PosSemidef.one.smul (by positivity), fun i => i.elim0⟩, ?_⟩
  simp only [SDPPrimal.objAt, unboundedSDP, neg_mul, one_mul, trace_neg, trace_smul,
    trace_one, Fintype.card_fin, Nat.cast_one, smul_eq_mul, mul_one]
  linarith [neg_abs_le t]

/-- **`HasStrongDuality` is false as stated**: primal strict feasibility alone does not
yield a strong-duality pair. -/
theorem not_hasStrongDuality_unboundedSDP :
    ¬ HasStrongDuality unboundedSDP unboundedSDP_strictlyFeasible := by
  intro H
  obtain ⟨p⟩ := H.pair
  have h := p.dual_feas.2 (fun _ => 1)
  simp [SDPPrimal.dualSlack, unboundedSDP] at h
  simp [dotProduct, Matrix.neg_mulVec, Matrix.one_mulVec] at h
  linarith

theorem not_forall_hasStrongDuality :
    ¬ ∀ (sdp : SDPPrimal 1 ℝ (Fin 0)) (h : sdp.IsStrictlyFeasible), HasStrongDuality sdp h :=
  fun H => not_hasStrongDuality_unboundedSDP (H _ _)

end MathlibExtBridge

end QOU.Mathlib.SDPStrongDuality
