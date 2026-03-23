import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qu-to-qou",
  lean: { decl: "QOU.QuToQou" },
  status: "stated",
  title: "Quantum universe with observability and Yekutieli is a QOU",
  tags: ["main-theorem", "qou", "yekutieli", "descent"],
  examples: ["ex:qu-to-qou-su2"],
  uses: [
    "def:quantum-universe",
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:yekutieli-lifting-condition",
    "def:quantum-characteristic-classes",
    "def:projective-line-object",
    "prop:jet-prolongation",
    "prop:yekutieli-lifting",
    "prop:fiber-adjoint-involution",
  ],
  proofs: ["prf:qu-to-qou"],
});
