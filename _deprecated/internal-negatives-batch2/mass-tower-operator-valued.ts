import { proposition } from "../../schema/builders";

/**
 * The Stage-1 unblock of the SUPERSEDED `prop:mass-endomorphism-tower`.
 *
 * The original scalar Wedderburn-volume tower
 *   𝔪 = |∏ V̂_i| + Σ F(|V̂_i|) + z² Σ F(|V̂_i V̂_j|)
 * was structurally wrong because it is braid-class-independent at the
 * ρ_q = 1/ℏ_q² ansatz level, while ρ_K^CODATA varies ~30× across atoms
 * (rho-k-graded-expansion).
 *
 * The replacement is the operator-valued form using
 * A^λ_{μ_1,...,μ_{Z+N}}(I) ∈ End(⊗ V_{μ_i}) from the iterated Hecke
 * branching trace decomposition (Wenzl 1988 + Hoefsmit 1974). The
 * dimensional mass scale lives in the off-diagonal Hoefsmit matrix
 * entries √(1 - h_q(d_T)²) of A^λ_{vec μ}(I), NOT in the scalar
 * volumes V̂_i.
 *
 * Connects to:
 * - prop:hecke-branching-trace-decomposition (the two-factor case, proved)
 * - prop:lr-tensor-character-bridge (I = 1 specialisation)
 * - prop:rho-k-graded-expansion (the scalar limit's open pair-gen piece
 *   is identified as the operator's off-diagonal residual)
 * - prop:li2q-phiq-bar-symmetrization (resolves the Φ_q vs Li_2^q
 *   context-split by carrying dim mass scale in the operator instead)
 *
 * Status: boxed identity PROVED at two-factor level
 * (sublemma-2-1-A-operator-extract.witness.json, 10^-15 across all
 * 11 partitions of λ ⊢ 6); bridge claim to the mass tower
 * (prediction of m_p/m_e ≈ 1836) is CONDITIONAL on the iterated
 * A^λ_{vec μ}(I) being computable for Z+N ≥ 3 and the off-diagonal
 * residual closing the pair-gen open piece.
 */
export default proposition({
  label: "prop:mass-tower-operator-valued",
  title:
    "Operator-valued mass-endomorphism tower via iterated $A^\\lambda_{\\vec\\mu}(I)$",
  uses: [
    "prop:hecke-branching-trace-decomposition",
    "prop:rho-k-graded-expansion",
    "prop:li2q-phiq-bar-symmetrization",
    "prop:bar-symmetric-three-layer-synthesis",
    "def:canonical-braid-interface-composition",
    "prop:plancherel-term-7-formulation",
  ],
  cites: ["wenzl1988", "hoefsmit1974"],
  computation: {
    engine: "python",
    script: "computations/mass_tower_operator_valued.py",
    witness: [
      "computations/mass-tower-operator-valued.witness.json",
      "computations/sublemma-2-1-h9-tritium-branching-verify.witness.json",
    ],
    status: "verified",
    requires: ["mpmath", "numpy"],
  },
  lean: {
    ref: "qou:QOU.BraidKnot.massTowerOperatorValued",
    validation: "not_checked",
  },
  tags: [
    "mass-endomorphism",
    "operator-valued",
    "wedderburn",
    "hecke-branching",
    "littlewood-richardson",
    "stage-1-unblock",
    "wenzl-1988",
    "hoefsmit-1974",
    "conditional-class",
  ],
});
