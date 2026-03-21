/**
 * Content-Object AST — Authoritative document model for QOU.
 *
 * ## Directory convention
 *
 * Content is organized by document structure:
 *
 *   content/
 *     <paper-name>/
 *       <paper-name>.ts          — Paper manifest (references chapter URIs)
 *       <chapter-name>/
 *         <chapter-name>.ts      — Chapter manifest (sections + block refs)
 *         <block-name>.ts        — Typed block manifest (kind, label, lean, etc.)
 *         <block-name>.md        — Narrative content (markdown + TeX snippets)
 *         <block-name>.lean      — Lean formalization (when required by kind)
 *
 * The paper .ts is authoritative for where chapter .ts files live, via URI
 * (defaults to relative local path).  Chapter .ts references blocks within
 * its directory.
 *
 * ## File naming convention
 *
 * Each content object has sibling files sharing the same root name:
 *   rigid-monoidal-category.ts   — manifest
 *   rigid-monoidal-category.md   — narrative
 *   rigid-monoidal-category.lean — Lean (when required)
 *
 * ## Content convention (in .md files)
 *
 * - Inline math: $...$
 * - Display math: $$...$$
 * - Complex TeX (tikzcd, align, custom macros): fenced code block with `tex` tag
 *
 * ```tex
 * \begin{tikzcd}
 *   A \arrow[r] & B
 * \end{tikzcd}
 * ```
 *
 * ## Constraint enforcement
 *
 * TypeScript types enforce structure at compile time.
 * Zod schemas (constraints.ts) validate at runtime + CI.
 * Pipeline validates sibling files exist where required.
 *
 * @module content/schema/types
 */

// ── Lean linkage ─────────────────────────────────────────────────

/** Reference to a Lean 4 declaration. */
export interface LeanRef {
  /** Fully qualified Lean 4 name (e.g. "QOU.QuantumUniverse"). */
  decl: string;
  /** Path to .lean file relative to lean/ directory (resolved from sibling if omitted). */
  file?: string;
  /** Whether the declaration is sorry-free. */
  sorryFree?: boolean;
  /** Related mathlib4 declaration names. */
  mathlibLinks?: string[];
}

// ── Companion file references ────────────────────────────────────

/**
 * References to companion files, resolved by pipeline from root name.
 *
 * For `content/objects/quantum-universe.ts`:
 *   md   → "quantum-universe.md"
 *   lean → "quantum-universe.lean"
 *   test → "quantum-universe.test.ts"
 *
 * Explicit paths override the convention.
 */
export interface Companions {
  /** Markdown content file. Resolved from sibling by default. */
  md?: string;
  /** Lean formalization file (relative to lean/ dir, or sibling). */
  lean?: string;
  /** Test report reference (e.g. test ID or file). */
  test?: string;
  /** Additional companion files by role. */
  [role: string]: string | undefined;
}

// ── Formalization constraints ────────────────────────────────────

export type FormalizationStatus =
  | "not_started"
  | "stated"
  | "has_sorry"
  | "proved"
  | "mathlib_ok";

export type ObjectKind =
  | "definition"
  | "theorem"
  | "lemma"
  | "proposition"
  | "corollary"
  | "conjecture"
  | "example"
  | "remark";

// ── Block types (discriminated union on `kind`) ──────────────────

/** Base fields shared by all environment blocks. */
interface BlockBase {
  /** Label following project convention (e.g. "def:quantum-universe"). */
  label: string;
  /** Optional display title. */
  title?: string;
  /** Labels of objects this one depends on (\uses{} in LaTeX). */
  uses?: string[];
  /** Override companion file resolution (normally by root-name convention). */
  companions?: Companions;
  /** Freeform metadata (chapter assignment, tags, etc.). */
  meta?: Record<string, unknown>;
}

// ── Blocks that REQUIRE Lean ─────────────────────────────────────

/**
 * Definition — MUST have a Lean declaration.
 *
 * Pipeline validates:
 *   - .lean sibling exists (or companions.lean resolves)
 *   - lean.decl is a valid Lean identifier
 */
export interface DefinitionBlock extends BlockBase {
  kind: "definition";
  /** Required: every definition must be formalized. */
  lean: LeanRef;
  status: FormalizationStatus;
}

// ── Blocks where Lean is expected but may be WIP ─────────────────

/**
 * Base interface for provable blocks (theorems, lemmas, propositions, corollaries).
 * Lean is expected but may be WIP — missing lean triggers a warning, not an error.
 */
interface ProvableBase extends BlockBase {
  /** Lean declaration reference (expected but not strictly required). */
  lean?: LeanRef;
  /** Formalization progress. */
  status?: FormalizationStatus;
  /**
   * Whether this block has an inline proof in its .md file.
   * If false/omitted, the proof lives in a separate block or Lean file.
   */
  hasProof?: boolean;
}

/** Theorem — a major result. Lean expected; proof may be inline or in .lean. */
export interface TheoremBlock extends ProvableBase {
  kind: "theorem";
}

/** Lemma — auxiliary result supporting a theorem. */
export interface LemmaBlock extends ProvableBase {
  kind: "lemma";
}

/** Proposition — a result of moderate significance. */
export interface PropositionBlock extends ProvableBase {
  kind: "proposition";
}

/** Corollary — a consequence of a theorem or proposition. */
export interface CorollaryBlock extends ProvableBase {
  kind: "corollary";
}

/** Conjecture — an unproven statement. Lean stub optional. */
export interface ConjectureBlock extends BlockBase {
  kind: "conjecture";
  /** Optional Lean stub for the conjecture statement. */
  lean?: LeanRef;
}

// ── Blocks where Lean is optional ────────────────────────────────

/** Example — a concrete instance illustrating a definition or theorem. */
export interface ExampleBlock extends BlockBase {
  kind: "example";
  /** Optional Lean formalization of the example. */
  lean?: LeanRef;
}

/** Remark — expository commentary. Rarely needs Lean. */
export interface RemarkBlock extends BlockBase {
  kind: "remark";
  /** Optional Lean reference (unusual but allowed). */
  lean?: LeanRef;
}

// ── Prose (non-environment content) ──────────────────────────────

/**
 * Freeform narrative text between environments.
 * Content lives entirely in the sibling .md file.
 */
export interface ProseBlock {
  kind: "prose";
  /** Optional label for cross-referencing. */
  label?: string;
  companions?: Companions;
  meta?: Record<string, unknown>;
}

// ── Display math / equations ─────────────────────────────────────

/** Standalone display equation. Short TeX can live inline; complex in .md. */
export interface EquationBlock {
  kind: "equation";
  /** Equation label (e.g. "eq:snake-identities"). */
  label?: string;
  /** Inline TeX for the equation (short enough to live in .ts). */
  tex?: string;
  companions?: Companions;
  meta?: Record<string, unknown>;
}

// ── Diagrams ─────────────────────────────────────────────────────

/** Commutative diagram or figure. Source is tikzcd or other diagram TeX. */
export interface DiagramBlock {
  kind: "diagram";
  /** Diagram label (e.g. "fig:monoidal-structure"). */
  label?: string;
  /** tikzcd or diagram TeX source (can live inline for short diagrams). */
  tex?: string;
  /** Caption text (rendered below diagram in LaTeX). */
  caption?: string;
  companions?: Companions;
  meta?: Record<string, unknown>;
}

// ── The discriminated union ──────────────────────────────────────

export type Block =
  | DefinitionBlock
  | TheoremBlock
  | LemmaBlock
  | PropositionBlock
  | CorollaryBlock
  | ConjectureBlock
  | ExampleBlock
  | RemarkBlock
  | ProseBlock
  | EquationBlock
  | DiagramBlock;

/** Blocks that represent theorem-like environments. */
export type EnvironmentBlock =
  | DefinitionBlock
  | TheoremBlock
  | LemmaBlock
  | PropositionBlock
  | CorollaryBlock
  | ConjectureBlock
  | ExampleBlock
  | RemarkBlock;

/** Blocks that can (or must) have Lean declarations. */
export type FormalizableBlock =
  | DefinitionBlock
  | TheoremBlock
  | LemmaBlock
  | PropositionBlock
  | CorollaryBlock;

// ── Document structure ───────────────────────────────────────────

export interface Section {
  title: string;
  label?: string;
  /** Ordered list of block root names (resolved to .ts files in section/chapter dir). */
  blocks: string[];
  /** Subsections (inline or referenced). */
  subsections?: (Section | SectionRef)[];
}

/**
 * Section reference — used by chapter .ts to locate section .ts files.
 *
 * Sections can be:
 *   - Inline (Section object directly in the chapter)
 *   - Referenced by name (resolved to `<name>/<name>.ts` in chapter dir)
 *   - Referenced by explicit URI
 */
export interface SectionRef {
  /** Root name of the section dir/file. */
  name: string;
  /** URI override (defaults to `./<name>/<name>.ts`). */
  uri?: string;
}

/**
 * Chapter reference — used by the paper manifest to locate chapter .ts files.
 *
 * The `uri` defaults to a relative local path based on directory convention:
 *   `./<chapter-dir>/<chapter-dir>.ts`
 *
 * Can be overridden to point to a remote URI for multi-repo setups.
 */
export interface ChapterRef {
  /** URI to the chapter .ts manifest (default: relative local). */
  uri?: string;
  /** Directory name under the paper root (e.g. "ch1-quantum-observable-universe"). */
  dir: string;
}

export interface Chapter {
  number: number;
  title: string;
  label?: string;
  /** Sections can be inline Section objects or SectionRef references. */
  sections: (Section | SectionRef)[];
  meta?: Record<string, unknown>;
}

/**
 * Paper manifest — top-level document.
 *
 * The paper .ts is authoritative for where chapter .ts files live.
 * Each entry in `chapters` is either:
 *   - A ChapterRef (with optional URI override)
 *   - An inline Chapter (for simple cases)
 */
export interface Paper {
  title: string;
  authors: string[];
  date?: string;
  /** Chapter references — URIs to chapter .ts manifests. */
  chapters: ChapterRef[];
  meta?: Record<string, unknown>;
}

/**
 * @deprecated Use Paper instead. Kept for backward compatibility.
 */
export interface Document {
  title: string;
  authors: string[];
  date?: string;
  chapters: Chapter[];
  meta?: Record<string, unknown>;
}

// ── Validation result ────────────────────────────────────────────

export interface ValidationIssue {
  level: "error" | "warning" | "info";
  block: string;
  message: string;
  file?: string;
}

export interface ValidationResult {
  valid: boolean;
  issues: ValidationIssue[];
}
