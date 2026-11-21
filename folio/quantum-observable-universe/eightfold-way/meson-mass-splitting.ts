import { remark } from "../../schema/builders";

/**
 * Meson mass splitting via q-deformation.
 *
 * Explains how the crossing energy E_×(q) and quantum dimensions
 * split the mass degeneracy of the meson octet. The hexagonal
 * weight pattern is q-independent; the dynamics (mass, transitions)
 * are q-dependent.
 *
 * ANTI-FITTING: The Gell-Mann-Okubo relation is stated as an
 * open cross-check, not claimed as derived. Conditional on N=3 and Y.
 */
export default remark({
  label: "rem:meson-mass-splitting",
  title: "Meson mass splitting from q-deformed dynamics",
  interprets: "prop:meson-octet-decomposition",
  // Lean backs the NEGATIVE result: GMO is an identity of the first-order
  // octet ansatz and therefore cannot discriminate between mechanisms. It does
  // NOT back any derivation of the splitting — see bean qou-8pl2.
  // The ref now names a DECLARATION, not the module. `gmo_cannot_discriminate`
  // is the negative result stated above: two different breaking parameter sets
  // (a,b,c) and (a',b',c') both satisfy GMO, so the relation cannot select
  // between mechanisms.
  lean: {
    ref: "qou:QOU.Eightfold.GellMannOkuboIdentity.gmo_cannot_discriminate",
  },
  uses: [
    "prop:a2-from-three-strands",
    "rem:q-deformation-weight-lattice",
    "prop:meson-octet-decomposition",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is proved over any commutative ring in\n`QOU/Eightfold/GellMannOkuboIdentity.lean`\n, together with the sharper consequence\n`gmo_cannot_discriminate`: two arbitrarily" },
  ],
});
