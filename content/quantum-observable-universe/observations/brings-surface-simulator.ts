import { simulator } from "../../../folio-assistant/schemas/builders";

/**
 * Bring's Surface — quaternionic spectral resolvent visualisation.
 *
 * 3D WebGL rendering of the spectral resolvent coordinates on Bring's
 * surface, showing the four β-branches and their growth factor profiles.
 */
export default simulator({
  label: "sim:brings-surface",
  title: "Bring's Surface Simulator",
  html: "simulators/brings_surface.html",
  uses: ["def:quaternionic-spectral-resolvents"],
  tags: ["brings-surface", "spectral-resolvent", "3d", "simulation"],
  defaultView: {
    name: "default",
    title: "Standard resolvent view",
    params: {
      rMin: 0.12,
      rMax: 2.5,
      deltaR: 0.14,
      deltaZeta: 0.09,
      N: 18,
      projection: "omega",
      showSurface: true,
      showGrid: true,
      autoRotate: true,
    },
  },
  views: [
    {
      name: "high-precision",
      title: "High-precision ($N = 28$)",
      params: {
        rMin: 0.05,
        rMax: 4.0,
        deltaR: 0.06,
        deltaZeta: 0.04,
        N: 28,
        projection: "omega",
        showSurface: true,
        showGrid: true,
        autoRotate: false,
      },
    },
    {
      name: "wide-range",
      title: "Wide radial range",
      params: {
        rMin: 0.02,
        rMax: 6.0,
        deltaR: 0.14,
        deltaZeta: 0.09,
        N: 18,
        projection: "omega",
        showSurface: true,
        showGrid: true,
        autoRotate: true,
      },
    },
  ],
});
