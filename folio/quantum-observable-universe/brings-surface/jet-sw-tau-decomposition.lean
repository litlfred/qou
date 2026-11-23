import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Data.Complex.Basic

/-!
# `QOU.Brings.jet_sw_tau_decomposition` — SW = jet decomposition of `τ`

Formalises `prop:jet-sw-tau-decomposition` (Lemma **L2** of the step-9 binding-closure
chain): the Archimedean realisation `τ` applied to the surface-ordered MI integral
over the exceptional divisor `S_c` decomposes across vertical jet degrees `n` into the
sum of prolonged Seiberg–Witten periods `a_D^{(n)} = ∮ λ_SW^{(n)}`:

  `τ(MI∫_{S_c}) = ∑_n a_D^{(n)} = ∑_n (2πi · ∑_{p ∈ E} Res_p λ_SW^{(n)})`.

## Mathematical structure

1. **Abstract graded-sum composition (`JetSWArchDecomposition`)**:
   Combines exhaustiveness/additivity on the associated graded with levelwise
   abelianisation `τ(graded_n) = a_D^{(n)}` (`jet_sw_tau_decomposition`).
2. **Concrete `ℂ`-linear jet prolongation tower (`ProlongedJetTower`)**:
   Models the vertical jet space as a `ℂ`-module `V`, `τ : V →ₗ[ℂ] ℂ` as a genuine
   `ℂ`-linear map, and `miIntegral = ∑_{n < N} jetPiece n` in `V`. Additivity of `τ`
   is *proved* from `map_sum` (`ProlongedJetTower.toDecomposition`), and composed
   with enclosed-pole residue evaluation + Fubini sum interchange
   (`jet_sw_tau_linear_residue_expansion`).
3. **Baseline electron (`n = 0`) + higher-jet separation (`jet_sw_electron_plus_higher_jets`)**:
   Splits `τ(MI∫_{S_c}) = a_D^{(0)} + ∑_{k = 0}^{m-1} a_D^{(k+1)}`.

## References

- [leitner2026] §5-brings-surface/jet-sw-tau-decomposition (`prop:jet-sw-tau-decomposition`)
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4
-/

namespace QOU.Brings

open scoped BigOperators

/-- **Jet / `τ` decomposition data** packaging finite vertical truncation order
    `maxOrder`, prolonged SW periods `period`, graded `τ`-pieces `tauGraded`, and
    the two structural hypotheses (`tau_additive`, `graded_eq_period`). -/
structure JetSWArchDecomposition where
  /-- Highest vertical (jet) degree retained (`0 ≤ n < maxOrder`). -/
  maxOrder : ℕ
  /-- The `n`-th prolonged SW period `a_D^{(n)} = ∮ λ_SW^{(n)}`. -/
  period : ℕ → ℂ
  /-- The `τ`-image `τ(graded_n)` of the `n`-th vertical jet graded piece. -/
  tauGraded : ℕ → ℂ
  /-- The Archimedean value `τ(MI∫_{S_c})`. -/
  tauValue : ℂ
  /-- Additivity / exhaustiveness of `τ` across the associated graded jet tower. -/
  tau_additive : tauValue = ∑ n ∈ Finset.range maxOrder, tauGraded n
  /-- Levelwise MI-to-SW abelianisation (`prop:mi-sw-abelianisation`). -/
  graded_eq_period : ∀ n, tauGraded n = period n

/-- **L2 (`prop:jet-sw-tau-decomposition`).** The `τ`-image of the MI integral equals
    the finite sum over vertical jet degrees of the prolonged Seiberg–Witten periods. -/
-- Ref: [leitner2026] §5-brings-surface
theorem jet_sw_tau_decomposition (D : JetSWArchDecomposition) :
    D.tauValue = ∑ n ∈ Finset.range D.maxOrder, D.period n := by
  rw [D.tau_additive]
  exact Finset.sum_congr rfl (fun n _ => D.graded_eq_period n)

/-- Separation of the classical `n = 0` electron baseline `a_D^{(0)}` from the higher
    prolonged jet corrections `n = 1, …, m` (`maxOrder = m + 1`). -/
theorem jet_sw_electron_plus_higher_jets (D : JetSWArchDecomposition)
    {m : ℕ} (hm : D.maxOrder = m + 1) :
    D.tauValue = D.period 0 + ∑ k ∈ Finset.range m, D.period (k + 1) := by
  rw [jet_sw_tau_decomposition D, hm, Finset.sum_range_succ']
  exact add_comm _ _

/-- **Concrete `ℂ`-linear jet prolongation tower** over a `ℂ`-module `V` of surface-ordered
    jet operators, equipped with a linear Archimedean realisation `tau : V →ₗ[ℂ] ℂ` and
    enclosed branch-point residue evaluation at `k` poles. -/
structure ProlongedJetTower (V : Type*) [AddCommMonoid V] [Module ℂ V] (k : ℕ) where
  /-- Number of vertical jet levels retained. -/
  maxOrder : ℕ
  /-- `ℂ`-linear Archimedean realisation functor `τ : V →ₗ[ℂ] ℂ`. -/
  tau : V →ₗ[ℂ] ℂ
  /-- `n`-th vertical graded piece of the MI integral in `V`. -/
  jetPiece : ℕ → V
  /-- Total truncated MI integral in `V`. -/
  miIntegral : V
  /-- Jet-graded expansion in `V` before applying `τ`. -/
  mi_eq_jet_sum : miIntegral = ∑ n ∈ Finset.range maxOrder, jetPiece n
  /-- Subset of poles enclosed by the Seiberg–Witten period cycle. -/
  enclosed : Finset (Fin k)
  /-- `2πi` residue normalisation factor. -/
  twoPiI : ℂ
  /-- Branch-point residue `Res_p λ_SW^{(n)}` at jet level `n` and pole `p`. -/
  res : ℕ → Fin k → ℂ
  /-- Levelwise abelianisation + contour residue evaluation. -/
  tau_piece_eq_residue :
    ∀ n, tau (jetPiece n) = twoPiI * ∑ p ∈ enclosed, res n p

/-- Derive a `JetSWArchDecomposition` from a `ProlongedJetTower`, proving `tau_additive`
    directly from `ℂ`-linearity (`map_sum`) of `τ`. -/
def ProlongedJetTower.toDecomposition {V : Type*} [AddCommMonoid V] [Module ℂ V] {k : ℕ}
    (T : ProlongedJetTower V k) : JetSWArchDecomposition where
  maxOrder := T.maxOrder
  period n := T.twoPiI * ∑ p ∈ T.enclosed, T.res n p
  tauGraded n := T.tau (T.jetPiece n)
  tauValue := T.tau T.miIntegral
  tau_additive := by
    rw [T.mi_eq_jet_sum, map_sum]
  graded_eq_period := T.tau_piece_eq_residue

/-- **Linear jet-prolongation & enclosed-residue interchange theorem**:
    for any `ProlongedJetTower`, `τ(MI∫)` equals both the jet-level sum of enclosed
    residue periods and `2πi` times the per-pole sum of summed vertical jet residues. -/
-- Ref: [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4
theorem jet_sw_tau_linear_residue_expansion {V : Type*} [AddCommMonoid V] [Module ℂ V]
    {k : ℕ} (T : ProlongedJetTower V k) :
    T.tau T.miIntegral =
      (∑ n ∈ Finset.range T.maxOrder, (T.twoPiI * ∑ p ∈ T.enclosed, T.res n p)) ∧
    T.tau T.miIntegral =
      T.twoPiI * ∑ p ∈ T.enclosed, ∑ n ∈ Finset.range T.maxOrder, T.res n p := by
  have h1 : T.tau T.miIntegral =
      ∑ n ∈ Finset.range T.maxOrder, (T.twoPiI * ∑ p ∈ T.enclosed, T.res n p) :=
    jet_sw_tau_decomposition T.toDecomposition
  refine ⟨h1, ?_⟩
  rw [h1, ← Finset.mul_sum, Finset.sum_comm]

end QOU.Brings
