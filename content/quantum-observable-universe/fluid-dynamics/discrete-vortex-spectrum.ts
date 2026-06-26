import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the spectral theory of rigid rotors and Kelvin waves is standard, the mathematical novelty is formally unifying these classical phenomena as evaluations of representations of the quantum group $\\mathrm{SU}_q(2)$ over the $q$-Laplacian. This specific reframing rigorously anchors vortex intensity levels and selection rules to the discrete topology of the $q$-integer spectrum, replacing heuristic classical angular momentum derivations with exact categorical constraints." },
  ],
  label: "prop:discrete-vortex-spectrum",
  lean: { ref: "qou:QOU.FluidDynamics.discrete_vortex_spectrum", validation: "not_checked" },
  title: "Discrete vortex mode spectrum",
  uses: ["rem:vortex-intensity-modes"],
  tags: ["vortex", "quantization", "spectral"],
});
