import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:planck-reynolds",
  title: "Planck--Reynolds number and the turbulence transition",
  uses: [
    "def:substrate-parameter",
    "def:speed-of-light",
    "def:planck-length",
    "def:quantum-planck-constant",
    "rem:madelung-fluid",
    "prop:discrete-vortex-spectrum",
    "rem:vortex-intensity-modes",
  ],
  tags: ["reynolds-number", "turbulence", "planck-scale", "fluid-dynamics"],
});
