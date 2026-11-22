import { remark } from "../../schema/builders";

export default remark({
  label: "rem:convention-d-chirality-side",
  title: "Convention D weighs the two eigenlines of a crossing unequally",
  interprets: "prop:markov-trace-frobenius-selection",
  uses: ["prop:convention-d-kills-antisymmetriser"],
  cites: ["jones1987", "wenzl1988"],
  tags: ["trace-convention", "chirality", "observation", "scope-a"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body:
        "Added on owner instruction (bean `qou-wkcd`, relayed by the coordinator of " +
        "epic `qou-qs0e`): record convention D's one-sidedness as the corpus home of the " +
        "left/right choice, as an observation about a ruled convention. The identification " +
        "with weak chirality is explicitly NOT made (scope (a)). Lean: " +
        "`QOU/QuarkState/ConventionDLineWeights.lean`, `LeftLineDefinition.lean`, " +
        "`WeakChiralityRootLabel.lean`. Probes: `corner_sl2_multiplicity_probe.py`, " +
        "`corner_sl2_weighted_persistence_probe.py`. Audit: " +
        "`docs/audits/2026-11-15-weak-chirality-doublet-singlet.md` §6–§7.",
    },
  ],
});
