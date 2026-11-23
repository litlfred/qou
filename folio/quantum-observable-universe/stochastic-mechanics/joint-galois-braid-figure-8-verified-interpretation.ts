import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:joint-galois-braid-figure-8-verified",
  label: "rem:joint-galois-braid-figure-8-verified-interpretation",
  title:
    "Structural triviality of the figure-8 cell and the remaining chiral-pair cases",
  uses: [
    "conj:joint-galois-braid-figure-8-verified",
    "conj:joint-galois-braid-action",
    "prop:b1-figure-8-row-theorem",
  ],
});
