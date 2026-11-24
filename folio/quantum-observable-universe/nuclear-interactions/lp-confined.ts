import { definition } from "../../schema/builders";

export default definition({
  label: "def:lp-confined",
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation (moved from the definition prose 2026-11-19): What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Any generic categorical identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here." },
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.LPConfined", validation: "not_checked" },
  title: "LP-confined element of $H_3(q)$",
  tags: [
    "lp-stability",
    "confinement",
    "sub-braid",
    "hecke-algebra",
  ],
  uses: ["def:lp-stable"],
});
