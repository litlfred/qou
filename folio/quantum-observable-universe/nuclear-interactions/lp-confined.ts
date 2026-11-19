import { definition } from "../../schema/builders";

export default definition({
  label: "def:lp-confined",
  lean: { ref: "qou:QOU.ParticleInteractions.LPConfined", validation: "not_checked" },
  title: "LP-confined element of $H_3(q)$",
  tags: [
    "lp-stability",
    "confinement",
    "sub-braid",
    "hecke-algebra",
  ],
  uses: ["def:lp-stable"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
