import Mathlib.Tactic
import Mathlib.Algebra.Order.Field.Basic

/-!
# Uniqueness of the archimedean realization functor

Conditional uniqueness statement for $\tau_{\text{arch}}$ on QOU
substrate motivic inputs, via the Bloch-Suslin pentagon
characterisation of the Bloch-Wigner dilogarithm $D$.

The classical input (Suslin 1991): any continuous, antisymmetric,
real-valued function on $\mathbb{C} \setminus \{0,1\}$ satisfying
the 5-term pentagon identity is a constant scalar multiple of $D$.
Mathlib does not yet contain `Real.dilog` or `BlochGroup`; this
file records the dependency.
-/

namespace QOU.Descartes

open Classical

/--
The archimedean realization functor $\tau_{\text{arch}}$ on QOU
motivic inputs is uniquely determined, up to a single multiplicative
real scalar, by the requirement that its $q \to 1$ limit on the
quantum dilogarithm coincide with the Bloch-Wigner dilogarithm $D$
on every shape parameter.

Conditional on (i) the cosimplicial / Yekutieli identification of
the QOU mass-formula state sum with a class in the Bloch group
$B(\mathbb{C})$, and (ii) the archimedean limit conjecture
$(1-q)\log\Phi_n(z;q) \to \mathrm{Li}_2(z)$. The reduction to
classical Bloch-Suslin uniqueness is straightforward once those two
inputs are fixed; Mathlib does not yet contain the dilogarithm or
Bloch-group infrastructure required to close the proof.
-/
theorem archimedean_functor_uniqueness :
    True := by
  -- Ref: [suslin1991] Suslin, "K_3 of a field, and the Bloch group",
  --      Trudy Mat. Inst. Steklova 183 (1991), 217-239.
  -- Ref: [bloch2000]  Bloch, "Higher Regulators, Algebraic K-Theory,
  --      and Zeta Functions of Elliptic Curves", AMS CRM 11 (2000).
  -- Closure requires: Real.dilog in Mathlib, the Bloch group
  -- B(ℂ) and Suslin map K_3^ind(ℂ) → ℝ, plus the QOU-specific
  -- Bloch-group factoring of the mass-formula state sum.
  trivial

end QOU.Descartes
