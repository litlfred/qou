import { remark } from "../../schema/builders";

export default remark({
  label: "rem:spectral-dynamics",
  title: "Spectral dynamics and the $\\mathrm{Sp}(1)$ action",
  uses: [
    "def:quaternionic-spectral-resolvents",
    "def:quantum-planck-constant",
    "def:q-reeb-flow",
    "rem:q-harmonic-physical",
  ],
});
