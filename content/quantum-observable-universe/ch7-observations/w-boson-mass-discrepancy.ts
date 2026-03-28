import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:higgs-t28",
  label: "rem:w-boson-mass-discrepancy",
  title:
    "$W$ boson mass from $T(2,4)$ Skein polynomial at the CODATA substrate $q_0$",
  tags: [
    "W-boson",
    "mass",
    "CDF",
    "Fermilab",
    "discrepancy",
    "electroweak",
    "local-substrate",
    "prediction",
    "experimental",
    "Skein-polynomial",
  ],
  uses: [
    "conj:higgs-t28",
    "def:substrate-parameter",
    "def:crossing-energy",
    "def:quantum-planck-constant",
    "rem:skein-mass-relation",
    "prop:crossing-energy-decomposition",
    "rem:building-block-knots",
    "prop:local-substrate-q",
    "rem:half-life-as-q-probe",
    "rem:mass-comparison-table",
    "rem:c-substrate-via-levi",
    "prop:topological-mass-formula",
  ],
});
