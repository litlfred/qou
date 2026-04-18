import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:observables-algebraic-dependence",
  title:
    "Observational signatures if the QOU volumes are algebraically dependent",
  tags: [
    "transcendence",
    "falsifiability",
    "lattice-qcd",
    "proton-decay",
    "observations",
  ],
  uses: [
    "conj:hyperbolic-volume-transcendence",
    "rem:implications-algebraic-dependence",
    "rem:formal-chain-transcendence",
    "prop:topological-mass-formula",
  ],
  cites: ["yekutieli2010"],
});
