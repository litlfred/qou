import { remark } from "../../schema/builders";

export default remark({
  label: "rem:recursive-atom-knot-atlas-sdp-uniqueness-wiring",
  title: "Semidefinite uniqueness stratification across nuclear strand counts",
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
    {
      kind: "note",
      body:
        "Lean SDP-uniqueness wiring: parameterised theorem `nucleus_uniqueness_closed (3 * A)` in `NucleusEmptySDPUniqueness.lean` (generic for any `n : Nat`), with named wrappers in `Applied<Nucleus>Uniqueness.lean` (10 tracked light nuclei), `PeriodicTableUniqueness.lean` (118 elements H..Og), and `StableIsotopeUniqueness.lean` (252 stable nuclides H..Bi). Specific entries are cited as `qou:QOU.BraidKnot.<isotope>_uniqueness_closed` (or `@nucleus_uniqueness_closed (3*A)` outside the named-isotope set); element symbols follow `AtomicMass.lean` with an `_el` suffix where the short symbol collides with a reserved Lean identifier (e.g. `n_el_uniqueness_closed` for nitrogen).",
    },
  ],
});
