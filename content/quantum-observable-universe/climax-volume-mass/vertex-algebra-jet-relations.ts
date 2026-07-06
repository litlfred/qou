import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:vertex-algebra-jet-relations",
  lean: { ref: "qou:QOU.VertexAlgebra.JetRelations.euler_level_stable",
    validation: "not_checked",
  },
  title: "QU/QUO and cohomological relations on the jet bundle",
  tags: [
    "vertex-operator", "jet-prolongation", "brane-tower",
    "hecke-algebra", "knot-coordinates", "relations",
  ],
  uses: [
    "prop:vertex-algebra-relations",
    "rem:prolongation-categorical",
  ],
  cites: ["kassel1995", "jones1987", "yekutieli2010"],
});
