import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:tower-binding-energy",
  title:
    "Nuclear binding energy from the $3$-channel brane tower",
  tags: [
    "binding-energy",
    "brane-tower",
    "wedderburn",
    "three-channel",
    "partition-function",
    "zero-fitting",
    "analytic-continuation",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.towerBinding",
    validation: "not_checked",
  },
  // Was rem:hecke-charge-mass-duality, which the text never cites; that
  // remark reaches the open conj:hecke-mass-trace. The formula evaluates the
  // product quantum dilogarithm Phi_q (pole at |V| = q, named in the text),
  // which the disambiguation definition fixes. Retargeted 2026-11-20 (owner,
  // option 2 of the W11b ask on #8526; bean qou-tm3c).
  uses: [
    "def:quantum-dilogarithm-disambiguation",
  ],
});
