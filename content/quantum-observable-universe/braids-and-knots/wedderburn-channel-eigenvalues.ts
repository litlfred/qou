import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wedderburn-channel-eigenvalues",
  lean: {
    decl: "QOU.BraidsAndKnots.Stubs.wedderburn_channel_eigenvalues",
    file: "QOU/BraidsAndKnots/Stubs.lean",
    validation: "not_checked",
  },
  title:
    "Per-channel vertex volumes $\\hat{V}^{\\mathrm{sym/std/alt}}$ derived from $H_3(q)$ irrep matrices",
  uses: [
    "prop:three-parameters-wedderburn",
    "prop:tower-binding-energy",
    "thm:jones-markov-trace",
  ],
  tags: [
    "wedderburn",
    "hecke-algebra",
    "irrep-matrix",
    "vertex-volume",
  ],
});
