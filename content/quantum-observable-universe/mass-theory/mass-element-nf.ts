import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-element-nf",
  lean: { ref: "qou:QOU.BraidKnot.HeckeMassNF" },
  title: "Normal form of the Hecke mass element",
  uses: ["conj:mass-endomorphism"],
  tags: [
    "mass",
    "hecke-algebra",
    "normal-form",
    "degree-filtration",
    "brane-tower",
    "photon-massless",
  ],
});
