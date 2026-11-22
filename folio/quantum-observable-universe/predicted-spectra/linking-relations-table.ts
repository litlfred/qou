import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:embeddability-closure",
  label: "rem:linking-relations-table",
  title:
    "Linking relations between building block knots",
  tags: [
    "linking",
    "hopf-link",
    "skein",
    "crossing",
    "composite",
    "building-block",
    "appendix",
    "connected-sum",
    "satellite",
  ],
  uses: ["rem:knot-formula-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21; owner chose 'rebuild on sigma_0 sigma_1 sigma_0'): the electron in the beta-decay products is the word e^- = sigma_0 sigma_1 sigma_0 (closure: Hopf link), the positron sigma_0^-1 sigma_1^-1 sigma_0^-1. The 3 + 0 + 7 crossing split is now a braid identity, (sigma_0 sigma_1)^5 = e^- (e^- (sigma_0 sigma_1)^2) in B_3, proved in QOU.BraidKnot.WeakVertexElectronFactor. Issue #8822." },
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Rows of Tables 1 and 2 now name $T_{2,3}$, $T_{2,5}$, $T_{2,7}$ and mirrors as lepton partners of the quarks. Needs re-scoping: the readings $T_{2,3} \\oplus T_{2,3}^{\\sigma} = \\pi^{+}$, $T_{2,3} \\oplus T_{2,5}^{\\sigma} = K^{+}$ and the skein $T_{2,3} \\oplus T_{2,3} \\to 4_1$ (Higgs), which were argued from quark pairs as trefoil pairs. Still valid: the knot-theoretic sums and the global-mirror rows." },
  ],
});
