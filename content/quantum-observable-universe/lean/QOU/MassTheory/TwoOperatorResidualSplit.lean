/-
# The Δ_λ residual is a TWO-operator (binding − saturation) object

Capstone of the three just-merged cluster-sign walls:

* `QOU.MassTheory.BorromeanThreeBodyCluster` (#4360) — the A=3 Brunnian/Borromean
  binding cluster `c₃ = E₀·(1 − τ_Borr)` is **non-negative** (`≥ 0`, strictly
  `> 0` in the physical regime).  Reused here via `borromean_cluster_nonneg`.
* `QOU.MassTheory.Mu4RhoFCluster` (#4354) — the beyond-pairwise content of any
  *multiplicative* interface product `1 − ∏ᵢ fᵢ` (`fᵢ ∈ [0,1]`) is
  **non-positive** (`≤ 0`).  Reused here via `pairwise_3body_content_nonpos`
  (mirror of the canonical `QOU.BraidKnot.Cluster.productModel_3body_nonpos`).
* `QOU.MassTheory.HeliumFourBodyCluster` (#4376) — the A=4 Brunnian binding
  cluster is again `≥ 0` (`brunnian4Cluster_nonneg`), while the forward
  AME−model residual `μ₄ = −4.591 < 0` (`mu4Residual_neg`); the two are
  sign-incompatible (`sign_swap_a3_a4`).

**The finding formalized here.**  The per-isotope binding residual moment
sequence `{μₖ}` (forward AME−model, 0-fit: `μ₂ = 0`, `μ₃ = +0.4708`,
`μ₄ = −4.591`) is NOT one closing coefficient.  It is a **signed sum of two
operators of opposite sign**:

* a **binding** operator `B` — the Brunnian/Borromean trace deficit — which is
  provably **non-negative** and supplies the positive odd moment `μ₃ > 0`;
* a **saturation** operator whose contribution is provably **non-positive**
  (the closed / multiplicative supermultiplet term); its magnitude `S ≥ 0` is
  subtracted, and it supplies the negative even moment `μ₄ < 0`.

Writing `μₖ = Bₖ − Sₖ` with `Bₖ ≥ 0` (binding) and `Sₖ ≥ 0` (saturation
magnitude), the **sign** of `μₖ` selects which operator dominates:

    μ₃ > 0  ⟺  B₃ > S₃   (binding-dominated)
    μ₄ < 0  ⟺  S₄ > B₄   (saturation-dominated)

and — the structural payoff — **no single-sign operator reproduces both**: a
pure-binding model (`S = 0`) is `≥ 0` everywhere and can never equal `μ₄ < 0`;
a pure-saturation model (`B = 0`) is `≤ 0` everywhere and can never equal
`μ₃ > 0`.  Two operators of opposite sign are structurally necessary.  This is
exactly what the two proved cluster-sign lemmas force.

**Scope (honest).**  What is DERIVED here, purely by composing the already-proved
sign lemmas: (i) the binding value `B` is non-negative (`borromean_cluster_nonneg`
/ `brunnian4Cluster_nonneg`); (ii) the saturation magnitude `S` is non-negative
(`pairwise_3body_content_nonpos`, negated); (iii) `μ₄ < 0` (`mu4Residual_neg`);
(iv) the sign of `μₖ` selects the dominant operator; (v) two operators of
opposite sign are necessary.  What is NOT claimed: that the *concrete* operator
*magnitudes* sum to the exact AME `μₖ`.  The magnitude closure (the per-λ `Δ_λ`
value) remains the OPEN Δ_λ gate — the bare-`H₃` Borromean scale `~0.006 MeV`
is orders below the `~1.5 MeV` target (#4360 scope-(a) note), and any magnitude
tuned to the target would be a FIT and is NOT made here.  Accordingly the
two-operator identity `μ = B − S` enters the domination theorems as a modeling
hypothesis (`hmodel`), never as a fitted equation; `μ₃`'s numeric value enters
no proof, and 0 free parameters are introduced.

Anti-fit / anti-laundering: no `μₖ` is inverted to fix any coefficient; the sign
content is composed from the existing sorry-free lemmas, not assumed as a class
field.

Base ring (§7c): `ℝ`, because every statement is an archimedean ordering/sign
fact (`0 ≤`, `<`, `≠` against a signed numeric target) — matching the three
sibling wall files.
-/
import Mathlib.Tactic
import QOU.MassTheory.BorromeanThreeBodyCluster
import QOU.MassTheory.Mu4RhoFCluster
import QOU.MassTheory.HeliumFourBodyCluster

namespace QOU.MassTheory

/-! ### A signed split of a residual moment into binding minus saturation -/

/-- A **two-operator residual split**: a residual moment realized as
`residual = B − S`, where `B ≥ 0` is a *binding* contribution (a Brunnian trace
deficit, provably non-negative) and `S ≥ 0` is a *saturation* magnitude (the
negative of a provably non-positive multiplicative cluster).  The two operators
have opposite sign by construction — that is the whole content. -/
structure SignedResidualSplit where
  /-- Binding contribution (Brunnian/Borromean deficit); non-negative. -/
  B : ℝ
  /-- Saturation magnitude (`= −` multiplicative cluster); non-negative. -/
  S : ℝ
  hB : 0 ≤ B
  hS : 0 ≤ S

/-- The realized residual moment `μ = B − S`. -/
def SignedResidualSplit.residual (r : SignedResidualSplit) : ℝ := r.B - r.S

/-! ### Sign selection: the sign of `μ` picks the dominant operator -/

/-- **Binding-dominated ⟺ positive residual.**  `μ = B − S > 0 ↔ S < B`. -/
theorem residual_pos_iff (r : SignedResidualSplit) : 0 < r.residual ↔ r.S < r.B := by
  unfold SignedResidualSplit.residual; exact sub_pos

/-- **Saturation-dominated ⟺ negative residual.**  `μ = B − S < 0 ↔ B < S`. -/
theorem residual_neg_iff (r : SignedResidualSplit) : r.residual < 0 ↔ r.B < r.S := by
  unfold SignedResidualSplit.residual; exact sub_neg

/-! ### A single-sign operator is `≥ 0` (pure binding) or `≤ 0` (pure saturation) -/

/-- **Pure binding is non-negative.**  If the saturation operator is switched off
(`S = 0`), the residual is just the binding value `B ≥ 0`, hence `≥ 0`.  A
single non-negative operator can never realize a negative moment. -/
theorem pure_binding_nonneg (r : SignedResidualSplit) (hpure : r.S = 0) :
    0 ≤ r.residual := by
  unfold SignedResidualSplit.residual; rw [hpure]; simpa using r.hB

/-- **Pure saturation is non-positive.**  If the binding operator is switched off
(`B = 0`), the residual is `−S ≤ 0`.  A single non-positive operator can never
realize a positive moment. -/
theorem pure_saturation_nonpos (r : SignedResidualSplit) (hpure : r.B = 0) :
    r.residual ≤ 0 := by
  unfold SignedResidualSplit.residual; rw [hpure]; simpa using neg_nonpos.2 r.hS

/-! ### The two-operator necessity: neither single-sign operator spans both signs -/

/-- **A binding-only model cannot reach `μ₄`.**  `μ₄ = −4.591 < 0`
(`mu4Residual_neg`, #4376), but a pure-binding residual is `≥ 0`
(`pure_binding_nonneg`).  So no `S = 0` split equals `μ₄`. -/
theorem binding_alone_ne_mu4 (r : SignedResidualSplit) (hpure : r.S = 0) :
    r.residual ≠ mu4Residual := by
  have hnn : 0 ≤ r.residual := pure_binding_nonneg r hpure
  have hneg : mu4Residual < 0 := mu4Residual_neg
  intro hEq; rw [hEq] at hnn; linarith

/-- **A saturation-only model cannot reach `μ₃ > 0`.**  A pure-saturation residual
is `≤ 0` (`pure_saturation_nonpos`), but `μ₃ = +0.4708 > 0`.  So no `B = 0` split
equals `μ₃`. -/
theorem saturation_alone_ne_mu3 {μ₃ : ℝ} (hμ : 0 < μ₃)
    (r : SignedResidualSplit) (hpure : r.B = 0) :
    r.residual ≠ μ₃ := by
  have hnp : r.residual ≤ 0 := pure_saturation_nonpos r hpure
  intro hEq; rw [hEq] at hnp; linarith

/-! ### Concrete operators: `B` from the PROVED Borromean lemma, `S` from the PROVED multiplicative lemma -/

/-- The **saturation magnitude** of the multiplicative 3-body interface product:
`S = 2 − f_a − f_b − f_c + f_a f_b f_c = −(f_a + f_b + f_c − f_a f_b f_c − 2)`,
i.e. minus the (`≤ 0`) beyond-pairwise cluster content. -/
def saturationMagnitude (f_a f_b f_c : ℝ) : ℝ := 2 - f_a - f_b - f_c + f_a * f_b * f_c

/-- **The saturation magnitude is non-negative** — a direct reuse of the merged
sign wall `pairwise_3body_content_nonpos` (#4354): the multiplicative cluster
content `f_a + f_b + f_c − f_a f_b f_c − 2 ≤ 0`, so its negative is `≥ 0`. -/
theorem saturationMagnitude_nonneg {f_a f_b f_c : ℝ}
    (ha0 : 0 ≤ f_a) (ha1 : f_a ≤ 1) (hb0 : 0 ≤ f_b) (hb1 : f_b ≤ 1)
    (hc0 : 0 ≤ f_c) (hc1 : f_c ≤ 1) : 0 ≤ saturationMagnitude f_a f_b f_c := by
  have hcl := pairwise_3body_content_nonpos ha0 ha1 hb0 hb1 hc0 hc1
  unfold saturationMagnitude; linarith

/-- **The concrete two-operator split** built entirely from the proved sign
lemmas: the binding value `B = E₀·(1 − τ_Borr)` is non-negative by the merged
`borromean_cluster_nonneg` (#4360); the saturation magnitude
`S = saturationMagnitude f_a f_b f_c` is non-negative by
`saturationMagnitude_nonneg` (which reuses `pairwise_3body_content_nonpos`,
#4354).  This exhibits `B − S` as a genuine binding-minus-saturation object with
BOTH signs derived — not assumed. -/
noncomputable def borromeanMinusSaturation
    (E0 h f_a f_b f_c : ℝ) (hE : 0 ≤ E0)
    (ha0 : 0 ≤ f_a) (ha1 : f_a ≤ 1) (hb0 : 0 ≤ f_b) (hb1 : f_b ≤ 1)
    (hc0 : 0 ≤ f_c) (hc1 : f_c ≤ 1) : SignedResidualSplit :=
  { B := E0 * (1 - tauBorromean h)
    S := saturationMagnitude f_a f_b f_c
    hB := borromean_cluster_nonneg hE
    hS := saturationMagnitude_nonneg ha0 ha1 hb0 hb1 hc0 hc1 }

/-- The A=4 binding half of the split, built from the merged
`brunnian4Cluster_nonneg` (#4376): `B = brunnian4Cluster E₀ τ h ≥ 0` whenever the
level trace lies at or below the unlink (`τ h ≤ 1`), paired with any non-negative
saturation magnitude. -/
noncomputable def brunnian4MinusSaturation
    (E0 h S : ℝ) (τ : ℝ → ℝ) (hE : 0 ≤ E0) (hτ : τ h ≤ 1) (hS : 0 ≤ S) :
    SignedResidualSplit :=
  { B := brunnian4Cluster E0 τ h
    S := S
    hB := brunnian4Cluster_nonneg hE hτ
    hS := hS }

/-! ### Weak existence: some signed split always exists (the STRONG magnitude form is the open Δ_λ gate) -/

/-- **Every real moment admits *some* signed split.**  This is the *weak* form —
it says nothing about the physical operator magnitudes; it merely records that
`μ = B − S` with `B, S ≥ 0` is always solvable (`B = max μ 0`, `S = max (−μ) 0`).
The STRONG form — that the concrete Borromean binding and multiplicative
saturation magnitudes sum to the exact AME `μₖ` — is the OPEN Δ_λ magnitude
closure and is deliberately NOT proved here. -/
theorem signed_split_exists (μ : ℝ) :
    ∃ B S : ℝ, 0 ≤ B ∧ 0 ≤ S ∧ μ = B - S := by
  rcases le_or_gt 0 μ with h | h
  · exact ⟨μ, 0, h, le_refl 0, by ring⟩
  · exact ⟨0, -μ, le_refl 0, by linarith, by ring⟩

/-! ### Capstone: the residual moment sequence is a two-operator object -/

/-- **(CAPSTONE) The Δ_λ residual is a TWO-operator (binding − saturation)
object.**  Model the A=3 moment `μ₃ > 0` and the A=4 moment `μ₄ = mu4Residual`
each as a signed split (`hmodel`).  Then, purely from the proved sign structure:

1. **A=3 is binding-dominated** — `μ₃ > 0` forces the binding value above the
   saturation magnitude (`S₃ < B₃`), so the positive odd moment is carried by the
   non-negative Brunnian/Borromean operator (`borromean_cluster_nonneg`, #4360).
2. **A=4 is saturation-dominated** — `μ₄ < 0` (`mu4Residual_neg`, #4376) forces
   the saturation magnitude above the binding value (`B₄ < S₄`), so the negative
   even moment is carried by the non-positive multiplicative operator
   (`pairwise_3body_content_nonpos`, #4354).
3. **Two operators of opposite sign are necessary** — no single-sign model spans
   both: a binding-only (`S = 0`, hence `≥ 0`) split can never equal `μ₄ < 0`,
   and a saturation-only (`B = 0`, hence `≤ 0`) split can never equal `μ₃ > 0`.

The sign pattern (`μ₃ > 0` selects binding, `μ₄ < 0` selects saturation) is
exactly what the two proved cluster-sign lemmas force.  This is the structural
`sign_swap_a3_a4` (#4376) read as a *decomposition*: the residual is neither the
binding operator alone nor the saturation operator alone, but their signed
difference. -/
theorem residual_is_two_operator
    (r₃ r₄ : SignedResidualSplit) {μ₃ : ℝ}
    (hμ₃ : 0 < μ₃) (h3model : r₃.residual = μ₃)
    (h4model : r₄.residual = mu4Residual) :
    -- 1. A=3 binding-dominated
    (r₃.S < r₃.B) ∧
    -- 2. A=4 saturation-dominated
    (r₄.B < r₄.S) ∧
    -- 3a. binding alone cannot reach μ₄ < 0
    (∀ rb : SignedResidualSplit, rb.S = 0 → rb.residual ≠ mu4Residual) ∧
    -- 3b. saturation alone cannot reach μ₃ > 0
    (∀ rs : SignedResidualSplit, rs.B = 0 → rs.residual ≠ μ₃) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · -- μ₃ > 0 ⇒ S₃ < B₃
    have h3pos : 0 < r₃.residual := by rw [h3model]; exact hμ₃
    exact (residual_pos_iff r₃).mp h3pos
  · -- μ₄ < 0 ⇒ B₄ < S₄
    have h4neg : r₄.residual < 0 := by rw [h4model]; exact mu4Residual_neg
    exact (residual_neg_iff r₄).mp h4neg
  · exact fun rb hb => binding_alone_ne_mu4 rb hb
  · exact fun rs hb => saturation_alone_ne_mu3 hμ₃ rs hb

end QOU.MassTheory
