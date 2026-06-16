import { definition } from "../../schema/builders";

/**
 * Generic embeddable knot operator with geometric overlap weighting —
 * the categorical expression of σ > π bond strength, reusable downstream.
 */
export default definition({
  label: "def:embeddable-knot-operator",
  lean: {
    ref: "qou:QOU.Molecular.EmbeddableKnotOperator",
    validation: "not_checked",
  },
  title: "Embeddable knot operator with geometric overlap weight",
  computation: {
    engine: "python",
    script: "computations/embeddable_knot_operator.py",
    witness: [
      "computations/embeddable-knot-operator.witness.json",
    ],
    status: "verified",
  },
  uses: ["def:covalent-bond-types"],
  tags: ["knot-operator", "embedding", "overlap-weight", "sigma-pi", "reusable"],
});
