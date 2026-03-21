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
  /** Validation status of the Lean code. */
  validation?: LeanValidation;
}

/**
 * Detailed Lean validation status.
 *
 * Distinguishes between stub declarations, trivially-true lemmas,
 * externally-sourced proofs, and fully validated code.
 */
export type LeanValidation =
  | "not_checked"      // .lean file exists but not yet validated
  | "stub"             // declaration stated but body is `sorry` or `_`
  | "trivial"          // proof is `by trivial`, `by simp`, `by rfl`, etc.
  | "external"         // proof references external resource (mathlib, etc.)
  | "validated"        // built and type-checked successfully
  | "error"            // build error
  | "leanok"           // sorry-free, built successfully
  | "axioms_only";     // type-checks but uses axioms (no sorry)

// ── Pre-rendered content ─────────────────────────────────────────

/**
 * Reference to a pre-rendered asset (e.g. tikzcd → SVG).
 *
 * When a .md file contains ```tex blocks that cannot be rendered
 * client-side (tikzcd, complex align environments), the build pipeline
 * renders them server-side and records the output here.
 *
 * The HTML viewer checks `rendered[]` and displays the pre-rendered
 * asset instead of attempting client-side rendering.
 */
export interface RenderedAsset {
  /** MIME type of the rendered output. */
  mime: "image/svg+xml" | "image/png" | "application/pdf" | (string & {});
  /** URL or relative path to the rendered file. */
  url: string;
  /** 0-based index of the ```tex block this replaces in the .md file. */
  blockIndex: number;
  /** Content hash for cache invalidation. */
  hash?: string;
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
  | "remark"
  | "proof";

// ── Block types (discriminated union on `kind`) ──────────────────

/** Base fields shared by all environment blocks. */
interface BlockBase {
  /** Label following project convention (e.g. "def:quantum-universe"). */
  label: string;
  /** Optional display title. */
  title?: string;
  /** Labels of objects this one depends on (\uses{} in LaTeX). */
  uses?: string[];
  /**
   * Thematic tags for filtering and grouping.
   * Examples: "archimedean", "complex", "p-adic", "su2", "representation-theory"
   */
  tags?: string[];
  /** Override companion file resolution (normally by root-name convention). */
  companions?: Companions;
  /** Pre-rendered assets for ```tex blocks that can't be rendered client-side. */
  rendered?: RenderedAsset[];
  /** Freeform metadata (chapter assignment, tags, etc.). */
  meta?: Record<string, unknown>;
  /** Todo items attached to this block. */
  todos?: TodoItem[];
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
  /** Labels of example blocks illustrating this definition. */
  examples?: string[];
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
  /** Labels of proof blocks for this result (like examples[]). */
  proofs?: string[];
  /** Labels of example blocks illustrating this result. */
  examples?: string[];
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

/**
 * Proof — a standalone proof of a theorem/lemma/proposition/corollary.
 *
 * Multiple proofs can be linked to a single provable block via its
 * `proofs: ["prf:foo", "prf:bar"]` field, similar to how examples work.
 * Each proof is its own content object with .ts + .md + optional .lean files.
 */
export interface ProofBlock extends BlockBase {
  kind: "proof";
  /** Optional Lean formalization of the proof. */
  lean?: LeanRef;
  /** Formalization progress for this proof. */
  status?: FormalizationStatus;
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
  tags?: string[];
  companions?: Companions;
  /** Pre-rendered assets for ```tex blocks. */
  rendered?: RenderedAsset[];
  meta?: Record<string, unknown>;
  /** Todo items attached to this block. */
  todos?: TodoItem[];
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
  /** Pre-rendered equation (e.g. SVG from MathJax/KaTeX server). */
  rendered?: RenderedAsset[];
  meta?: Record<string, unknown>;
  /** Todo items attached to this block. */
  todos?: TodoItem[];
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
  /** Pre-rendered diagram (e.g. SVG from tikzcd server-side render). */
  rendered?: RenderedAsset[];
  meta?: Record<string, unknown>;
  /** Todo items attached to this block. */
  todos?: TodoItem[];
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
  | ProofBlock
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
  | RemarkBlock
  | ProofBlock;

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
  /** Chapter-level todos. */
  todos?: TodoItem[];
}

/**
 * Paper manifest — top-level document.
 *
 * The paper .ts is authoritative for where chapter .ts files live.
 * Each entry in `chapters` is either:
 *   - A ChapterRef (with optional URI override)
 *   - An inline Chapter (for simple cases)
 */
/**
 * A custom macro defined at the paper level.
 *
 * Used by all renderers: KaTeX (viewer), LaTeX (PDF), and plain-text (search).
 */
export interface PaperMacro {
  /** LaTeX expansion (e.g. "\\mathfrak{p}"). Used by KaTeX and LaTeX. */
  tex: string;
  /** UTF-8 display string for plain-text contexts (e.g. "𝔭"). */
  unicode?: string;
}

export interface Paper {
  title: string;
  authors: string[];
  affiliations?: string[];
  date?: string;
  /** Chapter references — URIs to chapter .ts manifests. */
  chapters: ChapterRef[];
  /**
   * Custom LaTeX macros for this paper.
   *
   * Keys are macro names WITHOUT backslash (e.g. "pp" for \pp).
   * Values define the TeX expansion and optional Unicode fallback.
   *
   * All renderers consume these:
   * - KaTeX: passed as `macros` option
   * - LaTeX pipeline: emitted as \newcommand in preamble
   * - Plain-text/search: uses `unicode` field
   */
  macros?: Record<string, PaperMacro>;
  meta?: Record<string, unknown>;
  /** Paper-level todos (cross-cutting concerns, overall tasks). */
  todos?: TodoItem[];
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

// ── Todo items ───────────────────────────────────────────────

/**
 * Priority level for a todo item.
 * Agents and humans use these to triage work.
 */
export type TodoPriority = "critical" | "high" | "medium" | "low";

/**
 * Status of a todo item through its lifecycle.
 */
export type TodoStatus =
  | "open"          // newly created, awaiting triage
  | "in_progress"   // actively being worked on
  | "blocked"       // waiting on external input (author, upstream change)
  | "resolved"      // completed successfully
  | "wontfix";      // closed without resolution

/**
 * Origin of a todo — who/what created it.
 */
export type TodoOrigin =
  | "agent"         // created by an editor/proof agent
  | "human"         // created by author via feedback UI
  | "qc"            // created by QC/validation pipeline
  | "extracted";    // extracted from existing proof-objects/comments

/**
 * A todo item attached to a content block or section.
 *
 * Serves as the unit of agent-to-agent and human-to-agent communication.
 * Each todo lives in the `todos` field of a block manifest (.ts) or in a
 * standalone todos manifest for section/chapter-level items.
 *
 * The `comment` field is a quick markdown narrative.  The optional `data`
 * field carries structured context at the discretion of the creating
 * agent or user.
 */
export interface TodoItem {
  /** Unique ID (e.g. "todo-001" or a nanoid). */
  id: string;
  /** Short summary (one line). */
  summary: string;
  /** Markdown narrative with context, rationale, questions. */
  comment: string;
  /** Current lifecycle status. */
  status: TodoStatus;
  /** Triage priority. */
  priority: TodoPriority;
  /** Who/what created this todo. */
  origin: TodoOrigin;
  /** Label of the block this todo is attached to (e.g. "def:rigid-monoidal-category"). */
  targetLabel?: string;
  /** Who this is assigned to (agent name or "author"). */
  assignee?: string;
  /** ISO 8601 timestamp of creation. */
  createdAt: string;
  /** ISO 8601 timestamp of last update. */
  updatedAt?: string;
  /** Agent/user who last updated. */
  updatedBy?: string;
  /** Structured data — schema is at agent/user discretion. */
  data?: Record<string, unknown>;
  /** Labels of related todos (for threading). */
  related?: string[];
}

// ── Folio (collection of papers) ─────────────────────────────

/**
 * Reference to a paper within the folio.
 *
 * The `dir` is the paper's directory name under content/.
 * The pipeline resolves `<dir>/<dir>.ts` by convention.
 */
export interface PaperRef {
  /** Directory name under content/ (e.g. "quantum-observable-universe"). */
  dir: string;
  /** Optional display title override (otherwise read from paper manifest). */
  title?: string;
  /** Optional description shown on the landing page. */
  description?: string;
  /** Tags for filtering on the landing page. */
  tags?: string[];
}

/**
 * Folio — a collection of papers in this repository.
 *
 * Lives at `content/folio.ts` by convention.  The assistant landing
 * page reads this to discover all papers and render the folio view.
 */
export interface Folio {
  /** Display name for the folio (e.g. "litlfred's Papers"). */
  title: string;
  /** Papers in the folio, ordered by display preference. */
  papers: PaperRef[];
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
