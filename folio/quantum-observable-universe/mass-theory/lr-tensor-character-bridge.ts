import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:lr-tensor-character-bridge",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.lr_tensor_character_bridge",
    validation: "not_checked",
  },
  title:
    "LR comultiplication bridge for tensor-product braids (trivial-interface, k-factor specialisation)",
  tags: ["hecke-algebra", "littlewood-richardson", "symmetric-functions",
         "markov-trace", "compute-bridge", "atomic-physics-specialisation"],
  uses: [
    "prop:hecke-branching-trace-decomposition",
    "prop:wenzl-bridge-applicability-qou",
    "def:canonical-braid-interface-composition",
  ],
  cites: ["wenzl1988", "macdonald1995", "geckpfeiffer2000", "ram1991"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling takes the sum-over-copies as its hypothesis and derives the displayed form, so the two claims are kept apart." },
    {
      kind: "status",
      body: "The companion Lean `lr_tensor_character_bridge` currently records a placeholder conclusion (`1 = 1`) rather than the full Littlewood--Richardson character-bridge identity; the content above is the intended statement, deferred via `sorry` (`-- Ref: [leitner2026]`).",
    },
  ],
});
