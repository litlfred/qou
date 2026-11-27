import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:mass-energy",
  label: "rem:mass-energy-equivalence-interpretation",
  title:
    "Legendre origin, boost-inertia hypothesis, and regime behaviour",
  uses: [
    "prop:mass-energy",
    "cor:mass-identity-C",
    "rem:mass-energy-electron-check",
    "rem:mass-energy-pair-creation",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): One treats the electron ([electron](#rem:mass-energy-electron-check)) and the pair-creation threshold ([pair creation](#rem:mass-energy-pair-creation)) separately." },
  ],
  foreshadows: [
    "rem:mass-energy-electron-check",
    "rem:mass-energy-pair-creation",
  ],
  cites: ["yekutieli2015"],
});
