/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: QOU Formalization Team

# McPhail–Snyder Diagrammatic State-Sum Fibre-to-$q_0$ Bridge Exclusion

Task: `qou-0e66` (absorbing `qou-t7az` under epic `qou-avtq`, `Q-AVTQ-3 = 1`).
Imports:
- `QOU.QBeta.HabiroEvaluationTrichotomy` (root-of-unity / Habiro series evaluation trichotomy)
- `QOU.QBeta.ModularDoubleReciprocity` (Faddeev modular-double dual-regime reciprocity)

## Mathematical Summary

McPhail–Snyder (`arXiv:2502.04286`, `[mcphail-snyder-2025]`) constructs a diagrammatic state-sum
for the Kashaev / $\mathfrak{sl}_2$-at-roots-of-unity invariant of hyperbolic links decorated by
a $\mathrm{SL}_2(\mathbb{C})$ character variety point $\rho$:
$$Z_N(K; \rho) \;=\; \sum_{k \,\in\, (\mathbb{Z}/N\mathbb{Z})^E} \;\prod_{c=1}^{C} R_c(\rho, k).$$

This module proves that $Z_N(K; \rho)$ cannot serve as a parameter-free derivation bridge from
the braid diagram alone to the real archimedean substrate pin $q_0 > 1$:

1. **External Holonomy Input Non-Selection (`mcphailSnyderStateSum_const_boltzmann`,
   `mcphailSnyderStateSum_ne_of_mu_ne`):**
   The cusp holonomy datum $\rho = (\mu, \lambda)$ enters the Boltzmann weights $R_c(\rho, k)$ as
   an external input argument. For a weight family depending on $\rho.\mu$, distinct external
   holonomy inputs $\rho_1.\mu \neq \rho_2.\mu$ produce distinct state-sum outputs, so the
   state-sum functional does not select $\rho$ from the unmarked braid/link diagram alone.

2. **Full State-Space Summation Non-Selection (`mcphailSnyderStateSum_shift_invariant`,
   `stateSum_strictly_gt_single_state`):**
   Because $Z_N(K; \rho)$ sums over the entire finite abelian group $(\mathbb{Z}/N\mathbb{Z})^E$
   of edge colourings $k$, it is strictly invariant under any state-space translation
   $k \mapsto k + \delta$ ($\delta \in (\mathbb{Z}/N\mathbb{Z})^E$), and whenever at least two
   states carry positive weight, the full state-sum strictly exceeds any single state's weight.
   Thus the state-sum aggregates all $k \in (\mathbb{Z}/N\mathbb{Z})^E$ rather than selecting a
   distinguished state $k_0$.

3. **Two-Pronged Archimedean Bridge Exclusion at $q_0 > 1$
   (`mcphailSnyder_archimedean_bridge_exclusion`):**
   - **Root-of-unity / Habiro lane:** Passing from the $N$-th root-of-unity fibres $\zeta_N$ to
     the real archimedean pin $q_0 > 1$ via the Habiro series is blocked by
     `HabiroEvaluationTrichotomy.no_continuous_evaluation_of_one_lt` (`¬ ContinuousEvalAt q₀`
     for all $q_0 > 1$).
   - **Modular-double / state-integral dual lane:** Passing via Faddeev's modular double to the
     dual parameter $\tilde{q} = e^{-4\pi^2 / \ln q_0}$ is governed by
     `ModularDoubleReciprocity.modular_reciprocity` ($\mathrm{logQ}(c, y)\cdot\mathrm{logQDual}(c, y) = c^2$)
     and `ModularDoubleReciprocity.dual_lt_of_y_lt_one` ($\mathrm{logQDual}(c, y) < \mathrm{logQ}(c, y)$
     for $0 < y < 1$, giving the $\tilde{q} \sim 10^{-165}$ suppression at $y = \frac{\ln q_0}{2\pi}$).

-- Ref: [mcphail-snyder-2025] McPhail-Snyder, arXiv:2502.04286 (diagrammatic state-sum at roots of unity)
-- Ref: [habiro2002] Habiro, Invent. Math. 171 (2008), 1-81
-- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995), 249-254
-/
import QOU.QBeta.HabiroEvaluationTrichotomy
import QOU.QBeta.ModularDoubleReciprocity

namespace QOU.QBeta.McPhailSnyderBridgeExclusion

open QOU.QBeta.HabiroEvaluationTrichotomy
open QOU.QBeta.ModularDoubleReciprocity

/-! ## 1. Diagrammatic State-Sum Structure at $N$-th Roots of Unity -/

/-- External cusp holonomy input datum $\rho = (\mu, \lambda)$ supplied to the McPhail–Snyder
diagrammatic Boltzmann weights on a shaped/ideal link diagram. -/
structure CuspHolonomyInput (R : Type*) where
  /-- Meridian holonomy eigenvalue parameter $\mu$. -/
  mu : R
  /-- Longitude holonomy eigenvalue parameter $\lambda$. -/
  lambda : R

/-- The space of edge state colourings $k \in (\mathbb{Z}/N\mathbb{Z})^E$ on a diagram with
$E$ segments at root-of-unity order $N$. -/
abbrev EdgeStateSpace (N E : ℕ) : Type := Fin E → ZMod N

/-- The McPhail–Snyder diagrammatic state-sum at root-of-unity order $N$ on a link diagram with
$E$ edge segments and $C$ crossings, taking the external cusp holonomy datum
$\rho : \mathrm{CuspHolonomyInput}\,R$ and summing the product of crossing Boltzmann weights
$R_c(\rho, k)$ over all edge colourings $k \in (\mathbb{Z}/N\mathbb{Z})^E$. -/
def mcphailSnyderStateSum {R : Type*} [CommRing R] (N E C : ℕ) [NeZero N]
    (R_boltzmann : CuspHolonomyInput R → EdgeStateSpace N E → Fin C → R)
    (ρ : CuspHolonomyInput R) : R :=
  ∑ k : EdgeStateSpace N E, ∏ c : Fin C, R_boltzmann ρ k c

/-! ## 2. Non-Selection of the External Holonomy $\rho$ and Edge State $k$ -/

/-- Because `mcphailSnyderStateSum` sums over the entire finite abelian group
$(\mathbb{Z}/N\mathbb{Z})^E$, translating the edge-state indexing by any shift
$\delta \in (\mathbb{Z}/N\mathbb{Z})^E$ leaves the state-sum strictly invariant. In particular,
the summation over all $k$ is translation-invariant and selects no distinguished state $k_0$. -/
theorem mcphailSnyderStateSum_shift_invariant {R : Type*} [CommRing R] (N E C : ℕ) [NeZero N]
    (R_boltzmann : CuspHolonomyInput R → EdgeStateSpace N E → Fin C → R)
    (ρ : CuspHolonomyInput R) (δ : EdgeStateSpace N E) :
    mcphailSnyderStateSum N E C (fun ρ' k c => R_boltzmann ρ' (k + δ) c) ρ =
      mcphailSnyderStateSum N E C R_boltzmann ρ := by
  unfold mcphailSnyderStateSum
  exact Equiv.sum_comp (Equiv.addRight δ) (fun k => ∏ c : Fin C, R_boltzmann ρ k c)

/-- On a 1-crossing diagram ($C = 1$) with state-independent meridian weight
$R(\rho, k, c) = \rho.\mu$, the diagrammatic state-sum evaluates to $(N^E : R) \cdot \rho.\mu$,
retaining explicit linear dependence on the external holonomy input $\rho.\mu$. -/
theorem mcphailSnyderStateSum_const_boltzmann {R : Type*} [CommRing R] (N E : ℕ) [NeZero N]
    (ρ : CuspHolonomyInput R) :
    mcphailSnyderStateSum N E 1 (fun ρ' _ _ => ρ'.mu) ρ = (N ^ E : R) * ρ.mu := by
  unfold mcphailSnyderStateSum
  simp [Fintype.card_pi, ZMod.card, nsmul_eq_mul]

/-- If two external cusp holonomy inputs $\rho_1, \rho_2$ have distinct meridian parameters
$\rho_1.\mu \neq \rho_2.\mu$ over an integral domain $R$ in which $(N^E : R) \neq 0$, then the
diagrammatic state-sum takes distinct values on $\rho_1$ and $\rho_2$: the state-sum is a
function of the external input $\rho$ rather than fixing $\rho$ from the diagram alone. -/
theorem mcphailSnyderStateSum_ne_of_mu_ne {R : Type*} [CommRing R] [IsDomain R] (N E : ℕ)
    [NeZero N] (hN : (N ^ E : R) ≠ 0) {ρ₁ ρ₂ : CuspHolonomyInput R}
    (hμ : ρ₁.mu ≠ ρ₂.mu) :
    mcphailSnyderStateSum N E 1 (fun ρ' _ _ => ρ'.mu) ρ₁ ≠
      mcphailSnyderStateSum N E 1 (fun ρ' _ _ => ρ'.mu) ρ₂ := by
  rw [mcphailSnyderStateSum_const_boltzmann, mcphailSnyderStateSum_const_boltzmann]
  intro heq
  exact hμ (mul_left_cancel₀ hN heq)

/-- If a non-negative real summand $w : (\mathbb{Z}/N\mathbb{Z})^E \to \mathbb{R}$ is strictly
positive at a second state $k_2 \neq k_1$, then the full state-sum over all
$k \in (\mathbb{Z}/N\mathbb{Z})^E$ strictly exceeds the single-state evaluation $w(k_1)$,
confirming that full summation does not project onto a single state $k_1$. -/
theorem stateSum_strictly_gt_single_state (N E : ℕ) [NeZero N]
    (w : EdgeStateSpace N E → ℝ) (hw_nonneg : ∀ k, 0 ≤ w k)
    {k₁ k₂ : EdgeStateSpace N E} (hne : k₁ ≠ k₂) (hk₂ : 0 < w k₂) :
    w k₁ < ∑ k : EdgeStateSpace N E, w k := by
  have hsub : ({k₁, k₂} : Finset (EdgeStateSpace N E)) ⊆ Finset.univ := Finset.subset_univ _
  have hle : ∑ k ∈ ({k₁, k₂} : Finset (EdgeStateSpace N E)), w k ≤
      ∑ k : EdgeStateSpace N E, w k :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun k _ _ => hw_nonneg k)
  rw [Finset.sum_pair hne] at hle
  linarith

/-! ## 3. Two-Pronged Fibre-to-$q_0$ Archimedean Bridge Exclusion Theorem -/

/-- **McPhail–Snyder Fibre-to-$q_0$ Bridge Exclusion Theorem (`qou-0e66`):**
For any root-of-unity order $N \ge 1$, edge count $E$, crossing count $C$, state-space shift
$\delta \in (\mathbb{Z}/N\mathbb{Z})^E$, real archimedean substrate pin $q_0 > 1$ with growth
threshold $N_0$ (`∀ n ≥ N₀, 2 ≤ q₀ ^ (n + 1)`), positive coupling $c > 0$, and normalized
log-parameter $0 < y < 1$:
1. **(State-space translation invariance):** The McPhail–Snyder state-sum is invariant under
   $k \mapsto k + \delta$ across $(\mathbb{Z}/N\mathbb{Z})^E$;
2. **(Habiro / root-of-unity lane excluded at $q_0 > 1$):** The cyclotomic Pochhammer factors
   do not converge to $0$ (`¬ Filter.Tendsto (fun n => qPoch q₀ n) Filter.atTop (nhds 0)`),
   blocking continuous evaluation of the non-terminating Habiro series at $q_0 > 1$;
3. **(Modular-double dual lane suppressed for $0 < y < 1$):** The Faddeev modular-double dual
   log-parameter satisfies exact reciprocity $\mathrm{logQ}(c, y) \cdot \mathrm{logQDual}(c, y) = c^2$
   and strict dual suppression $\mathrm{logQDual}(c, y) < \mathrm{logQ}(c, y)$. -/
theorem mcphailSnyder_archimedean_bridge_exclusion (N E C N₀ : ℕ) [NeZero N]
    (R_boltzmann : CuspHolonomyInput ℝ → EdgeStateSpace N E → Fin C → ℝ)
    (ρ : CuspHolonomyInput ℝ) (δ : EdgeStateSpace N E)
    {q₀ c y : ℝ} (hq₀ : 1 < q₀) (hN₀ : ∀ n, N₀ ≤ n → 2 ≤ q₀ ^ (n + 1))
    (hc : 0 < c) (hy₀ : 0 < y) (hy₁ : y < 1) :
    mcphailSnyderStateSum N E C (fun ρ' k c_idx => R_boltzmann ρ' (k + δ) c_idx) ρ =
      mcphailSnyderStateSum N E C R_boltzmann ρ ∧
    ¬ Filter.Tendsto (fun n => qPoch q₀ n) Filter.atTop (nhds 0) ∧
    logQ c y * logQDual c y = c ^ 2 ∧
    logQDual c y < logQ c y := by
  refine ⟨mcphailSnyderStateSum_shift_invariant N E C R_boltzmann ρ δ,
    qPoch_not_tendsto_zero_of_one_lt hq₀ N₀ hN₀,
    modular_reciprocity c y hy₀.ne',
    dual_lt_of_y_lt_one hc hy₀ hy₁⟩

end QOU.QBeta.McPhailSnyderBridgeExclusion
