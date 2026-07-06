import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-q-aj-machinery-identification",
  title: "$\\Phi_q$ / $\\mathrm{Li}_2^q$ machinery is the AJ-conjecture machinery",
  lean: {
    ref: "qou:QOU.BraidKnot.PhiQAJMachineryIdentification",
    validation: "not_checked",
  },
  uses: [
    "conj:quantum-langlands-dual",
    "conj:dim-master-pentagon",
  ],
  cites: [
    "garoufalidis2004",
    "faddeev1995",
    "kashaev1997",
    "murakami-murakami2001",
    "champanerkar2003",
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
