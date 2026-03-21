import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qu-to-qou",
  title: "Quantum universe with observability and Yekutieli is a QOU",
  hasProof: true,
  tags: ["main-theorem", "qou", "yekutieli", "descent"],
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
});
