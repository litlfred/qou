import QOU.SchurWeyl.JMProjector
import Mathlib.Topology.Instances.Matrix
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.SchurWeyl.JMProjectorContinuity — the Wedderburn idempotents vary continuously through `q = 1`

Gaps 2 and 3 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md` §5.1 (bean `qou-2vt5`),
in the form the rank-rigidity comparison consumes.

Let `x ↦ ρ x : H_{n+1}(q x) →ₐ[ℂ] M_m(ℂ)` be a family of representations over a parameter space
whose generator matrices `ρ x (σ_i)` are continuous on `S`. For a standard tableau `T` put

    projFamily ρ T x := jmProjIn (q x) (ρ x ∘ σ) (contentVec T),

the JM-Lagrange polynomial of `JMProjector` evaluated on the generator matrices. Then:

* `projFamily_eq_wedderburn` — at a generic `x` it is `ρ x ((heckeWedderburn (q x))⁻¹ E^λ_{TT})`;
* `continuousOn_projFamily` — **(gap 2)** it is continuous on `S` as soon as `q` is continuous and
  nonzero and the `q²`-integers `[d]_{q²}`, `|d| ≤ n`, are distinct on `S`; this holds at every
  positive real `q`, **including `q = 1`** (`sep_of_pos`, `qInt2_injective_ofReal`);
* `isIdempotentElem_projFamily` — **(gap 3)** it is idempotent at every point of `S`, including a
  non-generic base point such as `q = 1` (coupling `0`), provided the generic points are dense in
  `S` (`generic_of_pos` reduces this to density of `{q ≠ 1}` for positive real `q`);
* `projFamily_conj` — two families conjugate on the generators at a base point have conjugate
  projectors there (so equal ranks).

So the base point `κ = 0` (`q = 1`) needs no Wedderburn decomposition of `ℂ[S_n]` at all: only that
the two representations agree (up to conjugation) on the generators there. With
`IdempotentTraceRigidity.rank_const_of_isPreconnected` and `KohnoComparison.exists_conj_of_rank_eq`
(PR #7673) this gives conjugacy at every generic point of a preconnected `S` containing the base
point; the assembly is posted on #7673.
-/

namespace QOU.SchurWeyl

namespace JMProjector

open QOU.Mathlib (StandardYoungTableau)
open Hecke Topology

variable {X : Type*} [TopologicalSpace X] {S : Set X}

/-! ## Continuity of finite products of continuous families -/

theorem continuousOn_list_prod {M : Type*} [TopologicalSpace M] [Monoid M] [ContinuousMul M]
    {α : Type*} (l : List α) (F : α → X → M) (hF : ∀ a ∈ l, ContinuousOn (F a) S) :
    ContinuousOn (fun x => (l.map fun a => F a x).prod) S := by
  induction l with
  | nil => simpa using continuousOn_const
  | cons a l ih =>
      simp only [List.map_cons, List.prod_cons]
      exact (hF a (by simp)).mul (ih (fun b hb => hF b (by simp [hb])))

/-! ## Continuity in the parameter -/

section Cont

variable {q : X → ℂ} (hq : ContinuousOn q S) (hq0 : ∀ x ∈ S, q x ≠ 0)

include hq hq0 in
theorem continuousOn_qInt2 (c : ℤ) : ContinuousOn (fun x => qInt2 (q x) c) S := by
  unfold qInt2
  split_ifs with hc
  · exact continuousOn_finset_sum _ (fun j _ => hq.pow _)
  · refine (continuousOn_finset_sum _ (fun j _ => ?_)).neg
    exact ((hq.pow 2).inv₀ (fun x hx => pow_ne_zero 2 (hq0 x hx))).pow _

variable {m : Type*} [Fintype m] [DecidableEq m] {n : ℕ}
  {g : X → Fin n → Matrix m m ℂ} (hg : ∀ i, ContinuousOn (fun x => g x i) S)

include hq hq0 hg in
theorem continuousOn_jmAddIn : ∀ k, ContinuousOn (fun x => jmAddIn (q x) (g x) k) S
  | 0 => by simpa [jmAddIn] using continuousOn_const
  | k + 1 => by
      by_cases hk : k < n
      · simp only [jmAddIn_succ _ _ hk]
        exact (((hg _).mul (continuousOn_jmAddIn k)).mul (hg _)).add
          ((hq.inv₀ hq0).smul (hg _))
      · simp only [jmAddIn_succ_of_le _ _ (show n ≤ k by omega)]
        exact continuousOn_jmAddIn k

include hq hq0 hg in
/-- **The JM projector is continuous** wherever the `q²`-integers `[d]_{q²}`, `|d| ≤ n`, stay
pairwise distinct — in particular across `q = 1`. -/
theorem continuousOn_jmProjIn
    (hsep : ∀ x ∈ S, Set.InjOn (qInt2 (q x)) {d | d ∈ contentRange n}) (c : ℕ → ℤ)
    (hc : ∀ k ∈ List.range (n + 1), c k ∈ contentRange n) :
    ContinuousOn (fun x => jmProjIn (q x) (g x) c) S := by
  unfold jmProjIn jmFactorIn
  refine continuousOn_list_prod _ _ (fun k hk => ?_)
  refine continuousOn_list_prod _ _ (fun d hd => ?_)
  rw [List.mem_filter] at hd
  have hdc : d ≠ c k := by simpa using hd.2
  refine ContinuousOn.smul ?_ ?_
  · refine ((continuousOn_qInt2 hq hq0 _).sub (continuousOn_qInt2 hq hq0 _)).inv₀
      (fun x hx => sub_ne_zero.mpr (fun h => hdc (hsep x hx hd.1 (hc k hk) h.symm)))
  · refine (continuousOn_jmAddIn hq hq0 hg k).sub ?_
    simp only [Algebra.algebraMap_eq_smul_one]
    exact (continuousOn_qInt2 hq hq0 d).smul continuousOn_const

end Cont

/-! ## Positive real parameters, including `q = 1`, are admissible -/

theorem notRootOfUnity_ofReal {t : ℝ} (ht : 0 < t) (ht1 : t ≠ 1) :
    GenericParameter.NotRootOfUnity (t : ℂ) := by
  intro m hm h
  have h' : t ^ m = 1 := by exact_mod_cast h
  exact ht1 ((pow_eq_one_iff_of_nonneg ht.le (by omega)).mp h')

theorem qInt2_injective_ofReal {t : ℝ} (ht : 0 < t) :
    Function.Injective (qInt2 (t : ℂ)) := by
  by_cases ht1 : t = 1
  · subst ht1
    simpa using (qInt2_one_injective (K := ℂ))
  · exact qInt2_injective _ (by exact_mod_cast ht.ne') (notRootOfUnity_ofReal ht ht1)

/-! ## Idempotence passes to limit points -/

theorem isIdempotentElem_of_closure {R : Type*} [TopologicalSpace R] [T2Space R] [Semiring R]
    [ContinuousMul R] {e : X → R} (he : ContinuousOn e S) {G : Set X}
    (hG : ∀ x ∈ S ∩ G, IsIdempotentElem (e x)) (hdense : S ⊆ closure (S ∩ G)) :
    ∀ x ∈ S, IsIdempotentElem (e x) := by
  have h : Set.EqOn (fun x => e x * e x) e S :=
    Set.EqOn.of_subset_closure (fun x hx => hG x hx) (he.mul he) he Set.inter_subset_left hdense
  exact fun x hx => h hx


/-! ## Intertwiners pass through the projector -/

section Intertwine

variable {K : Type*} [Field K] (q : K) {A : Type*} [Ring A] [Algebra K A] {n : ℕ}

theorem intertwine_jmAddIn (g g' : Fin n → A) (U : A) (hU : ∀ i, U * g i = g' i * U) :
    ∀ k, U * jmAddIn q g k = jmAddIn q g' k * U
  | 0 => by simp [jmAddIn]
  | k + 1 => by
      by_cases hk : k < n
      · rw [jmAddIn_succ q g hk, jmAddIn_succ q g' hk, mul_add, add_mul, mul_smul_comm,
          smul_mul_assoc, hU]
        congr 1
        rw [← mul_assoc, ← mul_assoc, hU, mul_assoc, mul_assoc, mul_assoc,
          ← mul_assoc U, intertwine_jmAddIn g g' U hU k, mul_assoc, hU, ← mul_assoc,
          ← mul_assoc]
      · rw [jmAddIn_succ_of_le q g (by omega), jmAddIn_succ_of_le q g' (by omega),
          intertwine_jmAddIn g g' U hU k]

theorem intertwine_list_prod {α : Type*} (l : List α) (F F' : α → A) (U : A)
    (hF : ∀ a ∈ l, U * F a = F' a * U) :
    U * (l.map F).prod = (l.map F').prod * U := by
  induction l with
  | nil => simp
  | cons a l ih =>
      simp only [List.map_cons, List.prod_cons]
      rw [← mul_assoc, hF a (by simp), mul_assoc, ih (fun b hb => hF b (by simp [hb])),
        mul_assoc]

theorem intertwine_jmProjIn (g g' : Fin n → A) (U : A) (hU : ∀ i, U * g i = g' i * U)
    (c : ℕ → ℤ) : U * jmProjIn q g c = jmProjIn q g' c * U := by
  unfold jmProjIn jmFactorIn
  refine intertwine_list_prod _ _ _ U (fun k _ => ?_)
  refine intertwine_list_prod _ _ _ U (fun d _ => ?_)
  rw [mul_smul_comm, smul_mul_assoc, mul_sub, sub_mul, intertwine_jmAddIn q g g' U hU k,
    Algebra.commutes]

end Intertwine

/-! ## The interface for the rigidity comparison

A family of representations `ρ x : H_{n+1}(q x) →ₐ[ℂ] M_m(ℂ)` over a parameter space, whose
generator matrices `ρ x (σ_i)` are continuous on `S`. -/

section Family

variable {q : X → ℂ} {n : ℕ} {m : Type*} [Fintype m] [DecidableEq m]
  (ρ : ∀ x : X, Hecke ℂ (q x) (q x)⁻¹ n →ₐ[ℂ] Matrix m m ℂ) {lam' : Nat.Partition (n + 1)}

/-- The image under `ρ x` of the JM projector of `T`: a fixed polynomial in the generator matrices
`ρ x (σ_i)`, defined at every parameter, including where `q x = 1`. -/
noncomputable def projFamily (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam'))
    (x : X) : Matrix m m ℂ :=
  jmProjIn (q x) (fun i => ρ x (σ ℂ (q x) (q x)⁻¹ n i)) (contentVec T)

omit [TopologicalSpace X] in
theorem projFamily_eq_map (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam')) (x : X) :
    projFamily ρ T x = ρ x (jmProjIn (q x) (σ ℂ (q x) (q x)⁻¹ n) (contentVec T)) :=
  (map_jmProjIn (q x) (ρ x) _ _).symm

omit [TopologicalSpace X] in
/-- **(gap 2)** At a generic parameter the family *is* the representation evaluated on the
inverse Wedderburn matrix unit. -/
theorem projFamily_eq_wedderburn (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam'))
    (x : X) (hx0 : q x ≠ 0) (hgen : GenericParameter.NotRootOfUnity (q x)) :
    ρ x ((heckeWedderburn (q x) hx0 hgen n).symm (Pi.single lam' (Matrix.single T T 1)))
      = projFamily ρ T x := by
  rw [heckeWedderburn_symm_single, projFamily_eq_map]

/-- **(gap 2)** The family is continuous on `S` as soon as the generator matrices are, provided
`q` is continuous and nonvanishing on `S` and the `q²`-integers `[d]_{q²}`, `|d| ≤ n`, stay
distinct there. No genericity is needed: the set may contain `q = 1`. -/
theorem continuousOn_projFamily (hq : ContinuousOn q S) (hq0 : ∀ x ∈ S, q x ≠ 0)
    (hsep : ∀ x ∈ S, Set.InjOn (qInt2 (q x)) {d | d ∈ contentRange n})
    (hρ : ∀ i, ContinuousOn (fun x => ρ x (σ ℂ (q x) (q x)⁻¹ n i)) S)
    (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam')) :
    ContinuousOn (projFamily ρ T) S :=
  continuousOn_jmProjIn hq hq0 hρ hsep _ (fun k hk =>
    contentVec_mem (partitionShape_card_succ lam') T (by simpa using hk))

/-- **(gap 3)** The family is idempotent at every point of `S`, including non-generic base points
such as `q = 1`, provided the generic points are dense in `S`. -/
theorem isIdempotentElem_projFamily (hq : ContinuousOn q S) (hq0 : ∀ x ∈ S, q x ≠ 0)
    (hsep : ∀ x ∈ S, Set.InjOn (qInt2 (q x)) {d | d ∈ contentRange n})
    (hρ : ∀ i, ContinuousOn (fun x => ρ x (σ ℂ (q x) (q x)⁻¹ n i)) S)
    (hdense : S ⊆ closure (S ∩ {x | GenericParameter.NotRootOfUnity (q x)}))
    (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam')) :
    ∀ x ∈ S, IsIdempotentElem (projFamily ρ T x) := by
  refine isIdempotentElem_of_closure (continuousOn_projFamily ρ hq hq0 hsep hρ T)
    (fun x hx => ?_) hdense
  rw [← projFamily_eq_wedderburn ρ T x (hq0 x hx.1) hx.2]
  refine IsIdempotentElem.map ?_ (ρ x)
  refine IsIdempotentElem.map ?_ (heckeWedderburn (q x) (hq0 x hx.1) hx.2 n).symm
  unfold IsIdempotentElem
  rw [← Pi.single_mul, Matrix.single_mul_single_same, mul_one]

omit [TopologicalSpace X] in
/-- If two families agree up to conjugation at a base point `x₀`, so do their projector families
(the projector is a polynomial in the generators). -/
theorem projFamily_conj {ρ' : ∀ x : X, Hecke ℂ (q x) (q x)⁻¹ n →ₐ[ℂ] Matrix m m ℂ} {x₀ : X}
    (U : (Matrix m m ℂ)ˣ)
    (hU : ∀ i, (U : Matrix m m ℂ) * ρ x₀ (σ ℂ (q x₀) (q x₀)⁻¹ n i)
      = ρ' x₀ (σ ℂ (q x₀) (q x₀)⁻¹ n i) * U)
    (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam')) :
    (U : Matrix m m ℂ) * projFamily ρ T x₀ = projFamily ρ' T x₀ * U := by
  exact intertwine_jmProjIn (q x₀) _ _ _ hU _

omit [TopologicalSpace X] in
/-- Positive real parameters satisfy the separation hypothesis, `q = 1` included. -/
theorem sep_of_pos (hpos : ∀ x ∈ S, ∃ t : ℝ, 0 < t ∧ q x = t) :
    ∀ x ∈ S, Set.InjOn (qInt2 (q x)) {d | d ∈ contentRange n} := by
  intro x hx
  obtain ⟨t, ht, hqt⟩ := hpos x hx
  rw [hqt]
  exact (qInt2_injective_ofReal ht).injOn

omit [TopologicalSpace X] in
/-- On positive real parameters, every point with `q ≠ 1` is generic; so the density hypothesis
of `isIdempotentElem_projFamily` reduces to density of `{q ≠ 1}`. For a segment of KZ couplings
from `0` to the imaginary coupling `κ₀` (real `q ∈ [1, q₀]`) this is the density of the segment
minus its endpoint `κ = 0`. -/
theorem generic_of_pos (hpos : ∀ x ∈ S, ∃ t : ℝ, 0 < t ∧ q x = t) :
    S ∩ {x | q x ≠ 1} ⊆ S ∩ {x | GenericParameter.NotRootOfUnity (q x)} := by
  rintro x ⟨hx, hx1⟩
  obtain ⟨t, ht, hqt⟩ := hpos x hx
  refine ⟨hx, ?_⟩
  have hx1' : q x ≠ 1 := hx1
  show GenericParameter.NotRootOfUnity (q x)
  rw [hqt] at hx1' ⊢
  exact notRootOfUnity_ofReal ht (fun h => hx1' (by rw [h]; simp))

end Family

end JMProjector

end QOU.SchurWeyl
