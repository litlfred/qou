import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-parity-split",
  lean: {
    ref: "qou:QOU.Mass.evenPart_add_oddPart",
    validation: "validated",
  },
  title: "Binding (cosh) and β-decay (sinh) are the two bar-parities of one element",
  uses: [
    "prop:sl2-prolongation-recurrence",
    "def:bar-involution",
    "conj:binding-qbeta-complex-volume",
  ],
  proofs: ["prf:bar-parity-split"],
});
