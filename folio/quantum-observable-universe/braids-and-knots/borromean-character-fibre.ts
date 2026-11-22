import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:borromean-character-fibre",
  title: "Two values of the standard character determine the Borromean conjugacy class",
  lean: { ref: "qou:QOU.Mass.BorromeanSL2ZFibre.fibre_two_point" },
  uses: ["thm:borromean-word-minimal"],
  tags: ["borromean", "braid-word", "hecke-character", "sl2z", "lean-proved"],
});
