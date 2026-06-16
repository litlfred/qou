import { proposition } from "../../schema/builders";

/**
 * The refined Sub-lemma 2.1 from
 * `docs/audits/2026-05-04-confinement-nf-structure-forcing-proof.md`:
 * trace decomposition of β_1 · I · β_2 ∈ H_n(q) under the Wenzl 1988
 * branching V_λ ↓ ⊕ c^λ_{μν} V_μ ⊗ V_ν.
 *
 * The interface block A^λ_{μν}(I) ∈ End(V_μ ⊗ V_ν)^⊕c is generally
 * an operator-valued endomorphism (not a scalar α_shift) — this is
 * the key correction to the original scalar Sub-lemma 2.1 statement.
 *
 * Numerically verified to ~1e-15 for all 11 partitions λ ⊢ 6 in the
 * deuteron case (sublemma-2-1-A-operator-extract.witness.json).
 *
 * Categorical proof in 2026-05-04-sublemma-2-1-categorical-proof.md
 * uses Wenzl 1988 (Hecke branching) and Hoefsmit 1974 (seminormal
 * matrix elements) as standard ingredients.
 */
export default proposition({
  label: "prop:hecke-branching-trace-decomposition",
  title:
    "Trace decomposition $\\chi^\\lambda(\\beta_1 \\cdot I \\cdot \\beta_2) = \\sum c^\\lambda_{\\mu\\nu} \\operatorname{Tr}(A^\\lambda_{\\mu\\nu}(I) \\cdot \\rho_\\mu(\\beta_1) \\otimes \\rho_\\nu(\\beta_2))$ under Hecke branching",
  uses: [
    "prop:alpha-shift-torus-knot",
  ],
  cites: ["wenzl1988", "hoefsmit1974"],
  computation: {
    engine: "numpy",
    script: "computations/sublemma_2_1_A_operator_extract.py",
    witness: [
      "computations/sublemma-2-1-A-operator-extract.witness.json",
      "computations/sublemma-2-1-deuteron-branching.witness.json",
    ],
    status: "verified",
    requires: ["numpy", "sympy"],
  },
  lean: {
    ref: "qou:QOU.BraidKnot.heckeBranchingTraceDecomp",
    validation: "not_checked",
  },
  tags: [
    "hecke-algebra",
    "branching",
    "littlewood-richardson",
    "seminormal-basis",
    "trace-decomposition",
    "operator-valued",
    "wenzl-1988",
    "hoefsmit-1974",
  ],
});
