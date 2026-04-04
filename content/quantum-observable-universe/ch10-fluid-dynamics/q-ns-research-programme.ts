import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:q-ns-wellposedness",
  label: "rem:q-ns-research-programme",
  title: "The quantum Navier--Stokes programme: from categorical regularity to the Clay problem",
  uses: [
    "thm:q-ns-wellposedness",
    "conj:regularity-breakdown",
    "def:q-navier-stokes",
    "def:quantum-observable-universe",
    "rem:planck-reynolds",
    "prop:q-turbulence-spectrum",
    "rem:hamilton-jacobi-phase",
    "rem:berry-vortex-moduli",
    "prop:helicity-conservation",
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
