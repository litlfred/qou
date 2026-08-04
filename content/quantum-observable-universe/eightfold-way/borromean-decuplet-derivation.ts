import { proposition } from "../../schema/builders";

/**
 * Borromean decuplet derivation.
 *
 * Connects the Schur-Weyl decuplet (symmetric partition (3) at N=3)
 * to the Borromean baryon structure from Chapter 9. The fully symmetric
 * channel of 3⊗3⊗3 gives the 10-dimensional decuplet, realized
 * topologically by three quark-unknots in the Borromean link.
 *
 * ANTI-FITTING: conditional on N=3 (the chapter's central open problem).
 * At N=2, the symmetric channel gives only a quadruplet.
 */
export default proposition({
  label: "prop:borromean-decuplet",
  title: "The baryon decuplet as symmetric Borromean channel",
  md: "borromean-decuplet-derivation.md",
  uses: [
    "prop:schur-weyl-eightfold",
    "def:borromean-baryon",
  ],
});
