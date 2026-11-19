import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "conj:color-superconductivity-borromean",
  title:
    "Color superconductivity as Borromean-to-Hopf topological reconfiguration",
  lean: {
    ref: "qou:QOU.Archimedean.first_order_transition",
    validation: "not_checked",
  },
  tags: [
    "tier:E",
    "color-superconductivity",
    "diquark",
    "cooper-pair",
    "borromean",
    "hopf",
    "CFL",
    "color-flavor-locking",
    "neutron-star",
  ],
  uses: [
    "prop:borromean-hopf-energy-crossover",
    "rem:deconfinement-golden-threshold",
  ],
  cites: [
    "alford1999",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/m_p_borromean_verification_50dps.py",
    witness: "computations/m-p-borromean-verification-50dps.witness.json",
    status: "verified",
  },
});
