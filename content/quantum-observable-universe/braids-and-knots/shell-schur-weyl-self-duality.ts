import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-schur-weyl-self-duality",
  title:
    "Schur-Weyl justification of shell-operator self-duality",
  lean: {
    decl: "QOU.BraidKnot.ShellSchurWeylSelfDuality",
    validation: "not_checked",
  },
  uses: [
    "def:confinement-level",
    "def:stable-atom",
    "prop:bw-coefficient-shadow-price",
    "def:hecke-normal-form",
    "thm:jones-markov-trace",
    "def:quantum-su2",
  ],
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
});
