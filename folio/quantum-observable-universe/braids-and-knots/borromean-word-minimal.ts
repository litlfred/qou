import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:borromean-word-minimal",
  title: "The Borromean word is the shortest non-trivial pure zero-linking three-braid",
  lean: { ref: "qou:QOU.MassTheory.BorromeanWordForcing.minimal_pure_zeroLinking" },
  uses: ["def:f-bor-borromean-observable"],
  tags: ["borromean", "brunnian", "braid-word", "lean-proved"],
});
