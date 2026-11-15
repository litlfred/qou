import { definition } from "../../schema/builders";

/**
 * Snake identity (zig-zag identity) — the defining equations of
 * an exact pairing / duality in a rigid monoidal category.
 *
 * This is a formal definition block (not just a glossary wrapper)
 * because the paper's formulation involves specific composites
 * using associators and unitors that must be spelled out precisely.
 */
export default definition({
  label: "def:snake-identity",
  title: "Snake identity",
  tags: ["category-theory", "monoidal", "duality"],
  lean: {
    decl: "QOU.snake_identity_left",
    validation: "not_checked",
    mathlibLinks: [
      "CategoryTheory.ExactPairing.evaluation_coevaluation'",
      "CategoryTheory.ExactPairing.coevaluation_evaluation'",
    ],
  },
  uses: [],
  examples: [],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/snake-identity-0.svg", blockIndex: 0, hash: "1f029ef104c0" },
  ],

});
