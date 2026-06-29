import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-bsd-classical-limit",
  title:
    "$q$-BSD across $\\mathbb{P}^1$, the Kummer obstruction, and the classical limit",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "def:categorical-mordell-weil",
    "prop:root-of-unity-truncation",
    "prop:ns-kummer-specialisation",
    "rem:substrate-gm-torsion",
  ],
  tags: [
    "birch-swinnerton-dyer",
    "millennium-problem",
    "kummer",
    "gm-torsion",
    "projective-line",
    "classical-limit",
    "l-function",
  ],
});
