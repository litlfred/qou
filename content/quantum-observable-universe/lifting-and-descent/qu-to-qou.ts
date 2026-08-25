import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qu-to-qou",
  lean: { ref: "qou:QOU.Torsion.YekutieliTriple.qu_to_qou", validation: "not_checked" },
  title: "Quantum universe with observability and categorical lifting is a QOU",
  tags: ["main-theorem", "qou", "yekutieli", "descent"],
  examples: ["ex:qu-to-qou-su2"],
  uses: [
    "prop:yekutieli-lifting",
    "prop:fiber-adjoint-involution",
  ],
  proofs: ["prf:qu-to-qou"],
});
