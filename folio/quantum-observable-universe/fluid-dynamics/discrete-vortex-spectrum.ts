import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:discrete-vortex-spectrum",
  lean: { ref: "qou:QOU.FluidDynamics.discrete_vortex_spectrum", validation: "not_checked" },
  title: "Discrete vortex mode spectrum",
  uses: ["rem:vortex-intensity-modes"],
  tags: ["vortex", "quantization", "spectral"],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
