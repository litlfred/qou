/-
  Per-knot trace-convention gate (GAP-A-4 formalize-first invariants I-1, I-6).

  Companion to
    computations/probes/i6_trace_convention_pin.py
    computations/i6-trace-convention-pin.witness.json
    docs/scope/2026-07-02-gap-a4-perknot-density-rule-scoping.md  §I-1, §I-6

  Context.  Deriving the per-knot density ρ(K) requires first pinning WHICH
  Markov-trace object is canonical: the corpus carries two at q₀ for the same
  𝓑₃ proton family —
    (A) F_Bor's UNNORMALISED Borromean braid trace × [3]_q!/q³ framing
        ⇒ |tr_M(β_Bor)| ≈ 0.998562  (absolute-mass facade, canonical_mass.py),
    (B) the dim-λ-NORMALISED chi-cache tr_M(K) = Σ_λ y_λ χ^λ/dim λ
        ⇒ tr_M(p) ≈ 1.0653, tr_M(n) ≈ 0.9232  (per-knot density / binding).
  They differ by the explicit factor R_p ≈ 1.0668 (compute-checked in the
  witness above). This file formalises the two gate invariants those numbers
  underwrite.

  * I-1 (`no_uniform_scalar_density`) — a scope-(b) STRUCTURAL EXCLUSION.
    The round-trip density is near p/n-degenerate (ρ_p/ρ_n ≤ 1.001) while the
    chi-cache trace is ≥ 1.15 asymmetric, so NO single knot-independent scalar
    `f` with ρ = f·tr_M reproduces both — the whole uniform-scalar density
    family is foreclosed before any numerical scan. (Cited invariant for the
    §"refuted / ruled out" (b)-scope: a proved arithmetic impossibility.)

  * I-6 (`traceConventions_distinct_of_factor_ne_one`,
    `traceConvention_factor_determined`) — the two conventions are genuinely
    DISTINCT (factor ≠ 1), and once the canonical convention is fixed the
    relating factor R is UNIQUELY DETERMINED, i.e. the "convention freedom"
    the q-dim route probe flagged (span 0.41→5.62) is not a free DOF.

  Base ring (§7c): generic `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`
  — purely algebraic/ordered content, no archimedean construct, no q₀.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith

namespace QOU.MassTheory

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **I-1 — no uniform scalar per-knot density.**
If the proton/neutron chi-cache traces are ≥ 1.15 asymmetric
(`trp ≥ (115/100)·trn`) while the round-trip densities are ≤ 1.001
near-degenerate (`rp ≤ (1001/1000)·rn`), then there is NO knot-independent
scalar `f` with `ρ = f · tr_M` for both nucleons. Scope-(b) exclusion of the
uniform-scalar density family (the cited invariant is this impossibility). -/
theorem no_uniform_scalar_density
    (trp trn rp rn f : R) (htn : 0 < trn) (hrn : 0 < rn)
    (hasym : (115 : R) / 100 * trn ≤ trp)
    (hdeg : rp ≤ (1001 : R) / 1000 * rn)
    (hp : rp = f * trp) (hn : rn = f * trn) : False := by
  -- f must be positive: ρ_n = f·tr_n > 0 with tr_n > 0.
  have hf : 0 < f := by
    rcases lt_trichotomy f 0 with h | h | h
    · have hneg : f * trn < 0 := mul_neg_of_neg_of_pos h htn
      rw [← hn] at hneg; linarith
    · rw [h, zero_mul] at hn; linarith
    · exact h
  -- ρ_p = f·tr_p ≥ f·(1.15·tr_n) = 1.15·ρ_n.
  have key : (115 : R) / 100 * rn ≤ rp := by
    have hmul := mul_le_mul_of_nonneg_left hasym hf.le
    rw [hp, hn]; nlinarith [hmul]
  -- 1.15·ρ_n ≤ ρ_p ≤ 1.001·ρ_n with ρ_n > 0 is impossible.
  nlinarith [key, hdeg, hrn]

/-- **I-6 (distinctness).** If the chi-cache trace relates to the F_Bor braid
trace by `trChiCache = c · trFbor` with `trFbor > 0` and `c ≠ 1`, the two
conventions give genuinely different numbers. (Compute: `c = R_p ≈ 1.0668`.) -/
theorem traceConventions_distinct_of_factor_ne_one
    (trChiCache trFbor c : R) (hFbor : 0 < trFbor)
    (hrel : trChiCache = c * trFbor) (hc : c ≠ 1) :
    trChiCache ≠ trFbor := by
  rw [hrel]
  intro h
  exact hc (mul_right_cancel₀ (ne_of_gt hFbor) (h.trans (one_mul trFbor).symm))

/-- **I-6 (uniqueness / no hidden DOF).** Once the canonical convention is
fixed (`trFbor ≠ 0`), the relating factor is uniquely determined
`c = trChiCache / trFbor` — the convention freedom is not a free parameter. -/
theorem traceConvention_factor_determined
    (trChiCache trFbor c : R) (hFbor : trFbor ≠ 0)
    (hrel : trChiCache = c * trFbor) : c = trChiCache / trFbor := by
  rw [hrel, mul_div_assoc, div_self hFbor, mul_one]

end QOU.MassTheory
