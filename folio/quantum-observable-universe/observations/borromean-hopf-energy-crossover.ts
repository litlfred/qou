import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:borromean-hopf-energy-crossover",
  title:
    "Energy crossover between Borromean and Hopf-diquark phases",
  tags: [
    "borromean",
    "hopf",
    "diquark",
    "energy-crossover",
    "critical-density",
    "phase-transition",
    "color-superconductivity",
  ],
  lean: { ref: "qou:QOU.Archimedean.borromean_hopf_energy_crossover",
    validation: "not_checked",
  },
  uses: ["def:hopf-diquark"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/q-pinning-50-digit.witness.json",
      "computations/probes/casimir-hoefsmit-additivity-probe.witness.json",
    ],
    status: "verified",
  },
});
