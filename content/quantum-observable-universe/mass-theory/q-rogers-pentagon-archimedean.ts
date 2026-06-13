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
  authorNotes: [
    {
      kind: "status",
      body: "**Classical case ($q = 1$): proven** (Rogers 1907, Lewin 1981).\n**q-deformation: numerical evidence at $q_0$** to 1-5% (improving on\nclassical by 1.5–5$\\times$). Formal q-deformed proof tracked as open\nresearch; Lean skeleton in place.",
    },
  ],
});
