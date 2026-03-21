import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:euler-char-stability",
  title: "Stability of the Euler characteristic",
  hasProof: true,
  tags: ["euler-characteristic", "brane-tower", "spectral-sequence"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:quantum-characteristic-classes",
    "prop:jet-prolongation",
  ],
});
