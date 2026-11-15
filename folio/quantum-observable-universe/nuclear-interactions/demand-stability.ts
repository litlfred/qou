import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:demand-stability",
  lean: { ref: "qou:QOU.ParticleInteractions.demand_stability", validation: "not_checked" },
  title: "Demand profile determines nuclear and atomic stability",
  tags: [
    "stability",
    "demand",
    "normal-form",
    "beta-decay",
    "shell-closure",
    "magic-numbers",
  ],
  uses: ["def:derived-atom", "def:demand-profile"],
  computation: {
    engine: "python+mpmath",
    script: "computations/all_nuclides_sdp_admissibility_mp.py",
    witness: "computations/all-nuclides-sdp-admissibility-mp.witness.json",
    status: "verified",
  },
});
