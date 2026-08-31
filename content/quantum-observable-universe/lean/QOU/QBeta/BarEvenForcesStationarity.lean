/-
# Bar-evenness forces stationarity at `q = 1` — so the holonomy `t²` test is a
# bar-symmetry test

Bean `qou-pdix` (child of `qou-cds1`).

Entry (6) of that bean records a **tension with the convention-D ruling**: the
single-wrap phase under convention C matches a Kohno–Drinfeld holonomy angle
`c·ln q` through order `t²` in `q = 1 + t`, while under convention D it does
not.  This file proves the link that turns that tension into a restatement.

The chain, of which link 3 is the content here:

1. `α = (z − 1)·h/2` with `h = q − q⁻¹` has `t²` coefficient exactly
   `1/4 + z'(1)`.
2. A constant-residue holonomy angle is a multiple of `ln q` (Kohno–Drinfeld
   fixes the scale: `ħ = 2 ln q`), and with `c` pinned at `t¹` its `t²`
   coefficient is `1/4`.  So `α` is second-order logarithmic **iff `z'(1) = 0`**.
3. **`z` bar-even ⟹ `z'(1) = 0`.**  ← proved below, for an arbitrary function.
4. `z_C = √q/(q+1)` is bar-even; `z_D = q³/(q²+1)` is not, with `z_D'(1) = 1`.

**Consequence (the reason this file exists).** Convention C passes the `t²`
holonomy test *because it is bar-invariant*, and D fails it *because it is not*.
That is not independent evidence against the 2026-08-15 ruling — it is the
already-known non-bar-evenness of `z_D` in holonomy language.  `DFrameBarAction`
in this same namespace proves the stronger form (the whole bar *action* changes
shape: affine reflection under C, multiplicative under D).

**Corollary for route 5.**  The branch-3 acceptance test's first part
("reproduce `α` through `t²`") has **no discriminating power**: any construction
over a bar-even `z` passes it automatically and any over `z_D` fails it
automatically, whatever the construction is.  It tests the Markov parameter, not
the holonomy hypothesis.

Note the theorem below needs no hypothesis about *which* function `z` is — only
that `q = 1` is the fixed point of `q ↦ q⁻¹`.  That is what makes the corollary
about acceptance-test part 1 airtight rather than a property of two examples.

Companion probe: `computations/qbeta/qbeta_holonomy_t2_is_a_bar_symmetry_test_probe.py`
(11/11, exact ℚ(q) and ℚ(√q)).
-/
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Tactic

namespace QOU.QBeta.BarEven

open Filter Topology

/-- **Bar-evenness forces stationarity at the bar fixed point.**

If `f` agrees with `x ↦ f x⁻¹` near `1` and is differentiable at `1`, then
`deriv f 1 = 0`.

The proof is the one-line differentiation of `f (q⁻¹) = f q` at `q = 1`: the
chain rule contributes the factor `d/dq (q⁻¹) = −1` there, giving
`−f'(1) = f'(1)`.  Nothing about `f` beyond differentiability is used — the
statement is about the involution, not the function. -/
theorem deriv_at_one_eq_zero_of_barEven {f : ℝ → ℝ}
    (hf : DifferentiableAt ℝ f 1)
    (hsym : (fun x : ℝ => f x⁻¹) =ᶠ[𝓝 (1 : ℝ)] f) :
    deriv f 1 = 0 := by
  -- the inverse map has derivative `-1` at `1`
  have hinv : HasDerivAt (fun x : ℝ => x⁻¹) (-1 : ℝ) 1 := by
    simpa using hasDerivAt_inv (one_ne_zero (α := ℝ))
  -- so `x ↦ f x⁻¹` has derivative `-(deriv f 1)` at `1`
  have hcomp : HasDerivAt (fun x : ℝ => f x⁻¹) (deriv f 1 * (-1)) 1 := by
    have hf1 : HasDerivAt f (deriv f 1) ((1 : ℝ)⁻¹) := by
      rw [inv_one]; exact hf.hasDerivAt
    exact hf1.comp (1 : ℝ) hinv
  -- but that function equals `f` near `1`, so it also has derivative `deriv f 1`
  have hf' : HasDerivAt f (deriv f 1) 1 := hf.hasDerivAt
  have hcomp' : HasDerivAt (fun x : ℝ => f x⁻¹) (deriv f 1) 1 :=
    hf'.congr_of_eventuallyEq hsym
  -- uniqueness of the derivative
  have : deriv f 1 * (-1) = deriv f 1 := hcomp.unique hcomp'
  linarith [this]

/-- The Markov parameter of **convention C**, in the square-root variable
`u = √q`: `z_C = u/(u²+1)`.  Written this way it is manifestly invariant under
`u ↦ u⁻¹`, which is the bar involution. -/
noncomputable def zC (u : ℝ) : ℝ := u / (u ^ 2 + 1)

/-- The Markov parameter of **convention D**: `z_D = q³/(q²+1)`. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- **`z_C` is bar-even**, as an identity for every nonzero `u`. -/
theorem zC_barEven {u : ℝ} (hu : u ≠ 0) : zC u⁻¹ = zC u := by
  have h1 : u ^ 2 + 1 ≠ 0 := by positivity
  have h2 : (u⁻¹) ^ 2 + 1 ≠ 0 := by positivity
  unfold zC
  field_simp
  ring

/-- **`z_D` is NOT bar-even**: at `q = 2` it takes the value `8/5` while
`z_D(1/2) = (1/8)/(5/4) = 1/10`. -/
theorem zD_not_barEven : zD (2 : ℝ)⁻¹ ≠ zD 2 := by
  unfold zD; norm_num

/-- `z_D'(1) = 1 ≠ 0`, so nothing forces the `t²` match for convention D.
Stated as the explicit difference quotient limit's value via `deriv`. -/
theorem deriv_zD_at_one : deriv zD 1 = 1 := by
  have hd : HasDerivAt (fun q : ℝ => q ^ 3) 3 1 := by
    simpa using (hasDerivAt_pow 3 (1 : ℝ))
  have he : HasDerivAt (fun q : ℝ => q ^ 2 + 1) 2 1 := by
    simpa using (hasDerivAt_pow 2 (1 : ℝ)).add_const 1
  have hne : ((1 : ℝ) ^ 2 + 1) ≠ 0 := by norm_num
  have hdiv := hd.div he hne
  have h : HasDerivAt zD 1 1 := by
    unfold zD
    convert hdiv using 1
    norm_num
  exact h.deriv

/-- **The contrast, stated together.**  `z_C` is bar-even hence stationary at the
bar fixed point; `z_D` is not bar-even and is not stationary.  Since `α`'s `t²`
coefficient is `1/4 + z'(1)` and the `c·ln q` prediction is `1/4`, this is
exactly why C passes the holonomy `t²` test and D fails it — and therefore why
that failure is not independent evidence against convention D. -/
theorem zD_deriv_ne_zero : deriv zD 1 ≠ 0 := by
  rw [deriv_zD_at_one]; norm_num

end QOU.QBeta.BarEven
