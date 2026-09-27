import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:double-slit-q-phase",
  lean: { ref: "qou:QOU.Experimental.double_slit_q_phase",
    validation: "not_checked",
  },
  title: "$q$-deformed path phase",
  uses: [
    "def:categorical-q-ext-deriv",
    "def:quantum-planck-constant",
  ],
  tags: ["double-slit", "phase", "q-deformation", "interference"],
});
