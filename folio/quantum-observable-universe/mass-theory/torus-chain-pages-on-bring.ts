import { remark } from "../../schema/builders";

/**
 * The Milnor fibres of the torus-knot components embed on Bring's surface by
 * the corpus's own genus criterion, and the component complements carry the
 * same global PSL(2,R) frame as the Bring cone link. Keeps the proved
 * embeddability (Lean, `decide`) apart from the real-form question that the
 * cone-link Reeb triad raises.
 */
export default remark({
  interprets: "prop:canonical-closure-torus-chain",
  label: "rem:torus-chain-pages-on-bring",
  title:
    "The pages of the torus-knot components embed on Bring's surface, and their complements carry the Bring frame",
  lean: {
    ref: "qou:QOU.Mass.TorusKnotPages.pages_embed_on_bring",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "prop:canonical-closure-torus-chain",
    "prop:cohomological-embedding",
    "def:brings-surface",
  ],
  cites: ["milnor1950"],
  tags: [
    "mass-theory",
    "brings-surface",
    "torus-knots",
    "open-book",
    "reeb-flow",
    "lean-formalised",
    "draft",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (`pages_embed_on_bring`, machine-checked)." },
  ],
});
