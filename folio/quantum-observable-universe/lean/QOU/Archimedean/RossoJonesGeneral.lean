import QOU.IwahoriHecke.TensorMarkovModel

/-!
# QOU.Archimedean.RossoJonesGeneral — Rosso–Jones for every `r`, reduced to weight spaces

Part (iii) of [`prop:rj-canonical-inner-product`](../../../predicted-spectra/rj-canonical-inner-product.md)
for a general number of strands `r = n + 1`. The cases `r = 2, 3, 4` are proved outright in
`QOU.Archimedean.rj_canonical_inner_product` and `QOU.Archimedean.RossoJonesH4`.

By `QOU.IwahoriHecke.TensorMarkovModel.markov_cox_eq_quantumTrace'`, every Markov trace with
`z = z_D` on every Hecke-family algebra gives the torus braid `γ^p = (s₀ ⋯ s_{n−1})^p` the
value of the normalised quantum trace of `γ^p` on `V^{⊗(n+1)}`. This file splits that quantum
trace over the weight spaces of `V^{⊗(n+1)}` (basis states with `m` ones) and computes the
two extremal ones.

## What is proved (sorry-free, over any field, `q ≠ 0`, `q² + 1 ≠ 0`)

* `trace_W_eq_sum_T` — `tr(W · X) = Σ_{m=0}^{n+1} q^{2m} · T_m(X)`, `T_m(X)` the plain trace
  of `X` on the weight-`m` states (any matrix `X`).
* `T_zero`, `T_top` — on the two extremal weight spaces (all zeros, all ones) every
  `σᵢ` acts by `q`, so `T₀(γ^p) = T_{n+1}(γ^p) = q^{np}`.
* `rossoJones_of_middle` and `markov_rossoJones_of_middle` — **conditional on the named
  hypothesis `MiddleWeightTraces q n p`**, which says that on every non-extremal weight space
  `q^{2p} T_m(γ^p) = q^{p(n+2)} − q^{pn}`, every Markov trace `t` with `z_D` satisfies

      q^{2p} (q² + 1)^{n+1} t(γ^p) = (Σ_{m=0}^{n+1} q^{2m}) q^{p(n+2)} − (Σ_{m=1}^{n} q^{2m}) q^{pn}.

  With `Σ_{m=0}^{r} q^{2m} = q^r [r+1]` and `(q²+1)^r = q^r [2]^r` this is the block's
  `[2]^r t(γ^p) = [r+1] q^{p(r−1)} − [r−1] q^{p(r−3)}`, `r = n + 1`.

## What it does NOT prove

`MiddleWeightTraces` itself. It holds exactly when `gcd(n+1, p) = 1` for `r ≤ 5`
(probe `computations/probes/rj_weight_space_trace_probe.py`, exact sympy) and fails for every
non-coprime `(r, p)` tested. Its content is that the non-hook Temperley–Lieb standard modules
contribute nothing to `tr(γ^p)` for coprime `p` (`T_m − T_{m−1}` is the trace on `W_{r, r−2m}`
by quantum Schur–Weyl duality, which is itself not formalised). It is a hypothesis of the
theorems below, not an axiom and not a class field.

-- Ref: [rosso-jones1993] Rosso–Jones, *J. Knot Theory Ramifications* 2 (1993)
-/

namespace QOU.Archimedean.RossoJonesGeneral

open QOU.IwahoriHecke.TensorMarkovModel QOU.IwahoriHecke.JonesNormalForm
open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix QOU.IwahoriHecke.QuantumTrace
open QOU.IwahoriHecke.MarkovPeel

variable {R : Type*} [Field R]

/-- The number of ones in a basis state. -/
def ones {n : ℕ} (u : Fin n → Fin 2) : ℕ := (Finset.univ.filter (fun k => u k = 1)).card

/-- The torus generator `γ = σ₀ ⋯ σ_{n−1}` on `V^{⊗(n+1)}`. -/
noncomputable def gam (q : R) (n : ℕ) : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R :=
  cox (S q n) n

/-- The plain trace of `X` on the weight space of states with `m` ones. -/
noncomputable def T {n : ℕ} (X : Matrix (Fin n → Fin 2) (Fin n → Fin 2) R) (m : ℕ) : R :=
  ∑ u ∈ Finset.univ.filter (fun u : Fin n → Fin 2 => ones u = m), X u u

variable {q : R}

theorem wt_apply (q : R) (x : Fin 2) : wt q x = if x = 1 then q ^ 2 else 1 := by
  fin_cases x <;> simp [wt]

theorem prod_wt {n : ℕ} (q : R) (u : Fin n → Fin 2) : (∏ k, wt q (u k)) = (q ^ 2) ^ ones u := by
  classical
  simp only [wt_apply]
  rw [Finset.prod_ite, Finset.prod_const_one, mul_one, Finset.prod_const]
  rfl

theorem ones_le {n : ℕ} (u : Fin n → Fin 2) : ones u ≤ n := by
  unfold ones
  exact (Finset.card_filter_le _ _).trans (by simp)

/-- **The quantum trace splits over weight spaces.** -/
theorem trace_W_eq_sum_T (q : R) {n : ℕ} (X : Matrix (Fin n → Fin 2) (Fin n → Fin 2) R) :
    Matrix.trace (W q n * X) = ∑ m ∈ Finset.range (n + 1), (q ^ 2) ^ m * T X m := by
  classical
  rw [W, trace_siteWeight_mul]
  simp only [prod_wt]
  rw [← Finset.sum_fiberwise_of_maps_to (g := ones) (t := Finset.range (n + 1))
    (fun u _ => Finset.mem_range.mpr (Nat.lt_succ_of_le (ones_le u)))]
  refine Finset.sum_congr rfl fun m _ => ?_
  rw [T, Finset.mul_sum]
  refine Finset.sum_congr rfl fun u hu => ?_
  rw [(Finset.mem_filter.mp hu).2]

/-! ## The extremal weight spaces -/

theorem rCheck_const_row (q qi : R) (c : Fin 2) (b : Fin 2 × Fin 2) :
    rCheck q qi (c, c) b = if b = (c, c) then q else 0 := by
  obtain ⟨b1, b2⟩ := b
  fin_cases c <;> fin_cases b1 <;> fin_cases b2 <;> simp

/-- Every `σᵢ` fixes a constant state with eigenvalue `q` (row form). -/
theorem S_const_row (q : R) {n i : ℕ} (hi : i < n) (c : Fin 2)
    (v : Fin (n + 1) → Fin 2) :
    S q n i (fun _ => c) v = if v = (fun _ => c) then q else 0 := by
  classical
  rw [S_of_lt q hi, strandBraid, braidAt, embedPair_apply, rCheck_const_row]
  set I : Fin (n + 1) := (⟨i, hi⟩ : Fin n).castSucc
  set J : Fin (n + 1) := (⟨i, hi⟩ : Fin n).succ
  by_cases hv : v = fun _ => c
  · subst hv; simp
  · rw [if_neg hv]
    split_ifs with h1 h2
    · exfalso
      apply hv
      funext k
      by_cases hkI : k = I
      · rw [hkI]; exact (congrArg Prod.fst h2)
      · by_cases hkJ : k = J
        · rw [hkJ]; exact (congrArg Prod.snd h2)
        · exact (h1 k hkI hkJ).symm
    · rfl
    · rfl

theorem S_const_mul (q : R) {n i : ℕ} (hi : i < n) (c : Fin 2)
    (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R) (b : Fin (n + 1) → Fin 2) :
    (S q n i * X) (fun _ => c) b = q * X (fun _ => c) b := by
  classical
  rw [Matrix.mul_apply, Finset.sum_eq_single (fun _ => c)]
  · rw [S_const_row q hi, if_pos rfl]
  · intro v _ hv
    rw [S_const_row q hi, if_neg hv, zero_mul]
  · intro h; exact absurd (Finset.mem_univ _) h

theorem cox_const_mul (q : R) {n : ℕ} (c : Fin 2)
    (X : Matrix (Fin (n + 1) → Fin 2) (Fin (n + 1) → Fin 2) R) (b : Fin (n + 1) → Fin 2) :
    ∀ k, k ≤ n → (cox (S q n) k * X) (fun _ => c) b = q ^ k * X (fun _ => c) b := by
  intro k
  induction k generalizing X with
  | zero => intro _; simp [cox]
  | succ k ih =>
    intro hk
    rw [cox, mul_assoc, ih _ (by omega), S_const_mul q (by omega), pow_succ]
    ring

theorem gam_pow_const (q : R) (n : ℕ) (c : Fin 2) :
    ∀ p, (gam q n ^ p) (fun _ => c) (fun _ => c) = q ^ (n * p) := by
  intro p
  induction p with
  | zero => simp
  | succ p ih =>
    rw [pow_succ', gam, cox_const_mul q c _ _ n le_rfl, ← gam, ih, Nat.mul_succ, pow_add]
    ring

theorem ones_eq_zero_iff {n : ℕ} (u : Fin n → Fin 2) : ones u = 0 ↔ u = fun _ => 0 := by
  unfold ones
  rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
  constructor
  · intro h; funext k
    have h1 : u k ≠ 1 := h (Finset.mem_univ k)
    have h2 := (u k).isLt
    show u k = 0
    ext
    simp only [Fin.ext_iff, Fin.val_one, Fin.val_zero] at h1 ⊢
    omega
  · rintro rfl k _; simp

theorem ones_eq_top_iff {n : ℕ} (u : Fin n → Fin 2) : ones u = n ↔ u = fun _ => 1 := by
  unfold ones
  constructor
  · intro h
    have h' : Finset.univ.filter (fun k => u k = 1) = Finset.univ :=
      Finset.eq_univ_of_card _ (by rw [h, Fintype.card_fin])
    funext k
    exact Finset.filter_eq_self.mp h' k (Finset.mem_univ k)
  · rintro rfl; simp

theorem T_zero (q : R) (n p : ℕ) : T (gam q n ^ p) 0 = q ^ (n * p) := by
  classical
  rw [T, Finset.sum_eq_single (fun _ => 0)]
  · exact gam_pow_const q n 0 p
  · intro u hu hne
    exact absurd ((ones_eq_zero_iff u).mp (Finset.mem_filter.mp hu).2) hne
  · intro h; exact absurd (Finset.mem_filter.mpr ⟨Finset.mem_univ _, by
      rw [ones_eq_zero_iff]⟩) h

theorem T_top (q : R) (n p : ℕ) : T (gam q n ^ p) (n + 1) = q ^ (n * p) := by
  classical
  rw [T, Finset.sum_eq_single (fun _ => 1)]
  · exact gam_pow_const q n 1 p
  · intro u hu hne
    exact absurd ((ones_eq_top_iff u).mp (Finset.mem_filter.mp hu).2) hne
  · intro h; exact absurd (Finset.mem_filter.mpr ⟨Finset.mem_univ _, by
      rw [ones_eq_top_iff]⟩) h

/-! ## The conditional general-`r` formula -/

/-- **The named hypothesis.** On every non-extremal weight space of `V^{⊗(n+1)}`, the trace
of `γ^p` is `q^{p(n+2) − 2p} − q^{pn − 2p}`, i.e. `q^{p(r−1)} − q^{p(r−3)}` (`r = n + 1`),
stated with the factor `q^{2p}` cleared. Verified for `r ≤ 5` and `gcd(r, p) = 1` by the
probe; false when `gcd(r, p) > 1`. Not proved here. -/
def MiddleWeightTraces (q : R) (n p : ℕ) : Prop :=
  ∀ m, 0 < m → m < n + 1 → q ^ (2 * p) * T (gam q n ^ p) m = q ^ (p * (n + 2)) - q ^ (p * n)

/-- **Rosso–Jones on `V^{⊗(n+1)}`, conditional on `MiddleWeightTraces`.** -/
theorem rossoJones_of_middle (q : R) (n p : ℕ) (h : MiddleWeightTraces q n p) :
    q ^ (2 * p) * Matrix.trace (W q (n + 1) * gam q n ^ p)
      = (∑ m ∈ Finset.range (n + 2), (q ^ 2) ^ m) * q ^ (p * (n + 2))
        - (∑ m ∈ Finset.Ioo 0 (n + 1), (q ^ 2) ^ m) * q ^ (p * n) := by
  rw [trace_W_eq_sum_T, Finset.mul_sum]
  -- split off `m = 0` and `m = n + 1`
  have hr : Finset.range (n + 2) = insert 0 (insert (n + 1) (Finset.Ioo 0 (n + 1))) := by
    ext m; simp only [Finset.mem_range, Finset.mem_insert, Finset.mem_Ioo]; omega
  have h0 : (0 : ℕ) ∉ insert (n + 1) (Finset.Ioo 0 (n + 1)) := by simp
  have h1 : n + 1 ∉ Finset.Ioo 0 (n + 1) := by simp
  rw [hr, Finset.sum_insert h0, Finset.sum_insert h1, Finset.sum_insert h0, Finset.sum_insert h1,
    T_zero, T_top]
  have hmid : ∑ m ∈ Finset.Ioo 0 (n + 1), q ^ (2 * p) * ((q ^ 2) ^ m * T (gam q n ^ p) m)
      = ∑ m ∈ Finset.Ioo 0 (n + 1), (q ^ 2) ^ m * (q ^ (p * (n + 2)) - q ^ (p * n)) := by
    refine Finset.sum_congr rfl fun m hm => ?_
    obtain ⟨hm0, hm1⟩ := Finset.mem_Ioo.mp hm
    rw [← h m hm0 hm1]; ring
  rw [hmid, ← Finset.sum_mul]
  have e : q ^ (2 * p) * q ^ (n * p) = q ^ (p * (n + 2)) := by
    rw [← pow_add]; congr 1; ring
  simp only [pow_zero, one_mul]
  rw [e]
  ring

/-- **Rosso–Jones for every Markov trace with `z_D`, conditional on `MiddleWeightTraces`.**
For any algebra with a Hecke family `(N, q − q⁻¹, 1)`, `n ≤ N`, and any normalised, cyclic
Markov trace `t` with `z = z_D`. -/
theorem markov_rossoJones_of_middle (hq : q ≠ 0) (hq1 : q ^ 2 + 1 ≠ 0)
    {B : Type*} [Ring B] [Algebra R B] {N : ℕ} {s : ℕ → B}
    (hs : HeckeFamily N (q - q⁻¹) 1 s) (t : B →ₗ[R] R) (ht1 : t 1 = 1)
    (hcyc : ∀ x y : B, t (x * y) = t (y * x))
    (hmark : ∀ k, k < N → ∀ x ∈ Algebra.adjoin R (s '' Set.Iio k), t (x * s k) = zD q * t x)
    {n : ℕ} (hn : n ≤ N) (p : ℕ) (h : MiddleWeightTraces q n p) :
    q ^ (2 * p) * (q ^ 2 + 1) ^ (n + 1) * t (cox s n ^ p)
      = (∑ m ∈ Finset.range (n + 2), (q ^ 2) ^ m) * q ^ (p * (n + 2))
        - (∑ m ∈ Finset.Ioo 0 (n + 1), (q ^ 2) ^ m) * q ^ (p * n) := by
  rw [markov_cox_eq_quantumTrace' hq hq1 hs t ht1 hcyc hmark hn p, ← gam,
    ← rossoJones_of_middle q n p h]
  have h1 : (q ^ 2 + 1) ^ (n + 1) ≠ 0 := pow_ne_zero _ hq1
  field_simp

end QOU.Archimedean.RossoJonesGeneral
