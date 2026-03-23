# Agent Skills Framework — Design Document

> **Status**: Draft
> **Date**: 2026-03-23
> **Repository**: `litlfred/folio-assistant`

## 1. Problem Statement

AI coding agents (Claude Code, Copilot, etc.) use "skills" — structured instruction sets that guide agent behavior for specific tasks. Currently each repository defines skills ad hoc: YAML frontmatter in markdown files, Python modules, shell scripts, or prose in `CLAUDE.md`. There is no common schema for:

- **What a skill is** (typed metadata, capabilities, dependencies)
- **Who can invoke it** (role hierarchy, capability requirements)
- **What it depends on** (other skills, environment capabilities, workflow requirements)
- **How to validate its output** (conformance statements, validators)

This framework defines a portable TypeScript schema, directory convention, role model, dependency graph, and requirements system that any repository can adopt. It draws on the FHIR R5 resource model (ActorDefinition, Requirements, CapabilityStatement) as a conceptual backbone while remaining domain-agnostic.

---

## 2. Core Concepts

| Concept | What it models | FHIR R5 analog |
|---------|---------------|----------------|
| **Actor** | A human role or system service | `ActorDefinition` |
| **Capability** | Something the environment can provide | `CapabilityStatement` |
| **Skill** | An instruction set an agent can invoke | (no direct analog) |
| **Requirement** | A workflow rule agents must satisfy | `Requirements` |
| **Registry** | Central manifest of all the above | (bundle) |

---

## 3. TypeScript Schema

### 3.1 ActorDefinition

An actor is either a human role (`person`) or a system service (`system`). Roles form a DAG via `inherits` — a role transitively gains all capabilities of its ancestors.

```typescript
export type ActorType = "person" | "system";
export type Conformance = "SHALL" | "SHOULD" | "MAY" | "SHALL NOT";

export interface ActorDefinition {
  id: string;
  name: string;
  type: ActorType;
  description: string;
  /** Role IDs this actor inherits from (DAG). */
  inherits: string[];
  /** Capability IDs this actor possesses. */
  capabilities: string[];
  /** Domain-specific metadata (repo-defined). */
  meta?: Record<string, unknown>;
}
```

**Example hierarchies:**

```
Formal math repo:    reader → collaborator → owner
FHIR IG repo:        viewer → analyst → author → admin
Generic repo:        reader → writer → admin
```

### 3.2 CapabilityDefinition

A capability is a concrete service or tool the environment can provide. Skills declare which capabilities they need; actors declare which they possess. The `detection` field specifies how to probe for availability at session start.

```typescript
export interface CapabilityDefinition {
  id: string;
  name: string;
  description: string;
  detection: CapabilityDetection;
  /** Other capability IDs this depends on. */
  requires?: string[];
}

export type CapabilityDetection =
  | { method: "command"; command: string; expectExitCode?: number }
  | { method: "env-var"; variable: string }
  | { method: "file-exists"; path: string }
  | { method: "mcp-probe"; endpoint: string; healthPath?: string }
  | { method: "always" };
```

**Example capabilities:**

| ID | Detection | Domain |
|----|-----------|--------|
| `git-push` | `command: "git remote"` | Any |
| `lean-toolchain` | `command: "lean --version"` | Formal math |
| `lean-mcp` | `mcp-probe: endpoint` | Formal math |
| `ig-publisher` | `command: "java -jar publisher.jar"` | FHIR IG |
| `sushi-compiler` | `command: "sushi --version"` | FHIR IG |
| `docker` | `command: "docker info"` | Infrastructure |
| `bun-runtime` | `command: "bun --version"` | TypeScript |

### 3.3 SkillDefinition

The core type. A skill has typed metadata (who can invoke it, what it needs, what it validates) and a companion markdown file with instructions the agent reads.

```typescript
export interface SkillDefinition {
  id: string;
  name: string;
  description: string;
  /** Actor IDs that may invoke this skill (inheritance applies). */
  roles: string[];
  /** Capabilities required from the environment. */
  requiredCapabilities: SkillCapabilityRef[];
  /** Dependencies on other skills or requirements. */
  dependsOn?: SkillDependency[];
  /** Agent tools this skill may use. */
  allowedTools?: string[];
  /** Scripts this skill invokes. */
  scripts?: SkillScript[];
  /** MCP service IDs this skill uses. */
  mcpServices?: string[];
  /** Validators to run when this skill makes changes. */
  validators?: SkillValidator[];
  /** Request patterns for auto-routing. */
  routingPatterns?: string[];
  /** Tags for grouping/filtering. */
  tags?: string[];
  /** Source package (undefined = local). */
  package?: string;
}

export interface SkillCapabilityRef {
  capabilityId: string;
  /** What happens when the capability is absent. */
  degradation: "fail" | "warn" | "skip" | "fallback";
  fallbackCapabilityId?: string;
}

export interface SkillDependency {
  ref: string;
  kind: "skill" | "requirement";
  conformance: Conformance;
}

export interface SkillScript {
  /** Path relative to repo root. */
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
```

### 3.4 Requirement

Models workflow rules agents must follow. Uses FHIR R5 conformance verbs (SHALL/SHOULD/MAY) with traceable `satisfiedBy` references.

```typescript
export interface Requirement {
  id: string;
  title: string;
  description: string;
  /** Parent requirement IDs (hierarchy). */
  derivedFrom?: string[];
  /** Actor IDs involved. */
  actors: string[];
  statements: RequirementStatement[];
  tags?: string[];
}

export interface RequirementStatement {
  key: string;
  label: string;
  conformance: Conformance;
  requirement: string;
  actors?: string[];
  /** What satisfies this statement (traceable). */
  satisfiedBy?: SatisfiedByRef[];
  /** Other statement keys this depends on (ordering). */
  dependsOn?: string[];
}

export interface SatisfiedByRef {
  kind: "skill" | "capability" | "requirement-statement";
  ref: string;
}
```

### 3.5 SkillRegistry

The central manifest. Generated by scanning the skill directory tree.

```typescript
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

export interface SkillPackageRef {
  name: string;
  repo: string;
  path: string;
  ref: string;
  skills: string[];
}

export interface SessionHook {
  event: "SessionStart" | "PostToolUse" | "PreCommit"
       | "PostCommit" | "UserPromptSubmit";
  matcher?: string;
  commands: HookCommand[];
}

export interface HookCommand {
  type: "command";
  command: string;
  timeout?: number;
}
```

### 3.6 RoleAssignment

Maps user identities to actor roles. Evaluated at session start.

```typescript
export interface RoleAssignment {
  userPattern: string;
  identitySource: "git-config" | "github-oauth" | "google-oauth"
                 | "env-var" | "bearer-token" | "default";
  actorId: string;
  /** Higher priority wins when multiple patterns match. */
  priority: number;
}
```

---

## 4. Directory Structure

Every adopting repository uses this layout under `.claude/skills/`:

```
.claude/skills/
  registry.ts              ← Generated (auto-built from below)
  registry.json            ← Generated JSON Schema (for tooling)

  actors/                  ← Role and system actor definitions
    <actor-id>.ts

  capabilities/            ← Environment capability definitions
    <capability-id>.ts

  requirements/            ← Workflow requirements
    <requirement-id>.ts

  local/                   ← Repo-specific skills
    <skill-id>.md          ← Instructions (agent reads this)
    <skill-id>.ts          ← Structured metadata

  <package-name>/          ← External skill packages (synced)
    <skill-name>/
      SKILL.md
      skill.ts
      assets/

  roles/
    role-assignments.ts    ← User-to-role mapping

  hooks/
    session-start.sh       ← Environment + role detection
    detect-role.sh         ← Identity resolution
```

**Convention**: every local skill has both a `.md` (instructions the agent reads) and a `.ts` (typed metadata for routing, validation, and registry generation). The `.md` is authoritative for agent behavior; the `.ts` enables programmatic operations.

---

## 5. Role Hierarchy and Capability Resolution

### 5.1 Role Inheritance

Roles form a DAG. The runtime computes the transitive closure of capabilities by walking `inherits` edges. Each repo defines its own hierarchy — the framework imposes no fixed roles.

### 5.2 Session Start Protocol

At session start, a hook:

1. **Identifies the user** — git config, OAuth token, env var, bearer token, or default.
2. **Matches against `role-assignments.ts`** — highest priority match wins.
3. **Computes effective capabilities** — transitive closure of the matched actor's `capabilities` plus inherited capabilities.
4. **Probes environment capabilities** — runs each `CapabilityDefinition.detection` check.
5. **Writes session context** — stores resolved role + available capabilities for subsequent tool calls.

### 5.3 Skill Activation

When a skill is invoked:

1. **Role check**: user's actor must have a role in `skill.roles` (or inherit one).
2. **Capability check**: for each `requiredCapability`, probe availability.
3. **Degradation**: if a capability is missing, apply the strategy:
   - `fail` — refuse to activate
   - `warn` — activate with a warning
   - `skip` — silently omit capability-dependent features
   - `fallback` — try `fallbackCapabilityId`

---

## 6. Dependency Graph

### 6.1 Dependency Types

| Source | Target | Resolution |
|--------|--------|------------|
| Skill → Skill | Co-activate dependent skill | Pre-activation |
| Skill → Requirement | Validate output against requirement | Post-execution |
| Skill → Capability | Probe environment | Pre-activation |
| Requirement → Requirement | Transitive validation | Post-execution |

### 6.2 Resolution Algorithm

```
resolveSkillDeps(skillId, registry):
  1. Role check         → "forbidden" if user lacks access
  2. Capability check   → apply degradation per capability
  3. Skill deps (recursive) → "missing-dependency" if SHALL dep fails
  4. Requirement deps   → verify requirement exists (validated post-exec)
  return status: "ok" | "forbidden" | "missing-capability" | "missing-dependency"
```

---

## 7. Requirements Model

### 7.1 Requirement Hierarchy

Requirements form a tree via `derivedFrom`. Each statement carries a conformance level and traceable `satisfiedBy` references.

```
req:agent-workflow (root)
  ├── req:session-start
  │     - detect-role (SHALL)
  │     - check-capabilities (SHALL)
  │     - check-todos (SHOULD)
  ├── req:content-change
  │     - validate-schema (SHALL)
  │     - review-output (SHALL)
  │     - review-style (SHOULD)
  └── req:commit-hygiene
        - no-build-artifacts (SHALL)
        - no-secrets (SHALL)
        - pin-dependencies (SHALL)
```

Repos extend this tree with domain-specific requirements (e.g., `req:sorry-citation` for formal math, `req:fhir-validation` for FHIR IGs).

### 7.2 Verification Chain

Each `satisfiedBy` reference is automatically checkable:
- `kind: "skill"` — registry verifies the skill exists and is accessible
- `kind: "capability"` — session hook checks detection method
- `kind: "requirement-statement"` — transitive (the referenced statement must also be satisfied)

### 7.3 FHIR JSON Generation (optional)

For FHIR-based repos, a build script converts TypeScript requirements into FHIR R5 `Requirements` JSON resources:

| TypeScript | FHIR R5 |
|------------|---------|
| `id` | `Requirements.id` |
| `title` | `Requirements.title` |
| `derivedFrom` | `Requirements.derivedFrom` |
| `actors` | `Requirements.actor[]` |
| `statements[].key` | `Requirements.statement[].key` |
| `statements[].conformance` | `Requirements.statement[].conformance` |
| `statements[].satisfiedBy` | `Requirements.statement[].satisfiedBy` |

---

## 8. Concrete Example: Session Start Requirement

```typescript
import type { Requirement } from "@agent-skills/core";

export default {
  id: "req:session-start",
  title: "Session Start Protocol",
  description: "Every agent session must detect the user role and check "
    + "environment capabilities before proceeding.",
  derivedFrom: ["req:agent-workflow"],
  actors: ["reader", "collaborator", "owner"],
  statements: [
    {
      key: "detect-role",
      label: "Detect user role",
      conformance: "SHALL",
      requirement: "The agent MUST determine the user's role at session "
        + "start by checking identity sources against the role assignment table.",
      satisfiedBy: [{ kind: "capability", ref: "role-detection" }],
    },
    {
      key: "check-capabilities",
      label: "Check environment capabilities",
      conformance: "SHALL",
      requirement: "The agent MUST probe for all capabilities referenced "
        + "by skills the user's role can access.",
      dependsOn: ["detect-role"],
      satisfiedBy: [{ kind: "skill", ref: "editor" }],
    },
    {
      key: "check-todos",
      label: "Check open todos",
      conformance: "SHOULD",
      requirement: "The agent SHOULD check for open todos and present "
        + "a summary to the user.",
      dependsOn: ["detect-role"],
      satisfiedBy: [{ kind: "skill", ref: "todo-review" }],
    },
  ],
  tags: ["common", "session"],
} satisfies Requirement;
```

---

## 9. Adopting the Framework

### 9.1 Minimal adoption (any repo)

1. `npm install @agent-skills/core` (or vendor the types)
2. Create `.claude/skills/actors/` with at least one role
3. Create `.claude/skills/local/` with `.md` + `.ts` pairs for each skill
4. Run the registry generator to produce `registry.ts`
5. Add a `SessionStart` hook that runs `detect-role.sh`

### 9.2 Full adoption

Add `capabilities/`, `requirements/`, external `packages/`, and `validators/` as needed. The framework scales from a single skill to hundreds.

### 9.3 Package distribution

Skills can be shared across repos via `SkillPackageRef` entries in the registry. A nightly sync script pulls skills from external repos, parses their `SKILL.md` YAML frontmatter, and generates stub `SkillDefinition` objects.

---

## 10. Implementation Deliverables

| Deliverable | Description |
|-------------|-------------|
| `@agent-skills/core` | npm package with TypeScript types + Zod schemas |
| `generate-registry` | CLI that scans `.claude/skills/` and produces `registry.ts` + `registry.json` |
| `detect-role.sh` | Session-start hook for identity resolution |
| `check-capabilities.sh` | Probes environment capabilities from registry |
| `fhir-export` (optional) | Generates FHIR R5 JSON from requirements/actors |
| Example repos | Starter templates for common repo patterns |
