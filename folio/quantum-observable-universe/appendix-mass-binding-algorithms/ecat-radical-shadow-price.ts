import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:ecat-radical-shadow-price",
  renamedFrom: ["alg:confinement-sdp"],
  title:
    "Solver-Free $(1^3)$ Radical Shadow-Price Extraction on $H_3(q_0)$ ($\\mathcal{L}_0\\text{--}\\mathcal{L}_1$)",
  uses: [
    "prop:markov-gram-star-positive",
    "prop:operator-selection-lp",
  ],
  cites: [
    "farkas1902",
    "kantorovich1939",
    "wenzl1988",
  ],
  lean: {
    ref: "qou:QOU.Nuclear.ECatRadicalShadowPriceEvaluation.inner_coxeterSymmetric_radicalVec3",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script:
      "computations/probes/ecat_lp_dual_radical_geom/ecat_lp_dual_radical_geom_probe.py",
    witness: [
      "computations/a-K-via-lp-dual.witness.json",
      "computations/probes/ecat_lp_dual_radical_geom/ecat_lp_dual_radical_geom_probe.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "mba",
    "shadow-price",
    "radical",
    "lp-dual",
    "solver-free",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Replaces `mba-step10-confinement-sdp` (`python+numpy+cvxpy` on singular 6x6 Gram) with exact algebraic radical shadow-price evaluation over `Q(q_0)` (`QOU.Nuclear.ECatRadicalShadowPriceEvaluation`, witness `ecat_lp_dual_radical_geom_probe.witness.json`).",
    },
  ],
});
