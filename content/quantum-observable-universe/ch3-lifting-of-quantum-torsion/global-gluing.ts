import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:global-gluing",
  title: "Global gluing via Yekutieli's twisted quantization",
  hasProof: true,
  tags: ["yekutieli", "twisted-quantization", "global-gluing"],
  uses: [
    "def:quantum-observable-universe",
    "def:direct-limit-algebra",
    "def:quantum-planck-constant",
    "def:quantum-characteristic-classes",
    "prop:vacuum-state",
  ],
});
