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
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Witness provenance: `computations/all-nuclides-sdp-admissibility-mp.witness.json` (`computations/all_nuclides_sdp_admissibility_mp.py` at mpmath 50 dps + 10 guard digits, MPFR decimal transport to `solve_operator_selection_lp`, `nf_overflow_count = 0`, `rows_carrying_mpfr_dual = 4,932`) supersedes the binary64 `build_atom_nf` sweep (`all_nuclides_sdp_admissibility.py`).",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/all_nuclides_sdp_admissibility_mp.py",
    witness: "computations/all-nuclides-sdp-admissibility-mp.witness.json",
    status: "verified",
  },
});
