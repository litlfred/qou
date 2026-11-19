import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:substrate-telescope",
  title: "Substrate Telescopes: vacuum isotropy null and non-vacuum state anisotropy",
  lean: {
    ref: "qou:QOU.Information.BarEvenVacuumDispersionAndLorentzParity.observer_covariant_modular_derivation_and_vacuum_null",
  },
  uses: [
    "def:frobenius-hopf-substrate",
    "def:substrate-parameter",
    "ex:q-reeb-flow",
  ],
  tags: ["detector", "substrate", "observation", "lorentz-invariance"],
});
