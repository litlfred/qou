import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borromean-quark",
  title:
    "Quarks as Borromean-linked unknots in the exceptional divisor",
  tags: [
    "borromean",
    "quark",
    "unknot",
    "neutrino",
    "color-confinement",
    "exceptional-divisor",
    "hyperbolic-volume",
  ],
  uses: [
    "def:borromean-baryon",
    "def:neutrino-knot",
    "def:hadron",
    "def:crossing-energy",
    "prop:torus-knot-generators",
    "def:color-tube-coordinates",
    "sec:knot-notation-convention",
  ],
});
