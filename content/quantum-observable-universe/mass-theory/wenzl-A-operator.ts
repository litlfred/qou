import { definition } from "../../schema/builders";

/**
 * Wenzl A-operator A^λ_{μν}(I) — the (μ, ν)-block of an inter-block
 * interface generator in the Wenzl 1988 LR decomposition.
 *
 * Operator data named by Sub-lemma 2.1: for λ ⊢ n = n₁ + n₂ and
 * I = σ_{n₁} ∈ H_n(q),
 *   A^λ_{μν}(I) ∈ End(V_μ ⊗ V_ν)^{⊕ c^λ_{μν}}
 * with c^λ_{μν} the Littlewood–Richardson coefficient
 * (prop:lr-coefficient-hecke). Consumed by
 * prop:crystal-r-matrix-sub-lemma (pole order at q → 0) and
 * prop:operator-valued-combiner-convergence (per-peel accumulation).
 *
 * Numerical realisation: the bilinear-system extract
 * A_operator_extract_at_level.py and its
 * A-operator-extract-h{n}-{iface}.witness.json witnesses.
 */
export default definition({
  label: "def:wenzl-A-operator",
  title:
    "Wenzl A-operator $A^\\lambda_{\\mu\\nu}(I)$: the $(\\mu, \\nu)$-block of an interface generator",
  chapter: "mass-theory",
  uses: ["prop:lr-coefficient-hecke"],
  cites: ["wenzl1988", "hoefsmit1974"],
  defines: [],
  lean: {
    ref: "qou:QOU.BraidKnot.WenzlAOperator",
    validation: "stub",
  },
  computation: {
    engine: "python",
    script:
      "computations/a_operator/A_operator_extract_at_level.py",
    witness: [
      "computations/A-operator-extract-h9-pn.witness.json",
    ],
    status: "verified",
    requires: [],
  },
  tags: [
    "wenzl-a-operator",
    "operator-valued",
    "hecke-branching",
    "littlewood-richardson",
    "sub-lemma-2-1",
    "section-3b-cond",
  ],
});
