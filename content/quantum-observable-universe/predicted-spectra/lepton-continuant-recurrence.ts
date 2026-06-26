import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "This structural identification of the lepton-tower sequence as a positive-sign Morgan-Voyce continuant, distinct from standard Chebyshev U_n recurrences, introduces a novel algebraic lens that elegantly captures the unique combinatorial constraints of the lepton sector." },
  ],
  label: "prop:lepton-continuant-recurrence",
  title:
    "Continuant recurrence for the lepton tower $T_{2,n}$",
  tags: [
    "lepton",
    "torus-knot",
    "hecke-algebra",
    "normal-form",
    "continuant",
    "morgan-voyce",
    "electron",
    "muon",
    "tau",
  ],
  lean: { ref: "qou:QOU.Archimedean.lepton_continuant_recurrence",
    validation: "not_checked",
  },
  uses: [
    "def:beta-decay-skein",
    "rem:archimedean-leptons",
  ],
});
