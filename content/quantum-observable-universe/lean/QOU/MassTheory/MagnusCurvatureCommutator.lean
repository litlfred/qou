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

**What it does NOT settle — the mechanism is OPEN (measured,
`magnus_curvature_commutator_identity_probe.py`).** `(★)` says *what* the decay object is; it does
not say whether the `b(λ)`-decay is a **size** effect (already in `‖[ρ,σ_a]‖`) or a
**cancellation** in the pairing against `σ_{a+1}`. The probe reports the normalised
`Σ_a ‖[ρ,σ_a]‖_F / (dim·‖ρ‖_F)` next to `|tr|/dim`, and **the two orders disagree across the two
sizes measured so far**:

* **A = 2** (all 11 shapes): the norm *rises* on high-`b` shapes — 0.93 at `b=1`, then 1.11, 1.39,
  1.22 at `b = 3, 4` — while `|tr|/dim` falls monotonically. That would mean cancellation, and
  that no norm bound `|tr| ≤ Σ_a ‖[ρ,σ_a]‖·‖σ_{a+1}‖` can produce the decay.
* **A = 3** (partial, through `b = 4` of `b_max = 8`): the norm is uniformly smaller and *falls*
  — 0.76, 0.28, 0.17, 0.087, 0.20, 0.058 — which would suggest the opposite.

Both cannot be the general story, and the deciding data — the A = 3 high-`b` tail, exactly where
A = 2 turned upward — is **not yet measured**. So no claim is made here either way. What is
independently true is that the hook bound (#6520) *did* have to go through the spectrum (`e_j` of
the Burau moduli) rather than a norm; whether that was forced by cancellation or was merely the
route taken is part of the same open question.

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

end QOU.MassTheory
