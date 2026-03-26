import { definition } from "../../schema/builders";

export default definition({
  label: "def:double-slit-q-phase",
  lean: {
    decl: "QOU.Experimental.double_slit_q_phase",
    validation: "not_checked",
  },
  title: "$q$-deformed path phase",
  uses: [
    "def:categorical-q-ext-deriv",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "def:categorical-reeb",
  ],
  tags: ["double-slit", "phase", "q-deformation", "interference"],
});
