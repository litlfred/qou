import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:faddeev-phib-uniqueness",
  title:
    "Uniqueness of the modular-double $\\Phi_b$: strip growth pins the quantum dilogarithm up to scale",
  lean: {
    ref: "qou:QOU.QBeta.PhiBProdUniquenessMeromorphic.phiBProd_uniqueUpToScalar_of_meromorphic",
  },
  uses: [],
  cites: [
    "faddeev1995",
    "faddeev1994",
  ],
  tags: [
    "faddeev",
    "quantum-dilogarithm",
    "modular-double",
    "qbeta",
    "rigidity",
    "uniqueness",
  ],
});
