import { definition } from "../../schema/builders";

export default definition({
  label: "def:breit-wheeler-pair-production",
  title: "Breit--Wheeler pair production (categorical)",
  tags: [
    "breit-wheeler",
    "pair-production",
    "photon",
    "electron",
    "positron",
    "hecke-algebra",
    "colored-photon",
    "normal-form",
  ],
  uses: ["def:photon"],
  lean: { ref: "qou:QOU.Archimedean.BreitWheelerPairProduction",
    validation: "not_checked",
  },
});
