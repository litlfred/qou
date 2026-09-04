import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:content-scaling-correspondence",
  title: "Content $c = m_j$ by Schur--Weyl: box content determines BW scaling",
  lean: { ref: "qou:QOU.BraidKnot.BoxContent.boxContent", validation: "not_checked" },
  uses: ["prop:knot-eigenbasis-complete", "rem:hecke-algebra-from-braiding"],
  authorNotes: [
    { kind: "status", date: "2026-09-04", body: "The mathematical sentence — content $c = j - i$ equals the magnetic quantum number $m_j$ of the corresponding $\\mathrm{SU}_q(2)$ weight space — is **refuted in its literal reading** by sorry-free Lean in the carrier `lean/QOU/BraidKnot/BoxContent.lean` (bean `qou-59x9`): for a two-row shape $(a,b)$ the cell count $a+b$ never equals the weight count $a-b+1$ (`twoRow_card_cells_ne_card_weights`), and for $a+b \\geq 3$ the cell $(0,a-1)$ has a content outside the weight set of $V_{(a,b)}$ under any box-to-weight assignment (`top_content_not_weight`); $(2,0)$ is the only shape where every content is a weight. What holds is that contents are the $q$-Jucys–Murphy eigenvalues (`QOU.SchurWeyl.QJucysMurphyEigen`), a total-spin datum. The scaling table is a physics dictionary, not a theorem. `lean.ref` still names the definition `boxContent`; re-wording the proposition (content = JM eigenvalue; table to a follow-on remark) is the owner's call and is not done here." },
  ],
  tags: ["schur-weyl", "content", "magnetic-quantum-number", "scaling", "braid-graph"],
});
