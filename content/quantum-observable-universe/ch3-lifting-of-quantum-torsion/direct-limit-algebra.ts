import { definition } from "../../schema/builders";

export default definition({
  label: "def:direct-limit-algebra",
  lean: { decl: "QOU.DirectLimitAlgebra" },
  title: "Quantum Observable Universe as Direct Limit",
  tags: ["direct-limit", "algebra", "brane-tower"],
  uses: [
    "def:recursive-brane-tower",
    "ex:c-quantum-observable-universe",
  ],
  examples: ["rem:jet-shell"],
});
