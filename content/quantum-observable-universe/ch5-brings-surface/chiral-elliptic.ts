import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chiral-elliptic",
  title: "Chiral fibre as an elliptic curve",
  hasProof: true,
  uses: ["rem:braid-group-action", "rem:holonomy-trefoil"],
});
