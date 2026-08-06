import { proposition } from "../../schema/builders";

/**
 * Color SU(3) from octonionic G₂ stabilization.
 *
 * Derives color SU(3) ⊂ G₂ = Aut(𝕆) via the Günaydin–Gürsey
 * decomposition 7 = 1 ⊕ 3 ⊕ 3̄. The 3/3̄ are complex conjugates
 * (non-self-dual), passing the Sym² gate that eliminates the
 * corpus's icosahedral T₁.
 *
 * ANTI-FITTING: The G₂ → SU(3) stabilizer is a theorem of
 * octonionic algebra (Günaydin–Gürsey 1973), not imported physics.
 * QOU's contribution is connecting this to the Bring surface / S₅
 * machinery via the McKay correspondence A₅ → E₈.
 */
export default proposition({
  label: "prop:color-su3-from-g2",
  title: "Color $\\mathrm{SU}(3)$ from octonionic stabilization",
  md: "color-su3-from-g2.md",
  uses: [
    // NOTE: there is no `def:octonion-algebra` in the corpus. The octonion
    // algebra and its automorphism group G_2 are used here but never defined
    // as a content block — recorded as a gap in §8 and bean qou-8fl1.
  ],
  lean: { ref: "qou:QOU.Eightfold.Sym2Gate" },
});
