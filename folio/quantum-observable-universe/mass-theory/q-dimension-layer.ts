import { definition } from "../../schema/builders";

/**
 * The q-dimension layer R^|Par(n)|: the per-irrep target structure of
 * the δ_q decoration (def:delta-q-decoration). One coordinate per
 * partition λ ⊢ n, recording the per-irrep q-character that the Markov
 * trace collapses by summing. Split out of def:delta-q-decoration (one
 * definiendum per block).
 */
export default definition({
  label: "def:q-dimension-layer",
  title:
    "$q$-dimension layer $R^{|\\mathrm{Par}(n)|}$: per-irrep target of the $\\delta_q$-decoration",
  defines: ["q-dimension-layer"],
  uses: ["def:delta-q-decoration"],
  lean: { ref: "qou:QOU.BraidKnot.qDimensionLayer" },
  tags: [
    "delta-q",
    "q-dimension",
    "wedderburn-decomposition",
    "hecke-algebra",
    "infrastructure",
  ],
});
