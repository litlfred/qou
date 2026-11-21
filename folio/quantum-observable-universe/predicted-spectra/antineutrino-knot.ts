import { definition } from "../../schema/builders";

export default definition({
  label: "def:antineutrino-knot",
  title: "Antineutrino as mirror unknot $T_{1,0}^{\\sigma}$",
  tags: [
    "antineutrino",
    "unknot",
    "mirror",
    "antiparticle",
    "lepton",
    "fermion",
    "beta-decay",
  ],
  lean: { ref: "qou:QOU.Archimedean.Antineutrino",
    validation: "not_checked",
  },
  uses: [],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21; owner chose 'rebuild on sigma_0 sigma_1 sigma_0'): the electron in the beta-decay products is the word e^- = sigma_0 sigma_1 sigma_0 (closure: Hopf link), the positron sigma_0^-1 sigma_1^-1 sigma_0^-1. The 3 + 0 + 7 crossing split is now a braid identity, (sigma_0 sigma_1)^5 = e^- (e^- (sigma_0 sigma_1)^2) in B_3, proved in QOU.BraidKnot.WeakVertexElectronFactor. Issue #8822." },
  ],
});
