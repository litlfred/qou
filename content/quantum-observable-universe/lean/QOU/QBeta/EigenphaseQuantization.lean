/-
# The braid-image eigenphase is QUANTIZED, and a bounded rung cannot raise a base

Bean `qou-pdix` (the S1 blocker).  Two independent results, both elementary,
both closing a gap that the corpus currently leaves open by an argument that
stops one step short.

## 1. The constant-phase hole in the braid-image exclusion

`computations/qbeta/qbeta_braid_image_eigenphase_exclusion_probe.py` closes
branch (1) of the `EigenphaseCarrierVacuity` trichotomy like this: `tr ρ(w)` is
a Laurent polynomial, `|2 cos α| ≤ 2`, a Laurent polynomial bounded on `(0,∞)`
is constant, so `cos α` is constant — and `α_C`, `α_D` are both *non-constant*,
contradiction.

**That refutes a `q`-varying ansatz and leaves a constant `α` untouched.**
Nothing requires the ladder's phase to vary: `Q_N1 = Q_A · cos(α − u/2)` is
already `q`-dependent through `u`.  Someone proposing `α = α_req`, a pure
number, is excluded by nothing.

The repair is to carry the same boundedness argument one step further, through
**integrality**.  Word matrices lie over `ℤ[q,q⁻¹]` — because the Hecke relation
gives `σ⁻¹ = σ − (q − q⁻¹)·1` — so a *bounded* character is not merely constant
but a constant **integer**.  On the two-dimensional `V_(2,1)` that forces
`2 cos α ∈ ℤ ∩ [−2,2]`, hence

    cos α ∈ {−1, −1/2, 0, 1/2, 1}.

`two_cos_eq_int_cases` is that step.  `not_isInt_of_mem_Ioo_one_two` is the
exclusion it powers: the required phase has `2 cos α_req = 1.99725…`, which lies
**strictly between 1 and 2** and is therefore not an integer — so `α_req` is not
a `q`-uniform braid-image eigenphase, for any word, in any convention.

The exhaustive arithmetic check (all 5460 words `|w| ≤ 6`, exact `ℤ[q,q⁻¹]`) is
`computations/qbeta/qbeta_eigenphase_rationality_quantization_probe.py`, 14/14.

**Not formalised here, and named so it is not mistaken for done:** the step
"a Laurent polynomial bounded on `(0,∞)` is constant", and the general-`d`
Kronecker step (all power traces constant integers ⟹ integral characteristic
polynomial ⟹ eigenvalues are roots of unity ⟹ `α ∈ 2πℚ`).  Both are proved on
paper and verified numerically; neither has a Lean twin yet.

## 2. A bounded rung cannot lift a base that is already short

This is the sharper one for the arc, because it re-scopes the dependency chain
the S1 tranche is organised around.

`qou-iagg` (the dashboard re-score) waits on `qou-cds1` (the `c_k` ladder on the
ruled `z_D` base), which waits on this bean (derive `α`).  **The second link does
not hold.**  On the ruled base the ladder must supply a factor

    Q_codata / Q_D = 0.78233341 / 0.4447004 = 1.7592370…  > 1,

while its `N = 1` rung is `cos(α − u/2) ≤ 1` for *every* `α` and its `N = 2` rung
is `(1 + c₂u²) = 0.99992745… < 1` at `c₂ = −1`.  The first two rungs together are
bounded by `0.99992745 < 1 < 1.7592`.

So **deriving `α` cannot unblock `qou-cds1`**: no phase whatsoever repairs a base
that is 43 % low, because a cosine cannot exceed one.  `cos_rung_lt_of_base_short`
is that statement.  It is the mirror of this bean's own 2026-08-22 entry, which
excluded a `cosh` re-reading because `cosh ≥ 1` was on the wrong side of a
required value below 1; here the required value is above 1 and `cos ≤ 1` is on
the wrong side of it.

Scope (b) — a structural exclusion citing a proved invariant (`Real.cos_le_one`),
not a numerical miss.  What it does *not* say: that the ladder is wrong, or that
no `Q_β` closure exists.  It says the gap lives in the **base**, not in any rung,
so the `Q_β` L2 residual is not a phase problem and must not be worked as one.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

namespace QOU.QBeta.EigenphaseQuantization

open Real

/-- **A bounded multiplicative rung cannot lift a base that already falls short.**

If the base `Qbase`, already damped by the positive `N = 2` factor `d`, sits
below the target, then no choice of phase `α` rescues it: the `N = 1` rung is a
cosine, and `cos α ≤ 1`.

Instantiated on the ruled `z_D` base this is the statement that deriving the
eigenphase cannot close the `Q_β` gap — the gap is in the base. -/
theorem cos_rung_lt_of_base_short
    {Qbase d Qtarget α : ℝ}
    (hQ : 0 < Qbase) (hd : 0 < d) (hshort : Qbase * d < Qtarget) :
    Qbase * Real.cos α * d < Qtarget := by
  have hpos : 0 < Qbase * d := mul_pos hQ hd
  calc Qbase * Real.cos α * d
      = (Qbase * d) * Real.cos α := by ring
    _ ≤ (Qbase * d) * 1 :=
        mul_le_mul_of_nonneg_left (Real.cos_le_one α) hpos.le
    _ = Qbase * d := by ring
    _ < Qtarget := hshort

/-- The same statement with the damping factor written as `1 - u^2`, the shape
the committed ladder actually uses at `c₂ = -1`. -/
theorem cos_rung_lt_of_base_short_ladder
    {Qbase Qtarget u α : ℝ}
    (hQ : 0 < Qbase) (hu : u ^ 2 < 1)
    (hshort : Qbase * (1 - u ^ 2) < Qtarget) :
    Qbase * Real.cos α * (1 - u ^ 2) < Qtarget :=
  cos_rung_lt_of_base_short hQ (by linarith) hshort

/-- **Quantization of a `q`-uniform braid-image eigenphase on `V_(2,1)`.**

A character of the braid image lies in `ℤ[q,q⁻¹]`; if it is additionally bounded
on `(0,∞)` it is a constant integer, and on the two-dimensional irrep the bound
is `2`.  So `2 cos α` is an integer in `[-2,2]`, leaving five possible cosines. -/
theorem two_cos_eq_int_cases {α : ℝ} {c : ℤ}
    (h : 2 * Real.cos α = (c : ℝ)) :
    Real.cos α = -1 ∨ Real.cos α = -1/2 ∨ Real.cos α = 0
      ∨ Real.cos α = 1/2 ∨ Real.cos α = 1 := by
  have hlo : (-2 : ℝ) ≤ (c : ℝ) := by
    have := Real.neg_one_le_cos α; linarith
  have hhi : ((c : ℝ)) ≤ 2 := by
    have := Real.cos_le_one α; linarith
  have hlo' : (-2 : ℤ) ≤ c := by exact_mod_cast hlo
  have hhi' : c ≤ 2 := by exact_mod_cast hhi
  interval_cases c <;> push_cast at h <;>
    first
      | (left; linarith)
      | (right; left; linarith)
      | (right; right; left; linarith)
      | (right; right; right; left; linarith)
      | (right; right; right; right; linarith)

/-- A real strictly between two consecutive integers is not an integer.

This is the exclusion mechanism: the required phase has
`2 cos α_req = 1.99725…`, strictly inside `(1,2)`. -/
theorem not_isInt_of_mem_Ioo_one_two {x : ℝ} (h1 : 1 < x) (h2 : x < 2) :
    ¬ ∃ c : ℤ, x = (c : ℝ) := by
  rintro ⟨c, rfl⟩
  have hc1 : (1 : ℤ) < c := by exact_mod_cast h1
  have hc2 : c < (2 : ℤ) := by exact_mod_cast h2
  omega

/-- **The required ladder phase is not a `q`-uniform braid-image eigenphase.**

Given only that `2 cos α` lies strictly between `1` and `2` — which is what the
measured `α_req` satisfies, `2 cos α_req = 1.99725…` — the phase cannot be the
eigenphase of any braid-image matrix on `V_(2,1)` that is elliptic uniformly in
`q`, because such a character is a constant *integer*.

Note this covers a **constant** `α` as well as a `q`-varying one, which is
exactly the case the boundedness-only argument leaves open. -/
theorem not_braid_eigenphase_of_two_cos_mem_Ioo {α : ℝ}
    (h1 : 1 < 2 * Real.cos α) (h2 : 2 * Real.cos α < 2) :
    ¬ ∃ c : ℤ, 2 * Real.cos α = (c : ℝ) :=
  not_isInt_of_mem_Ioo_one_two h1 h2

end QOU.QBeta.EigenphaseQuantization
