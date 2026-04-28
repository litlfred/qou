import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-element-nf",
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
