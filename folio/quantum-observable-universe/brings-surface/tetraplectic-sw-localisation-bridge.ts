import { conjecture } from "../../schema/builders";

/**
 * Conjectural bridge: evaluate a tetraplectic matrix element combinatorially.
 *
 * In Seiberg–Witten theory the masses of BPS states and binding matrix
 * elements are integrals over the 4-manifold, and instanton path integrals
 * localize (Nekrasov) at fixed points classified by tuples of Young tableaux.
 * The Bring cone is a 4-manifold whose invariant measure already resolves
 * L²(M, Ω) into S₅ isotypic pieces indexed by partitions of 5.
 *
 * The suggestion is that the two indexings are the same indexing, so an
 * integral ∫_M ψ_λ* H ψ_μ Ω can be replaced by Clebsch–Gordan data of S₅ via
 * Schur's lemma and Wigner–Eckart. That would be the continuous-to-discrete
 * bridge the rest of the framework assumes; it is not established here.
 */
export default conjecture({
  label: "conj:tetraplectic-sw-localisation-bridge",
  title:
    "Combinatorial evaluation of tetraplectic matrix elements by $S_5$ localization",
  // The Askey conjecture is a SIBLING claim over the same measure, not a
  // premise of this one; edging to it as well as to the definition made the
  // definition edge transitively redundant (`uses-editorial-hygiene`). A
  // reader needs the measure and the isotypic decomposition, nothing else.
  uses: ["def:bring-cone-tetraplectic-structure"],
  lean: {
    ref: "qou:QOU.BringsSurface.TetraplecticSWLocalisationBridge",
    validation: "leanok",
  },
  cites: ["seiberg-witten1994b", "nekrasov2002"],
  tags: [
    "tetraplectic",
    "seiberg-witten",
    "localization",
    "wigner-eckart",
    "clebsch-gordan",
    "bring-cone",
    "open-problem",
    "conjectural-framing",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-24",
      body:
        "**A bridge that is asserted, not built.** Promoted from " +
        "`bring_tetraplectic.md` §3, which stated it as a suggestion. The " +
        "gap is precise: Nekrasov localization indexes fixed points by tuples " +
        "of Young tableaux for the *gauge group's* instanton moduli, while " +
        "the $S_5$ decomposition here indexes partitions of $5$ coming from " +
        "the curve's automorphisms. Nothing yet identifies the two indexings, " +
        "and until something does, the Wigner–Eckart step has no carrier.",
    },
  ],
});
