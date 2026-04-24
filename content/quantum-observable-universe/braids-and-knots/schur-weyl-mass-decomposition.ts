import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:schur-weyl-mass-decomposition",
  title:
    "Schur–Weyl decomposition of the atomic mass trace",
  lean: {
    decl: "QOU.BraidKnot.schur_weyl_mass_decomposition",
    validation: "not_checked",
  },
  uses: [
    "thm:wedderburn-mass-formula",
    "prop:three-parameters-wedderburn",
    "prop:hook-weight-derivation",
    "thm:markov-trace-product",
    "prop:wigner-2-coefficient",
    "prop:hecke-mass-trace",
    "prop:markov-pair-z2",
    "prop:shell-schur-weyl-self-duality",
    "prop:gb-residue-spectral-sum",
    "def:atomic-braid",
  ],
  tags: [
    "schur-weyl",
    "wedderburn",
    "mass",
    "hook-product",
    "partition",
    "hecke-algebra",
  ],
});
