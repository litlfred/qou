import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:mi-sw-abelianisation-cartan",
  title: "Cartan reduction recovers the SW differential",
  lean: {
    ref: "qou:QOU.ArchimedeanUniverse.mi_sw_cartan_reduction",
    validation: "not_checked",
  },
  uses: [
    "rem:brings-smoothness",
    "rem:weight-space-decomposition",
    "rem:coral-bundles",
  ],
  proofs: ["prf:mi-sw-abelianisation-cartan"],
  tags: [
    "seiberg-witten",
    "abelianisation",
    "cartan-reduction",
    "exceptional-divisor",
    "spectral-curve",
  ],
});
