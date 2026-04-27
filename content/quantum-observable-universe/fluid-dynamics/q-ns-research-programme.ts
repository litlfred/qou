import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:q-ns-wellposedness",
  label: "rem:q-ns-research-programme",
  title: "The quantum Navier--Stokes programme: from categorical regularity to the Clay problem",
  uses: [
    "conj:regularity-breakdown",
    "rem:berry-vortex-moduli",
    "rem:vortex-reconnection",
    "prop:acoustic-horizon-conditions",
  ],
  tags: [
    "research-programme",
    "millennium-problem",
    "navier-stokes",
    "regularity",
    "open-problems",
  ],
});
