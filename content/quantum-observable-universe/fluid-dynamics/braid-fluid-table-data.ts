import { table } from "../../schema/builders";

export default table({
  label: "tbl:braid-fluid-table-data",
  title: "Hecke-product reduction table for vortex pair collisions",
  caption:
    "Nine elementary Hecke products from a two-vortex collision " +
    "(3-term photon NF $\\times$ 3-term photon NF), showing the " +
    "algebraic product and its Hecke reduction. The linking " +
    "channels $L_+$, $L_-$ arise from cross-polarisation terms.",
  uses: ["rem:braid-fluid"],
  tags: ["braid-fluid", "hecke-product", "vortex-collision"],
});
