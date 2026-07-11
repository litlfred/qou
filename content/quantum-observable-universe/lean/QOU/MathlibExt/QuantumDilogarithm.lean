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

/-- **Index additivity (cocycle identity).** Splitting the product after the
first `M` factors and re-indexing the tail rescales the argument by `q^{2M}`:
$$P_{M+N}(q, x) \;=\; P_M(q, x)\,\cdot\,P_N(q,\; q^{2M} x).$$
This is the finite backbone from which both the functional equation
(`M = 1`, below) and — in the limit — the multiplicative cocycle of
$\Phi_q$ under the `q`-shift descend. -/
theorem qPochProd_add (q x : R) (M N : ℕ) :
    qPochProd q x (M + N) = qPochProd q x M * qPochProd q (q ^ (2 * M) * x) N := by
  simp only [qPochProd]
  rw [Finset.prod_range_add]
  refine congr_arg₂ (· * ·) rfl (Finset.prod_congr rfl fun i _ => ?_)
  rw [show 2 * (M + i) + 1 = 2 * i + 1 + 2 * M from by ring, pow_add]
  ring

/-- **Functional equation** (discrete `q`-difference precursor of $\Phi_q$),
the `M = 1` case of [`qPochProd_add`](#QOU.MathlibExt.QuantumDilogarithm.qPochProd_add):
$$P_{N+1}(q, x) \;=\; (1 + q x)\,P_N(q,\; q^2 x),$$
the finite shadow of $\Phi_q(q^2 x) = (1 + q x)\,\Phi_q(x)$. -/
theorem qPochProd_functional (q x : R) (N : ℕ) :
    qPochProd q x (N + 1) = (1 + q * x) * qPochProd q (q ^ 2 * x) N := by
  rw [add_comm N 1, qPochProd_add, qPochProd_one, mul_one]

/-- The constant term is `1`: $P_N(q, 0) = 1$ for every `N`
(the formal-power-series normalisation $\Phi_q(0) = 1$). -/
@[simp]
theorem qPochProd_zero_arg (q : R) (N : ℕ) : qPochProd q 0 N = 1 := by
  simp [qPochProd]

/-- At `q = 0` every factor collapses to `1` — since `2n+1 ≥ 1` we have
`0 ^ (2n+1) = 0`, so `1 + 0 ^ (2n+1) * x = 1` for *every* `n` (the first
factor included) — hence $P_N(0, x) = 1$ for all `N` (the classical,
undeformed truncation is trivial). -/
@[simp]
theorem qPochProd_q_zero (x : R) (N : ℕ) : qPochProd (0 : R) x N = 1 := by
  induction N with
  | zero => simp
  | succ n ih => rw [qPochProd_succ, ih]; simp

/-!
## Infinite limit — deferred (analytic layer)

The genuine compact quantum dilogarithm is the reciprocal of the `N → ∞`
limit,
$$\Phi_q(x) \;=\; \Bigl(\lim_{N\to\infty} P_N(q, x)\Bigr)^{-1},$$
which is **not** formalised here.  Two honest obstacles, per the
plan that scoped this file to the algebra first:

1. **Convergence is genuinely analytic.** The coefficient of `x^k` in
   `P_N` is the elementary symmetric polynomial `e_k(q, q^3, …, q^{2N-1})`,
   which *grows* with `N`; it stabilises only after summing the geometric
   `q`-series, so the limit lives in a completed ring (`X`-adic
   `PowerSeries`, or `|q| < 1` analytic), **not** in the finite-truncation
   algebra above.  Formalising it needs `Multipliable` in the `X`-adic
   topology (Mathlib `RingTheory.PowerSeries.Inverse` + a completion
   argument), which is the topological-ring layer this tranche defers.
2. **The `q`-shift cocycle survives to the limit** — [`qPochProd_add`](#QOU.MathlibExt.QuantumDilogarithm.qPochProd_add)
   is the finite backbone; the limiting functional equation
   `Φ_q(q² x) = (1 + q x)·Φ_q(x)` is its shadow.

TODO upstream: `Mathlib.RingTheory.PowerSeries.Inverse` — an `X`-adically
convergent infinite product `∏ (1 + aₙ X)` with unit-partial-products, and
its reciprocal, is a plausible Mathlib contribution.
-- Ref: [faddeev1994] https://doi.org/10.1007/BF02101594 — Faddeev, "Discrete
--       Heisenberg–Weyl group and modular group" (the quantum dilogarithm).

The physical **quark-ordering volumes** `Φ(uud) ≈ -0.8785`, `Φ(udd) ≈
-1.2261` consumed by `QOU.Torsion.neutron_proton_splitting` are evaluations
of this *analytic* `Φ_q` on the proton/neutron braid words at `q₀` — they
are **not** derivable from the finite algebra above, and (corpus-grep,
2026-07-11) no closed form for them exists in the corpus yet.  They remain
honest opaque inputs (`NeutronProtonSplittingContext` class fields) until
the braid-word argument identification lands.
-/

end QOU.MathlibExt.QuantumDilogarithm
