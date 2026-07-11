import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

/-!
# Compact Quantum Dilogarithm — formal power series backbone

The compact quantum dilogarithm (Faddeev–Kashaev) is the reciprocal infinite
product
$$\Phi_q(x) \;=\; \prod_{n=0}^{\infty} \bigl(1 + q^{2n+1}\,x\bigr)^{-1}.$$

This file develops the **algebraic** (formal power series) properties first,
deliberately deferring the analytic/convergence layer.  The core object is the
**finite denominator product**
$$P_N(q, x) \;=\; \prod_{n=0}^{N-1} \bigl(1 + q^{2n+1}\,x\bigr),$$
the finite `q`-Pochhammer symbol $(-qx; q^2)_N$, of which $\Phi_q(x)$ is the
reciprocal of the $N \to \infty$ limit.

Everything here is stated over a **generic `[CommRing R]`** (AGENTS.md §7c: pure
algebra, no archimedean structure).  Because `PowerSeries S` is itself a
`CommRing`, *every* lemma specialises to the formal-power-series statement by
taking `R := PowerSeries S` and `x : PowerSeries S` — no dedicated
`PowerSeries` infinite-product machinery is needed for the finite-truncation
algebra.  In particular the functional equation
[`qPochProd_functional`](#QOU.MathlibExt.QuantumDilogarithm.qPochProd_functional)
is the discrete precursor of the `q`-difference equation
$$\Phi_q(q^2 x) \;=\; (1 + q x)\,\Phi_q(x)$$
that pins the quantum dilogarithm uniquely.

## Consumers

* `QOU.NeutronProtonSplitting` — the hard-coded `quarkPhi` "volumes" are
  evaluations of $\Phi_q$ at the up/down quark orderings; this backbone lets
  them be *defined* rather than pinned as literals.
* `QOU.Archimedean.HyperbolicVolumeIndependence` — the hyperbolic volumes enter
  through the Rogers/Faddeev dilogarithm, whose finite `q`-analogue is $P_N$.

TODO upstream: `Mathlib.RingTheory.PowerSeries` — a general finite
`q`-Pochhammer symbol with its shift relation is a plausible Mathlib
contribution.
-/

namespace QOU.MathlibExt.QuantumDilogarithm

open Finset

variable {R : Type*} [CommRing R]

/-- Finite `q`-Pochhammer denominator product
$P_N(q, x) = \prod_{n=0}^{N-1} (1 + q^{2n+1} x)$, i.e. the truncation
$(-qx; q^2)_N$ whose reciprocal limit is the compact quantum dilogarithm
$\Phi_q(x)$. -/
def qPochProd (q x : R) (N : ℕ) : R :=
  ∏ n ∈ range N, (1 + q ^ (2 * n + 1) * x)

@[simp]
theorem qPochProd_zero (q x : R) : qPochProd q x 0 = 1 := by
  simp [qPochProd]

/-- Peel the **last** factor: $P_{N+1} = P_N \cdot (1 + q^{2N+1} x)$. -/
theorem qPochProd_succ (q x : R) (N : ℕ) :
    qPochProd q x (N + 1) = qPochProd q x N * (1 + q ^ (2 * N + 1) * x) := by
  simp [qPochProd, Finset.prod_range_succ]

@[simp]
theorem qPochProd_one (q x : R) : qPochProd q x 1 = 1 + q * x := by
  simp [qPochProd_succ]

/-- **Functional equation** (discrete `q`-difference precursor of $\Phi_q$).

Peeling the **first** factor and re-indexing gives
$$P_{N+1}(q, x) \;=\; (1 + q x)\,P_N(q,\; q^2 x),$$
the finite shadow of $\Phi_q(q^2 x) = (1 + q x)\,\Phi_q(x)$. -/
theorem qPochProd_functional (q x : R) (N : ℕ) :
    qPochProd q x (N + 1) = (1 + q * x) * qPochProd q (q ^ 2 * x) N := by
  simp only [qPochProd]
  rw [Finset.prod_range_succ', mul_comm]
  refine congr_arg₂ (· * ·) ?_ (Finset.prod_congr rfl fun i _ => ?_)
  · norm_num
  · rw [show 2 * (i + 1) + 1 = 2 * i + 1 + 2 from by ring, pow_add]
    ring

/-- The constant term is `1`: $P_N(q, 0) = 1$ for every `N`
(the formal-power-series normalisation $\Phi_q(0) = 1$). -/
@[simp]
theorem qPochProd_zero_arg (q : R) (N : ℕ) : qPochProd q 0 N = 1 := by
  simp [qPochProd]

/-- `q = 0` collapses every factor past the first to `1`, so
$P_{N+1}(0, x) = 1$ (the classical, undeformed limit is trivial at this
truncation). -/
theorem qPochProd_q_zero (x : R) (N : ℕ) : qPochProd (0 : R) x (N + 1) = 1 := by
  induction N with
  | zero => simp
  | succ n ih => rw [qPochProd_succ, ih]; simp

end QOU.MathlibExt.QuantumDilogarithm
