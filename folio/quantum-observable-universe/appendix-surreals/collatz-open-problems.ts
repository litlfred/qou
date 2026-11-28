import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-open-problems",
  title: "Open problems for the $q$-Collatz map",
  interprets: "conj:q-collatz",
  uses: ["prop:collatz-syracuse-lift", "prop:collatz-bounded-window", "prop:collatz-no-cycles"],
  tags: ["collatz", "open-problem", "mod-2-reduction", "lifting"],
  cites: ["hicksmullenyucaszavislak2008", "lagarias2010"],
});
