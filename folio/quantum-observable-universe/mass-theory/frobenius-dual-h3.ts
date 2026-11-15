import { definition } from "../../schema/builders";

export default definition({
  label: "def:frobenius-dual-h3",
  title: "Frobenius dual $K^\\vee$ in $H_3(q)$",
  lean: {
    ref: "qou:QOU.Archimedean.frobeniusDual",
    validation: "not_checked",
  },
  uses: ["prop:frobenius-gram-matrix"],
  cites: ["kassel1995"],
  tags: [
    "frobenius-dual",
    "gram-matrix",
    "hecke-algebra",
    "markov-trace",
    "non-degenerate",
  ],
});
