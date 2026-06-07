import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borel-zagier-qou-volumes",
  title:
    "Rational linear independence of QOU hyperbolic volumes (Borel--Zagier)",
  lean: { ref: "qou:QOU.Archimedean.BorelZagierQouVolumes", validation: "stub" },
  tags: [
    "tier:famous",
    "borel-regulator",
    "zagier-conjecture",
    "linear-independence",
    "hyperbolic-volume",
    "K-theory",
    "open-problem",
  ],
  uses: ["conj:single-volume-irrationality"],
  cites: ["borel1986", "borel1974"],
});
