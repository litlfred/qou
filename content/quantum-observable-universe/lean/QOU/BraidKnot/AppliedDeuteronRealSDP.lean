import QOU.MathlibExt.SDP
import QOU.MathlibExt.SDPRealUniqueness
import QOU.BraidKnot.AppliedDeuteronUniqueness

/-!
# QOU.BraidKnot.AppliedDeuteronRealSDP — ²H real per-nucleus SDP (Phase D)

Phase D of the [#1575] real-SDP workplan: replace the abstract
empty-constraint SDP (`deuteron_emptySDP`, cost = identity, no
constraints) with the **real** deuteron SDP whose cost and constraints
come from the mass-formula assembly.

The numeric assembly + dual certificate live in
`computations/deuteron_real_sdp.py` →
`deuteron-real-sdp.witness.json` (Phase A cost, Phase B branching
constraints, Phase C strong-duality solve).  This file is the Lean
**type-level** wiring: it states the real SDP as an `SDPPrimal` over the
11 Wedderburn blocks `λ ⊢ 6`, and derives uniqueness from the generic
ℝ-uniqueness bridge `real_strict_complementarity_unique_of_dualSlack_posDef`
**conditional on** the dual-slack PosDef certificate the SDP solve emits.

## Status

This is a **scaffold**.  The cost vector and the dual-slack PosDef
certificate are abstracted as hypotheses (`RealSDPCertificate`), matching
the §3b-cond conditional-class pattern: the Lean statement is fully
verified modulo the single class instance that the numeric witness
supplies.  Discharging the instance from the witness JSON (the
clarabel/cvxpy dual) is the final wiring step, tracked as a follow-up.

## References

- `QOU.BraidKnot.NucleusEmptySDPUniqueness` (the abstract layer this
  replaces for ²H)
- `QOU.MathlibExt.SDPRealUniqueness.real_strict_complementarity_unique_of_dualSlack_posDef`
- `deuteron-real-sdp.witness.json` (numeric cost + dual certificate)
- PR #1582 (Phase A/B/C compute)
-/

namespace QOU.BraidKnot

open Matrix

/-- Number of Wedderburn blocks for ²H at `H_6` — the partitions
    `λ ⊢ 6`.  `heckeDim 6` is the full algebra dimension; the real SDP
    is block-diagonal, so the *effective* variable count is the number
    of central idempotents `p(6) = 11`.  We work at the block level. -/
abbrev deuteronBlockCount : ℕ := 11

/-- **Real deuteron SDP certificate** (§3b-cond conditional class).

    Bundles the data the numeric solve
    (`deuteron_real_sdp.py` → `deuteron-real-sdp.witness.json`) produces
    that Lean cannot yet recompute internally:

    * `sdp`     — the real per-nucleus SDP (non-identity cost from the
                  mass formula, branching constraints), at the block
                  dimension `m`.
    * `rs`      — a real strong-duality pair (primal optimum `Φ⋆`, dual
                  `y⋆`) certified by the clarabel/cvxpy solve.
    * `dualSlack_posDef` — the dual slack `S(y⋆) = T − Σ yᵢ⋆ Aᵢ` is
                  positive-definite (strong-duality / strict-
                  complementarity certificate; the bounded positive-norm
                  subspace solve in #1582 supplies this).

    A term of this class is exactly the witness's strong-duality
    certificate.  Everything downstream is proved from it. -/
structure RealSDPCertificate (m : ℕ) where
  /-- The real per-nucleus SDP at block dimension `m`. -/
  sdp : SDPPrimal m ℝ (Fin 3)
  /-- The certified real strong-duality pair. -/
  rs : RealStrongDualityPair sdp
  /-- The dual slack is PosDef (the solve's certificate). -/
  dualSlack_posDef : (sdp.dualSlack rs.ystar).PosDef

/-- **²H real-SDP uniqueness, conditional on the solve certificate.**

    Given the real deuteron SDP certificate, the primal optimum is the
    unique feasible matrix achieving the optimal objective.  Fully
    verified by Lean modulo the single `RealSDPCertificate` instance
    (which the numeric dual supplies) — the §3b-cond rigorous-
    conditional pattern. -/
theorem deuteron_realSDP_uniqueness
    {m : ℕ} (cert : RealSDPCertificate m)
    {Φ' : Matrix (Fin m) (Fin m) ℝ}
    (h_feas : cert.sdp.IsFeasible Φ')
    (h_obj : cert.sdp.objAt Φ' = cert.sdp.objAt cert.rs.Φstar) :
    Φ' = cert.rs.Φstar :=
  real_strict_complementarity_unique_of_dualSlack_posDef
    cert.rs cert.dualSlack_posDef h_feas h_obj

/-- **²H real-SDP optimum is a Subsingleton** among objective-optimal
    feasible matrices — the uniqueness statement in `Subsingleton`
    form, matching `deuteron_uniqueness_via_empty_sdp` but for the real
    SDP. -/
theorem deuteron_realSDP_subsingleton
    {m : ℕ} (cert : RealSDPCertificate m) :
    Subsingleton {Φ : Matrix (Fin m) (Fin m) ℝ //
      cert.sdp.IsFeasible Φ ∧
      cert.sdp.objAt Φ = cert.sdp.objAt cert.rs.Φstar} := by
  refine ⟨fun a b => ?_⟩
  apply Subtype.ext
  rw [deuteron_realSDP_uniqueness cert a.2.1 a.2.2,
      deuteron_realSDP_uniqueness cert b.2.1 b.2.2]

end QOU.BraidKnot
