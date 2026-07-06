import { proposition } from "../../schema/builders";

/**
 * Per-new-nucleon additive linearity of the atomic Markov-trace
 * denominator shift exponent: shift(Z+1, N) - shift(Z, N) = 18,
 * shift(Z, N+1) - shift(Z, N) = 21, fixing shift = 18Z + 21N + 1
 * for A >= 2 in the canonical pppnnn ordering.
 *
 * Verified at A = 2..6 (D, T, ³He, ⁴He, ⁵Li, ⁶Li) via the
 * markov_peel symbolic pipeline. Witness:
 *   computations/per-nucleon-shift-derivation.witness.json
 *
 * Closes the residual research question on
 * `claude/w3-w4-followups` (the per-nucleon coefficient origin),
 * by replacing the conjectured "factor-of-3 from triple-cover of
 * seminormal hook denominators" with a clean per-new-nucleon
 * inductive derivation.
 *
 * Generator decomposition: each new nucleon adds 12 generators
 * (11 nucleon + 1 interface), DP-max increment 12, with
 * cancellation 3 (proton) or 1.5 (neutron) yielding shift 18 or 21.
 *
 * Use cases: closed-form D(u) prediction for ⁷Li, ⁸Be, ¹²C, etc.
 * without Hecke NF computation.
 */
export default proposition({
  label: "prop:per-nucleon-shift-additive-linearity",
  lean: { ref: "qou:QOU.BraidKnot.per_nucleon_shift_additive_linearity", validation: "not_checked" },
  title:
    "Per-new-nucleon additive linearity: $\\mathrm{shift}(Z, N) = 18Z + 21N + 1$ on canonical pppnnn ordering",
  uses: [],
  computation: {
    engine: "python",
    script: "computations/per_nucleon_shift_derivation.py",
    witness: "computations/per-nucleon-shift-derivation.witness.json",
    status: "verified",
    requires: ["numpy"],
  },
  tags: [
    "atomic-markov-trace",
    "shift-exponent",
    "per-nucleon-decomposition",
    "additive-linearity",
    "canonical-pppnnn-ordering",
    "d-u-closed-form",
    "isotope-prediction",
  ],
});
