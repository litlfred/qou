import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:mi-sw-abelianisation-cartan",
  lean: { ref: "qou:QOU.ArchimedeanUniverse.mi_sw_cartan_reduction",
    validation: "not_checked",
  },
  title: "Cartan reduction recovers the Seiberg--Witten differential",
  tags: ["weight-space", "cartan", "seiberg-witten-differential", "exceptional-divisor"],
  uses: ["rem:weight-space-decomposition", "rem:color-bundles"],
  proofs: ["prf:mi-sw-abelianisation-cartan"],
});
