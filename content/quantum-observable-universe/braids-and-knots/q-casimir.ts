import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-casimir",
  title: "The $q$-Casimir element of $\\mathcal{U}_q(\\mathfrak{su}(2))$",
  tags: [
    "casimir",
    "quantum-group",
    "su-q-2",
    "central-element",
    "hopf-algebra",
    "q-deformed",
  ],
  lean: { ref: "qou:QOU.QCasimir",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-su2",
  ],
  cites: ["kassel1995", "lusztig1993"],
});
