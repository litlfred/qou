import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chirality-trefoil-electron-positron",
  title:
    "Electron and positron words: a mirror pair",
  interprets: "prop:antiparticle-crossing-reversal",
  tags: [
    "trefoil",
    "chirality",
    "electron",
    "positron",
    "antiparticle",
    "time-reversal",
    "exceptional-divisor",
  ],
  uses: ["prop:antiparticle-crossing-reversal"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21; owner chose 'rebuild on sigma_0 sigma_1 sigma_0'): rebuilt on e^- = sigma_0 sigma_1 sigma_0 and e^+ = its inverse. New finding: the Hopf link is amphichiral as an unoriented link, so the electron/positron distinction lives in the braid (writhe +3 vs -3, Lean QOU.BraidKnot.ElectronPositronWrithe) and the closure's orientation, not in the unoriented link type as it did for the trefoil. Quark letters follow the up-quark ruling (unknot strands). The label is kept so citations stay valid. Issue #8822." },
  ],
});
