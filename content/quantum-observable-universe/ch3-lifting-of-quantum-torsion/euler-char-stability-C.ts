import { proof } from "../../schema/builders";

export default proof({
  label: "prf:euler-char-stability-C",
  title: "Archimedean proof of Euler characteristic stability",
  uses: [
    "prop:euler-char-stability",
    "def:recursive-brane-tower",
    "def:quantum-characteristic-classes",
    "prop:jet-prolongation",
  ],
});
