import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sw-classical-jet-exactness",
  lean: {
    ref: "qou:QOU.Brings.classical_jet_period_zero",
  },
  title: "The classical-jet prolongation of $\\lambda_{\\mathrm{SW}}$ is exact for $n \\ge 1$",
  uses: [
    "prop:sw-period-residue-sum",
    "prop:mi-sw-abelianisation",
  ],
  proofs: ["prf:sw-classical-jet-exactness"],
});
