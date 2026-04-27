import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:periodic-table-demand",
  title:
    "The valley of stability is the demand-minimizing locus in $(Z, N)$-space",
  tags: [
    "periodic-table",
    "valley-of-stability",
    "demand",
    "magic-numbers",
    "conjecture",
    "nuclear-physics",
  ],
  uses: ["prop:demand-stability"],
});
