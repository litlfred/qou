import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:vacuum-epsilon",
  title:
    "Infinitesimal vacuum: $\\mathrm{Geom}(\\unicode{9737}) = \\varepsilon$",
  lean: { ref: "qou:QOU.AppendixSurreals.VacuumEpsilon", validation: "stub" },
  tags: [
    "surreal-numbers",
    "vacuum",
    "unknot",
    "regularisation",
    "infinitesimal",
    "open-problem",
  ],
  uses: ["conj:archimedean-stpart"],
  cites: ["robinson1966"],
});
