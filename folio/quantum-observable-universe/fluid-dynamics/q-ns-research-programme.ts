import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:q-ns-wellposedness",
  label: "rem:q-ns-research-programme",
  title: "Open problems in the $q$-deformed Navier--Stokes programme",
  uses: [
    "rem:berry-vortex-moduli",
    "rem:vortex-reconnection",
    "prop:acoustic-horizon-conditions",
    "conj:regularity-breakdown",
    "conj:levi-degeneracy",
  ],
  tags: [
    "research-programme",
    "navier-stokes",
    "regularity",
    "open-problems",
  ],
});
