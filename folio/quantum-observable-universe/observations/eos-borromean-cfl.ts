import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:eos-borromean-cfl",
  title:
    "Equation of state: Borromean hadronic matter vs CFL quark matter",
  tags: [
    "equation-of-state",
    "pressure",
    "energy-density",
    "speed-of-sound",
    "conformal-limit",
    "neutron-star",
    "borromean",
    "CFL",
    "fermi-gas",
  ],
  lean: { ref: "qou:QOU.Archimedean.eos_borromean_cfl",
    validation: "not_checked",
  },
  uses: ["prop:borromean-hopf-energy-crossover"],
  computation: {
    engine: "mpmath",
    script: "computations/m_p_borromean_verification_50dps.py",
    witness: "computations/m-p-borromean-verification-50dps.witness.json",
    status: "verified",
  },
});
