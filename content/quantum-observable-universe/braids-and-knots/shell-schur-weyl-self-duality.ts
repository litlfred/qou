import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-schur-weyl-self-duality",
  title:
    "Schur-Weyl justification of shell-operator self-duality",
  lean: { ref: "qou:QOU.BraidKnot.ShellSchurWeylSelfDuality",
    validation: "not_checked",
  },
  cites: [
    "kassel1995",
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
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_atom_shell_self_duality_mpfr.py",
    witness: "folio-assistant/computations/probe-atom-shell-self-duality-mpfr.witness.json",
    status: "experimental",
  },
});
