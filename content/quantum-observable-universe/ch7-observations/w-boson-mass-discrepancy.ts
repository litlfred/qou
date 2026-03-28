import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:higgs-t28",
  label: "rem:w-boson-mass-discrepancy",
  title:
    "$W$ boson mass discrepancy: CDF~II vs.\\ Standard Model from substrate running",
  tags: [
    "W-boson",
    "mass",
    "CDF",
    "Fermilab",
    "discrepancy",
    "electroweak",
    "substrate-running",
    "prediction",
    "experimental",
  ],
  uses: [
    "conj:higgs-t28",
    "def:substrate-parameter",
    "def:crossing-energy",
    "def:quantum-planck-constant",
    "rem:skein-mass-relation",
    "prop:crossing-energy-decomposition",
    "rem:building-block-knots",
    "prop:em-coupling-projection",
    "rem:mass-comparison-table",
  ],
});
