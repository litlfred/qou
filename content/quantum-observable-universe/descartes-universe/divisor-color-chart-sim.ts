import { simulator } from "../../../folio-assistant/schemas/builders";

/**
 * Divisor Visualization — Color Tubes on Brane (P⁴ embedding).
 *
 * 3D WebGL rendering of the three color tube coordinates
 * (c_r, c_g, c_b) on the Brings surface with projective
 * parameterization z ∈ [0, ∞] = P¹(R), smooth brane profile
 * R(z) = s·√((2+z+2z²)/3), q-dependent torsion, and selectable
 * base scalings (arctan, log, √z, linear).
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
      zMax: 8,
      braneScale: 0.35,
      scale: "projective",
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
        zMax: 8,
        braneScale: 0.35,
        scale: "projective",
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
        zMax: 8,
        braneScale: 0.35,
        scale: "projective",
        tubeRadius: 0.07,
        showBrane: true,
        showTubes: true,
        showDivisors: true,
        autoRotate: true,
      },
    },
    {
      name: "wide-range",
      title: "Wide range ($z_{\\max} = 20$, log scale)",
      params: {
        q: 1.1097,
        twistRate: 0.50,
        zMax: 20,
        braneScale: 0.25,
        scale: "log",
        tubeRadius: 0.05,
        showBrane: true,
        showTubes: true,
        showDivisors: true,
        autoRotate: true,
      },
    },
  ],
});
