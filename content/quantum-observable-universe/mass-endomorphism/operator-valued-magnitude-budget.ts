import { remark } from "../../schema/builders";

/**
 * Quantitative interpretation of prop:hecke-branching-trace-decomposition:
 * how much of the trace structure is operator-valued vs scalar?
 *
 * Probe probe_operator_valued_ansatze_from_mass_endo.py reads the
 * H_6 deuteron-interface A^λ_{μν}(I) extracts from the witness
 * sublemma-2-1-A-operator-extract.witness.json and for each of the
 * 35 (λ,μ,ν) blocks computes the orthogonal decomposition
 *
 *   A^λ_{μν}(I) = A_scalar + Δ_op
 *
 * where A_scalar = tr(A)/(d_μ d_ν) · 𝟙 is the best scalar
 * approximation and Δ_op is the operator-valued residual. By
 * Pythagoras, ‖Δ_op‖_F² = ‖A‖_F² − |tr A|²/(d_μ d_ν).
 *
 * Aggregate (across all 35 blocks):
 *   scalar-approximation Frobenius : 3.517
 *   operator-valued correction      : 3.603  (> scalar)
 *   ratio op/sqrt(scalar^2+op^2)    : 0.72
 *   non-scalar blocks               : 19 / 35
 *
 * The operator-valued correction Frobenius EXCEEDS the scalar
 * approximation. Symmetric scalar substrate ansatze capture less
 * than half the structural magnitude — quantitative justification
 * for the 4-negatives convergence onto operator-valued / Z↔N-
 * asymmetric corrections (PR #671 structural-diagnosis audit).
 */
export default remark({
  label: "rem:operator-valued-magnitude-budget",
  title:
    "Magnitude budget: operator-valued vs scalar approximation of $A^\\lambda_{\\mu\\nu}(I)$",
  interprets: "prop:hecke-branching-trace-decomposition",
  uses: [
    "prop:hecke-branching-trace-decomposition",
  ],
  computation: {
    engine: "python",
    script:
      "computations/probe_operator_valued_ansatze_from_mass_endo.py",
    witness: [
      "computations/operator-valued-ansatze-from-mass-endo.witness.json",
    ],
    status: "verified",
    requires: ["python"],
  },
  tags: [
    "operator-valued",
    "wedderburn-blocks",
    "frobenius-decomposition",
    "structural-magnitude-budget",
    "empirical-finding",
  ],
});
