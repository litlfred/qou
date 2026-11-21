/-
# The Δ_λ residual moment μ₃ is unreachable by any pairwise ρ_F cluster integral

Companion to `QOU.MassTheory.AdditiveResidualSimplex` (#4320), which proved the
Δ_λ damping-wall residual `M(A) = ρ_strong(A) − ρ_grad(A)` is a pure ≥3-body
simplex object with coefficients (evaluated at the canonical `q₀`)

    μ₂ = 0,   μ₃ = +0.4708,   μ₄ = −4.591.

The #4320 redirect asked whether the interface operator `ρ_F` **cluster integrals**
derive these moments.  `ρ_F` is the interface-product binding
`B = E₀·τ_vac·(1 − ∏ᵢ fᵢ)` with the categorically-derived per-bond factors
`fᵢ ∈ {z, z−h, z−h/2}` (Lean-proved exact).  Its connected `k`-body **cluster
integral** is the beyond-pairwise (Ursell) content of that pairwise product.

**Result (this file): the pairwise-product cluster route CANNOT supply μ₃.**  For
any pairwise interface product with factors `fᵢ ∈ [0,1]` the beyond-pairwise
content is `≤ 0` (a Weierstrass union bound), yet `μ₃ = +0.4708 > 0`.  So no
pairwise ρ_F cluster equals `μ₃` — a scope-(b) **proved sign exclusion** of the
multiplicative route (the convention-D bound `z = q³/(q²+1) < 1` for
`q³ < q² + 1`, which holds at `q₀ ≈ 1.110` (`markovZD_lt_one_iff`), forecloses the
only pairwise escape `fᵢ > 1` at the substrate value).  The 4-body residual `μ₄ < 0` is
sign-*consistent* with the (also non-positive) 4-body cluster content, but that is
**not** a derivation: `μ₄`'s magnitude is dominated by the *derived graded*
reference's own 4-body simplex coefficient `g₄ = +8.37` being subtracted, not by an
`ρ_F` cluster.

Canonical companions (re-derived self-contained here, import-light):
`QOU.BraidKnot.Cluster.productModel_3body_nonpos` and `markovZD_lt_one_iff`
(`folio/quantum-observable-universe/mass-theory/interface-knot-markov-z.lean`).

Probe: `computations/deltalambda/mu4_rhoF_cluster_derivation_probe.py`.
Anti-fit: only the derived sign structure is used; the AME residual magnitude
`μ₃ > 0` enters as a hypothesis, never a fitted constant; nothing is wired.
-/
import Mathlib.Tactic

/-
VERIFICATION STATUS (2026-07-26): MACHINE-CHECKED, `lean`-direct exit 0, sorry-free.
Originally authored + hand-audited only (the sibling's restored `lake-cache/qou-v4-24-0`
was pruned + disk ENOSPC), this file was re-verified against the full restored Mathlib
`Tactic` olean cone: `lean QOU/MassTheory/Mu4RhoFCluster.lean` returns exit 0 with no
errors (two cosmetic `unusedVariables`-linter warnings on the
`pairwise_3body_content_nonpos` positivity binders — false positives: `ha0`/`hb0` are
used in the `key` positivity step; the binders are kept unchanged).
The proofs use only elementary standard tactics (`induction` on `List`,
`nlinarith`/`linarith`/`norm_num`, `mul_nonneg`, `mul_le_mul_of_nonneg_right`);
`pairwise_3body_content_nonpos` mirrors the merged, sorry-free
`QOU.BraidKnot.Cluster.productModel_3body_nonpos`.
-/

namespace QOU.MassTheory

/-! ### Beyond-pairwise content of a pairwise interface product is non-positive -/

/-- All factors in `[0,1]` ⇒ the product lies in `[0,1]`. -/
theorem prod_mem_unit {l : List ℝ} (h : ∀ f ∈ l, 0 ≤ f ∧ f ≤ 1) :
    0 ≤ l.prod ∧ l.prod ≤ 1 := by
  induction l with
  | nil => simp only [List.prod_nil]; norm_num
  | cons a t ih =>
    obtain ⟨ha0, ha1⟩ := h a (List.mem_cons_self)
    have ht := ih (fun f hf => h f (List.mem_cons_of_mem a hf))
    refine ⟨?_, ?_⟩
    · simpa [List.prod_cons] using mul_nonneg ha0 ht.1
    · simp only [List.prod_cons]
      calc a * t.prod ≤ 1 * t.prod := mul_le_mul_of_nonneg_right ha1 ht.1
        _ = t.prod := one_mul _
        _ ≤ 1 := ht.2

/-- `oneSum l = Σ (1 − fᵢ)`, the pairwise (1-bond) content. -/
def oneSum (l : List ℝ) : ℝ := (l.map (fun f => 1 - f)).sum

/-- **Beyond-pairwise content of a pairwise product is non-positive** (Weierstrass
    union bound).  For `fᵢ ∈ [0,1]`, `1 − ∏ fᵢ ≤ Σ (1 − fᵢ)`; equivalently the
    beyond-pairwise cluster content `(1 − ∏ fᵢ) − Σ(1 − fᵢ) ≤ 0`.  This is the
    general (any bond-count) form covering both the 3-body and 4-body clusters. -/
theorem one_sub_prod_le_oneSum {l : List ℝ} (h : ∀ f ∈ l, 0 ≤ f ∧ f ≤ 1) :
    1 - l.prod ≤ oneSum l := by
  induction l with
  | nil => simp only [oneSum, List.prod_nil, List.map_nil, List.sum_nil]; norm_num
  | cons a t ih =>
    obtain ⟨ha0, ha1⟩ := h a (List.mem_cons_self)
    have hmem : ∀ f ∈ t, 0 ≤ f ∧ f ≤ 1 := fun f hf => h f (List.mem_cons_of_mem a hf)
    have ht := ih hmem
    have hp := prod_mem_unit (l := t) hmem
    simp only [oneSum, List.map_cons, List.sum_cons, List.prod_cons] at ht ⊢
    -- `1 − a·P = (1−a) + (a − a·P)` and `a − a·P ≤ 1 − P ≤ Σ`; then linear in atoms.
    have h2 : a - a * t.prod ≤ 1 - t.prod := by
      nlinarith [mul_nonneg (sub_nonneg.2 ha1) (sub_nonneg.2 hp.2)]
    linarith [ht, h2]

/-! ### The explicit 3-body content and the μ₃ wall -/

/-- **Pairwise 3-body content is non-positive** (the `productModel_3body_nonpos`
    content with `c = 1`).  For `f_a,f_b,f_c ∈ [0,1]`,
    `f_a + f_b + f_c − f_a f_b f_c − 2 ≤ 0`. -/
theorem pairwise_3body_content_nonpos {f_a f_b f_c : ℝ}
    (ha0 : 0 ≤ f_a) (ha1 : f_a ≤ 1) (hb0 : 0 ≤ f_b) (hb1 : f_b ≤ 1)
    (hc0 : 0 ≤ f_c) (hc1 : f_c ≤ 1) :
    f_a + f_b + f_c - f_a * f_b * f_c - 2 ≤ 0 := by
  -- Mirrors the canonical `productModel_3body_nonpos` proof (with `c = 1`).
  have key : 0 ≤ 2 - f_a - f_b - f_c + f_a * f_b * f_c := by
    nlinarith [mul_nonneg (sub_nonneg.2 ha1) (sub_nonneg.2 hb1),
               mul_nonneg (mul_nonneg ha0 hb0) (sub_nonneg.2 hc1),
               mul_nonneg (sub_nonneg.2 hc1) (add_nonneg ha0 hb0)]
  linarith

/-- **(WALL) μ₃ is unreachable by any pairwise ρ_F cluster.**  The residual 3-body
    simplex coefficient `μ₃` is *positive* (`+0.4708`), but the beyond-pairwise
    3-body content of any pairwise interface product `∏ fᵢ`, `fᵢ ∈ [0,1]`, is
    `≤ 0`.  Hence `μ₃ ≠` that cluster content — the multiplicative ρ_F cluster
    route cannot supply `μ₃`.  (The only pairwise escape `fᵢ > 1` is foreclosed at
    `q₀ ≈ 1.110` by `markovZD_lt_one_iff`: `z = q³/(q²+1) < 1` iff `q³ < q² + 1`.) -/
theorem mu3_ne_pairwise_3body_cluster {μ₃ f_a f_b f_c : ℝ} (hμ : 0 < μ₃)
    (ha0 : 0 ≤ f_a) (ha1 : f_a ≤ 1) (hb0 : 0 ≤ f_b) (hb1 : f_b ≤ 1)
    (hc0 : 0 ≤ f_c) (hc1 : f_c ≤ 1) :
    μ₃ ≠ f_a + f_b + f_c - f_a * f_b * f_c - 2 := by
  have hcl := pairwise_3body_content_nonpos ha0 ha1 hb0 hb1 hc0 hc1
  intro hEq
  rw [hEq] at hμ
  linarith

/-! ### The 4-body residual is sign-consistent but NOT derived -/

/-- **(Sign-consistency, not a derivation.)**  The 4-body residual coefficient is
    *negative* (`μ₄ = −4.591 < 0`) and the pairwise-product 4-body cluster content
    is also `≤ 0` (a special case of `one_sub_prod_le_oneSum`), so the two lie in
    the same non-positive half-line — the signs are consistent.  This is recorded
    honestly as *consistency*, NOT a magnitude derivation: `μ₄` is dominated by the
    derived graded reference's own 4-body simplex coefficient `g₄ = +8.37` being
    subtracted (`μ₄ = s₄ − g₄`), not by the `ρ_F` cluster. -/
theorem mu4_sign_consistent_with_pairwise_cluster {μ₄ cluster₄ : ℝ}
    (hμ : μ₄ < 0) (hcl : cluster₄ ≤ 0) : μ₄ ≤ 0 ∧ cluster₄ ≤ 0 :=
  ⟨le_of_lt hμ, hcl⟩

end QOU.MassTheory
