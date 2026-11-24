import Mathlib.Analysis.Normed.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

namespace QOU.MathlibExt.ListProdPerturbation

variable {R : Type*} [NormedRing R] {ι : Type*}

/-- Right-closure of a set under a family of multipliers propagates to list products. -/
theorem mul_prod_mem (S : Set R) (P : ι → R) (hcl : ∀ g ∈ S, ∀ x, g * P x ∈ S) :
    ∀ (l : List ι) (g : R), g ∈ S → g * (l.map P).prod ∈ S := by
  intro l
  induction l with
  | nil => intro g hg; simpa using hg
  | cons x l ih =>
    intro g hg
    simpa [List.map_cons, List.prod_cons, mul_assoc] using ih (g * P x) (hcl g hg x)

/-- Product perturbation bound: if every element of `S` has norm at most `M`, `S` is closed
under right multiplication by each `P x`, `1 ∈ S`, and `‖A x - P x‖ ≤ δ`, then for `g ∈ S`
the perturbed product differs from the unperturbed one by at most `M((1+Mδ)^n - 1)`. -/
theorem prod_perturb (S : Set R) (P A : ι → R) (M δ : ℝ) (hδ : 0 ≤ δ)
    (h1 : (1 : R) ∈ S) (hS : ∀ g ∈ S, ‖g‖ ≤ M) (hcl : ∀ g ∈ S, ∀ x, g * P x ∈ S)
    (hAP : ∀ x, ‖A x - P x‖ ≤ δ) :
    ∀ (l : List ι) (g : R), g ∈ S →
      ‖g * (l.map A).prod - g * (l.map P).prod‖ ≤ M * ((1 + M * δ) ^ l.length - 1) := by
  have hM : 0 ≤ M := (norm_nonneg _).trans (hS 1 h1)
  intro l
  induction l with
  | nil => intro g _; simp
  | cons x l ih =>
    intro g hg
    set Z := (l.map A).prod
    set Y := (l.map P).prod
    set e := M * ((1 + M * δ) ^ l.length - 1)
    have hgP : g * P x ∈ S := hcl g hg x
    have hIH : ‖g * P x * Z - g * P x * Y‖ ≤ e := ih _ hgP
    have hZY : ‖Z - Y‖ ≤ e := by simpa using ih 1 h1
    have hY : ‖Y‖ ≤ M := by simpa using hS _ (mul_prod_mem S P hcl l 1 h1)
    have hZ : ‖Z‖ ≤ M * (1 + M * δ) ^ l.length := by
      have : ‖Z‖ ≤ ‖Z - Y‖ + ‖Y‖ := by
        simpa using norm_add_le (Z - Y) Y
      have : ‖Z‖ ≤ e + M := by linarith
      simp only [e] at this; nlinarith
    have hg : ‖g‖ ≤ M := hS g hg
    have hsplit : g * (A x * Z) - g * (P x * Y)
        = (g * P x * Z - g * P x * Y) + g * (A x - P x) * Z := by noncomm_ring
    have h2 : ‖g * (A x - P x) * Z‖ ≤ M * δ * (M * (1 + M * δ) ^ l.length) := by
      calc ‖g * (A x - P x) * Z‖ ≤ ‖g‖ * ‖A x - P x‖ * ‖Z‖ := by
            refine (norm_mul_le _ _).trans ?_
            exact mul_le_mul_of_nonneg_right (norm_mul_le _ _) (norm_nonneg _)
        _ ≤ M * δ * (M * (1 + M * δ) ^ l.length) := by
            apply mul_le_mul (mul_le_mul hg (hAP x) (norm_nonneg _) hM) hZ (norm_nonneg _)
            exact mul_nonneg hM hδ
    simp only [List.map_cons, List.prod_cons, List.length_cons]
    rw [hsplit]
    calc ‖(g * P x * Z - g * P x * Y) + g * (A x - P x) * Z‖
        ≤ ‖g * P x * Z - g * P x * Y‖ + ‖g * (A x - P x) * Z‖ := norm_add_le _ _
      _ ≤ e + M * δ * (M * (1 + M * δ) ^ l.length) := add_le_add hIH h2
      _ = M * ((1 + M * δ) ^ (l.length + 1) - 1) := by simp only [e]; ring

/-- Bernoulli-type bound: `(1+x)^n (1 - n x) ≤ 1` for `x ≥ 0`. -/
theorem one_add_pow_mul_one_sub_le (x : ℝ) (hx : 0 ≤ x) :
    ∀ n : ℕ, (1 + x) ^ n * (1 - n * x) ≤ 1 := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    have hp : 0 ≤ (1 + x) ^ n := pow_nonneg (by linarith) n
    have key : (1 + x) * (1 - (n + 1 : ℕ) * x) ≤ 1 - n * x := by
      push_cast; nlinarith [sq_nonneg x, mul_nonneg (Nat.cast_nonneg n) (sq_nonneg x)]
    calc (1 + x) ^ (n + 1) * (1 - ((n + 1 : ℕ) : ℝ) * x)
        = (1 + x) ^ n * ((1 + x) * (1 - (n + 1 : ℕ) * x)) := by ring
      _ ≤ (1 + x) ^ n * (1 - n * x) := mul_le_mul_of_nonneg_left key hp
      _ ≤ 1 := ih

/-- If `n·M·δ·(M+1) ≤ 1` (with `M > 0`, `δ ≥ 0`), then `M((1+Mδ)^n - 1) ≤ 1`. -/
theorem perturb_le_one (M δ : ℝ) (n : ℕ) (hM : 0 < M) (hδ : 0 ≤ δ)
    (h : n * M * δ * (M + 1) ≤ 1) : M * ((1 + M * δ) ^ n - 1) ≤ 1 := by
  set x := M * δ with hxdef
  have hx : 0 ≤ x := mul_nonneg hM.le hδ
  have hB := one_add_pow_mul_one_sub_le x hx n
  have hnx : n * x * (M + 1) ≤ 1 := by simp only [x]; linarith [h]
  -- 1 - n x ≥ M/(M+1) > 0
  have hlow : M / (M + 1) ≤ 1 - n * x := by
    rw [div_le_iff₀ (by linarith)]; nlinarith
  have hpos : 0 < M / (M + 1) := div_pos hM (by linarith)
  have hp : 0 ≤ (1 + x) ^ n := pow_nonneg (by linarith) n
  have h3 : (1 + x) ^ n * (M / (M + 1)) ≤ 1 :=
    (mul_le_mul_of_nonneg_left hlow hp).trans hB
  have h4 : (1 + x) ^ n * M ≤ M + 1 := by
    rw [mul_div_assoc', div_le_iff₀ (by linarith)] at h3; linarith
  nlinarith

end QOU.MathlibExt.ListProdPerturbation
