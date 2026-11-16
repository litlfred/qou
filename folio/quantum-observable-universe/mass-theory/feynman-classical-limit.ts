import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:feynman-classical-limit",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.ClassicalLimitDegeneration",
    validation: "not_checked",
  },
  title: "Classical limit: recovery of the symmetric path integral",
  tags: ["path-integral", "feynman", "classical-limit", "hecke-degeneration"],
  uses: [
    "prop:feynman-categorical-trace",
    "def:q-energy",
    "conj:classical-limit-stpart",
  ],
  proofs: [],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "Item 2 previously said z → 0 and that tr_M degenerates to the augmentation ε. Both were wrong: under convention D, z(1) = 1/2 and the limit trace is 2^{-(n-c(w))}; ε is the z = 1 trace and z → 0 gives δ_{w,1}. Item 5 said every closure becomes the unknot; the value depends on the number of components. Still open for the weak-proofs pass: the class `ClassicalLimitStpart` asserts only that a constant function ℕ → ℝ equal to 1 exists, which is trivially true and carries none of the conjecture's content.",
    },
  ],
});
