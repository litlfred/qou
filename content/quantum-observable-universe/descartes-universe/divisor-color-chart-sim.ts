import { simulator } from "../../../folio-assistant/schemas/builders";

/**
 * Divisor Visualization — Brings Cover on the Riemann Sphere.
 *
 * The base P¹(C) is shown as the Riemann sphere S².  The brane lives
 * on the INTERIOR (the 3-ball).  The three color sheets of the cover
 * π: Σ₄ → P¹(C) live on the EXTERIOR, at radius R_brane + ΔR.
 * At each pole (z=0 and z=∞) all three sheets converge to a single
 * point — these are the EXCEPTIONAL DIVISORS between brane (interior)
 * and color (exterior).
 */
export default simulator({
  label: "sim:divisor-color-chart",
  title: "Divisor Visualization — Brings Cover on Riemann Sphere",
  html: "folio-assistant/simulators/divisor_color_chart.html",
  uses: [
    "def:color-tube-coordinates",
    "def:brings-surface",
    "def:briggs-klein-chart",
  ],
  tags: ["brings-surface", "color-tube", "divisor", "brane", "riemann-sphere", "torsion", "simulation"],
  defaultView: {
    name: "default",
    title: "Standard view ($q \\approx 1.1$)",
    params: {
      q: 1.1097,
      twistRate: 0.50,
      zMax: 8,
      braneRadius: 1.10,
      tubeOffset: 0.40,
      scale: "projective",
      tubeRadius: 0.07,
      showBrane: true,
      showTubes: true,
      showDivisors: true,
      showEnvelope: false,
      showProjection: false,
      autoRotate: true,
    },
  },
  views: [
    {
      name: "no-torsion",
      title: "Classical limit ($q = 1$)",
      params: {
        q: 1.0, twistRate: 0.50, zMax: 8,
        braneRadius: 1.10, tubeOffset: 0.40,
        scale: "projective", tubeRadius: 0.07,
        showBrane: true, showTubes: true, showDivisors: true,
        showEnvelope: false, showProjection: false, autoRotate: true,
      },
    },
    {
      name: "with-projection",
      title: "With $\\pi$ projection lines",
      params: {
        q: 1.1097, twistRate: 0.50, zMax: 8,
        braneRadius: 1.10, tubeOffset: 0.60,
        scale: "projective", tubeRadius: 0.06,
        showBrane: true, showTubes: true, showDivisors: true,
        showEnvelope: false, showProjection: true, autoRotate: false,
      },
    },
    {
      name: "high-torsion",
      title: "High torsion ($q = 1.8$)",
      params: {
        q: 1.8, twistRate: 0.50, zMax: 8,
        braneRadius: 1.10, tubeOffset: 0.40,
        scale: "projective", tubeRadius: 0.07,
        showBrane: true, showTubes: true, showDivisors: true,
        showEnvelope: false, showProjection: false, autoRotate: true,
      },
    },
  ],
});
