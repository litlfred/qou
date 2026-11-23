import Mathlib.Algebra.Field.Basic
import Mathlib.Analysis.Normed.Group.Basic


/-!
# QOU.Braiding.hecke_mass_trace — Mass via the Markov trace

The categorical mass equals the Frobenius norm of the Markov trace
of the Hecke mass element:

  m(ϱ_β) = ‖tr_M(Φ_mass(β))‖_F

Moreover, the topological decomposition (descended + transient)
descends to H_n(q) via the linearity of tr_M.

**Two-tier split.** Per the audit
[`docs/audits/2026-05-03-pre-archimedean-proof-audit.md`](../../../docs/audits/2026-05-03-pre-archimedean-proof-audit.md)
§1 Step 19, the previous version typed every trace component as
`ℝ` and used the Archimedean `|·|`.  But `tr_M : H_n(R, q) → R`
maps into the Laurent ring; the Frobenius norm is `R`-valued, not
`ℝ`-valued.  We split into:

  - `Pre`  — formal Markov trace data over an abstract field `R`,
    Frobenius norm `‖·‖_F` valued in `R`.
  - `Arch` — the Archimedean realisation `R = ℝ` with `|·|`, the
    Kashaev/dilog bridge `Vol(K)/ℏ²`, and the explicit positivity
    hypotheses on `vol, ℏ`.

LaTeX label: `conj:hecke-mass-trace`

## References

- [leitner2026] §4/hecke-mass-trace
- [jones1987] https://doi.org/10.2307/1971403
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.Braiding

/-! ## §1.  Pre-Archimedean tier (formal `R`-valued trace) -/

namespace Pre

universe u

/-- Pre-Arch data for the Markov trace computation of mass.

    Polymorphic in the ground field `R`.  Encodes the fibre-functor
    image: the categorical trace becomes the Markov trace, and the
    mass integrand becomes the Hecke mass element.  The Frobenius
    norm of `tr_M(Φ_mass)` (computed in `R`, not `ℝ`) equals the
    categorical mass. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
structure MarkovMassData (R : Type u) [Field R] where
  /-- The Markov trace of the mass element: `tr_M(Φ_mass(β))`. -/
  markovTrace : R
  /-- The Markov trace of the descended component: `tr_M(Φ^desc)`. -/
  descendedTrace : R
  /-- The Markov trace of the transient component: `tr_M(Φ^trans)`. -/
  transientTrace : R
  /-- Linearity of `tr_M`:
      `tr_M(Φ_mass) = tr_M(Φ^desc) + tr_M(Φ^trans)`. -/
  trace_decomposition :
    markovTrace = descendedTrace + transientTrace

/-- **Pre-Arch mass via the Markov trace.**

    The categorical mass-squared equals the Frobenius pairing of
    `tr_M(Φ_mass)` with itself, valued in `R`.  Caller supplies
    the Frobenius pairing. -/
-- Ref: [leitner2026] §4/hecke-mass-trace
def categoricalMassSquaredFromMarkov {R : Type u} [Field R]
    (frobeniusPairing : R → R → R)
    (d : MarkovMassData R) : R :=
  frobeniusPairing d.markovTrace d.markovTrace

end Pre

/-! ## §2.  Archimedean tier (post-τ realisation) -/

namespace Arch

/-! ## Mass via the Markov trace of the Hecke mass element -/

/-- Data for the Markov trace computation of mass.

    Encodes the fibre-functor image: the categorical trace becomes
    the Markov trace, and the mass integrand becomes the Hecke mass
    element.  The norm of tr_M(Φ_mass) equals the categorical mass.

    Per `QOU.GroundRingAnnotations`, this is the Archimedean
    realisation; the pre-Arch declaration lives in `Pre` above. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
structure MarkovMassData where
  /-- The Markov trace of the mass element: tr_M(Φ_mass(β)). -/
  markovTrace : ℝ
  /-- The Markov trace of the descended component: tr_M(Φ^desc). -/
  descendedTrace : ℝ
  /-- The Markov trace of the transient component: tr_M(Φ^trans). -/
  transientTrace : ℝ
  /-- Linearity of tr_M: tr_M(Φ_mass) = tr_M(Φ^desc) + tr_M(Φ^trans). -/
  trace_decomposition : markovTrace = descendedTrace + transientTrace

/-- **Trace-side mass** for `conj:hecke-mass-trace`.

    This is the absolute value of the Markov trace of the Hecke mass
    element, |tr_M(Φ_mass(β))|. The conjecture is that it equals the
    categorical mass m(ϱ_β). This definition does not prove that; it names
    the trace side. The theorems below are statements about this quantity.

    The heuristic argument for the conjecture:
    1. The fibre functor τ is exact and monoidal
    2. τ sends the categorical trace to the Markov trace (Jones)
    3. τ sends the mass integrand to the Hecke mass element (Schur–Weyl)
    4. The norm over ℝ is the absolute value (step 4 of the sketch
       `rem:hecke-mass-trace-sketch`; asserted, not proved) -/
-- Ref: [leitner2026] §4/hecke-mass-trace
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
noncomputable def categoricalMassFromMarkov (d : MarkovMassData) : ℝ :=
  |d.markovTrace|

/-- The mass decomposes via the triangle inequality. -/
-- Ref: [leitner2026] §4/hecke-mass-trace
theorem mass_markov_upper_bound (d : MarkovMassData) :
    categoricalMassFromMarkov d ≤
    |d.descendedTrace| + |d.transientTrace| := by
  unfold categoricalMassFromMarkov
  rw [d.trace_decomposition]
  exact abs_add_le d.descendedTrace d.transientTrace

/-- Exact decomposition when both trace components are non-negative
    (as guaranteed in the archimedean realisation, where trace values
    are norms of holonomies and quantum dilogarithms). -/
-- Ref: [leitner2026] §4/hecke-mass-trace
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem mass_markov_exact (d : MarkovMassData)
    (h_desc : 0 ≤ d.descendedTrace)
    (h_trans : 0 ≤ d.transientTrace) :
    categoricalMassFromMarkov d =
    |d.descendedTrace| + |d.transientTrace| := by
  unfold categoricalMassFromMarkov
  rw [d.trace_decomposition,
      abs_of_nonneg (add_nonneg h_desc h_trans),
      abs_of_nonneg h_desc,
      abs_of_nonneg h_trans]

/-- Compatibility with the archimedean mass formula:
    |tr_M(Φ_mass)| = Vol(K) / ℏ_q² when the Markov trace evaluates
    to the hyperbolic volume divided by the quantum Planck constant
    squared.

    This is the Kashaev/dilogarithm bridge: it explicitly applies
    the fibre functor τ and so lives strictly in the Archimedean
    tier (`conj:phi-q-tower-jsj-bridge`). -/
-- Ref: [leitner2026] §4/hecke-mass-trace
theorem mass_markov_archimedean
    (d : MarkovMassData)
    (vol : ℝ) (hvol : 0 < vol)
    (ℏ : ℝ) (hℏ : 0 < ℏ)
    (h_eval : d.markovTrace = vol / ℏ ^ 2) :
    categoricalMassFromMarkov d = vol / ℏ ^ 2 := by
  unfold categoricalMassFromMarkov
  rw [h_eval, abs_of_pos (div_pos hvol (pow_pos hℏ 2))]

end Arch

end QOU.Braiding
