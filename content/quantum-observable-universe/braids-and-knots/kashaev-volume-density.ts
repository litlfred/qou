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
    "prop:algebraic-volume-specialization",
    "rem:body-asymptotics-catalog",
  ],
  cites: ["kashaev1997", "murakami-murakami2001"],
});
