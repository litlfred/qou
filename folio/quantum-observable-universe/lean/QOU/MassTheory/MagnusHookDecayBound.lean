import QOU.MassTheory.MagnusHookExteriorPower
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic

/-!
# The sharp bound on the hook column of the gauge-invariant curvature (qou-o6ov)

**Context (#6464, #6480, and `magnus_gauge_hook_decay_bound_probe.py`).** On a hook
`(k,1ⁿ⁻ᵏ) = Λʲ(V)`, `j = n − k`, the projector curvature `Ω₂^P` has the reduced-Burau closed form
```
tr_hook(ρ·Ω₂^P) = c · Σ_a [ e_j(μ⁺_a) − e_j(μ⁻_a) ],    c = (4/[2]_q²)·q^{(L+2)(1−j)},
```
with `μ^±_a` the Burau spectra of the commutator-member words `ρσ_aσ_{a+1}`, `ρσ_{a+1}σ_a`
(`MagnusGaugeCurvatureHookColumn.trace_mul_curvature_eq_of_word_traces`). For hooks
`b(λ) = n − λ₁ = j`, so a bound in `j` **is** the hook-column decay statement.

The probe measured two bounds. The crude spectral-radius bound `|e_j| ≤ C(n−1,j)·rʲ` is a binomial
hump (it decays only past `j ≈ (n−1)·d/(1+d)`, `d = q^{−(L+2)}·r ≈ q^{−2}·(r/q^L)` — the twist
exactly cancels the dominant Burau eigenvalue `≈ q^L`, so the crude bound throws away the whole
subdominant spectrum). The **sharp** bound keeps it:
```
|tr_hook(ρ·Ω₂^P)| ≤ |c| · Σ_a [ e_j(|μ⁺_a|) + e_j(|μ⁻_a|) ]  =: B'_j,
```
and **`B'_j / C(n−1,j)` is strictly decreasing in `j` at A = 2 and A = 3** (exact mpf), while the
crude bound is not. This file formalizes the *only* inequality the sharp bound uses.

**What is formalized.** Three sorry-free lemmas over a generic linearly ordered commutative ring
(the ordering is what `|·|` needs — this is the §7c archimedean-side specialisation, kept in its
own file so `MagnusHookExteriorPower` stays a bare `CommRing` statement):

* `abs_esymm_le_esymm_abs` — the triangle inequality for the elementary symmetric sum:
  `|e_j(μ)| ≤ e_j(|μ|)`.
* `abs_sum_esymm_sub_le` — applied across the commutator sum:
  `|Σ_a (e_j(μ⁺_a) − e_j(μ⁻_a))| ≤ Σ_a (e_j(|μ⁺_a|) + e_j(|μ⁻_a|))`.
* `abs_mul_sum_esymm_sub_le` — with the twist scalar `c`: `|c·Σ_a(…)| ≤ |c|·Σ_a(…)`, which is
  exactly `B'_j`.

**What is not.** The monotonicity of `B'_j / C(n−1,j)` in `j` is a property of the *measured*
Burau moduli (they fall off geometrically, ratio ≈ 0.71–0.77 per step at A = 2, 3), not a theorem
for arbitrary spectra; the seminormal construction, the atom word and the twist are outside
Mathlib, as in the sibling files. The lemmas here turn "the hook column decays" into a statement
about one list of moduli per commutator member — which the probe then checks.
-/

namespace QOU.MassTheory

open Finset BigOperators

variable {ι : Type*} [Fintype ι]
  {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Triangle inequality for the elementary symmetric sum.** `|e_j(μ)| ≤ e_j(|μ|)`: the
`j`-th elementary symmetric function of a spectrum is bounded by the same function of its
moduli. This is the single inequality behind the sharp hook-column bound. -/
theorem abs_esymm_le_esymm_abs (j : ℕ) (μ : ι → R) :
    |esymm j μ| ≤ esymm j (fun i => |μ i|) := by
  unfold esymm
  refine (Finset.abs_sum_le_sum_abs _ _).trans (le_of_eq ?_)
  refine Finset.sum_congr rfl ?_
  intro S _
  exact Finset.abs_prod S μ

/-- **Across the commutator sum.** Each member of `Σ_a (e_j(μ⁺_a) − e_j(μ⁻_a))` is bounded by
the sum of the two moduli-symmetric values, so the whole signed sum is bounded by
`Σ_a (e_j(|μ⁺_a|) + e_j(|μ⁻_a|))`. -/
theorem abs_sum_esymm_sub_le (j m : ℕ) (μp μm : ℕ → ι → R) :
    |∑ a ∈ range m, (esymm j (μp a) - esymm j (μm a))|
      ≤ ∑ a ∈ range m, (esymm j (fun i => |μp a i|) + esymm j (fun i => |μm a i|)) := by
  refine (Finset.abs_sum_le_sum_abs _ _).trans ?_
  refine Finset.sum_le_sum ?_
  intro a _
  refine (abs_sub _ _).trans ?_
  exact add_le_add (abs_esymm_le_esymm_abs j (μp a)) (abs_esymm_le_esymm_abs j (μm a))

/-- **The sharp bound `B'_j`.** With the twist scalar `c = (4/[2]_q²)·q^{(L+2)(1−j)}` in front,
`|c · Σ_a (e_j(μ⁺_a) − e_j(μ⁻_a))| ≤ |c| · Σ_a (e_j(|μ⁺_a|) + e_j(|μ⁻_a|))`. Composed with
`trace_mul_curvature_eq_of_word_traces`, the left side is `|tr_hook(ρ·Ω₂^P)|` and the right side
is the bound the probe finds strictly decreasing per dimension. -/
theorem abs_mul_sum_esymm_sub_le (c : R) (j m : ℕ) (μp μm : ℕ → ι → R) :
    |c * ∑ a ∈ range m, (esymm j (μp a) - esymm j (μm a))|
      ≤ |c| * ∑ a ∈ range m, (esymm j (fun i => |μp a i|) + esymm j (fun i => |μm a i|)) := by
  rw [abs_mul]
  exact mul_le_mul_of_nonneg_left (abs_sum_esymm_sub_le j m μp μm) (abs_nonneg c)

end QOU.MassTheory
