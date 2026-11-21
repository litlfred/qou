import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-energy",
  label: "rem:mass-energy-electron-check",
  title: "Electron: crossing energy does not determine energy",
  tags: [
    "mass-energy",
    "electron",
    "trefoil",
    "crossing-energy",
    "information-theory",
  ],
  uses: [
    "def:mass-energy",
    "def:crossing-energy",
    "def:mass-identity",
    "rem:mass-energy-not-crossing-energy",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "Until 2026-11-15 this remark predicted the electron mass as $3q(q-1)^2$ from its crossing energy. That rested on the false identity of crossing energy with $\\mathfrak{m} c_q^2$ and is withdrawn.",
    },
  ],
});
