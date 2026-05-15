import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cfs-as-traceful-projection-of-qou",
  title:
    "CFS as the traceful (Plancherel) projection of QOU — commutative spectral shadow via $\\mathrm{tr}_M$",
  lean: {
    ref: "qou:QOU.Observations.CfsAsTracefulProjection",
    validation: "not_checked",
  },
  uses: [
    "prop:algebraic-causal-action-structure",
    "prop:algebraic-gns-embedding",
    "prop:wedderburn-weight-canonical",
    "thm:jones-markov-trace",
  ],
  cites: [
    "finster2021",
    "finster2024",
    "biane1998",
    "wenzl1988",
  ],
  tags: [
    "causal-fermion-systems",
    "trace-projection",
    "commutative-shadow",
    "plancherel",
    "universality",
    "free-probability",
    "established-structural",
  ],
});
