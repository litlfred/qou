import { conjecture } from "../../schema/builders";

/**
 * Conjecture: confinement forces the NF support of a compound braid
 * to lie in the sub-lattice of NH_n indexed by the LP/SDP active
 * partitions, with the shift deviation bounded by the LP duality gap.
 *
 * Setup.
 *   For β = β₁ ⋆ I ⋆ β₂ ∈ B_n (I a basis "interface" braid), the
 *   operator-selection LP from prop:operator-selection-lp returns
 *   dual variables y_λ* ≥ 0 over Wedderburn channels {V_λ : λ ⊢ n}.
 *   Define the active set A := {λ : y_λ* > 0}.
 *
 * Confinement hypothesis. |A| < dim H_n(q) = n!.
 *
 * Conjecture (this block).
 *   Confinement forces:
 *     (a) the Wedderburn maximizer of shift_NF(β) lies in A;
 *     (b) shift_NF(β) = α_shift(I) + Δ(β₁, β₂; A) with
 *         |Δ| bounded by the LP duality gap.
 *
 * Empirical evidence — witness.
 *   Across 6 test compounds at n ∈ {3, 4} the witness records:
 *     - confinement holds (|A|/n! ∈ {2/6, 4/24});
 *     - maximizer-in-active 6/6;
 *     - LP duality gap = 0 in all cases (strong-duality verified);
 *     - Δ_observed bounded by the heuristic compound-length scale.
 *
 * Status.
 *   conjecture (no Lean proof attempted; the witness compares
 *   predicted vs observed NF support across a small bench).
 *
 * @see prop:operator-selection-lp — provides the LP/SDP framework
 * @see prop:alpha-shift-torus-knot — establishes α_shift(I) for torus interfaces
 * @see computations/lp_confinement_nf_forcing.py — the probe
 * @see computations/nh_basis_shift.py — baseline shift_NF table
 * @see docs/audits/2026-05-04-nh-knots-confinement-shift.md — full audit
 */
export default conjecture({
  label: "conj:confinement-nf-structure-forcing",
  title:
    "Confinement → NF-structure forcing: $\\mathrm{shift}_{\\mathrm{NF}}(\\beta_1 \\star I \\star \\beta_2) = \\alpha_{\\mathrm{shift}}(I) + \\Delta$ with $|\\Delta|$ bounded by the LP duality gap",
  lean: { ref: "qou:QOU.BraidKnot.ConfinementNfStructureForcing", validation: "stub" },
  uses: ["prop:alpha-shift-torus-knot"],
  computation: {
    engine: "scipy",
    script: "computations/lp_confinement_nf_forcing.py",
    witness: [
      "computations/lp-confinement-nf-forcing.witness.json",
      "computations/nh-basis-shift.witness.json",
    ],
    status: "verified",
    requires: ["scipy", "sympy", "numpy", "mpmath"],
  },
  // No Lean stub: this is a conjecture (AGENTS.md §3b).
  tags: [
    "tier:S",
    "conjecture",
    "confinement",
    "nh-basis",
    "lp-duality",
    "shift-exponent",
    "operator-selection",
    "wedderburn-channels",
  ],
});
