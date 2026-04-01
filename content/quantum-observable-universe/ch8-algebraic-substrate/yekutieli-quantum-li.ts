import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-von-mangoldt-function",
  label: "rem:yekutieli-quantum-li",
  title: "The Yekutieli integral as the quantum $\\mathrm{Li}(x)$",
  tags: ["exposition", "yekutieli", "logarithmic-integral", "stokes", "holonomy"],
  uses: [
    "def:q-von-mangoldt-function",
    "def:q-chebyshev-function",
    "prop:explicit-formula",
    "rem:yekutieli-stokes",
    "prop:yekutieli-lifting",
  ],
});
