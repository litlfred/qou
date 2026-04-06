import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:braid-twist-flip",
  label: "rem:rho-s3-holonomy-exposition",
  title: "The $\\rho$ representation as $S_3$ holonomy",
  tags: ["exposition", "holonomy", "s3", "chiral-sheets", "lagrange-resolvents"],
  uses: [
    "def:braid-twist-flip",
    "def:su2-generators",
    "rem:holonomy-trefoil",
    "prop:lagrange-resolvent-transform",
  ],
});
