import { simulator } from "../../../folio-assistant/schemas/builders";

/**
 * Quantum Bring's Surface — chiral tubes on the projective space-time brane.
 *
 * Advanced 3D WebGL simulator with multi-canvas analysis: chiral grid,
 * Weierstrass curves, affine charts, CP¹ fibers, Julia sets, and
 * Möbius spectral classification.
 */
export default simulator({
  label: "sim:quantum-brings-surface",
  title: "Quantum Bring's Surface Simulator",
  html: "folio-assistant/simulators/quantum_brings_surface.html",
  uses: [
    "def:quaternionic-spectral-resolvents",
    "prop:color-elliptic",
    "def:color-tube-coordinates",
  ],
  tags: ["brings-surface", "chiral", "quantum", "julia-set", "3d", "simulation"],
  defaultView: {
    name: "default",
    title: "Chiral tube overview",
    params: {
      rMin: 0.12,
      rMax: 2.5,
      deltaR: 0.14,
      deltaZeta: 0.09,
      N: 18,
      projection: "omega",
      showSurface: true,
      showGrid: true,
      showChiral: true,
      autoRotate: true,
    },
  },
  views: [
    {
      name: "julia-set",
      title: "Julia set analysis",
      params: {
        rMin: 0.12,
        rMax: 2.5,
        deltaR: 0.14,
        deltaZeta: 0.09,
        N: 18,
        projection: "omega",
        showSurface: true,
        showGrid: false,
        showChiral: false,
        showJulia: true,
        autoRotate: false,
      },
    },
    {
      name: "weierstrass",
      title: "Weierstrass invariants",
      params: {
        rMin: 0.12,
        rMax: 2.5,
        deltaR: 0.14,
        deltaZeta: 0.09,
        N: 18,
        projection: "omega",
        showSurface: true,
        showGrid: true,
        showChiral: false,
        showWeierstrass: true,
        autoRotate: false,
      },
    },
  ],
});
