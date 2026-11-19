import { proof } from "../../schema/builders";

export default proof({
  label: "prf:genus-maximal-descent",
  title: "Proof of Genus of the one-complex-dimensional descent",
  uses: [
    "prop:genus-maximal-descent",
    "rem:three-euler-characteristics",
  ],
});
