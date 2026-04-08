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
  lean: {
    decl: "QOU.Descartes.BreitWheelerPairProduction",
    validation: "not_checked",
  },
  uses: [
    "def:electron-knot",
    "def:positron-knot",
    "sec:knot-notation-convention",
  ],
});
