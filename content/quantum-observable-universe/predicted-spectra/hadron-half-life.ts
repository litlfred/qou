import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "status", date: "2026-09-04", body: "Partially formalised. `lean.ref` names `hadron_half_life`, an alias for `BetaDecayData.halfLife = ln 2 / qPrefactor q` with `qPrefactor q = (q + q^{-1})(q - q^{-1})^5`; the sibling proves its positivity and the classical vanishing. No declaration states the proposition's rate $\\Gamma_\\beta = |\\mathcal{W}(q)|^2 \\mu_0/(2\\pi^3) \\cdot [2]_q \\cdot |\\mathcal{M}_q|^2 \\cdot f(Q)$. Measured in docs/audits/2026-09-04-lean-ref-resolution-count-mass-theory.md; gap bean opened the same day." },
  ],
  label: "prop:hadron-half-life",
  title:
    "Hadron half-life from the $q$-deformed transition amplitude",
  tags: [
    "half-life",
    "beta-decay",
    "hadron",
    "transition-amplitude",
    "substrate-parameter",
    "valley-of-stability",
  ],
  lean: { ref: "qou:QOU.Archimedean.hadron_half_life",
    validation: "not_checked",
  },
  uses: ["prop:integer-stability"],
});
