import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wedderburn-bratteli-recursion",
  proofs: ["prf:wedderburn-bratteli-recursion"],
  title:
    "Wedderburn--Bratteli recursion for Jones--Markov weights $y_\\lambda$ at $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.wedderburn_bratteli_recursion",
    validation: "not_checked",
  },
  uses: [
    "prop:alpha-k-derivation-procedure",
    "prop:explicit-alpha-k-h3",
  ],
  tags: [
    "wedderburn",
    "bratteli",
    "recursion",
    "jones-markov",
    "y-lambda",
    "q-content",
    "hoefsmit",
    "structural-derivation",
  ],
});
