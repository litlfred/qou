import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body:
        "Proved over any integral domain R at non-roots of unity (`∀ m ≠ 0, q^(2m) ≠ 1`): any two Joseph-Letzter Cartan-ansatz " +
        "elements `F E + P(K)` whose difference commutes with E in the PBW basis differ by a ground-ring scalar " +
        "(`casimir_ansatz_unique_up_to_scalar`) and are equal under spin-0 eigenvalue normalisation (`casimir_ansatz_unique_of_spin_zero`), " +
        "alongside `QCasimir.not_unique_up_to_scalar_unconstrained` showing the PBW/normalisation hypotheses are necessary.",
    },
  ],
  label: "prop:q-casimir-unique",
  title: "Uniqueness of the $q$-Casimir element up to scalar",
  lean: { ref: "qou:QOU.UqCasimirUniqueness.casimir_ansatz_unique_of_spin_zero",
    validation: "not_checked",
  },
  uses: ["prop:q-casimir-exists"],
  proofs: ["prf:q-casimir-unique"],
  tags: ["uniqueness", "casimir", "central-element"],
});
