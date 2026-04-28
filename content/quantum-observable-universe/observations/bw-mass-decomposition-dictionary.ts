import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:schur-weyl-mass-decomposition",
  label: "rem:bw-mass-decomposition-dictionary",
  title:
    "Empirical Bethe–Weizsäcker terms as Schur–Weyl strata",
  tags: [
    "bethe-weizsacker",
    "schur-weyl",
    "mass-formula",
    "dictionary",
    "nuclear-physics",
    "interpretation",
  ],
  uses: [
    "prop:schur-weyl-mass-decomposition",
    "prop:gb-residue-spectral-sum",
    "prop:markov-pair-z2",
    "prop:shell-schur-weyl-self-duality",
    "prop:wigner-2-coefficient",
  ],
});
