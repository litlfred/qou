import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:observables-algebraic-independence",
  title:
    "Observational signatures if the QOU volumes are algebraically independent",
  tags: [
    "transcendence",
    "falsifiability",
    "lattice-qcd",
    "proton-decay",
    "observations",
  ],
  uses: [
    "conj:hyperbolic-volume-transcendence",
    "rem:implications-algebraic-independence",
    "prop:topological-mass-formula",
  ],
  cites: ["yekutieli2010"],
});
