import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): `rem:baryon-period-ratio`).**" },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "conj:geom-yekutieli-alignment",
  title:
    "Geometric invariant $\\mathrm{Geom}(K)$ as rigid dualizing evaluation",
  lean: { ref: "qou:QOU.BraidKnot.geom_yekutieli_alignment",
    validation: "not_checked",
  },
  uses: [
    "prop:topological-mass-formula",
    "prop:yekutieli-lifting",
    "conj:hyperbolic-volume-transcendence",
  ],
  cites: ["yekutieli2010", "yekutieli2015"],
  tags: [
    "rigid-dualizing",
    "yekutieli",
    "frobenius-pairing",
    "self-duality",
    "thurston-geometrization",
    "volume-conjecture",
    "chern-simons",
  ],
});
