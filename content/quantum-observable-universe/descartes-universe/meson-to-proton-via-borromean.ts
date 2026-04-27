import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-proton",
  label: "rem:meson-to-proton-via-borromean",
  title:
    "Proton formation: three pair productions and the energy scale $\\mathbf{E}_0$",
  tags: [
    "proton",
    "baryon-number",
    "borromean",
    "energy-scale",
    "typed-crossings",
    "beta-decay",
    "formation-chain",
    "hecke-algebra",
    "computational-witness",
    "pair-production",
  ],
  uses: [
    "def:quark-antiquark-production",
    "rem:energy-scale-planck",
  ],
});
