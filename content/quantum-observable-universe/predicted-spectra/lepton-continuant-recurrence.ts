import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lepton-continuant-recurrence",
  proofs: ["prf:lepton-continuant-recurrence"],
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
