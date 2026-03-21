/**
 * Content schema — public API.
 *
 * @example
 *   import { definition, theorem, prose } from "./schema";
 *   import type { Block, Chapter, Document } from "./schema";
 */

// Types
export type {
  Block,
  EnvironmentBlock,
  FormalizableBlock,
  DefinitionBlock,
  TheoremBlock,
  LemmaBlock,
  PropositionBlock,
  CorollaryBlock,
  ConjectureBlock,
  ExampleBlock,
  RemarkBlock,
  ProseBlock,
  EquationBlock,
  DiagramBlock,
  LeanRef,
  Companions,
  FormalizationStatus,
  ObjectKind,
  Section,
  SectionRef,
  Chapter,
  ChapterRef,
  Paper,
  Document,
  ValidationIssue,
  ValidationResult,
} from "./types";

// Builders
export {
  definition,
  theorem,
  lemma,
  proposition,
  corollary,
  conjecture,
  example,
  remark,
  prose,
  equation,
  diagram,
  section,
  sectionRef,
  chapter,
  chapterRef,
  paper,
  document,
} from "./builders";

// Zod schemas (for runtime validation, CI, tests)
export {
  BlockSchema,
  DefinitionSchema,
  TheoremSchema,
  LemmaSchema,
  PropositionSchema,
  CorollarySchema,
  ConjectureSchema,
  ExampleSchema,
  RemarkSchema,
  ProseSchema,
  EquationSchema,
  DiagramSchema,
  ChapterSchema,
  ChapterRefSchema,
  SectionRefSchema,
  PaperSchema,
  DocumentSchema,
  LeanRefSchema,
  CONSTRAINT_RULES,
  type ConstraintRule,
  type ConstraintContext,
} from "./constraints";
