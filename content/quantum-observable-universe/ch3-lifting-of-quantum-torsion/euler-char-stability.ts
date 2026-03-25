import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:euler-char-stability",
  title: "Stability of the Euler characteristic",
  tags: ["euler-characteristic", "brane-tower", "frobenius-trace"],
  lean: {
    decl: "QOU.Torsion.euler_char_constant",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:quantum-characteristic-classes",
    "prop:jet-prolongation",
  ],
  proofs: ["prf:euler-char-stability", "prf:euler-char-stability-C"],
});
