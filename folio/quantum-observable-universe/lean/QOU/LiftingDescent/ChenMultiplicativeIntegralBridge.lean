import QOU.LiftingDescent.MassTraceIdentity
import MathlibExt.YekutieliIntegration
import QOU.Core.CategoricalLagrangianTwoTermBridge
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.ODE.ExistUnique
import Mathlib.Analysis.Matrix.Normed
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Normed.Operator.Mul
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.SpecificLimits.Basic

/-!
# Continuous Chen / Picard–Dyson Multiplicative Integral & `MassTraceIdentity` Substrate `nablaEndo` Instantiation

Workstream W7 (`Q-Gap-5`; beans `qou-9sj3`, `qou-ywyq`, `qou-wp3h`, `qou-ni4b`).

This module bridges the discrete ordered-product layer of `QOU.Torsion.MassTraceIdentity` and
`QOU.MathlibExt.YekutieliIntegration` to:
1. **Discrete-to-Continuous Picard–Dyson / Chen Multiplicative Integration (§1–§3):**
   - Time-ordered path products `orderedProd` (`P(γ₁ ⋆ γ₂) = P(γ₂) · P(γ₁)`), discrete boundary
     gauge covariance (`P_N(U') = g_N · P_N(U) · g_0⁻¹`), closed-loop trace gauge invariance
     (`Tr(g_0 · P(γ) · g_0⁻¹) = Tr(P(γ))`), and Drinfeld-associator intertwiner trace invariance
     over arbitrary `[CommRing R]` (§7c).
   - Formal Chen iterated-integral signatures on the word/tensor coalgebra over `[CommRing R]`:
     proves the **Shuffle–Deconcatenation Hopf Bialgebra Theorem** (`shuffleEval_chenSigMul`),
     the division-free binomial shuffle identity (`shuffleEval_wordProd`), segment group-likeness
     (`isShuffleGroupLike_segmentSig`), and **group-like closure under Chen path concatenation**
     (`IsShuffleGroupLike.chenSigMul`, i.e. `Δ_sh(J(γ₁ ⋆ γ₂)) = J(γ₁ ⋆ γ₂) ⊗ J(γ₁ ⋆ γ₂)`).
   - Explicit **Picard Cauchy contraction** (`norm_picardOp_sub_le`), Grönwall ODE uniqueness
     (`IsLinearFundSol.eqOn`), and **discrete Grönwall `O(1/N)` error bound**
     (`eulerOrderedProd_error_bound` & `tendsto_eulerOrderedProd_isFundSol`) proving that the
     `N`-step ordered product `∏_{j=1}^N (1 + ∫_{(j-1)/N}^{j/N} X(s) ds)` converges in any
     complete normed `ℝ`-algebra `A` to the unique fundamental solution of `U'(t) = X(t) U(t)`,
     `U(0) = 1`, with explicit error `≤ M² exp(2M) / N`.
2. **Concrete Non-Commutative Matrix Substrate & `nablaEndo` Instantiation (§4–§5):**
   - Constructs the `R`-linear braided monoidal category `FinMatObj R` and the non-commutative
     `d²`-dimensional matrix Frobenius–Hopf substrate `matFrobHopf d` (`Mat_d(R)`), discharging
     `frobeniusForm = counit` definitionally (`rfl`) and evaluating both forms of
     `MassTraceIdentity` (`∫_A(Ψ ∘ hol w) = Tr(M₁ ⋯ M_k)` and `tr_{End(A)}(L_{hol w} ∘ Ψ) = d · Tr(M₁ ⋯ M_k)`).
   - Instantiates `QOU.CategoricalConnection` via the genuine Leibniz inner derivation
     `adEndo Ω` (`∇_Ω(XY) = ∇_Ω(X)Y + X∇_Ω(Y)`, `adEndo Ω ≠ 0` for non-central KZ Casimir `Ω`),
     and instantiates normalised `QOU.CategoricalLagrangian` configurations discharging all
     hypotheses (`hQn`, `hQp`, `hNabla`, `hCross`, `hReebN`, `hReebP`, `hHoriz`, `hMatReebN`,
     `hMatReebP`) of `CategoricalLagrangianTwoTermBridge.trace_lagrangian_diff_concrete_borromean_weight_space`.
     **Scope honesty:** this proves non-vacuous joint satisfiability and structural consistency of
     the substrate axioms (`∫_A = ε`, `nablaEndo ≠ 0`, automatic `hCross` and `hHoriz` vanishing
     by Leibniz + trace cyclicity); selecting the continuum Reeb sector matrices `(M, N)` from a
     first-principles variational principle remains an explicit physical modelling input.
   - Constructs division-free `[CommRing R]` Hecke and KZ representations on `B_3` (`[2,1]`, `d = 2`)
     and `B_4` (`[2,2]`, `d = 2`, and `[3,1]`, `d = 3`), proves the Kohno–Arnold 4T flatness
     identities and continuous KZ half-turn `IsLinearFundSol` ODE solutions, and proves exact trace
     agreement `Tr(M_KZ(σ_j)) = Tr(ρ_Hecke(σ_j))` at both complex `q = exp(i π ħ_KZ)` and real
     hyperbolic `q_0 = exp(η_0)`.

Zero empirical constants (`CODATA`, `AME2020`, `PDG`) enter this file.

## References

- Ref: [yekutieli2015] https://doi.org/10.1142/9537 — non-abelian multiplicative integration.
- Ref: [kohno1987] https://doi.org/10.5802/aif.1114 — monodromy of the KZ connection and Hecke representations.
- Ref: [drinfeld1990] — quasi-Hopf algebras and the KZ associator `Φ_KZ`.
- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 — Frobenius objects in monoidal categories.
- Ref: [jimbo1986] https://doi.org/10.1007/BF00704588 — quantum `R`-matrices and Hecke representations.
- Ref: [jones1987] https://doi.org/10.2307/1971403 — Hecke algebra representations of braid groups.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory
open CategoryTheory Matrix Set Filter Topology

namespace QOU.Torsion.ChenMultiplicativeIntegralBridge

/-! ## §1. Discrete Time-Ordered Multiplicative Integral, Dyson Convolution, & Gauge Covariance -/

section OrderedProductAndGauge

/-- **Time-ordered path product** of local step transports `[U₁, …, U_k]` (`U₁` earliest, `U_k` latest),
    matching column-vector ODE parallel transport `Φ(t_k) = U_k ⋯ U₁ Φ(t₀)`. -/
def orderedProd {A : Type*} [Monoid A] : List A → A
  | [] => 1
  | u :: us => orderedProd us * u

@[simp] theorem orderedProd_nil {A : Type*} [Monoid A] : orderedProd ([] : List A) = 1 := rfl

@[simp] theorem orderedProd_cons {A : Type*} [Monoid A] (u : A) (us : List A) :
    orderedProd (u :: us) = orderedProd us * u := rfl

@[simp] theorem orderedProd_singleton {A : Type*} [Monoid A] (u : A) :
    orderedProd [u] = u := one_mul u

/-- **Path-concatenation multiplicativity (`P(γ₁ ⋆ γ₂) = P(γ₂) · P(γ₁)`):**
    concatenating an initial transport list `us₁` followed by `us₂` composes their time-ordered
    products in operator order (`us₂` acting after `us₁`). -/
theorem orderedProd_append {A : Type*} [Monoid A] (us₁ us₂ : List A) :
    orderedProd (us₁ ++ us₂) = orderedProd us₂ * orderedProd us₁ := by
  induction us₁ with
  | nil => simp
  | cons u us ih => simp [ih, mul_assoc]

/-- Comparison with `YekutieliIntegration.holonomy`: `orderedProd` is `holonomy` on the reversed list. -/
theorem orderedProd_eq_yekutieli_holonomy_reverse {A : Type*} [Monoid A] (us : List A) :
    orderedProd us = QOU.MathlibExt.YekutieliIntegration.holonomy us.reverse := by
  induction us with
  | nil => rfl
  | cons u us ih =>
    simp [orderedProd, ih, QOU.MathlibExt.YekutieliIntegration.holonomy_append]

/-- Discrete Euler/Riemann multiplicative integral `∏_{j} (1 + dA_j)` of infinitesimal increments. -/
def eulerStepProd {A : Type*} [Semiring A] (dA : List A) : A :=
  orderedProd (dA.map fun X => 1 + X)

/-- Path-concatenation multiplicativity of the discrete Euler/Riemann multiplicative integral. -/
theorem eulerStepProd_append {A : Type*} [Semiring A] (dA₁ dA₂ : List A) :
    eulerStepProd (dA₁ ++ dA₂) = eulerStepProd dA₂ * eulerStepProd dA₁ := by
  simp [eulerStepProd, List.map_append, orderedProd_append]

/-- Indexed `N`-step time-ordered product `U_{N-1} ⋯ U_0`. -/
def orderedProdFin {A : Type*} [Monoid A] (U : ℕ → A) : ℕ → A
  | 0 => 1
  | k + 1 => U k * orderedProdFin U k

/-- **Discrete non-abelian gauge covariance by telescoping:**
    if each step transport transforms as `U'_k = g_{k+1} U_k g_k⁻¹` in a group `G` (or unit group `Aˣ`),
    the `N`-step ordered product transforms by boundary values `P_N(U') = g_N P_N(U) g_0⁻¹`. -/
theorem orderedProdFin_gauge_covariant {G : Type*} [Group G] (g U U' : ℕ → G)
    (hcov : ∀ k, U' k = g (k + 1) * U k * (g k)⁻¹) (N : ℕ) :
    orderedProdFin U' N = g N * orderedProdFin U N * (g 0)⁻¹ := by
  induction N with
  | zero => simp [orderedProdFin]
  | succ k ih =>
    rw [orderedProdFin, orderedProdFin, hcov k, ih]
    group

/-- **Matrix gauge transformation** `g₁ · P · g₀⁻¹` on `Matrix n n R` over `[CommRing R]`. -/
def gaugeTransform {R : Type*} [CommRing R] {n : Type*} [Fintype n] [DecidableEq n]
    (g₁ g₀ : (Matrix n n R)ˣ) (P : Matrix n n R) : Matrix n n R :=
  (g₁ : Matrix n n R) * P * ((g₀⁻¹ : (Matrix n n R)ˣ) : Matrix n n R)

/-- Gauge transformations compose multiplicatively across concatenated path endpoints. -/
theorem gaugeTransform_mul {R : Type*} [CommRing R] {n : Type*} [Fintype n] [DecidableEq n]
    (g₂ g₁ g₀ : (Matrix n n R)ˣ) (P₂ P₁ : Matrix n n R) :
    gaugeTransform g₂ g₁ P₂ * gaugeTransform g₁ g₀ P₁ =
      gaugeTransform g₂ g₀ (P₂ * P₁) := by
  unfold gaugeTransform
  have cancel : ((g₁⁻¹ : (Matrix n n R)ˣ) : Matrix n n R) * (g₁ : Matrix n n R) = 1 :=
    Units.inv_mul g₁
  calc (g₂ : Matrix n n R) * P₂ * ↑g₁⁻¹ * (↑g₁ * P₁ * ↑g₀⁻¹)
      = (g₂ : Matrix n n R) * P₂ * ((↑g₁⁻¹ * ↑g₁) * P₁) * ↑g₀⁻¹ := by
          simp only [Matrix.mul_assoc]
    _ = (g₂ : Matrix n n R) * (P₂ * P₁) * ↑g₀⁻¹ := by
          rw [cancel, Matrix.one_mul]; simp only [Matrix.mul_assoc]

/-- **Closed-loop holonomy trace gauge invariance (`g₁ = g₀`):**
    `Tr(g₀ · P · g₀⁻¹) = Tr(P)` over any `[CommRing R]`. -/
theorem trace_gaugeTransform_closed_loop {R : Type*} [CommRing R]
    {n : Type*} [Fintype n] [DecidableEq n] (g₀ : (Matrix n n R)ˣ) (P : Matrix n n R) :
    Matrix.trace (gaugeTransform g₀ g₀ P) = Matrix.trace P := by
  unfold gaugeTransform
  rw [Matrix.trace_mul_cycle, Units.inv_mul, Matrix.one_mul]

/-- **Drinfeld associator / intertwiner trace invariance:**
    if an invertible matrix `W` (such as the KZ associator intertwiner `Φ_KZ`) satisfies
    `W · P = Q · W`, then `Tr(P) = Tr(Q)` over any `[CommRing R]`. -/
theorem trace_eq_of_units_intertwine {R : Type*} [CommRing R]
    {n : Type*} [Fintype n] [DecidableEq n] (W : (Matrix n n R)ˣ) {P Q : Matrix n n R}
    (hW : (W : Matrix n n R) * P = Q * (W : Matrix n n R)) :
    Matrix.trace P = Matrix.trace Q := by
  have hP : P = ((W⁻¹ : (Matrix n n R)ˣ) : Matrix n n R) * Q * (W : Matrix n n R) := by
    calc P = (↑W⁻¹ * ↑W) * P := by rw [Units.inv_mul, Matrix.one_mul]
      _ = ↑W⁻¹ * (↑W * P) := by rw [Matrix.mul_assoc]
      _ = ↑W⁻¹ * (Q * ↑W) := by rw [hW]
      _ = ↑W⁻¹ * Q * ↑W := by rw [Matrix.mul_assoc]
  rw [hP, Matrix.trace_mul_cycle, Units.mul_inv, Matrix.one_mul]

/-- **Weighted trace invariance under a Cartan-commuting intertwiner:**
    if `W · P = Q · W` and `W · K = K · W`, then `Tr(K · P) = Tr(K · Q)`. -/
theorem weighted_trace_eq_of_commuting_intertwine {R : Type*} [CommRing R]
    {n : Type*} [Fintype n] [DecidableEq n] (W : (Matrix n n R)ˣ) {K P Q : Matrix n n R}
    (hK : (W : Matrix n n R) * K = K * (W : Matrix n n R))
    (hW : (W : Matrix n n R) * P = Q * (W : Matrix n n R)) :
    Matrix.trace (K * P) = Matrix.trace (K * Q) :=
  trace_eq_of_units_intertwine W (by
    rw [← Matrix.mul_assoc, hK, Matrix.mul_assoc, hW, ← Matrix.mul_assoc])

/-- **Graded Picard–Dyson convolution** of formal iterated-integral towers `J : ℕ → A` over `[Semiring A]`:
    `(J₂ ⋆ J₁)_n = ∑_{k=0}^n J₂(n - k) · J₁(k)`. -/
def chenDysonConv {A : Type*} [Semiring A] (J₂ J₁ : ℕ → A) (n : ℕ) : A :=
  ∑ k ∈ Finset.range (n + 1), J₂ (n - k) * J₁ k

/-- Identity tower `1_0 = 1`, `1_{n+1} = 0` for `chenDysonConv`. -/
def chenDysonUnit {A : Type*} [Semiring A] : ℕ → A
  | 0 => 1
  | _ + 1 => 0

theorem chenDysonUnit_left {A : Type*} [Semiring A] (J : ℕ → A) (n : ℕ) :
    chenDysonConv chenDysonUnit J n = J n := by
  unfold chenDysonConv
  rw [Finset.sum_eq_single n]
  · simp [chenDysonUnit]
  · intro k hk hkn
    have hlt : k < n := Nat.lt_of_le_of_ne (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)) hkn
    obtain ⟨m, hm⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.sub_ne_zero_of_lt hlt)
    rw [hm]; simp [chenDysonUnit]
  · intro hn; exact absurd (Finset.mem_range.mpr (Nat.lt_succ_self n)) hn

theorem chenDysonUnit_right {A : Type*} [Semiring A] (J : ℕ → A) (n : ℕ) :
    chenDysonConv J chenDysonUnit n = J n := by
  unfold chenDysonConv
  rw [Finset.sum_eq_single 0]
  · simp [chenDysonUnit]
  · intro k _ hk0
    obtain ⟨m, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hk0
    simp [chenDysonUnit]
  · intro h0; exact absurd (Finset.mem_range.mpr (Nat.zero_lt_succ n)) h0

end OrderedProductAndGauge

/-! ## §2. Formal Chen Signature Shuffle–Deconcatenation Hopf Bialgebra & Group-Like Law -/

section ChenShuffleCoalgebra

variable {α R : Type*} [CommRing R]

/-- Identity signature `1([]) = 1`, `1(a :: w) = 0` for the deconcatenation coalgebra. -/
def chenSigOne : List α → R
  | [] => 1
  | _ :: _ => 0

/-- **Chen deconcatenation convolution** `(F ⋆ G)(w) = ∑_{k=0}^{|w|} F(w_{<k}) · G(w_{≥k})`. -/
def chenSigMul (F G : List α → R) (w : List α) : R :=
  ∑ k ∈ Finset.range (w.length + 1), F (w.take k) * G (w.drop k)

/-- Left unit law `1 ⋆ G = G` for `chenSigMul`. -/
theorem chenSigOne_mul (G : List α → R) (w : List α) :
    chenSigMul chenSigOne G w = G w := by
  unfold chenSigMul
  rw [Finset.sum_eq_single 0]
  · simp [chenSigOne]
  · intro k hk hk0
    obtain ⟨m, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hk0
    cases w with
    | nil =>
      simp only [List.length_nil, zero_add, Finset.mem_range] at hk
      omega
    | cons _ _ => simp [chenSigOne]
  · intro h0; exact absurd (Finset.mem_range.mpr (Nat.zero_lt_succ _)) h0

/-- Right unit law `F ⋆ 1 = F` for `chenSigMul`. -/
theorem mul_chenSigOne (F : List α → R) (w : List α) :
    chenSigMul F chenSigOne w = F w := by
  unfold chenSigMul
  rw [Finset.sum_eq_single w.length]
  · simp [chenSigOne]
  · intro k hk hkw
    have hlt : k < w.length := Nat.lt_of_le_of_ne (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)) hkw
    have hdrop : w.drop k ≠ [] := by
      intro hnil
      have := congrArg List.length hnil
      rw [List.length_drop, List.length_nil] at this
      omega
    cases hd : w.drop k with
    | nil => exact absurd hd hdrop
    | cons _ _ => simp [chenSigOne]
  · intro hw; exact absurd (Finset.mem_range.mpr (Nat.lt_succ_self _)) hw

/-- Letter-prepend shift `(sigShift a S)(w) = S(a :: w)`. -/
def sigShift (a : α) (S : List α → R) (w : List α) : R := S (a :: w)

lemma chenSigMul_cons (F G : List α → R) (a : α) (w : List α) :
    chenSigMul F G (a :: w) = F [] * G (a :: w) + chenSigMul (sigShift a F) G w := by
  unfold chenSigMul sigShift
  rw [List.length_cons, Finset.sum_range_succ']
  simp [add_comm]

/-- Associativity of Chen deconcatenation convolution `(F ⋆ G) ⋆ H = F ⋆ (G ⋆ H)`. -/
theorem chenSigMul_assoc (F G H : List α → R) :
    ∀ w : List α, chenSigMul (chenSigMul F G) H w = chenSigMul F (chenSigMul G H) w
  | [] => by simp [chenSigMul, mul_assoc]
  | a :: w => by
    rw [chenSigMul_cons, chenSigMul_cons]
    have hshift : sigShift a (chenSigMul F G) =
        fun u => F [] * sigShift a G u + chenSigMul (sigShift a F) G u := by
      funext u; exact chenSigMul_cons F G a u
    have hlin : chenSigMul (fun u => F [] * sigShift a G u + chenSigMul (sigShift a F) G u) H w =
        F [] * chenSigMul (sigShift a G) H w + chenSigMul (chenSigMul (sigShift a F) G) H w := by
      unfold chenSigMul
      simp only [add_mul, mul_assoc, Finset.sum_add_distrib, Finset.mul_sum]
    have hGH : chenSigMul G H (a :: w) = G [] * H (a :: w) + chenSigMul (sigShift a G) H w :=
      chenSigMul_cons G H a w
    rw [hshift, hlin, chenSigMul_assoc (sigShift a F) G H w, hGH]
    have hF0 : (chenSigMul F G) [] = F [] * G [] := by simp [chenSigMul]
    rw [hF0]
    ring

/-- **All shuffles** `u ⊔⊔ v` of two words `u, v : List α`. -/
def shuffles : List α → List α → List (List α)
  | [], v => [v]
  | a :: u, [] => [a :: u]
  | a :: u, b :: v =>
    (shuffles u (b :: v)).map (a :: ·) ++ (shuffles (a :: u) v).map (b :: ·)

/-- **Chen shuffle pairing** `⟨S, u ⊔⊔ v⟩ = ∑_{w ∈ shuffles(u, v)} S(w)`. -/
def shuffleEval (S : List α → R) (u v : List α) : R :=
  ((shuffles u v).map S).sum

@[simp] theorem shuffleEval_nil_left (S : List α → R) (v : List α) :
    shuffleEval S [] v = S v := by
  simp [shuffleEval, shuffles]

@[simp] theorem shuffleEval_nil_right (S : List α → R) (u : List α) :
    shuffleEval S u [] = S u := by
  cases u <;> simp [shuffleEval, shuffles]

theorem shuffleEval_cons_cons (S : List α → R) (a b : α) (u v : List α) :
    shuffleEval S (a :: u) (b :: v) =
      shuffleEval (sigShift a S) u (b :: v) + shuffleEval (sigShift b S) (a :: u) v := by
  simp only [shuffleEval, shuffles, List.map_append, List.sum_append, List.map_map]
  rfl

private lemma list_map_sum_add {β : Type*} (f g : β → R) (l : List β) :
    (l.map fun x => f x + g x).sum = (l.map f).sum + (l.map g).sum := by
  induction l with
  | nil => simp
  | cons _ _ ih => simp [ih]; ring

private lemma list_map_sum_const_mul {β : Type*} (c : R) (f : β → R) (l : List β) :
    (l.map fun x => c * f x).sum = c * (l.map f).sum := by
  induction l with
  | nil => simp
  | cons _ _ ih => simp [ih]; ring

theorem shuffleEval_add (S₁ S₂ : List α → R) (u v : List α) :
    shuffleEval (fun w => S₁ w + S₂ w) u v = shuffleEval S₁ u v + shuffleEval S₂ u v :=
  list_map_sum_add S₁ S₂ (shuffles u v)

theorem shuffleEval_const_mul (c : R) (S : List α → R) (u v : List α) :
    shuffleEval (fun w => c * S w) u v = c * shuffleEval S u v :=
  list_map_sum_const_mul c S (shuffles u v)

/-- **Group-like signature (`Δ_sh(S) = S ⊗ S`):**
    `S([]) = 1` and `⟨S, u ⊔⊔ v⟩ = S(u) · S(v)` for all words `u, v`. -/
def IsShuffleGroupLike (S : List α → R) : Prop :=
  S [] = 1 ∧ ∀ u v : List α, shuffleEval S u v = S u * S v

/-- The trivial signature `chenSigOne` is group-like. -/
theorem isShuffleGroupLike_one : IsShuffleGroupLike (chenSigOne : List α → R) := by
  refine ⟨rfl, fun u v => ?_⟩
  cases u with
  | nil => simp [chenSigOne]
  | cons a u =>
    cases v with
    | nil => simp [chenSigOne]
    | cons b v =>
      rw [shuffleEval_cons_cons]
      have hzero : ∀ (x : α), sigShift x (chenSigOne : List α → R) = fun _ => 0 := by
        intro x; funext w; rfl
      rw [hzero a, hzero b]
      have hz : ∀ p q : List α, shuffleEval (fun _ : List α => (0 : R)) p q = 0 := by
        intro p q
        have := shuffleEval_const_mul (0 : R) (fun _ => (1 : R)) p q
        simpa using this
      simp [hz, chenSigOne]

/-- Unnormalized word monomial `wordProd x [a₁, …, a_k] = x(a₁) ⋯ x(a_k)` over `[CommRing R]`. -/
def wordProd (x : α → R) : List α → R
  | [] => 1
  | a :: w => x a * wordProd x w

/-- **Division-free binomial shuffle identity over `[CommRing R]`:**
    `⟨wordProd x, u ⊔⊔ v⟩ = C(|u| + |v|, |u|) · wordProd x u · wordProd x v`. -/
theorem shuffleEval_wordProd (x : α → R) :
    ∀ u v : List α,
      shuffleEval (wordProd x) u v =
        (Nat.choose (u.length + v.length) u.length : R) * wordProd x u * wordProd x v
  | [], v => by simp [wordProd]
  | a :: u, [] => by simp [wordProd]
  | a :: u, b :: v => by
    rw [shuffleEval_cons_cons]
    have hs : ∀ c : α, sigShift c (wordProd x) = fun w => x c * wordProd x w := by
      intro c; funext w; rfl
    rw [hs a, hs b, shuffleEval_const_mul, shuffleEval_const_mul,
      shuffleEval_wordProd x u (b :: v), shuffleEval_wordProd x (a :: u) v]
    simp only [List.length_cons, wordProd]
    have hlen1 : u.length + 1 + v.length = u.length + (v.length + 1) := by omega
    have hlen2 : u.length + 1 + (v.length + 1) = (u.length + (v.length + 1)) + 1 := by omega
    have hchoose :
        Nat.choose ((u.length + (v.length + 1)) + 1) (u.length + 1) =
          Nat.choose (u.length + (v.length + 1)) u.length +
            Nat.choose (u.length + (v.length + 1)) (u.length + 1) :=
      Nat.choose_succ_succ (u.length + (v.length + 1)) u.length
    rw [hlen1, hlen2, hchoose]
    push_cast
    ring

/-- Exponential Chen signature of a linear segment `x : α → K`:
    `segmentSig x w = wordProd x w / |w|!`. -/
def segmentSig {K : Type*} [Field K] (x : α → K) (w : List α) : K :=
  wordProd x w / (Nat.factorial w.length : K)

/-- **Every linear segment signature is shuffle-group-like (`Δ_sh(S_x) = S_x ⊗ S_x`):**
    over `[Field K] [CharZero K]`, `segmentSig x` satisfies `IsShuffleGroupLike`. -/
theorem isShuffleGroupLike_segmentSig {K : Type*} [Field K] [CharZero K] (x : α → K) :
    IsShuffleGroupLike (segmentSig x) := by
  refine ⟨by simp [segmentSig, wordProd], fun u v => ?_⟩
  have hlen_sh : ∀ w ∈ shuffles u v, w.length = u.length + v.length := by
    intro w hw
    have aux : ∀ (p q : List α) (z : List α), z ∈ shuffles p q → z.length = p.length + q.length := by
      intro p
      induction p with
      | nil => intro q z hz; simp [shuffles] at hz; subst hz; simp
      | cons a p ihp =>
        intro q
        induction q with
        | nil => intro z hz; simp [shuffles] at hz; subst hz; simp
        | cons b q ihq =>
          intro z hz
          simp only [shuffles, List.mem_append, List.mem_map] at hz
          rcases hz with ⟨z', hz', rfl⟩ | ⟨z', hz', rfl⟩
          · have := ihp (b :: q) z' hz'; simp at this ⊢; omega
          · have := ihq z' hz'; simp at this ⊢; omega
    exact aux u v w hw
  have hmap : (shuffles u v).map (segmentSig x) =
      (shuffles u v).map (fun w => (Nat.factorial (u.length + v.length) : K)⁻¹ * wordProd x w) := by
    refine List.map_congr_left fun w hw => ?_
    rw [segmentSig, hlen_sh w hw, div_eq_inv_mul]
  unfold shuffleEval
  rw [hmap, list_map_sum_const_mul]
  change (Nat.factorial (u.length + v.length) : K)⁻¹ * shuffleEval (wordProd x) u v = _
  rw [shuffleEval_wordProd x u v, segmentSig, segmentSig]
  have hfu : (Nat.factorial u.length : K) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _)
  have hfv : (Nat.factorial v.length : K) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _)
  have hfuv : (Nat.factorial (u.length + v.length) : K) ≠ 0 :=
    Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _)
  have hcho := Nat.choose_mul_factorial_mul_factorial (Nat.le_add_right u.length v.length)
  rw [Nat.add_sub_cancel_left] at hcho
  have hchoK : (Nat.choose (u.length + v.length) u.length : K) *
      (Nat.factorial u.length : K) * (Nat.factorial v.length : K) =
      (Nat.factorial (u.length + v.length) : K) := by exact_mod_cast hcho
  field_simp
  linear_combination wordProd x u * wordProd x v * hchoK

/-- **Shuffle–Deconcatenation Hopf Bialgebra Theorem over `[CommRing R]`:**
    `⟨F ⋆ G, u ⊔⊔ v⟩ = ∑_{i=0}^{|u|} ∑_{j=0}^{|v|} ⟨F, u_{<i} ⊔⊔ v_{<j}⟩ · ⟨G, u_{≥i} ⊔⊔ v_{≥j}⟩`. -/
theorem shuffleEval_chenSigMul :
    ∀ (F G : List α → R) (u v : List α),
      shuffleEval (chenSigMul F G) u v =
        ∑ i ∈ Finset.range (u.length + 1),
          ∑ j ∈ Finset.range (v.length + 1),
            shuffleEval F (u.take i) (v.take j) * shuffleEval G (u.drop i) (v.drop j)
  | F, G, [], v => by simp [chenSigMul]
  | F, G, a :: u, [] => by simp [chenSigMul]
  | F, G, a :: u, b :: v => by
    rw [shuffleEval_cons_cons]
    have hconsF : ∀ x : α, sigShift x (chenSigMul F G) =
        fun w => F [] * sigShift x G w + chenSigMul (sigShift x F) G w := by
      intro x; funext w; exact chenSigMul_cons F G x w
    rw [hconsF a, hconsF b, shuffleEval_add, shuffleEval_add,
      shuffleEval_const_mul, shuffleEval_const_mul,
      shuffleEval_chenSigMul (sigShift a F) G u (b :: v),
      shuffleEval_chenSigMul (sigShift b F) G (a :: u) v]
    have hsum1 :
        (∑ i ∈ Finset.range (u.length + 1),
          ∑ j ∈ Finset.range ((b :: v).length + 1),
            shuffleEval (sigShift a F) (u.take i) ((b :: v).take j) *
              shuffleEval G (u.drop i) ((b :: v).drop j)) =
        (∑ i ∈ Finset.range (u.length + 1),
          F (a :: u.take i) * shuffleEval G (u.drop i) (b :: v)) +
        (∑ i ∈ Finset.range (u.length + 1),
          ∑ j ∈ Finset.range (v.length + 1),
            shuffleEval (sigShift a F) (u.take i) (b :: v.take j) *
              shuffleEval G (u.drop i) (v.drop j)) := by
      rw [← Finset.sum_add_distrib]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [List.length_cons, Finset.sum_range_succ']
      simp [sigShift, add_comm]
    have hsum2 :
        (∑ i ∈ Finset.range ((a :: u).length + 1),
          ∑ j ∈ Finset.range (v.length + 1),
            shuffleEval (sigShift b F) ((a :: u).take i) (v.take j) *
              shuffleEval G ((a :: u).drop i) (v.drop j)) =
        (∑ j ∈ Finset.range (v.length + 1),
          F (b :: v.take j) * shuffleEval G (a :: u) (v.drop j)) +
        (∑ i ∈ Finset.range (u.length + 1),
          ∑ j ∈ Finset.range (v.length + 1),
            shuffleEval (sigShift b F) (a :: u.take i) (v.take j) *
              shuffleEval G (u.drop i) (v.drop j)) := by
      rw [List.length_cons, Finset.sum_range_succ']
      simp only [List.take_zero, List.drop_zero, shuffleEval_nil_left, sigShift,
        List.take_succ_cons, List.drop_succ_cons]
      ring
    rw [hsum1, hsum2]
    have hrhs_outer :
        (∑ i ∈ Finset.range ((a :: u).length + 1),
          ∑ j ∈ Finset.range ((b :: v).length + 1),
            shuffleEval F ((a :: u).take i) ((b :: v).take j) *
              shuffleEval G ((a :: u).drop i) ((b :: v).drop j)) =
        (F [] * shuffleEval G (a :: u) (b :: v) +
          ∑ j ∈ Finset.range (v.length + 1),
            F (b :: v.take j) * shuffleEval G (a :: u) (v.drop j)) +
        ((∑ i ∈ Finset.range (u.length + 1),
            F (a :: u.take i) * shuffleEval G (u.drop i) (b :: v)) +
          ∑ i ∈ Finset.range (u.length + 1),
            ∑ j ∈ Finset.range (v.length + 1),
              (shuffleEval (sigShift a F) (u.take i) (b :: v.take j) +
               shuffleEval (sigShift b F) (a :: u.take i) (v.take j)) *
                shuffleEval G (u.drop i) (v.drop j)) := by
      rw [List.length_cons, Finset.sum_range_succ']
      simp only [List.take_zero, List.drop_zero, List.take_succ_cons, List.drop_succ_cons,
        shuffleEval_nil_left]
      have hr0 :
          (∑ j ∈ Finset.range ((b :: v).length + 1),
            F ((b :: v).take j) * shuffleEval G (a :: u) ((b :: v).drop j)) =
          F [] * shuffleEval G (a :: u) (b :: v) +
            ∑ j ∈ Finset.range (v.length + 1),
              F (b :: v.take j) * shuffleEval G (a :: u) (v.drop j) := by
        rw [List.length_cons, Finset.sum_range_succ']
        simp [add_comm]
      have hr1 :
          (∑ i ∈ Finset.range (u.length + 1),
            ∑ j ∈ Finset.range ((b :: v).length + 1),
              shuffleEval F (a :: u.take i) ((b :: v).take j) *
                shuffleEval G (u.drop i) ((b :: v).drop j)) =
          (∑ i ∈ Finset.range (u.length + 1),
            F (a :: u.take i) * shuffleEval G (u.drop i) (b :: v)) +
          ∑ i ∈ Finset.range (u.length + 1),
            ∑ j ∈ Finset.range (v.length + 1),
              (shuffleEval (sigShift a F) (u.take i) (b :: v.take j) +
               shuffleEval (sigShift b F) (a :: u.take i) (v.take j)) *
                shuffleEval G (u.drop i) (v.drop j) := by
        rw [← Finset.sum_add_distrib]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [List.length_cons, Finset.sum_range_succ']
        simp [shuffleEval_cons_cons, add_comm]
      rw [hr0, hr1]
      ring
    rw [hrhs_outer, shuffleEval_cons_cons G a b u v]
    simp only [add_mul, Finset.sum_add_distrib]
    ring

/-- **Chen Group-Like Path-Concatenation Theorem (`Δ_sh(S₂ ⋆ S₁) = (S₂ ⋆ S₁) ⊗ (S₂ ⋆ S₁)`):**
    the deconcatenation product of two shuffle-group-like signatures is again shuffle-group-like. -/
theorem IsShuffleGroupLike.chenSigMul {S₂ S₁ : List α → R}
    (h₂ : IsShuffleGroupLike S₂) (h₁ : IsShuffleGroupLike S₁) :
    IsShuffleGroupLike (ChenMultiplicativeIntegralBridge.chenSigMul S₂ S₁) := by
  refine ⟨by simp [ChenMultiplicativeIntegralBridge.chenSigMul, h₂.1, h₁.1], fun u v => ?_⟩
  rw [shuffleEval_chenSigMul]
  simp_rw [h₂.2, h₁.2]
  unfold ChenMultiplicativeIntegralBridge.chenSigMul
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun j _ => by ring

/-- Time-ordered Chen signature of a piecewise-linear path `[x₁, …, x_N]` of segment covectors. -/
def piecewiseLinearSig {K : Type*} [Field K] : List (α → K) → (List α → K)
  | [] => chenSigOne
  | x :: xs => chenSigMul (piecewiseLinearSig xs) (segmentSig x)

/-- Path-concatenation homomorphism `J(γ₁ ++ γ₂) = J(γ₂) ⋆ J(γ₁)` for piecewise-linear Chen signatures. -/
theorem piecewiseLinearSig_append {K : Type*} [Field K] (xs₁ xs₂ : List (α → K)) :
    piecewiseLinearSig (xs₁ ++ xs₂) =
      chenSigMul (piecewiseLinearSig xs₂) (piecewiseLinearSig xs₁) := by
  induction xs₁ with
  | nil =>
    funext w
    exact (mul_chenSigOne (piecewiseLinearSig xs₂) w).symm
  | cons x xs ih =>
    funext w
    simp only [List.cons_append, piecewiseLinearSig, ih]
    exact chenSigMul_assoc (piecewiseLinearSig xs₂) (piecewiseLinearSig xs) (segmentSig x) w

/-- **Every piecewise-linear path Chen signature is group-like (`Δ_sh(J(γ)) = J(γ) ⊗ J(γ)`).** -/
theorem isShuffleGroupLike_piecewiseLinear {K : Type*} [Field K] [CharZero K]
    (xs : List (α → K)) : IsShuffleGroupLike (piecewiseLinearSig xs) := by
  induction xs with
  | nil => exact isShuffleGroupLike_one
  | cons x xs ih => exact ih.chenSigMul (isShuffleGroupLike_segmentSig x)

end ChenShuffleCoalgebra

/-! ## §3. Picard Contraction & Discrete Grönwall `O(1/N)` Bound for `N`-Step Ordered Products -/

section PicardAndGronwall

variable {A : Type*} [NormedRing A] [NormedAlgebra ℝ A] [CompleteSpace A] [NormOneClass A]

/-- `U` is a fundamental solution of the linear matrix/algebra ODE `U'(t) = X(t) U(t)` on `[0, 1]`
    with `U(0) = 1`. -/
def IsLinearFundSol (X U : ℝ → A) : Prop :=
  U 0 = 1 ∧ ∀ t ∈ Icc (0 : ℝ) 1, HasDerivWithinAt U (X t * U t) (Icc 0 1) t

omit [CompleteSpace A] [NormOneClass A] in
lemma IsLinearFundSol.continuousOn {X U : ℝ → A} (hU : IsLinearFundSol X U) :
    ContinuousOn U (Icc 0 1) :=
  fun t ht => (hU.2 t ht).continuousWithinAt

omit [CompleteSpace A] [NormOneClass A] in
lemma hasDerivWithinAt_Ici_of_Icc_zero_one {f : ℝ → A} {f' : A} {t : ℝ} (ht : t ∈ Ico (0 : ℝ) 1)
    (h : HasDerivWithinAt f f' (Icc 0 1) t) : HasDerivWithinAt f f' (Ici t) t := by
  have hmem : Icc (0 : ℝ) 1 ∈ nhdsWithin t (Ici t) :=
    Filter.mem_of_superset (Icc_mem_nhdsGE ht.2) (Icc_subset_Icc_left ht.1)
  exact (hasDerivWithinAt_inter' hmem).1 (h.mono inter_subset_right)

omit [CompleteSpace A] [NormOneClass A] in
/-- **Grönwall Uniqueness of the Fundamental Solution** on `[0, 1]`. -/
theorem IsLinearFundSol.eqOn {X U₁ U₂ : ℝ → A} (hXc : ContinuousOn X (Icc 0 1))
    (hU₁ : IsLinearFundSol X U₁) (hU₂ : IsLinearFundSol X U₂) :
    EqOn U₁ U₂ (Icc 0 1) := by
  obtain ⟨C, hC⟩ := (isCompact_Icc (a := (0 : ℝ)) (b := 1)).exists_bound_of_continuousOn hXc
  have hlip : ∀ t ∈ Ico (0 : ℝ) 1,
      LipschitzOnWith C.toNNReal (fun y : A => X t * y) (univ : Set A) := by
    intro t ht
    refine (LipschitzWith.of_dist_le_mul fun x y => ?_).lipschitzOnWith
    rw [dist_eq_norm, dist_eq_norm, ← mul_sub]
    calc ‖X t * (x - y)‖ ≤ ‖X t‖ * ‖x - y‖ := norm_mul_le _ _
      _ ≤ C.toNNReal * ‖x - y‖ := mul_le_mul_of_nonneg_right
          ((hC t (Ico_subset_Icc_self ht)).trans (Real.le_coe_toNNReal C)) (norm_nonneg _)
  exact ODE_solution_unique_of_mem_Icc_right (v := fun t y => X t * y) (s := fun _ => univ) hlip
    hU₁.continuousOn
    (fun t ht => hasDerivWithinAt_Ici_of_Icc_zero_one ht (hU₁.2 t (Ico_subset_Icc_self ht)))
    (fun _ _ => trivial)
    hU₂.continuousOn
    (fun t ht => hasDerivWithinAt_Ici_of_Icc_zero_one ht (hU₂.2 t (Ico_subset_Icc_self ht)))
    (fun _ _ => trivial)
    (hU₁.1.trans hU₂.1.symm)

/-- **Picard integral operator** `(picardOp X Φ)(t) = 1 + ∫_0^t X(s) Φ(s) ds`. -/
noncomputable def picardOp (X Φ : ℝ → A) (t : ℝ) : A :=
  1 + ∫ s in (0 : ℝ)..t, X s * Φ s

omit [CompleteSpace A] [NormOneClass A] in
/-- **Picard Cauchy contraction bound on `[0, t]`:**
    `‖picardOp X Φ₁ t - picardOp X Φ₂ t‖ ≤ M * t * B` whenever `‖X s‖ ≤ M` and `‖Φ₁ s - Φ₂ s‖ ≤ B`. -/
theorem norm_picardOp_sub_le {X Φ₁ Φ₂ : ℝ → A} {t M B : ℝ}
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1) (hM0 : 0 ≤ M)
    (hXc : ContinuousOn X (Icc 0 1))
    (hΦ₁ : ContinuousOn Φ₁ (Icc 0 1)) (hΦ₂ : ContinuousOn Φ₂ (Icc 0 1))
    (hX : ∀ s ∈ Icc (0 : ℝ) 1, ‖X s‖ ≤ M)
    (hΦ : ∀ s ∈ Icc (0 : ℝ) t, ‖Φ₁ s - Φ₂ s‖ ≤ B) :
    ‖picardOp X Φ₁ t - picardOp X Φ₂ t‖ ≤ M * t * B := by
  have hsub : Icc (0 : ℝ) t ⊆ Icc 0 1 := Icc_subset_Icc le_rfl ht1
  have hi1 : IntervalIntegrable (fun s => X s * Φ₁ s) MeasureTheory.volume 0 t :=
    ((hXc.mono hsub).mul (hΦ₁.mono hsub)).intervalIntegrable_of_Icc ht0
  have hi2 : IntervalIntegrable (fun s => X s * Φ₂ s) MeasureTheory.volume 0 t :=
    ((hXc.mono hsub).mul (hΦ₂.mono hsub)).intervalIntegrable_of_Icc ht0
  have heq : picardOp X Φ₁ t - picardOp X Φ₂ t = ∫ s in (0 : ℝ)..t, X s * (Φ₁ s - Φ₂ s) := by
    unfold picardOp
    rw [add_sub_add_left_eq_sub, ← intervalIntegral.integral_sub hi1 hi2]
    congr 1; funext s; rw [mul_sub]
  rw [heq]
  have hbd : ∀ s ∈ uIoc (0 : ℝ) t, ‖X s * (Φ₁ s - Φ₂ s)‖ ≤ M * B := by
    intro s hs
    rw [uIoc_of_le ht0] at hs
    have hst : s ∈ Icc (0 : ℝ) t := ⟨hs.1.le, hs.2⟩
    calc ‖X s * (Φ₁ s - Φ₂ s)‖ ≤ ‖X s‖ * ‖Φ₁ s - Φ₂ s‖ := norm_mul_le _ _
      _ ≤ M * B := mul_le_mul (hX s (hsub hst)) (hΦ s hst) (norm_nonneg _) hM0
  calc ‖∫ s in (0 : ℝ)..t, X s * (Φ₁ s - Φ₂ s)‖
      ≤ (M * B) * |t - 0| := intervalIntegral.norm_integral_le_of_norm_le_const hbd
    _ = M * t * B := by rw [sub_zero, abs_of_nonneg ht0]; ring

/-- Uniform partition point `t_k = k / N` on `[0, 1]`. -/
noncomputable def meshPt (N k : ℕ) : ℝ := (k : ℝ) / (N : ℝ)

/-- Partial `k`-step time-ordered Euler–Riemann product `∏_{j=1}^k (1 + ∫_{t_{j-1}}^{t_j} X(s) ds)`. -/
noncomputable def eulerOrderedStep (X : ℝ → A) (N : ℕ) : ℕ → A
  | 0 => 1
  | k + 1 => (1 + ∫ s in (meshPt N k)..(meshPt N (k + 1)), X s) * eulerOrderedStep X N k

/-- Full `N`-step time-ordered multiplicative integral `∏_{j=1}^N (1 + ∫_{(j-1)/N}^{j/N} X(s) ds)`. -/
noncomputable def eulerOrderedProd (X : ℝ → A) (N : ℕ) : A :=
  eulerOrderedStep X N N

omit [CompleteSpace A] in
/-- Grönwall norm growth bound `‖U(t)‖ ≤ exp(M t)` for a fundamental solution `U' = X U`, `U(0) = 1`. -/
theorem isFundSol_norm_le_exp {X U : ℝ → A} (hU : IsLinearFundSol X U) {M : ℝ}
    (hX : ∀ t ∈ Icc (0 : ℝ) 1, ‖X t‖ ≤ M) {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) :
    ‖U t‖ ≤ Real.exp (M * t) := by
  have hbound := norm_le_gronwallBound_of_norm_deriv_right_le
    (f := U) (f' := fun s => X s * U s) (δ := 1) (K := M) (ε := 0) (a := 0) (b := 1)
    hU.continuousOn
    (fun s hs => hasDerivWithinAt_Ici_of_Icc_zero_one hs (hU.2 s (Ico_subset_Icc_self hs)))
    (by rw [hU.1, norm_one])
    (fun s hs => by
      rw [add_zero]
      calc ‖X s * U s‖ ≤ ‖X s‖ * ‖U s‖ := norm_mul_le _ _
        _ ≤ M * ‖U s‖ := mul_le_mul_of_nonneg_right (hX s (Ico_subset_Icc_self hs)) (norm_nonneg _))
    t ht
  simp only [gronwallBound, sub_zero, one_mul] at hbound
  split_ifs at hbound with hM0
  · subst hM0; simpa using hbound
  · simpa using hbound

/-- Local single-step `O(1/N²)` truncation bound for `U' = X U` on `[k/N, (k+1)/N]`. -/
theorem norm_isFundSol_step_truncation_le {X U : ℝ → A} (hXc : ContinuousOn X (Icc 0 1))
    (hU : IsLinearFundSol X U) {M : ℝ} (hM0 : 0 ≤ M) (hX : ∀ t ∈ Icc (0 : ℝ) 1, ‖X t‖ ≤ M)
    {N k : ℕ} (hk : k < N) :
    ‖U (meshPt N (k + 1)) -
        (1 + ∫ s in (meshPt N k)..(meshPt N (k + 1)), X s) * U (meshPt N k)‖ ≤
      M ^ 2 * Real.exp M / (N : ℝ) ^ 2 := by
  have hNpos : (0 : ℝ) < N := Nat.cast_pos.mpr (Nat.zero_lt_of_lt hk)
  set a := meshPt N k
  set b := meshPt N (k + 1)
  have hab_eq : b - a = 1 / (N : ℝ) := by
    simp only [a, b, meshPt]; push_cast; ring
  have hab : a ≤ b := by
    have hba : (0 : ℝ) ≤ b - a := by rw [hab_eq]; positivity
    linarith
  have ha0 : 0 ≤ a := by simp only [a, meshPt]; positivity
  have hb1 : b ≤ 1 := by
    simp only [b, meshPt]
    rw [div_le_one hNpos]
    exact_mod_cast Nat.succ_le_of_lt hk
  have hsub : Icc a b ⊆ Icc (0 : ℝ) 1 := Icc_subset_Icc ha0 hb1
  have hXUc : ContinuousOn (fun s => X s * U s) (Icc a b) :=
    (hXc.mono hsub).mul (hU.continuousOn.mono hsub)
  have hftc : ∫ s in a..b, X s * U s = U b - U a := by
    refine intervalIntegral.integral_eq_sub_of_hasDeriv_right ?_ ?_
      (hXUc.intervalIntegrable_of_Icc (μ := MeasureTheory.volume) hab)
    · rw [uIcc_of_le hab]; exact hU.continuousOn.mono hsub
    · intro x hx
      rw [min_eq_left hab, max_eq_right hab] at hx
      have hx01 : x ∈ Ico (0 : ℝ) 1 := ⟨ha0.trans hx.1.le, hx.2.trans_le hb1⟩
      exact (hasDerivWithinAt_Ici_of_Icc_zero_one hx01 (hU.2 x (Ico_subset_Icc_self hx01))).mono
        Ioi_subset_Ici_self
  let R_Ua : A →L[ℝ] A := (ContinuousLinearMap.mul ℝ A).flip (U a)
  have hR : (∫ s in a..b, X s) * U a = ∫ s in a..b, X s * U a := by
    have := (R_Ua.intervalIntegral_comp_comm
      ((hXc.mono hsub).intervalIntegrable_of_Icc (μ := MeasureTheory.volume) hab)).symm
    simpa [R_Ua] using this
  have hdiff_eq :
      U b - (1 + ∫ s in a..b, X s) * U a = ∫ s in a..b, X s * (U s - U a) := by
    rw [add_mul, one_mul, hR]
    have hsub_eq : U b - (U a + ∫ s in a..b, X s * U a) =
        (∫ s in a..b, X s * U s) - ∫ s in a..b, X s * U a := by
      rw [hftc]; abel
    have hi2 : IntervalIntegrable (fun s => X s * U a) MeasureTheory.volume a b :=
      ((hXc.mono hsub).mul continuousOn_const).intervalIntegrable_of_Icc
        (μ := MeasureTheory.volume) hab
    rw [hsub_eq, ← intervalIntegral.integral_sub
      (hXUc.intervalIntegrable_of_Icc (μ := MeasureTheory.volume) hab) hi2]
    congr 1; funext s; rw [mul_sub]
  rw [hdiff_eq]
  have hUbound : ∀ s ∈ Icc (0 : ℝ) 1, ‖X s * U s‖ ≤ M * Real.exp M := by
    intro s hs
    calc ‖X s * U s‖ ≤ ‖X s‖ * ‖U s‖ := norm_mul_le _ _
      _ ≤ M * Real.exp (M * s) := mul_le_mul (hX s hs) (isFundSol_norm_le_exp hU hX hs)
          (norm_nonneg _) hM0
      _ ≤ M * Real.exp M := by
          gcongr
          calc M * s ≤ M * 1 := mul_le_mul_of_nonneg_left hs.2 hM0
            _ = M := mul_one M
  have hmvt : ∀ s ∈ Icc a b, ‖U s - U a‖ ≤ M * Real.exp M / (N : ℝ) := by
    intro s hs
    have h1 := Convex.norm_image_sub_le_of_norm_hasDerivWithin_le
      (𝕜 := ℝ) (s := Icc (0 : ℝ) 1) (f := U) (f' := fun r => X r * U r)
      hU.2 hUbound (convex_Icc 0 1) (hsub ⟨le_rfl, hab⟩) (hsub hs)
    rw [Real.norm_eq_abs, abs_of_nonneg (sub_nonneg.mpr hs.1)] at h1
    have hsb : s - a ≤ 1 / (N : ℝ) := by linarith [hs.2, hab_eq]
    calc ‖U s - U a‖ ≤ M * Real.exp M * (s - a) := h1
      _ ≤ M * Real.exp M * (1 / (N : ℝ)) := mul_le_mul_of_nonneg_left hsb (by positivity)
      _ = M * Real.exp M / (N : ℝ) := by ring
  have hint_bound : ∀ s ∈ uIoc a b, ‖X s * (U s - U a)‖ ≤ M ^ 2 * Real.exp M / (N : ℝ) := by
    intro s hs
    rw [uIoc_of_le hab] at hs
    have hsab : s ∈ Icc a b := ⟨hs.1.le, hs.2⟩
    calc ‖X s * (U s - U a)‖ ≤ ‖X s‖ * ‖U s - U a‖ := norm_mul_le _ _
      _ ≤ M * (M * Real.exp M / (N : ℝ)) :=
          mul_le_mul (hX s (hsub hsab)) (hmvt s hsab) (norm_nonneg _) hM0
      _ = M ^ 2 * Real.exp M / (N : ℝ) := by ring
  calc ‖∫ s in a..b, X s * (U s - U a)‖
      ≤ (M ^ 2 * Real.exp M / (N : ℝ)) * |b - a| :=
        intervalIntegral.norm_integral_le_of_norm_le_const hint_bound
    _ = (M ^ 2 * Real.exp M / (N : ℝ)) * (1 / (N : ℝ)) := by
        rw [hab_eq, abs_of_pos (by positivity)]
    _ = M ^ 2 * Real.exp M / (N : ℝ) ^ 2 := by ring

/-- **Explicit Discrete Grönwall `O(1/N)` Error Bound for `N`-Step Ordered Products:**
    for any continuous `X : ℝ → A` on `[0, 1]` with `‖X(t)‖ ≤ M` (`M ≥ 0`) and fundamental
    solution `U` of `U'(t) = X(t) U(t)`, `U(0) = 1`, every `N ≥ 1` satisfies
    `‖U 1 - eulerOrderedProd X N‖ ≤ M² exp(2M) / N`. -/
theorem eulerOrderedProd_error_bound {X U : ℝ → A} (hXc : ContinuousOn X (Icc 0 1))
    (hU : IsLinearFundSol X U) {M : ℝ} (hM0 : 0 ≤ M) (hX : ∀ t ∈ Icc (0 : ℝ) 1, ‖X t‖ ≤ M)
    {N : ℕ} (hN : 1 ≤ N) :
    ‖U 1 - eulerOrderedProd X N‖ ≤ M ^ 2 * Real.exp (2 * M) / (N : ℝ) := by
  have hNpos : (0 : ℝ) < N := Nat.cast_pos.mpr (Nat.lt_of_lt_of_le Nat.zero_lt_one hN)
  set α := Real.exp (M / (N : ℝ))
  set τ := M ^ 2 * Real.exp M / (N : ℝ) ^ 2
  have hα1 : 1 ≤ α := Real.one_le_exp (by positivity)
  have hτ0 : 0 ≤ τ := by positivity
  have hstep_norm : ∀ k < N, ‖(1 : A) + ∫ s in (meshPt N k)..(meshPt N (k + 1)), X s‖ ≤ α := by
    intro k hk
    set a := meshPt N k
    set b := meshPt N (k + 1)
    have hab_eq : b - a = 1 / (N : ℝ) := by simp only [a, b, meshPt]; push_cast; ring
    have hab : a ≤ b := by
      have hba : (0 : ℝ) ≤ b - a := by rw [hab_eq]; positivity
      linarith
    have ha0 : 0 ≤ a := by simp only [a, meshPt]; positivity
    have hb1 : b ≤ 1 := by
      simp only [b, meshPt]; rw [div_le_one hNpos]; exact_mod_cast Nat.succ_le_of_lt hk
    have hsub : Icc a b ⊆ Icc (0 : ℝ) 1 := Icc_subset_Icc ha0 hb1
    have hbd : ∀ s ∈ uIoc a b, ‖X s‖ ≤ M := fun s hs => by
      rw [uIoc_of_le hab] at hs; exact hX s (hsub ⟨hs.1.le, hs.2⟩)
    calc ‖(1 : A) + ∫ s in a..b, X s‖
        ≤ ‖(1 : A)‖ + ‖∫ s in a..b, X s‖ := norm_add_le _ _
      _ ≤ 1 + M * |b - a| := by
          rw [norm_one]
          exact add_le_add_right (intervalIntegral.norm_integral_le_of_norm_le_const hbd) 1
      _ = 1 + M / (N : ℝ) := by rw [hab_eq, abs_of_pos (by positivity)]; ring
      _ ≤ α := by linarith [Real.add_one_le_exp (M / (N : ℝ))]
  have hrec : ∀ k ≤ N, ‖U (meshPt N k) - eulerOrderedStep X N k‖ ≤ (k : ℝ) * α ^ k * τ := by
    intro k
    induction k with
    | zero =>
      intro _
      simp [meshPt, eulerOrderedStep, hU.1]
    | succ k ih =>
      intro hkN
      have hk : k < N := Nat.lt_of_succ_le hkN
      set S := (1 : A) + ∫ s in (meshPt N k)..(meshPt N (k + 1)), X s
      have hsplit : U (meshPt N (k + 1)) - eulerOrderedStep X N (k + 1) =
          (U (meshPt N (k + 1)) - S * U (meshPt N k)) +
            S * (U (meshPt N k) - eulerOrderedStep X N k) := by
        simp only [eulerOrderedStep, S, mul_sub]
        abel
      have hα_pow : 1 ≤ α ^ (k + 1) := one_le_pow₀ hα1
      calc ‖U (meshPt N (k + 1)) - eulerOrderedStep X N (k + 1)‖
          ≤ ‖U (meshPt N (k + 1)) - S * U (meshPt N k)‖ +
              ‖S * (U (meshPt N k) - eulerOrderedStep X N k)‖ := by
            rw [hsplit]; exact norm_add_le _ _
        _ ≤ τ + ‖S‖ * ‖U (meshPt N k) - eulerOrderedStep X N k‖ :=
            add_le_add (norm_isFundSol_step_truncation_le hXc hU hM0 hX hk) (norm_mul_le _ _)
        _ ≤ τ + α * ((k : ℝ) * α ^ k * τ) :=
            add_le_add_right (mul_le_mul (hstep_norm k hk) (ih hk.le) (norm_nonneg _)
              (by positivity)) τ
        _ = 1 * τ + (k : ℝ) * α ^ (k + 1) * τ := by rw [pow_succ']; ring
        _ ≤ α ^ (k + 1) * τ + (k : ℝ) * α ^ (k + 1) * τ :=
            add_le_add_left (mul_le_mul_of_nonneg_right hα_pow hτ0) _
        _ = ((k + 1 : ℕ) : ℝ) * α ^ (k + 1) * τ := by push_cast; ring
  have hN_step := hrec N le_rfl
  have hmN : meshPt N N = 1 := div_self hNpos.ne'
  have hαN : α ^ N = Real.exp M := by
    simp only [α, ← Real.exp_nat_mul]
    congr 1; field_simp
  rw [hmN] at hN_step
  calc ‖U 1 - eulerOrderedProd X N‖
      ≤ (N : ℝ) * α ^ N * τ := hN_step
    _ = (N : ℝ) * Real.exp M * (M ^ 2 * Real.exp M / (N : ℝ) ^ 2) := by rw [hαN]
    _ = M ^ 2 * (Real.exp M * Real.exp M) / (N : ℝ) := by field_simp
    _ = M ^ 2 * Real.exp (2 * M) / (N : ℝ) := by rw [← Real.exp_add, two_mul]

/-- **Convergence of `N`-Step Ordered Products to the Continuous Multiplicative Integral:**
    `eulerOrderedProd X N → U 1` as `N → ∞` for any continuous connection `X : ℝ → A` on `[0, 1]`. -/
theorem tendsto_eulerOrderedProd_isFundSol {X U : ℝ → A} (hXc : ContinuousOn X (Icc 0 1))
    (hU : IsLinearFundSol X U) :
    Tendsto (eulerOrderedProd X) atTop (nhds (U 1)) := by
  obtain ⟨M₀, hM₀⟩ := (isCompact_Icc (a := (0 : ℝ)) (b := 1)).exists_bound_of_continuousOn hXc
  set M := max M₀ 0
  have hM0 : 0 ≤ M := le_max_right M₀ 0
  have hX : ∀ t ∈ Icc (0 : ℝ) 1, ‖X t‖ ≤ M := fun t ht => (hM₀ t ht).trans (le_max_left M₀ 0)
  rw [Metric.tendsto_atTop]
  intro ε hε
  set C := M ^ 2 * Real.exp (2 * M)
  obtain ⟨N₀, hN₀⟩ := exists_nat_gt (C / ε)
  refine ⟨max N₀ 1, fun N hN => ?_⟩
  have hN1 : 1 ≤ N := (le_max_right N₀ 1).trans hN
  have hNN₀ : (N₀ : ℝ) ≤ (N : ℝ) := Nat.cast_le.mpr ((le_max_left N₀ 1).trans hN)
  have hNpos : (0 : ℝ) < (N : ℝ) := Nat.cast_pos.mpr (Nat.lt_of_lt_of_le Nat.zero_lt_one hN1)
  rw [dist_comm, dist_eq_norm]
  calc ‖U 1 - eulerOrderedProd X N‖
      ≤ C / (N : ℝ) := eulerOrderedProd_error_bound hXc hU hM0 hX hN1
    _ < ε := by
        rw [div_lt_iff₀ hNpos]
        have hlt : C < (N₀ : ℝ) * ε := (div_lt_iff₀ hε).mp hN₀
        nlinarith

end PicardAndGronwall

/-! ## §4. Non-Commutative Matrix Substrate `FinMatObj R`, `matFrobHopf`, & `nablaEndo` Instantiation -/

section MatrixSubstrate

/- Lean 4.35 port: `FinMatObj` carriers (`(matObj R d).carrier = Fin d × Fin d`, the
monoidal-structure fields) are no longer unfolded at implicit transparency, which
breaks `rw`/`simp` against the section's own `stdVec`/`prodVec` lemmas. Mathlib uses
the same switch where a structure literal's projections must unfold. -/
set_option backward.isDefEq.respectTransparency false

/-- Objects of `FinMatObj R`: finite index types carrying `Fintype` and `DecidableEq`. -/
structure FinMatObj (R : Type*) where
  carrier : Type
  [fintype : Fintype carrier]
  [decEq : DecidableEq carrier]

attribute [instance] FinMatObj.fintype FinMatObj.decEq

/-- Morphisms `X ⟶ Y` in `FinMatObj R`: matrices `Matrix Y.carrier X.carrier R` acting on columns. -/
@[ext]
structure FinMatHom {R : Type*} (X Y : FinMatObj R) where
  mat : Matrix Y.carrier X.carrier R

section CategoryStructure

variable {R : Type*} [CommRing R]

instance : Category (FinMatObj R) where
  Hom X Y := FinMatHom X Y
  id _ := ⟨1⟩
  comp f g := ⟨g.mat * f.mat⟩
  id_comp f := FinMatHom.ext (Matrix.mul_one f.mat)
  comp_id f := FinMatHom.ext (Matrix.one_mul f.mat)
  assoc f g h := FinMatHom.ext (Matrix.mul_assoc h.mat g.mat f.mat).symm

@[ext]
lemma hom_ext {X Y : FinMatObj R} {f g : X ⟶ Y}
    (h : ∀ y x, f.mat y x = g.mat y x) : f = g :=
  FinMatHom.ext (Matrix.ext h)

@[simp] lemma mat_id (X : FinMatObj R) : (𝟙 X : X ⟶ X).mat = 1 := rfl
@[simp] lemma mat_comp {X Y Z : FinMatObj R} (f : X ⟶ Y) (g : Y ⟶ Z) :
    (f ≫ g).mat = g.mat * f.mat := rfl

instance (X Y : FinMatObj R) : AddCommGroup (X ⟶ Y) where
  add f g := ⟨f.mat + g.mat⟩
  add_assoc f g h := FinMatHom.ext (add_assoc f.mat g.mat h.mat)
  zero := ⟨0⟩
  zero_add f := FinMatHom.ext (zero_add f.mat)
  add_zero f := FinMatHom.ext (add_zero f.mat)
  nsmul n f := ⟨n • f.mat⟩
  nsmul_zero f := FinMatHom.ext (zero_smul ℕ f.mat)
  nsmul_succ n f := FinMatHom.ext (succ_nsmul f.mat n)
  neg f := ⟨-f.mat⟩
  sub f g := ⟨f.mat - g.mat⟩
  sub_eq_add_neg f g := FinMatHom.ext (sub_eq_add_neg f.mat g.mat)
  zsmul z f := ⟨z • f.mat⟩
  zsmul_zero' f := FinMatHom.ext (zero_smul ℤ f.mat)
  zsmul_succ' n f := FinMatHom.ext (SubNegMonoid.zsmul_succ' n f.mat)
  zsmul_neg' n f := FinMatHom.ext (SubNegMonoid.zsmul_neg' n f.mat)
  neg_add_cancel f := FinMatHom.ext (neg_add_cancel f.mat)
  add_comm f g := FinMatHom.ext (add_comm f.mat g.mat)

@[simp] lemma mat_add {X Y : FinMatObj R} (f g : X ⟶ Y) : (f + g).mat = f.mat + g.mat := rfl
@[simp] lemma mat_sub {X Y : FinMatObj R} (f g : X ⟶ Y) : (f - g).mat = f.mat - g.mat := rfl
@[simp] lemma mat_neg {X Y : FinMatObj R} (f : X ⟶ Y) : (-f).mat = -f.mat := rfl
@[simp] lemma mat_zero (X Y : FinMatObj R) : (0 : X ⟶ Y).mat = 0 := rfl

instance : Preadditive (FinMatObj R) where
  add_comp _ _ _ f f' g := FinMatHom.ext (by show g.mat * (f.mat + f'.mat) = _; exact Matrix.mul_add _ _ _)
  comp_add _ _ _ f g g' := FinMatHom.ext (by show (g.mat + g'.mat) * f.mat = _; exact Matrix.add_mul _ _ _)

instance (X Y : FinMatObj R) : Module R (X ⟶ Y) where
  smul r f := ⟨r • f.mat⟩
  one_smul f := FinMatHom.ext (one_smul R f.mat)
  mul_smul r s f := FinMatHom.ext (mul_smul r s f.mat)
  smul_zero r := FinMatHom.ext (smul_zero r)
  smul_add r f g := FinMatHom.ext (smul_add r f.mat g.mat)
  add_smul r s f := FinMatHom.ext (add_smul r s f.mat)
  zero_smul f := FinMatHom.ext (zero_smul R f.mat)

@[simp] lemma mat_smul {X Y : FinMatObj R} (r : R) (f : X ⟶ Y) : (r • f).mat = r • f.mat := rfl

instance : Linear R (FinMatObj R) where
  smul_comp _ _ _ r f g := FinMatHom.ext (by show g.mat * (r • f.mat) = _; exact Matrix.mul_smul _ _ _)
  comp_smul _ _ _ f r g := FinMatHom.ext (by show (r • g.mat) * f.mat = _; exact Matrix.smul_mul _ _ _)

/-- Tensor product of objects in `FinMatObj R`. -/
abbrev tensObj (X Y : FinMatObj R) : FinMatObj R := ⟨X.carrier × Y.carrier⟩

/-- Monoidal unit `PUnit.{1}` (`Unit`) in `FinMatObj R`. -/
abbrev unitObj (R : Type*) : FinMatObj R := ⟨PUnit.{1}⟩

/-- Kronecker product of matrix morphisms in `FinMatObj R`. -/
def tensHom {X Y X' Y' : FinMatObj R} (f : X ⟶ Y) (g : X' ⟶ Y') :
    tensObj X X' ⟶ tensObj Y Y' :=
  ⟨Matrix.of fun y x => f.mat y.1 x.1 * g.mat y.2 x.2⟩

/-- Permutation matrix morphism induced by an equivalence `e : X.carrier ≃ Y.carrier`. -/
def permHom {X Y : FinMatObj R} (e : X.carrier ≃ Y.carrier) : X ⟶ Y :=
  ⟨Matrix.of fun y x => if e x = y then 1 else 0⟩

lemma permHom_refl (X : FinMatObj R) : permHom (R := R) (Equiv.refl X.carrier) = 𝟙 X := by
  ext y x; simp [permHom, Matrix.one_apply, eq_comm]

lemma permHom_comp {X Y Z : FinMatObj R} (e₁ : X.carrier ≃ Y.carrier) (e₂ : Y.carrier ≃ Z.carrier) :
    permHom (R := R) e₁ ≫ permHom (R := R) e₂ = permHom (e₁.trans e₂) := by
  ext z x
  simp only [mat_comp, permHom, Matrix.mul_apply, Matrix.of_apply, Equiv.trans_apply]
  rw [Fintype.sum_eq_single (e₁ x)]
  · simp
  · intro y hy; simp [Ne.symm hy]

lemma tensHom_permHom {X Y X' Y' : FinMatObj R}
    (e₁ : X.carrier ≃ Y.carrier) (e₂ : X'.carrier ≃ Y'.carrier) :
    tensHom (permHom (R := R) e₁) (permHom (R := R) e₂) = permHom (e₁.prodCongr e₂) := by
  ext ⟨y, y'⟩ ⟨x, x'⟩
  simp only [tensHom, permHom, Matrix.of_apply]
  change (if e₁ x = y then (1 : R) else 0) * (if e₂ x' = y' then 1 else 0) =
    if (e₁ x, e₂ x') = (y, y') then 1 else 0
  by_cases h1 : e₁ x = y <;> by_cases h2 : e₂ x' = y' <;> simp [h1, h2]

/-- Isomorphism in `FinMatObj R` induced by a bijection of basis types. -/
def permIso {X Y : FinMatObj R} (e : X.carrier ≃ Y.carrier) : X ≅ Y where
  hom := permHom e
  inv := permHom e.symm
  hom_inv_id := by rw [permHom_comp, Equiv.self_trans_symm, permHom_refl]
  inv_hom_id := by rw [permHom_comp, Equiv.symm_trans_self, permHom_refl]

lemma permHom_comp_any {X Y Z : FinMatObj R} (e : X.carrier ≃ Y.carrier) (g : Y ⟶ Z) :
    permHom (R := R) e ≫ g = ⟨Matrix.of fun z x => g.mat z (e x)⟩ := by
  ext z x
  simp only [mat_comp, permHom, Matrix.mul_apply, Matrix.of_apply]
  rw [Fintype.sum_eq_single (e x)]
  · simp
  · intro y hy; simp [Ne.symm hy]

lemma any_comp_permHom {W X Y : FinMatObj R} (f : W ⟶ X) (e : X.carrier ≃ Y.carrier) :
    f ≫ permHom (R := R) e = ⟨Matrix.of fun y w => f.mat (e.symm y) w⟩ := by
  ext y w
  simp only [mat_comp, permHom, Matrix.mul_apply, Matrix.of_apply]
  rw [Fintype.sum_eq_single (e.symm y)]
  · simp
  · intro x hx
    have hne : e x ≠ y := fun he => hx (by rw [← he, e.symm_apply_apply])
    simp [hne]

instance : MonoidalCategoryStruct (FinMatObj R) where
  tensorObj := tensObj
  whiskerLeft X _ _ f := tensHom (𝟙 X) f
  whiskerRight f Y := tensHom f (𝟙 Y)
  tensorHom := tensHom
  tensorUnit := unitObj R
  associator X Y Z := permIso (Equiv.prodAssoc X.carrier Y.carrier Z.carrier)
  leftUnitor X := permIso (Equiv.punitProd X.carrier)
  rightUnitor X := permIso (Equiv.prodPUnit X.carrier)

instance : MonoidalCategory (FinMatObj R) where
  tensorHom_def {X₁ Y₁ X₂ Y₂} f g := by
    ext ⟨y₁, y₂⟩ ⟨x₁, x₂⟩
    symm
    change ∑ p : Y₁.carrier × X₂.carrier,
        ((1 : Matrix Y₁.carrier Y₁.carrier R) y₁ p.1 * g.mat y₂ p.2) *
          (f.mat p.1 x₁ * (1 : Matrix X₂.carrier X₂.carrier R) p.2 x₂) =
      f.mat y₁ x₁ * g.mat y₂ x₂
    rw [Fintype.sum_eq_single (y₁, x₂)]
    · simp [mul_comm]
    · intro p hp
      by_cases h1 : y₁ = p.1
      · have h2 : p.2 ≠ x₂ := fun h2 => hp (Prod.ext h1.symm h2)
        simp [Matrix.one_apply, h1, h2]
      · simp [Matrix.one_apply, h1]
  id_tensorHom_id X Y := by
    ext ⟨x₁, y₁⟩ ⟨x₂, y₂⟩
    change (1 : Matrix X.carrier X.carrier R) x₁ x₂ * (1 : Matrix Y.carrier Y.carrier R) y₁ y₂ =
      (1 : Matrix (X.carrier × Y.carrier) (X.carrier × Y.carrier) R) (x₁, y₁) (x₂, y₂)
    by_cases h1 : x₁ = x₂ <;> by_cases h2 : y₁ = y₂ <;> simp [Matrix.one_apply, h1, h2]
  tensorHom_comp_tensorHom f₁ f₂ g₁ g₂ := by
    ext ⟨z₁, z₂⟩ ⟨x₁, x₂⟩
    change ∑ p : _ × _, (g₁.mat z₁ p.1 * g₂.mat z₂ p.2) * (f₁.mat p.1 x₁ * f₂.mat p.2 x₂) =
      (∑ a, g₁.mat z₁ a * f₁.mat a x₁) * (∑ b, g₂.mat z₂ b * f₂.mat b x₂)
    rw [Fintype.sum_prod_type, Finset.sum_mul]
    refine Finset.sum_congr rfl fun a _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun b _ => by ring
  whiskerLeft_id X Y := by
    ext ⟨x₁, y₁⟩ ⟨x₂, y₂⟩
    change (1 : Matrix X.carrier X.carrier R) x₁ x₂ * (1 : Matrix Y.carrier Y.carrier R) y₁ y₂ =
      (1 : Matrix (X.carrier × Y.carrier) (X.carrier × Y.carrier) R) (x₁, y₁) (x₂, y₂)
    by_cases h1 : x₁ = x₂ <;> by_cases h2 : y₁ = y₂ <;> simp [Matrix.one_apply, h1, h2]
  id_whiskerRight X Y := by
    ext ⟨x₁, y₁⟩ ⟨x₂, y₂⟩
    change (1 : Matrix X.carrier X.carrier R) x₁ x₂ * (1 : Matrix Y.carrier Y.carrier R) y₁ y₂ =
      (1 : Matrix (X.carrier × Y.carrier) (X.carrier × Y.carrier) R) (x₁, y₁) (x₂, y₂)
    by_cases h1 : x₁ = x₂ <;> by_cases h2 : y₁ = y₂ <;> simp [Matrix.one_apply, h1, h2]
  associator_naturality f₁ f₂ f₃ := by
    change tensHom (tensHom f₁ f₂) f₃ ≫ permHom _ = permHom _ ≫ tensHom f₁ (tensHom f₂ f₃)
    rw [any_comp_permHom, permHom_comp_any]
    ext ⟨y₁, y₂, y₃⟩ ⟨⟨x₁, x₂⟩, x₃⟩
    change (f₁.mat y₁ x₁ * f₂.mat y₂ x₂) * f₃.mat y₃ x₃ =
      f₁.mat y₁ x₁ * (f₂.mat y₂ x₂ * f₃.mat y₃ x₃)
    ring
  leftUnitor_naturality f := by
    change tensHom (𝟙 _) f ≫ permHom _ = permHom _ ≫ f
    rw [any_comp_permHom, permHom_comp_any]
    ext y ⟨⟨⟩, x⟩
    change (1 : Matrix Unit Unit R) () () * f.mat y x = f.mat y x
    simp
  rightUnitor_naturality f := by
    change tensHom f (𝟙 _) ≫ permHom _ = permHom _ ≫ f
    rw [any_comp_permHom, permHom_comp_any]
    ext y ⟨x, ⟨⟩⟩
    change f.mat y x * (1 : Matrix Unit Unit R) () () = f.mat y x
    simp
  pentagon W X Y Z := by
    change tensHom (permHom _) (𝟙 Z) ≫ permHom _ ≫ tensHom (𝟙 W) (permHom _) =
      permHom _ ≫ permHom _
    rw [← permHom_refl Z, ← permHom_refl W, tensHom_permHom, tensHom_permHom,
      permHom_comp, permHom_comp, permHom_comp]
    rfl
  triangle X Y := by
    change permHom _ ≫ tensHom (𝟙 X) (permHom _) = tensHom (permHom _) (𝟙 Y)
    rw [← permHom_refl X, ← permHom_refl Y, tensHom_permHom, tensHom_permHom, permHom_comp]
    rfl

instance : BraidedCategory (FinMatObj R) where
  braiding X Y := permIso (Equiv.prodComm X.carrier Y.carrier)
  braiding_naturality_right X Y₁ Y₂ f := by
    change tensHom (𝟙 X) f ≫ permHom _ = permHom _ ≫ tensHom f (𝟙 X)
    rw [any_comp_permHom, permHom_comp_any]
    ext ⟨y, x₁⟩ ⟨x₂, y'⟩
    change (1 : Matrix X.carrier X.carrier R) x₁ x₂ * f.mat y y' =
      f.mat y y' * (1 : Matrix X.carrier X.carrier R) x₁ x₂
    ring
  braiding_naturality_left f Z := by
    change tensHom f (𝟙 Z) ≫ permHom _ = permHom _ ≫ tensHom (𝟙 Z) f
    rw [any_comp_permHom, permHom_comp_any]
    ext ⟨z₁, y⟩ ⟨x, z₂⟩
    change f.mat y x * (1 : Matrix Z.carrier Z.carrier R) z₁ z₂ =
      (1 : Matrix Z.carrier Z.carrier R) z₁ z₂ * f.mat y x
    ring
  hexagon_forward X Y Z := by
    change permHom _ ≫ permHom _ ≫ permHom _ =
      tensHom (permHom _) (𝟙 Z) ≫ permHom _ ≫ tensHom (𝟙 Y) (permHom _)
    rw [← permHom_refl Z, ← permHom_refl Y, tensHom_permHom, tensHom_permHom,
      permHom_comp, permHom_comp, permHom_comp, permHom_comp]
    rfl
  hexagon_reverse X Y Z := by
    change permHom _ ≫ permHom _ ≫ permHom _ =
      tensHom (𝟙 X) (permHom _) ≫ permHom _ ≫ tensHom (permHom _) (𝟙 Y)
    rw [← permHom_refl X, ← permHom_refl Y, tensHom_permHom, tensHom_permHom,
      permHom_comp, permHom_comp, permHom_comp, permHom_comp]
    rfl

/-! ### Basis-vector action API (`act`) for `FinMatObj R` -/

/-- Column-vector action of a morphism `f : X ⟶ Y` in `FinMatObj R`. -/
def act {X Y : FinMatObj R} (f : X ⟶ Y) (v : X.carrier → R) : Y.carrier → R :=
  Matrix.mulVec f.mat v

/-- Standard basis vector `e_x` of `X.carrier → R`. -/
def stdVec (X : FinMatObj R) (x : X.carrier) : X.carrier → R :=
  fun x' => if x' = x then 1 else 0

/-- Tensor product of column vectors. -/
def prodVec {X Y : FinMatObj R} (u : X.carrier → R) (v : Y.carrier → R) : (X ⊗ Y).carrier → R :=
  fun p => u p.1 * v p.2

lemma hom_eq_of_act_stdVec {X Y : FinMatObj R} {f g : X ⟶ Y}
    (h : ∀ x : X.carrier, act f (stdVec X x) = act g (stdVec X x)) : f = g := by
  ext y x
  have hx := congrFun (h x) y
  simp only [act, stdVec, Matrix.mulVec, dotProduct] at hx
  rw [Fintype.sum_eq_single x (fun x' hx' => by simp [hx']),
      Fintype.sum_eq_single x (fun x' hx' => by simp [hx'])] at hx
  simpa using hx

@[simp] lemma act_id {X : FinMatObj R} (v : X.carrier → R) : act (𝟙 X) v = v :=
  Matrix.one_mulVec v

@[simp] lemma act_comp {X Y Z : FinMatObj R} (f : X ⟶ Y) (g : Y ⟶ Z) (v : X.carrier → R) :
    act (f ≫ g) v = act g (act f v) :=
  (Matrix.mulVec_mulVec v g.mat f.mat).symm

@[simp] lemma act_zero_vec {X Y : FinMatObj R} (f : X ⟶ Y) : act f 0 = 0 :=
  Matrix.mulVec_zero f.mat

@[simp] lemma act_add_hom {X Y : FinMatObj R} (f g : X ⟶ Y) (v : X.carrier → R) :
    act (f + g) v = act f v + act g v :=
  Matrix.add_mulVec f.mat g.mat v

@[simp] lemma act_smul {X Y : FinMatObj R} (f : X ⟶ Y) (r : R) (v : X.carrier → R) :
    act f (r • v) = r • act f v :=
  Matrix.mulVec_smul f.mat r v

@[simp] lemma act_sum {X Y : FinMatObj R} {ι : Type*} (s : Finset ι)
    (f : X ⟶ Y) (v : ι → X.carrier → R) :
    act f (∑ i ∈ s, v i) = ∑ i ∈ s, act f (v i) := by
  funext y
  simp only [act, Finset.sum_apply, Matrix.mulVec, dotProduct, Finset.mul_sum]
  exact Finset.sum_comm

@[simp] lemma prodVec_zero_left {X Y : FinMatObj R} (v : Y.carrier → R) :
    prodVec (X := X) (Y := Y) 0 v = 0 := by funext p; simp [prodVec]

@[simp] lemma prodVec_zero_right {X Y : FinMatObj R} (u : X.carrier → R) :
    prodVec (X := X) (Y := Y) u 0 = 0 := by funext p; simp [prodVec]

@[simp] lemma prodVec_smul_left {X Y : FinMatObj R} (r : R)
    (u : X.carrier → R) (v : Y.carrier → R) :
    prodVec (X := X) (Y := Y) (r • u) v = r • prodVec (X := X) (Y := Y) u v := by
  funext p; simp [prodVec, mul_assoc]

@[simp] lemma prodVec_smul_right {X Y : FinMatObj R} (r : R)
    (u : X.carrier → R) (v : Y.carrier → R) :
    prodVec (X := X) (Y := Y) u (r • v) = r • prodVec (X := X) (Y := Y) u v := by
  funext p; simp [prodVec, mul_left_comm]

lemma prodVec_stdVec (X Y : FinMatObj R) (x : X.carrier) (y : Y.carrier) :
    prodVec (X := X) (Y := Y) (stdVec (R := R) X x) (stdVec (R := R) Y y) =
      stdVec (R := R) (X ⊗ Y) (x, y) := by
  funext ⟨x', y'⟩
  change (if x' = x then (1 : R) else 0) * (if y' = y then 1 else 0) =
    if (x', y') = (x, y) then 1 else 0
  by_cases h1 : x' = x <;> by_cases h2 : y' = y <;> simp [h1, h2]

@[simp] lemma stdVec_tensor (X Y : FinMatObj R) (p : (X ⊗ Y).carrier) :
    stdVec (R := R) (X ⊗ Y) p =
      prodVec (X := X) (Y := Y) (stdVec (R := R) X p.1) (stdVec (R := R) Y p.2) :=
  (prodVec_stdVec X Y p.1 p.2).symm

@[simp] lemma prodVec_sum_left {X Y : FinMatObj R} {ι : Type*} (s : Finset ι)
    (u : ι → X.carrier → R) (v : Y.carrier → R) :
    prodVec (X := X) (Y := Y) (∑ i ∈ s, u i) v = ∑ i ∈ s, prodVec (X := X) (Y := Y) (u i) v := by
  funext p; simp [prodVec, Finset.sum_mul]

@[simp] lemma prodVec_sum_right {X Y : FinMatObj R} {ι : Type*} (s : Finset ι)
    (u : X.carrier → R) (v : ι → Y.carrier → R) :
    prodVec (X := X) (Y := Y) u (∑ i ∈ s, v i) = ∑ i ∈ s, prodVec (X := X) (Y := Y) u (v i) := by
  funext p; simp [prodVec, Finset.mul_sum]

@[simp] lemma act_tensorHom {X Y X' Y' : FinMatObj R} (f : X ⟶ Y) (g : X' ⟶ Y')
    (u : X.carrier → R) (v : X'.carrier → R) :
    act (f ⊗ₘ g) (prodVec (X := X) (Y := X') u v) = prodVec (X := Y) (Y := Y') (act f u) (act g v) := by
  funext ⟨y, y'⟩
  simp only [act, prodVec, MonoidalCategoryStruct.tensorHom, tensHom, Matrix.mulVec,
    dotProduct, Matrix.of_apply]
  change ∑ p : X.carrier × X'.carrier, (f.mat y p.1 * g.mat y' p.2) * (u p.1 * v p.2) =
    (∑ a, f.mat y a * u a) * (∑ b, g.mat y' b * v b)
  rw [Fintype.sum_prod_type, Finset.sum_mul]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun b _ => by ring

@[simp] lemma act_whiskerLeft (X : FinMatObj R) {Y₁ Y₂ : FinMatObj R} (f : Y₁ ⟶ Y₂)
    (u : X.carrier → R) (v : Y₁.carrier → R) :
    act (X ◁ f) (prodVec (X := X) (Y := Y₁) u v) = prodVec (X := X) (Y := Y₂) u (act f v) := by
  change act (𝟙 X ⊗ₘ f) _ = _; rw [act_tensorHom, act_id]

@[simp] lemma act_whiskerRight {X₁ X₂ : FinMatObj R} (f : X₁ ⟶ X₂) (Y : FinMatObj R)
    (u : X₁.carrier → R) (v : Y.carrier → R) :
    act (f ▷ Y) (prodVec (X := X₁) (Y := Y) u v) = prodVec (X := X₂) (Y := Y) (act f u) v := by
  change act (f ⊗ₘ 𝟙 Y) _ = _; rw [act_tensorHom, act_id]

@[simp] lemma act_permHom_stdVec {X Y : FinMatObj R} (e : X.carrier ≃ Y.carrier) (x : X.carrier) :
    act (permHom (R := R) e) (stdVec X x) = stdVec Y (e x) := by
  funext y
  simp only [act, permHom, stdVec, Matrix.mulVec, dotProduct, Matrix.of_apply]
  rw [Fintype.sum_eq_single x (fun x' hx' => by simp [hx'])]
  by_cases h : e x = y
  · simp [h]
  · have h' : y ≠ e x := Ne.symm h
    simp [h, h']

@[simp] lemma act_assoc_hom_std (X Y Z : FinMatObj R)
    (x : X.carrier) (y : Y.carrier) (z : Z.carrier) :
    act (α_ X Y Z).hom
        (prodVec (X := X ⊗ Y) (Y := Z)
          (prodVec (X := X) (Y := Y) (stdVec (R := R) X x) (stdVec (R := R) Y y))
          (stdVec (R := R) Z z)) =
      prodVec (X := X) (Y := Y ⊗ Z) (stdVec (R := R) X x)
        (prodVec (X := Y) (Y := Z) (stdVec (R := R) Y y) (stdVec (R := R) Z z)) := by
  simp only [prodVec_stdVec]
  exact act_permHom_stdVec (X := (X ⊗ Y) ⊗ Z) (Y := X ⊗ (Y ⊗ Z))
    (Equiv.prodAssoc X.carrier Y.carrier Z.carrier) ((x, y), z)

@[simp] lemma act_assoc_inv_std (X Y Z : FinMatObj R)
    (x : X.carrier) (y : Y.carrier) (z : Z.carrier) :
    act (α_ X Y Z).inv
        (prodVec (X := X) (Y := Y ⊗ Z) (stdVec (R := R) X x)
          (prodVec (X := Y) (Y := Z) (stdVec (R := R) Y y) (stdVec (R := R) Z z))) =
      prodVec (X := X ⊗ Y) (Y := Z)
        (prodVec (X := X) (Y := Y) (stdVec (R := R) X x) (stdVec (R := R) Y y))
        (stdVec (R := R) Z z) := by
  simp only [prodVec_stdVec]
  exact act_permHom_stdVec (X := X ⊗ (Y ⊗ Z)) (Y := (X ⊗ Y) ⊗ Z)
    (Equiv.prodAssoc X.carrier Y.carrier Z.carrier).symm (x, (y, z))

@[simp] lemma act_braiding_hom_std (X Y : FinMatObj R) (x : X.carrier) (y : Y.carrier) :
    act (β_ X Y).hom (prodVec (X := X) (Y := Y) (stdVec (R := R) X x) (stdVec (R := R) Y y)) =
      prodVec (X := Y) (Y := X) (stdVec (R := R) Y y) (stdVec (R := R) X x) := by
  simp only [prodVec_stdVec]
  exact act_permHom_stdVec (X := X ⊗ Y) (Y := Y ⊗ X)
    (Equiv.prodComm X.carrier Y.carrier) (x, y)

@[simp] lemma act_leftUnitor_hom_std (X : FinMatObj R) (x : X.carrier) :
    act (λ_ X).hom
        (prodVec (X := 𝟙_ (FinMatObj R)) (Y := X)
          (stdVec (R := R) (𝟙_ (FinMatObj R)) ()) (stdVec (R := R) X x)) =
      stdVec (R := R) X x := by
  rw [prodVec_stdVec]
  exact act_permHom_stdVec (X := 𝟙_ (FinMatObj R) ⊗ X) (Y := X)
    (Equiv.punitProd X.carrier) ((), x)

@[simp] lemma act_leftUnitor_inv_std (X : FinMatObj R) (x : X.carrier) :
    act (λ_ X).inv (stdVec (R := R) X x) =
      prodVec (X := 𝟙_ (FinMatObj R)) (Y := X)
        (stdVec (R := R) (𝟙_ (FinMatObj R)) ()) (stdVec (R := R) X x) := by
  rw [prodVec_stdVec]
  exact act_permHom_stdVec (X := X) (Y := 𝟙_ (FinMatObj R) ⊗ X)
    (Equiv.punitProd X.carrier).symm x

@[simp] lemma act_rightUnitor_hom_std (X : FinMatObj R) (x : X.carrier) :
    act (ρ_ X).hom
        (prodVec (X := X) (Y := 𝟙_ (FinMatObj R))
          (stdVec (R := R) X x) (stdVec (R := R) (𝟙_ (FinMatObj R)) ())) =
      stdVec (R := R) X x := by
  rw [prodVec_stdVec]
  exact act_permHom_stdVec (X := X ⊗ 𝟙_ (FinMatObj R)) (Y := X)
    (Equiv.prodPUnit X.carrier) (x, ())

@[simp] lemma act_rightUnitor_inv_std (X : FinMatObj R) (x : X.carrier) :
    act (ρ_ X).inv (stdVec (R := R) X x) =
      prodVec (X := X) (Y := 𝟙_ (FinMatObj R))
        (stdVec (R := R) X x) (stdVec (R := R) (𝟙_ (FinMatObj R)) ()) := by
  rw [prodVec_stdVec]
  exact act_permHom_stdVec (X := X) (Y := X ⊗ 𝟙_ (FinMatObj R))
    (Equiv.prodPUnit X.carrier).symm x

/-! ### Non-commutative `d × d` matrix Frobenius–Hopf substrate `matFrobHopf` -/

/-- Matrix algebra object `Mat_d(R)` in `FinMatObj R`, of carrier `Fin d × Fin d` (rank `d²`). -/
def matObj (R : Type*) (d : ℕ) : FinMatObj R := ⟨Fin d × Fin d⟩

@[simp] lemma stdVec_matObj_apply {d : ℕ} (p q : (matObj R d).carrier) :
    stdVec (R := R) (matObj R d) p q = if q.1 = p.1 ∧ q.2 = p.2 then 1 else 0 := by
  rcases p with ⟨p1, p2⟩; rcases q with ⟨q1, q2⟩
  change (if (q1, q2) = (p1, p2) then (1 : R) else 0) = _
  simp

@[simp] lemma stdVec_unitObj_apply (u v : (𝟙_ (FinMatObj R)).carrier) :
    stdVec (R := R) (𝟙_ (FinMatObj R)) u v = 1 := by
  rcases u with ⟨⟩; rcases v with ⟨⟩; simp [stdVec]

/-- Matrix multiplication morphism `μ : Mat_d(R) ⊗ Mat_d(R) → Mat_d(R)`. -/
def matMul (d : ℕ) : (matObj R d ⊗ matObj R d) ⟶ matObj R d :=
  ⟨Matrix.of fun p q =>
    if q.1.1 = p.1 then if q.1.2 = q.2.1 then if q.2.2 = p.2 then 1 else 0 else 0 else 0⟩

/-- Identity matrix unit morphism `η : 𝟙 → Mat_d(R)`. -/
def matUnit (d : ℕ) : (𝟙_ (FinMatObj R)) ⟶ matObj R d :=
  ⟨Matrix.of fun p _ => if p.1 = p.2 then 1 else 0⟩

/-- Frobenius comultiplication `Δ(E_{ij}) = ∑_k E_{ik} ⊗ E_{kj}`. -/
def matComul (d : ℕ) : matObj R d ⟶ (matObj R d ⊗ matObj R d) :=
  ⟨Matrix.of fun q p =>
    if q.1.1 = p.1 then if q.1.2 = q.2.1 then if q.2.2 = p.2 then 1 else 0 else 0 else 0⟩

/-- Matrix trace counit / Frobenius form `ε(X) = ∫(X) = Tr(X)`. -/
def matCounit (d : ℕ) : matObj R d ⟶ (𝟙_ (FinMatObj R)) :=
  ⟨Matrix.of fun _ p => if p.1 = p.2 then 1 else 0⟩

/-- Matrix transpose antipode `S(E_{ij}) = E_{ji}`. -/
def matAntipode (d : ℕ) : matObj R d ⟶ matObj R d :=
  permHom (Equiv.prodComm (Fin d) (Fin d))

/-- Self-duality coevaluation `coev(1) = ∑_{a,b} E_{ab} ⊗ E_{ba}`. -/
def matCoev (d : ℕ) : (𝟙_ (FinMatObj R)) ⟶ (matObj R d ⊗ matObj R d) :=
  ⟨Matrix.of fun q _ => if q.1.1 = q.2.2 then if q.1.2 = q.2.1 then 1 else 0 else 0⟩

@[simp] lemma act_matMul {d : ℕ} (a b c e : Fin d) :
    act (matMul (R := R) d)
        (prodVec (X := matObj R d) (Y := matObj R d)
          (stdVec (matObj R d) (a, b)) (stdVec (matObj R d) (c, e))) =
      if b = c then stdVec (matObj R d) (a, e) else 0 := by
  rw [prodVec_stdVec]
  funext ⟨i, j⟩
  simp only [act, matMul, stdVec, Matrix.mulVec, dotProduct, Matrix.of_apply]
  change ∑ q : (Fin d × Fin d) × (Fin d × Fin d),
      (if q.1.1 = i then if q.1.2 = q.2.1 then if q.2.2 = j then (1 : R) else 0 else 0 else 0) *
        (if q = ((a, b), (c, e)) then 1 else 0) =
    (if b = c then fun x' : Fin d × Fin d => if x' = (a, e) then (1 : R) else 0 else 0) (i, j)
  rw [Fintype.sum_eq_single ((a, b), (c, e)) (fun q hq => by simp [hq])]
  by_cases hbc : b = c <;> by_cases hai : a = i <;> by_cases hej : e = j <;>
    simp [hbc, hai, hej, eq_comm]

@[simp] lemma act_matUnit {d : ℕ} :
    act (matUnit (R := R) d) (stdVec (𝟙_ (FinMatObj R)) ()) =
      ∑ i : Fin d, stdVec (matObj R d) (i, i) := by
  funext ⟨a, b⟩
  simp only [act, matUnit, Finset.sum_apply, stdVec_matObj_apply, stdVec_unitObj_apply,
    Matrix.mulVec, dotProduct, Matrix.of_apply, mul_one]
  dsimp only [MonoidalCategoryStruct.tensorUnit, unitObj]
  rw [Fintype.sum_unique]
  by_cases hab : a = b
  · subst hab
    rw [Fintype.sum_eq_single a (fun k hk => by simp [Ne.symm hk])]
    simp
  · simp only [hab, ↓reduceIte]
    symm
    exact Finset.sum_eq_zero fun k _ => by
      by_cases hak : a = k
      · subst hak; simp [Ne.symm hab]
      · simp [hak]

@[simp] lemma act_matComul {d : ℕ} (i j : Fin d) :
    act (matComul (R := R) d) (stdVec (matObj R d) (i, j)) =
      ∑ k : Fin d,
        prodVec (X := matObj R d) (Y := matObj R d)
          (stdVec (matObj R d) (i, k)) (stdVec (matObj R d) (k, j)) := by
  funext ⟨⟨a, b⟩, ⟨c, e⟩⟩
  simp only [act, matComul, prodVec, Finset.sum_apply, stdVec_matObj_apply, Matrix.mulVec,
    dotProduct, Matrix.of_apply]
  dsimp only [matObj]
  rw [Fintype.sum_eq_single (i, j) (fun p hp => by
    by_cases h1 : p.1 = i
    · have h2 : p.2 ≠ j := fun h2 => hp (Prod.ext h1 h2)
      simp [h1, h2]
    · simp [h1])]
  simp only [and_self, ↓reduceIte, mul_one]
  by_cases hbc : b = c
  · subst hbc
    rw [Fintype.sum_eq_single b (fun k hk => by simp [Ne.symm hk])]
    by_cases hai : a = i <;> by_cases hej : e = j <;> simp [hai, hej]
  · simp only [hbc, ↓reduceIte, ite_self]
    symm
    exact Finset.sum_eq_zero fun k _ => by
      by_cases hbk : b = k
      · subst hbk; have hcb : c ≠ b := Ne.symm hbc; simp [hcb]
      · simp [hbk]

@[simp] lemma act_matCounit {d : ℕ} (i j : Fin d) :
    act (matCounit (R := R) d) (stdVec (matObj R d) (i, j)) =
      if i = j then stdVec (𝟙_ (FinMatObj R)) () else 0 := by
  funext ⟨⟩
  simp only [act, matCounit, stdVec_matObj_apply, Matrix.mulVec, dotProduct, Matrix.of_apply]
  dsimp only [matObj]
  rw [Fintype.sum_eq_single (i, j) (fun p hp => by
    by_cases h1 : p.1 = i
    · have h2 : p.2 ≠ j := fun h2 => hp (Prod.ext h1 h2)
      simp [h1, h2]
    · simp [h1])]
  by_cases hij : i = j <;> simp [hij]

@[simp] lemma act_matAntipode {d : ℕ} (i j : Fin d) :
    act (matAntipode (R := R) d) (stdVec (matObj R d) (i, j)) = stdVec (matObj R d) (j, i) :=
  act_permHom_stdVec (X := matObj R d) (Y := matObj R d) (Equiv.prodComm (Fin d) (Fin d)) (i, j)

@[simp] lemma act_matCoev {d : ℕ} :
    act (matCoev (R := R) d) (stdVec (𝟙_ (FinMatObj R)) ()) =
      ∑ a : Fin d, ∑ b : Fin d,
        prodVec (X := matObj R d) (Y := matObj R d)
          (stdVec (matObj R d) (a, b)) (stdVec (matObj R d) (b, a)) := by
  funext ⟨⟨i, j⟩, ⟨k, l⟩⟩
  simp only [act, matCoev, prodVec, Finset.sum_apply, stdVec_matObj_apply, stdVec_unitObj_apply,
    Matrix.mulVec, dotProduct, Matrix.of_apply, mul_one]
  dsimp only [MonoidalCategoryStruct.tensorUnit, unitObj]
  rw [Fintype.sum_unique]
  by_cases h1 : i = l
  · subst h1
    by_cases h2 : j = k
    · subst h2
      rw [Fintype.sum_eq_single i (fun a ha => by
        exact Finset.sum_eq_zero fun b _ => by simp [Ne.symm ha])]
      rw [Fintype.sum_eq_single j (fun b hb => by simp [Ne.symm hb])]
      simp
    · simp only [↓reduceIte, h2]
      symm
      exact Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ => by
        by_cases hjb : j = b
        · subst hjb; have hkj : k ≠ j := Ne.symm h2; simp [hkj]
        · simp [hjb]
  · simp only [h1, ↓reduceIte]
    symm
    exact Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ => by
      by_cases hia : i = a
      · subst hia; have hli : l ≠ i := Ne.symm h1; simp [hli]
      · simp [hia]

/-- **Concrete `d × d` Matrix `FrobeniusHopfData` Substrate (`Mat_d(R)`):**
    non-commutative for `d ≥ 2`, with `frobeniusForm = counit` (`= Tr`) holding definitionally. -/
@[reducible]
def matFrobHopf (d : ℕ) : QOU.FrobeniusHopfData (FinMatObj R) where
  obj := matObj R d
  mul := matMul d
  unit := matUnit d
  comul := matComul d
  counit := matCounit d
  antipode := matAntipode d
  frobeniusForm := matCounit d
  coevaluation := matCoev d
  pairing_snake_left := by
    refine hom_eq_of_act_stdVec fun ⟨i, j⟩ => ?_
    simp only [act_comp, act_id, act_rightUnitor_inv_std, act_whiskerLeft, act_matCoev,
      prodVec_sum_right, act_sum, act_assoc_inv_std, act_whiskerRight, act_matMul]
    have hstep : ∀ a b : Fin d,
        act (λ_ (matObj R d)).hom
          (prodVec (X := 𝟙_ (FinMatObj R)) (Y := matObj R d)
            (act (matCounit d) (if j = a then stdVec (matObj R d) (i, b) else 0))
            (stdVec (matObj R d) (b, a))) =
          if j = a ∧ i = b then stdVec (matObj R d) (b, a) else 0 := by
      intro a b
      by_cases hja : j = a <;> by_cases hib : i = b <;> simp [hja, hib]
    simp_rw [hstep]
    rw [Fintype.sum_eq_single j (fun a ha => Finset.sum_eq_zero fun b _ => by simp [Ne.symm ha])]
    rw [Fintype.sum_eq_single i (fun b hb => by simp [Ne.symm hb])]
    simp
  pairing_snake_right := by
    refine hom_eq_of_act_stdVec fun ⟨i, j⟩ => ?_
    simp only [act_comp, act_id, act_leftUnitor_inv_std, act_whiskerRight, act_matCoev,
      prodVec_sum_left, act_sum, act_assoc_hom_std, act_whiskerLeft, act_matMul]
    have hstep : ∀ a b : Fin d,
        act (ρ_ (matObj R d)).hom
          (prodVec (X := matObj R d) (Y := 𝟙_ (FinMatObj R)) (stdVec (matObj R d) (a, b))
            (act (matCounit d) (if a = i then stdVec (matObj R d) (b, j) else 0))) =
          if a = i ∧ b = j then stdVec (matObj R d) (a, b) else 0 := by
      intro a b
      by_cases hai : a = i <;> by_cases hbj : b = j <;> simp [hai, hbj]
    simp_rw [hstep]
    rw [Fintype.sum_eq_single i (fun a ha => Finset.sum_eq_zero fun b _ => by simp [ha])]
    rw [Fintype.sum_eq_single j (fun b hb => by simp [hb])]
    simp
  frobenius_relation := by
    refine hom_eq_of_act_stdVec fun ⟨⟨a, b⟩, ⟨c, e⟩⟩ => ?_
    by_cases hbc : b = c
    · subst hbc; simp
    · simp [hbc]
  one_mul := by
    refine hom_eq_of_act_stdVec fun ⟨⟨⟩, ⟨a, b⟩⟩ => ?_
    simp_rw [stdVec_tensor, act_comp, act_whiskerRight, act_matUnit, prodVec_sum_left,
      act_sum, act_matMul, act_leftUnitor_hom_std]
    rw [Fintype.sum_eq_single a (fun k hk => by simp [hk])]
    simp
  mul_one := by
    refine hom_eq_of_act_stdVec fun ⟨⟨a, b⟩, ⟨⟩⟩ => ?_
    simp_rw [stdVec_tensor, act_comp, act_whiskerLeft, act_matUnit, prodVec_sum_right,
      act_sum, act_matMul, act_rightUnitor_hom_std]
    rw [Fintype.sum_eq_single b (fun k hk => by simp [Ne.symm hk])]
    simp
  mul_assoc := by
    refine hom_eq_of_act_stdVec fun ⟨⟨⟨a, b⟩, ⟨c, e⟩⟩, ⟨k, l⟩⟩ => ?_
    by_cases hbc : b = c <;> by_cases hek : e = k <;> simp [hbc, hek]
  counit_comul := by
    refine hom_eq_of_act_stdVec fun ⟨i, j⟩ => ?_
    simp only [act_comp, act_matComul, act_sum, act_whiskerRight, act_matCounit,
      act_leftUnitor_inv_std]
    rw [Fintype.sum_eq_single i (fun k hk => by simp [Ne.symm hk])]
    simp
  comul_counit := by
    refine hom_eq_of_act_stdVec fun ⟨i, j⟩ => ?_
    simp only [act_comp, act_matComul, act_sum, act_whiskerLeft, act_matCounit,
      act_rightUnitor_inv_std]
    rw [Fintype.sum_eq_single j (fun k hk => by simp [hk])]
    simp
  comul_assoc := by
    refine hom_eq_of_act_stdVec fun ⟨i, j⟩ => ?_
    simp only [act_comp, act_matComul, act_sum, act_whiskerLeft, act_whiskerRight,
      prodVec_sum_right, prodVec_sum_left, act_assoc_hom_std]
    rw [Finset.sum_comm]
  antipode_anti_mul := by
    refine hom_eq_of_act_stdVec fun ⟨⟨a, b⟩, ⟨c, e⟩⟩ => ?_
    by_cases hbc : b = c
    · subst hbc; simp
    · have hcb : c ≠ b := Ne.symm hbc; simp [hbc, hcb]
  antipode_anti_comul := by
    refine hom_eq_of_act_stdVec fun ⟨i, j⟩ => ?_
    simp only [act_comp, act_matAntipode, act_matComul, act_sum, act_braiding_hom_std, act_tensorHom]
  antipode_unit := by
    refine hom_eq_of_act_stdVec fun ⟨⟩ => ?_
    simp_rw [act_comp, act_matUnit, act_sum, act_matAntipode]
  antipode_counit := by
    refine hom_eq_of_act_stdVec fun ⟨i, j⟩ => ?_
    by_cases hij : i = j <;> simp [hij, eq_comm]
  antipode_involutive := by
    show matAntipode d ≫ matAntipode d = 𝟙 (matObj R d)
    unfold matAntipode
    rw [permHom_comp]
    have htr : (Equiv.prodComm (Fin d) (Fin d)).trans (Equiv.prodComm (Fin d) (Fin d)) =
        Equiv.refl ((matObj R d).carrier) := by ext ⟨i, j⟩ <;> rfl
    rw [htr]
    exact permHom_refl (matObj R d)
  antipode_frobeniusForm := by
    refine hom_eq_of_act_stdVec fun ⟨i, j⟩ => ?_
    by_cases hij : i = j <;> simp [hij, eq_comm]

/-- `frobeniusForm = counit` holds definitionally on `matFrobHopf d`. -/
@[simp] theorem matFrobHopf_frobeniusForm_eq_counit (d : ℕ) :
    (matFrobHopf (R := R) d).frobeniusForm = (matFrobHopf (R := R) d).counit := rfl

/-- Embed `M : Matrix (Fin d) (Fin d) R` as a generalized element `𝟙 ⟶ matObj R d`. -/
def ofMat {d : ℕ} (M : Matrix (Fin d) (Fin d) R) : (𝟙_ (FinMatObj R)) ⟶ matObj R d :=
  ⟨Matrix.of fun p _ => M p.1 p.2⟩

/-- Extract a scalar `R` from an endomorphism of the monoidal unit `𝟙 ⟶ 𝟙`. -/
def toScalar (s : (𝟙_ (FinMatObj R)) ⟶ (𝟙_ (FinMatObj R))) : R := s.mat () ()

@[simp] lemma ofMat_one (d : ℕ) : ofMat (1 : Matrix (Fin d) (Fin d) R) = (matFrobHopf d).unit := by
  ext ⟨i, j⟩ ⟨⟩; simp [ofMat, matUnit, Matrix.one_apply]

lemma act_ofMat {d : ℕ} (M : Matrix (Fin d) (Fin d) R) :
    act (ofMat M) (stdVec (𝟙_ (FinMatObj R)) ()) =
      ∑ a : Fin d, ∑ b : Fin d, M a b • stdVec (matObj R d) (a, b) := by
  funext ⟨i, j⟩
  simp only [act, ofMat, Finset.sum_apply, Pi.smul_apply, smul_eq_mul, stdVec_matObj_apply,
    stdVec_unitObj_apply, Matrix.mulVec, dotProduct, Matrix.of_apply, mul_one]
  dsimp only [MonoidalCategoryStruct.tensorUnit, unitObj]
  rw [Fintype.sum_unique]
  rw [Fintype.sum_eq_single i (fun a ha => Finset.sum_eq_zero fun b _ => by simp [Ne.symm ha])]
  rw [Fintype.sum_eq_single j (fun b hb => by simp [Ne.symm hb])]
  simp

/-- Convolution in `Hom(𝟙, matObj R d)` is matrix multiplication: `conv(ofMat M, ofMat N) = ofMat (M * N)`. -/
theorem matFrobHopf_conv_ofMat {d : ℕ} (M N : Matrix (Fin d) (Fin d) R) :
    Torsion.MassTraceIdentity.conv (matFrobHopf (R := R) d) (ofMat M) (ofMat N) = ofMat (M * N) := by
  refine hom_eq_of_act_stdVec fun ⟨⟩ => ?_
  change act ((λ_ (𝟙_ (FinMatObj R))).inv ≫ (ofMat M ⊗ₘ ofMat N) ≫ matMul d)
      (stdVec (𝟙_ (FinMatObj R)) ()) = _
  simp_rw [act_comp, act_leftUnitor_inv_std, act_tensorHom, act_ofMat,
    prodVec_sum_left, prodVec_sum_right, act_sum, prodVec_smul_left, prodVec_smul_right,
    act_smul, act_matMul]
  funext ⟨i, j⟩
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, Matrix.mul_apply, stdVec_matObj_apply]
  conv_rhs =>
    rw [Fintype.sum_eq_single i (fun a ha => Finset.sum_eq_zero fun b _ => by simp [Ne.symm ha])]
    rw [Fintype.sum_eq_single j (fun b hb => by simp [Ne.symm hb])]
  simp only [and_self, ↓reduceIte, mul_one]
  rw [Fintype.sum_eq_single i]
  · refine Finset.sum_congr rfl fun k _ => ?_
    rw [Fintype.sum_eq_single k]
    · rw [Fintype.sum_eq_single j]
      · simp
      · intro e he; simp [Ne.symm he]
    · intro c hc
      exact Finset.sum_eq_zero fun e _ => by
        have hkc : k ≠ c := Ne.symm hc
        simp [hkc]
  · intro a ha
    exact Finset.sum_eq_zero fun b _ => Finset.sum_eq_zero fun c _ => Finset.sum_eq_zero fun e _ => by
      by_cases hbc : b = c <;> simp [hbc, Ne.symm ha]

/-- Discrete holonomy `MassTraceIdentity.hol` on `matFrobHopf d` equals `ofMat` of `List.prod`. -/
theorem matFrobHopf_hol_eq_ofMat_prod {d : ℕ} (Ms : List (Matrix (Fin d) (Fin d) R)) :
    Torsion.MassTraceIdentity.hol (matFrobHopf (R := R) d) (Ms.map ofMat) = ofMat Ms.prod := by
  induction Ms with
  | nil => exact (ofMat_one d).symm
  | cons M Ms ih =>
    rw [List.map_cons, List.prod_cons,
      Torsion.MassTraceIdentity.hol_cons (matFrobHopf (R := R) d), ih,
      matFrobHopf_conv_ofMat]

/-- Evaluating `counit` (`= frobeniusForm`) on `ofMat M` recovers `Matrix.trace M`. -/
theorem toScalar_ofMat_counit {d : ℕ} (M : Matrix (Fin d) (Fin d) R) :
    toScalar (ofMat M ≫ (matFrobHopf (R := R) d).counit) = Matrix.trace M := by
  simp only [toScalar, ofMat, matCounit, mat_comp, Matrix.mul_apply,
    Matrix.of_apply, Matrix.trace, Matrix.diag]
  dsimp only [matObj]
  rw [Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Fintype.sum_eq_single i (fun j hj => by simp [Ne.symm hj])]
  simp

/-- **Concrete `MassTraceIdentity` Option-1 Theorem on `Mat_d(R)`:**
    `∫_A(Ψ ∘ hol(Ms)) = Tr(M₁ ⋯ M_k)` with `∫_A = ε` discharged automatically. -/
theorem matFrobHopf_frobeniusMass_eq_trace {d : ℕ} (Ms : List (Matrix (Fin d) (Fin d) R)) :
    toScalar (Torsion.MassTraceIdentity.hol (matFrobHopf (R := R) d) (Ms.map ofMat) ≫
      Torsion.MassTraceIdentity.massIntegrand (matFrobHopf (R := R) d) ≫
      (matFrobHopf (R := R) d).frobeniusForm) = Matrix.trace Ms.prod := by
  rw [Torsion.MassTraceIdentity.frobeniusForm_massIntegrand_hol_of_frobeniusForm_eq_counit
      (matFrobHopf (R := R) d) rfl,
    matFrobHopf_hol_eq_ofMat_prod, matFrobHopf_frobeniusForm_eq_counit, toScalar_ofMat_counit]

/-- Casimir element `c = coev ≫ mul` of `matFrobHopf d` equals `d • I_d`. -/
theorem matFrobHopf_casimir_eq {d : ℕ} :
    Torsion.MassTraceIdentity.casimir (matFrobHopf (R := R) d) =
      ofMat ((d : R) • (1 : Matrix (Fin d) (Fin d) R)) := by
  refine hom_eq_of_act_stdVec fun ⟨⟩ => ?_
  change act (matCoev d ≫ matMul d) (stdVec (𝟙_ (FinMatObj R)) ()) =
    act (ofMat ((d : R) • (1 : Matrix (Fin d) (Fin d) R))) (stdVec (𝟙_ (FinMatObj R)) ())
  rw [act_comp, act_matCoev, act_ofMat]
  simp_rw [act_sum, act_matMul]
  funext ⟨i, j⟩
  simp only [↓reduceIte, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
    Finset.sum_apply, Pi.smul_apply, nsmul_eq_mul, smul_eq_mul,
    Matrix.smul_apply, Matrix.one_apply, stdVec_matObj_apply]
  by_cases hij : i = j
  · subst hij
    rw [Fintype.sum_eq_single i (fun a ha => by simp [Ne.symm ha]),
        Fintype.sum_eq_single i (fun a ha => Finset.sum_eq_zero fun b _ => by simp [Ne.symm ha])]
    rw [Fintype.sum_eq_single i (fun b hb => by simp [Ne.symm hb])]
    simp
  · rw [Finset.sum_eq_zero (fun a _ => by
          by_cases ha : i = a
          · subst ha; simp [Ne.symm hij]
          · simp [ha]),
        Finset.sum_eq_zero (fun a _ => Finset.sum_eq_zero fun b _ => by
          by_cases ha : i = a
          · subst ha
            by_cases hb : j = b
            · subst hb; simp [hij]
            · simp [hb]
          · simp [ha])]

/-- **Concrete `MassTraceIdentity` Regular-Trace Theorem on `Mat_d(R)`:**
    `tr_{End(A)}(L_{hol(Ms)} ∘ Ψ) = d · Tr(M₁ ⋯ M_k)`. -/
theorem matFrobHopf_leftTrace_eq_dim_mul_trace {d : ℕ} (Ms : List (Matrix (Fin d) (Fin d) R)) :
    toScalar ((matFrobHopf (R := R) d).leftTrace
      (Torsion.MassTraceIdentity.leftMul (matFrobHopf (R := R) d)
        (Torsion.MassTraceIdentity.hol (matFrobHopf (R := R) d) (Ms.map ofMat)) ≫
        Torsion.MassTraceIdentity.massIntegrand (matFrobHopf (R := R) d))) =
      (d : R) * Matrix.trace Ms.prod := by
  rw [Torsion.MassTraceIdentity.massTrace_eq_functional_hol_of_frobeniusForm_eq_counit
      (matFrobHopf (R := R) d) rfl,
    ← Category.assoc, Torsion.MassTraceIdentity.comp_leftMul (matFrobHopf (R := R) d),
    matFrobHopf_hol_eq_ofMat_prod, matFrobHopf_casimir_eq, matFrobHopf_conv_ofMat,
    matFrobHopf_frobeniusForm_eq_counit, toScalar_ofMat_counit,
    Matrix.mul_smul, Matrix.mul_one, Matrix.trace_smul, smul_eq_mul]

/-! ### Inner Derivation Connection `adEndo Ω` (`nablaEndo`) & `CategoricalLagrangian` Instantiation -/

/-- Matrix-space linear operator `matEndo L : matObj R d ⟶ matObj R d` induced by a linear map on matrices. -/
def matEndo {d : ℕ} (L : Matrix (Fin d) (Fin d) R →ₗ[R] Matrix (Fin d) (Fin d) R) :
    matObj R d ⟶ matObj R d :=
  ⟨Matrix.of fun p q => L (Matrix.single q.1 q.2 1) p.1 p.2⟩

/-- Evaluation of `matEndo L` on `ofMat X`: `ofMat X ≫ matEndo L = ofMat (L X)`. -/
theorem ofMat_comp_matEndo {d : ℕ}
    (L : Matrix (Fin d) (Fin d) R →ₗ[R] Matrix (Fin d) (Fin d) R)
    (X : Matrix (Fin d) (Fin d) R) :
    ofMat X ≫ matEndo L = ofMat (L X) := by
  have hX : X = ∑ a : Fin d, ∑ b : Fin d, X a b • Matrix.single a b (1 : R) := by
    ext i j
    simp only [Matrix.sum_apply, Matrix.smul_apply, Matrix.single, Matrix.of_apply, smul_eq_mul]
    rw [Fintype.sum_eq_single i (fun a ha => Finset.sum_eq_zero fun b _ => by simp [ha])]
    rw [Fintype.sum_eq_single j (fun b hb => by simp [hb])]
    simp
  ext ⟨i, j⟩ ⟨⟩
  simp only [mat_comp, ofMat, matEndo, Matrix.mul_apply, Matrix.of_apply]
  dsimp only [matObj]
  rw [Fintype.sum_prod_type]
  conv_rhs => rw [hX, map_sum]
  rw [Matrix.sum_apply]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [map_sum, Matrix.sum_apply]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [LinearMap.map_smul, Matrix.smul_apply, smul_eq_mul, mul_comm]

@[simp] lemma act_matEndo_std {d : ℕ}
    (L : Matrix (Fin d) (Fin d) R →ₗ[R] Matrix (Fin d) (Fin d) R) (a b : Fin d) :
    act (matEndo L) (stdVec (matObj R d) (a, b)) =
      ∑ i : Fin d, ∑ j : Fin d, L (Matrix.single a b 1) i j • stdVec (matObj R d) (i, j) := by
  have hstd : act (ofMat (Matrix.single a b (1 : R))) (stdVec (𝟙_ (FinMatObj R)) ()) =
      stdVec (matObj R d) (a, b) := by
    rw [act_ofMat]
    rw [Fintype.sum_eq_single a (fun u hu => Finset.sum_eq_zero fun v _ => by
      simp [Matrix.single, Matrix.of_apply, Ne.symm hu])]
    rw [Fintype.sum_eq_single b (fun v hv => by simp [Matrix.single, Matrix.of_apply, Ne.symm hv])]
    simp [Matrix.single, Matrix.of_apply]
  rw [← hstd, ← act_comp, ofMat_comp_matEndo, act_ofMat]

/-- Commutator linear map `X ↦ Ω * X - X * Ω` on `Mat_d(R)`. -/
def adLin {d : ℕ} (Ω : Matrix (Fin d) (Fin d) R) :
    Matrix (Fin d) (Fin d) R →ₗ[R] Matrix (Fin d) (Fin d) R where
  toFun X := Ω * X - X * Ω
  map_add' X Y := by rw [Matrix.mul_add, Matrix.add_mul]; abel
  map_smul' r X := by simp [smul_sub]

/-- **Concrete Substrate `nablaEndo` (`adEndo Ω`)** on `matFrobHopf d`: `X ↦ [Ω, X]`. -/
def adEndo {d : ℕ} (Ω : Matrix (Fin d) (Fin d) R) : matObj R d ⟶ matObj R d :=
  matEndo (adLin Ω)

/-- Right multiplication morphism `R_x : A ⟶ A` (`Y ↦ Y * X`) dual to `MassTraceIdentity.leftMul`. -/
def matRightMul {d : ℕ} (x : (𝟙_ (FinMatObj R)) ⟶ matObj R d) : matObj R d ⟶ matObj R d :=
  (ρ_ (matObj R d)).inv ≫ (matObj R d ◁ x) ≫ (matFrobHopf d).mul

lemma ofMat_comp_leftMul {d : ℕ} (Ω X : Matrix (Fin d) (Fin d) R) :
    ofMat X ≫ Torsion.MassTraceIdentity.leftMul (matFrobHopf (R := R) d) (ofMat Ω) =
      ofMat (Ω * X) := by
  rw [Torsion.MassTraceIdentity.comp_leftMul (matFrobHopf (R := R) d), matFrobHopf_conv_ofMat]

lemma ofMat_comp_rightMul {d : ℕ} (Ω X : Matrix (Fin d) (Fin d) R) :
    ofMat X ≫ matRightMul (ofMat Ω) = ofMat (X * Ω) := by
  have hunit : (ofMat X ≫ (ρ_ (matObj R d)).inv) ≫ (matObj R d ◁ ofMat Ω) =
      (λ_ (𝟙_ (FinMatObj R))).inv ≫ (ofMat X ⊗ₘ ofMat Ω) := by
    refine hom_eq_of_act_stdVec fun ⟨⟩ => ?_
    have h1 : act (ofMat X ≫ (ρ_ (matObj R d)).inv) (stdVec (𝟙_ (FinMatObj R)) ()) =
        prodVec (X := matObj R d) (Y := 𝟙_ (FinMatObj R))
          (act (ofMat X) (stdVec (𝟙_ (FinMatObj R)) ()))
          (stdVec (𝟙_ (FinMatObj R)) ()) := by
      rw [act_comp, act_ofMat]
      simp_rw [act_sum, prodVec_sum_left, act_smul, act_rightUnitor_inv_std, prodVec_smul_left]
    rw [act_comp, h1, act_whiskerLeft]
    simp only [act_comp, act_leftUnitor_inv_std, act_tensorHom]
  unfold matRightMul
  rw [← Category.assoc, ← Category.assoc, hunit, Category.assoc]
  exact matFrobHopf_conv_ofMat X Ω

/-- `adEndo Ω` decomposes categorically as `leftMul (ofMat Ω) - matRightMul (ofMat Ω)`. -/
lemma adEndo_eq_leftMul_sub_rightMul {d : ℕ} (Ω : Matrix (Fin d) (Fin d) R) :
    adEndo Ω = Torsion.MassTraceIdentity.leftMul (matFrobHopf (R := R) d) (ofMat Ω) -
      matRightMul (ofMat Ω) := by
  refine hom_eq_of_act_stdVec fun ⟨a, b⟩ => ?_
  have hstd : act (ofMat (Matrix.single a b (1 : R))) (stdVec (𝟙_ (FinMatObj R)) ()) =
      stdVec (matObj R d) (a, b) := by
    rw [act_ofMat]
    rw [Fintype.sum_eq_single a (fun u hu => Finset.sum_eq_zero fun v _ => by
      simp [Matrix.single, Matrix.of_apply, Ne.symm hu])]
    rw [Fintype.sum_eq_single b (fun v hv => by simp [Matrix.single, Matrix.of_apply, Ne.symm hv])]
    simp [Matrix.single, Matrix.of_apply]
  rw [← hstd, ← act_comp, ← act_comp, adEndo, ofMat_comp_matEndo, Preadditive.comp_sub,
    ofMat_comp_leftMul, ofMat_comp_rightMul]
  have hsub : ofMat (Ω * Matrix.single a b (1 : R)) - ofMat (Matrix.single a b 1 * Ω) =
      ofMat (adLin Ω (Matrix.single a b 1)) := by
    ext ⟨i, j⟩ ⟨⟩; simp [ofMat, adLin]
  rw [hsub]

/-- **Exact Leibniz Derivation Law for `adEndo Ω`:**
    `μ ≫ adEndo Ω = (adEndo Ω ▷ A) ≫ μ + (A ◁ adEndo Ω) ≫ μ`, i.e. `∇_Ω(XY) = ∇_Ω(X)Y + X∇_Ω(Y)`. -/
theorem adEndo_leibniz {d : ℕ} (Ω : Matrix (Fin d) (Fin d) R) :
    (matFrobHopf (R := R) d).mul ≫ adEndo Ω =
      (adEndo Ω ▷ matObj R d) ≫ (matFrobHopf (R := R) d).mul +
        (matObj R d ◁ adEndo Ω) ≫ (matFrobHopf (R := R) d).mul := by
  dsimp only [matFrobHopf]
  refine hom_eq_of_act_stdVec fun ⟨⟨a, b⟩, ⟨c, e⟩⟩ => ?_
  simp_rw [stdVec_tensor, adEndo, act_add_hom, act_comp, act_whiskerRight, act_whiskerLeft,
    act_matMul, act_matEndo_std, prodVec_sum_left, prodVec_sum_right, act_sum,
    prodVec_smul_left, prodVec_smul_right, act_smul, act_matMul]
  have hsingle_mul : Matrix.single a b (1 : R) * Matrix.single c e 1 =
      if b = c then Matrix.single a e 1 else 0 := by
    ext i j
    simp only [Matrix.mul_apply, Matrix.single, Matrix.of_apply]
    rw [Fintype.sum_eq_single b (fun k hk => by simp [Ne.symm hk])]
    by_cases hbc : b = c
    · subst hbc
      by_cases hai : a = i <;> by_cases hej : e = j <;> simp [hai, hej]
    · simp [hbc, Ne.symm hbc]
  have hleib : adLin Ω (Matrix.single a b (1 : R) * Matrix.single c e 1) =
      adLin Ω (Matrix.single a b 1) * Matrix.single c e 1 +
        Matrix.single a b 1 * adLin Ω (Matrix.single c e 1) := by
    simp only [adLin, LinearMap.coe_mk, AddHom.coe_mk, Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_assoc]
    abel
  have hlhs :
      act (matEndo (adLin Ω)) (if b = c then stdVec (matObj R d) (a, e) else 0) =
        ∑ i : Fin d, ∑ j : Fin d,
          adLin Ω (Matrix.single a b 1 * Matrix.single c e 1) i j • stdVec (matObj R d) (i, j) := by
    rw [hsingle_mul]
    by_cases hbc : b = c
    · subst hbc; simp [act_matEndo_std]
    · simp [hbc]
  rw [hlhs, hleib]
  funext ⟨i, j⟩
  simp only [Finset.sum_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul, Matrix.add_apply,
    Matrix.mul_apply, Matrix.single, Matrix.of_apply, stdVec_matObj_apply]
  rw [Fintype.sum_eq_single i (fun x hx => Finset.sum_eq_zero fun y _ => by simp [Ne.symm hx])]
  rw [Fintype.sum_eq_single j (fun y hy => by simp [Ne.symm hy])]
  simp only [and_self, ↓reduceIte, mul_one]
  congr 1
  · rw [Fintype.sum_eq_single i (fun x hx => Finset.sum_eq_zero fun y _ => by
      by_cases hyc : y = c
      · subst hyc; simp [Ne.symm hx]
      · simp [hyc])]
    by_cases hje : j = e
    · subst hje
      rw [Fintype.sum_eq_single c (fun y hy => by simp [Ne.symm hy])]
      rw [Fintype.sum_eq_single c (fun y hy => by simp [hy])]
      simp
    · rw [Finset.sum_eq_zero (fun y _ => by simp [Ne.symm hje]),
          Finset.sum_eq_zero (fun y _ => by
            by_cases hyc : y = c
            · subst hyc; simp [hje]
            · simp [hyc])]
  · by_cases hia : i = a
    · subst hia
      rw [Fintype.sum_eq_single b (fun x hx => by simp [Ne.symm hx])]
      rw [Fintype.sum_eq_single b (fun x hx => Finset.sum_eq_zero fun y _ => by simp [Ne.symm hx])]
      rw [Fintype.sum_eq_single j (fun y hy => by simp [Ne.symm hy])]
      simp
    · rw [Finset.sum_eq_zero (fun x _ => by simp [Ne.symm hia]),
          Finset.sum_eq_zero (fun x _ => Finset.sum_eq_zero fun y _ => by
            by_cases hbx : b = x
            · subst hbx; simp [hia]
            · simp [hbx])]

/-- **Non-triviality of `adEndo Ω`:** whenever `Ω` has a non-zero off-diagonal entry `Ω i j ≠ 0`
    (`i ≠ j`), the connection endomorphism `adEndo Ω` is non-zero. -/
theorem adEndo_ne_zero_of_offDiag {d : ℕ} {Ω : Matrix (Fin d) (Fin d) R}
    {i j : Fin d} (hij : i ≠ j) (hΩ : Ω i j ≠ 0) :
    adEndo Ω ≠ 0 := by
  intro h0
  have h : (ofMat (Matrix.single j j 1) ≫ adEndo Ω).mat (i, j) () =
      (ofMat (Matrix.single j j 1) ≫ (0 : matObj R d ⟶ matObj R d)).mat (i, j) () := by
    rw [h0]
  rw [adEndo, ofMat_comp_matEndo, Limits.comp_zero] at h
  simp only [mat_zero, Matrix.zero_apply, ofMat, Matrix.of_apply,
    adLin, LinearMap.coe_mk, AddHom.coe_mk, Matrix.sub_apply, Matrix.mul_apply,
    Matrix.single] at h
  rw [Fintype.sum_eq_single j (fun k hk => by simp [Ne.symm hk]),
      Finset.sum_eq_zero (fun k _ => by simp [hij.symm])] at h
  simp only [and_self, ↓reduceIte, mul_one, sub_zero] at h
  exact hΩ h

/-- **Concrete `QOU.CategoricalConnection` on `matFrobHopf d`** induced by `adEndo Ω`. -/
def matConnection {d : ℕ} (Ω : Matrix (Fin d) (Fin d) R) :
    QOU.CategoricalConnection (FinMatObj R) (matFrobHopf d) where
  Omega1 := 𝟙_ (FinMatObj R)
  nabla := adEndo Ω ≫ (ρ_ (matObj R d)).inv
  leibniz_rhs := ((adEndo Ω ▷ matObj R d) ≫ (matFrobHopf d).mul +
      (matObj R d ◁ adEndo Ω) ≫ (matFrobHopf d).mul) ≫ (ρ_ (matObj R d)).inv
  leibniz := by rw [← Category.assoc, adEndo_leibniz]

/-- Linear evaluation trace functional `τ_eval(f) = Tr(f(I_d))` on `End(matObj R d)`. -/
def evalTraceLin (d : ℕ) : (matObj R d ⟶ matObj R d) →ₗ[R] R where
  toFun f := toScalar ((matFrobHopf (R := R) d).unit ≫ f ≫ (matFrobHopf (R := R) d).frobeniusForm)
  map_add' f g := by
    simp only [Preadditive.add_comp, Preadditive.comp_add, toScalar, mat_add, Matrix.add_apply]
  map_smul' r f := by
    simp only [Linear.smul_comp, Linear.comp_smul, toScalar, mat_smul, Matrix.smul_apply,
      RingHom.id_apply, smul_eq_mul]

/-- Concrete Reeb endomorphism `substrateReebLin M N` on `Mat_{d+2}(R)`:
    maps `X ↦ X_{11} E_{01} + X_{01} M + (X_{00} - X_{11}) N`. -/
def substrateReebLin {d : ℕ} (M N : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    Matrix (Fin (d + 2)) (Fin (d + 2)) R →ₗ[R] Matrix (Fin (d + 2)) (Fin (d + 2)) R where
  toFun X := X 1 1 • Matrix.single 0 1 1 + X 0 1 • M + (X 0 0 - X 1 1) • N
  map_add' X Y := by
    ext i j; simp only [Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]; ring
  map_smul' r X := by
    ext i j; simp only [Matrix.smul_apply, Matrix.add_apply, RingHom.id_apply, smul_eq_mul]; ring

/-- Categorical Reeb endomorphism `substrateReeb M N : matObj R (d + 2) ⟶ matObj R (d + 2)`. -/
def substrateReeb {d : ℕ} (M N : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    matObj R (d + 2) ⟶ matObj R (d + 2) :=
  matEndo (substrateReebLin M N)

/-- Concrete `CategoricalDiracOperator` with spatial connection `adEndo Ω` and Reeb `substrateReeb M N`. -/
def substrateDirac {d : ℕ} (q qinv : R) (hq : q * qinv = 1)
    (Ω M N : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    QOU.CategoricalDiracOperator R (FinMatObj R) (matFrobHopf (d + 2)) where
  connection := matConnection Ω
  q := q
  qinv := qinv
  q_unit := hq
  nablaEndo := adEndo Ω
  reeb := substrateReeb M N
  dirac := qinv • adEndo Ω + (1 - qinv) • substrateReeb M N
  dirac_formula := rfl

/-- Normalised `(0,0)`-entry costate `X ↦ X_{00}` on `matObj R (d + 2)`. -/
def e00Costate (d : ℕ) : matObj R (d + 2) ⟶ 𝟙_ (FinMatObj R) :=
  ⟨Matrix.of fun _ p => if p = (0, 0) then 1 else 0⟩

/-- Concrete normalised `CategoricalLagrangian` on `matFrobHopf (d + 2)`. -/
def substrateLagrangian {d : ℕ} (q qinv : R) (hq : q * qinv = 1)
    (Ω M N : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    QOU.CategoricalLagrangian R (FinMatObj R) (matFrobHopf (d + 2)) where
  dirac := substrateDirac q qinv hq Ω M N
  state := ofMat (Matrix.single 0 0 1)
  costate := e00Costate d
  lagrangian :=
    ((substrateDirac q qinv hq Ω M N).dirac ≫ (substrateDirac q qinv hq Ω M N).dirac) +
      (e00Costate d ≫ ofMat (Matrix.single 0 0 1) ≫ (substrateDirac q qinv hq Ω M N).dirac)
  lagrangian_formula := rfl

/-- The substrate Lagrangian state is normalised (`state ≫ costate = 𝟙`). -/
theorem substrateLagrangian_normalised {d : ℕ} (q qinv : R) (hq : q * qinv = 1)
    (Ω M N : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    (substrateLagrangian q qinv hq Ω M N).state ≫
      (substrateLagrangian q qinv hq Ω M N).costate = 𝟙 (𝟙_ (FinMatObj R)) := by
  ext ⟨⟩ ⟨⟩
  simp only [substrateLagrangian, ofMat, e00Costate, mat_comp, mat_id, Matrix.mul_apply,
    Matrix.of_apply, Matrix.one_apply]
  dsimp only [matObj]
  rw [Fintype.sum_eq_single ((0 : Fin (d + 2)), (0 : Fin (d + 2)))
    (fun p hp => by simp [hp])]
  simp [Matrix.single, Matrix.of_apply]

/-- **Automatic vanishing of the spatial-Reeb cross-trace (`hCross`):**
    by Leibniz (`[Ω, I] = 0`) and trace cyclicity (`Tr([Ω, L(I)]) = 0`),
    `evalTraceLin (adEndo Ω ≫ f + f ≫ adEndo Ω) = 0` for **every** `Ω` and **every** `f = matEndo L`. -/
theorem evalTraceLin_cross_zero {d : ℕ} (Ω : Matrix (Fin d) (Fin d) R)
    (L : Matrix (Fin d) (Fin d) R →ₗ[R] Matrix (Fin d) (Fin d) R) :
    evalTraceLin d (adEndo Ω ≫ matEndo L + matEndo L ≫ adEndo Ω) = 0 := by
  rw [map_add]
  unfold evalTraceLin
  simp only [LinearMap.coe_mk, AddHom.coe_mk, adEndo]
  have h1 : (matFrobHopf (R := R) d).unit ≫
      (matEndo (adLin Ω) ≫ matEndo L) ≫ (matFrobHopf d).frobeniusForm =
      ofMat (L (adLin Ω 1)) ≫ (matFrobHopf d).counit := by
    rw [← ofMat_one, ← Category.assoc, ← Category.assoc, ofMat_comp_matEndo, Category.assoc,
        ← Category.assoc, ofMat_comp_matEndo, matFrobHopf_frobeniusForm_eq_counit]
  have h2 : (matFrobHopf (R := R) d).unit ≫
      (matEndo L ≫ matEndo (adLin Ω)) ≫ (matFrobHopf d).frobeniusForm =
      ofMat (adLin Ω (L 1)) ≫ (matFrobHopf d).counit := by
    rw [← ofMat_one, ← Category.assoc, ← Category.assoc, ofMat_comp_matEndo, Category.assoc,
        ← Category.assoc, ofMat_comp_matEndo, matFrobHopf_frobeniusForm_eq_counit]
  rw [h1, h2, toScalar_ofMat_counit, toScalar_ofMat_counit]
  have hI : adLin Ω 1 = 0 := by simp [adLin]
  rw [hI, map_zero, Matrix.trace_zero, zero_add]
  simp [adLin, Matrix.trace_sub, Matrix.trace_mul_comm Ω]

lemma unit_comp_e00Costate (d : ℕ) :
    (matFrobHopf (R := R) (d + 2)).unit ≫ e00Costate d = 𝟙 (𝟙_ (FinMatObj R)) := by
  ext ⟨⟩ ⟨⟩
  simp only [matFrobHopf, matUnit, e00Costate, mat_comp, mat_id, Matrix.mul_apply,
    Matrix.of_apply, Matrix.one_apply]
  dsimp only [matObj]
  rw [Fintype.sum_eq_single ((0 : Fin (d + 2)), (0 : Fin (d + 2)))
    (fun p hp => by simp [hp])]
  simp

/-- **Automatic vanishing of the horizontal matter trace (`hHoriz`):**
    `evalTraceLin (e00Costate ≫ ofMat E_{00} ≫ adEndo Ω) = Tr([Ω, E_{00}]) = 0`. -/
theorem evalTraceLin_horiz_zero {d : ℕ} (Ω : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    evalTraceLin (d + 2)
      (e00Costate d ≫ ofMat (Matrix.single 0 0 1) ≫ adEndo Ω) = 0 := by
  unfold evalTraceLin
  simp only [LinearMap.coe_mk, AddHom.coe_mk]
  have h : (matFrobHopf (R := R) (d + 2)).unit ≫
      (e00Costate d ≫ ofMat (Matrix.single 0 0 1) ≫ adEndo Ω) ≫
        (matFrobHopf (d + 2)).frobeniusForm =
      ofMat (adLin Ω (Matrix.single 0 0 1)) ≫ (matFrobHopf (d + 2)).counit := by
    rw [← Category.assoc, ← Category.assoc, unit_comp_e00Costate, Category.id_comp,
        adEndo, ofMat_comp_matEndo, matFrobHopf_frobeniusForm_eq_counit]
  rw [h, toScalar_ofMat_counit]
  simp [adLin, Matrix.trace_sub, Matrix.trace_mul_comm Ω]

private lemma fin_zero_ne_one (d : ℕ) : (0 : Fin (d + 2)) ≠ 1 := by
  intro h; have := congrArg Fin.val h; simp at this

/-- **Exact Bosonic Reeb-Square Trace (`hReebP` / `hReebN`):**
    `evalTraceLin (substrateReeb M N ≫ substrateReeb M N) = Tr(M)`. -/
theorem evalTraceLin_reeb_sq {d : ℕ} (M N : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    evalTraceLin (d + 2) (substrateReeb M N ≫ substrateReeb M N) = Matrix.trace M := by
  unfold evalTraceLin substrateReeb
  simp only [LinearMap.coe_mk, AddHom.coe_mk]
  have h : (matFrobHopf (R := R) (d + 2)).unit ≫
      (matEndo (substrateReebLin M N) ≫ matEndo (substrateReebLin M N)) ≫
        (matFrobHopf (d + 2)).frobeniusForm =
      ofMat (substrateReebLin M N (substrateReebLin M N 1)) ≫ (matFrobHopf (d + 2)).counit := by
    rw [← ofMat_one, ← Category.assoc, ← Category.assoc, ofMat_comp_matEndo, Category.assoc,
        ← Category.assoc, ofMat_comp_matEndo, matFrobHopf_frobeniusForm_eq_counit]
  rw [h, toScalar_ofMat_counit]
  have h01 : (0 : Fin (d + 2)) ≠ 1 := fin_zero_ne_one d
  have hR1 : substrateReebLin M N 1 = Matrix.single 0 1 1 := by
    simp [substrateReebLin, h01]
  have hR2 : substrateReebLin M N (Matrix.single 0 1 1) = M := by
    simp [substrateReebLin, Matrix.single, Matrix.of_apply, h01]
  rw [hR1, hR2]

/-- **Exact Fermionic Matter Reeb Trace (`hMatReebP` / `hMatReebN`):**
    `evalTraceLin (e00Costate ≫ ofMat E_{00} ≫ substrateReeb M N) = Tr(N)`. -/
theorem evalTraceLin_matter_reeb {d : ℕ} (M N : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    evalTraceLin (d + 2)
      (e00Costate d ≫ ofMat (Matrix.single 0 0 1) ≫ substrateReeb M N) = Matrix.trace N := by
  unfold evalTraceLin substrateReeb
  simp only [LinearMap.coe_mk, AddHom.coe_mk]
  have h : (matFrobHopf (R := R) (d + 2)).unit ≫
      (e00Costate d ≫ ofMat (Matrix.single 0 0 1) ≫ matEndo (substrateReebLin M N)) ≫
        (matFrobHopf (d + 2)).frobeniusForm =
      ofMat (substrateReebLin M N (Matrix.single 0 0 1)) ≫ (matFrobHopf (d + 2)).counit := by
    rw [← Category.assoc, ← Category.assoc, unit_comp_e00Costate, Category.id_comp,
        ofMat_comp_matEndo, matFrobHopf_frobeniusForm_eq_counit]
  rw [h, toScalar_ofMat_counit]
  have h01 : (0 : Fin (d + 2)) ≠ 1 := fin_zero_ne_one d
  have hRN : substrateReebLin M N (Matrix.single 0 0 1) = N := by
    simp [substrateReebLin, Matrix.single, Matrix.of_apply, h01]
  rw [hRN]

/-- Joint verification of all nine trace hypotheses of `CategoricalLagrangianTwoTermBridge`
    on `substrateLagrangian` over an arbitrary `[CommRing R]`. -/
theorem substrateLagrangian_trace_hyps {d : ℕ} (q qinv : R) (hq : q * qinv = 1)
    (Ω M_n N_n M_p N_p : Matrix (Fin (d + 2)) (Fin (d + 2)) R) :
    let L_n := substrateLagrangian q qinv hq Ω M_n N_n
    let L_p := substrateLagrangian q qinv hq Ω M_p N_p
    L_n.dirac.qinv = qinv ∧
    L_p.dirac.qinv = qinv ∧
    L_n.dirac.nablaEndo = L_p.dirac.nablaEndo ∧
    evalTraceLin (d + 2)
        (L_n.dirac.nablaEndo ≫ L_n.dirac.reeb + L_n.dirac.reeb ≫ L_n.dirac.nablaEndo) =
      evalTraceLin (d + 2)
        (L_p.dirac.nablaEndo ≫ L_p.dirac.reeb + L_p.dirac.reeb ≫ L_p.dirac.nablaEndo) ∧
    evalTraceLin (d + 2) (L_n.dirac.reeb ≫ L_n.dirac.reeb) = Matrix.trace M_n ∧
    evalTraceLin (d + 2) (L_p.dirac.reeb ≫ L_p.dirac.reeb) = Matrix.trace M_p ∧
    evalTraceLin (d + 2) (L_n.costate ≫ L_n.state ≫ L_n.dirac.nablaEndo) =
      evalTraceLin (d + 2) (L_p.costate ≫ L_p.state ≫ L_p.dirac.nablaEndo) ∧
    evalTraceLin (d + 2) (L_n.costate ≫ L_n.state ≫ L_n.dirac.reeb) = Matrix.trace N_n ∧
    evalTraceLin (d + 2) (L_p.costate ≫ L_p.state ≫ L_p.dirac.reeb) = Matrix.trace N_p := by
  intro L_n L_p
  refine ⟨rfl, rfl, rfl, ?_, evalTraceLin_reeb_sq M_n N_n, evalTraceLin_reeb_sq M_p N_p,
    rfl, evalTraceLin_matter_reeb M_n N_n, evalTraceLin_matter_reeb M_p N_p⟩
  dsimp [L_n, L_p, substrateLagrangian, substrateDirac, substrateReeb]
  rw [evalTraceLin_cross_zero, evalTraceLin_cross_zero]

end CategoryStructure

/-- **Concrete Unconditional Substrate Instantiation of `CategoricalLagrangianTwoTermBridge`:**
    for any `[Field F]`, `q ≠ 0`, `3 ≠ 0`, and any spatial KZ connection matrix `Ω : Mat_3(F)`,
    the concrete substrate configurations `L_n` and `L_p` on `matFrobHopf 3` satisfy every
    hypothesis of `trace_lagrangian_diff_concrete_borromean_weight_space` without uninstantiated
    oracles. -/
theorem substrate_borromean_two_term_instantiation {F : Type*} [Field F]
    (q : F) (hq : q ≠ 0) (h3 : (3 : F) ≠ 0) (Ω : Matrix (Fin 3) (Fin 3) F) :
    let L_n := substrateLagrangian (d := 1) q q⁻¹ (mul_inv_cancel₀ hq) Ω
      (q⁻¹ • QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.borromeanV3B q)
      ((QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.Q12n +
        QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.Q23n) *
          QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.borromeanV3B q)
    let L_p := substrateLagrangian (d := 1) q q⁻¹ (mul_inv_cancel₀ hq) Ω
      (q • QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.borromeanV3A q)
      ((QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.Q12p +
        QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.Q23p) *
          QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.borromeanV3A q)
    evalTraceLin 3 L_n.lagrangian - evalTraceLin 3 L_p.lagrangian =
      (1 - q⁻¹) ^ 2 * (q⁻¹ - q) *
        (-(q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6) +
      (1 - q⁻¹) *
        ((2 * q ^ 12 - 7 * q ^ 10 + 10 * q ^ 8 - 12 * q ^ 6 + 10 * q ^ 4 - 7 * q ^ 2 + 2) /
          (3 * q ^ 6)) := by
  intro L_n L_p
  have H := substrateLagrangian_trace_hyps (d := 1) q q⁻¹ (mul_inv_cancel₀ hq) Ω
    (q⁻¹ • QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.borromeanV3B q)
    ((QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.Q12n +
      QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.Q23n) *
        QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.borromeanV3B q)
    (q • QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.borromeanV3A q)
    ((QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.Q12p +
      QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.Q23p) *
        QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm.borromeanV3A q)
  exact QOU.CategoricalLagrangianTwoTermBridge.trace_lagrangian_diff_concrete_borromean_weight_space
    (evalTraceLin 3) L_n L_p q hq h3 H.1 H.2.1 H.2.2.1 H.2.2.2.1
    (H.2.2.2.2.1.trans (by rw [Matrix.trace_smul, smul_eq_mul]))
    (H.2.2.2.2.2.1.trans (by rw [Matrix.trace_smul, smul_eq_mul]))
    H.2.2.2.2.2.2.1 H.2.2.2.2.2.2.2.1 H.2.2.2.2.2.2.2.2

end MatrixSubstrate

/-! ## §5. Two-Row KZ / Hecke Representations on `B_3` (`[2,1]`) and `B_4` (`[2,2]`, `[3,1]`)
    & Continuous KZ Monodromy Trace Agreement -/

section TwoRowKZAndHecke

section GenericCommRing

variable {R : Type*} [CommRing R]

/-- Generator `T_0` on the 2D `[2,1]` Specht module of `H_3(q)` (division-free over `[CommRing R]`). -/
def heckeB3_21_T0 (q qi : R) : Matrix (Fin 2) (Fin 2) R := !![q, 1; 0, -qi]

/-- Generator `T_1` on the 2D `[2,1]` Specht module of `H_3(q)`. -/
def heckeB3_21_T1 (q qi : R) : Matrix (Fin 2) (Fin 2) R := !![-qi, 0; 1, q]

/-- Inverse `T_1⁻¹ = T_1 - (q - q⁻¹) I` on `[2,1]`. -/
def heckeB3_21_T1Inv (q qi : R) : Matrix (Fin 2) (Fin 2) R := !![-q, 0; 1, qi]

/-- Hecke quadratic `(T_0 - q I)(T_0 + q⁻¹ I) = 0` on `B_3` `[2,1]`. -/
theorem heckeB3_21_T0_quad (q qi : R) :
    (heckeB3_21_T0 q qi - q • 1) * (heckeB3_21_T0 q qi + qi • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [heckeB3_21_T0, Matrix.mul_apply, Fin.sum_univ_two]

/-- Hecke quadratic `(T_1 - q I)(T_1 + q⁻¹ I) = 0` on `B_3` `[2,1]`. -/
theorem heckeB3_21_T1_quad (q qi : R) :
    (heckeB3_21_T1 q qi - q • 1) * (heckeB3_21_T1 q qi + qi • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [heckeB3_21_T1, Matrix.mul_apply, Fin.sum_univ_two]

/-- Exact inverse `T_1 · T_1⁻¹ = I_2` on `B_3` `[2,1]`. -/
theorem heckeB3_21_T1_mul_inv (q qi : R) (hq : q * qi = 1) :
    heckeB3_21_T1 q qi * heckeB3_21_T1Inv q qi = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [heckeB3_21_T1, heckeB3_21_T1Inv, Matrix.mul_apply, Fin.sum_univ_two]
  · linear_combination hq
  · exact hq

/-- **Yang–Baxter braid relation `T_0 T_1 T_0 = T_1 T_0 T_1`** on `B_3` `[2,1]`. -/
theorem heckeB3_21_braid (q qi : R) (hq : q * qi = 1) :
    heckeB3_21_T0 q qi * heckeB3_21_T1 q qi * heckeB3_21_T0 q qi =
      heckeB3_21_T1 q qi * heckeB3_21_T0 q qi * heckeB3_21_T1 q qi := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [heckeB3_21_T0, heckeB3_21_T1, Matrix.mul_apply, Fin.sum_univ_two]
  · linear_combination -(q + qi) * hq
  · linear_combination -hq
  · linear_combination hq
  · linear_combination (q + qi) * hq

/-- Elementary generator traces on `B_3` `[2,1]`: `Tr(T_0) = Tr(T_1) = q - q⁻¹`. -/
theorem heckeB3_21_trace_gen (q qi : R) :
    Matrix.trace (heckeB3_21_T0 q qi) = q - qi ∧
      Matrix.trace (heckeB3_21_T1 q qi) = q - qi := by
  constructor <;> { simp [heckeB3_21_T0, heckeB3_21_T1, Matrix.trace_fin_two]; ring }

lemma heckeB3_21_T0_mul_T1 (q qi : R) (hq : q * qi = 1) :
    heckeB3_21_T0 q qi * heckeB3_21_T1 q qi = !![0, q; -qi, -1] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [heckeB3_21_T0, heckeB3_21_T1, Matrix.mul_apply, Fin.sum_univ_two]
  · linear_combination -hq
  · linear_combination hq

/-- Closed-form `[2,1]` trace on trefoil `3_1 = (σ_0 σ_1)²` and torus knot `T(3,5) = (σ_0 σ_1)⁵`. -/
theorem heckeB3_21_trace_trefoil_and_T35 (q qi : R) (hq : q * qi = 1) :
    Matrix.trace ((heckeB3_21_T0 q qi * heckeB3_21_T1 q qi) ^ 2) = -1 ∧
      Matrix.trace ((heckeB3_21_T0 q qi * heckeB3_21_T1 q qi) ^ 5) = -1 := by
  rw [heckeB3_21_T0_mul_T1 q qi hq]
  have hsq : (!![0, q; -qi, -1] : Matrix (Fin 2) (Fin 2) R) ^ 2 = !![-1, -q; qi, 0] := by
    rw [sq]
    ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
    · exact hq
    · linear_combination -hq
  have hcube : (!![0, q; -qi, -1] : Matrix (Fin 2) (Fin 2) R) ^ 3 = 1 := by
    have : (3 : ℕ) = 2 + 1 := rfl
    rw [this, pow_add, pow_one, hsq]
    ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
    · exact hq
    · linear_combination hq
  have h5 : (!![0, q; -qi, -1] : Matrix (Fin 2) (Fin 2) R) ^ 5 =
      (!![0, q; -qi, -1] : Matrix (Fin 2) (Fin 2) R) ^ 2 := by
    have : (5 : ℕ) = 3 + 2 := rfl
    rw [this, pow_add, hcube, Matrix.one_mul]
  rw [h5, and_self, hsq]
  simp [Matrix.trace_fin_two]

lemma heckeB3_21_T0_mul_T1Inv (q qi : R) :
    heckeB3_21_T0 q qi * heckeB3_21_T1Inv q qi = !![1 - q ^ 2, qi; -qi, -qi ^ 2] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [heckeB3_21_T0, heckeB3_21_T1Inv, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- Closed-form `[2,1]` trace on figure-eight `4_1 = (σ_0 σ_1⁻¹)²`:
    `Tr((T_0 T_1⁻¹)²) = q⁴ - 2q² + 1 - 2q⁻² + q⁻⁴`. -/
theorem heckeB3_21_trace_figureEight (q qi : R) :
    Matrix.trace ((heckeB3_21_T0 q qi * heckeB3_21_T1Inv q qi) ^ 2) =
      q ^ 4 - 2 * q ^ 2 + 1 - 2 * qi ^ 2 + qi ^ 4 := by
  rw [heckeB3_21_T0_mul_T1Inv, sq]
  simp [Matrix.trace_fin_two]
  ring

/-- Generators `T_0, T_1, T_2` on the 2D `[2,2]` Specht module of `H_4(q)` (`T_2 = T_0`). -/
def heckeB4_22_T0 (q qi : R) : Matrix (Fin 2) (Fin 2) R := heckeB3_21_T0 q qi
def heckeB4_22_T1 (q qi : R) : Matrix (Fin 2) (Fin 2) R := heckeB3_21_T1 q qi
def heckeB4_22_T2 (q qi : R) : Matrix (Fin 2) (Fin 2) R := heckeB3_21_T0 q qi

/-- Complete `H_4(q)` defining relations on the 2D `[2,2]` representation over `[CommRing R]`. -/
theorem heckeB4_22_relations (q qi : R) (hq : q * qi = 1) :
    (heckeB4_22_T2 q qi - q • 1) * (heckeB4_22_T2 q qi + qi • 1) = 0 ∧
    heckeB4_22_T0 q qi * heckeB4_22_T2 q qi = heckeB4_22_T2 q qi * heckeB4_22_T0 q qi ∧
    heckeB4_22_T0 q qi * heckeB4_22_T1 q qi * heckeB4_22_T0 q qi =
      heckeB4_22_T1 q qi * heckeB4_22_T0 q qi * heckeB4_22_T1 q qi ∧
    heckeB4_22_T1 q qi * heckeB4_22_T2 q qi * heckeB4_22_T1 q qi =
      heckeB4_22_T2 q qi * heckeB4_22_T1 q qi * heckeB4_22_T2 q qi :=
  ⟨heckeB3_21_T0_quad q qi, rfl, heckeB3_21_braid q qi hq, (heckeB3_21_braid q qi hq).symm⟩

/-- Elementary generator traces on `B_4` `[2,2]`: `Tr(T_0) = Tr(T_1) = Tr(T_2) = q - q⁻¹`. -/
theorem heckeB4_22_trace_gen (q qi : R) :
    Matrix.trace (heckeB4_22_T0 q qi) = q - qi ∧
    Matrix.trace (heckeB4_22_T1 q qi) = q - qi ∧
    Matrix.trace (heckeB4_22_T2 q qi) = q - qi :=
  ⟨(heckeB3_21_trace_gen q qi).1, (heckeB3_21_trace_gen q qi).2, (heckeB3_21_trace_gen q qi).1⟩

/-- Generators `T_0, T_1, T_2` on the 3D `[3,1]` Specht module of `H_4(q)` over `[CommRing R]`. -/
def heckeB4_31_T0 (q qi : R) : Matrix (Fin 3) (Fin 3) R := !![-qi, 1, 0; 0, q, 0; 0, 0, q]
def heckeB4_31_T1 (q qi : R) : Matrix (Fin 3) (Fin 3) R := !![q, 0, 0; 1, -qi, 1; 0, 0, q]
def heckeB4_31_T2 (q qi : R) : Matrix (Fin 3) (Fin 3) R := !![q, 0, 0; 0, q, 0; 0, 1, -qi]

/-- Complete `H_4(q)` defining relations on the 3D `[3,1]` representation over `[CommRing R]`. -/
theorem heckeB4_31_relations (q qi : R) (hq : q * qi = 1) :
    (heckeB4_31_T0 q qi - q • 1) * (heckeB4_31_T0 q qi + qi • 1) = 0 ∧
    (heckeB4_31_T1 q qi - q • 1) * (heckeB4_31_T1 q qi + qi • 1) = 0 ∧
    (heckeB4_31_T2 q qi - q • 1) * (heckeB4_31_T2 q qi + qi • 1) = 0 ∧
    heckeB4_31_T0 q qi * heckeB4_31_T2 q qi = heckeB4_31_T2 q qi * heckeB4_31_T0 q qi ∧
    heckeB4_31_T0 q qi * heckeB4_31_T1 q qi * heckeB4_31_T0 q qi =
      heckeB4_31_T1 q qi * heckeB4_31_T0 q qi * heckeB4_31_T1 q qi ∧
    heckeB4_31_T1 q qi * heckeB4_31_T2 q qi * heckeB4_31_T1 q qi =
      heckeB4_31_T2 q qi * heckeB4_31_T1 q qi * heckeB4_31_T2 q qi := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [heckeB4_31_T0, Matrix.mul_apply, Fin.sum_univ_three]; ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [heckeB4_31_T1, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [heckeB4_31_T2, Matrix.mul_apply, Fin.sum_univ_three]; ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [heckeB4_31_T0, heckeB4_31_T2, Matrix.mul_apply, Fin.sum_univ_three] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [heckeB4_31_T0, heckeB4_31_T1, Matrix.mul_apply, Fin.sum_univ_three]
    · linear_combination (q + qi) * hq
    · linear_combination -hq
    · linear_combination hq
    · linear_combination -(q + qi) * hq
    · linear_combination -hq
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [heckeB4_31_T1, heckeB4_31_T2, Matrix.mul_apply, Fin.sum_univ_three]
    · linear_combination -hq
    · linear_combination (q + qi) * hq
    · linear_combination -hq
    · linear_combination hq
    · linear_combination -(q + qi) * hq

/-- KZ pairwise residue matrices `Ω_{01}, Ω_{12}, Ω_{02}` on `[2,1]` (`B_3`) and `[2,2]` (`B_4`). -/
def kzOmega01 : Matrix (Fin 2) (Fin 2) R := !![1, 1; 0, -1]
def kzOmega12 : Matrix (Fin 2) (Fin 2) R := !![-1, 0; 1, 1]
def kzOmega02 : Matrix (Fin 2) (Fin 2) R := !![0, -1; -1, 0]

/-- Involution (`Ω² = I_2`), tracelessness (`Tr(Ω) = 0`), and **Kohno–Arnold 4T flatness**
    `[Ω_{01}, Ω_{02} + Ω_{12}] = 0` and `[Ω_{12}, Ω_{01} + Ω_{02}] = 0` over `[CommRing R]`. -/
theorem kzOmega_involutive_traceless_and_4T :
    (kzOmega01 : Matrix (Fin 2) (Fin 2) R) * kzOmega01 = 1 ∧
    (kzOmega12 : Matrix (Fin 2) (Fin 2) R) * kzOmega12 = 1 ∧
    (kzOmega02 : Matrix (Fin 2) (Fin 2) R) * kzOmega02 = 1 ∧
    Matrix.trace (kzOmega01 : Matrix (Fin 2) (Fin 2) R) = 0 ∧
    Matrix.trace (kzOmega12 : Matrix (Fin 2) (Fin 2) R) = 0 ∧
    (kzOmega01 : Matrix (Fin 2) (Fin 2) R) * (kzOmega02 + kzOmega12) =
      (kzOmega02 + kzOmega12) * kzOmega01 ∧
    (kzOmega12 : Matrix (Fin 2) (Fin 2) R) * (kzOmega01 + kzOmega02) =
      (kzOmega01 + kzOmega02) * kzOmega12 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;> simp [kzOmega01, Matrix.mul_apply, Fin.sum_univ_two]
  · ext i j; fin_cases i <;> fin_cases j <;> simp [kzOmega12, Matrix.mul_apply, Fin.sum_univ_two]
  · ext i j; fin_cases i <;> fin_cases j <;> simp [kzOmega02, Matrix.mul_apply, Fin.sum_univ_two]
  · simp [kzOmega01, Matrix.trace_fin_two]
  · simp [kzOmega12, Matrix.trace_fin_two]
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [kzOmega01, kzOmega12, kzOmega02, Matrix.mul_apply, Fin.sum_univ_two]
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [kzOmega01, kzOmega12, kzOmega02, Matrix.mul_apply, Fin.sum_univ_two]

/-- Non-triviality of `adEndo kzOmega01` on `matFrobHopf 2`: `nablaEndo ≠ 0` over any `[Nontrivial R]`. -/
theorem adEndo_kzOmega01_ne_zero [Nontrivial R] :
    adEndo (kzOmega01 : Matrix (Fin 2) (Fin 2) R) ≠ 0 :=
  adEndo_ne_zero_of_offDiag (i := 0) (j := 1) (by decide) (by simp [kzOmega01])

end GenericCommRing

/-! ### Continuous KZ Half-Turn ODE Fundamental Solution & Exact KZ–Hecke Trace Agreement -/

section ContinuousKZMonodromy

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

/-- Exact continuous fundamental solution `Φ_S(η, t) = cosh(η t) I + sinh(η t) S` on `[0, 1]`
    for any involutive residue matrix `S` (`S * S = 1`) at real hyperbolic parameter `η₀`. -/
noncomputable def kzHalfTurnFundReal {n : Type*} [Fintype n] [DecidableEq n]
    (S : Matrix n n ℝ) (η₀ t : ℝ) : Matrix n n ℝ :=
  ((Real.exp (η₀ * t) + Real.exp (-(η₀ * t))) / 2) • (1 : Matrix n n ℝ) +
    ((Real.exp (η₀ * t) - Real.exp (-(η₀ * t))) / 2) • S

/-- **Continuous ODE Proof (`IsLinearFundSol`) at Real Hyperbolic `q₀ = exp(η₀)`:**
    `kzHalfTurnFundReal S η₀` solves `Φ'(t) = (η₀ • S) * Φ(t)`, `Φ(0) = I`, on `[0, 1]`. -/
theorem kzHalfTurnFundReal_isFundSol {n : Type*} [Fintype n] [DecidableEq n]
    (S : Matrix n n ℝ) (hS : S * S = 1) (η₀ : ℝ) :
    IsLinearFundSol (fun _ => η₀ • S) (kzHalfTurnFundReal S η₀) := by
  refine ⟨by simp [kzHalfTurnFundReal], fun t _ => ?_⟩
  have hd1 : HasDerivAt (fun s : ℝ => Real.exp (η₀ * s)) (η₀ * Real.exp (η₀ * t)) t := by
    simpa [mul_comm] using ((hasDerivAt_id t).const_mul η₀).exp
  have hd2 : HasDerivAt (fun s : ℝ => Real.exp (-(η₀ * s))) (-(η₀ * Real.exp (-(η₀ * t)))) t := by
    simpa [mul_comm] using ((hasDerivAt_id t).const_mul η₀).neg.exp
  have hc : HasDerivAt (fun s : ℝ => (Real.exp (η₀ * s) + Real.exp (-(η₀ * s))) / 2)
      (η₀ * ((Real.exp (η₀ * t) - Real.exp (-(η₀ * t))) / 2)) t := by
    convert (hd1.add hd2).div_const 2 using 1; ring
  have hs : HasDerivAt (fun s : ℝ => (Real.exp (η₀ * s) - Real.exp (-(η₀ * s))) / 2)
      (η₀ * ((Real.exp (η₀ * t) + Real.exp (-(η₀ * t))) / 2)) t := by
    convert (hd1.sub hd2).div_const 2 using 1; ring
  have htot := ((hc.smul_const (1 : Matrix n n ℝ)).add (hs.smul_const S)).hasDerivWithinAt
    (s := Icc (0 : ℝ) 1)
  refine htot.congr_deriv ?_
  unfold kzHalfTurnFundReal
  rw [Matrix.mul_add, Matrix.smul_mul, Matrix.mul_smul, Matrix.mul_one,
      Matrix.smul_mul, Matrix.mul_smul, hS, smul_smul, smul_smul, add_comm]

/-- Local KZ half-turn monodromy `M_KZ(η₀) = S · Φ_S(η₀, 1)` at real hyperbolic `q₀ = exp(η₀)`. -/
noncomputable def kzLocalMonodromyReal {n : Type*} [Fintype n] [DecidableEq n]
    (S : Matrix n n ℝ) (η₀ : ℝ) : Matrix n n ℝ :=
  S * kzHalfTurnFundReal S η₀ 1

/-- **Exact Hecke Quadratic for the Real Hyperbolic KZ Monodromy (`q₀ = exp(η₀)`):**
    `(M_KZ(η₀) - q₀ I)(M_KZ(η₀) + q₀⁻¹ I) = 0`. -/
theorem kzLocalMonodromyReal_hecke_quad {n : Type*} [Fintype n] [DecidableEq n]
    (S : Matrix n n ℝ) (hS : S * S = 1) (η₀ : ℝ) :
    let q₀ := Real.exp η₀
    (kzLocalMonodromyReal S η₀ - q₀ • 1) * (kzLocalMonodromyReal S η₀ + q₀⁻¹ • 1) = 0 := by
  intro q₀
  have hM : kzLocalMonodromyReal S η₀ =
      ((Real.exp η₀ - Real.exp (-η₀)) / 2) • (1 : Matrix n n ℝ) +
        ((Real.exp η₀ + Real.exp (-η₀)) / 2) • S := by
    unfold kzLocalMonodromyReal kzHalfTurnFundReal
    rw [mul_one, Matrix.mul_add, Matrix.mul_smul, Matrix.mul_smul, Matrix.mul_one, hS, add_comm]
  have hqi : q₀⁻¹ = Real.exp (-η₀) := (Real.exp_neg η₀).symm
  rw [hM, hqi]
  have hL : ((Real.exp η₀ - Real.exp (-η₀)) / 2) • (1 : Matrix n n ℝ) +
      ((Real.exp η₀ + Real.exp (-η₀)) / 2) • S - Real.exp η₀ • 1 =
      (-(Real.exp η₀ + Real.exp (-η₀)) / 2) • (1 - S) := by
    ext i j; simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]; ring
  have hR : ((Real.exp η₀ - Real.exp (-η₀)) / 2) • (1 : Matrix n n ℝ) +
      ((Real.exp η₀ + Real.exp (-η₀)) / 2) • S + Real.exp (-η₀) • 1 =
      ((Real.exp η₀ + Real.exp (-η₀)) / 2) • (1 + S) := by
    ext i j; simp only [Matrix.add_apply, Matrix.smul_apply, smul_eq_mul]; ring
  have hdiff : (1 - S) * (1 + S) = 0 := by
    rw [Matrix.sub_mul, Matrix.one_mul, Matrix.mul_add, Matrix.mul_one, hS]
    abel
  rw [hL, hR, Matrix.smul_mul, Matrix.mul_smul, hdiff, smul_zero, smul_zero]

/-- **Exact Real-Hyperbolic KZ–Hecke Monodromy Trace Agreement on `B_3` (`[2,1]`) and `B_4` (`[2,2]`):**
    at `q₀ = exp(η₀)`, the continuous KZ half-turn monodromy trace around every elementary braid
    generator agrees identically with the Hecke representation trace `q₀ - q₀⁻¹`. -/
theorem kzMonodromy_trace_eq_hecke_real (η₀ : ℝ) :
    let q₀ := Real.exp η₀
    Matrix.trace (kzLocalMonodromyReal (kzOmega01 : Matrix (Fin 2) (Fin 2) ℝ) η₀) =
      Matrix.trace (heckeB3_21_T0 q₀ q₀⁻¹) ∧
    Matrix.trace (kzLocalMonodromyReal (kzOmega12 : Matrix (Fin 2) (Fin 2) ℝ) η₀) =
      Matrix.trace (heckeB3_21_T1 q₀ q₀⁻¹) ∧
    Matrix.trace (kzLocalMonodromyReal (kzOmega01 : Matrix (Fin 2) (Fin 2) ℝ) η₀) =
      Matrix.trace (heckeB4_22_T2 q₀ q₀⁻¹) := by
  intro q₀
  have hprops := kzOmega_involutive_traceless_and_4T (R := ℝ)
  have htr : ∀ (S : Matrix (Fin 2) (Fin 2) ℝ), S * S = 1 → Matrix.trace S = 0 →
      Matrix.trace (kzLocalMonodromyReal S η₀) = q₀ - q₀⁻¹ := by
    intro S hS hSt
    unfold kzLocalMonodromyReal kzHalfTurnFundReal
    rw [mul_one, Matrix.mul_add, Matrix.mul_smul, Matrix.mul_smul, Matrix.mul_one, hS,
      Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul, hSt, Matrix.trace_one,
      Fintype.card_fin, Nat.cast_ofNat, smul_eq_mul, smul_eq_mul, mul_zero, zero_add,
      Real.exp_neg]
    dsimp [q₀]; ring
  rw [htr _ hprops.1 hprops.2.2.2.1, htr _ hprops.2.1 hprops.2.2.2.2.1,
    (heckeB3_21_trace_gen q₀ q₀⁻¹).1, (heckeB3_21_trace_gen q₀ q₀⁻¹).2,
    (heckeB4_22_trace_gen q₀ q₀⁻¹).2.2]
  exact ⟨rfl, rfl, rfl⟩

/-- Complex KZ half-turn fundamental solution `Φ_S(ħ_KZ, t) = cosh(iπħ_KZ t) I + sinh(iπħ_KZ t) S`
    for `q = exp(i π ħ_KZ)`. -/
noncomputable def kzHalfTurnFundComplex {n : Type*} [Fintype n] [DecidableEq n]
    (S : Matrix n n ℂ) (ħKZ : ℂ) (t : ℝ) : Matrix n n ℂ :=
  let θ := Complex.I * Real.pi * ħKZ
  ((Complex.exp (θ * t) + Complex.exp (-(θ * t))) / 2) • (1 : Matrix n n ℂ) +
    ((Complex.exp (θ * t) - Complex.exp (-(θ * t))) / 2) • S

/-- Complex KZ half-turn monodromy `M_KZ(ħ_KZ) = S · Φ_S(ħ_KZ, 1)`. -/
noncomputable def kzLocalMonodromyComplex {n : Type*} [Fintype n] [DecidableEq n]
    (S : Matrix n n ℂ) (ħKZ : ℂ) : Matrix n n ℂ :=
  S * kzHalfTurnFundComplex S ħKZ 1

/-- **Exact Complex KZ–Hecke Monodromy Trace Agreement at `q = exp(i π ħ_KZ)`**
    across all elementary generators of `B_3` (`[2,1]`) and `B_4` (`[2,2]`). -/
theorem kzMonodromy_trace_eq_hecke_complex (ħKZ : ℂ) :
    let q := Complex.exp (Complex.I * Real.pi * ħKZ)
    Matrix.trace (kzLocalMonodromyComplex (kzOmega01 : Matrix (Fin 2) (Fin 2) ℂ) ħKZ) =
      Matrix.trace (heckeB3_21_T0 q q⁻¹) ∧
    Matrix.trace (kzLocalMonodromyComplex (kzOmega12 : Matrix (Fin 2) (Fin 2) ℂ) ħKZ) =
      Matrix.trace (heckeB3_21_T1 q q⁻¹) ∧
    Matrix.trace (kzLocalMonodromyComplex (kzOmega01 : Matrix (Fin 2) (Fin 2) ℂ) ħKZ) =
      Matrix.trace (heckeB4_22_T2 q q⁻¹) := by
  intro q
  have hprops := kzOmega_involutive_traceless_and_4T (R := ℂ)
  have htr : ∀ (S : Matrix (Fin 2) (Fin 2) ℂ), S * S = 1 → Matrix.trace S = 0 →
      Matrix.trace (kzLocalMonodromyComplex S ħKZ) = q - q⁻¹ := by
    intro S hS hSt
    unfold kzLocalMonodromyComplex kzHalfTurnFundComplex
    simp only [Complex.ofReal_one, mul_one]
    rw [Matrix.mul_add, Matrix.mul_smul, Matrix.mul_smul, Matrix.mul_one, hS,
      Matrix.trace_add, Matrix.trace_smul, Matrix.trace_smul, hSt, Matrix.trace_one,
      Fintype.card_fin, Nat.cast_ofNat, smul_eq_mul, smul_eq_mul, mul_zero, zero_add,
      Complex.exp_neg]
    dsimp [q]; ring
  rw [htr _ hprops.1 hprops.2.2.2.1, htr _ hprops.2.1 hprops.2.2.2.2.1,
    (heckeB3_21_trace_gen q q⁻¹).1, (heckeB3_21_trace_gen q q⁻¹).2,
    (heckeB4_22_trace_gen q q⁻¹).2.2]
  exact ⟨rfl, rfl, rfl⟩

/-- **Convention-D Two-Row Markov Trace Wedderburn Synthesis on `H_3(q)` and `H_4(q)` (`qou-ni4b`):**
    over any `[Field K]` with `q ≠ 0` and `q² + 1 ≠ 0`, weighting the 1-row (`[n]`) and 2-row
    (`[2,1]` at `n = 3`; `[3,1]` and `[2,2]` at `n = 4`) traces by the rank-2 colour-twisted
    Convention-D Ocneanu weights reproduces `1` on the identity and `z_D = q³ / (q² + 1)` on the
    elementary braid generators. -/
theorem conventionD_twoRow_generator_synthesis {K : Type*} [Field K]
    (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    let y3 := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2
    let y21 := q ^ 2 / (q ^ 2 + 1) ^ 2
    let y4 := (1 + q ^ 2 + q ^ 4 + q ^ 6 + q ^ 8) / (q ^ 2 + 1) ^ 4
    let y31 := q ^ 2 * (1 + q ^ 2 + q ^ 4) / (q ^ 2 + 1) ^ 4
    let y22 := q ^ 4 / (q ^ 2 + 1) ^ 4
    let zD := q ^ 3 / (q ^ 2 + 1)
    (y3 * 1 + y21 * 2 = 1) ∧
    (y3 * q + y21 * Matrix.trace (heckeB3_21_T0 q q⁻¹) = zD) ∧
    (y4 * 1 + y31 * 3 + y22 * 2 = 1) ∧
    (y4 * q + y31 * Matrix.trace (heckeB4_31_T0 q q⁻¹) +
      y22 * Matrix.trace (heckeB4_22_T0 q q⁻¹) = zD) := by
  intro y3 y21 y4 y31 y22 zD
  have htr31 : Matrix.trace (heckeB4_31_T0 q q⁻¹) = 2 * q - q⁻¹ := by
    simp [heckeB4_31_T0, Matrix.trace_fin_three]; ring
  rw [(heckeB3_21_trace_gen q q⁻¹).1, (heckeB4_22_trace_gen q q⁻¹).1, htr31]
  dsimp [y3, y21, y4, y31, y22, zD]
  refine ⟨by field_simp; ring, by field_simp; ring, by field_simp; ring, by field_simp; ring⟩

end ContinuousKZMonodromy

end TwoRowKZAndHecke

end QOU.Torsion.ChenMultiplicativeIntegralBridge
