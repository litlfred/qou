import { definition } from "../../schema/builders";

export default definition({
  label: "def:lp-stable",
  lean: { ref: "qou:QOU.ParticleInteractions.LPStable", validation: "not_checked" },
  title: "LP-stable element of $H_3(q)$",
  tags: [
    "lp-stability",
    "gram-matrix",
    "confinement",
    "hecke-algebra",
  ],
  uses: [],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
