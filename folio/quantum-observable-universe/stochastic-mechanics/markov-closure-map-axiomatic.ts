import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-closure-map-axiomatic",
  title:
    "Factorising the Markov-closure to Hopf-link identification into two atomic hypotheses",
  interprets: "prop:q-beta-c3-hopf-three-fold-markov",
  uses: ["rem:F3-eps6-leading-eq-neg-2b-cubed"],
  cites: ["jones1985"],
  tags: [
    "lean-infrastructure",
    "track-C-step-B",
    "markov-closure",
    "hopf-link",
    "axiomatic-reduction",
  ],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "status",
      body: "Lean stub: **no `sorry`s**, but the substantive content is in **2\nclass fields** that encode the atomic axioms. Each field corresponds\nto a specific, named, published knot-theoretic result; the eventual\nLean discharge requires:\n\n- Atom 1 (`closure 2 = Hopf link`): a Lean definition of braid groups\n  + Markov closure + the Hopf link, plus the theorem identifying them.\n- Atom 2 (`jones_at_one 2 = -2`): already closed.\n\nThis is the **Step B** completion of the Track-C plan; **Step A**\n(full braid/link Lean infrastructure) discharges Atom 1 from\nfirst principles. Companion file `markov-closure-map-axiomatic.lean` defines `MarkovClosureMap2Strand`, `TrackCReducedAxiom` (refining `ThreeFoldMarkovHopfExtraction`), and proves `track_C_c_3_eq_neg_two`.",
    },
  ],
});
