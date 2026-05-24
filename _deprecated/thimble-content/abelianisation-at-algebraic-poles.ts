import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:abelianisation-at-algebraic-poles",
  title:
    "MI abelianises at algebraic denominator zeros, becoming the prolonged SW differential",
  lean: {
    ref: "qou:QOU.PicardLefschetz.abelianisation_at_algebraic_poles",
    validation: "not_checked",
  },
  uses: [
    "prop:mi-sw-abelianisation",
    "lem:mi-sw-abelianisation-cartan",
    "conj:denominator-zeros-as-sw-critical-points",
    "def:q-pochhammer-partial-product",
    "rem:brings-smoothness",
  ],
  cites: [
    "kashaev1997",
    "witten2011",
    "yekutieli2015",
  ],
  tags: [
    "seiberg-witten",
    "abelianisation",
    "cartan",
    "exceptional-divisor",
    "gauge",
    "open-problem",
  ],
});
