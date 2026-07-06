import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:gravity-spectral-prefactor",
  label: "rem:gravity-spectral-prefactor-interpretation",
  title: "Newton's $G$ as the macroscopic-stratum signature of the mass functional",
  tags: [
    "gravity",
    "newton-constant",
    "universal-residue",
    "plancherel",
    "macroscopic-stratum",
    "interpretation",
  ],
  uses: ["prop:gravity-spectral-prefactor"],
});
