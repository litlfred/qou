import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:global-gluing",
  lean: { ref: "qou:QOU.Torsion.global_gluing",
    validation: "not_checked",
  },
  title: "Global gluing via twisted quantization",
  tags: ["yekutieli", "twisted-quantization", "global-gluing"],
  uses: [
    "def:quantum-planck-constant",
    "def:quantum-characteristic-classes",
    "prop:vacuum-state",
  ],
  proofs: ["prf:global-gluing"],
});
