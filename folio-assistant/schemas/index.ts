/**
 * Unified schema package — public API.
 *
 * ## Content-object model (types, constraints, builders)
 *
 * The authoritative document model for QOU content objects.
 * Used by content blocks, the pipeline, and the viewer.
 *
 * ## CI/Output schemas (qou-types)
 *
 * Proof objects, glossary, coverage, and test infrastructure types
 * consumed by CI pipelines and published to GitHub Pages.
 *
 * @module schemas
 */

// ── Content-object model ────────────────────────────────────────

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
  ProofBlock,
  ProseBlock,
  EquationBlock,
  DiagramBlock,
  LeanRef,
  LeanValidation,
  RenderedAsset,
  Companions,
  FormalizationStatus,
  ObjectKind,
  Section,
  SectionRef,
  Chapter,
  ChapterRef,
  Paper,
  PaperMacro,
  PaperRef,
  Folio,
  Document,
  TodoItem,
  TodoPriority,
  TodoStatus,
  TodoOrigin,
  FeedbackItem,
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
  proof,
  prose,
  equation,
  diagram,
  section,
  sectionRef,
  chapter,
  chapterRef,
  paper,
  paperRef,
  folio,
  document,
  feedbackItem,
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
  ProofSchema,
  ProseSchema,
  EquationSchema,
  DiagramSchema,
  ChapterSchema,
  ChapterRefSchema,
  SectionSchema,
  SectionRefSchema,
  PaperSchema,
  PaperRefSchema,
  FolioSchema,
  DocumentSchema,
  LeanRefSchema,
  TodoItemSchema,
  FeedbackItemSchema,
  CONSTRAINT_RULES,
  type ConstraintRule,
  type ConstraintContext,
} from "./constraints";

// ── CI/Output schemas ───────────────────────────────────────────

export type {
  // Proof objects
  ObjectType,
  ReviewType,
  Verdict,
  Severity,
  ReviewerType,
  DependencyRelation,
  LaTeXLocation,
  LeanReference,
  ReviewIssue,
  LeanReviewStatus,
  ReviewRecord,
  ProofObject,
  DependencyEdge,
  Manuscript,
  ProofObjectsManifest,
  // Glossary
  UniverseLevel,
  LeanDeclKind,
  GlossaryEntry,
  AmbiguityFlag,
  GlossaryManifest,
  // Mapping
  NarrativeMapping,
  MappingManifest,
  // Proof state
  ProofGoal,
  ProofHypothesis,
  ProofStateExport,
  ProofStateManifest,
  // Category theory
  CategoryLevel,
  CategoryGlossaryEntry,
  // Tactic mapping
  TacticMapping,
  // Knot theory
  CrossingSign,
  PDCrossing,
  PlanarDiagram,
  CODATAConstants,
  // Test infrastructure
  TestCategory,
  TestSeverity,
  TestOutcome,
  TestDefinition,
  TestResult,
  TestSummary,
  TestReport,
  // Coverage
  CoverageStatus,
  CoverageEntry,
  CoverageManifest,
} from "./qou-types";

export { DEFAULT_TACTIC_MAPPINGS } from "./qou-types";

// ── Assistant framework schemas ──────────────────────────────────

export type {
  // Actors
  ActorType,
  Conformance,
  ActorDefinition,
  // Capabilities
  CapabilityDetection,
  CapabilityDefinition,
  // Skills
  SkillCapabilityRef,
  SkillDependency,
  SkillScript,
  SkillValidator,
  SkillSchemaRef,
  SkillDefinition,
  // Requirements
  SatisfiedByRef,
  RequirementStatement,
  Requirement,
  // Registry
  SkillPackageRef,
  SessionHook,
  HookCommand,
  RoleAssignment,
  SkillRegistry,
} from "./assistant-types";

export type {
  AptDependency,
  InstallerDependency,
  PythonDependency,
  NodeDependency,
  PackageManifest,
} from "./assistant-package";

// Workflow lifecycle
export type {
  LifecycleStage,
  StageTransition,
  StageSkillBinding,
  WorkflowDefinition,
} from "./assistant-workflow";

export { mathAuthoringWorkflow } from "./assistant-workflow";

// ── Lean package registry ───────────────────────────────────────

export type { LeanPackage, ParsedLeanRef } from "./lean-packages";
export {
  LEAN_PACKAGES,
  LEAN_REF_PATTERN,
  formatLeanRef,
  isLeanPackageName,
  leanPackageByName,
  leanPackageByPaperDir,
  parseLeanRef,
} from "./lean-packages";
