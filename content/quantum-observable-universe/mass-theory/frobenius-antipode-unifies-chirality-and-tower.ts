import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:frobenius-antipode-unifies-chirality-and-tower",
  title:
    "Frobenius antipode $S\\colon \\sigma \\leftrightarrow \\sigma^{-1}$ unifies chirality (Term 5) and neutron-tower closure",
  lean: {
    ref: "qou:QOU.BraidKnot.frobenius_antipode_unifies",
    validation: "not_checked",
  },
  uses: [
    "prop:chirality-dual-space-derivation",
    "thm:six-term-mass-formula-complete",
  ],
  cites: ["kassel1995"],
  tags: [
    "frobenius",
    "antipode",
    "chirality",
    "neutron-tower",
    "alpha-blend",
    "catalan",
    "unification",
  ],
});
