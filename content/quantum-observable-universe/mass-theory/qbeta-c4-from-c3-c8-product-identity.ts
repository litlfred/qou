import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-c4-from-c3-c8-product-identity",
  title:
    "c_4 = c_8 / c_3 via the structural product identity c_3 · c_4 = c_8",
  tags: [
    "qbeta",
    "c-4",
    "c-k",
    "product-identity",
    "j-hopf",
    "silver-ratio",
    "lean",
  ],
  lean: {
    ref: "qou:QOU.QBeta.c4_eq_c8_div_c3_at_silver",
    validation: "not_checked",
  },
  uses: ["prop:qbeta-c8-c10-silver-rationals"],
});
