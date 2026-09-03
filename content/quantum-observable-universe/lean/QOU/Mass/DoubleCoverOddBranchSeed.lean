/-
# The ramified double cover does not supply `w_3` — a dichotomy, by depth

`QOU.Mass.BindingScalarKernelParityExclusion.no_scalar_kernel_on_carrier`
(sorry-free) shows no scalar kernel acts on the q-Borel-normalised carrier: it is
pure isoclinic of Newton slope `1/2`, every rank-1 q-difference module has
integer slope, and `2u - 2p = 1` is unsolvable over `ℤ`. Its scope note names the
structure that is missing rather than absent:

> "The exclusion is over `K(x)`: after a degree-2 **ramified** base change
>  (adjoining `q^(1/2), x^(1/2)`) the slope becomes the integer `1` and a scalar
>  kernel **does** exist on the double cover, relating half-shifts — i.e. even
>  and odd body orders separately."

`2026-08-29-w3-closeability.md` measured four routes to a second base case, found
none, and recorded this one as **"untried, and the one route nothing measured
here excludes"** (bean `qou-v8qx`). Its question, verbatim: *"whether the odd
branch's seed is fixed by something already derived — `n=2` seeds the even
branch; what seeds the odd branch?"*

## The answer: nothing does, and the reason splits by the kernel's depth

Index the odd branch directly, `v k := w (2k+1)`, so `v 0 = w_1` (one-body) and
`v 1 = w_3` — the unknown. The **one-body seed is forced to vanish**: `w_1` is
the connected one-body cumulant, i.e. the binding of a single free nucleon,
which is zero by definition. (This is also why the Ursell inversion in
`he4_body_order_shortfall_location_probe` starts at `b₂` — not an omission.)

* **Depth 1** — `v (k+1) = r * v k`. The forced seed propagates:
  `oddBranch_eq_zero_of_depthOne` gives `v k = 0` for every `k`, so `w_3 = 0`,
  so `b₃ = 0`. Against the measured `b₃ = +1.426222` MeV that horn is
  **refuted**, and refuted structurally rather than numerically — the vanishing
  is forced by `w_1 = 0` alone, for every `r`.

* **Depth 2** — `v (k+2) = p * v (k+1) + s * v k`. The relation now needs *two*
  seeds and the corpus supplies one. `seed_not_determined_of_depthTwo` exhibits,
  **for every kernel `(p, s)`**, two solutions agreeing at `v 0 = 0` and taking
  any two prescribed values at `v 1`. So `w_3` is a free parameter of the route,
  which is to say the route **renames** it.

Neither horn closes `w_3`. The bean's own disposition applies to the second:
*"if it is another free constant, the route renames `w_3` and should be recorded
as such."* This file is that record.

**Scope.** The depth-1 horn is a genuine structural exclusion of *that depth*,
with the invariant cited (vanishing one-body binding). The depth-2 horn is not a
refutation at all — it is the observation that a rank-2 problem still needs two
boundary conditions after the base change, which is what
`no_scalar_kernel_on_carrier` said before it. Nothing here excludes the ramified
base change itself, its slope computation, or the existence of the kernel on the
cover; what is excluded is the hope that the parity split *supplies* the missing
seed. Depths `≥ 3` are not treated: they need three or more seeds and are
strictly worse by the same counting.

Base ring generic `CommRing` (AGENTS.md §7c) — the content is recursion
bookkeeping, with no ordering and no archimedean input.

Beans `qou-90b1` (this unit), `qou-v8qx` (the question), `qou-1xne` (the four
measured routes).
-/
import Mathlib.Algebra.Ring.Defs

namespace QOU.Mass.DoubleCoverOddBranchSeed

variable {R : Type*} [CommRing R]

/-- The odd body-order branch of the weights, reindexed: `v k = w (2k+1)`. A
**depth-1** scalar kernel on the double cover relates consecutive half-shifts. -/
def DepthOne (r : R) (v : ℕ → R) : Prop := ∀ k, v (k + 1) = r * v k

/-- A **depth-2** scalar kernel on the double cover. -/
def DepthTwo (p s : R) (v : ℕ → R) : Prop := ∀ k, v (k + 2) = p * v (k + 1) + s * v k

/-- **Depth-1 horn.** The one-body weight is the binding of a single free
nucleon, hence zero; a depth-1 kernel propagates that to the whole odd branch. -/
theorem oddBranch_eq_zero_of_depthOne {r : R} {v : ℕ → R} (h : DepthOne r v)
    (h0 : v 0 = 0) : ∀ k, v k = 0 := by
  intro k
  induction k with
  | zero => exact h0
  | succ n ih => rw [h n, ih, mul_zero]

/-- The consequence for the unknown: `w_3 = v 1 = 0`, for every kernel `r`. So a
depth-1 kernel on the cover predicts a vanishing connected three-body cumulant,
which the AME2020 inversion (`b₃ = +1.426222` MeV) contradicts. -/
theorem w3_eq_zero_of_depthOne {r : R} {v : ℕ → R} (h : DepthOne r v)
    (h0 : v 0 = 0) : v 1 = 0 :=
  oddBranch_eq_zero_of_depthOne h h0 1

/-- Contrapositive, in the form the measurement meets it: a nonzero `w_3` rules
out every depth-1 kernel on the odd branch at once. -/
theorem not_depthOne_of_w3_ne_zero {r : R} {v : ℕ → R} (h0 : v 0 = 0)
    (h3 : v 1 ≠ 0) : ¬ DepthOne r v :=
  fun h => h3 (w3_eq_zero_of_depthOne h h0)

/-- The solution of a depth-2 relation from its two seeds. Used to witness that
the second seed is genuinely free. -/
def twoStep (p s v0 v1 : R) : ℕ → R
  | 0 => v0
  | 1 => v1
  | (k + 2) => p * twoStep p s v0 v1 (k + 1) + s * twoStep p s v0 v1 k

theorem twoStep_isDepthTwo (p s v0 v1 : R) : DepthTwo p s (twoStep p s v0 v1) :=
  fun _ => rfl

/-- **Depth-2 horn.** For *every* kernel `(p, s)`, and any two prescribed values,
there are two solutions of the depth-2 relation agreeing on the forced one-body
seed and disagreeing at `w_3`. The relation therefore does not determine `w_3`:
the double cover reparametrises the unknown rather than removing it, exactly as
`kernel_coeff_existsUnique` records for the uncovered case. -/
theorem seed_not_determined_of_depthTwo (p s u u' : R) :
    ∃ v v' : ℕ → R,
      DepthTwo p s v ∧ DepthTwo p s v' ∧ v 0 = v' 0 ∧ v 1 = u ∧ v' 1 = u' :=
  ⟨twoStep p s 0 u, twoStep p s 0 u',
    twoStep_isDepthTwo _ _ _ _, twoStep_isDepthTwo _ _ _ _, rfl, rfl, rfl⟩

end QOU.Mass.DoubleCoverOddBranchSeed
