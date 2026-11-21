import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-schur-weyl-self-duality",
  title:
    "Schur-Weyl justification of shell-operator self-duality",
  lean: { ref: "qou:QOU.BraidKnot.ShellSchurWeylSelfDuality.fixed_iff_coeff_symm",
    validation: "not_checked",
  },
  cites: [
    "kassel1995",
    "mathas1999",
    "dipper-james1986",
  ],
  tags: [
    "schur-weyl",
    "representation-duality",
    "shell-closure",
    "conjugate-partition",
    "self-duality",
    "quantum-group",
    "sigma-shell",
  ],
});
