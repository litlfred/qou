import { example } from "../../schema/builders";

export default example({
  label: "ex:hydrogen-derived-nf",
  title: "Hydrogen: full normal form from pair production",
  interprets: "conj:four-term-pair-nucleon",
  tags: ["hydrogen", "atom", "normal-form", "derived", "hopf-link"],
  uses: ["prop:frobenius-gram-matrix"],
});
