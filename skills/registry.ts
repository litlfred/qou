/**
 * Skill Registry — Central manifest for the qou assistant framework.
 *
 * Combines actors, capabilities, skills, requirements, packages, and hooks
 * into a single typed registry. This is the TypeScript-authoritative source;
 * registry.json is generated from it.
 */
import type { SkillRegistry } from "./framework/types.js";

// Actors
import { reader } from "./actors/reader.js";
import { collaborator } from "./actors/collaborator.js";
import { owner } from "./actors/owner.js";
import { leanMcp } from "./actors/lean-mcp.js";

// Capabilities
import { gitRead } from "./capabilities/git-read.js";
import { gitPush } from "./capabilities/git-push.js";
import { leanToolchain } from "./capabilities/lean-toolchain.js";
import { leanMcp as leanMcpCap } from "./capabilities/lean-mcp.js";
import { deployAccess } from "./capabilities/deploy-access.js";
import { llmApi } from "./capabilities/llm-api.js";

// Skills (local)
import { editor } from "./local/editor.js";
import { formalizer } from "./local/formalizer.js";
import { categoryTheory } from "./local/category-theory.js";
import { contentValidation } from "./local/content-validation.js";
import { latexValidation } from "./local/latex-validation.js";
import { scientificAccuracy } from "./local/scientific-accuracy.js";
import { readabilityEditing } from "./local/readability-editing.js";
import { leanGeneration } from "./local/lean-generation.js";
import { leanProofReview } from "./local/lean-proof-review.js";
import { proofTriage } from "./local/proof-triage.js";
import { proofStatusTracking } from "./local/proof-status-tracking.js";
import { proofSimplifier } from "./local/proof-simplifier.js";
import { ontologist } from "./local/ontologist.js";
import { contentBlockReview } from "./local/content-block-review.js";
import { chapterAnalysis } from "./local/chapter-analysis.js";
import { criticalPathAnalysis } from "./local/critical-path-analysis.js";
import { todoReview } from "./local/todo-review.js";
import { paperImporter } from "./local/paper-importer.js";
import { testEngineer } from "./local/test-engineer.js";
import { deploymentAuth } from "./local/deployment-auth.js";
import { leanEnvironmentSetup } from "./local/lean-environment-setup.js";
import { docsGeneration } from "./local/docs-generation.js";

// Requirements
import { sessionStart } from "./requirements/session-start.js";
import { contentChangeReview } from "./requirements/content-change-review.js";
import { sorryCitation } from "./requirements/sorry-citation.js";
import { commitHygiene } from "./requirements/commit-hygiene.js";

// Role assignments
import { roleAssignments } from "./roles/role-assignments.js";

export const registry: SkillRegistry = {
  schemaVersion: "1.0",
  repository: "litlfred/qou",

  actors: [reader, collaborator, owner, leanMcp],

  capabilities: [
    gitRead,
    gitPush,
    leanToolchain,
    leanMcpCap,
    deployAccess,
    llmApi,
  ],

  skills: [
    editor,
    formalizer,
    categoryTheory,
    contentValidation,
    latexValidation,
    scientificAccuracy,
    readabilityEditing,
    leanGeneration,
    leanProofReview,
    proofTriage,
    proofStatusTracking,
    proofSimplifier,
    ontologist,
    contentBlockReview,
    chapterAnalysis,
    criticalPathAnalysis,
    todoReview,
    paperImporter,
    testEngineer,
    deploymentAuth,
    leanEnvironmentSetup,
    docsGeneration,
  ],

  requirements: [sessionStart, contentChangeReview, sorryCitation, commitHygiene],

  packages: [
    {
      name: "claude-scientific-skills",
      repo: "K-Dense-AI/claude-scientific-skills",
      path: "scientific-skills",
      ref: "main",
      skills: [
        "arxiv-database",
        "citation-management",
        "hypothesis-generation",
        "latex-posters",
        "literature-review",
        "matplotlib",
        "peer-review",
        "scientific-brainstorming",
        "scientific-critical-thinking",
        "scientific-visualization",
        "scientific-writing",
        "sympy",
      ],
    },
  ],

  hooks: [
    {
      event: "SessionStart",
      commands: [
        { type: "command", command: "./scripts/session-start-coord-sweep.sh" },
        { type: "command", command: "./scripts/lean-build-bg.sh &" },
      ],
    },
    {
      event: "PostToolUse",
      matcher: "Edit|Write",
      commands: [
        { type: "command", command: "./scripts/render-on-change.sh" },
      ],
    },
    {
      event: "UserPromptSubmit",
      commands: [
        { type: "command", command: "./scripts/greeting-task-selection.sh", timeout: 5 },
      ],
    },
    {
      event: "PreCommit",
      commands: [
        { type: "command", command: "./scripts/check-no-lean-artifacts.sh" },
      ],
    },
    {
      event: "PostCommit",
      commands: [
        { type: "command", command: "./scripts/check-upstream.sh", timeout: 15 },
      ],
    },
  ],

  roleAssignments,
};
