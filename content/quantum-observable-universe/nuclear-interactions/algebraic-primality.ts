import { definition } from "../../schema/builders";

export default definition({
  label: "def:algebraic-primality",
  title: "Algebraic primality of a strand count",
  lean: {
    ref: "qou:QOU.Interactions.AlgebraicPrimality.IsAlgebraicallyPrime",
    validation: "not_checked",
  },
  uses: [],
  tags: [
    "magic-numbers",
    "primality",
    "tensor-irreducibility",
    "confinement-sdp",
    "naming",
  ],
});
