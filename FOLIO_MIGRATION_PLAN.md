# Folio Assistant Migration Plan

## Vision

**folio-assistant** is a standalone, repo-agnostic content assistant platform.
Users subscribe it to any GitHub repo containing structured content. GitHub
OAuth controls access — repo permissions map to folio roles. Content-specific
editing is delegated to specialized editor skills that live in the content repo.

The originating content repo becomes a pure content repo. All generic
infrastructure (auth, server, UI, deploy) lives in folio-assistant.

---

## Architecture

```
┌──────────────────────────────────────────────────────┐
│                   folio-assistant                      │
│                                                        │
│  ┌──────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │ Auth     │  │ Folio Server │  │ Assistant UI   │  │
│  │ Gateway  │  │ (MCP + HTTP) │  │ (SPA)          │  │
│  └────┬─────┘  └──────┬───────┘  └────────────────┘  │
│       │               │                                │
│  ┌────┴───────────────┴───────────────────────────┐   │
│  │           Content Adapter Layer                │   │
│  │  ┌──────────────┐  ┌────────────────────────┐ │   │
│  │  │ paper-adapter │  │ guideline-adapter     │ │   │
│  │  └──────────────┘  └────────────────────────┘ │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  ┌────────────────────────────────────────────────┐   │
│  │           Skill Package Registry               │   │
│  │  authoring-math │ authoring-health │ lifecycle │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  ┌────────────────────────────────────────────────┐   │
│  │           Deploy Infrastructure                │   │
│  │  Docker Compose │ Caddy │ Cloud │ CI/CD        │   │
│  └────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────┘
          │                    │
          ▼                    ▼
   ┌──────────────┐    ┌──────────────┐
   │ Content      │    │ Content      │
   │ Repo A       │    │ Repo B       │
   │ (papers)     │    │ (guidelines) │
   │              │    │              │
   │ content/     │    │ input/       │
   │ feedback/    │    │ feedback/    │
   │ .claude/     │    │ .claude/     │
   │   skills/    │    │   skills/    │
   └──────────────┘    └──────────────┘
```

### Key Design Decisions

1. **Two access modes: private (default) and public.**

   Every repo subscription defaults to **private mode**. Public mode must be
   explicitly enabled via `"visibility": "public"` in the folio-assistant
   deployment config.

   **Private mode** (default):
   - **GitHub OAuth** → collaborator/owner roles (repo write/admin access)
   - **Google OAuth** → viewer role, **gated by whitelist** (`google-viewers.txt`)
   - Whitelist is manually maintained by repo owner (protected file)

   **Public mode** (opt-in per repo):
   - **GitHub OAuth** → collaborator/owner roles (same as private)
   - **Google OAuth** → viewer role, **open to any Google account** (no whitelist)
   - Useful for public-facing content (published guidelines, open-access papers)
   - Must be explicitly set: `"visibility": "public"` in subscription config

   ```json
   {
     "subscriptions": [
       {
         "repo": "org/private-content",
         "type": "paper",
         "visibility": "private"
       },
       {
         "repo": "org/public-content",
         "type": "guideline",
         "visibility": "public"
       }
     ]
   }
   ```

   The auth gateway checks visibility per-repo:
   - Private → Google login succeeds only if email is in `google-viewers.txt`
   - Public → any authenticated Google user gets viewer role
   - GitHub permissions always checked against the actual repo via API

2. **GitHub OAuth for collaborators, Google OAuth for viewers.** GitHub repo
   permissions determine collaborator/owner roles. Google OAuth provides a
   lightweight viewer path — whitelisted in private mode, open in public mode.

3. **Repo subscription model.** folio-assistant stores a list of subscribed
   repos. Each content repo declares its type via a `folio.config.json` at
   its root.

4. **Content adapters.** The folio server loads a content adapter based on
   the repo's declared type. Adapters implement a common interface:
   - `listItems()` → folio index
   - `getOutline(id)` → section/chapter tree
   - `getBlock(id, path)` → content + metadata
   - `renderOutput(id)` → compiled output (PDF, HTML, IG, etc.)
   - `validate(id)` → validation results

5. **feedback/ is universal.** All content types use `feedback/<item>/<block>.json`.
   The folio server manages this generically — no content-specific logic needed.

6. **Content-specific editors are delegated.** The main folio editor handles
   navigation, feedback, and branch management. When a user wants to *edit*
   content, folio dispatches to the content-specific editor skill (which lives
   in the content repo's `.claude/skills/`).

---

## Migration Phases

### Phase 1: Establish folio-assistant core

**Goal:** Move generic infrastructure into folio-assistant, define the content
adapter interface.

#### 1a. Define content adapter interface

```typescript
// src/adapters/types.ts
interface ContentAdapter {
  type: string;                          // "paper" | "guideline" | ...

  // Discovery
  listItems(): Promise<FolioItem[]>;
  getOutline(itemId: string): Promise<Outline>;
  getDetail(itemId: string, path: string): Promise<BlockDetail>;

  // Feedback (universal — handled by core, but adapter can enrich)
  getFeedback(itemId: string, blockId: string): Promise<FeedbackItem[]>;
  addFeedback(itemId: string, blockId: string, fb: NewFeedback): Promise<FeedbackItem>;

  // Rendering (adapter-specific output format)
  renderOutput(itemId: string, format?: string): Promise<Buffer>;

  // Validation (adapter-specific rules)
  validate(itemId: string): Promise<ValidationResult>;

  // Diff
  diff(itemId: string, base: string, head: string): Promise<DiffResult>;
}
```

#### 1b. Move auth gateway

- **GitHub OAuth** → collaborator/owner roles:
  - `GET /repos/{owner}/{repo}/collaborators/{user}/permission` per subscribed repo
  - `push` permission → collaborator role
  - `admin` permission → owner role
  - Read-only or no access → no collaborator/owner grant
- **Google OAuth** → viewer role, visibility-dependent:
  - **Private repos** (default): check email against `google-viewers.txt` whitelist
  - **Public repos** (`"visibility": "public"`): any Google-authenticated user gets viewer
  - Whitelist file remains a protected file — owner-managed only
- Keep bearer token bypass for API/CLI access
- Auth gateway reads `visibility` from subscription config per-repo and applies
  the correct check on each request

#### 1c. Move MCP server core

Extract generic parts:
- HTTP server skeleton (both stdio + HTTP modes)
- Role-based middleware
- Feedback CRUD endpoints
- Branch management endpoints (`/api/branches`, `/api/git/*`)
- AI triage endpoint (content-agnostic — takes text, returns assessment)
- Static file serving for assistant UI

Leave behind / make adapter-specific:
- Content manifest parsing (adapter responsibility)
- Format-specific rendering pipelines (LaTeX, FHIR IG Publisher, etc.)
- Domain-specific tool proxying (Lean LSP, FHIR validators, etc.)
- Content-object validation rules

#### 1d. Move assistant UI

- Generalize all terminology → "document" / "item" / "section" / "block"
- Keep: branch selector, feedback panel, diff view, theme toggle
- Abstract: content rendering → pluggable content renderer per adapter
- Add: repo selector (when multiple repos are subscribed)

#### 1e. Move deploy infrastructure

- Docker Compose, Caddy template, provisioning scripts
- CI workflows for building + deploying folio-assistant image
- Generalize config → `folio.config.json`

### Phase 2: Build content adapters

**Goal:** Implement pluggable adapters for each content type.

#### 2a. Paper adapter

For repos containing structured academic papers (content-object triples:
`.ts` manifest + `.md` narrative + optional `.lean` formalization).

```typescript
// src/adapters/paper/index.ts
class PaperContentAdapter implements ContentAdapter {
  type = "paper";

  constructor(private repoPath: string) {}

  async listItems(): Promise<FolioItem[]> {
    // Read folio manifest, resolve paper manifests
  }

  async getOutline(paperId: string): Promise<Outline> {
    // Read paper manifest → chapter manifests → section stubs
  }

  async getDetail(paperId: string, path: string): Promise<BlockDetail> {
    // Read block .ts + .md + optional .lean siblings
  }

  async renderOutput(paperId: string): Promise<Buffer> {
    // content pipeline → LaTeX → PDF
  }

  async validate(paperId: string): Promise<ValidationResult> {
    // Zod schema + constraint rules + AST validation
  }
}
```

Optional extensions registered by this adapter:
- Lean LSP proxy tools (if repo has a `lean/` directory)
- LaTeX preview tools
- Proof status tracking

#### 2b. Guideline adapter (future)

For repos containing structured health guidelines (FHIR resources,
decision tables, CQL logic).

```typescript
class GuidelineContentAdapter implements ContentAdapter {
  type = "guideline";
  // FHIR IG Publisher rendering, FSH validation, etc.
}
```

### Phase 3: Add repo subscription model

**Goal:** Support multiple repos with different content types.

#### 3a. Deployment config

```json
// folio.config.json (deployment-level)
{
  "subscriptions": [
    {
      "repo": "org/repo-a",
      "type": "paper",
      "branch": "main",
      "label": "Research Paper Collection",
      "visibility": "private"
    },
    {
      "repo": "org/repo-b",
      "type": "guideline",
      "branch": "main",
      "label": "Clinical Guidelines",
      "visibility": "public"
    }
  ],
  "domain": "folio.example.org",
  "auth": {
    "github": { "enabled": true },
    "google": { "enabled": true, "viewersWhitelist": "google-viewers.txt" }
  }
}
```

**visibility** (per subscription):
- `"private"` (default if omitted) — Google viewers must be whitelisted
- `"public"` — any Google-authenticated user can view

#### 3b. Repo-level folio manifest

Each subscribed repo declares its content type at its root:

```json
// <content-repo>/folio.config.json
{
  "contentType": "paper",
  "adapter": "paper",
  "feedbackDir": "feedback",
  "skills": ".claude/skills/local"
}
```

#### 3c. Permission model

```
GitHub OAuth (collaborator/owner path):
  → User authenticates with GitHub
  → folio-assistant calls: GET /repos/{owner}/{repo}/collaborators/{user}/permission
  → push → collaborator, admin → owner
  → Caches permission for session duration

Google OAuth (viewer path):
  → User authenticates with Google
  → Check subscription visibility for requested repo:
     - "private" → email must be in google-viewers.txt → viewer role (or reject)
     - "public"  → any Google account → viewer role
  → Viewer can read content + submit feedback (with author name attached)
```

### Phase 4: Slim down content repos

**Goal:** Remove migrated infrastructure from content repos, keep content only.

#### 4a. Remove from content repos

- `deploy/auth-gateway/` → lives in folio-assistant
- `scripts/mcp-server/` → generic parts in folio-assistant, adapter there too
- `assistant/` → lives in folio-assistant
- `deploy/docker-compose.folio.yml` → lives in folio-assistant
- `deploy/Caddyfile.folio.template` → lives in folio-assistant
- `deploy/provision*.sh`, `deploy/update-server.sh` → lives in folio-assistant
- `.github/workflows/deploy-folio.yml` → lives in folio-assistant
- Domain-specific MCP config → replaced by `folio.config.json`

#### 4b. Keep in content repos

- Content directories — all authored content (authoritative source)
- Domain-specific tooling (Lean, FHIR, etc.)
- `.claude/skills/local/` — content-specific skills
- `feedback/` — feedback storage (gitignored)
- `folio.config.json` — declares content type for folio-assistant
- Content-specific CI workflows (build, test, publish)

#### 4c. Update .mcp.json in content repos

```json
{
  "mcpServers": {
    "folio-assistant": {
      "url": "https://folio.example.org/mcp"
    }
  }
}
```

Or for local development:
```json
{
  "mcpServers": {
    "folio-assistant": {
      "command": "npx",
      "args": ["folio-assistant", "--stdio", "--repo", "."]
    }
  }
}
```

---

## File-Level Migration Map

| Source (content repo) | Destination (folio-assistant) | Changes needed |
|----------------------|------------------------------|----------------|
| `scripts/mcp-server/server.ts` | `src/server.ts` | Extract generic HTTP/MCP skeleton; content-specific logic → adapter |
| `scripts/mcp-server/git.ts` | `src/git.ts` | Reusable as-is (branch ops are generic) |
| `scripts/mcp-server/paths.ts` | `src/paths.ts` | Parameterize repo root |
| `scripts/mcp-server/tools/render.ts` | `src/adapters/paper/tools/render.ts` | Adapter-specific |
| `scripts/mcp-server/tools/validate.ts` | `src/adapters/paper/tools/validate.ts` | Adapter-specific |
| `scripts/mcp-server/tools/preview.ts` | `src/tools/preview.ts` | Generic (formula/diagram preview) |
| `scripts/mcp-server/tools/preferences.ts` | `src/tools/preferences.ts` | Generic |
| `scripts/mcp-server/tools/lean.ts` | `src/adapters/paper/tools/lean.ts` | Adapter-specific extension |
| `scripts/mcp-server/tools/check-deps.ts` | `src/tools/check-deps.ts` | Generic |
| `deploy/auth-gateway/server.ts` | `src/auth/server.ts` | Replace whitelists with GitHub API + visibility check |
| `assistant/app.js` | `src/ui/app.js` | Generalize terminology, add repo selector |
| `assistant/index.html` | `src/ui/index.html` | Add repo selector |
| `assistant/styles.css` | `src/ui/styles.css` | Minimal changes |
| `deploy/docker-compose.folio.yml` | `deploy/docker-compose.yml` | Generalize service names |
| `deploy/Caddyfile.folio.template` | `deploy/Caddyfile.template` | Minimal changes |
| `deploy/provision-hetzner.sh` | `deploy/provision.sh` | Generalize cloud provider |
| `deploy/self-update-folio.sh` | `deploy/self-update.sh` | Update repo refs |
| Domain-specific MCP config | `folio.config.json` | New schema with subscriptions |

---

## Skills Audit

Skills in folio-assistant must be content-agnostic. Content-specific skills
stay in their respective content repos.

### Skills that move to folio-assistant (generic)

These skills are content-type-independent and belong in the platform:

| Skill | Current location | Notes for generalization |
|-------|-----------------|------------------------|
| `content-lifecycle/` | folio-assistant (already there) | 8-stage workflow — already generic |
| `deployment-auth` | content repo `.claude/skills/` | Remove content-specific examples, generalize OAuth docs |
| `editor` (core parts) | content repo `.claude/skills/` | Extract generic session-start, triage, branch coordination; remove content-specific refs |
| `todo-review` | content repo `.claude/skills/` | Already generic — references `feedback/` directory |
| `readability-editing` | content repo `.claude/skills/` | Prose editing is content-agnostic — remove domain-specific examples |

### Skills that stay in content repos (domain-specific)

| Skill | Why it stays |
|-------|-------------|
| `formalizer` | Lean-specific proof writing |
| `category-theory` | Math domain knowledge |
| `lean-generation` | Lean code generation |
| `lean-proof-review` | Lean-specific review |
| `lean-build-fix` | Lean toolchain |
| `proof-triage` | Proof-specific prioritization |
| `proof-simplifier` | Proof-specific optimization |
| `proof-status-tracking` | Lean formalization status |
| `lean-environment-setup` | Lean toolchain setup |
| `scientific-accuracy` | Domain-specific fact-checking |
| `latex-validation` | LaTeX-specific (moves with paper adapter) |
| `content-validation` | Schema-specific (moves with paper adapter) |
| `content-block-review` | Content-object-specific review |
| `ontologist` | Domain-specific terminology |
| `paper-importer` | Paper-specific import |
| `critical-path-analysis` | Proof dependency analysis |
| `chapter-analysis` | Paper structure analysis |

### Skills to audit and generalize

Each skill moving to folio-assistant needs these changes:

1. **Remove hardcoded content references** — no specific paper titles, theorem
   names, chapter numbers, or domain terminology in skill instructions
2. **Parameterize examples** — use placeholders like `<content-item>`,
   `<block-name>`, `<section>` instead of specific content references
3. **Remove tool assumptions** — don't assume Lean MCP, LaTeX tools, etc.
   are available; check adapter capabilities
4. **Generalize role descriptions** — "reviewer" not "proof reviewer",
   "content block" not "theorem block"
5. **Update routing tables** — skill routing in folio-assistant should be
   adapter-aware: the adapter declares which skills it supports

### Adapter-declared skill routing

Each content adapter declares which skills it requires/supports:

```json
// In adapter package-manifest.json
{
  "adapter": "paper",
  "requiredSkills": [
    "content-validation",
    "latex-validation",
    "scientific-accuracy"
  ],
  "optionalSkills": [
    "formalizer",
    "lean-generation",
    "lean-proof-review"
  ]
}
```

The folio editor checks the active adapter's skill list before routing
user requests. If a skill isn't available for the current content type,
the editor explains this rather than failing silently.

---

## Content Type Extension Points

To add a new content type:

1. Create `src/adapters/<type>/index.ts` implementing `ContentAdapter`
2. Add a `package-manifest.json` declaring required/optional skills
3. Register the adapter in the adapter registry
4. Content repo adds `folio.config.json` with `"contentType": "<type>"`
5. Subscribe the repo in folio-assistant's deployment config
6. Content repo provides domain-specific skills in `.claude/skills/local/`

The adapter handles:
- How to discover/list content items
- How to parse the content structure
- How to render output (PDF, HTML, IG, etc.)
- How to validate (schema rules, domain rules)
- Which MCP tools to register (Lean LSP, FHIR validator, etc.)

The folio server handles generically:
- Authentication + authorization (GitHub OAuth + Google OAuth)
- Feedback collection + AI triage
- Branch management + diff
- UI navigation + rendering
- Skill routing (adapter-aware)

---

## Cross-Repo PR Strategy

The migration involves coordinated changes across repos:

1. **PR in folio-assistant**: Add core server, auth, UI, adapters,
   deploy infra — extracted and generalized from content repo
2. **PR in content repo**: Remove migrated code, add `folio.config.json`,
   update `.mcp.json` and CI workflows

folio-assistant PRs are independent (additive). Content repo cleanup
PRs depend on folio-assistant being functional.

---

## Immediate Next Steps

1. **Grant folio-assistant repo access** to agent tooling
2. **Start Phase 1a-1b**: Define adapter interface + refactor auth gateway
3. **Create tracking issue** in folio-assistant referencing this plan
4. **Run skills audit**: Review each skill file for content-specific
   references and create generalization tasks
5. **Add `folio.config.json`** to content repo (non-breaking, additive)
