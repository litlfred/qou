import { simulator } from "../../../folio-assistant/cat-harness/schemas/builders";

/**
 * Beta-Decay Half-Life Simulator.
 *
 * Interactive transfer-matrix computation of nuclear beta-decay
 * half-lives from the substrate parameter q alone.  Implements
 * the Level 0 Skein polynomial ratio (bare + shell correction)
 * and the exact Fermi phase-space integral with Skein-Coulomb
 * enhancement.
 */
export default simulator({
  label: "sim:beta-decay-halflife",
  title: "Beta-Decay Half-Life Simulator",
  html: "fsh-guts/deprecated/simulators/beta_decay_halflife.html",
  uses: ["cor:spectral-decomposition-qvalue"],
  tags: [
    "beta-decay",
    "half-life",
    "transfer-matrix",
    "skein-polynomial",
    "simulation",
  ],
  defaultView: {
    name: "default",
    title: "Tritium $\\beta^-$ decay at canonical $q$",
    params: {
      q: 1.110,
      nucleus: "3H",
      mode: "from-q",
      showShellCorrection: false,
    },
  },
  views: [
    {
      name: "carbon-14",
      title: "Carbon-14 $\\beta^-$ decay",
      params: {
        q: 1.110,
        nucleus: "14C",
        mode: "from-q",
        showShellCorrection: true,
      },
    },
    {
      name: "experimental-q",
      title: "Experimental $Q$-values (all benchmarks)",
      params: {
        q: 1.110,
        nucleus: "3H",
        mode: "from-Qexp",
        showShellCorrection: false,
      },
    },
  ],
});
