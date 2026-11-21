import { remark } from "../../schema/builders";

export default remark({
  label: "rem:beta-decay-skein-properties",
  interprets: "def:beta-decay-skein",
  title:
    "Weak vertex, $10$-crossing budget, and $Q$-value of the $\\beta$-decay Skein operation",
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
  uses: [
    "def:beta-decay-skein",
    "def:stable-nucleus",
    "prop:nuclear-groebner-reduction",
    "def:categorical-proton",
    "def:categorical-neutron",
    "rem:force-knot-identification",
    "def:Q-value-transition",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21; owner chose 'rebuild on sigma_0 sigma_1 sigma_0'): the electron in the beta-decay products is the word e^- = sigma_0 sigma_1 sigma_0 (closure: Hopf link), the positron sigma_0^-1 sigma_1^-1 sigma_0^-1. The 3 + 0 + 7 crossing split is now a braid identity, (sigma_0 sigma_1)^5 = e^- (e^- (sigma_0 sigma_1)^2) in B_3, proved in QOU.BraidKnot.WeakVertexElectronFactor. Issue #8822." },
  ],
});
