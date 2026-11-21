import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:vacuum-epsilon",
  title:
    "Infinitesimal vacuum: $\\mathrm{Geom}(\\bigcirc) = \\varepsilon$",
  lean: { ref: "qou:QOU.AppendixSurreals.VacuumEpsilon", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "vacuum",
    "unknot",
    "regularisation",
    "infinitesimal",
    "open-problem",
  ],
  uses: ["conj:archimedean-stpart"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The Casimir force ([Casimir force](#conj:casimir-epsilon-vacuum)) is the $\\mathrm{st}$-image of the plate-constrained unknot-count gradient times $\\varepsilon$." },
  ],
  cites: ["robinson1966"],
});
