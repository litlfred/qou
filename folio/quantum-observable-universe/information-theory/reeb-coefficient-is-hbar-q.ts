import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
  label: "prop:reeb-coefficient-is-hbar-q",
  title:
    "The Reeb coefficient of $D_\\nabla$ is the quantum Planck constant: $1 - q^{-1} = (q-1)/q$",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.reeb_coefficient_eq_hbar_q",
    validation: "not_checked",
  },
  // def:quantum-planck-constant is deliberately NOT listed: def:planck-time
  // already uses[] it, so naming both is transitively redundant on the
  // editorial relation (reading order is transitive).
  uses: ["def:planck-time"],
  tags: [
    "reeb-flow",
    "dirac-operator",
    "hbar-q",
    "information-theory",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_wave3_periodic_table_synthesis_probe.py",
    witness: [
      "computations/probes/nuclear-wave3-periodic-table-synthesis.witness.json",
      "computations/probe-markov-trace-factorization.witness.json",
    ],
    status: "verified",
  },
});
