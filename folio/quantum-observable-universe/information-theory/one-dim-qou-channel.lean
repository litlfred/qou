import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# One-dimensional QOU channel (optical fibre)

A 1D QOU channel is a bounded braid carrier: `n` strands (the fibre modes)
propagate along a line carrying a braid word, and the transmitted,
measurable datum is its Markov trace `trace : R`. The cladding is a
topological boundary that confines the braid, so a strand cannot cross
the surface of the fibre.

Parallel placement of two cladded channels is a *split* configuration —
the boundary suppresses every inter-channel crossing — and the Markov
trace is multiplicative over split links, so the joint channel's trace is
the product. This file proves the resulting laws: parallel placement is
commutative, associative, has the vacuum channel as identity, and
factorises the trace. Non-interacting fibres thus compose as independent
multiplicative information sources.

Ref: docs/audits/2026-06-08-q-regime-map-coordination.md (q-regime seam);
split-link multiplicativity of the Markov trace is the Jones/Markov trace
property (the disjoint-union rule for the bracket).
-/

namespace QOU.Information

/-- A **one-dimensional QOU channel** over a coefficient ring `R`: the
carried information is summarised by its Markov-trace value `trace`. -/
structure OneDimChannel (R : Type*) [CommRing R] where
  trace : R

namespace OneDimChannel

variable {R : Type*} [CommRing R]

/-- The **vacuum channel** (empty fibre): trivial braid, trace `1`. -/
def vacuum : OneDimChannel R := ⟨1⟩

/-- **Parallel placement** of two cladded channels. The surface boundary
makes the configuration a split link, over which the Markov trace
multiplies, so the joint trace is the product. -/
def parallel (A B : OneDimChannel R) : OneDimChannel R := ⟨A.trace * B.trace⟩

/-- **Non-interaction.** The transmitted invariant of two parallel fibres
factorises: `tr_M(A ∥ B) = tr_M(A) · tr_M(B)`. -/
theorem parallel_noninteraction (A B : OneDimChannel R) :
    (parallel A B).trace = A.trace * B.trace := rfl

/-- Parallel placement is commutative. -/
theorem parallel_comm (A B : OneDimChannel R) : parallel A B = parallel B A := by
  simp only [parallel, mul_comm A.trace B.trace]

/-- Parallel placement is associative. -/
theorem parallel_assoc (A B C : OneDimChannel R) :
    parallel (parallel A B) C = parallel A (parallel B C) := by
  simp only [parallel, mul_assoc]

/-- The vacuum channel is a left identity. -/
theorem vacuum_parallel (A : OneDimChannel R) : parallel vacuum A = A := by
  cases A; simp only [parallel, vacuum, one_mul]

/-- The vacuum channel is a right identity. -/
theorem parallel_vacuum (A : OneDimChannel R) : parallel A vacuum = A := by
  cases A; simp only [parallel, vacuum, mul_one]

end OneDimChannel

end QOU.Information
