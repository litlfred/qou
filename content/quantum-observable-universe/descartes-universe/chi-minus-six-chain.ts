import { example } from "../../schema/builders";

export default example({
  label: "ex:chi-minus-six-derivation",
  title: "Why $\\chi(A) = -6$: the complete derivation chain",
  interprets: "def:descartes-condition",
  uses: [
    "def:descartes-condition",
    "prop:euler-char-stability",
  ],
  tags: ["descartes", "chi", "derivation", "example"],
});
