import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borromean-quark",
  title:
    "Quarks as Borromean-linked unknots in the exceptional divisor",
  lean: {
    ref: "qou:QOU.Archimedean.BorromeanQuark",
    validation: "not_checked",
  },
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
    "def:neutrino-knot",
    "prop:bn-mtc-action",
  ],
});
