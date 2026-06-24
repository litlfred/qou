import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:p-bandwidth-bound",
  proofs: ["prf:p-bandwidth-bound"],
  lean: { ref: "qou:QOU.Information.p_bandwidth_bound", validation: "not_checked" },
  title: "Polynomial computation as sub-horizon bandwidth",
  tags: [
    "P-class",
    "bandwidth",
    "information-flow",
    "planck-step",
    "complexity",
    "polynomial-time",
  ],
  uses: ["def:computational-horizon"],
});
