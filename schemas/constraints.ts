/**
 * Zod schemas for runtime validation of content objects.
 *
 * These mirror the TypeScript types in types.ts but add runtime checks:
 * - Label format validation (prefix must match kind)
 * - Required fields per kind (e.g. definitions MUST have lean)
 * - Companion file existence (checked by pipeline, not Zod)
 *
 * @module content/schema/constraints
 */

import { z } from "zod";

// ── Label patterns ───────────────────────────────────────────────

/** Label prefix must match object kind. */
const LABEL_PREFIXES: Record<string, string> = {
  definition: "def:",
  theorem: "thm:",
  lemma: "lem:",
  proposition: "prop:",
  corollary: "cor:",
  conjecture: "conj:",
  example: "ex:",
  remark: "rem:",
  proof: "prf:",
  equation: "eq:",
  diagram: "fig:",
};

function labelForKind(kind: string) {
  const prefix = LABEL_PREFIXES[kind];
  if (!prefix) return z.string().min(1);
  return z.string().startsWith(prefix, {
    message: `Label for ${kind} must start with "${prefix}"`,
  });
}

// ── Lean reference ───────────────────────────────────────────────

const LeanValidationSchema = z.enum([
  "not_checked", "stub", "trivial", "external", "validated", "error",
  "leanok",        // sorry-free, built successfully
  "axioms_only",   // type-checks but uses axioms (no sorry)
]);

export const LeanRefSchema = z.object({
  decl: z.string().min(1, "Lean declaration name is required"),
  file: z.string().optional(),
  sorryFree: z.boolean().optional(),
  mathlibLinks: z.array(z.string()).optional(),
  validation: LeanValidationSchema.optional(),
});

// ── Companions ───────────────────────────────────────────────────

export const CompanionsSchema = z.record(z.string(), z.string().optional());

// ── Todo schema ──────────────────────────────────────────────

export const TodoItemSchema = z.object({
  id: z.string().min(1),
  summary: z.string().min(1),
  comment: z.string(),
  status: z.enum(["open", "in_progress", "blocked", "resolved", "wontfix"]),
  priority: z.enum(["critical", "high", "medium", "low"]),
  origin: z.enum(["agent", "human", "qc", "extracted"]),
  targetLabel: z.string().optional(),
  assignee: z.string().optional(),
  createdAt: z.string(),
  updatedAt: z.string().optional(),
  updatedBy: z.string().optional(),
  data: z.record(z.string(), z.unknown()).optional(),
  related: z.array(z.string()).optional(),
});

// ── Block schemas ────────────────────────────────────────────────

const RenderedAssetSchema = z.object({
  mime: z.string(),
  url: z.string(),
  blockIndex: z.number().int().nonnegative(),
  hash: z.string().optional(),
});

const BlockBaseSchema = z.object({
  title: z.string().optional(),
  uses: z.array(z.string()).optional(),
  tags: z.array(z.string()).optional(),
  companions: CompanionsSchema.optional(),
  rendered: z.array(RenderedAssetSchema).optional(),
  meta: z.record(z.string(), z.unknown()).optional(),
});

export const DefinitionSchema = BlockBaseSchema.extend({
  kind: z.literal("definition"),
  label: labelForKind("definition"),
  lean: LeanRefSchema,
  status: z.enum(["not_started", "stated", "has_sorry", "proved", "mathlib_ok"]),
  examples: z.array(z.string()).optional(),
});

const ProvableBaseSchema = BlockBaseSchema.extend({
  proofs: z.array(z.string()).optional(),
  examples: z.array(z.string()).optional(),
});

export const TheoremSchema = ProvableBaseSchema.extend({
  kind: z.literal("theorem"),
  label: labelForKind("theorem"),
});

export const LemmaSchema = ProvableBaseSchema.extend({
  kind: z.literal("lemma"),
  label: labelForKind("lemma"),
});

export const PropositionSchema = ProvableBaseSchema.extend({
  kind: z.literal("proposition"),
  label: labelForKind("proposition"),
});

export const CorollarySchema = ProvableBaseSchema.extend({
  kind: z.literal("corollary"),
  label: labelForKind("corollary"),
});

export const ConjectureSchema = BlockBaseSchema.extend({
  kind: z.literal("conjecture"),
  label: labelForKind("conjecture"),
  lean: LeanRefSchema.optional(),
});

export const ExampleSchema = BlockBaseSchema.extend({
  kind: z.literal("example"),
  label: labelForKind("example"),
  lean: LeanRefSchema.optional(),
});

export const RemarkSchema = BlockBaseSchema.extend({
  kind: z.literal("remark"),
  label: labelForKind("remark"),
  lean: LeanRefSchema.optional(),
});

export const ProofSchema = BlockBaseSchema.extend({
  kind: z.literal("proof"),
  label: labelForKind("proof"),
  lean: LeanRefSchema.optional(),
  status: z.enum(["not_started", "stated", "has_sorry", "proved", "mathlib_ok"]).optional(),
});

export const ProseSchema = z.object({
  kind: z.literal("prose"),
  label: z.string().optional(),
  tags: z.array(z.string()).optional(),
  companions: CompanionsSchema.optional(),
  rendered: z.array(RenderedAssetSchema).optional(),
  meta: z.record(z.string(), z.unknown()).optional(),

});

export const EquationSchema = z.object({
  kind: z.literal("equation"),
  label: labelForKind("equation").optional(),
  tex: z.string().optional(),
  tags: z.array(z.string()).optional(),
  companions: CompanionsSchema.optional(),
  rendered: z.array(RenderedAssetSchema).optional(),
  meta: z.record(z.string(), z.unknown()).optional(),

});

export const DiagramSchema = z.object({
  kind: z.literal("diagram"),
  label: labelForKind("diagram").optional(),
  tex: z.string().optional(),
  caption: z.string().optional(),
  tags: z.array(z.string()).optional(),
  companions: CompanionsSchema.optional(),
  rendered: z.array(RenderedAssetSchema).optional(),
  meta: z.record(z.string(), z.unknown()).optional(),

});

/** Discriminated union — validates any Block. */
export const BlockSchema = z.discriminatedUnion("kind", [
  DefinitionSchema,
  TheoremSchema,
  LemmaSchema,
  PropositionSchema,
  CorollarySchema,
  ConjectureSchema,
  ExampleSchema,
  RemarkSchema,
  ProofSchema,
  ProseSchema,
  EquationSchema,
  DiagramSchema,
]);

// ── Chapter / Document schemas ───────────────────────────────────

export const SectionSchema = z.object({
  title: z.string().min(1),
  label: z.string().optional(),
  blocks: z.array(z.string().min(1)),
});

export const SectionRefSchema = z.object({
  name: z.string().min(1),
  uri: z.string().optional(),
});

export const ChapterSchema = z.object({
  number: z.number().int().positive().optional(),
  title: z.string().min(1),
  label: z.string().optional(),
  sections: z.array(z.union([SectionSchema, SectionRefSchema])),
  meta: z.record(z.string(), z.unknown()).optional(),

});

export const ChapterRefSchema = z.object({
  uri: z.string().optional(),
  dir: z.string().min(1),
});

const PaperMacroSchema = z.object({
  tex: z.string().min(1),
  unicode: z.string().optional(),
});

export const PaperSchema = z.object({
  title: z.string().min(1),
  authors: z.array(z.string().min(1)).min(1),
  affiliations: z.array(z.string()).optional(),
  emails: z.array(z.string().email()).optional(),
  urls: z.array(z.string().url()).optional(),
  date: z.string().optional(),
  abstract: z.string().optional(),
  chapters: z.array(ChapterRefSchema),
  macros: z.record(z.string(), PaperMacroSchema).optional(),
  meta: z.record(z.string(), z.unknown()).optional(),
});

/** @deprecated Use PaperSchema. */
export const DocumentSchema = z.object({
  title: z.string().min(1),
  authors: z.array(z.string().min(1)).min(1),
  date: z.string().optional(),
  chapters: z.array(ChapterSchema),
  meta: z.record(z.string(), z.unknown()).optional(),
});

// ── Folio schemas ─────────────────────────────────────────────

export const PaperRefSchema = z.object({
  dir: z.string().min(1),
  title: z.string().optional(),
  description: z.string().optional(),
  tags: z.array(z.string()).optional(),
});

export const FolioSchema = z.object({
  title: z.string().min(1),
  papers: z.array(PaperRefSchema).min(1),
  meta: z.record(z.string(), z.unknown()).optional(),
});

// ── Constraint rules (beyond schema shape) ───────────────────────

export interface ConstraintRule {
  id: string;
  description: string;
  /** Which block kinds this rule applies to. */
  appliesTo: string[];
  /** Check function — returns error message or null. */
  check: (block: z.infer<typeof BlockSchema>, context: ConstraintContext) => string | null;
}

export interface ConstraintContext {
  /** Root name of the .ts file. */
  rootName: string;
  /** Directory containing the object files. */
  dir: string;
  /** Set of all labels in the document (for cross-ref validation). */
  allLabels: Set<string>;
  /** File existence checker. */
  fileExists: (path: string) => boolean;
}

/**
 * Built-in constraint rules.
 *
 * Pipeline runs these after Zod schema validation.
 * Add custom rules by appending to this array.
 */
export const CONSTRAINT_RULES: ConstraintRule[] = [
  {
    id: "md-exists",
    description: "Every block must have a companion .md file",
    appliesTo: [
      "definition", "theorem", "lemma", "proposition", "corollary",
      "conjecture", "example", "remark", "prose",
    ],
    check: (block, ctx) => {
      const mdPath = `${ctx.dir}/${ctx.rootName}.md`;
      return ctx.fileExists(mdPath) ? null : `Missing companion: ${mdPath}`;
    },
  },
  {
    id: "lean-file-exists",
    description: "Definitions must have a companion .lean file or lean.file reference",
    appliesTo: ["definition"],
    check: (block, ctx) => {
      if ("lean" in block && block.lean?.file) return null;
      const leanPath = `${ctx.dir}/${ctx.rootName}.lean`;
      return ctx.fileExists(leanPath) ? null
        : `Definition "${block.label}" requires Lean formalization. Expected: ${leanPath} or lean.file`;
    },
  },
  {
    id: "uses-resolve",
    description: "All labels in uses[] must exist in the document",
    appliesTo: [
      "definition", "theorem", "lemma", "proposition", "corollary",
      "conjecture", "example", "remark",
    ],
    check: (block, ctx) => {
      if (!("uses" in block) || !block.uses) return null;
      const missing = block.uses.filter((u: string) => !ctx.allLabels.has(u));
      return missing.length === 0 ? null
        : `Unresolved uses: ${missing.join(", ")}`;
    },
  },
  {
    id: "provable-lean-warning",
    description: "Theorems/lemmas/propositions/corollaries should have Lean (warning)",
    appliesTo: ["theorem", "lemma", "proposition", "corollary"],
    check: (block, _ctx) => {
      if ("lean" in block && block.lean) return null;
      // Return as warning-level message (prefix convention)
      return `[warning] ${block.label}: no Lean declaration yet`;
    },
  },
];
