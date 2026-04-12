import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-element-nf",
  title: "Normal form of the Hecke mass element",
  uses: [
    "def:hecke-mass-element",
    "prop:hecke-mass-trace",
    "prop:categorical-mass-markov",
    "conj:mass-endomorphism",
  ],
  tags: [
    "mass",
    "hecke-algebra",
    "normal-form",
    "degree-filtration",
    "brane-tower",
    "photon-massless",
  ],
});
