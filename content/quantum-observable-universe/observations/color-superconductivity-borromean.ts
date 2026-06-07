import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:color-superconductivity-borromean",
  title:
    "Color superconductivity as Borromean-to-Hopf topological reconfiguration",
  lean: {
    ref: "qou:QOU.Archimedean.first_order_transition",
    validation: "not_checked",
  },
  tags: [
    "tier:E",
    "color-superconductivity",
    "diquark",
    "cooper-pair",
    "borromean",
    "hopf",
    "CFL",
    "color-flavor-locking",
    "neutron-star",
  ],
  uses: [
    "prop:borromean-hopf-energy-crossover",
    "rem:deconfinement-golden-threshold",
  ],
  cites: [
    "alford1999",
  ],
});
