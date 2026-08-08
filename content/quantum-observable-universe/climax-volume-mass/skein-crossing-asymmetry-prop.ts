import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-crossing-asymmetry",
  title: "Crossing asymmetry and per-crossing Coulomb correction",
  tags: ["skein", "crossing", "coulomb", "asymmetry", "r-matrix"],
  lean: { ref: "qou:QOU.Braiding.skein_crossing_asymmetry",
    validation: "not_checked",
  },
  uses: ["def:coulomb-charge"],
  authorNotes: [
    {
      kind: "status",
      body: "The companion Lean `skein_crossing_asymmetry` currently encodes a placeholder (`: True`); the intended statement ($q > 1 \\Rightarrow \\tfrac{1}{2}(q - q^{-1}) > 0$) is sketched in-file and deferred via `sorry` (`-- Ref: [manuscript]`).",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**Triaged clean, one sign gloss fixed.** Swept during the " +
        "`def:coulomb-charge` decomposition-correction propagation. The block's " +
        "math is unaffected: its ratio $(q - q^{-1})/(q + q^{-1})$ is a ratio of " +
        "*per-crossing* weights, which carries no multiplicity factor, so it needs " +
        "none of the $m = 0$ qualification the channel-total ratio does. " +
        "$\\delta_{\\mathrm{Coulomb}} = q - \\tfrac{1}{2}(q + q^{-1}) = " +
        "\\tfrac{1}{2}(q - q^{-1})$ is also exactly consistent with the corrected " +
        "split, since $\\tfrac{1}{2}(q + q^{-1})$ is the (signed) bar-even weight " +
        "of a positive crossing. Only the opening gloss was fixed: it said the " +
        "Skein relation gives a negative crossing “a weight of $q^{-1}$”, " +
        "dropping the sign that the displayed relation immediately below it and " +
        "`def:crossing-energy` both carry ($-q^{-1}$). The name " +
        "“Coulomb correction” inherits the channel identification " +
        "withdrawn upstream and is left for the author's relabelling call.",
      see: "docs/audits/2026-08-08-coulomb-decomposition-downstream-propagation.md",
    },
  ],
});
