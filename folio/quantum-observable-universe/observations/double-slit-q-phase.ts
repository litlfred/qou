import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c), accompanied by generic field infrastructure in QOU.MathlibInfra.LorentzBoostPhase and QOU.Observations.DeBroglieBoostedReebPhase." },
  ],
  label: "def:double-slit-q-phase",
  lean: { ref: "qou:QOU.Experimental.double_slit_q_phase",
    validation: "not_checked",
  },
  title: "$q$-deformed path phase",
  uses: [
    "def:substrate-parameter",
    "def:categorical-reeb",
    "def:categorical-q-ext-deriv",
    "def:quantum-planck-constant",
    "rem:meridian-exceptional-divisor-note",
    "rem:q-laplacian-expansion",
  ],
  cites: [
    "bach2013",
  ],
  tags: ["double-slit", "phase", "q-deformation", "interference", "de-broglie"],
});
