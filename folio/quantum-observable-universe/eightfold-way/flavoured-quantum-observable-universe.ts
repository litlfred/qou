import { definition } from "../../schema/builders";

/**
 * The flavour fundamental W as an axiom datum.
 *
 * Owner ruling 2026-11-27 (bean qou-j3w6, option A; supersedes owner
 * decision 4d of 2026-10-10): keep condition (iii) of
 * def:quantum-observable-universe (Λ²V ≅ 1, N = 2) and add a second
 * fundamental W with Λ³W ≅ 1 and no invariant self-pairing.
 *
 * This POSTULATES flavour SU(3); it does not derive it. Every result that
 * consumes this block is a consequence of the extended axioms.
 */
export default definition({
  label: "def:flavoured-quantum-observable-universe",
  title: "Flavoured quantum observable universe",
  defines: ["flavoured-quantum-observable-universe", "flavour-fundamental"],
  uses: ["def:quantum-observable-universe", "prop:schur-weyl-eightfold"],
  lean: {
    ref: "qou:QOU.FlavouredQuantumObservableUniverse",
  },
  tags: ["eightfold", "flavour", "axiom-datum", "volume-form"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Owner ruling 2026-11-27 (qou-j3w6 option A). Axiom datum, not a " +
        "derivation: flavour SU(3) is postulated through W.",
    },
  ],
});
