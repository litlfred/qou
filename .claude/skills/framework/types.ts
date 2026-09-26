/**
 * Assistant Framework — Re-exports from the authoritative schemas/ directory.
 *
 * The canonical type definitions live in `schemas/assistant-types.ts`.
 * This file re-exports them so that `.claude/skills/` code can import
 * from a relative path without reaching outside its directory tree.
 *
 * Design ref: https://github.com/litlfred/folio-assistant/issues/1
 */
export type {
  ActorType,
  Conformance,
  ActorDefinition,
  CapabilityDetection,
  CapabilityDefinition,
  SkillCapabilityRef,
  SkillDependency,
  SkillScript,
  SkillValidator,
  SkillSchemaRef,
  SkillDefinition,
  SatisfiedByRef,
  RequirementStatement,
  Requirement,
  SkillPackageRef,
  SessionHook,
  HookCommand,
  RoleAssignment,
  SkillRegistry,
} from "../../../folio-assistant/cat-harness/schemas/assistant-types.js";
