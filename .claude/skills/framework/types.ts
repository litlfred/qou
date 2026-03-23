/**
 * Assistant Framework — Core type definitions.
 *
 * Cross-repository schema for skill management, role-based access control,
 * and capability detection. TypeScript is authoritative; JSON Schema is
 * a generated artifact.
 *
 * Design ref: https://github.com/litlfred/folio-assistant/issues/1
 */

// ---------------------------------------------------------------------------
// Actors
// ---------------------------------------------------------------------------

export type ActorType = "person" | "system";
export type Conformance = "SHALL" | "SHOULD" | "MAY" | "SHALL NOT";

export interface ActorDefinition {
  id: string;
  name: string;
  type: ActorType;
  description: string;
  /** Actor IDs this role inherits from (DAG — no cycles). */
  inherits: string[];
  /** Capability IDs granted to this actor. */
  capabilities: string[];
  meta?: Record<string, unknown>;
}

// ---------------------------------------------------------------------------
// Capabilities
// ---------------------------------------------------------------------------

export type CapabilityDetection =
  | { method: "command"; command: string; expectExitCode?: number }
  | { method: "env-var"; variable: string }
  | { method: "file-exists"; path: string }
  | { method: "mcp-probe"; endpoint: string; healthPath?: string }
  | { method: "always" };

export interface CapabilityDefinition {
  id: string;
  name: string;
  description: string;
  detection: CapabilityDetection;
  /** Other capability IDs this one depends on. */
  requires?: string[];
}

// ---------------------------------------------------------------------------
// Skills
// ---------------------------------------------------------------------------

export interface SkillCapabilityRef {
  capabilityId: string;
  /** What to do when the capability is unavailable. */
  degradation: "fail" | "warn" | "skip" | "fallback";
  fallbackCapabilityId?: string;
}

export interface SkillDependency {
  ref: string;
  kind: "skill" | "requirement";
  conformance: Conformance;
}

export interface SkillScript {
  path: string;
  runtime: "bash" | "python" | "typescript" | "bun";
  phase: "pre" | "execute" | "validate" | "post";
  args?: string[];
}

export interface SkillValidator {
  id: string;
  path: string;
  runtime: "bash" | "python" | "typescript" | "bun";
  scope: "file" | "block" | "chapter" | "project";
}

export interface SkillDefinition {
  id: string;
  name: string;
  description: string;
  /** Roles that may invoke this skill. */
  roles: string[];
  requiredCapabilities: SkillCapabilityRef[];
  dependsOn?: SkillDependency[];
  allowedTools?: string[];
  scripts?: SkillScript[];
  mcpServices?: string[];
  validators?: SkillValidator[];
  /** Regex patterns for routing user requests to this skill. */
  routingPatterns?: string[];
  tags?: string[];
  /** External package this skill belongs to (undefined = local). */
  package?: string;
}

// ---------------------------------------------------------------------------
// Requirements (FHIR R5–aligned)
// ---------------------------------------------------------------------------

export interface SatisfiedByRef {
  kind: "skill" | "capability" | "requirement-statement";
  ref: string;
}

export interface RequirementStatement {
  key: string;
  label: string;
  conformance: Conformance;
  requirement: string;
  actors?: string[];
  satisfiedBy?: SatisfiedByRef[];
  dependsOn?: string[];
}

export interface Requirement {
  id: string;
  title: string;
  description: string;
  derivedFrom?: string[];
  actors: string[];
  statements: RequirementStatement[];
  tags?: string[];
}

// ---------------------------------------------------------------------------
// Registry
// ---------------------------------------------------------------------------

export interface SkillPackageRef {
  name: string;
  repo: string;
  path: string;
  ref: string;
  skills: string[];
  /** Path to the package's PackageManifest (relative to .claude/skills/). */
  manifestPath?: string;
}

export interface SessionHook {
  event:
    | "SessionStart"
    | "PostToolUse"
    | "PreCommit"
    | "PostCommit"
    | "UserPromptSubmit";
  matcher?: string;
  commands: HookCommand[];
}

export interface HookCommand {
  type: "command";
  command: string;
  timeout?: number;
}

export interface RoleAssignment {
  userPattern: string;
  identitySource:
    | "git-config"
    | "github-oauth"
    | "google-oauth"
    | "env-var"
    | "bearer-token"
    | "default";
  actorId: string;
  priority: number;
}

export interface SkillRegistry {
  schemaVersion: "1.0";
  repository: string;
  actors: ActorDefinition[];
  capabilities: CapabilityDefinition[];
  skills: SkillDefinition[];
  requirements: Requirement[];
  packages: SkillPackageRef[];
  hooks: SessionHook[];
}
