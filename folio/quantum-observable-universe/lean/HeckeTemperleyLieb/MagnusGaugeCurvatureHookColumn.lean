import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Algebra.Algebra.Defs
import Mathlib.Tactic

/-!
# The hook column of the gauge-invariant curvature reduces to word-traces (qou-o6ov)

**Context (PR #6445, #6464).** The projector curvature
`Ω₂^P = (4/[2]_q²) · Σ_a [σ_a, σ_{a+1}]` is a genuine element of the Hecke algebra, unlike the
representation-specific germ `q·∂σ·σ⁻¹`. Because it is an algebra element, the reduced-Burau hook
identity of `MagnusHookExteriorPower` (numerically exact to 139 digits, for every *word* `w`)
```
tr_{(k,1ⁿ⁻ᵏ)}(w) = q^{len(w)(1−j)} · e_j(eig w^V),   j = n − k,
```
extends from the plain character to the curvature, giving the closed form verified to the dps
floor on every hook in `computations/deltalambda/magnus_gauge_hook_closed_form_probe.py`:
```
tr_{hook}(ρ·Ω₂^P) = (4/[2]_q²) · q^{(L+2)(1−j)} · Σ_a [ e_j(eig ρσ_aσ_{a+1}) − e_j(eig ρσ_{a+1}σ_a) ].
```

**What is formalized here is the step that makes this a one-line consequence.** The seminormal
Hecke construction, the specific atom word, and the `q`-twist are outside Mathlib (as in
`MagnusHookExteriorPower`). The algebraic content is two facts, general over any `CommRing R`
and any `R`-algebra `A` with an `R`-linear functional `tr` (a trace):

* `trace_mul_curvature_eq_sum_word_traces` — **linearity.** `tr (ρ · Σ_a [σ_a, σ_{a+1}])` equals
  `Σ_a (tr (ρσ_aσ_{a+1}) − tr (ρσ_{a+1}σ_a))`: the curvature trace is a signed sum of traces of
  **words**, each two generators longer than `ρ`. Sorry-free, unconditional.
* `trace_mul_curvature_eq_of_word_traces` — **the closed form, conditional on the hook
  identity.** If every such word-trace is `c · (its elementary-symmetric value)` for a *single*
  scalar `c` — the common twist `q^{(L+2)(1−j)}`, common precisely because both words in each
  commutator have the same length `L+2` — then `tr (ρ · Σ_a [σ_a,σ_{a+1}]) = c · Σ_a (E_a − F_a)`.

The *single* `c` is not a convenience: the probe's first pass used the twist of `ρ` (length `L`)
instead of that of `ρσσ` (length `L+2`) and matched only at `j = 0, 1` and the two endpoints,
where the discrepancy is invisible. Requiring one `c` for both members of every commutator is
that correction stated structurally.

Hypothesis-carrying, per AGENTS.md §"Conditional-proved ≠ premise-established": the theorem proves
the implication; the per-word hook identity is the numerically-established premise, not proved here.
-/

namespace QOU.MassTheory

open Finset BigOperators

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The second-order (projector) curvature as a sum of nearest-neighbour commutators of the
generators `σ`, over the interior pairs `a = 0, …, m−1`: `Σ_a (σ_a σ_{a+1} − σ_{a+1} σ_a)`. The
overall scalar `4/[2]_q²` of `Ω₂^P` is omitted — it is a constant that commutes with everything
below and is restored at the end. -/
def curvatureSum (σ : ℕ → A) (m : ℕ) : A :=
  ∑ a ∈ range m, (σ a * σ (a + 1) - σ (a + 1) * σ a)

/-- **Linearity: the curvature trace is a signed sum of word-traces.** For any `R`-linear
functional `tr : A →ₗ[R] R`,
`tr (ρ · Σ_a [σ_a, σ_{a+1}]) = Σ_a (tr (ρ σ_a σ_{a+1}) − tr (ρ σ_{a+1} σ_a))`.
Each term on the right is the trace of a *word* two generators longer than `ρ`, which is what
lets the reduced-Burau hook identity apply term by term. Sorry-free, unconditional. -/
theorem trace_mul_curvature_eq_sum_word_traces (tr : A →ₗ[R] R) (ρ : A) (σ : ℕ → A) (m : ℕ) :
    tr (ρ * curvatureSum σ m)
      = ∑ a ∈ range m, (tr (ρ * σ a * σ (a + 1)) - tr (ρ * σ (a + 1) * σ a)) := by
  unfold curvatureSum
  rw [Finset.mul_sum, map_sum]
  refine Finset.sum_congr rfl ?_
  intro a _
  rw [mul_sub, map_sub, mul_assoc, mul_assoc]

/-- **The closed form, conditional on the per-word hook identity with a common twist.**
Suppose every commutator-member word-trace is `c` times an elementary-symmetric value —
`tr (ρσ_aσ_{a+1}) = c · E a` and `tr (ρσ_{a+1}σ_a) = c · F a` — with **one** scalar `c` for all
of them (the common twist `q^{(L+2)(1−j)}`; common because every such word has length `L+2`).
Then `tr (ρ · Σ_a [σ_a, σ_{a+1}]) = c · Σ_a (E a − F a)`, which is the reduced-Burau closed form
for the hook column of the gauge-invariant curvature (the `4/[2]_q²` prefactor restored
externally). Sorry-free; proves the implication only (`_of_` naming per `local/formalizer`). -/
theorem trace_mul_curvature_eq_of_word_traces (tr : A →ₗ[R] R) (ρ : A) (σ : ℕ → A) (m : ℕ)
    (c : R) (E F : ℕ → R)
    (hE : ∀ a ∈ range m, tr (ρ * σ a * σ (a + 1)) = c * E a)
    (hF : ∀ a ∈ range m, tr (ρ * σ (a + 1) * σ a) = c * F a) :
    tr (ρ * curvatureSum σ m) = c * ∑ a ∈ range m, (E a - F a) := by
  rw [trace_mul_curvature_eq_sum_word_traces, Finset.mul_sum]
  refine Finset.sum_congr rfl ?_
  intro a ha
  rw [hE a ha, hF a ha, mul_sub]

end QOU.MassTheory
