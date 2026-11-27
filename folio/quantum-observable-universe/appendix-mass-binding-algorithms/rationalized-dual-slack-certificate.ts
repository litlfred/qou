import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:rationalized-dual-slack-certificate",
  renamedFrom: ["alg:lp-sdp-dual-emission", "alg:witness-json-pipeline"],
  title:
    "Solver-External Rationalized Dual-Slack Optimality and Uniqueness Certification ($\\mathcal{L}_0\\text{--}\\mathcal{L}_4$)",
  uses: [
    "prop:operator-selection-lp",
    "prop:nuclear-chamber-groebner-basis",
  ],
  cites: [
    "farkas1902",
    "kantorovich1939",
    "gatermann-parrilo2004",
    "simmons-duffin2015",
    "goulart-chen2024",
    "dvorak-kolmogorov2024",
  ],
  lean: {
    ref: "qou:ToricConicOpt.SymmetryReducedDualCertificate.unique_primal_of_strict_dual_slack",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script:
      "computations/probes/lp_bootstrap_dual_gaps/lp_bootstrap_dual_gaps_probe.py",
    witness: [
      "computations/rho-k-h3a-lp-dual.witness.json",
      "computations/probes/lp_bootstrap_dual_gaps/lp-bootstrap-dual-gaps.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "mba",
    "lp-dual",
    "dual-slack",
    "strict-complementarity",
    "formal-certificate",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Replaces `mba-sidecar-lp-sdp-dual-emission` (`python+numpy+cvxpy`) and retires `mba-sidecar-witness-json-pipeline` (`WitnessBuilder` packaging docs) under `qou-mba8`, grounding dual certification in `QOU.MathlibInfra.SymmetryReducedDualCertificate` (`lp_optimal_of_zero_gap`, `unique_support_of_strict_dual_slack`, `unique_primal_of_strict_dual_slack`).",
    },
  ],
});
