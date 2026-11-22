import QOU.FormalGroups.FormalGroupLaw

/-!
# The distribution algebra `Dist(G)` of a formal group law

A distribution on the formal coordinates `σ` is a finitely supported family of coefficients
`μ : (σ →₀ ℕ) →₀ R`, paired with power series by `⟨μ, f⟩ = Σ_d μ_d · coeff_d f`.

* `pullback`: the transpose of a substitution `f ↦ f(a)`, with `pair_pullback` and
  functoriality `pullback_pullback`.
* `tensor`: `μ ⊠ ν` in disjoint variables, with `pair_tensor_embed_mul`
  (`⟨μ ⊠ ν, P(X) Q(Y)⟩ = ⟨μ, P⟩⟨ν, Q⟩`) and the compatibility `pair_tensor_pullback`.
* `conv`: convolution `⟨μ * ν, f⟩ = ⟨μ ⊠ ν, f(F(X, Y))⟩` for a formal group law `G`.
  `conv_assoc` follows from `G.assoc`, and `one_conv`, `conv_one` from the unit laws, so
  `Dist(G)` is a unital associative algebra. Everything is sorry-free and over a general
  commutative ring.
-/

namespace QOU.FormalGroups
open MvPowerSeries
noncomputable section

variable {R : Type*} [CommRing R]

variable (R) in
/-- Distributions on the formal coordinates `σ`: finitely supported coefficient families,
acting on `R⟦σ⟧` by `⟨μ, f⟩ = Σ_d μ_d · coeff_d f`. `δ_d` is dual to the monomial `X^d`. -/
abbrev Dist (σ : Type*) := (σ →₀ ℕ) →₀ R

/-- The pairing `⟨μ, f⟩ = Σ_d μ_d · coeff_d f`. -/
def pair {σ : Type*} (μ : Dist R σ) (f : MvPowerSeries σ R) : R :=
  μ.sum fun d c => c * coeff d f

section Pair
variable {σ : Type*}

@[simp] lemma pair_single (d : σ →₀ ℕ) (c : R) (f : MvPowerSeries σ R) :
    pair (Finsupp.single d c) f = c * coeff d f := by
  simp [pair]

lemma pair_add (μ ν : Dist R σ) (f : MvPowerSeries σ R) :
    pair (μ + ν) f = pair μ f + pair ν f :=
  Finsupp.sum_add_index' (fun _ => zero_mul _) (fun _ _ _ => add_mul _ _ _)

lemma pair_smul (r : R) (μ : Dist R σ) (f : MvPowerSeries σ R) :
    pair (r • μ) f = r * pair μ f := by
  classical
  simp only [pair, Finsupp.sum, Finset.mul_sum]
  rw [Finset.sum_subset Finsupp.support_smul]
  · exact Finset.sum_congr rfl fun d _ => by simp [mul_assoc]
  · intro d _ hd; simp only [Finsupp.mem_support_iff, not_not] at hd; simp [hd]

lemma pair_zero (f : MvPowerSeries σ R) : pair (0 : Dist R σ) f = 0 := by simp [pair]

lemma pair_monomial (μ : Dist R σ) (d : σ →₀ ℕ) : pair μ (monomial d 1) = μ d := by
  classical
  simp only [pair, coeff_monomial, mul_ite, mul_one, mul_zero]
  rw [Finsupp.sum_ite_eq']; split_ifs with h
  · rfl
  · simp only [Finsupp.mem_support_iff, not_not] at h; exact h.symm

/-- Distributions are determined by their pairings. -/
theorem ext_pair {μ ν : Dist R σ} (h : ∀ f, pair μ f = pair ν f) : μ = ν :=
  Finsupp.ext fun d => by simpa [pair_monomial] using h (monomial d 1)

end Pair

section Pullback
variable {σ τ : Type*} {a : σ → MvPowerSeries τ R}

/-- For each `e`, only finitely many `d` have `coeff_e (a^d) ≠ 0` (substitute the series all
of whose coefficients are `1`). -/
lemma finite_coeff_prod (ha : HasSubst a) (e : τ →₀ ℕ) :
    (Function.support fun d : σ →₀ ℕ => coeff e (d.prod fun s n => a s ^ n)).Finite := by
  refine (coeff_subst_finite ha (fun _ => (1 : R)) e).subset fun d hd => ?_
  simp only [Function.mem_support] at hd ⊢
  change (1 : R) • _ ≠ 0
  rwa [one_smul]

/-- The pullback of `δ_e` along the substitution `f ↦ f(a)`: `d ↦ coeff_e (a^d)`. -/
def pullDelta (ha : HasSubst a) (e : τ →₀ ℕ) : Dist R σ :=
  Finsupp.ofSupportFinite _ (finite_coeff_prod ha e)

lemma pullDelta_apply (ha : HasSubst a) (e : τ →₀ ℕ) (d : σ →₀ ℕ) :
    pullDelta ha e d = coeff e (d.prod fun s n => a s ^ n) := rfl

lemma pair_pullDelta (ha : HasSubst a) (e : τ →₀ ℕ) (f : MvPowerSeries σ R) :
    pair (pullDelta ha e) f = coeff e (subst a f) := by
  classical
  rw [coeff_subst ha, finsum_eq_sum_of_support_subset (s := (pullDelta ha e).support)]
  · simp only [pair, Finsupp.sum, pullDelta_apply, smul_eq_mul, mul_comm]
  · intro d hd
    simp only [Function.mem_support, smul_eq_mul] at hd
    rw [Finset.mem_coe, Finsupp.mem_support_iff, pullDelta_apply]
    exact right_ne_zero_of_mul hd

/-- The pullback `a^* μ` of a distribution along `f ↦ f(a)`. -/
def pullback (ha : HasSubst a) (μ : Dist R τ) : Dist R σ :=
  μ.sum fun e c => c • pullDelta ha e

/-- **Defining property.** `⟨a^* μ, f⟩ = ⟨μ, f(a)⟩`. -/
theorem pair_pullback (ha : HasSubst a) (μ : Dist R τ) (f : MvPowerSeries σ R) :
    pair (pullback ha μ) f = pair μ (subst a f) := by
  classical
  induction μ using Finsupp.induction_linear with
  | zero => simp [pullback, pair_zero]
  | add μ ν hμ hν =>
    simp only [pullback] at hμ hν ⊢
    rw [Finsupp.sum_add_index' (h := fun e c => c • pullDelta ha e) (fun _ => zero_smul _ _)
      (fun _ _ _ => add_smul _ _ _), pair_add, hμ, hν, pair_add]
  | single e c =>
    simp only [pullback]
    rw [Finsupp.sum_single_index (h := fun e c => c • pullDelta ha e) (zero_smul _ _), pair_smul,
      pair_pullDelta, pair_single]

/-- **Functoriality.** Pulling back along `a` then `b` is pulling back along `b(a)`. -/
theorem pullback_pullback {υ : Type*} {b : υ → MvPowerSeries σ R} (ha : HasSubst a)
    (hb : HasSubst b) (μ : Dist R τ) :
    pullback hb (pullback ha μ) = pullback (hb.comp ha) μ := by
  refine ext_pair fun f => ?_
  rw [pair_pullback, pair_pullback, pair_pullback, subst_comp_subst_apply hb ha]
  simp only [substAlgHom_apply]

end Pullback

section Embed
variable {σ τ : Type*} [Finite σ]

/-- Renaming variables along `e : σ → τ`: `P ↦ P(X ∘ e)`. -/
def embed (e : σ → τ) (P : MvPowerSeries σ R) : MvPowerSeries τ R :=
  subst (fun s => (X (e s) : MvPowerSeries τ R)) P

lemma hasSubst_X_comp (e : σ → τ) : HasSubst (fun s => (X (e s) : MvPowerSeries τ R)) :=
  hasSubst_of_constantCoeff_zero fun s => by simp

omit [Finite σ] in
lemma prod_X_pow (e : σ → τ) (c : σ →₀ ℕ) :
    (c.prod fun s n => (X (e s) : MvPowerSeries τ R) ^ n) =
      monomial (Finsupp.mapDomain e c) 1 := by
  classical
  induction c using Finsupp.induction_linear with
  | zero => simp [monomial_zero_one]
  | add c d hc hd =>
    rw [Finsupp.prod_add_index' (fun _ => pow_zero _) (fun _ _ _ => pow_add _ _ _), hc, hd,
      Finsupp.mapDomain_add, monomial_mul_monomial, mul_one]
  | single s n =>
    rw [Finsupp.prod_single_index (h := fun s n => (X (e s) : MvPowerSeries τ R) ^ n) (pow_zero _),
      X_pow_eq, Finsupp.mapDomain_single]

lemma coeff_embed (e : σ → τ) (P : MvPowerSeries σ R) (u : τ →₀ ℕ) :
    coeff u (embed e P) = finsum fun c : σ →₀ ℕ =>
      coeff c P • coeff u (monomial (Finsupp.mapDomain e c) (1 : R)) := by
  rw [embed, coeff_subst (hasSubst_X_comp e)]
  simp only [prod_X_pow]

lemma coeff_embed_mapDomain {e : σ → τ} (he : Function.Injective e) (P : MvPowerSeries σ R)
    (d : σ →₀ ℕ) : coeff (Finsupp.mapDomain e d) (embed e P) = coeff d P := by
  classical
  rw [coeff_embed, finsum_eq_single _ d]
  · simp
  · intro c hc
    rw [coeff_monomial, if_neg, smul_zero]
    exact fun h => hc ((Finsupp.mapDomain_injective he) h).symm

lemma coeff_embed_eq_zero (e : σ → τ) (P : MvPowerSeries σ R) {u : τ →₀ ℕ}
    (hu : ∀ d, Finsupp.mapDomain e d ≠ u) : coeff u (embed e P) = 0 := by
  classical
  rw [coeff_embed]
  exact finsum_eq_zero_of_forall_eq_zero fun c => by
    rw [coeff_monomial, if_neg (hu c).symm, smul_zero]

end Embed


section Tensor
variable {τ₁ τ₂ T : Type*} [Finite τ₁] [Finite τ₂] {e₁ : τ₁ → T} {e₂ : τ₂ → T}

omit [Finite τ₁] [Finite τ₂] in
/-- Disjoint injective embeddings give a unique decomposition of exponents. -/
lemma mapDomain_add_inj (he₁ : Function.Injective e₁) (he₂ : Function.Injective e₂)
    (hd : ∀ x y, e₁ x ≠ e₂ y) {a a' : τ₁ →₀ ℕ} {b b' : τ₂ →₀ ℕ}
    (h : Finsupp.mapDomain e₁ a + Finsupp.mapDomain e₂ b =
      Finsupp.mapDomain e₁ a' + Finsupp.mapDomain e₂ b') : a = a' ∧ b = b' := by
  have n₂ : ∀ (c : τ₂ →₀ ℕ) x, Finsupp.mapDomain e₂ c (e₁ x) = 0 := fun c x =>
    Finsupp.mapDomain_notin_range _ _ (by rintro ⟨y, hy⟩; exact hd x y hy.symm)
  have n₁ : ∀ (c : τ₁ →₀ ℕ) y, Finsupp.mapDomain e₁ c (e₂ y) = 0 := fun c y =>
    Finsupp.mapDomain_notin_range _ _ (by rintro ⟨x, hx⟩; exact hd x y hx)
  constructor
  · ext x; have := congrArg (fun f => f (e₁ x)) h
    simpa [Finsupp.mapDomain_apply he₁, n₂] using this
  · ext y; have := congrArg (fun f => f (e₂ y)) h
    simpa [Finsupp.mapDomain_apply he₂, n₁] using this

lemma exists_of_coeff_embed_ne_zero (e : τ₁ → T) {P : MvPowerSeries τ₁ R} {u : T →₀ ℕ}
    (h : coeff u (embed e P) ≠ 0) : ∃ d, Finsupp.mapDomain e d = u := by
  by_contra hc; push_neg at hc; exact h (coeff_embed_eq_zero e P hc)

/-- Coefficients of a product of series in disjoint variables. -/
lemma coeff_embed_mul_embed (he₁ : Function.Injective e₁) (he₂ : Function.Injective e₂)
    (hd : ∀ x y, e₁ x ≠ e₂ y) (P : MvPowerSeries τ₁ R) (Q : MvPowerSeries τ₂ R)
    (d₁ : τ₁ →₀ ℕ) (d₂ : τ₂ →₀ ℕ) :
    coeff (Finsupp.mapDomain e₁ d₁ + Finsupp.mapDomain e₂ d₂) (embed e₁ P * embed e₂ Q) =
      coeff d₁ P * coeff d₂ Q := by
  classical
  rw [coeff_mul, Finset.sum_eq_single (Finsupp.mapDomain e₁ d₁, Finsupp.mapDomain e₂ d₂)]
  · rw [coeff_embed_mapDomain he₁, coeff_embed_mapDomain he₂]
  · rintro ⟨u, v⟩ huv hne
    by_contra h0
    obtain ⟨a, ha⟩ := exists_of_coeff_embed_ne_zero e₁ (left_ne_zero_of_mul h0)
    obtain ⟨b, hb⟩ := exists_of_coeff_embed_ne_zero e₂ (right_ne_zero_of_mul h0)
    rw [Finset.mem_antidiagonal] at huv
    have huv' : Finsupp.mapDomain e₁ a + Finsupp.mapDomain e₂ b =
        Finsupp.mapDomain e₁ d₁ + Finsupp.mapDomain e₂ d₂ := by
      rw [ha, hb]; exact huv
    obtain ⟨h1, h2⟩ := mapDomain_add_inj he₁ he₂ hd huv'
    apply hne
    simp only at ha hb
    rw [← ha, ← hb, h1, h2]
  · intro h; exact absurd (Finset.mem_antidiagonal.mpr (by rfl)) h

lemma embed_monomial (e : τ₁ → T) (d : τ₁ →₀ ℕ) :
    embed e (monomial d (1 : R)) = monomial (Finsupp.mapDomain e d) 1 := by
  rw [embed, subst_monomial (hasSubst_X_comp e), prod_X_pow]
  simp

/-- The pairing is additive in the distribution. -/
def pairHom {σ : Type*} (f : MvPowerSeries σ R) : Dist R σ →+ R where
  toFun μ := pair μ f
  map_zero' := pair_zero f
  map_add' μ ν := pair_add μ ν f

variable (e₁ e₂) in
/-- The tensor product `μ ⊠ ν` of distributions in disjoint variables: `δ_m ⊠ δ_n =
δ_{e₁ m + e₂ n}`. -/
def tensor (μ : Dist R τ₁) (ν : Dist R τ₂) : Dist R T :=
  μ.sum fun m a => ν.sum fun n b =>
    Finsupp.single (Finsupp.mapDomain e₁ m + Finsupp.mapDomain e₂ n) (a * b)

omit [Finite τ₁] [Finite τ₂] in
lemma pair_tensor (μ : Dist R τ₁) (ν : Dist R τ₂) (g : MvPowerSeries T R) :
    pair (tensor e₁ e₂ μ ν) g = μ.sum fun m a => ν.sum fun n b =>
      a * b * coeff (Finsupp.mapDomain e₁ m + Finsupp.mapDomain e₂ n) g := by
  change pairHom g _ = _
  simp only [tensor, map_finsuppSum]
  refine Finsupp.sum_congr fun m _ => Finsupp.sum_congr fun n _ => ?_
  change pair _ g = _
  rw [pair_single]

/-- **Tensor and products.** `⟨μ ⊠ ν, P(X_{e₁}) · Q(X_{e₂})⟩ = ⟨μ, P⟩ ⟨ν, Q⟩`. -/
lemma pair_tensor_embed_mul (he₁ : Function.Injective e₁) (he₂ : Function.Injective e₂)
    (hd : ∀ x y, e₁ x ≠ e₂ y) (μ : Dist R τ₁) (ν : Dist R τ₂) (P : MvPowerSeries τ₁ R)
    (Q : MvPowerSeries τ₂ R) :
    pair (tensor e₁ e₂ μ ν) (embed e₁ P * embed e₂ Q) = pair μ P * pair ν Q := by
  rw [pair_tensor, pair, pair, Finsupp.sum_mul]
  refine Finsupp.sum_congr fun m _ => ?_
  rw [Finsupp.mul_sum]
  refine Finsupp.sum_congr fun n _ => ?_
  rw [coeff_embed_mul_embed he₁ he₂ hd]; ring

lemma tensor_apply (he₁ : Function.Injective e₁) (he₂ : Function.Injective e₂)
    (hd : ∀ x y, e₁ x ≠ e₂ y) (μ : Dist R τ₁) (ν : Dist R τ₂) (d₁ : τ₁ →₀ ℕ) (d₂ : τ₂ →₀ ℕ) :
    tensor e₁ e₂ μ ν (Finsupp.mapDomain e₁ d₁ + Finsupp.mapDomain e₂ d₂) = μ d₁ * ν d₂ := by
  have hm : (monomial (Finsupp.mapDomain e₁ d₁ + Finsupp.mapDomain e₂ d₂) (1 : R)) =
      embed e₁ (monomial d₁ 1) * embed e₂ (monomial d₂ 1) := by
    rw [embed_monomial, embed_monomial, monomial_mul_monomial, mul_one]
  rw [← pair_monomial, hm, pair_tensor_embed_mul he₁ he₂ hd, pair_monomial, pair_monomial]

end Tensor

section TensorLinear
variable {τ₁ τ₂ T : Type*} (e₁ : τ₁ → T) (e₂ : τ₂ → T)

@[simp] lemma tensor_zero_left (ρ : Dist R τ₂) : tensor e₁ e₂ (0 : Dist R τ₁) ρ = 0 := by
  simp [tensor]

@[simp] lemma tensor_zero_right (μ : Dist R τ₁) : tensor e₁ e₂ μ (0 : Dist R τ₂) = 0 := by
  simp [tensor]

lemma tensor_single_single (m : τ₁ →₀ ℕ) (n : τ₂ →₀ ℕ) (a b : R) :
    tensor e₁ e₂ (Finsupp.single m a) (Finsupp.single n b) =
      Finsupp.single (Finsupp.mapDomain e₁ m + Finsupp.mapDomain e₂ n) (a * b) := by
  simp [tensor]

lemma tensor_add_left (μ μ' : Dist R τ₁) (ρ : Dist R τ₂) :
    tensor e₁ e₂ (μ + μ') ρ = tensor e₁ e₂ μ ρ + tensor e₁ e₂ μ' ρ := by
  unfold tensor
  refine Finsupp.sum_add_index' (fun m => by simp) fun m a a' => ?_
  rw [← Finsupp.sum_add]
  exact Finsupp.sum_congr fun n _ => by rw [add_mul, Finsupp.single_add]

lemma tensor_add_right (μ : Dist R τ₁) (ρ ρ' : Dist R τ₂) :
    tensor e₁ e₂ μ (ρ + ρ') = tensor e₁ e₂ μ ρ + tensor e₁ e₂ μ ρ' := by
  unfold tensor
  rw [← Finsupp.sum_add]
  refine Finsupp.sum_congr fun m _ => ?_
  exact Finsupp.sum_add_index' (fun n => by simp) fun n b b' => by
    rw [mul_add, Finsupp.single_add]

lemma tensor_smul_left (c : R) (μ : Dist R τ₁) (ρ : Dist R τ₂) :
    tensor e₁ e₂ (c • μ) ρ = c • tensor e₁ e₂ μ ρ := by
  unfold tensor
  rw [Finsupp.sum_smul_index (fun m => by simp), Finsupp.smul_sum]
  refine Finsupp.sum_congr fun m _ => ?_
  rw [Finsupp.smul_sum]
  exact Finsupp.sum_congr fun n _ => by rw [Finsupp.smul_single, smul_eq_mul, mul_assoc]

lemma tensor_smul_right (c : R) (μ : Dist R τ₁) (ρ : Dist R τ₂) :
    tensor e₁ e₂ μ (c • ρ) = c • tensor e₁ e₂ μ ρ := by
  unfold tensor
  rw [Finsupp.smul_sum]
  refine Finsupp.sum_congr fun m _ => ?_
  rw [Finsupp.sum_smul_index (fun n => by simp), Finsupp.smul_sum]
  exact Finsupp.sum_congr fun n _ => by
    rw [Finsupp.smul_single, smul_eq_mul]; ring_nf

end TensorLinear

section PullbackLinear
variable {σ τ : Type*} {a : σ → MvPowerSeries τ R} (ha : HasSubst a)

@[simp] lemma pullback_zero : pullback ha (0 : Dist R τ) = 0 := by simp [pullback]

lemma pullback_add (μ ν : Dist R τ) : pullback ha (μ + ν) = pullback ha μ + pullback ha ν :=
  Finsupp.sum_add_index' (fun _ => zero_smul _ _) fun _ _ _ => add_smul _ _ _

lemma pullback_single (e : τ →₀ ℕ) (c : R) :
    pullback ha (Finsupp.single e c) = c • pullDelta ha e :=
  Finsupp.sum_single_index (h := fun e c => c • pullDelta ha e) (zero_smul _ _)

end PullbackLinear

section TensorPullback
variable {σ τ κ T T' : Type*} [Finite σ] [Finite τ] [Finite κ]
  {a : σ → MvPowerSeries τ R} (ha : HasSubst a)
  {i₁ : σ → T} {i₂ : κ → T} {j₁ : τ → T'} {j₂ : κ → T'}
  {b : T → MvPowerSeries T' R} (hb : HasSubst b)
  (hb₁ : ∀ s, b (i₁ s) = embed j₁ (a s)) (hb₂ : ∀ k, b (i₂ k) = X (j₂ k))

/-- `embed` as an algebra map. -/
lemma embed_eq_substAlgHom {σ τ : Type*} [Finite σ] (e : σ → τ) (P : MvPowerSeries σ R) :
    embed e P = substAlgHom (R := R) (hasSubst_X_comp e) P := by
  rw [substAlgHom_apply]; rfl

omit [Finite σ] in
include hb₁ hb₂ in
lemma prod_b_decomp (d : σ →₀ ℕ) (n : κ →₀ ℕ) :
    ((Finsupp.mapDomain i₁ d + Finsupp.mapDomain i₂ n).prod fun t k => b t ^ k) =
      embed j₁ (d.prod fun s k => a s ^ k) * embed j₂ (monomial n (1 : R)) := by
  classical
  rw [Finsupp.prod_add_index' (fun _ => pow_zero _) (fun _ _ _ => pow_add _ _ _),
    Finsupp.prod_mapDomain_index (fun _ => pow_zero _) (fun _ _ _ => pow_add _ _ _),
    Finsupp.prod_mapDomain_index (fun _ => pow_zero _) (fun _ _ _ => pow_add _ _ _),
    embed_monomial, ← prod_X_pow]
  congr 1
  · rw [embed_eq_substAlgHom, map_finsuppProd]
    simp only [map_pow, hb₁, embed_eq_substAlgHom]
  · simp only [hb₂]

omit [Finite σ] [Finite κ] in
lemma exists_decomp (hcov : ∀ t, (∃ s, i₁ s = t) ∨ (∃ k, i₂ k = t)) (D : T →₀ ℕ) :
    ∃ d n, Finsupp.mapDomain i₁ d + Finsupp.mapDomain i₂ n = D := by
  induction D using Finsupp.induction_linear with
  | zero => exact ⟨0, 0, by simp⟩
  | add D D' h h' =>
    obtain ⟨d, n, rfl⟩ := h; obtain ⟨d', n', rfl⟩ := h'
    exact ⟨d + d', n + n', by simp only [Finsupp.mapDomain_add]; abel⟩
  | single t m =>
    rcases hcov t with ⟨s, rfl⟩ | ⟨k, rfl⟩
    · exact ⟨Finsupp.single s m, 0, by simp [Finsupp.mapDomain_single]⟩
    · exact ⟨0, Finsupp.single k m, by simp [Finsupp.mapDomain_single]⟩

variable (hi₁ : Function.Injective i₁) (hi₂ : Function.Injective i₂) (hid : ∀ x y, i₁ x ≠ i₂ y)
  (hcov : ∀ t, (∃ s, i₁ s = t) ∨ (∃ k, i₂ k = t))
  (hj₁ : Function.Injective j₁) (hj₂ : Function.Injective j₂) (hjd : ∀ x y, j₁ x ≠ j₂ y)

include hb hb₁ hb₂ hi₁ hi₂ hid hcov hj₁ hj₂ hjd in
lemma pair_tensor_pullDelta_single (e : τ →₀ ℕ) (n : κ →₀ ℕ) (g : MvPowerSeries T R) :
    pair (tensor i₁ i₂ (pullDelta ha e) (Finsupp.single n 1)) g =
      coeff (Finsupp.mapDomain j₁ e + Finsupp.mapDomain j₂ n) (subst b g) := by
  classical
  have key : ∀ (d : σ →₀ ℕ) (n' : κ →₀ ℕ),
      coeff (Finsupp.mapDomain j₁ e + Finsupp.mapDomain j₂ n)
        ((Finsupp.mapDomain i₁ d + Finsupp.mapDomain i₂ n').prod fun t k => b t ^ k) =
      pullDelta ha e d * coeff n (monomial n' (1 : R)) := by
    intro d n'
    rw [prod_b_decomp hb₁ hb₂, coeff_embed_mul_embed hj₁ hj₂ hjd, pullDelta_apply]
  rw [pair_tensor, coeff_subst hb,
    finsum_eq_sum_of_support_subset (s := (pullDelta ha e).support.image
      fun d => Finsupp.mapDomain i₁ d + Finsupp.mapDomain i₂ n)]
  · rw [Finset.sum_image fun d _ d' _ h => (mapDomain_add_inj hi₁ hi₂ hid h).1]
    refine Finset.sum_congr rfl fun d _ => ?_
    dsimp only
    rw [Finsupp.sum_single_index (by simp), key, coeff_monomial, if_pos rfl, smul_eq_mul]
    ring
  · intro D hD
    obtain ⟨d, n', rfl⟩ := exists_decomp hcov D
    simp only [Function.mem_support, smul_eq_mul, key] at hD
    have h1 := right_ne_zero_of_mul hD
    have h2 := left_ne_zero_of_mul (right_ne_zero_of_mul hD)
    rw [coeff_monomial] at h1
    split_ifs at h1 with hn
    · subst hn
      rw [Finset.coe_image]
      exact ⟨d, Finsupp.mem_support_iff.mpr h2, rfl⟩
    · exact (h1 (mul_zero _)).elim

include hb hb₁ hb₂ hi₁ hi₂ hid hcov hj₁ hj₂ hjd in
/-- **Tensor and pullback.** Pulling back the first factor along `a` is the same as
substituting `a` into the first block of variables. -/
theorem pair_tensor_pullback (μ : Dist R τ) (ρ : Dist R κ) (g : MvPowerSeries T R) :
    pair (tensor i₁ i₂ (pullback ha μ) ρ) g = pair (tensor j₁ j₂ μ ρ) (subst b g) := by
  classical
  induction μ using Finsupp.induction_linear with
  | zero => simp [pair_zero]
  | add μ μ' h h' => rw [pullback_add, tensor_add_left, tensor_add_left, pair_add, pair_add, h, h']
  | single e c =>
    rw [pullback_single, tensor_smul_left, pair_smul]
    rw [show (Finsupp.single e c : Dist R τ) = c • Finsupp.single e 1 by simp,
      tensor_smul_left, pair_smul]
    congr 1
    induction ρ using Finsupp.induction_linear with
    | zero => simp [pair_zero]
    | add ρ ρ' h h' => rw [tensor_add_right, tensor_add_right, pair_add, pair_add, h, h']
    | single n c' =>
      rw [show (Finsupp.single n c' : Dist R κ) = c' • Finsupp.single n 1 by simp,
        tensor_smul_right, tensor_smul_right, pair_smul, pair_smul,
        pair_tensor_pullDelta_single ha hb hb₁ hb₂ hi₁ hi₂ hid hcov hj₁ hj₂ hjd,
        tensor_single_single, pair_single]
      ring

end TensorPullback

section TensorComm
variable {τ₁ τ₂ T : Type*} (e₁ : τ₁ → T) (e₂ : τ₂ → T)

lemma tensor_comm (μ : Dist R τ₁) (ν : Dist R τ₂) :
    tensor e₁ e₂ μ ν = tensor e₂ e₁ ν μ := by
  unfold tensor
  rw [Finsupp.sum_comm]
  exact Finsupp.sum_congr fun n _ => Finsupp.sum_congr fun m _ => by rw [add_comm, mul_comm]

end TensorComm

section Convolution
variable {ι : Type*} [Finite ι] (G : FormalGroupLaw R ι)

/-- The two coordinate blocks of `Fin m × ι`. -/
def blk {m : ℕ} (k : Fin m) : ι → Fin m × ι := fun i => (k, i)

lemma blk_injective {m : ℕ} (k : Fin m) : Function.Injective (blk (ι := ι) k) :=
  fun _ _ h => (Prod.mk.inj h).2

lemma blk_disjoint {m : ℕ} {k l : Fin m} (h : k ≠ l) (x y : ι) : blk k x ≠ blk l y :=
  fun e => h (Prod.mk.inj e).1

/-- `μ ⊠ ν` as a distribution in the variables `Fin 2 × ι`. -/
def tensor2 (μ ν : Dist R ι) : Dist R (Fin 2 × ι) := tensor (blk 0) (blk 1) μ ν

lemma FormalGroupLaw.hasSubst_F : HasSubst G.F := hasSubst_of_constantCoeff_zero G.noConst

/-- **Convolution** on `Dist(G)`: `⟨μ * ν, f⟩ = ⟨μ ⊠ ν, f(F(X, Y))⟩`. -/
def conv (μ ν : Dist R ι) : Dist R ι := pullback G.hasSubst_F (tensor2 μ ν)

theorem pair_conv (μ ν : Dist R ι) (f : MvPowerSeries ι R) :
    pair (conv G μ ν) f = pair (tensor2 μ ν) (subst G.F f) := pair_pullback _ _ _

/-- The unit of `Dist(G)`: evaluation at the origin. -/
def one : Dist R ι := Finsupp.single 0 1
/-- The first two blocks of `Fin 3 × ι`. -/
def J₁ : Fin 2 × ι → Fin 3 × ι := fun p => (p.1.castSucc, p.2)
/-- The last two blocks of `Fin 3 × ι`. -/
def K₁ : Fin 2 × ι → Fin 3 × ι := fun p => (p.1.succ, p.2)

omit [Finite ι] in
lemma J₁_injective : Function.Injective (J₁ (ι := ι)) := fun p q h => by
  obtain ⟨h1, h2⟩ := Prod.mk.inj h; exact Prod.ext (Fin.castSucc_injective _ h1) h2

omit [Finite ι] in
lemma K₁_injective : Function.Injective (K₁ (ι := ι)) := fun p q h => by
  obtain ⟨h1, h2⟩ := Prod.mk.inj h; exact Prod.ext (Fin.succ_injective _ h1) h2

omit [Finite ι] in
lemma cover2 (t : Fin 2 × ι) : (∃ s, blk 1 s = t) ∨ (∃ k, blk 0 k = t) := by
  obtain ⟨k, i⟩ := t; fin_cases k
  · exact Or.inr ⟨i, rfl⟩
  · exact Or.inl ⟨i, rfl⟩

lemma subst2_coords01 (f : MvPowerSeries (Fin 2 × ι) R) :
    subst2 (coords (m := 3) 0) (coords 1) f = embed J₁ f := by
  unfold subst2 embed; congr 1; funext p; obtain ⟨k, i⟩ := p; fin_cases k <;> rfl

lemma subst2_coords12 (f : MvPowerSeries (Fin 2 × ι) R) :
    subst2 (coords (m := 3) 1) (coords 2) f = embed K₁ f := by
  unfold subst2 embed; congr 1; funext p; obtain ⟨k, i⟩ := p; fin_cases k <;> rfl

omit [Finite ι] in
lemma tensor3_eq (μ ν ρ : Dist R ι) :
    tensor J₁ (blk 2) (tensor2 μ ν) ρ = tensor K₁ (blk 0) (tensor2 ν ρ) μ := by
  classical
  unfold tensor2
  induction μ using Finsupp.induction_linear with
  | zero => simp
  | add μ μ' h h' => rw [tensor_add_left, tensor_add_left, tensor_add_right, h, h']
  | single m a =>
    rw [show (Finsupp.single m a : Dist R ι) = a • Finsupp.single m 1 by simp]
    simp only [tensor_smul_left, tensor_smul_right]
    congr 1
    induction ν using Finsupp.induction_linear with
    | zero => simp
    | add ν ν' h h' => rw [tensor_add_right, tensor_add_left, tensor_add_left, tensor_add_left, h, h']
    | single n b =>
      rw [show (Finsupp.single n b : Dist R ι) = b • Finsupp.single n 1 by simp]
      simp only [tensor_smul_left, tensor_smul_right]
      congr 1
      induction ρ using Finsupp.induction_linear with
      | zero => simp
      | add ρ ρ' h h' => rw [tensor_add_right, tensor_add_right, tensor_add_left, h, h']
      | single p c =>
        rw [show (Finsupp.single p c : Dist R ι) = c • Finsupp.single p 1 by simp]
        simp only [tensor_smul_left, tensor_smul_right, tensor_single_single, mul_one]
        congr 2
        simp only [Finsupp.mapDomain_add, ← Finsupp.mapDomain_comp]
        have e1 : J₁ ∘ blk (ι := ι) 0 = blk 0 := rfl
        have e2 : J₁ ∘ blk (ι := ι) 1 = blk 1 := rfl
        have e3 : K₁ ∘ blk (ι := ι) 0 = blk 1 := rfl
        have e4 : K₁ ∘ blk (ι := ι) 1 = blk 2 := rfl
        rw [e1, e2, e3, e4]; abel

/-- **Associativity of convolution**, from the associativity of `F`. -/
theorem conv_assoc (μ ν ρ : Dist R ι) : conv G (conv G μ ν) ρ = conv G μ (conv G ν ρ) := by
  refine ext_pair fun f => ?_
  have hu : NoConst (fun i => subst2 (coords (m := 3) 0) (coords 1) (G.F i)) :=
    noConst_subst2 (noConst_coords 0) (noConst_coords 1) G.noConst
  have hv : NoConst (fun i => subst2 (coords (m := 3) 1) (coords 2) (G.F i)) :=
    noConst_subst2 (noConst_coords 1) (noConst_coords 2) G.noConst
  have hbL := hasSubst2 hu (noConst_coords (m := 3) 2)
  have hbR := hasSubst2 (noConst_coords (m := 3) 0) hv
  have hL : pair (conv G (conv G μ ν) ρ) f =
      pair (tensor J₁ (blk 2) (tensor2 μ ν) ρ)
        (subst (fun s => subst2 (fun i => subst2 (coords (m := 3) 0) (coords 1) (G.F i))
          (coords 2) (G.F s)) f) := by
    rw [pair_conv, tensor2, conv,
      pair_tensor_pullback G.hasSubst_F hbL
        (fun s => by simp only [blk, Matrix.cons_val_zero]; exact subst2_coords01 _)
        (fun k => by simp [coords, blk])
        (blk_injective 0) (blk_injective 1) (blk_disjoint (by decide))
        (fun t => (cover2 t).symm) J₁_injective (blk_injective 2)
        (fun x y h => by obtain ⟨k, i⟩ := x; fin_cases k <;> simp [J₁, blk] at h),
      subst_comp_subst_apply G.hasSubst_F hbL]
    rfl
  have hR : pair (conv G μ (conv G ν ρ)) f =
      pair (tensor K₁ (blk 0) (tensor2 ν ρ) μ)
        (subst (fun s => subst2 (coords (m := 3) 0)
          (fun i => subst2 (coords 1) (coords 2) (G.F i)) (G.F s)) f) := by
    rw [pair_conv, tensor2, conv, tensor_comm,
      pair_tensor_pullback G.hasSubst_F hbR
        (fun s => by simp only [blk, Matrix.cons_val_one]; exact subst2_coords12 _)
        (fun k => by simp [coords, blk])
        (blk_injective 1) (blk_injective 0) (blk_disjoint (by decide))
        cover2 K₁_injective (blk_injective 0)
        (fun x y h => by obtain ⟨k, i⟩ := x; fin_cases k <;> simp [K₁, blk] at h),
      subst_comp_subst_apply G.hasSubst_F hbR]
    rfl
  rw [hL, hR, tensor3_eq, G.assoc]
lemma hasSubst_zero_empty : HasSubst (0 : ι → MvPowerSeries Empty R) :=
  hasSubst_of_constantCoeff_zero fun _ => by simp

lemma pullback_zero_empty :
    pullback (hasSubst_zero_empty (R := R) (ι := ι)) (Finsupp.single 0 1) = one := by
  classical
  rw [pullback_single, one_smul, one]
  ext d
  rw [pullDelta_apply, Finsupp.single_apply]
  by_cases hd : d = 0
  · subst hd; simp
  · rw [if_neg (Ne.symm hd)]
    obtain ⟨s, hs⟩ := Finsupp.ne_iff.mp hd
    rw [Finsupp.prod, Finset.prod_eq_zero (i := s) (Finsupp.mem_support_iff.mpr hs)]
    · simp
    · simp [zero_pow hs]

lemma pair_tensor_one_embed (μ : Dist R ι) (f : MvPowerSeries ι R) :
    pair (tensor (Empty.elim : Empty → Fin 1 × ι) (blk 0) (Finsupp.single 0 1) μ)
      (embed (blk 0) f) = pair μ f := by
  classical
  induction μ using Finsupp.induction_linear with
  | zero => simp [pair_zero]
  | add μ μ' h h' => rw [tensor_add_right, pair_add, pair_add, h, h']
  | single n c =>
    rw [tensor_single_single, pair_single, pair_single, Finsupp.mapDomain_zero, zero_add,
      coeff_embed_mapDomain (blk_injective 0), one_mul]

lemma embed_zero' {σ τ : Type*} [Finite σ] (e : σ → τ) : embed e (0 : MvPowerSeries σ R) = 0 := by
  rw [embed_eq_substAlgHom, map_zero]

lemma coords_eq_X_blk {m : ℕ} (k : Fin m) :
    (coords k : ι → MvPowerSeries (Fin m × ι) R) = fun j => X (blk k j) := rfl

/-- `one` is a left unit, from `F(0, Y) = Y`. -/
theorem one_conv (μ : Dist R ι) : conv G one μ = μ := by
  refine ext_pair fun f => ?_
  have hb := hasSubst2 (noConst_zero (R := R) (ι := ι) (τ := Fin 1 × ι)) (noConst_coords 0)
  rw [pair_conv, tensor2, ← pullback_zero_empty,
    pair_tensor_pullback hasSubst_zero_empty hb
      (j₁ := (Empty.elim : Empty → Fin 1 × ι)) (j₂ := blk 0)
      (fun s => by simp [blk, embed_zero'])
      (fun k => by simp [coords, blk])
      (blk_injective 0) (blk_injective 1) (blk_disjoint (by decide))
      (fun t => (cover2 t).symm) (fun x => x.elim) (blk_injective 0) (fun x => x.elim),
    subst_comp_subst_apply G.hasSubst_F hb]
  have hU : (fun s => subst (fun p : Fin 2 × ι => (![0, coords 0] : Fin 2 → ι → MvPowerSeries (Fin 1 × ι) R) p.1 p.2)
      (G.F s)) = (coords (m := 1) 0 : ι → MvPowerSeries (Fin 1 × ι) R) := G.unit_right
  rw [hU, coords_eq_X_blk]
  exact pair_tensor_one_embed μ f

/-- `one` is a right unit, from `F(X, 0) = X`. -/
theorem conv_one (μ : Dist R ι) : conv G μ one = μ := by
  refine ext_pair fun f => ?_
  have hb := hasSubst2 (noConst_coords (R := R) (ι := ι) (m := 1) 0) noConst_zero
  rw [pair_conv, tensor2, tensor_comm, ← pullback_zero_empty,
    pair_tensor_pullback hasSubst_zero_empty hb
      (j₁ := (Empty.elim : Empty → Fin 1 × ι)) (j₂ := blk 0)
      (fun s => by simp [blk, embed_zero'])
      (fun k => by simp [coords, blk])
      (blk_injective 1) (blk_injective 0) (blk_disjoint (by decide))
      cover2 (fun x => x.elim) (blk_injective 0) (fun x => x.elim),
    subst_comp_subst_apply G.hasSubst_F hb]
  have hU : (fun s => subst (fun p : Fin 2 × ι => (![coords 0, 0] : Fin 2 → ι → MvPowerSeries (Fin 1 × ι) R) p.1 p.2)
      (G.F s)) = (coords (m := 1) 0 : ι → MvPowerSeries (Fin 1 × ι) R) := G.unit_left
  rw [hU, coords_eq_X_blk]
  exact pair_tensor_one_embed μ f

end Convolution

end
end QOU.FormalGroups
