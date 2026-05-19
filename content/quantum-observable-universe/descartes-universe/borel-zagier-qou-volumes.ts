import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borel-zagier-qou-volumes",
  title:
    "Rational linear independence of QOU hyperbolic volumes (Borel--Zagier)",
  lean: { ref: "qou:QOU.Descartes.BorelZagierQouVolumes", validation: "stub" },
  tags: [
    "borel-regulator",
    "zagier-conjecture",
    "linear-independence",
    "hyperbolic-volume",
    "K-theory",
    "open-problem",
  ],
  uses: ["conj:single-volume-irrationality"],
});
