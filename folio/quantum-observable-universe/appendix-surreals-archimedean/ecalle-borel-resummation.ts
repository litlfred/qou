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
  cites: ["ecalle1981", "arxiv-2302.08363v2"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The coefficient-wise division $a_n \\mapsto a_n / n!$ is formalised as `borelCoeff` in the Lean sibling." },
    {
      kind: "note",
      date: "2026-07-13",
      body:
        "The uniqueness underlying the median resummation (the lateral sum is " +
        "asymptotic to the Gevrey-1 series, and the median sum is the unique " +
        "real single-valued resummation) is the Watson / Nevanlinna–Sokal " +
        "theorem, now formalized sorry-free in the Mathlib-gap library " +
        "`QOU.Mathlib.Borel` (bean el8w): `watson_uniqueness_rhp_open` (open " +
        "right half-plane) and `watson_uniqueness_sector` (sector-at-0), built " +
        "on the Gevrey-1 ⇒ Borel-disc convergence and the term-wise Laplace " +
        "engine (`laplace_borel_term`) with the regularity `borelSum_eq_tsum` " +
        "(Borel sum = ordinary sum on the disc of convergence). These are the " +
        "general analysis engine; they are distinct from this block's own " +
        "`borelCoeff` sibling and do not by themselves discharge any specific " +
        "series' asymptotic (e.g. the figure-eight volume conjecture, which " +
        "additionally needs the saddle-point existence/value).",
    },
  ],
});
