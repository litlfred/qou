import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:defect-legendrian-knot",
  title: "The unit defect as a Legendrian knot",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.defect_legendrian_knot",
    validation: "stub",
  },
  uses: [
    "def:unit-particle-state",
    "def:categorical-reeb-derivation",
  ],
  tags: ["legendrian", "knot", "contact-geometry", "torsion-leaf"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**Demoted `proposition` -> `conjecture` (bean `qou-8b0q`).** The Lean sibling is a single `def defect_legendrian_knot` that NAMES the claim; it derives nothing, and the manifest's own `validation: \"stub\"` said so. A provable kind whose Lean only names its statement is the `proof-statement-integrity` gap AGENTS.md §3b-cond item 5 defines, so the honest kind is `conjecture` until the geometric content (the $q$-torsion leaf / Reeb-derivation substrate its docstring defers to) is actually formalised. Predecessor `qou-q407` had already converted the vacuous `theorem (h : P) : P := h` form to an honest declaration; this completes the pair by fixing the block kind to match. Nothing about the mathematics changed. Blast radius measured before the relabel: **0 `uses[]` edges** reference this label, and **1** prose anchor (the auto-generated `definition-index.md`, regenerated here).",
    },
  ],
});
