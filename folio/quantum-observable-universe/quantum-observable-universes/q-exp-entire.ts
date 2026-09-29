import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-02",
      body:
        "Analytic licence for the categorical Wick rotation: entirety of $\\exp_q$ makes the single grouplike function defined on all of $\\mathbb{C}$, so the continuation from the real (Laplace) axis to the imaginary (Fourier) axis is legitimate. The identity $F(\\xi)=L(i\\xi)$ itself is definitional once one grouplike element is used; summability-everywhere is the falsifiable core. Lean sibling is the archimedean specialisation over $\\mathbb{C}$ (AGENTS.md §7c); the combinatorial $[n]_q!$ growth is generic. Sorry-free; axioms `propext, Classical.choice, Quot.sound` only.",
    },
  ],
  label: "prop:q-exp-entire",
  title: "The $q$-exponential is entire",
  tags: ["q-exponential", "wick-rotation", "summability", "categorical"],
  lean: { ref: "qou:QOU.QExp.qExpTerm_summable", validation: "not_checked" },
  uses: ["prop:braiding-eigenvalue-extraction"],
});
