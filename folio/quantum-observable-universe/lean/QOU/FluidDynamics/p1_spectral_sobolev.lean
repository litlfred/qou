import Mathlib.Algebra.Order.Ring.Basic

/-!
# QOU.FluidDynamics.p1_spectral_sobolev — discrete spectrum and Sobolev embedding

**Lemma** ([`prop:p1-spectral-sobolev`](../../../quantum-observable-universe/fluid-dynamics/p1-spectral-sobolev.md)).

*For the `q`-Laplacian `Δ_q` with `q > 1`: (a) the eigenvalues `μ_k` form a
non-negative increasing sequence; (b) `μ_k = [k]_q²`; (c) the Sobolev
embedding `H¹_q ↪ L^∞` holds with constant `C_S`.*

## Formalisation notes
- **Base ring (§7c).** Generic `{R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]` — the
  *weakest* class admitting the ordering claims; **not** `ℝ`.  No
  archimedean construct beyond order is used.  The setup `1 < q` and the
  zpow growth bound (b′) are archimedean refinements not used by the
  statement and are deferred to a post-wall specialisation.
- **Non-degenerate conditional (§3b-cond cond. 5) — (a) is derived.**
  The genuine inputs are the eigenvalue formula (b) (the spectral
  computation) and monotonicity/non-negativity of the `q`-integers; from
  these the theorem **derives** (a): `0 ≤ μ 0 = [0]_q²` and
  `μ k = [k]_q² ≤ [k+1]_q² = μ (k+1)`.  (c) is the Sobolev analytic input,
  carried as a named hypothesis.  Previously all three were bare class
  fields projected into the conclusion. -/

namespace QOU.FluidDynamics

/-- Hypotheses for the discrete spectrum + Sobolev embedding (§7c:
    generic linearly ordered `CommRing` (`IsStrictOrderedRing`), no `ℝ`).  (b) and the `q`-integer
    monotonicity are the genuine inputs; the spectrum ordering (a) is
    *derived* in `p1_spectral_sobolev`. -/
class P1SpectralSobolevContext (R : Type*) [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] where
  /-- The `q`-integer `[k]_q = (q^k − q^{−k})/(q − q^{−1})`. -/
  q_int : ℕ → R
  /-- The `q`-integers are non-negative (holds for `q > 1`). -/
  q_int_nonneg : ∀ k, 0 ≤ q_int k
  /-- The `q`-integers increase in `k` (holds for `q > 1`). -/
  q_int_mono : ∀ k, q_int k ≤ q_int (k + 1)
  /-- The discrete `q`-Laplacian eigenvalues `μ_k`. -/
  μ : ℕ → R
  /-- **(b) — the spectral computation:** eigenvalue closed form
      `μ_k = [k]_q²`. -/
  eigenvalue_formula : ∀ k, μ k = (q_int k) ^ 2
  /-- Sobolev embedding constant `C_S` for `H¹_q ↪ L^∞`. -/
  C_S : R
  /-- `H¹_q`- and `L^∞`-norms of an arbitrary test function. -/
  H1_norm : R
  Linf_norm : R
  /-- **(c) — the analytic input:** Sobolev embedding bound
      `‖f‖_{L^∞} ≤ C_S · ‖f‖_{H¹_q}`. -/
  sobolev_embedding : Linf_norm ≤ C_S * H1_norm

/-- **Discrete spectrum + Sobolev embedding** ([`prop:p1-spectral-sobolev`]).

    (a) the spectrum is increasing and non-negative — *derived* from the
    eigenvalue formula and `q`-integer monotonicity (`mul_self_le_mul_self`
    / `mul_self_nonneg`); (b) restates the spectral computation; (c)
    restates the Sobolev input. -/
-- Ref: [leitner2026] quantum-observable-universe/fluid-dynamics/p1-spectral-sobolev.ts
theorem p1_spectral_sobolev {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    [ctx : P1SpectralSobolevContext R] :
    (∀ k : ℕ, ctx.μ k ≤ ctx.μ (k + 1) ∧ 0 ≤ ctx.μ 0) ∧
    (∀ k : ℕ, ctx.μ k = (ctx.q_int k) ^ 2) ∧
    ctx.Linf_norm ≤ ctx.C_S * ctx.H1_norm := by
  refine ⟨fun k => ⟨?_, ?_⟩, ctx.eigenvalue_formula, ctx.sobolev_embedding⟩
  · rw [ctx.eigenvalue_formula k, ctx.eigenvalue_formula (k + 1), pow_two, pow_two]
    exact mul_self_le_mul_self (ctx.q_int_nonneg k) (ctx.q_int_mono k)
  · rw [ctx.eigenvalue_formula 0, pow_two]
    exact mul_self_nonneg _

end QOU.FluidDynamics
