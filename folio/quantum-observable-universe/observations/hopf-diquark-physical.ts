import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hopf-diquark-physical",
  title: "Borromean contrast and the CFL flavor-antisymmetric channel",
  interprets: "def:hopf-diquark",
  tags: [
    "diquark",
    "hopf",
    "cooper-pair",
    "color-superconductivity",
    "borromean",
  ],
  uses: ["def:hopf-diquark", "conj:borromean-quark"],
});
