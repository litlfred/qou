import HeckeTemperleyLieb.TemperleyLiebSpinChainTwo
import HeckeTemperleyLieb.TemperleyLiebMarkovNondegenerate
import Mathlib.LinearAlgebra.Trace
import HeckeTemperleyLieb.TLVacuumRowFromJonesWenzl

/-!
# A Markov trace on the Temperley–Lieb tower from the quantum spin chain

`TemperleyLiebMarkovNondegenerate` states its results for an abstract `MarkovTower δ ε`, and the
corpus had no instance of that structure. This file constructs one at every loop value
`δ = q + q⁻¹` with `q ≠ 0` and `δ ≠ 0`, in particular at a root of unity.

* `Eq q i`: the `U_q(sl₂)` spin-chain generator on sites `i, i+1` of `(K²)^{⊗(n+1)}`, the rank-one
  operator with matrix `[[q, −1], [−1, q⁻¹]]` on `span(|01⟩, |10⟩)`; `spinRepQ` is the resulting
  algebra map `TL_{n+1}(δ) → End((Fin (n+1) → Fin 2) → K)` (this generalises the `q = 1` map of
  `TemperleyLiebSpinChainTwo`).
* `trw`: the quantum trace `Σ_τ w(τ)·f(|τ⟩)(τ)` with weight `w(τ) = ∏ₜ g(τₜ)`, `g(0) = q`,
  `g(1) = q⁻¹`.
* `spinMarkovTower`: `τ_n(x) = δ^{−(n+1)} trw(ρ(x))` is a `MarkovTower δ δ⁻¹`. The Markov
  property is the partial trace of the last generator against `diag(q, q⁻¹)`, which is the
  identity.
* `vacuum_row_spin`: at `q = ζ` a primitive `2(k+2)`-th root of unity, this tower discharges the
  trace hypothesis of `TLVacuumRow.vacuum_row_eq_sMatrix`, so the vacuum row of the level-`k`
  `S`-matrix holds with no assumption on the trace.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] https://doi.org/10.1007/BF01389127
-/

namespace QOU.HeckeTemperleyLieb.TLSpinChainMarkov

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.MathlibExt.TemperleyLiebSpinChainTwo

variable {K : Type*} [Field K] {n : ℕ}

/-- The `q`-singlet coefficient: `a(0,1) = 1`, `a(1,0) = −q⁻¹`, `a(x,x) = 0`. -/
def aq (q : K) (x y : Fin 2) : K :=
  if x = 0 ∧ y = 1 then 1 else if x = 1 ∧ y = 0 then -q⁻¹ else 0

/-- The `q`-deformed generator `e_i`. -/
def Eq (q : K) (i : Fin n) : Module.End K (Spin n → K) where
  toFun v τ := aq q (τ i.castSucc) (τ i.succ) * (q * v (put τ i 0 1) - v (put τ i 1 0))
  map_add' v w := by funext τ; simp only [Pi.add_apply]; ring
  map_smul' c v := by funext τ; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem Eq_apply (q : K) (i : Fin n) (v : Spin n → K) (τ : Spin n) :
    Eq q i v τ = aq q (τ i.castSucc) (τ i.succ) * (q * v (put τ i 0 1) - v (put τ i 1 0)) := rfl

variable {q : K} (hq : q ≠ 0)
include hq

theorem Eq_sq (i : Fin n) :
    Eq q i * Eq q i = algebraMap K (Module.End K (Spin n → K)) (q + q⁻¹) * Eq q i := by
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, Eq_apply, put_castSucc, put_succ, put_put,
    Module.algebraMap_end_apply, Pi.smul_apply, smul_eq_mul]
  simp only [aq]
  norm_num
  all_goals (try split_ifs)
  all_goals (try field_simp)
  all_goals (try ring)

theorem Eq_adj_up {i j : Fin n} (hij : i.val + 1 = j.val) : Eq q i * Eq q j * Eq q i = Eq q i := by
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, Eq_apply]
  rw [put_i_eq hij τ 0 1, put_i_eq hij τ 1 0]
  simp only [put_i_put3 hij, put_j_put3 hij, put3_a (neq_ab hij) (neq_ac hij),
    put3_b (neq_bc hij), put3_c, ← succ_eq hij]
  generalize τ j.succ = z
  fin_cases z <;> simp only [aq] <;> norm_num
  all_goals (try split_ifs)
  all_goals (try field_simp)
  all_goals (try ring)

theorem Eq_adj_down {i j : Fin n} (hij : i.val + 1 = j.val) :
    Eq q j * Eq q i * Eq q j = Eq q j := by
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, Eq_apply]
  rw [put_j_eq hij τ 0 1, put_j_eq hij τ 1 0]
  simp only [put_i_put3 hij, put_j_put3 hij, put3_a (neq_ab hij) (neq_ac hij),
    put3_b (neq_bc hij), put3_c, ← succ_eq hij]
  generalize τ i.castSucc = z
  fin_cases z <;> simp only [aq] <;> norm_num
  all_goals (try split_ifs)
  all_goals (try field_simp)
  all_goals (try ring)

omit hq in
theorem Eq_comm {i j : Fin n} (hfar : i.val + 2 ≤ j.val ∨ j.val + 2 ≤ i.val) :
    Eq q i * Eq q j = Eq q j * Eq q i := by
  have hfar' : j.val + 2 ≤ i.val ∨ i.val + 2 ≤ j.val := hfar.symm
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, Eq_apply, put_jc hfar, put_js hfar, put_jc hfar',
    put_js hfar', put_comm hfar]
  ring

omit hq in
theorem adjFin_cases {i j : Fin n} (h : adjFin i j) : i.val + 1 = j.val ∨ j.val + 1 = i.val := h

variable (q) in
/-- **The `U_q(sl₂)` spin-chain representation** of `TL_{n+1}(δ)`, `δ = q + q⁻¹`. -/
noncomputable def spinRepQ {δ : K} (hδ : δ = q + q⁻¹) (n : ℕ) :
    TLFin K δ n →ₐ[K] Module.End K (Spin n → K) :=
  lift K δ adjFin (fun i => Eq q i) (fun i => by rw [hδ]; exact Eq_sq hq i)
    (fun i j h => by
      rcases adjFin_cases h with h | h
      · exact Eq_adj_up hq h
      · exact Eq_adj_down hq h)
    (fun i j h => by
      by_cases hij : i = j
      · subst hij; rfl
      · apply Eq_comm
        have h1 : i.val ≠ j.val := fun h' => hij (Fin.ext h')
        have h2 : ¬ (i.val + 1 = j.val ∨ j.val + 1 = i.val) := h
        omega)

@[simp] theorem spinRepQ_e {δ : K} (hδ : δ = q + q⁻¹) (i : Fin n) :
    spinRepQ q hq hδ n (e K δ adjFin i) = Eq q i :=
  lift_e K δ adjFin _ _ _ _ i

/-! ## The quantum weight -/

omit hq in
variable (q) in
/-- Site weight `g(0) = q`, `g(1) = q⁻¹`. -/
def g (x : Fin 2) : K := if x = 0 then q else q⁻¹

omit hq in
variable (q) in
/-- Configuration weight `w(τ) = ∏ₜ g(τₜ)`. -/
def wt (τ : Spin n) : K := ∏ t, g q (τ t)

omit hq in
theorem wt_update (τ : Spin n) (t : Fin (n + 1)) (x : Fin 2) :
    wt q (Function.update τ t x) * g q (τ t) = wt q τ * g q x := by
  unfold wt
  have hf : (fun s => g q (Function.update τ t x s)) =
      Function.update (fun s => g q (τ s)) t (g q x) := by
    funext s; by_cases h : s = t
    · subst h; simp
    · simp [Function.update_of_ne h]
  rw [hf, Finset.prod_update_of_mem (Finset.mem_univ t), Finset.sdiff_singleton_eq_erase,
    ← Finset.mul_prod_erase Finset.univ (fun s => g q (τ s)) (Finset.mem_univ t)]
  ring

omit hq in
theorem wt_put (τ : Spin n) (i : Fin n) (x y : Fin 2) :
    wt q (put τ i x y) * (g q (τ i.castSucc) * g q (τ i.succ)) = wt q τ * (g q x * g q y) := by
  have h1 := wt_update (q := q) (Function.update τ i.castSucc x) i.succ y
  have h2 := wt_update (q := q) τ i.castSucc x
  rw [Function.update_of_ne (castSucc_ne_succ i).symm] at h1
  unfold put
  linear_combination g q (τ i.castSucc) * h1 + g q y * h2

theorem g_mul_g_of_aq {a b : Fin 2} (h : aq q a b ≠ 0) : g q a * g q b = 1 := by
  fin_cases a <;> fin_cases b <;> simp [aq, g] at h ⊢ <;> field_simp

theorem g_zero_mul_g_one : g q 0 * g q 1 = 1 := by simp [g]; field_simp
theorem g_one_mul_g_zero : g q 1 * g q 0 = 1 := by simp [g]; field_simp

theorem wt_put_eq (τ : Spin n) (i : Fin n) (h : aq q (τ i.castSucc) (τ i.succ) ≠ 0) (x y : Fin 2)
    (hxy : g q x * g q y = 1) : wt q (put τ i x y) = wt q τ := by
  have := wt_put (q := q) τ i x y
  rw [g_mul_g_of_aq hq h, hxy, mul_one, mul_one] at this
  exact this

omit hq in
variable (q) in
/-- The diagonal weight operator `W`. -/
def Wop : Module.End K (Spin n → K) where
  toFun v τ := wt q τ * v τ
  map_add' v w := by funext τ; simp only [Pi.add_apply]; ring
  map_smul' c v := by funext τ; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem Wop_comm_Eq (i : Fin n) : Wop q * Eq q i = Eq q i * Wop q := by
  apply LinearMap.ext; intro v; funext τ
  simp only [Module.End.mul_apply, Eq_apply, Wop, LinearMap.coe_mk, AddHom.coe_mk]
  by_cases h : aq q (τ i.castSucc) (τ i.succ) = 0
  · rw [h]; ring
  · rw [wt_put_eq hq τ i h 0 1 (g_zero_mul_g_one hq), wt_put_eq hq τ i h 1 0 (g_one_mul_g_zero hq)]
    ring

theorem spinRepQ_comm_W {δ : K} (hδ : δ = q + q⁻¹) (x : TLFin K δ n) :
    Commute (Wop q) (spinRepQ q hq hδ n x) := by
  have hmem : spinRepQ q hq hδ n x ∈ Subalgebra.centralizer K {Wop q} := by
    have hx : x ∈ Algebra.adjoin K (Set.range (e K δ adjFin)) := mem_adjoin_e x
    have : (Algebra.adjoin K (Set.range (e K δ adjFin))).map (spinRepQ q hq hδ n) ≤
        Subalgebra.centralizer K {Wop q} := by
      rw [AlgHom.map_adjoin, Algebra.adjoin_le_iff]
      rintro _ ⟨_, ⟨i, rfl⟩, rfl⟩
      rw [SetLike.mem_coe, Subalgebra.mem_centralizer_iff]
      intro w hw
      rw [Set.mem_singleton_iff] at hw
      subst hw
      rw [spinRepQ_e]
      exact Wop_comm_Eq hq i
    exact this ⟨x, hx, rfl⟩
  rw [Subalgebra.mem_centralizer_iff] at hmem
  exact hmem _ (Set.mem_singleton _)

/-! ## The quantum trace -/

omit hq in
variable (q) in
/-- The quantum trace `trw f = Σ_τ w(τ)·f(|τ⟩)(τ)`. -/
def trw (n : ℕ) : Module.End K (Spin n → K) →ₗ[K] K where
  toFun f := ∑ τ, wt q τ * f (Pi.single τ 1) τ
  map_add' f h := by simp only [LinearMap.add_apply, Pi.add_apply, mul_add, Finset.sum_add_distrib]
  map_smul' c f := by
    simp only [LinearMap.smul_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply, Finset.mul_sum]
    exact Finset.sum_congr rfl (fun _ _ => by ring)

omit hq in
theorem trace_eq_sum (f : Module.End K (Spin n → K)) :
    LinearMap.trace K _ f = ∑ τ, f (Pi.single τ 1) τ := by
  rw [LinearMap.trace_eq_matrix_trace K (Pi.basisFun K (Spin n)), Matrix.trace]
  simp only [Matrix.diag, LinearMap.toMatrix_apply, Pi.basisFun_apply, Pi.basisFun_repr]

omit hq in
theorem trw_eq_trace (f : Module.End K (Spin n → K)) :
    trw q n f = LinearMap.trace K _ (Wop q * f) := by
  rw [trace_eq_sum]; rfl

theorem trw_comm {δ : K} (hδ : δ = q + q⁻¹) (x y : TLFin K δ n) :
    trw q n (spinRepQ q hq hδ n x * spinRepQ q hq hδ n y) =
      trw q n (spinRepQ q hq hδ n y * spinRepQ q hq hδ n x) := by
  rw [trw_eq_trace, trw_eq_trace, ← mul_assoc, LinearMap.trace_mul_comm,
    ← mul_assoc, ← (spinRepQ_comm_W hq hδ y).eq, mul_assoc]

/-! ## Adding a site -/

omit hq in
/-- The operator `f ⊗ id` on `n + 2` sites. -/
def extE (f : Module.End K (Spin n → K)) : Module.End K (Spin (n + 1) → K) where
  toFun v τ := f (fun σ => v (Fin.snoc σ (τ (Fin.last (n + 1))))) (Fin.init τ)
  map_add' v w := by
    funext τ; exact congrFun (map_add f (fun σ => v (Fin.snoc σ (τ (Fin.last (n + 1)))))
      (fun σ => w (Fin.snoc σ (τ (Fin.last (n + 1)))))) _
  map_smul' c v := by
    funext τ; exact congrFun (map_smul f c (fun σ => v (Fin.snoc σ (τ (Fin.last (n + 1)))))) _

omit hq in
theorem extE_apply (f : Module.End K (Spin n → K)) (v : Spin (n + 1) → K) (τ : Spin (n + 1)) :
    extE f v τ = f (fun σ => v (Fin.snoc σ (τ (Fin.last (n + 1))))) (Fin.init τ) := rfl

omit hq in
variable (n) in
/-- `f ↦ f ⊗ id` as an algebra map. -/
def extHom : Module.End K (Spin n → K) →ₐ[K] Module.End K (Spin (n + 1) → K) :=
  AlgHom.ofLinearMap
    { toFun := extE
      map_add' := fun f h => by
        apply LinearMap.ext; intro v; funext τ; simp [extE_apply]
      map_smul' := fun c f => by
        apply LinearMap.ext; intro v; funext τ; simp [extE_apply] }
    (by apply LinearMap.ext; intro v; funext τ; simp [extE_apply])
    (fun f h => by
      apply LinearMap.ext; intro v; funext τ
      simp only [LinearMap.coe_mk, AddHom.coe_mk, Module.End.mul_apply, extE_apply,
        Fin.init_snoc, Fin.snoc_last])

omit hq in
theorem snoc_put (τ : Spin (n + 1)) (i : Fin n) (x y : Fin 2) :
    (Fin.snoc (put (Fin.init τ) i x y) (τ (Fin.last (n + 1))) : Spin (n + 1)) =
      put τ i.castSucc x y := by
  funext t
  refine Fin.lastCases ?_ (fun s => ?_) t
  · simp only [Fin.snoc_last, put, Function.update_apply]
    split_ifs <;> simp_all [Fin.ext_iff] <;> omega
  · simp only [Fin.snoc_castSucc, put, Function.update_apply, Fin.init]
    split_ifs <;> simp_all [Fin.ext_iff] <;> omega

omit hq in
theorem Eq_castSucc (i : Fin n) : Eq q (Fin.castSucc i) = extHom n (Eq q i) := by
  apply LinearMap.ext; intro v; funext τ
  show _ = extE (Eq q i) v τ
  rw [extE_apply, Eq_apply, Eq_apply, snoc_put, snoc_put]
  simp only [Fin.init, Fin.succ_castSucc]

theorem spinRepQ_incl {δ : K} (hδ : δ = q + q⁻¹) (x : TLFin K δ n) :
    spinRepQ q hq hδ (n + 1) (incl δ n x) = extHom n (spinRepQ q hq hδ n x) := by
  have h : (spinRepQ q hq hδ (n + 1)).comp (incl δ n) = (extHom n).comp (spinRepQ q hq hδ n) :=
    hom_ext _ _ _ _ _ (fun i => by simp [Eq_castSucc])
  exact AlgHom.congr_fun h x

omit hq in
theorem sum_spin_succ (F : Spin (n + 1) → K) :
    ∑ τ, F τ = ∑ ρ : Spin n, ∑ b : Fin 2, F (Fin.snoc ρ b) := by
  rw [← (Fin.snocEquiv (fun _ => Fin 2)).sum_comp, Fintype.sum_prod_type, Finset.sum_comm]
  rfl

omit hq in
theorem wt_snoc (ρ : Spin n) (b : Fin 2) :
    wt q (Fin.snoc ρ b : Spin (n + 1)) = wt q ρ * g q b := by
  simp [wt, Fin.prod_univ_castSucc]

omit hq in
theorem single_snoc (ρ σ : Spin n) (b c : Fin 2) :
    (Pi.single (M := fun _ : Spin (n + 1) => K) (Fin.snoc ρ b) 1) (Fin.snoc σ c) =
      if σ = ρ ∧ c = b then 1 else 0 := by
  simp only [Pi.single_apply, Fin.snoc_inj]

theorem trw_ext (f : Module.End K (Spin n → K)) :
    trw q (n + 1) (extHom n f) = (q + q⁻¹) * trw q n f := by
  show ∑ τ, wt q τ * extE f (Pi.single τ 1) τ = _
  rw [sum_spin_succ]
  simp only [extE_apply, Fin.snoc_last, Fin.init_snoc, wt_snoc, single_snoc, and_true]
  have : ∀ ρ : Spin n, (fun σ : Spin n => if σ = ρ then (1 : K) else 0) = Pi.single ρ 1 := by
    intro ρ; funext σ; simp [Pi.single_apply]
  simp only [this, Fin.sum_univ_two]
  show _ = (q + q⁻¹) * ∑ τ, wt q τ * f (Pi.single τ 1) τ
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun ρ _ => ?_)
  simp only [g]; norm_num; ring

/-! ## The Markov property -/

omit hq in
variable (q) in
/-- The partial-trace coefficients of the last generator: `c(0,1) = q`, `c(1,0) = q⁻¹`. -/
def cm (x y : Fin 2) : K := if x = 0 ∧ y = 1 then q else if x = 1 ∧ y = 0 then q⁻¹ else 0

omit hq in
theorem put_snoc_last (σ : Spin n) (b x y : Fin 2) :
    put (Fin.snoc σ b : Spin (n + 1)) (Fin.last n) x y =
      Fin.snoc (Function.update σ (Fin.last n) x) y := by
  funext t
  refine Fin.lastCases ?_ (fun s => ?_) t
  · simp only [Fin.snoc_last, put, Function.update_apply, Fin.succ_last]
    split_ifs <;> simp_all [Fin.ext_iff]
  · have := s.isLt
    simp only [Fin.snoc_castSucc, put, Function.update_apply, Fin.succ_last]
    split_ifs <;> simp_all [Fin.ext_iff]
    all_goals omega

omit hq in
theorem fin_two_cases (s : Fin 2) : s = 0 ∨ s = 1 := by fin_cases s <;> simp

omit hq in
theorem markov_vec (ρ : Spin n) (b : Fin 2) :
    (fun σ : Spin n => Eq q (Fin.last n)
        (Pi.single (M := fun _ : Spin (n + 1) => K) (Fin.snoc ρ b) 1) (Fin.snoc σ b)) =
      cm q (ρ (Fin.last n)) b • Pi.single (M := fun _ : Spin n => K) ρ 1 := by
  funext σ
  rw [Eq_apply, put_snoc_last, put_snoc_last, single_snoc, single_snoc]
  simp only [Fin.snoc_castSucc, Fin.succ_last, Fin.snoc_last, Pi.smul_apply, Pi.single_apply,
    smul_eq_mul]
  have h0 : ∀ x : Fin 2, σ (Fin.last n) = x → Function.update σ (Fin.last n) x = σ :=
    fun x h => by rw [← h]; exact Function.update_eq_self _ _
  by_cases hσ : σ = ρ
  · subst hσ
    rcases fin_two_cases (σ (Fin.last n)) with hs | hs
    · have h1 : Function.update σ (Fin.last n) 1 ≠ σ := fun h => by
        have := congrFun h (Fin.last n); simp [hs] at this
      rw [h0 0 hs, hs]
      fin_cases b <;> simp [aq, cm, h1]
    · have h1 : Function.update σ (Fin.last n) 0 ≠ σ := fun h => by
        have := congrFun h (Fin.last n); simp [hs] at this
      rw [h0 1 hs, hs]
      fin_cases b <;> simp [aq, cm, h1]
  · rcases fin_two_cases (σ (Fin.last n)) with hs | hs
    · rw [h0 0 hs, hs]
      fin_cases b <;> simp [aq, hσ]
    · rw [h0 1 hs, hs]
      fin_cases b <;> simp [aq, hσ]

theorem trw_markov (f : Module.End K (Spin n → K)) :
    trw q (n + 1) (extHom n f * Eq q (Fin.last n)) = trw q n f := by
  show ∑ τ, wt q τ * extE f (Eq q (Fin.last n) (Pi.single τ 1)) τ =
    ∑ τ, wt q τ * f (Pi.single τ 1) τ
  rw [sum_spin_succ]
  simp only [extE_apply, Fin.snoc_last, Fin.init_snoc, wt_snoc]
  refine Finset.sum_congr rfl (fun ρ _ => ?_)
  rw [Fin.sum_univ_two, markov_vec, markov_vec, map_smul, map_smul]
  simp only [Pi.smul_apply, smul_eq_mul]
  rcases fin_two_cases (ρ (Fin.last n)) with hs | hs
  · rw [hs]; simp only [cm, g]; norm_num; field_simp
  · rw [hs]; simp only [cm, g]; norm_num; field_simp

/-! ## The tower -/

omit hq in
theorem trw_zero_one : trw q 0 1 = q + q⁻¹ := by
  show ∑ τ, wt q τ * (Pi.single (M := fun _ : Spin 0 => K) τ 1) τ = _
  rw [← Equiv.sum_comp (Equiv.funUnique (Fin 1) (Fin 2)).symm
    (fun τ : Spin 0 => wt q τ * Pi.single (M := fun _ : Spin 0 => K) τ 1 τ), Fin.sum_univ_two]
  simp [wt, g]

variable (q) in
/-- **A Markov trace on the Temperley–Lieb tower**, at `δ = q + q⁻¹ ≠ 0`: the normalised quantum
trace of the `U_q(sl₂)` spin chain. -/
noncomputable def spinMarkovTower {δ : K} (hδ : δ = q + q⁻¹) (hδ0 : δ ≠ 0) :
    MarkovTower δ δ⁻¹ where
  τ n := (δ⁻¹) ^ (n + 1) • ((trw q n).comp (spinRepQ q hq hδ n).toLinearMap)
  tr_one := by
    simp only [LinearMap.smul_apply, LinearMap.comp_apply, AlgHom.toLinearMap_apply, map_one,
      trw_zero_one, ← hδ, smul_eq_mul, zero_add, pow_one]
    exact inv_mul_cancel₀ hδ0
  tr_incl n x := by
    simp only [LinearMap.smul_apply, LinearMap.comp_apply, AlgHom.toLinearMap_apply, smul_eq_mul,
      spinRepQ_incl hq hδ, trw_ext hq, ← hδ]
    rw [pow_succ, mul_assoc, ← mul_assoc δ⁻¹, inv_mul_cancel₀ hδ0, one_mul]
  tr_comm n x y := by
    simp only [LinearMap.smul_apply, LinearMap.comp_apply, AlgHom.toLinearMap_apply, smul_eq_mul,
      map_mul, trw_comm hq hδ]
  tr_markov n x := by
    simp only [LinearMap.smul_apply, LinearMap.comp_apply, AlgHom.toLinearMap_apply, smul_eq_mul,
      map_mul, spinRepQ_incl hq hδ, spinRepQ_e, trw_markov hq]
    ring

omit hq

/-! ## The vacuum row, unconditionally -/

open QOU.HeckeTemperleyLieb.TLRootOfUnity QOU.HeckeTemperleyLieb.TLVacuumRow in
/-- **The vacuum row of the level-`k` `S`-matrix, with no hypothesis on the trace**: the
spin-chain Markov trace at `q = ζ` satisfies the hypothesis of `vacuum_row_eq_sMatrix`, so the
unnormalised trace of each Jones–Wenzl projector on `n + 1 ≤ k` strands is `S_{0,n+1}`. -/
theorem vacuum_row_spin {ζ : Kˣ} (k : ℕ) (hk : 1 ≤ k) (hζ : IsPrimitiveRoot ζ (2 * (k + 2)))
    (n : ℕ) (hn : n + 1 ≤ k) :
    ∃ T : MarkovTower ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) ((ζ : K) + ((ζ⁻¹ : Kˣ) : K))⁻¹,
      ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) ^ (n + 1) * T.τ n (jw ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) n) =
        sMatrix ζ k 0 ⟨n + 1, by omega⟩ := by
  have hδ0 : (ζ : K) + ((ζ⁻¹ : Kˣ) : K) ≠ 0 := by
    have h := qInt_ne_zero (K := K) k hζ (m := 2) (by omega) (by omega)
    rw [← qint_eq_qInt] at h
    simpa [qint] using h
  have hδ : (ζ : K) + ((ζ⁻¹ : Kˣ) : K) = (ζ : K) + (ζ : K)⁻¹ := by rw [Units.val_inv_eq_inv_val]
  refine ⟨spinMarkovTower (ζ : K) ζ.ne_zero hδ hδ0, ?_⟩
  exact vacuum_row_eq_sMatrix k hζ _ (mul_inv_cancel₀ hδ0) n hn

end QOU.HeckeTemperleyLieb.TLSpinChainMarkov
