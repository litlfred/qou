import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Algebra.Algebra.Defs
import Mathlib.LinearAlgebra.Trace
import Mathlib.Tactic

/-!
# The curvature trace is a commutator-with-ρ sum, in every irrep (qou-o6ov)

**Context.** The projector curvature `Ω₂^P = (4/[2]_q²)·Σ_a [σ_a, σ_{a+1}]` (#6445) is a genuine
Hecke-algebra element. Every previous handle on its trace was **family-specific**: the hook column
via the reduced Burau (#6464, #6480, #6520), the two-row column via R-matrix weight sectors
(#6525). This file records the identity that is **family-independent** — it holds in every irrep
and follows from trace cyclicity alone:

```
tr (ρ · Σ_a [σ_a, σ_{a+1}]) = Σ_a tr ([ρ, σ_a] · σ_{a+1}).            (★)
```

Derivation, one commutator at a time:
`tr(ρσ_aσ_{a+1}) − tr(ρσ_{a+1}σ_a) = tr(ρσ_aσ_{a+1}) − tr(σ_aρσ_{a+1}) = tr([ρ,σ_a]·σ_{a+1})`,
the middle step being cyclicity applied to `ρ·σ_{a+1}` and `σ_a`.

**Why it matters.** `(★)` puts the decay object on `[ρ, σ_a]` — the arc's *original* single-window
object — and says the whole thing is governed by how the braid word fails to commute with each
generator: if `ρ` commuted with every `σ_a`, the trace would vanish identically in every irrep.

**What it does NOT give: the decay is CANCELLATION, not size (settled by the conjugate-pair
control, `magnus_conjugate_pair_cancellation_probe.py`).** `(★)` says *what* the decay object is,
not why it falls with `b(λ)`. The control is conjugate partitions: `dim λ = dim λ'` **exactly**
while `b` flips, so a pair is two irreps of identical dimension at very different `b` — the
dimension confound removed by a theorem rather than by normalisation. Measured at A = 2 and 3
(exact mpf), ratios being higher-`b` partner ÷ lower-`b`:

* **9 of 9 pairs: commutator-norm ratio ≥ 1** (1.13–1.31, clustered near 1.25) while the
  **trace ratio is 0.003–0.27**. Sharpest: `(8,1)` vs `(2,1⁷)`, both dimension 8 —
  `‖[ρ,σ_a]‖` rises `0.755 → 0.955` while `|tr|/dim` falls `33.65 → 0.115`.

So at equal dimension the high-`b` irrep has *larger* commutators and a *far smaller* trace.
Consequently **no bound of the form `|tr| ≤ Σ_a ‖[ρ,σ_a]‖·‖σ_{a+1}‖` can produce the decay** — it
runs the wrong way on every pair measured. This is scope-(a): the plain norm route as-is is
excluded, not every norm-flavoured argument. It also explains why the hook bound (#6520) had to go
through the *spectrum* (`e_j` of the Burau moduli); that was the route available, not merely the
route taken, and a general-`λ` bound should be spectral in the same sense.

A raw `b`-scan cannot see this: the normalised norm is **U-shaped** in `b` (falls to a mid-`b`
minimum, then rises), so a scan truncated before the tail reads as "the norm falls with `b`" and
inverts the answer. An earlier version of this docstring asserted the conclusion from A = 2 alone,
was then retracted to "open" on half-measured A = 3 data, and is now restored on the control that
actually establishes it — see
`docs/audits/2026-09-04-magnus-b-decay-is-cancellation-not-size.md`.

**Scope.** Sorry-free and unconditional, over any `R`-algebra `A` with an `R`-linear functional
`tr` satisfying cyclicity `tr (x*y) = tr (y*x)` — the hypothesis is carried explicitly, since a
general linear functional is not a trace. The Hecke-specific content (the seminormal
construction, the atom word) is outside Mathlib, as in the sibling files.
-/

namespace QOU.MassTheory

open Finset BigOperators

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The nearest-neighbour commutator sum `Σ_a [σ_a, σ_{a+1}]` — the projector curvature `Ω₂^P`
without its constant `4/[2]_q²` prefactor. Mirrors `MagnusGaugeCurvatureHookColumn.curvatureSum`;
restated here so this file stands alone on the cyclicity argument. -/
def commSum (σ : ℕ → A) (m : ℕ) : A :=
  ∑ a ∈ range m, (σ a * σ (a + 1) - σ (a + 1) * σ a)

/-- **One commutator, rewritten onto `[ρ, σ_a]`.** For a cyclic linear functional,
`tr (ρ · [x, y]) = tr ([ρ, x] · y)`. This is the whole content of `(★)`; the sum is a
`Finset.sum_congr` over it. -/
theorem trace_mul_commutator_eq (tr : A →ₗ[R] R)
    (hcyc : ∀ x y : A, tr (x * y) = tr (y * x)) (ρ x y : A) :
    tr (ρ * (x * y - y * x)) = tr ((ρ * x - x * ρ) * y) := by
  have h : tr (ρ * (y * x)) = tr ((x * ρ) * y) := by
    rw [← mul_assoc, hcyc (ρ * y) x, mul_assoc]
  rw [mul_sub, map_sub, h, sub_mul, map_sub, ← mul_assoc]

/-- **(★) The curvature trace is a commutator-with-`ρ` sum.**
`tr (ρ · Σ_a [σ_a, σ_{a+1}]) = Σ_a tr ([ρ, σ_a] · σ_{a+1})`, in every representation — no
Burau, no R-matrix, no family restriction. Sorry-free; the only hypothesis is cyclicity of `tr`. -/
theorem trace_mul_commSum_eq_sum_comm (tr : A →ₗ[R] R)
    (hcyc : ∀ x y : A, tr (x * y) = tr (y * x)) (ρ : A) (σ : ℕ → A) (m : ℕ) :
    tr (ρ * commSum σ m) = ∑ a ∈ range m, tr ((ρ * σ a - σ a * ρ) * σ (a + 1)) := by
  unfold commSum
  rw [Finset.mul_sum, map_sum]
  refine Finset.sum_congr rfl ?_
  intro a _
  exact trace_mul_commutator_eq tr hcyc ρ (σ a) (σ (a + 1))

/-- **The vanishing corollary.** If `ρ` commutes with every generator, the curvature trace is
zero in every representation. This is the sharp statement of what `(★)` identifies as the source
of the whole decay object: it is entirely a failure-to-commute effect. -/
theorem trace_mul_commSum_eq_zero_of_commute (tr : A →ₗ[R] R)
    (hcyc : ∀ x y : A, tr (x * y) = tr (y * x)) (ρ : A) (σ : ℕ → A) (m : ℕ)
    (hcomm : ∀ a, ρ * σ a = σ a * ρ) :
    tr (ρ * commSum σ m) = 0 := by
  rw [trace_mul_commSum_eq_sum_comm tr hcyc ρ σ m]
  refine Finset.sum_eq_zero ?_
  intro a _
  rw [hcomm a, sub_self, zero_mul, map_zero]

/-- **The curvature sum is annihilated by every cyclic functional.**  `ρ = 1` in the vanishing
corollary above: the identity commutes with everything, so `tr (Ω₂) = 0` for ANY cyclic linear
`tr`, in every representation, with no hypothesis on `tr` beyond cyclicity. -/
theorem trace_commSum_eq_zero (tr : A →ₗ[R] R)
    (hcyc : ∀ x y : A, tr (x * y) = tr (y * x)) (σ : ℕ → A) (m : ℕ) :
    tr (commSum σ m) = 0 := by
  have h := trace_mul_commSum_eq_zero_of_commute tr hcyc 1 σ m
    (fun a => by rw [one_mul, mul_one])
  rwa [one_mul] at h

/-- **(★★) THE `ρ = I` CONTROL IS WEIGHT-BLIND.**  Any two cyclic linear functionals agree on the
curvature sum — both give zero.  So a control that checks `tr (Ω₂) = 0` at trivial density tests
**cyclicity and nothing else**: it carries no information whatever distinguishing one weight
family from another.

Why this is worth stating as a theorem rather than an observation.  The Magnus-Ω₂ sign probes
(`{deuteron,triton}_magnus_omega2_sign_probe.py`,
`he4_magnus_omega2_sign_sparse_probe.py`) each report a `ρ = I` control confirming
`tr(Ω₂) = 0`, and their docstrings correctly read that as *"any nonzero sign REQUIRES the
density"*.  The tempting further step — that a passing control is evidence the aggregation
measure is the right one — is what this refutes: the control passes for the quantum Plancherel
measure and for the Ocneanu/Wenzl family alike, and would pass for any cyclic functional
whatsoever, including ones nobody would propose.

Consequence for `qou-za3q` decision 1: the weight family cannot be chosen on the strength of
the control.  It is fixed instead by the Markov-trace characterisation —
`QOU.SchurWeyl.HeckeCoset.markovTrace_unique` together with
`QOU.SchurWeyl.SeminormalRep.eq_wtrace_of_markov`, which identify the unique Markov trace at
`z_D = q³/(q²+1)` with the Ocneanu/Wenzl weighted seminormal trace.

Note the scope precisely: this says the control cannot DISCRIMINATE.  It does not say the
control is worthless — a control that FAILED would mean the germ or the trace was broken, which
is exactly how the probes use it. -/
theorem trace_commSum_indep_of_cyclic (tr₁ tr₂ : A →ₗ[R] R)
    (h₁ : ∀ x y : A, tr₁ (x * y) = tr₁ (y * x))
    (h₂ : ∀ x y : A, tr₂ (x * y) = tr₂ (y * x)) (σ : ℕ → A) (m : ℕ) :
    tr₁ (commSum σ m) = tr₂ (commSum σ m) := by
  rw [trace_commSum_eq_zero tr₁ h₁ σ m, trace_commSum_eq_zero tr₂ h₂ σ m]

end QOU.MassTheory
