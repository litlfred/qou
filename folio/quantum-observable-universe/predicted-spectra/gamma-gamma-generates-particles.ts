import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gamma-gamma-generates-particles",
  title: "$\\gamma\\gamma$ production generates the operator basis",
  tags: [
    "photon",
    "pair-production",
    "gamma-gamma",
    "hecke-algebra",
    "generation",
    "chirality",
    "knot-operator",
  ],
  uses: ["def:breit-wheeler-pair-production"],
  lean: {
    ref: "qou:QOU.Archimedean.GammaGammaGeneration.gamma_gamma_span_top",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Sidecar retriage 2026-11-21: lean.ref moved from the def-based gamma_gamma_chirality_surjective to gamma_gamma_span_top, a new theorem on the def:photon normal form pairNFChiral that encodes the closing claim (the two-photon products span H_3(q)). The six witnesses are written out in the prose." },
  ],
});
