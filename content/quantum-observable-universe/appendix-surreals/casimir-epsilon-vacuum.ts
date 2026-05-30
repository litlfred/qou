import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:casimir-epsilon-vacuum",
  title:
    "Casimir force as $\\mathrm{st}$-image of $\\varepsilon$-vacuum density gradient",
  lean: {
    ref: "qou:QOU.AppendixSurreals.CasimirEpsilonVacuum",
    validation: "stub",
  },
  uses: [
    "prop:vacuum-epsilon",
    "prop:archimedean-stpart",
    "def:standard-part-functor",
  ],
  cites: [
    "casimir1948",
    "mohideen-roy1998",
    "lamoreaux1997",
    "robinson1966",
  ],
  tags: [
    "surreal-numbers",
    "vacuum",
    "casimir-effect",
    "unknot",
    "regularisation",
    "infinitesimal",
    "boundary-condition",
    "conditional-on-class",
    "open-problem",
  ],
});
