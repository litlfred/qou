import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:blowup-yekutieli",
  title:
    "Blowup mechanism as Yekutieli lifting obstruction in the brane tower",
  uses: [
    "conj:regularity-breakdown",
    "prop:descent-condition",
    "def:local-cohomology-group",
    "rem:vortex-reconnection",
  ],
  tags: [
    "blowup",
    "yekutieli",
    "obstruction",
    "cohomology",
    "brane-tower",
    "gerbe",
    "millennium-problem",
  ],
});
