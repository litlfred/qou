import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-rogers-pentagon-archimedean",
  title:
    "Post-τ pentagon = pre-τ pentagon + q-log² Rogers correction",
  lean: {
    ref: "qou:QOU.BraidKnot.QRogersAnalyticContinuation",
    validation: "not_checked",
  },
  uses: [
    "def:q-dilogarithm",
    "def:q-logarithm",
    "def:archimedean-realization-functor",
    "prop:li2q-phiq-bar-symmetrization",
    "rem:pre-tau-vs-post-tau",
  ],
  cites: ["rogers1907", "abel1826", "lewin1981"],
  computation: {
    engine: "python",
    script:
      "folio-assistant/computations/pentagon_reduction_li2q.py",
    witness:
      "folio-assistant/computations/pentagon-reduction-li2q.witness.json",
    status: "verified",
  },
  tags: [
    "pentagon",
    "rogers-five-term",
    "archimedean-wall",
    "q-logarithm",
    "log-squared-correction",
  ],
});
