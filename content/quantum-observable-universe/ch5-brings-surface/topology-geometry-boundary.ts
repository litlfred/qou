import { remark } from "../../schema/builders";

export default remark({
  label: "rem:topology-geometry-boundary",
  title:
    "What $q$ alone computes vs what needs the geometric input",
  tags: [
    "topology",
    "geometry",
    "q-parameter",
    "mass",
    "energy",
    "volume",
    "hecke-algebra",
    "killing-form",
    "boundary",
  ],
  uses: [
    "def:substrate-parameter",
    "def:categorical-lagrangian",
    "def:qou-canonical-action",
    "thm:markov-trace-factorization",
    "thm:groebner-shirshov-energy",
    "prop:reidemeister-action-table",
    "prop:topological-mass-formula",
    "def:skein-binding-lagrangian",
  ],
});
