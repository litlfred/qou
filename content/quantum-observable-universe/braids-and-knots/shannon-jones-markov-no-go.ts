import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shannon-jones-markov-no-go",
  title:
    "The Jones--Markov measure $p_q(\\lambda) = y_\\lambda \\, d_\\lambda$ cannot serve as the Shannon probability for $n \\geq 4$",
  lean: {
    ref: "qou:QOU.BraidKnot.shannon_jones_markov_no_go",
    validation: "not_checked",
  },
  proofs: ["prf:shannon-jones-markov-no-go"],
  uses: [
    "rem:y-lambda-sign-pattern",
    "conj:tau-codim-shannon",
    "thm:frobenius-codim-universal",
  ],
  cites: ["kassel1995"],
  tags: [
    "shannon",
    "jones-markov",
    "y-lambda",
    "no-go",
    "sign-indefinite",
    "conjecture-refinement",
  ],
});
