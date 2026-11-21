import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "deprecated", date: "2026-08-31", body: "The scalar substrate density $\\rho_q = 1/\\hbar_q^2$ used below is the structurally-wrong leading-order ansatz; the operator-valued $A^\\lambda_{\\mu, \\nu}(I)$ graded expansion supersedes it." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:quantum-temperature",
  title: "Quantum temperature",
  tags: [
    "temperature",
    "statistical-mechanics",
    "reeb-flow",
    "planck-time",
    "non-abelian-stokes",
    "surface-integral",
  ],
  lean: { ref: "qou:QOU.Information.quantumTemperature",
    validation: "not_checked",
  },
  // rem:kashaev-volume-density dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // not cited in the definition. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: ["def:quantum-entropy", "def:planck-time"],
});
