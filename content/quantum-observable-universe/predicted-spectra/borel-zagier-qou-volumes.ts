import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borel-zagier-qou-volumes",
  title:
    "Rational linear independence of QOU hyperbolic volumes (Borel--Zagier)",
  lean: { ref: "qou:QOU.Archimedean.BorelZagierQouVolumes", validation: "stub" },
  tags: [
    "borel-regulator",
    "zagier-conjecture",
    "linear-independence",
    "hyperbolic-volume",
    "K-theory",
    "open-problem",
  ],
  uses: ["prop:single-volume-irrationality"],
  cites: ["borel1986", "borel1974"],
});
