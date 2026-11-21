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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The companion witness [`computations/all-nuclides-sdp-admissibility-mp.witness.json`](../../../computations/all-nuclides-sdp-admissibility-mp.witness.json), produced by [`computations/all_nuclides_sdp_admissibility_mp.py`](../../../computations/all_nuclides_sdp_admissibility_mp.py) at `mpmath` 50 dps (+10 guard digits) with MPFR decimal-string transport to `solve_operator_selection_lp`, supersedes the legacy float64 sweep: | native float64 `build_atom_nf` overflowed" },
  ],
});
