# Common Agent Skills Framework — Design Document

> **Status**: Draft
> **Date**: 2026-03-23
> **Scope**: Cross-repo framework for `qou` (formal math paper) and `smart-base` (WHO FHIR IG)

## 1. Problem Statement

Two fundamentally different repositories — a formal mathematics paper (`qou`) and a WHO FHIR Implementation Guide (`smart-base`) — both use agent skills but with incompatible schemas, directory layouts, and role models. This design defines a common TypeScript schema, directory structure, role hierarchy, skill dependency graph, and requirements model that both repos can adopt.

The FHIR R5 resource model (ActorDefinition, Requirements, CapabilityStatement) provides the conceptual backbone. TypeScript is the authoritative schema; JSON Schema is a generated artifact.

---

## 2. Common TypeScript Schema

All types live in a standalone package (`@agent-skills/core`) that both repos depend on.

### 2.1 ActorDefinition (Role/Persona)

Maps to FHIR R5 `ActorDefinition`.

```typescript
export type ActorType = "person" | "system";
export type Conformance = "SHALL" | "SHOULD" | "MAY" | "SHALL NOT";

export interface ActorDefinition {
  /** Unique identifier (e.g. "reader", "collaborator", "owner", "lean-mcp"). */
  id: string;
  name: string;
  /** person = human user; system = CI bot, MCP server, Docker service. */
  type: ActorType;
  description: string;
  /**
   * Actor IDs this role inherits from (DAG).
   * "collaborator" inherits all capabilities of "reader".
   */
  inherits: string[];
  /**
   * Capabilities this actor possesses.
   * Persons: permissions (e.g. "can-push-git").
   * Systems: services provided (e.g. "lean-diagnostics").
   */
  capabilities: string[];
  /**
   * Domain-specific metadata.
   * qou: { provider: "github", whitelist: "deploy/github-collaborators.txt" }
   * smart-base: { fshResource: "input/actors/BusinessAnalyst.fsh" }
   */
  meta?: Record<string, unknown>;
}
```

### 2.2 CapabilityDefinition

A concrete capability that tools, services, or environments provide. Skills declare which capabilities they require; actors declare which they possess.

```typescript
export interface CapabilityDefinition {
  id: string;
  name: string;
  description: string;
  detection: CapabilityDetection;
  requires?: string[];
}

export type CapabilityDetection =
  | { method: "command"; command: string; expectExitCode?: number }
  | { method: "env-var"; variable: string }
  | { method: "file-exists"; path: string }
  | { method: "mcp-probe"; endpoint: string; healthPath?: string }
  | { method: "always" };
```

### 2.3 SkillDefinition

The core type. Unifies qou's markdown-with-YAML-frontmatter skills and smart-base's Python-module skills.

```typescript
export interface SkillDefinition {
  id: string;
  name: string;
  description: string;
  /** Actor IDs that may invoke this skill (inheriting actors get access transitively). */
  roles: string[];
  requiredCapabilities: SkillCapabilityRef[];
  dependsOn?: SkillDependency[];
  allowedTools?: string[];
  scripts?: SkillScript[];
  mcpServices?: string[];
  validators?: SkillValidator[];
  /** Request patterns that route to this skill. */
  routingPatterns?: string[];
  tags?: string[];
  /** Source package (undefined = local skill). */
  package?: string;
}

export interface SkillCapabilityRef {
  capabilityId: string;
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
```

### 2.4 Requirement (FHIR R5 Requirements)

Models workflow process steps that agents must follow.

```typescript
export interface Requirement {
  id: string;
  title: string;
  description: string;
  derivedFrom?: string[];
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
  satisfiedBy?: SatisfiedByRef[];
  dependsOn?: string[];
}

export interface SatisfiedByRef {
  kind: "skill" | "capability" | "requirement-statement";
  ref: string;
}
```

### 2.5 SkillRegistry

Central manifest listing all skills, actors, capabilities, and requirements.

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
  event: "SessionStart" | "PostToolUse" | "PreCommit" | "PostCommit" | "UserPromptSubmit";
  matcher?: string;
  commands: HookCommand[];
}

export interface HookCommand {
  type: "command";
  command: string;
  timeout?: number;
}
```

### 2.6 RoleAssignment (User-to-Role Mapping)

```typescript
export interface RoleAssignment {
  userPattern: string;
  identitySource: "git-config" | "github-oauth" | "google-oauth" | "env-var" | "bearer-token" | "default";
  actorId: string;
  priority: number;
}
```

---

## 3. Directory Structure

Both repos adopt a common layout under `.claude/skills/`:

```
.claude/
  skills/
    registry.ts              -- Generated SkillRegistry (auto-built from below)
    registry.json            -- Generated JSON Schema version (for FHIR tooling)

    actors/
      reader.ts              -- ActorDefinition
      collaborator.ts
      owner.ts
      lean-mcp.ts            -- (qou) System actor for Lean MCP server
      ig-publisher.ts        -- (smart-base) System actor for IG Publisher

    capabilities/
      git-push.ts            -- CapabilityDefinition
      lean-toolchain.ts      -- (qou)
      lean-mcp.ts            -- (qou)
      ig-publisher.ts        -- (smart-base)
      llm-api.ts             -- (smart-base)

    requirements/
      session-start.ts       -- Common: environment check + role detection
      content-change-review.ts   -- (qou)
      sorry-citation.ts          -- (qou)
      commit-hygiene.ts          -- Common: no artifacts, no secrets
      fhir-validation.ts        -- (smart-base)

    local/
      editor.md              -- Skill instructions (markdown, read by agents)
      editor.ts              -- SkillDefinition (structured metadata)
      formalizer.md           -- (qou)
      formalizer.ts           -- (qou)
      bpmn-author.md         -- (smart-base)
      bpmn-author.ts         -- (smart-base)

    <package-name>/          -- External skill packages (synced)
      <skill-name>/
        SKILL.md
        skill.ts
        assets/

    roles/
      role-assignments.ts    -- RoleAssignment[]

    hooks/
      session-start.sh       -- Common session-start hook
      detect-role.sh         -- Role detection script
```

**Key decisions:**

1. Every local skill has both a `.md` (instructions for the agent) and a `.ts` (structured metadata). The `.md` remains the primary document agents read; the `.ts` enables programmatic routing, validation, and registry generation.

2. External packages keep their existing structure (`SKILL.md` convention). The registry generator synthesizes `SkillDefinition` objects from YAML frontmatter.

3. The `registry.ts` is generated by a build script that scans all `.ts` files in `actors/`, `capabilities/`, `requirements/`, and `local/`, plus parses YAML frontmatter from external packages.

---

## 4. Role Hierarchy and Capability Model

### 4.1 Inheritance

Roles form a DAG via `ActorDefinition.inherits`. The runtime computes the transitive closure of capabilities.

```
qou:        reader -> collaborator -> owner
smart-base: viewer -> analyst -> author -> admin
```

### 4.2 Capability Resolution

When a skill is invoked, the router:

1. Checks the user's actor has a role listed in `skill.roles` (or inherits from one).
2. For each `requiredCapability`, checks availability via `CapabilityDefinition.detection`.
3. Applies degradation strategy: `fail` (refuse), `warn` (activate with warning), `skip` (omit feature), `fallback` (try alternative).

This generalizes qou's existing editor handling of Lean availability (local/remote/degraded/none modes).

### 4.3 Session Start Protocol

The session-start hook resolves a user's effective capabilities by:

1. Determining identity (git config email, GitHub OAuth, Google OAuth, env var, bearer token).
2. Matching against `role-assignments.ts` entries by priority.
3. Computing transitive closure of the matched actor's capabilities.
4. Storing resolved role + capabilities in `/tmp/.claude-session-<pid>.json`.

---

## 5. Skill Dependency Graph

### 5.1 Dependency Types

| Type | Example | Resolution |
|------|---------|------------|
| Skill-to-skill | `formalizer` depends on `category-theory` | Co-activate dependent skills |
| Skill-to-requirement | `formalizer` depends on `req:sorry-citation` | Post-execution validation |
| Skill-to-capability | `formalizer` requires `lean-mcp` | Pre-activation probe |

### 5.2 Resolution Algorithm

```
resolveSkillDeps(skillId, registry):
  1. Check role access → forbidden if user lacks role
  2. Check capabilities → apply degradation strategy per cap
  3. Check skill deps (recursive) → fail if SHALL dep missing
  4. Check requirement deps → verify requirement exists (validated post-exec)
  return { status: "ok" | "forbidden" | "missing-capability" | "missing-dependency" }
```

---

## 6. Requirements as Validators

### 6.1 Requirement Hierarchy

```
req:agent-workflow (root)
  +-- req:session-start
  |     - detect-role (SHALL)
  |     - check-capabilities (SHALL)
  |     - check-todos (SHOULD)
  +-- req:content-change
  |     - validate-schema (SHALL) → content-validation skill
  |     - review-accuracy (SHALL) → scientific-accuracy skill
  |     - review-readability (SHOULD) → readability-editing skill
  +-- req:commit-hygiene
  |     - no-build-artifacts (SHALL)
  |     - no-secrets (SHALL)
  |     - pin-dependencies (SHALL)
  +-- req:sorry-citation [qou-specific]
  |     - ref-annotation (SHALL)
  |     - bib-match (SHALL)
  +-- req:fhir-validation [smart-base-specific]
        - sushi-compile (SHALL)
        - ig-publisher-qa (SHALL)
```

### 6.2 Concrete Example

```typescript
// .claude/skills/requirements/session-start.ts
import type { Requirement } from "@agent-skills/core";

export default {
  id: "req:session-start",
  title: "Session Start Protocol",
  description: "Every agent session must detect the user role and check environment capabilities.",
  derivedFrom: ["req:agent-workflow"],
  actors: ["reader", "collaborator", "owner"],
  statements: [
    {
      key: "detect-role",
      label: "Detect user role",
      conformance: "SHALL",
      requirement: "The agent MUST determine the user's role at session start.",
      satisfiedBy: [{ kind: "capability", ref: "role-detection" }],
    },
    {
      key: "check-capabilities",
      label: "Check environment capabilities",
      conformance: "SHALL",
      requirement: "The agent MUST probe for all capabilities referenced by accessible skills.",
      dependsOn: ["detect-role"],
      satisfiedBy: [{ kind: "skill", ref: "editor" }],
    },
    {
      key: "check-todos",
      label: "Check open todos",
      conformance: "SHOULD",
      requirement: "The agent SHOULD check for open todos and present a summary.",
      dependsOn: ["detect-role"],
      satisfiedBy: [{ kind: "skill", ref: "todo-review" }],
    },
  ],
  tags: ["common", "session"],
} satisfies Requirement;
```

### 6.3 FHIR JSON Schema Generation

A build script converts TypeScript requirement definitions into FHIR R5 Requirements JSON:

| TypeScript field | FHIR R5 Requirements field |
|---|---|
| `id` | `Requirements.id` |
| `title` | `Requirements.title` |
| `description` | `Requirements.description` |
| `derivedFrom` | `Requirements.derivedFrom` |
| `actors` | `Requirements.actor[]` |
| `statements[].key` | `Requirements.statement[].key` |
| `statements[].conformance` | `Requirements.statement[].conformance` |
| `statements[].satisfiedBy` | `Requirements.statement[].satisfiedBy` |

For smart-base, generated FHIR JSON files go directly into `input/requirements/` and publish as part of the IG.

### 6.4 Verification Chain

Each requirement statement with `satisfiedBy` is automatically checkable:
- `satisfiedBy: skill` — registry verifies the skill exists and is accessible
- `satisfiedBy: capability` — session-start hook checks detection
- `satisfiedBy: requirement-statement` — transitive validation

---

## 7. Migration Plan

### 7.1 qou (Phase 1 — non-breaking)

1. Create `.claude/skills/actors/` with `reader.ts`, `collaborator.ts`, `owner.ts`, `lean-mcp.ts`
2. For each of the 21 existing local skills, create a companion `.ts` alongside the `.md` (parse YAML frontmatter, add `requiredCapabilities`, `scripts`, `validators`, `routingPatterns`)
3. Create `.claude/skills/capabilities/` for `git-push`, `lean-toolchain`, `lean-mcp`, `bun-runtime`, `latex-compiler`
4. Create `.claude/skills/requirements/` with workflow requirements from `editor.md` and `CLAUDE.md`
5. Write `scripts/generate-skill-registry.ts` to produce `registry.ts` + `registry.json`
6. Update `skills-config.json` with `schemaVersion` field

### 7.2 qou (Phase 2 — role detection)

7. Add `detect-role.sh` hook, wire into `SessionStart` in `.claude/settings.json`
8. Update `editor.md` routing table to reference registry skill IDs (data-driven routing)

### 7.3 qou (Phase 3 — external packages)

9. Update nightly sync to parse external `SKILL.md` frontmatter into stub `SkillDefinition` objects

### 7.4 smart-base (Phase 1)

1. Move skills from `.github/skills/` to `.claude/skills/local/` with `.md` + `.ts` pairs
2. Create actors from existing FSH `ActorDefinition` resources (with `meta.fshResource` backlink)
3. Define hierarchy: `viewer < analyst < author < admin`
4. Create capabilities: `ig-publisher`, `docker`, `llm-api`, `sushi-compiler`, `git-push`
5. Create requirements for DAK authoring workflow steps
6. Generate `registry.ts` + `registry.json`

### 7.5 smart-base (Phase 2 — FHIR conformance)

7. Script to generate FHIR R5 Requirements JSON from `requirements/*.ts`
8. Script to generate FHIR R5 ActorDefinition JSON from `actors/*.ts` (bidirectional sync with FSH)

### 7.6 smart-base (Phase 3 — Python integration)

9. `SkillDefinition.scripts[]` references existing Python modules with `runtime: "python"`
10. `skills_registry.yaml` replaced by (or generated from) `registry.ts`

---

## 8. Key Implementation Files

| File | Purpose |
|------|---------|
| `schemas/types.ts` | Extend with framework interfaces (or use as pattern for `@agent-skills/core`) |
| `schemas/builders.ts` | Pattern for `actor()`, `skill()`, `capability()`, `requirement()` builders |
| `schemas/constraints.ts` | Zod schema patterns to replicate for new types |
| `.claude/skills/local/editor.md` | Reference implementation for routing + session-start |
| `skills-config.json` | Existing package subscription model (must remain compatible) |
