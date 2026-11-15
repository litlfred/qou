/**
 * Re-export from the canonical locations. The theorem-family builders live in
 * folio-assistant-sci (mathpaper-vocabulary.ts); the rest in cat-harness-tools
 * (schemas/builders.ts, moved from cat-harness in bean 8lcl, 2026-10-30).
 * @module folio/schema/builders
 */
export {
  definition,
  theorem,
  lemma,
  proposition,
  corollary,
  conjecture,
  proof,
} from "../../folio-assistant/folio-assistant-sci/schemas/mathpaper-vocabulary";
export {
  algorithm,
  example,
  remark,
  prose,
  equation,
  diagram,
  table,
  figure,
  simulator,
  section,
  sectionRef,
  chapter,
  chapterRef,
  paper,
  paperRef,
  folio,
  document,
} from "../../folio-assistant/cat-harness-tools/schemas/builders";
