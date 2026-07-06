import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:degree-two-baryon-weight",
  title: "Degree-2 weight $\\beta_2 = -2[3]_q$ from baryon quantum number",
  lean: { ref: "qou:QOU.BaryonWeight.beta2_approx",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
});
