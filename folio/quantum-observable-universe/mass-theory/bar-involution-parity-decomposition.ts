import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:bar-involution-parity-decomposition",
  lean: {
    ref: "qou:QOU.Mass.evenPart_add_oddPart",
    validation: "validated",
  },
  title: "Even/odd decomposition under a linear involution",
  uses: ["def:bar-involution"],
  proofs: ["prf:bar-involution-parity-decomposition"],
});
