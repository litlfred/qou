import Mathlib.Analysis.Meromorphic.Divisor
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Analysis.Complex.Basic
import Mathlib.MeasureTheory.Integral.CircleIntegral

/-!
# The argument principle — scaffold (PI-3, bean `qou-bmyx`)

For `f` meromorphic on a closed disc `\overline{B}(c,R)` with **no zeros or poles
on the bounding circle**, the contour integral of the logarithmic derivative
counts zeros minus poles with multiplicity:

$$\frac{1}{2\pi i}\oint_{|z-c|=R} \frac{f'(z)}{f(z)}\,dz
   \;=\; \sum_{w\in B(c,R)} \operatorname{ord}_w f
   \;=\; \#\{\text{zeros}\} - \#\{\text{poles}\}\quad(\text{with multiplicity}).$$

This is the **argument principle**. It is the least-Analysis-blocked of the three
`PentagonRigidity` infra walls (PI-1 Hadamard factorization, PI-2 elliptic
divisor-degree, PI-3 here): PI-2's degree-zero theorem and PI-1's canonical-product
zero-counting BOTH reduce to it (`elliptic_divisor_degree_zero` names the argument
principle as its explicit open core; a canonical product's zero count is this
integral applied to an entire `f`). The `f'/f`-integrand carries the *analytic*
content; the RHS is the purely-combinatorial divisor sum.

MOTIVATION (epic `qou-lbth`). The residual analytic leg of
`PentagonRigidity.uniqueUpToScalar` needs to pin the canonical minimal Faddeev
solution `phiBProd` among its elliptic multiples by counting zeros; the
argument principle is the tool that turns "a contour integral of `f'/f`" into
"an integer count of zeros", and is the shared engine under both PI-1 and PI-2.

## What is authored here — bricks vs. open core

**Elementary bricks (full proofs, Mathlib-only cone — see the verification caveat):**

* `toNat_sub_toNat_neg` — the integer identity `n.toNat - (-n).toNat = n`.
* `zeroCount` / `poleCount` and `zeroCount_sub_poleCount_eq_sum_divisor` — the
  RHS bookkeeping: `#zeros - #poles = Σ ord`, decomposing the divisor sum into its
  positive (zero) and negative (pole) parts. This is the combinatorial half of the
  argument principle, complete and independent of any analysis.
* `two_pi_I_ne_zero'` — the normalization `2πi ≠ 0`, making the `(2πi)⁻¹` factor
  well-defined (Mathlib also has `Complex.two_pi_I_ne_zero`; reproved locally to
  keep the cone explicit).

**Stated open (the genuinely-hard analytic core — a real Mathlib v4.24.0 gap):**

* `residue_logDeriv_eq_order` — the **local** argument principle: for `f`
  meromorphic at `w`, the small-circle integral `(2πi)⁻¹ ∮_{C(w,r)} f'/f` equals the
  order `ord_w f`. This is the single-point residue-of-a-logarithmic-derivative fact
  (`f'/f` has a simple pole at `w` with residue `ord_w f`). It is THE missing brick.
* `argument_principle` — the global statement (contour integral = divisor sum),
  the composition of the local residue with the residue theorem over the finitely
  many divisor points in the disc.
* `entire_zero_count` — the PI-3 **canonical-product application**: for an entire
  `f` (no poles ⇒ `divisor ≥ 0`), `(2πi)⁻¹ ∮_{C(c,R)} f'/f` equals the number of
  zeros in `B(c,R)` with multiplicity. This is what counts the zeros of a Hadamard
  canonical product (PI-1).

Each `sorry` carries `-- Ref:`. **Not** vacuous `True`, **not** axiomatized as
proved (§Axiomatization-is-NOT-a-Proof): the deep theorem is stated with its real
content and left open.

## Mathlib v4.24.0 gap — exactly what is present vs. absent

Present: `Complex.CauchyIntegral` (`circleIntegral_sub_center_inv_smul_of_…`,
the Cauchy integral / residue of a *simple explicit* pole `(z-c)⁻¹`),
`MeromorphicOn.divisor` (the ℤ-valued zeros-minus-poles counting function, with
`divisor_apply`, `divisor_mul`, `divisor_inv`, `divisor_nonneg`),
`meromorphicOrderAt` (per-point order), `logDeriv` (`= f'/f`, with `logDeriv_mul`,
`logDeriv_zpow`), Jensen's formula (`Analysis/Complex/JensenFormula`,
`extract_zeros_poles`), and the Nevanlinna value-distribution cone
(`Analysis/Complex/ValueDistribution/`, `logCounting`, First Main Theorem).

Absent: the **argument principle itself** — the identity linking `(1/2πi)∮ f'/f`
to `Σ ord`. Concretely, the missing link is `residue_logDeriv_eq_order`: that the
residue of `logDeriv f` at `w` equals `meromorphicOrderAt f w`. Mathlib has the
Cauchy formula for a bare `(z-c)⁻¹` factor but NOT the computation that `f'/f`
develops a simple pole of residue `ord_w f` at each zero/pole `w`, nor the residue
theorem summing those residues over a contour. `Complex.residue`, a general residue
theorem, and `windingNumber` are all absent. So the gap `(1/2πi)∮ f'/f = #zeros −
#poles` is exactly ONE local lemma (`residue_logDeriv_eq_order`) plus a residue-sum
assembly.

-- Ref: [manuscript] Argument principle / residue of the logarithmic derivative;
--   standard complex analysis (Ahlfors, *Complex Analysis*, Ch. 5 §2; Conway
--   VI.1). Absent from Mathlib v4.24.0. See
--   docs/audits/2026-07-20-argument-principle-scaffold.md.

## VERIFICATION STATUS (STRICT, honest)

**COMPILE-VERIFIED `lean`-direct, exit 0** (2026-07-20, this environment; the
Analysis oleans present — `Complex.CauchyIntegral`, `CircleIntegral`,
`Meromorphic/*`, `Calculus/LogDeriv` — turned out sufficient to elaborate the import
cone via `LEAN_PATH` over the package olean dirs). The three elementary bricks
(`toNat_sub_toNat_neg`, `zeroCount_sub_poleCount_eq_sum_divisor`, `two_pi_I_ne_zero'`)
are **sorry-free**; the only warnings are the three intended
`declaration uses 'sorry'` on the deep open theorems below
(`residue_logDeriv_eq_order`, `argument_principle`, `entire_zero_count`), each with a
cited `-- Ref:`. Not vacuous `True`, not axiomatized as proved. A full `lake build QOU`
on a host with the complete Analysis cone remains the CI gate.
-/

open Filter Topology Complex

namespace QOU.Mathlib.ArgumentPrinciple

/-! ### Combinatorial brick: `#zeros − #poles = Σ ord` (analysis-free) -/

/-- **The integer split identity** `n = n⁺ − n⁻`, i.e. `n.toNat − (−n).toNat = n`.
For `n ≥ 0` this is `n − 0`; for `n < 0` it is `0 − (−n)`. This is the per-point
statement that a divisor value (zero-order minus pole-order) decomposes into a
zero contribution and a pole contribution. -/
theorem toNat_sub_toNat_neg (n : ℤ) : (n.toNat : ℤ) - ((-n).toNat : ℤ) = n := by
  omega

/-- **Zero count**: the sum of positive divisor values (orders of zeros) over a
finite set `S` of points. With `S` = the divisor's support inside a region, this is
`#zeros` counted with multiplicity. -/
def zeroCount (D : ℂ → ℤ) (S : Finset ℂ) : ℕ := ∑ w ∈ S, (D w).toNat

/-- **Pole count**: the sum of the magnitudes of negative divisor values (orders of
poles). With `S` = the divisor support inside a region, this is `#poles` counted
with multiplicity. -/
def poleCount (D : ℂ → ℤ) (S : Finset ℂ) : ℕ := ∑ w ∈ S, ((-(D w)).toNat)

/-- **The RHS of the argument principle, combinatorially.** For any ℤ-valued
divisor `D` and finite support set `S`, `#zeros − #poles = Σ ord`:
`(zeroCount D S) − (poleCount D S) = ∑_{w∈S} D w`. This is the whole right-hand
side, complete and analysis-free — the argument principle's remaining content is
entirely the *left*-hand (contour-integral) side. -/
theorem zeroCount_sub_poleCount_eq_sum_divisor (D : ℂ → ℤ) (S : Finset ℂ) :
    (zeroCount D S : ℤ) - (poleCount D S : ℤ) = ∑ w ∈ S, D w := by
  simp only [zeroCount, poleCount, Nat.cast_sum]
  rw [← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl (fun w _ => toNat_sub_toNat_neg (D w))

/-! ### Normalization brick: `2πi ≠ 0` -/

/-- **The Cauchy normalization `2πi ≠ 0`.** Makes the `(2πi)⁻¹` prefactor of the
argument principle a genuine inverse (Mathlib: `Complex.two_pi_I_ne_zero`; reproved
locally to keep this file's cited API explicit). -/
theorem two_pi_I_ne_zero' : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
  have hpi : (Real.pi : ℂ) ≠ 0 := by
    exact_mod_cast Real.pi_ne_zero
  exact mul_ne_zero (mul_ne_zero two_ne_zero hpi) Complex.I_ne_zero

/-! ### The local argument principle (deep core — stated open)

The single missing Mathlib brick: the residue of the logarithmic derivative at a
point equals the meromorphic order there. Everything global is this, summed. -/

/-- **Residue of the logarithmic derivative = order** (the local argument
principle). For `f` meromorphic at `w` with finite order `n = ord_w f`, and all
sufficiently small circles `C(w,r)` avoiding other zeros/poles, the small-circle
average of `f'/f` recovers the integer order:
`(2πi)⁻¹ ∮_{C(w,r)} logDeriv f = n`.

Reason: near `w`, `f(z) = (z-w)^n·g(z)` with `g` analytic and nonvanishing
(`meromorphicOrderAt_eq_int_iff`), so `logDeriv f = n/(z-w) + logDeriv g`; the
analytic `logDeriv g` integrates to `0` (Cauchy), and `∮ (z-w)⁻¹ = 2πi`
(`circleIntegral_sub_center_inv_smul_of_differentiable_on_off_countable`), leaving
`n`. Mathlib has BOTH ingredients but not this composition.

**OPEN — the genuine Mathlib v4.24.0 gap.** Hypotheses (finiteness of the order,
smallness of `r`, pole-avoidance on the circle) are packaged so the analytic core
is isolated. -/
theorem residue_logDeriv_eq_order {f : ℂ → ℂ} {w : ℂ} {r : ℝ} {n : ℤ}
    (hf : MeromorphicAt f w) (hr : 0 < r)
    (horder : meromorphicOrderAt f w = (n : WithTop ℤ))
    (hclean : ∀ z ∈ Metric.sphere w r, f z ≠ 0)
    (hsmall : ∀ z ∈ Metric.closedBall w r, z ≠ w → meromorphicOrderAt f z = 0) :
    (2 * (Real.pi : ℂ) * Complex.I)⁻¹ * (∮ z in C(w, r), logDeriv f z) = (n : ℂ) := by
  -- Ref: [manuscript] Ahlfors §5.2 (residue of f'/f = order); Mathlib gap. See
  --   docs/audits/2026-07-20-argument-principle-scaffold.md.
  sorry

/-! ### The global argument principle (deep core — stated open) -/

/-- **The argument principle.** For `f` meromorphic on the closed disc
`\overline B(c,R)`, with no zeros or poles on the boundary circle, the contour
integral of `f'/f` counts the interior divisor:
`(2πi)⁻¹ ∮_{C(c,R)} logDeriv f = Σ_{w∈S} ord_w f`,
where `S` enumerates the finitely many interior points where the divisor is
nonzero. Combined with `zeroCount_sub_poleCount_eq_sum_divisor`, the RHS is
`#zeros − #poles` with multiplicity.

**OPEN.** Classical proof: `residue_logDeriv_eq_order` at each point of `S`, summed
by the residue theorem (contour deformation onto small circles around each divisor
point). The residue theorem for meromorphic functions is itself absent from
Mathlib v4.24.0; the per-point residue is `residue_logDeriv_eq_order`. Finiteness of
`S` (`MeromorphicOn.divisor` is `locallyFinsuppWithin`, intersected with the compact
disc) is passed as `hS` to isolate the analytic core. -/
theorem argument_principle {f : ℂ → ℂ} {c : ℂ} {R : ℝ} (hR : 0 < R)
    (hf : MeromorphicOn f (Metric.closedBall c R))
    (hclean : ∀ z ∈ Metric.sphere c R, meromorphicOrderAt f z = 0)
    (S : Finset ℂ)
    (hS : (S : Set ℂ) =
      {z | z ∈ Metric.ball c R ∧ (MeromorphicOn.divisor f (Metric.closedBall c R)) z ≠ 0}) :
    (2 * (Real.pi : ℂ) * Complex.I)⁻¹ * (∮ z in C(c, R), logDeriv f z)
      = ((∑ w ∈ S, (MeromorphicOn.divisor f (Metric.closedBall c R)) w : ℤ) : ℂ) := by
  -- Ref: [manuscript] argument principle = Σ residues of f'/f; Mathlib gap. See
  --   docs/audits/2026-07-20-argument-principle-scaffold.md.
  sorry

/-! ### PI-3 canonical-product application: zero-counting for entire `f` -/

/-- **Zero count of an entire function (canonical-product application).** For `f`
entire (`Differentiable ℂ f`) — in particular a Hadamard canonical product (PI-1) —
there are no poles, so `divisor ≥ 0` and the argument principle counts *zeros*:
`(2πi)⁻¹ ∮_{C(c,R)} f'/f = zeroCount = #zeros in B(c,R)` with multiplicity.

This is the PI-3 payload for the pentagon program: it makes the number of zeros of
the canonical minimal Faddeev product `phiBProd` inside a disc an explicit contour
integral, the tool that pins `phiBProd` among its elliptic multiples.

**OPEN** — specialization of `argument_principle` to the entire (pole-free) case
(`hf` entire ⇒ `divisor f` supported on zeros only, so `Σ ord = zeroCount`). Stated
open because it composes the open `argument_principle`. -/
theorem entire_zero_count {f : ℂ → ℂ} {c : ℂ} {R : ℝ} (hR : 0 < R)
    (hf : Differentiable ℂ f)
    (hclean : ∀ z ∈ Metric.sphere c R, f z ≠ 0)
    (S : Finset ℂ)
    (hS : (S : Set ℂ) =
      {z | z ∈ Metric.ball c R ∧
        (MeromorphicOn.divisor f (Metric.closedBall c R)) z ≠ 0}) :
    (2 * (Real.pi : ℂ) * Complex.I)⁻¹ * (∮ z in C(c, R), logDeriv f z)
      = (zeroCount (fun z => (MeromorphicOn.divisor f (Metric.closedBall c R)) z) S : ℂ) := by
  -- Ref: [manuscript] argument principle for entire f (pole-free ⇒ counts zeros);
  --   Mathlib gap. See docs/audits/2026-07-20-argument-principle-scaffold.md.
  sorry

end QOU.Mathlib.ArgumentPrinciple
