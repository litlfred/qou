import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vertex-algebra-relations",
  lean: { ref: "qou:QOU.VertexAlgebra.descartes_genus",
    validation: "not_checked",
  },
  title: "QU and QUO axioms as relations on Hecke generators",
  tags: [
    "vertex-operator", "hecke-algebra", "knot-coordinates",
    "quantum-universe", "relations", "generators",
  ],
  uses: [
    "prop:frobenius-relation",
    "prop:categorical-dq-squared",
    "rem:hodge-laplacian-relation",
    "prop:cohomological-embedding",
    "rem:instanton-on-shell",
  ],
  cites: ["kassel1995", "jones1987", "yekutieli2010"],
});
