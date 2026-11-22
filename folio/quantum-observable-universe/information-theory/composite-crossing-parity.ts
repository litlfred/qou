import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "refined-framing", date: "2026-11-15", body: "Filed as a conjecture by owner ruling (2026-11-15): the claim that one Hecke decomposition determines both nuclear shell structure and thermodynamic phase behaviour is not proved. The Lean sibling proves only the parity count $n_K(\mathcal{A}(Z,N)) \equiv Z \pmod 2$ (`crossing_parity_eq_Z`), which is used by [rem:crossing-parity-test](#rem:crossing-parity-test)." },
  ],
  label: "conj:composite-crossing-parity",
  title: "Sublimation from shell-filling representation theory",
  tags: [
    "sublimation",
    "shell-structure",
    "young-diagram",
    "hecke-representation",
    "phase-transition",
    "magic-numbers",
  ],
  lean: { ref: "qou:QOU.Information.crossing_parity_eq_Z",
    validation: "not_checked",
  },
  uses: [
    "conj:borromean-quark",
    "prop:shell-structure-eigenvalues",
    "prop:noble-gas-characterization",
  ],
});
