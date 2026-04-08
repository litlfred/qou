import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-proton",
  label: "rem:meson-to-proton-via-borromean",
  title:
    "From meson to proton: Borromean composition and the energy scale $\\mathbf{E}_0$",
  tags: [
    "proton",
    "meson",
    "borromean",
    "energy-scale",
    "typed-crossings",
    "beta-decay",
    "formation-chain",
    "hecke-algebra",
    "computational-witness",
  ],
  uses: [
    "def:categorical-proton",
    "def:categorical-meson",
    "conj:borromean-quark",
    "rem:beta-decay-energy-scale",
  ],
});
