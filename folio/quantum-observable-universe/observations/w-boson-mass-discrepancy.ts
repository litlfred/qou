import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:local-substrate-q",
  label: "rem:w-boson-mass-discrepancy",
  title:
    "Electroweak boson masses from vertex $\\delta q$ at the CODATA aether",
  tags: [
    "W-boson",
    "Z-boson",
    "Higgs",
    "mass",
    "CDF",
    "Fermilab",
    "ATLAS",
    "CMS",
    "discrepancy",
    "electroweak",
    "local-substrate",
    "q-distortion",
    "prediction",
    "experimental",
    "Skein-polynomial",
    "Markov-trace",
    "Gauss--Bonnet",
    "Euler-characteristic",
  ],
  uses: [
    "rem:half-life-as-q-probe",
    "rem:mass-comparison-table",
  ],
});
