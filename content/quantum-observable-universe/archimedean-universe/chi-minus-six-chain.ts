import { example } from "../../schema/builders";

export default example({
  label: "ex:chi-minus-six-derivation",
  title: "$\\chi(A) = -6$: complete derivation chain",
  interprets: "def:descartes-condition",
  uses: [
    "def:descartes-condition",
    "prop:euler-char-stability",
    "def:motivic-substrate",
    "rem:kummer-tower",
  ],
  tags: ["descartes", "chi", "derivation", "example", "motivic-galois"],
});
