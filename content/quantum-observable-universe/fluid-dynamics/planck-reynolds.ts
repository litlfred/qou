import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:planck-reynolds",
  title: "Planck--Reynolds number and the turbulence transition",
  uses: ["def:information-speed-of-light"],
  // Chapter overview (§0): both are results this block previews to situate
  // the turbulence dial, and both sentences state inline what they need (the
  // four intensity levels are listed on the spot). Forward pointers, not
  // prerequisites.
  foreshadows: [
    "prop:discrete-vortex-spectrum",
    "rem:vortex-intensity-modes",
  ],
  tags: ["reynolds-number", "turbulence", "planck-scale", "fluid-dynamics"],
});
