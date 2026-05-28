import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:color-superconductivity-borromean",
  title:
    "Color superconductivity as Borromean-to-Hopf topological reconfiguration",
  lean: {
    ref: "qou:QOU.Archimedean.first_order_transition",
    validation: "not_checked",
  },
  tags: [
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
