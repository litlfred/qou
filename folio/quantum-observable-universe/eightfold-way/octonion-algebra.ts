import { definition } from "../../schema/builders";

/**
 * The octonion algebra 𝕆.
 *
 * Closes the §8 ledger row "used throughout but never defined" (beans
 * qou-7arp, qou-8fl1). The gap was EXPOSITION only: the citation side
 * (baez2002) and the Lean side (nine QOU/MathlibExt/Octonion*.lean files,
 * including the concrete Baez-convention `octMul`) were both already in
 * place. This block is the definition they had nothing to point at.
 *
 * Scope: the algebra itself. The colour SU(3) ⊂ G₂ decomposition
 * 7 = 1 ⊕ 3 ⊕ 3̄ that consumes it is prop:color-su3-from-g2, and the
 * octonions remain an EXTERNAL input there — this block does not
 * construct 𝕆 from the categorical substrate, and does not claim to.
 */
export default definition({
  label: "def:octonion-algebra",
  title: "The octonion algebra $\\mathbb{O}$",
  defines: ["octonion-algebra"],
  // Points at the canonical product in the library tree; no sibling .lean,
  // per the no-shadowing-stubs rule (AGENTS.md §0a).
  lean: { ref: "qou:QOU.MathlibExt.OctonionDerivations.octMul" },
  cites: ["baez2002", "albuquerque-majid1999"],
  tags: ["octonion", "division-algebra", "G2", "color", "eightfold"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): matching the\nmultiplication `octMul` fixed in the Lean sibling.\n\nThe Lean sibling realises the product over $\\mathbb{Q}$ in exact rational\narithmetic." },
  ],
});
