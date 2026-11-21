import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:flavor-split-substrate-mass",
  title: "The nucleon mass split equals the substrate flavor-split formula",
  tags: ["flavor-split", "u-d-splitting", "fitted-ansatz", "conjecture"],
  uses: [
    "prop:flavor-split-substrate",
    "lem:pair-skein-mass-formula",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "Split out of `prop:flavor-split-substrate` by owner ruling 2026-11-21 (issue #8922). " +
        "That proposition is now only the algebraic identity between the closed and factored forms. " +
        "This conjecture carries the physical identification, which rests on the per-quark ansatz of Step 2 of " +
        "`prf:flavor-split-substrate`, a fitted step with no derivation on record. " +
        "PR #8931 proves in Lean (`QOU.FlavorDressing.PivotSplitOrder.ansatz_ne_pivotSplit`) that no " +
        "additive-strand split with a power-of-$q$ nucleon ratio gives that ansatz. Open research: bean `qou-agc6`.",
    },
  ],
});
