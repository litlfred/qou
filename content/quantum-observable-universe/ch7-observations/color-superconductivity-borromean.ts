import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:color-superconductivity-borromean",
  title:
    "Color superconductivity as Borromean-to-Hopf topological reconfiguration",
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
    "conj:borromean-quark",
    "prop:strangelet-crossing-energy",
    "rem:deconfinement-golden-threshold",
    "def:crossing-energy",
  ],
});
