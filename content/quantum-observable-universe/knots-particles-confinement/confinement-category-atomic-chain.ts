import { example } from "../../schema/builders";

/**
 * The quark → nucleon → atom → neutral atom → molecule chain as a
 * composite morphism in the confinement category.
 */
export default example({
  label: "ex:confinement-category-atomic-chain",
  title: "The atomic chain in $\\mathbf{Conf}$",
  interprets: "def:confinement-category",
  uses: ["def:confinement-category"],
  tags: [
    "confinement",
    "category",
    "atomic-chain",
    "morphism",
  ],
});
