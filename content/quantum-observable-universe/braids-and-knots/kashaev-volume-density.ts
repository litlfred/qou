import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:topological-mass-formula",
  label: "rem:kashaev-volume-density",
  title: "Topological mass as volume $\\times$ density, via the Kashaev limit",
  tags: [
    "mass",
    "kashaev",
    "volume-conjecture",
    "hecke",
    "markov-trace",
    "quantum-planck",
    "non-archimedean",
  ],
  uses: [
    "prop:topological-mass-formula",
    "thm:topological-mass",
    "def:quantum-planck-constant",
    "def:substrate-parameter",
    "def:algebraic-quantum-volume",
    "prop:algebraic-volume-specialization",
    "def:habiro-ring",
    "thm:jones-markov-trace",
    "thm:markov-trace-product",
    "def:crossing-energy",
    "prop:nuclear-groebner-reduction",
  ],
  cites: ["kashaev1997", "murakami-murakami2001"],
});
