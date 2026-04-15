import { example } from "../../schema/builders";

export default example({
  label: "ex:half-life-shell-worked",
  title:
    "Shell structure in half-lives: ${}^3\\mathrm{H}$ and ${}^{14}\\mathrm{C}$ as worked examples",
  tags: [
    "half-life",
    "shell-correction",
    "tritium",
    "carbon-14",
    "matrix-element",
    "skein-factorization",
    "mirror-transition",
  ],
  uses: [
    "ex:hadron-half-life-verification",
    "conj:skein-shell-correction",
    "prop:hadron-q-self-correction",
    "prop:skein-coulomb-enhancement",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/half-life-shell-worked-0.svg", blockIndex: 0, hash: "a434e44f9b8d" },
  ],

});
