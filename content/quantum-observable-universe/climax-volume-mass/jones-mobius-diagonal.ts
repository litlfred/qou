import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:jones-mobius-diagonal",
  proofs: ["prf:jones-mobius-diagonal"],
  lean: {
    ref: "qou:QOU.Braiding.JonesMobiusDiagonal.markov_eq_mobius_contact",
    validation: "not_checked",
  },
  title: "Jones polynomial as the diagonal of the categorical Möbius kernel",
  uses: [
    "prop:mobius-energy",
    "lem:mobius-energy-frobenius-kernel",
    "thm:jones-markov-trace",
    "rem:mobius-surreal-renormalization",
  ],
  cites: ["freedman1994", "ohara1991"],
});
