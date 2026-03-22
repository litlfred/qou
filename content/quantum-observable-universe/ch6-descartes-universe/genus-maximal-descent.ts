import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:genus-maximal-descent",
  title: "Genus of the one-complex-dimensional descent",
  tags: ["descartes-universe", "genus", "riemann-roch"],
  uses: [
    "def:descartes-condition",
  ],
  proofs: ["prf:genus-maximal-descent"],
});
