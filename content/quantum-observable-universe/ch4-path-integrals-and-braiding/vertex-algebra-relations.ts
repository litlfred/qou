import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vertex-algebra-relations",
  lean: {
    decl: "QOU.vertex_algebra_relations",
    validation: "not_checked",
  },
  title: "QU and QUO axioms as relations on Hecke generators",
  tags: [
    "vertex-operator", "hecke-algebra", "knot-coordinates",
    "quantum-universe", "relations", "generators",
  ],
  uses: [
    "def:quantum-universe",
    "def:quantum-observable-universe",
    "def:vertex-operator",
    "def:frobenius-pairing",
    "prop:frobenius-relation",
    "def:snake-identity",
    "thm:jones-markov-trace",
    "rem:r-matrix-braiding",
    "def:braid-group",
  ],
  cites: ["kassel1995", "jones1987", "turaev1988"],
});
