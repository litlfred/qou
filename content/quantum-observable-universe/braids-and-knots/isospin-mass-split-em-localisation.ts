import { remark } from "../../schema/builders";

export default remark({
  label: "rem:isospin-mass-split-em-localisation",
  title: "Mirror-isobar mass split lives outside the spin-/sign-invariant sector",
  interprets: "prop:crystal-isospin-degeneracy",
  uses: [
    "prop:crystal-isospin-degeneracy",
    "prop:spin-involution-lp-dual-invariance",
    "rem:lp-dual-isospin-invariance",
    "def:coulomb-charge",
  ],
  tags: [
    "isospin",
    "tritium",
    "helium-3",
    "mass-split",
    "coulomb",
    "electromagnetic",
    "localisation",
    "structural-impossibility",
  ],
});
