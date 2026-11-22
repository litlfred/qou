import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-q-aj-machinery-identification",
  title: "$\\Phi_q$ / $\\mathrm{Li}_2^q$ machinery is the AJ-conjecture machinery",
  lean: {
    ref: "qou:QOU.BraidKnot.PhiQAJMachineryIdentification.phi_q_li2_q_unified_via_aj",
    validation: "not_checked",
  },
  uses: [
    "conj:quantum-langlands-dual",
    "conj:dim-master-pentagon",
    "rem:dilog-saddle-regime",
  ],
  cites: [
    "garoufalidis2004",
    "faddeev1995",
    "kashaev1997",
    "murakami-murakami2001",
    "champanerkar2003",
    "arxiv-hep-th-0306165v1",
    "dimofte-gukov2010",
    "hikami2006",
    "takata2004",
  ],
  tags: [
    "aj-conjecture",
    "phi-q-faddeev",
    "li-2-q-rogers",
    "quantum-a-polynomial",
    "minimal-archimedean",
    "conditional-class-3b-cond",
  ],
});
