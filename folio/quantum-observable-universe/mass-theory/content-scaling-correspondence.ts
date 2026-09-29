import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:content-scaling-correspondence",
  title: "Box content is the $q$-Jucys--Murphy eigenvalue exponent",
  lean: { ref: "qou:QOU.SchurWeyl.SeminormalRep.seminormalRep_qJM", validation: "not_checked" },
  uses: ["prop:knot-eigenbasis-complete", "rem:hecke-algebra-from-braiding"],
  cites: ["jimbo1986", "ram1997"],
  authorNotes: [
    { kind: "status", date: "2026-09-04", body: "Re-worded (bean `qou-kpx7`, on the owner's go after PR #6600). Until 2026-09-04 the statement read *content $c = j - i$ equals the magnetic quantum number $m_j$ of the corresponding $\\mathrm{SU}_q(2)$ weight space* and `lean.ref` named the definition `boxContent`. That sentence is refuted, sorry-free, in `lean/QOU/BraidKnot/BoxContent.lean` (`twoRow_card_cells_ne_card_weights`, `top_content_not_weight`: for a two-row shape the box count never equals the weight count, and for three or more boxes a content lies outside the weight set under any assignment; $(2,0)$ is the only shape where every content is a weight). The statement now carried is the true one, `QOU.SchurWeyl.SeminormalRep.seminormalRep_qJM` (Ram 1997 Thm 4.1 for this construction): the $q$-Jucys–Murphy element acts on the seminormal basis by $q^{2\\cdot\\mathrm{content}}$. The BW scaling table that used to sit in this block is a physics dictionary, not a theorem, and moved to `rem:content-scaling-dictionary`." },
  ],
  tags: ["schur-weyl", "content", "magnetic-quantum-number", "scaling", "braid-graph"],
});
