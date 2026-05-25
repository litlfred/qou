import { table } from "../../schema/builders";

export default table({
  label: "tbl:breit-wheeler-pair-production-table-data",
  title: "Breit-Wheeler pair-production Hecke product table",
  caption:
    "Nine elementary Hecke products from a two-photon collision " +
    "(3-term photon NF $\\times$ 3-term photon NF), showing the " +
    "algebraic product and its Hecke reduction into output channels " +
    "($\\gamma$, $\\sigma_0$, $\\sigma_1$, $L_+$, $L_-$).",
  uses: ["def:breit-wheeler-pair-production"],
  tags: ["breit-wheeler", "pair-production", "hecke-product"],
});
