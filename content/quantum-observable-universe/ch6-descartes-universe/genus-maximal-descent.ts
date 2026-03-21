import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:genus-maximal-descent",
  title: "Genus of the one-complex-dimensional descent",
  hasProof: true,
  tags: ["descartes-universe", "genus", "riemann-roch"],
  uses: [
    "def:descartes-condition",
  ],
});
