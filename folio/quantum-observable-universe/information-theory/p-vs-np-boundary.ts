import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "status", date: "2026-11-15", body: "Demoted from proposition to conjecture (owner ruling 2026-11-15). The text already called itself a conjecture; the Lean `boundary_dichotomy` proves only the classical-logic dichotomy 'empty iff not non-empty' and says nothing about P or NP. `thm:geometry-of-incompleteness` listed this block in `uses` without using it (its Lean imports only PhysicalIntractability); that edge was replaced by the blocks its text rests on." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "conj:p-vs-np-boundary",
  lean: { ref: "qou:QOU.PvsNPBoundary.boundary_dichotomy" },
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ as jet horizon opacity",
  tags: [
    "P-vs-NP",
    "jet-horizon",
    "boundary-condition",
    "complexity",
    "information-barrier",
    "event-horizon",
    "computational-horizon",
  ],
  uses: [
    "prop:p-bandwidth-bound",
    "def:polynomial-observable-subcategory",
    "def:computational-boundary",
    "rem:substrate-gm-torsion",
  ],
  cites: ["cook1971", "freedman2003"],
});
