import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:partition-sum-proton-residual",
  title:
    "Proton tower residual = $m_e \\cdot \\mathrm{tr}_M(C_{\\mathrm{Frob}}) = m_e(2 + 1/[2]_q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.proton_tower_residual_frobenius",
    validation: "not_checked",
  },
  uses: ["prop:schur-weyl-mass-decomposition"],
  tags: [
    "proton",
    "residual",
    "frobenius",
    "co-casimir",
    "self-dual",
    "partition-sum",
    "hook-length",
    "mass-endomorphism",
    "gb-filtration",
  ],
});
