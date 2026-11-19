import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:beta-decay-energy-scale",
  label: "rem:negative-debt-confinement",
  title:
    "Negative coefficient debt, confinement, and the nine-strand direction",
  tags: [
    "beta-decay",
    "confinement",
    "negative-debt",
    "nine-strand",
    "hecke-algebra",
    "groebner-shirshov",
    "computational-witness",
    "status-remark",
  ],
  uses: ["rem:beta-decay-energy-scale"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/confinement-operator-selection.witness.json",
    status: "verified",
  },
});
