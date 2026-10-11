import { simulator } from "../../schema/builders";

/**
 * Double-Slit Analytical View — intensity pattern plotter.
 *
 * Plots the analytical intensity envelope for the q-deformed double-slit
 * experiment, comparing two scattering modes (massive particle and photon)
 * and overlaying experimental data from Bach et al. 2013.
 */
export default simulator({
  label: "sim:double-slit-analytical",
  title: "Double-Slit Analytical Simulator",
  html: "simulators/double_slit_simulator.html",
  uses: [
    "prop:local-substrate-q",
    "def:categorical-dirac-operator",
    "prop:variational-equations",
  ],
  tags: ["double-slit", "q-deformation", "analytical", "simulation"],
  defaultView: {
    name: "default",
    title: "Bach 2013 electrons (600 eV)",
    params: {
      q: 1.020,
      a: 50,
      d: 280,
      lambda: 50,
      reebRatio: 0.1,
      showStandard: true,
      showEnvelope: false,
      showBachData: true,
    },
  },
  views: [
    {
      name: "fullerene",
      title: "$\\mathrm{C}_{60}$ fullerene",
      params: {
        q: 1.15,
        a: 50,
        d: 280,
        lambda: 2.5,
        reebRatio: 0.25,
        showStandard: true,
        showEnvelope: true,
        showBachData: false,
      },
    },
    {
      name: "classical",
      title: "Classical limit ($q = 1$)",
      params: {
        q: 1.0,
        a: 50,
        d: 280,
        lambda: 50,
        reebRatio: 0,
        showStandard: true,
        showEnvelope: false,
        showBachData: false,
      },
    },
    {
      name: "visible-photon",
      title: "Visible photon ($\\lambda = 500\\,\\mathrm{nm}$)",
      params: {
        q: 1.005,
        a: 100,
        d: 500,
        lambda: 500,
        reebRatio: 0.05,
        showStandard: true,
        showEnvelope: true,
        showBachData: false,
      },
    },
  ],
});
