import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:genus-maximal-descent",
  lean: { ref: "qou:QOU.Archimedean.genus_maximal_descent",
    validation: "not_checked",
  },
  title: "Genus of the one-complex-dimensional descent",
  tags: ["archimedean-universe", "genus", "riemann-roch"],
  uses: [
    "def:archimedean-condition",
    "rem:three-euler-characteristics",
  ],
  proofs: ["prf:genus-maximal-descent"],
});
