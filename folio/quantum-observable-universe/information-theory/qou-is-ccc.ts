import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qou-is-ccc",
  title:
    "Aeon boundaries satisfy the horizon-local conditions of a conformal cyclic cosmology",
  tags: [
    "ccc", "aeon", "conformal-cyclic-cosmology",
    "penrose", "jet-horizon", "conformal-invariance",
  ],
  lean: { ref: "qou:QOU.qou_is_ccc",
    validation: "not_checked",
  },
  uses: ["prop:horizon-conformal-invariance"],
  cites: ["penrose2010"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-09-14",
      body:
        "**Title narrowed from \"A QOU with aeons is a conformal cyclic " +
        "cosmology\".** The Lean witness `QOU.qou_is_ccc` establishes CCC-1 " +
        "and CCC-3 only — the horizon-local conditions — and its proof is " +
        "`\u27e8H.degree_zero_vanishes, H.degree_one_leaks, " +
        "H.degree_two_leaks\u27e9`, three field projections of the " +
        "`JetHorizon` structure whose fields are exactly those three " +
        "conclusions. CCC-2, boundary-data inheritance, is the only " +
        "non-definitional leg and the Lean docstring records that it is not " +
        "formalised. The `.md` body was already accurate on all of this " +
        "(`penrose-ccc.md` lists four explicit departures from Penrose and " +
        "states the mechanism differs; the proof block carries a " +
        "\"Limitations of the claim\" paragraph) — only the title asserted " +
        "more than the block delivers.",
    },
  ],
});
