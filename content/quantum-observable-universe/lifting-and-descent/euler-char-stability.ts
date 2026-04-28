import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:euler-char-stability",
  title: "Stability of the Euler characteristic",
  tags: ["euler-characteristic", "brane-tower", "frobenius-trace"],
  lean: { ref: "qou:QOU.Torsion.euler_char_constant",
    validation: "not_checked",
  },
  uses: ["def:quantum-characteristic-classes"],
  proofs: ["prf:euler-char-stability", "prf:euler-char-stability-C"],
});
