import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:orbital-fourier-decomposition",
  title:
    "Quantum numbers from Fourier decomposition of normal-bundle sections",
  tags: [
    "orbital",
    "fourier",
    "normal-bundle",
    "quantum-numbers",
    "spherical-harmonic",
    "laplacian",
    "trefoil",
  ],
  lean: { ref: "qou:QOU.orbital_fourier_decomposition",
    validation: "not_checked",
  },
  uses: ["conj:orbital-space-normal-bundle"],
});
