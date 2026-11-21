import { conjecture } from "../../schema/builders";

/**
 * Working conjecture for the proton's /q^3.
 *
 * The factor q^{-3} in the normaliser c_sign = [3]_q! q^{-3} of F_Bor is the
 * derivative of the sign-block Markov trace tr_z(x_-) at the convention-D
 * point z_D, read in a coordinate tr(b), b = u sigma + v, that spans H_2 with
 * 1 over Z[q, q^{-1}] and is bar-invariant.
 *
 * Proved (Lean, sorry-free): such coordinates are exactly b = +-(sigma - q) + c
 * with c bar-invariant, so the derivative is +-q^{-3}; each condition is needed;
 * the same rule gives the trivial block's q^3. Not proved: that the observable
 * must be read in such a coordinate. Audit:
 * docs/audits/2026-11-21-proton-q3-kl-coordinate.md (PR #8964).
 */
export default conjecture({
  label: "conj:proton-normaliser-kl-coordinate",
  title:
    "The proton normaliser $q^{-3}$ as a derivative in an integral, bar-invariant coordinate",
  uses: ["def:f-bor-borromean-observable", "def:bar-involution"],
  cites: ["kazhdan-lusztig1979", "geer-patureau-mirand-turaev-2009"],
  tags: [
    "proton",
    "schur-element",
    "kazhdan-lusztig",
    "bar-involution",
    "modified-trace",
    "working-conjecture",
    "open-problem",
  ],
});
