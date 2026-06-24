import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:unit-modulus-eigenvalue",
  title:
    "Unit-modulus eigenvalues on $V_{(2,1)}$ and the Borromean fixed point",
  uses: [
    "prop:borromean-markov-trace-closed-form",
    "prop:hoefsmit-binding-amplitude",
  ],
  lean: { ref: "qou:QOU.BraidsAndKnots.borromean_eigenvalue_neg_one" },
  tags: [
    "eigenvalue",
    "unit-modulus",
    "borromean",
    "meson",
    "wedderburn",
    "standard-rep",
  ],
});
