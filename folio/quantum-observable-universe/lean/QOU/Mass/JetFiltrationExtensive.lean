import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Tactic.Linarith

/-!
# QOU.Mass.JetFiltrationExtensive — the extensive property of the jet-filtration binding

Formalises the **provable core** of the body-order (jet-filtration) binding
(`conj:binding-manybody-eq-jet-filtration`), the compute consumer implemented in
`computations/binding_manybody_jet_filtration.py`:

  `B(K) = Σ_{n=2}^{A} m_e · a_D^(n) · w_n(K)`,

where `a_D^(n) = ∮_{S_c} λ_SW^(n)` is the non-abelian-Stokes SW prolongation period
(`QOU.Mass.NaStokesKeystone`), equal to the super-exponential mean quantum dimension
`lw(n−1)` (#1765), and `w_n(K)` is the (open) per-atom residue weight.

**What is proved here (sorry-free, generic):** the binding is **extensive** — a finite
sum of non-negative body-order contributions, hence *monotone non-decreasing in the
body-order cutoff `A`*, and *strictly increasing* when a new body-order has positive
contribution. This is precisely the property the **intensive** rotation-phase
`θ_λ = arccos(χ^λ/d_λ)` route structurally lacked (`probe_full_theta_binding.py`: the
bounded phase cannot grow with `A`).

**What is NOT proved here (honest scope):** the super-exponential *magnitude* of
`a_D^(n)` (the √-branch falling-factorial growth), the na-Stokes identity
`a_D^(n) = lw(n−1)` (the owner-gated keystone conj #1765), and the residue weight
`w_n(K)` (the open q-difference "ρ·A" kernel) are conjectural inputs, carried here as
abstract non-negativity/positivity hypotheses on `aD`, `w` — not derived.
-/

namespace QOU.Mass

open Finset

/-- The body-order (jet-filtration) binding
    `B(A) = Σ_{n=2}^{A} m_e · a_D(n) · w(n)`. -/
noncomputable def jetBinding (me : ℝ) (aD w : ℕ → ℝ) (A : ℕ) : ℝ :=
  ∑ n ∈ Finset.Icc 2 A, me * aD n * w n

/-- Each body-order term is non-negative when the electron scale, the SW period, and
    the residue weight are non-negative. -/
theorem jetBinding_term_nonneg {me : ℝ} {aD w : ℕ → ℝ}
    (hme : 0 ≤ me) (haD : ∀ n, 0 ≤ aD n) (hw : ∀ n, 0 ≤ w n) (n : ℕ) :
    0 ≤ me * aD n * w n :=
  mul_nonneg (mul_nonneg hme (haD n)) (hw n)

/-- **Extensive (monotone).** The jet-filtration binding is monotone non-decreasing in
    the body-order cutoff `A`: adding nucleon body-orders can only increase binding.
    (The intensive rotation-phase `θ_λ` route lacked this.) -/
theorem jetBinding_mono {me : ℝ} {aD w : ℕ → ℝ}
    (hme : 0 ≤ me) (haD : ∀ n, 0 ≤ aD n) (hw : ∀ n, 0 ≤ w n)
    {A A' : ℕ} (hAA' : A ≤ A') :
    jetBinding me aD w A ≤ jetBinding me aD w A' := by
  unfold jetBinding
  refine Finset.sum_le_sum_of_subset_of_nonneg
    (Finset.Icc_subset_Icc (le_refl 2) hAA') ?_
  intro n _ _
  exact jetBinding_term_nonneg hme haD hw n

/-- **Strictly extensive.** A body-order with strictly positive contribution strictly
    increases the binding. Combined with the (conjectural) super-exponential growth of
    `a_D^(n) = lw(n−1)`, this is the mechanism by which the na-Stokes period supplies the
    extensive `A`-growth of nuclear binding. -/
theorem jetBinding_lt_succ {me : ℝ} {aD w : ℕ → ℝ}
    {A : ℕ} (hA : 2 ≤ A + 1)
    (hpos : 0 < me * aD (A + 1) * w (A + 1)) :
    jetBinding me aD w A < jetBinding me aD w (A + 1) := by
  unfold jetBinding
  rw [Finset.sum_Icc_succ_top hA]
  linarith

/-- **Reflexive specialization of `jetBinding_mono` (`qou-172h`).**
For non-negative `me`, `aD`, and `w`, `jetBinding me aD w A ≤ jetBinding me aD w A`. -/
theorem jetBinding_self_le {me : ℝ} {aD w : ℕ → ℝ}
    (hme : 0 ≤ me) (haD : ∀ n, 0 ≤ aD n) (hw : ∀ n, 0 ≤ w n) (A : ℕ) :
    jetBinding me aD w A ≤ jetBinding me aD w A :=
  jetBinding_mono hme haD hw (le_refl A)

end QOU.Mass
