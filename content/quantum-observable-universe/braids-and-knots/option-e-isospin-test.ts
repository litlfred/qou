import { remark } from "../../schema/builders";

export default remark({
  label: "rem:option-e-isospin-test",
  title:
    "Option E ($c_\\lambda$ Kashiwara crystal weight) and the $T = {}^3\\mathrm{He}$ isospin invariance",
  interprets: "prop:crystal-isospin-degeneracy",
  uses: [
    "prop:crystal-isospin-degeneracy",
    "prop:spin-involution-lp-dual-invariance",
    "rem:isospin-mass-split-em-localisation",
    "rem:lp-dual-isospin-invariance",
  ],
  tags: [
    "kashiwara-crystal",
    "option-e",
    "isospin",
    "tritium",
    "helium-3",
    "delta-i",
    "canonical-braid",
    "h-followup",
  ],
  cites: ["kashiwara1991", "lecouvey2007"],
});
