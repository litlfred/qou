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
  uses: [
    // NOTE: there is no `def:octonion-algebra` in the corpus. The octonion
    // algebra and its automorphism group G_2 are used here but never defined
    // as a content block — recorded as a gap in §8 and bean qou-8fl1.
  ],
  // The ref now names a DECLARATION, not the module.
  //
  // What is backed: `sym2_dim_3` gives dim Sym²(V) = 6 at dim V = 3 — the
  // arithmetic of the "6 | Sym²(3) | no singlet ⇒ complex type" row of the
  // representation table below. That is all.
  //
  // What is NOT backed, and must not be read as machine-checked:
  //  - this block's headline (PSL(2,7) colour from the octonionic G₂ via the
  //    Fano plane) has no Lean formalisation anywhere in the corpus;
  //  - neither does the scope-(b) marked-pair obstruction the .md derives
  //    (S₄ has no orbit of size ≤ 2 on P², via absolute irreducibility of its
  //    3-dimensional representation) — that argument is verified in exact
  //    arithmetic by `s4_marked_pair_obstruction.py`, not in Lean;
  //  - the rest of QOU.Eightfold.Sym2Gate is vacuous — `su3_sym2_irreducible`
  //    is an `axiom … : True`, and the two gate "theorems" conclude
  //    arithmetic tautologies. Drain tracked as bean qou-8fl1 item 3; the
  //    module docstring records it at the point of use.
  //
  // The parity criterion that actually decides the Sym² gate is formalised
  // (sorry-free, real content) in QOU.Eightfold.Sym2GateParity. It is not
  // cited as this block's ref because it is a statement about SU(2) irreps,
  // not about the SU(3) fundamental this block invokes.
  lean: { ref: "qou:QOU.Eightfold.Sym2Gate.sym2_dim_3" },
});
