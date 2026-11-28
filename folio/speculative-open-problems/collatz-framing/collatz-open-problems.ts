import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-open-problems",
  title: "Open problems for the Laurent map $\\mathcal{C}_q$",
  interprets: "conj:q-collatz",
  uses: [
    "conj:q-collatz",
    "rem:collatz-three-forms",
    "quantum-observable-universe:prop:q-syracuse-lift",
    "quantum-observable-universe:prop:laurent-bounded-window",
    "quantum-observable-universe:prop:balanced-holonomy-exclusion",
  ],
  tags: ["collatz", "open-problem", "mod-2-reduction", "lifting"],
  cites: ["hicksmullenyucaszavislak2008", "lagarias2010"],
});
