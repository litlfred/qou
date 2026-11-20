import { remark } from "../../schema/builders";

export default remark({
  label: "rem:markov-closure-map-axiomatic",
  title:
    "Factorising the Markov-closure → Hopf-link content into two atomic Lean axioms (closure type at k=2 + classical Jones value), reducing the open content to a smaller surface",
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean encoding\n\nThe companion file [`markov-closure-map-axiomatic.lean`](markov-closure-map-axiomatic.lean) defines `class MarkovClosureMap2Strand` with explicit fields mapping crossing-count to closure type and tracking the classical-limit Jones value. It defines `class TrackCReducedAxiom` carrying the single axiomatic statement that $c_3$ factors through the Hopf identification. It proves `track_C_c_3_eq_neg_two`: under both classes, $c_3 = -2$." },
    {
      kind: "status",
      body: "Lean stub: **no `sorry`s**, but the substantive content is in **2\nclass fields** that encode the atomic axioms. Each field corresponds\nto a specific, named, published knot-theoretic result; the eventual\nLean discharge requires:\n\n- Atom 1 (`closure 2 = Hopf link`): a Lean definition of braid groups\n  + Markov closure + the Hopf link, plus the theorem identifying them.\n- Atom 2 (`jones_at_one 2 = -2`): already closed.\n\nThis is the **Step B** completion of the Track-C plan; **Step A**\n(full braid/link Lean infrastructure) discharges Atom 1 from\nfirst principles.",
    },
  ],
});
