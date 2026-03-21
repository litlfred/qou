import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-dq-squared",
  title: "Non-vanishing of $d_q^2$",
  tags: ["exterior-derivative", "deformation"],
  lean: {
    decl: "QOU.categorical_dq_squared",
    validation: "leanok",
  },
  status: "not_started",
  hasProof: true,
  uses: [
    "def:categorical-q-ext-deriv",
    "def:weight-decomposition",
  ],
});
