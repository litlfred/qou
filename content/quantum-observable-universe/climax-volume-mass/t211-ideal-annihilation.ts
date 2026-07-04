import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  interprets: "prop:vertex-algebra-jet-relations",
  label: "rem:t211-ideal-annihilation",
  title: "Behaviour of $T_{2,11}$ on the jet bundle ideals",
  tags: [
    "torus-knot", "genus-bound", "spectral-filter",
    "hecke-algebra", "knot-coordinates", "ideal",
  ],
  uses: [
    "prop:genus-filtration-ideal",
    "prop:vertex-algebra-jet-relations",
    "prop:shell-structure-eigenvalues",
    "prop:x5-bring-weight-identification",
    "thm:hyperelliptic-z5-classification",
  ],
  cites: ["kassel1995", "jones1987"],
});
