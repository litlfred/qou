import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-characteristic-classes",
  title: "Quantum Characteristic Classes (Yekutieli obstruction)",
  tags: ["yekutieli", "obstruction", "cohomology", "brane-tower"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:yekutieli-lifting-condition",
    "prop:jet-prolongation",
    "prop:yekutieli-lifting",
  ],
});
