import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "caveat", date: "2026-11-16", body: "**Demoted to conjecture (owner, 2026-11-16).** The topological input is correct: the chain $\\mathcal{C}_N$ carries total linking number $N-1$ and the threaded ring $T(2,N)$ carries linking number $N/2$, the value of the reduced Alexander polynomial $\\tilde\\Delta$ at $t=1$. The claim that crossing energy is proportional to this weight has no derivation in the corpus, so the statement is a conjecture. Earlier text called $\\tilde\\Delta$ the Alexander polynomial; the true Alexander polynomial of a link with two or more components vanishes at $t=1$." },
  ],
  label: "conj:ring-closure-barrier",
  title: "Ring-closure energy barrier from braid rearrangement",
  tags: [
    "ring-closure",
    "energy-barrier",
    "braid",
    "rearrangement",
    "activation-energy",
    "topological",
    "crossing-energy",
  ],
  lean: { ref: "qou:QOU.Organic.alexanderWeightDifference",
    validation: "not_checked",
  },
  uses: ["def:molecular-hopf-ring"],
});
