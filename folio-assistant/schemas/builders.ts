/**
 * Builder functions for content objects.
 *
 * Usage:
 *   import { definition, theorem, prose } from "../schema/builders";
 *
 *   export default definition({
 *     label: "def:quantum-universe",
 *     lean: { decl: "QOU.QuantumUniverse" },
 *     status: "proved",
 *   });
 *
 * Each builder validates against its Zod schema at construction time,
 * giving immediate feedback in the editor / at import time.
 *
 * @module content/schema/builders
 */

import type {
  DefinitionBlock,
  TheoremBlock,
  LemmaBlock,
  PropositionBlock,
  CorollaryBlock,
  AlgorithmBlock,
  ConjectureBlock,
  SpeculationBlock,
  ExampleBlock,
  RemarkBlock,
  ProofBlock,
  SimulatorBlock,
  ProseBlock,
  EquationBlock,
  DiagramBlock,
  TableBlock,
  Chapter,
  ChapterRef,
  Section,
  SectionRef,
  Paper,
  PaperRef,
  Folio,
  Document,
  FeedbackItem,
} from "./types";

import {
  DefinitionSchema,
  TheoremSchema,
  LemmaSchema,
  PropositionSchema,
  CorollarySchema,
  AlgorithmSchema,
  ConjectureSchema,
  SpeculationSchema,
  ExampleSchema,
  RemarkSchema,
  ProofSchema,
  SimulatorSchema,
  ProseSchema,
  EquationSchema,
  DiagramSchema,
  TableSchema,
  ChapterSchema,
  ChapterRefSchema,
  SectionRefSchema,
  PaperSchema,
  PaperRefSchema,
  FolioSchema,
  DocumentSchema,
  FeedbackItemSchema,
  citesProvable,
} from "./constraints";

// ── Generic validated builder ────────────────────────────────────

function validated<T>(schema: { parse: (v: unknown) => unknown }, data: T): T {
  schema.parse(data);
  return data;
}

// ── Block builders ───────────────────────────────────────────────

export function definition(data: Omit<DefinitionBlock, "kind">): DefinitionBlock {
  // Provide default lean ref so partially-authored definitions
  // load instead of crashing the viewer/MCP server with Zod errors.
  // Uses the qou package by default; callers working in other papers
  // must pass an explicit `lean.ref`.
  const label = data.label || "def:unknown";
  const defaultDecl = "QOU." + label.replace(/^def:/, "").replace(/-./g, m => m[1].toUpperCase()).replace(/^./, c => c.toUpperCase());
  if (!data.lean) (data as any).lean = { ref: `qou:${defaultDecl}` };
  return validated(DefinitionSchema, { kind: "definition" as const, ...data });
}

export function theorem(data: Omit<TheoremBlock, "kind">): TheoremBlock {
  return validated(TheoremSchema, { kind: "theorem" as const, ...data });
}

export function lemma(data: Omit<LemmaBlock, "kind">): LemmaBlock {
  return validated(LemmaSchema, { kind: "lemma" as const, ...data });
}

export function proposition(data: Omit<PropositionBlock, "kind">): PropositionBlock {
  return validated(PropositionSchema, { kind: "proposition" as const, ...data });
}

export function corollary(data: Omit<CorollaryBlock, "kind">): CorollaryBlock {
  return validated(CorollarySchema, { kind: "corollary" as const, ...data });
}

export function algorithm(data: Omit<AlgorithmBlock, "kind">): AlgorithmBlock {
  const block = validated(AlgorithmSchema, { kind: "algorithm" as const, ...data });
  // Per "downstream of math" invariant (also enforced by
  // `BlockSchema.superRefine`): an algorithm without a cited
  // provable in `uses[]` is rejected at construction time so
  // authoring errors fail loudly in the editor.
  if (!citesProvable(block.uses)) {
    throw new Error(
      `algorithm block "${block.label}" must cite at least one provable ` +
        `(def:/prop:/thm:/lem:/cor:/conj:) in uses[] — algorithms are downstream of math.`,
    );
  }
  return block;
}

export function conjecture(data: Omit<ConjectureBlock, "kind">): ConjectureBlock {
  return validated(ConjectureSchema, { kind: "conjecture" as const, ...data });
}

export function speculation(data: Omit<SpeculationBlock, "kind">): SpeculationBlock {
  return validated(SpeculationSchema, { kind: "speculation" as const, ...data });
}

export function example(data: Omit<ExampleBlock, "kind">): ExampleBlock {
  return validated(ExampleSchema, { kind: "example" as const, ...data });
}

export function remark(data: Omit<RemarkBlock, "kind">): RemarkBlock {
  return validated(RemarkSchema, { kind: "remark" as const, ...data });
}

export function proof(data: Omit<ProofBlock, "kind">): ProofBlock {
  return validated(ProofSchema, { kind: "proof" as const, ...data });
}

export function simulator(data: Omit<SimulatorBlock, "kind">): SimulatorBlock {
  return validated(SimulatorSchema, { kind: "simulator" as const, ...data });
}

export function prose(data?: Omit<ProseBlock, "kind">): ProseBlock {
  return validated(ProseSchema, { kind: "prose" as const, ...data });
}

export function equation(data: Omit<EquationBlock, "kind">): EquationBlock {
  return validated(EquationSchema, { kind: "equation" as const, ...data });
}

export function diagram(data: Omit<DiagramBlock, "kind">): DiagramBlock {
  return validated(DiagramSchema, { kind: "diagram" as const, ...data });
}

export function table(data: Omit<TableBlock, "kind">): TableBlock {
  return validated(TableSchema, { kind: "table" as const, ...data });
}

// ── Structure builders ───────────────────────────────────────────

export function section(data: Section): Section {
  return data;
}

export function sectionRef(data: SectionRef): SectionRef {
  return validated(SectionRefSchema, data) as SectionRef;
}

export function chapter(data: Chapter): Chapter {
  return validated(ChapterSchema, data) as Chapter;
}

export function chapterRef(data: ChapterRef): ChapterRef {
  return validated(ChapterRefSchema, data) as ChapterRef;
}

export function paper(data: Paper): Paper {
  return validated(PaperSchema, data) as Paper;
}

export function paperRef(data: PaperRef): PaperRef {
  return validated(PaperRefSchema, data) as PaperRef;
}

export function folio(data: Folio): Folio {
  return validated(FolioSchema, data) as Folio;
}

/** @deprecated Use paper() instead. */
export function document(data: Document): Document {
  return validated(DocumentSchema, data) as Document;
}

// ── Feedback builder ──────────────────────────────────────────────

export function feedbackItem(data: FeedbackItem): FeedbackItem {
  return validated(FeedbackItemSchema, data) as FeedbackItem;
}
