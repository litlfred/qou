import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:discrete-vortex-spectrum",
  title: "Discrete vortex mode spectrum",
  uses: [
    "rem:vortex-intensity-modes",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "rem:primordial-vortex",
  ],
  tags: ["vortex", "quantization", "spectral"],
});
