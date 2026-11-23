import { proof } from "../../schema/builders";

export default proof({
  label: "prf:shell-schur-weyl-self-duality",
  title: "Proof of shell schur weyl self duality",
  uses: ["prop:shell-schur-weyl-self-duality"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean.** Steps 1 and 3 are proved in the sibling file. Step 2 is cited." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This result refines [mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price) (which gives $y_\\lambda$ per partition) by characterising when the shell operator's coefficients are symmetric under transposition." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): It complements [skein-crossing-asymmetry](#prop:skein-crossing-asymmetry) (which encodes the parity-violation mechanism at level 3)." },
  ],
});
