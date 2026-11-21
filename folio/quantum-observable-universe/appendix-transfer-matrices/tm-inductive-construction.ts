import { prose } from "../../schema/builders";

export default prose({
  label: "tm-inductive-construction",
  title: "Inductive construction ($A \\to A+1$)",
  uses: [
    "prop:shell-closure-stability",
    "prop:generator-volume-decomposition",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Given the reduced nucleus element $\\bar{\\mathcal{N}}(A)$, Hopf-linking the next nucleon and applying the Gröbner--Shirshov division algorithm requires only Hecke reductions — zero Yang--Baxter and zero far-commutativity steps — and the resulting chain state, with coefficients produced by the transfer-matrix recurrence, is the exact normal form. This is the content of [the Hecke-only reduction proposition](#prop:tm-gs-normal-form), proved by induction on $A$." },
  ],
  tags: [
    "transfer-matrix",
    "inductive",
    "shell-closure",
    "shell-folding",
    "complexity",
    "magic-numbers",
    "groebner",
    "appendix",
  ],
});
