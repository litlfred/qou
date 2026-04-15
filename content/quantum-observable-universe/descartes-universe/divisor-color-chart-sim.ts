import { simulator } from "../../../folio-assistant/schemas/builders";

/**
 * Divisor Visualization — Color Tubes on Brane.
 *
 * 3D WebGL rendering of the three color tube coordinates
 * (c_r, c_g, c_b) on the Brings surface affine chart,
 * with q-dependent torsion and divisor markers where
 * color tubes cross the brane surface.
 */
export default simulator({
  label: "sim:divisor-color-chart",
  title: "Divisor Visualization — Color Tubes on Brane",
  html: "folio-assistant/simulators/divisor_color_chart.html",
  uses: [
    "def:color-tube-coordinates",
    "def:brings-surface",
    "def:briggs-klein-chart",
  ],
  tags: ["brings-surface", "color-tube", "divisor", "brane", "torsion", "simulation"],
  defaultView: {
    name: "default",
    title: "Standard view ($q \\approx 1.1$)",
    params: {
      q: 1.1097,
      twistRate: 0.50,
      zMin: -2,
      zMax: 3,
      tubeRadius: 0.07,
      showBrane: true,
      showTubes: true,
      showDivisors: true,
      autoRotate: true,
    },
  },
  views: [
    {
      name: "no-torsion",
      title: "Classical limit ($q = 1$)",
      params: {
        q: 1.0,
        twistRate: 0.50,
        zMin: -2,
        zMax: 3,
        tubeRadius: 0.07,
        showBrane: true,
        showTubes: true,
        showDivisors: true,
        autoRotate: true,
      },
    },
    {
      name: "high-torsion",
      title: "High torsion ($q = 1.8$)",
      params: {
        q: 1.8,
        twistRate: 0.50,
        zMin: -2,
        zMax: 3,
        tubeRadius: 0.07,
        showBrane: true,
        showTubes: true,
        showDivisors: true,
        autoRotate: true,
      },
    },
    {
      name: "wide-range",
      title: "Wide affine chart ($z \\in [-4, 6]$)",
      params: {
        q: 1.1097,
        twistRate: 0.50,
        zMin: -4,
        zMax: 6,
        tubeRadius: 0.05,
        showBrane: true,
        showTubes: true,
        showDivisors: true,
        autoRotate: true,
      },
    },
  ],
});
