import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:delta-lambda-categorical-closure",
  title:
    "Per-partition $\\Delta_\\lambda(K)$ as the per-block algebraic residue at $\\mathcal{O}_{\\mathrm{prin}}^{(\\lambda)}$",
  tags: [
    "delta-lambda",
    "binding-energy",
    "algebraic-residue",
    "wedderburn-block",
    "categorical-closure",
    "open-problem",
  ],
  uses: [
    "prop:sw-period-thimble-equivalence",
    "prop:mobius-limit-from-thimble",
    "prop:morse-wall-q-moduli",
    "rem:picard-lefschetz-thimble",
    "rem:color-tube-cubic",
  ],
  cites: [
    "grothendieck1966",
    "hartshorne1966",
    "pham1965",
    "seidel2008",
  ],
});
