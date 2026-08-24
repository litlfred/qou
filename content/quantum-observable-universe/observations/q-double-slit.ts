import { simulator } from "../../../folio-assistant/schemas/builders";

/**
 * q-Deformed Double Slit — overhead diffraction particle simulator.
 *
 * Visualises individual particle arrivals through a q-deformed double slit,
 * showing how the substrate parameter q modifies the interference pattern
 * via the Reeb contraction term in the categorical Dirac operator.
 */
export default simulator({
  label: "sim:q-double-slit",
  title: "q-Deformed Double-Slit Simulator",
  html: "folio-assistant/simulators/q_double_slit.html",
  uses: [
    "prop:local-substrate-q",
    "def:categorical-dirac-operator",
    "def:localized-knot",
  ],
  tags: ["double-slit", "q-deformation", "scattering", "simulation"],
  defaultView: {
    name: "default",
    title: "Default: moderate q-deformation",
    params: {
      q: 1.1099785827513808,
      D: 0.5,
      d: 100,
      w: 50,
      lambda: 500,
      w0: 1.0,
      volK: 7.327724,
      torsion: 1.0,
      rate: 10,
      speed: 4,
    },
  },
  views: [
    {
      name: "classical",
      title: "Classical limit (q = 1)",
      params: {
        q: 1.0,
        D: 0.5,
        d: 100,
        w: 50,
        lambda: 500,
        w0: 1.0,
        volK: 0,
        torsion: 0,
        rate: 10,
        speed: 4,
      },
    },
    {
      name: "heavy-atom",
      title: "Heavy atom: large q-deformation",
      params: {
        q: 1.35,
        D: 0.5,
        d: 100,
        w: 50,
        lambda: 500,
        w0: 1.0,
        volK: 12.0,
        torsion: 2.5,
        rate: 10,
        speed: 4,
      },
    },
  ],
});
