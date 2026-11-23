import { simulator } from "../../schema/builders";

/**
 * Double-Slit Analytical View — intensity pattern plotter.
 *
 * Plots the analytical intensity envelope for the q-deformed double-slit
 * experiment, comparing two scattering modes (massive particle and photon)
 * and overlaying experimental data from Bach et al. 2013.
 */
export default simulator({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Bean qou-x9tm: retired the un-derived default slider claim q = 1.020 under NO FITTING, EXCEPT CAL-1/2/3. Aperture-averaged wall-grazing evaluation at 80 working dps (50 dps serialized, proton pin, zero float64) in `computations/probes/double_slit_wall_grazing_q_local/double_slit_wall_grazing_q_local_probe.py` (`double_slit_wall_grazing_q_local_probe.witness.json`) gives <q_local - 1>_{a=50 nm} = 6.2195832e-9 (pion Yukawa r_pi) to 1.6987700e-6 (electron reduced Compton lambda_bar_{C,e}) even at saturating wall amplitude q_0 - 1, 4 to 6 orders of magnitude below 0.020.",
    },
  ],
  label: "sim:double-slit-analytical",
  title: "Double-Slit Analytical Simulator",
  html: "simulators/double_slit_simulator.html",
  uses: [
    "prop:local-substrate-q",
    "def:categorical-dirac-operator",
    "prop:variational-equations",
  ],
  cites: ["bach2013"],
  computation: {
    engine: "mpmath",
    script:
      "computations/probes/double_slit_wall_grazing_q_local/double_slit_wall_grazing_q_local_probe.py",
    witness:
      "computations/probes/double_slit_wall_grazing_q_local/double_slit_wall_grazing_q_local_probe.witness.json",
    status: "verified",
  },
  tags: ["double-slit", "q-deformation", "analytical", "simulation"],
  defaultView: {
    name: "default",
    title: "Bach 2013 electrons (600 eV)",
    params: {
      q: 1.0,
      a: 50,
      d: 280,
      lambda: 50,
      reebRatio: 0,
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
