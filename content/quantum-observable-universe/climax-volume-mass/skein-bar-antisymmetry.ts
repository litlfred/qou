import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-bar-antisymmetry",
  proofs: ["prf:skein-bar-antisymmetry"],
  title:
    "Skein relation $L_+ - L_- = (q - q^{-1})\\,L_0$ is bar-antisymmetric",
  tags: [
    "skein-relation",
    "hecke-algebra",
    "bar-involution",
    "skew-symmetry",
    "crossing",
    "jones-polynomial",
  ],
  lean: {
    ref: "qou:QOU.BraidsAndKnots.SkeinBarAntisymmetry.skein_bar_antisymmetry",
    validation: "not_checked",
  },
  uses: ["def:bar-involution"],
});
