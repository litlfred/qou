import { example } from "../../schema/builders";

export default example({
  label: "ex:chi-minus-six-derivation",
  title: "$\\chi(A) = -6$: complete derivation chain",
  interprets: "def:archimedean-condition",
  uses: [
    "def:archimedean-condition",
    "def:motivic-substrate",
    "prop:euler-char-stability",
    "rem:kummer-tower",
    "thm:motivic-perpetual-obstruction",
  ],
  tags: ["descartes", "chi", "derivation", "example", "motivic-galois"],
});
