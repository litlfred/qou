import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:quantum-gap-collapse",
  title: "Collapse of the quantum gap",
  lean: {
    decl: "QOU.AlgebraicSubstrate.quantum_gap_collapse",
    validation: "not_checked",
  },
  uses: [
    "def:classical-limit-functor",
    "def:substrate-parameter-planck",
    "def:categorical-reeb-derivation",
  ],
  tags: [
    "quantum-gap",
    "classical-limit",
    "collapse",
    "braiding-trivialization",
  ],
});
