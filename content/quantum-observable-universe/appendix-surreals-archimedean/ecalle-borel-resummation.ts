import { definition } from "../../schema/builders";

export default definition({
  label: "def:ecalle-borel-resummation",
  lean: {
    ref: "qou:QOU.AppendixSurreals.EcalleBorelResummation.borelCoeff",
    validation: "not_checked",
  },
  title:
    "Écalle–Borel resummation: the Borel transform $\\mathcal{B}$ and its lateral and median sums",
  tags: [
    "resurgence",
    "borel-transform",
    "median-resummation",
    "alien-derivative",
    "asymptotic-series",
    "archimedean",
  ],
  cites: ["ecalle1981"],
});
