import { example } from "../../schema/builders";

export default example({
  label: "ex:tritium-decay-knot-equation",
  title:
    "Tritium decay as a Skein crossing change: ${}^3_1\\mathrm{H} \\to {}^3_2\\mathrm{He} + e^- + \\bar{\\nu}_e$",
  tags: [
    "tritium",
    "beta-decay",
    "skein-relation",
    "knot-equation",
    "worked-example",
    "helium-3",
    "borromean",
  ],
  uses: [
    "def:beta-decay-skein",
    "def:lepton-number-categorical",
    "def:categorical-proton",
    "def:categorical-neutron",
    "def:electron-knot",
    "def:neutrino-knot",
    "prop:nuclear-groebner-reduction",
    "thm:markov-trace-factorization",
  ],
});
