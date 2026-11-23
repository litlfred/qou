import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-sdp-uniqueness-wiring",
  title: "Lean SDP-uniqueness wiring for the atlas entries",
  interprets: "prop:recursive-atom-knot-atlas",
  uses: [
    "prop:recursive-atom-knot-atlas",
    "def:confined-particle",
  ],
  tags: [
    "atlas",
    "sdp-uniqueness",
    "appendix",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Original heading \"SDP uniqueness, Lean side\"; \"SDP-uniqueness theorem on the Lean side\"; \"The same statement, supplied by the parameterised `NucleusEmptySDPUniqueness` module, covers any nucleus once ...\". Moved section: Named wrappers expose this at four granularity layers — from the ten\nthe tracked nuclei, through per-element and per-stable-isotope\ncoverage, down to the generic module valid for any $n : \\mathbb{N}$:\n\n| Granularity | Lean file | Coverage |\n|---|---|---|\n| tracked nuclei | `Applied<Nucleus>Uniqueness.lean` (10 files) | $^2$H, $^3$H, $^3$He, $^4$He, $^6$Li, $^9$Be, $^{11}$B, $^{12}$C, $^{14}$N, $^{16}$O |\n| Per-element (AME2020 ref) | `PeriodicTableUniqueness.lean` | 118 elements H..Og |\n| Per-stable-isotope | `StableIsotopeUniqueness.lean` | 252 stable nuclides H..Bi |\n| Generic | `NucleusEmptySDPUniqueness.lean` | Any $n : \\mathbb{N}$ |\n\nTo cite a specific entry, use\n`qou:QOU.BraidKnot.<isotope>_uniqueness_closed`; for atoms outside\nthe named-isotope set, apply `@nucleus_uniqueness_closed (3*A)`\ndirectly with the atlas $A$. Element symbols follow `AtomicMass.lean`,\nwith an `_el` suffix where the short symbol collides with a reserved\nLean identifier (e.g. `n_el_uniqueness_closed` for nitrogen)." },
  ],
});
