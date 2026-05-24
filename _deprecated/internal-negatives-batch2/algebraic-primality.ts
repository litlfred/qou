import { definition } from "../../schema/builders";

export default definition({
  label: "def:algebraic-primality",
  title:
    "Algebraic primality of $n$ at substrate $q$",
  lean: {
    ref: "qou:QOU.Interactions.AlgebraicPrimality.IsAlgebraicallyPrime",
    validation: "not_checked",
  },
  uses: [
    "prop:confinement-sdp",
    "prop:operator-selection-lp",
  ],
  cites: [
    "mathas1999",
    "kassel1995",
  ],
  tags: [
    "magic-numbers",
    "primality",
    "tensor-product",
    "irreducibility",
    "sdp",
    "definition",
  ],
});
