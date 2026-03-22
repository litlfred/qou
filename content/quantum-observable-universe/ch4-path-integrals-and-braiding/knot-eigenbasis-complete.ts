import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-eigenbasis-complete",
  title: "Completeness of the knot-type eigenbasis",
  tags: ["braid-group", "hecke-algebra", "knot-invariant", "schur-weyl"],
  uses: ["prop:braid-action-tensor"],
  proofs: ["prf:knot-eigenbasis-complete"],
});
