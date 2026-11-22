import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21; owner chose 'rebuild on sigma_0 sigma_1 sigma_0'): the electron in the beta-decay products is the word e^- = sigma_0 sigma_1 sigma_0 (closure: Hopf link), the positron sigma_0^-1 sigma_1^-1 sigma_0^-1. The 3 + 0 + 7 crossing split is now a braid identity, (sigma_0 sigma_1)^5 = e^- (e^- (sigma_0 sigma_1)^2) in B_3, proved in QOU.BraidKnot.WeakVertexElectronFactor. Issue #8822." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:beta-decay-skein",
  title:
    "Beta decay as a Skein crossing change on the Gröbner normal form",
  tags: [
    "beta-decay",
    "skein-relation",
    "groebner-basis",
    "hecke-algebra",
    "weak-force",
    "crossing-change",
    "lepton",
    "normal-form",
  ],
  lean: { ref: "qou:QOU.Archimedean.BetaDecaySkein",
    validation: "not_checked",
  },
  uses: ["def:positron-knot"],
});
