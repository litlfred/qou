import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vacuum-epsilon",
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
  uses: ["prop:archimedean-stpart"],
  cites: ["robinson1966"],
});
