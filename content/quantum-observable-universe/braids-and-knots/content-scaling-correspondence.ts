import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:content-scaling-correspondence",
  title: "Content $c = m_j$ by Schur--Weyl: box content determines BW scaling",
  lean: { decl: "QOU.BraidKnot.content_scaling", validation: "not_checked" },
  uses: ["prop:knot-eigenbasis-complete", "rem:hecke-algebra-from-braiding"],
  tags: ["schur-weyl", "content", "magnetic-quantum-number", "scaling", "braid-graph"],
});
