import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-von-mangoldt-function",
  label: "rem:yekutieli-quantum-li",
  title: "The multiplicative integral as the quantum $\\mathrm{Li}(x)$",
  tags: ["exposition", "yekutieli", "logarithmic-integral", "stokes", "holonomy"],
  uses: [
    "conj:explicit-formula",
    "rem:yekutieli-stokes",
    "prop:yekutieli-lifting",
  ],
  cites: [
    "yekutieli2015",
  ],
});
