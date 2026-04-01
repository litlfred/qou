import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quaternionic-spectral-resolvents",
  label: "rem:spectral-dynamics",
  title: "Spectral dynamics and the $\\mathrm{Sp}(1)$ action",
  uses: [
    "def:quaternionic-spectral-resolvents",
    "def:quantum-planck-constant",
    "ex:q-reeb-flow",
    "rem:q-harmonic-physical",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/spectral-dynamics-0.svg", blockIndex: 0, hash: "dbf0b9977a75" },
  ],
  simulator: { ref: "sim:quantum-brings-surface" },
});
