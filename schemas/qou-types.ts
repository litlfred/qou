/**
 * QOU Type Definitions — Proof Objects, Glossary, and Formalization Pipeline
 *
 * TypeScript type definitions replacing JSON schemas for the Quantum Observable
 * Universe formalization pipeline.  These types define the data structures for
 * proof tracking, semantic glossary, narrative-to-Lean mapping, and proof state
 * export.
 *
 * @module schemas/qou-types
 */

// =============================================================================
// §1  Proof Objects Manifest (replaces proof-objects.schema.json)
// =============================================================================

export type FormalizationStatus =
  | "not_started"
  | "stated"
  | "has_sorry"
  | "proved"
  | "mathlib_ok";

export type ObjectType =
  | "definition"
  | "theorem"
  | "lemma"
  | "proposition"
  | "corollary"
  | "conjecture"
  | "example"
  | "remark";

export type ReviewType =
  | "scientific-accuracy"
  | "latex-validation"
  | "readability"
  | "lean-proof-check"
  | "mathematical-rigor"
  | "general";

export type Verdict = "APPROVE" | "REQUEST_CHANGES" | "NEEDS_DISCUSSION";
export type Severity = "critical" | "major" | "minor";
export type ReviewerType = "human" | "agentic";
export type DependencyRelation = "uses" | "proves";

export interface LaTeXLocation {
  /** Path to the LaTeX source file relative to repo root. */
  file: string;
  /** Line number of the \begin{environment}. */
  line: number;
  /** Chapter number. */
  chapter?: number;
  /** Rendered theorem number (e.g., "4.12"). */
  number?: string;
}

export interface LeanReference {
  /** Fully qualified Lean declaration name. */
  decl?: string;
  /** URL to the Lean declaration on doc-gen4 or GitHub Pages. */
  url?: string;
  /** Path to .lean file relative to lean/ directory. */
  file?: string;
  /** Whether the declaration is free of sorry. */
  sorry_free?: boolean;
  /** URL to the Lean source file on GitHub (at the specific commit). */
  github_source_url?: string;
  /** URL to the Lean source file published on GitHub Pages. */
  gh_pages_url?: string;
  /** Git commit SHA at which this Lean file was last modified. */
  last_edited_commit?: string;
  /** Related mathlib4 declaration names. */
  mathlib_links?: string[];
}

export interface ReviewIssue {
  severity: Severity;
  message: string;
  line?: number;
  suggestion?: string;
}

export interface LeanReviewStatus {
  sorry_count?: number;
  /** Outstanding goal strings from sorry sites. */
  sorry_goals?: string[];
  type_checks?: boolean;
  build_log_url?: string;
}

export interface ReviewRecord {
  /** Identifier for the reviewer (model name, GitHub username, etc.). */
  reviewer_id: string;
  reviewer_type: ReviewerType;
  review_type: ReviewType;
  /** ISO-8601 timestamp. */
  timestamp: string;
  verdict: Verdict;
  /** Reviewer's confidence in the verdict (0–1). */
  confidence?: number;
  severity_counts?: Record<Severity, number>;
  issues?: ReviewIssue[];
  lean_status?: LeanReviewStatus;
  commit_sha?: string;
  notes?: string;
}

export interface ProofObject {
  /** LaTeX label following the project labeling convention. */
  label: string;
  object_type: ObjectType;
  title?: string | null;
  latex: LaTeXLocation;
  lean?: LeanReference;
  formalization_status?: FormalizationStatus;
  reviews?: ReviewRecord[];
  /** Labels of objects this one depends on (from \uses{}). */
  uses?: string[];
}

export interface DependencyEdge {
  /** Label of the object that uses another. */
  from: string;
  /** Label of the object being used. */
  to: string;
  relation?: DependencyRelation;
}

export interface Manuscript {
  /** GitHub repository (owner/name). */
  repo: string;
  /** Git commit SHA from which objects were extracted. */
  commit_sha: string;
  /** ISO-8601 timestamp of extraction. */
  generated_at: string;
  /** URL to the published PDF. */
  pdf_url?: string;
  /** Base URL for doc-gen4 Lean documentation pages. */
  lean_docs_url?: string;
}

export interface ProofObjectsManifest {
  version: "1.0";
  manuscript: Manuscript;
  objects: ProofObject[];
  dependencies?: DependencyEdge[];
}

// =============================================================================
// §2  Semantic Glossary (Ontologist output)
// =============================================================================

/** Universe assignment for Lean category-theoretic types. */
export interface UniverseLevel {
  /** Universe for objects (typically `u`). */
  objects: string;
  /** Universe for morphisms (typically `v`). */
  morphisms?: string;
}

/** How a glossary term maps into Lean's type system. */
export type LeanDeclKind = "def" | "class" | "structure" | "axiom" | "constant" | "instance";

/** A single entry in the semantic glossary. */
export interface GlossaryEntry {
  /** Narrative string as it appears in the paper. */
  narrative_term: string;
  /** Lean 4 identifier (fully qualified). */
  lean_name: string;
  /** Lean declaration kind. */
  kind: LeanDeclKind;
  /** Lean 4 type signature (the `: Type*` or `: Prop` part). */
  lean_type?: string;
  /** The original prose definition from the manuscript. */
  narrative_definition?: string;
  /** LaTeX source label where this term is defined. */
  latex_label?: string;
  /** Chapter number where this term first appears. */
  chapter?: number;
  /** Mathlib type this maps to (if any). */
  mathlib_type?: string;
  /** Mathlib module path. */
  mathlib_import?: string;
  /** Universe level requirements for category-theoretic types. */
  universes?: UniverseLevel;
  /** Other glossary entries this one depends on. */
  depends_on?: string[];
  /** Ambiguity flags — terms that could not be uniquely resolved. */
  ambiguity?: AmbiguityFlag;
}

/** Flag for terms requiring human disambiguation. */
export interface AmbiguityFlag {
  /** Whether the term is ambiguous and needs resolution. */
  is_ambiguous: boolean;
  /** Description of the ambiguity. */
  message: string;
  /** Candidate types the term could map to. */
  candidates: string[];
  /** The resolution chosen (filled in after disambiguation). */
  resolved_to?: string;
}

export interface GlossaryManifest {
  version: "1.0";
  /** ISO-8601 timestamp. */
  generated_at: string;
  commit_sha: string;
  /** Total number of entries. */
  entry_count: number;
  /** Number of unresolved ambiguities. */
  ambiguity_count: number;
  entries: GlossaryEntry[];
}

// =============================================================================
// §3  Narrative-to-Lean Mapping (mapping.json)
// =============================================================================

/** Bidirectional mapping between narrative strings and Lean identifiers. */
export interface NarrativeMapping {
  /** Narrative string (e.g., "Bring's Surface"). */
  narrative: string;
  /** Lean identifier (e.g., "QOU.BringsSurface.BringsSurface"). */
  lean_id: string;
  /** LaTeX label (e.g., "def:brings-surface"). */
  latex_label?: string;
  /** Context in which this mapping is valid. */
  context?: string;
}

export interface MappingManifest {
  version: "1.0";
  generated_at: string;
  mappings: NarrativeMapping[];
}

// =============================================================================
// §4  Proof State Export (for external analysis tools)
// =============================================================================

/** A single goal in a Lean proof state. */
export interface ProofGoal {
  /** Goal index (0-based). */
  index: number;
  /** The type to be proved (the goal). */
  target: string;
  /** Local context: hypotheses available. */
  hypotheses: ProofHypothesis[];
}

export interface ProofHypothesis {
  /** Hypothesis name. */
  name: string;
  /** Hypothesis type. */
  type: string;
  /** Whether this hypothesis was introduced by the user. */
  is_user_introduced: boolean;
}

/** Proof state at a specific point in a Lean proof. */
export interface ProofStateExport {
  /** Fully qualified declaration name. */
  declaration: string;
  /** File path relative to lean/. */
  file: string;
  /** Line number in the Lean file. */
  line: number;
  /** Column number. */
  column: number;
  /** Current tactic (if in tactic mode). */
  current_tactic?: string;
  /** Outstanding goals. */
  goals: ProofGoal[];
  /** Whether the proof is complete (no remaining goals). */
  is_complete: boolean;
  /** Timestamp of export. */
  exported_at: string;
}

export interface ProofStateManifest {
  version: "1.0";
  states: ProofStateExport[];
}

// =============================================================================
// §5  Category Theory Metadata
// =============================================================================

/** Category-theoretic structure classification. */
export type CategoryLevel =
  | "Category"
  | "SmallCategory"
  | "Preadditive"
  | "Abelian"
  | "Monoidal"
  | "BraidedMonoidal"
  | "SymmetricMonoidal"
  | "Rigid";

/** Extended glossary entry for category-theoretic objects. */
export interface CategoryGlossaryEntry extends GlossaryEntry {
  /** Category-theoretic classification. */
  category_level?: CategoryLevel;
  /** Required Lean typeclasses. */
  required_instances?: string[];
  /** Whether this type involves functorial operations. */
  is_functorial?: boolean;
  /** Functor-specific data. */
  functor_data?: {
    /** Source category. */
    source: string;
    /** Target category. */
    target: string;
    /** Whether this is a monoidal functor. */
    is_monoidal?: boolean;
  };
}

// =============================================================================
// §6  Tactic Mapping (Formalizer configuration)
// =============================================================================

/** Maps narrative proof phrases to Lean tactics. */
export interface TacticMapping {
  /** Narrative phrase pattern (regex or literal). */
  pattern: string;
  /** Whether the pattern is a regex. */
  is_regex: boolean;
  /** Primary Lean tactic to try. */
  primary_tactic: string;
  /** Fallback tactics if primary fails. */
  fallback_tactics: string[];
  /** Context in which this mapping applies. */
  context?: "algebra" | "topology" | "category_theory" | "analysis" | "general";
}

/** Default tactic mappings from the design spec. */
export const DEFAULT_TACTIC_MAPPINGS: TacticMapping[] = [
  {
    pattern: "by calculation",
    is_regex: false,
    primary_tactic: "ring",
    fallback_tactics: ["field_simp", "polyrith"],
    context: "algebra",
  },
  {
    pattern: "clearly follows from",
    is_regex: false,
    primary_tactic: "aesop",
    fallback_tactics: ["linarith", "omega"],
    context: "general",
  },
  {
    pattern: "by induction on (\\w+)",
    is_regex: true,
    primary_tactic: "induction $1 with",
    fallback_tactics: ["cases $1"],
    context: "general",
  },
  {
    pattern: "by the universal property",
    is_regex: false,
    primary_tactic: "exact Limits.IsLimit.lift",
    fallback_tactics: ["exact Limits.IsLimit.hom_ext"],
    context: "category_theory",
  },
  {
    pattern: "diagram commutes|naturality",
    is_regex: true,
    primary_tactic: "aesop_cat",
    fallback_tactics: ["slice_lhs 1 2 => { rw [Category.assoc] }", "simp [CategoryTheory.Category.assoc]"],
    context: "category_theory",
  },
  {
    pattern: "by contradiction",
    is_regex: false,
    primary_tactic: "by_contra",
    fallback_tactics: ["exfalso"],
    context: "general",
  },
  {
    pattern: "by definition",
    is_regex: false,
    primary_tactic: "rfl",
    fallback_tactics: ["unfold", "simp only"],
    context: "general",
  },
];

// =============================================================================
// §7  Knot Theory Types (for combinatorial representations)
// =============================================================================

/** Planar diagram crossing type. */
export type CrossingSign = "positive" | "negative";

/** A crossing in a planar diagram (PD code). */
export interface PDCrossing {
  /** Crossing index. */
  index: number;
  /** Four strand indices meeting at the crossing [i, j, k, l]. */
  strands: [number, number, number, number];
  sign: CrossingSign;
}

/** Planar Diagram representation of a knot. */
export interface PlanarDiagram {
  /** Knot name (e.g., "4_1" for figure-eight). */
  name: string;
  /** Number of crossings. */
  crossing_count: number;
  crossings: PDCrossing[];
  /** Hyperbolic volume (if known). */
  hyperbolic_volume?: number;
  /** Error bound on the volume. */
  volume_error_bound?: number;
}

/** Physical constants used in QOU mass derivations. */
export interface CODATAConstants {
  /** Source (e.g., "CODATA 2026"). */
  source: string;
  values: Record<string, { value: number; uncertainty?: number; unit: string }>;
}
