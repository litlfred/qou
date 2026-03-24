# Folio Assistant Migration Plan

## Vision

**folio-assistant** becomes a standalone, repo-agnostic assistant platform.
Users subscribe it to any GitHub repo containing structured content (papers,
WHO SMART guidelines, etc.). Authentication is via GitHub OAuth — repo access
= folio access. Content-specific editing is delegated to specialized editors
that live in the content repo.

**qou** becomes a pure content repo — papers, Lean proofs, and content-specific
skills only. All generic infrastructure moves to folio-assistant.

---

## Current State

### What lives in qou today (to be migrated)

| Component | Location in qou | Lines | Purpose |
|-----------|----------------|-------|---------|
| MCP Server | `scripts/mcp-server/server.ts` | ~2,500 | Content serving, feedback, diff, AI triage, MCP tools |
| Auth Gateway | `deploy/auth-gateway/server.ts` | ~520 | Dual OAuth, role sessions, proxy |
| Assistant UI | `assistant/` | ~1,800 | Paper viewer, feedback panel, branch mgmt |
| Deploy Stack | `deploy/` | ~10 scripts | Docker Compose, Caddy, Hetzner provisioning |
| Docker Build | `.github/docker/Dockerfile.lean-mcp` | — | CI image build |
| Deploy Workflow | `.github/workflows/deploy-folio.yml` | — | Auto-deploy |
| Config | `lean-mcp.config.json` | 30 | Domain, auth, image refs |

### What already exists in folio-assistant

| Component | Purpose |
|-----------|---------|
| `schemas/` | Zod-based type system (ActorDefinition, SkillDefinition, CapabilityDefinition) |
| `skills/authoring-math/` | Math/Lean skill package manifest |
| `skills/authoring-who-smart-guidelines/` | WHO SMART skill package |
| `skills/content-lifecycle/` | Generic 8-stage content workflow |
| `Dockerfile` | Multi-skill Docker image (Ubuntu + Lean + FHIR + LaTeX) |
| Scripts | generate-docs, generate-schemas, validate-skills |

---

## Architecture After Migration

```
┌─────────────────────────────────────────────────────┐
│                  folio-assistant                      │
│                                                       │
│  ┌──────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Auth     │  │ Folio Server │  │ Assistant UI  │  │
│  │ Gateway  │  │ (MCP + HTTP) │  │ (SPA)         │  │
│  └────┬─────┘  └──────┬───────┘  └───────────────┘  │
│       │               │                               │
│  ┌────┴───────────────┴──────────────────────────┐   │
│  │          Content Adapter Layer                 │   │
│  │  ┌─────────────┐  ┌──────────────────────┐   │   │
│  │  │ paper-adapter│  │ smart-guide-adapter  │   │   │
│  │  │ (qou-style)  │  │ (FHIR/WHO)          │   │   │
│  │  └─────────────┘  └──────────────────────┘   │   │
│  └───────────────────────────────────────────────┘   │
│                                                       │
│  ┌───────────────────────────────────────────────┐   │
│  │          Skill Package Registry               │   │
│  │  authoring-math │ authoring-who │ lifecycle   │   │
│  └───────────────────────────────────────────────┘   │
│                                                       │
│  ┌───────────────────────────────────────────────┐   │
│  │          Deploy Infrastructure                │   │
│  │  Docker Compose │ Caddy │ Hetzner │ CI/CD    │   │
│  └───────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
          │                    │
          ▼                    ▼
   ┌──────────┐        ┌──────────────┐
   │   qou    │        │  smart-base  │
   │ (papers) │        │ (guidelines) │
   │          │        │              │
   │ content/ │        │ input/       │
   │ lean/    │        │ fsh/         │
   │ feedback/│        │ feedback/    │
   └──────────┘        └──────────────┘
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
   - This is the current qou model — unchanged

   **Public mode** (opt-in per repo):
   - **GitHub OAuth** → collaborator/owner roles (same as private)
   - **Google OAuth** → viewer role, **open to any Google account** (no whitelist)
   - Useful for public-facing content (e.g. published WHO guidelines)
   - Must be explicitly set: `"visibility": "public"` in subscription config

   ```json
   // folio-assistant deployment config
   {
     "subscriptions": [
       {
         "repo": "litlfred/qou",
         "type": "paper",
         "visibility": "private"
       },
       {
         "repo": "litlfred/smart-base",
         "type": "smart-guideline",
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
   repos (e.g. `litlfred/qou`, `litlfred/smart-base`). Each repo declares
   its content type via a `folio.config.json` at its root.

3. **Content adapters.** The folio server loads a content adapter based on
   the repo's declared type. Adapters implement a common interface:
   - `listPapers()` / `listGuides()` → folio index
   - `getOutline(id)` → chapter/section tree
   - `getBlock(id, path)` → content + metadata
   - `renderPdf(id)` → compiled output
   - `validate(id)` → validation results

4. **feedback/ is universal.** All content types use `feedback/<item>/<block>.json`.
   The folio server manages this generically — no content-specific logic needed.

5. **Content-specific editors are delegated.** The main folio editor handles
   navigation, feedback, and branch management. When a user wants to *edit*
   content, folio dispatches to the content-specific editor skill (which lives
   in the content repo's `.claude/skills/`).

---

## Migration Phases

### Phase 1: Establish folio-assistant core (folio-assistant repo)

**Goal:** Move generic infrastructure to folio-assistant, define the content
adapter interface.

#### 1a. Define content adapter interface

```typescript
// folio-assistant/src/adapters/types.ts
interface ContentAdapter {
  type: string;                          // "paper" | "smart-guideline" | ...

  // Discovery
  listItems(): Promise<FolioItem[]>;
  getOutline(itemId: string): Promise<Outline>;
  getDetail(itemId: string, path: string): Promise<BlockDetail>;

  // Feedback (universal)
  getFeedback(itemId: string, blockId: string): Promise<FeedbackItem[]>;
  addFeedback(itemId: string, blockId: string, fb: NewFeedback): Promise<FeedbackItem>;

  // Rendering
  renderPdf(itemId: string): Promise<Buffer>;

  // Validation
  validate(itemId: string): Promise<ValidationResult>;

  // Diff
  diff(itemId: string, base: string, head: string): Promise<DiffResult>;
}
```

#### 1b. Move auth gateway (from qou `deploy/auth-gateway/`)

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

#### 1c. Move MCP server core (from qou `scripts/mcp-server/`)

Extract generic parts:
- HTTP server skeleton (both stdio + HTTP modes)
- Role-based middleware
- Feedback CRUD endpoints
- Branch management endpoints (`/api/branches`, `/api/git/*`)
- AI triage endpoint (content-agnostic — takes text, returns assessment)
- Static file serving for assistant UI

Leave behind / make adapter-specific:
- Paper manifest parsing (`importTsBranch`, content schema awareness)
- LaTeX rendering pipeline
- Lean tool proxying
- Content-object validation

#### 1d. Move assistant UI (from qou `assistant/`)

- Generalize "paper" terminology → "document" / "item"
- Keep: branch selector, feedback panel, diff view, theme toggle
- Abstract: content rendering (paper viewer → pluggable content renderer)
- Add: repo selector (when multiple repos are subscribed)

#### 1e. Move deploy infrastructure (from qou `deploy/`)

- Docker Compose, Caddy template, provisioning scripts
- Generalize `lean-mcp.config.json` → `folio.config.json`
- CI workflows for building + deploying folio-assistant image

### Phase 2: Create paper content adapter (folio-assistant repo)

**Goal:** Re-implement qou's content serving as a pluggable adapter.

#### 2a. Paper adapter implementation

```typescript
// folio-assistant/src/adapters/paper/index.ts
class PaperContentAdapter implements ContentAdapter {
  type = "paper";

  constructor(private repoPath: string) {}

  async listItems(): Promise<FolioItem[]> {
    // Read content/folio.ts, resolve paper manifests
  }

  async getOutline(paperId: string): Promise<Outline> {
    // Read paper manifest → chapter manifests → section stubs
  }

  async getDetail(paperId: string, path: string): Promise<BlockDetail> {
    // Read block .ts + .md + .lean siblings
  }

  async renderPdf(paperId: string): Promise<Buffer> {
    // content pipeline → LaTeX → latexmk
  }

  async validate(paperId: string): Promise<ValidationResult> {
    // Zod schema + constraint rules + AST validation
  }
}
```

#### 2b. Register Lean MCP tools as optional extension

- If repo has `lean/` directory, proxy lean-lsp-mcp tools
- If not, Lean tools are simply not registered

### Phase 3: Add repo subscription model (folio-assistant repo)

**Goal:** Support multiple repos with different content types.

#### 3a. Subscription config

```json
// folio-assistant/folio.config.json (deployment config)
{
  "subscriptions": [
    {
      "repo": "litlfred/qou",
      "type": "paper",
      "branch": "main",
      "label": "Quantum Observable Universe",
      "visibility": "private"
    },
    {
      "repo": "litlfred/smart-base",
      "type": "smart-guideline",
      "branch": "main",
      "label": "WHO SMART Guidelines",
      "visibility": "public"
    }
  ],
  "domain": "folio.litlfred.org",
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

Each subscribed repo declares its content type:

```json
// qou/folio.config.json (in content repo root)
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

### Phase 4: Slim down qou (qou repo)

**Goal:** Remove migrated infrastructure, add folio.config.json, keep content.

#### 4a. Remove from qou

- `deploy/auth-gateway/` → lives in folio-assistant
- `scripts/mcp-server/` → generic parts in folio-assistant, paper adapter there too
- `assistant/` → lives in folio-assistant
- `deploy/docker-compose.folio.yml` → lives in folio-assistant
- `deploy/Caddyfile.folio.template` → lives in folio-assistant
- `deploy/provision*.sh`, `deploy/update-server.sh` → lives in folio-assistant
- `.github/workflows/deploy-folio.yml` → lives in folio-assistant
- `lean-mcp.config.json` → replaced by `folio.config.json`

#### 4b. Keep in qou

- `content/` — all content objects (authoritative)
- `lean/` — Lean formalization
- `chapters/` — generated LaTeX
- `main.tex`, `references.bib` — LaTeX preamble
- `.claude/skills/local/` — content-specific skills
- `feedback/` — feedback storage (gitignored)
- `folio.config.json` — declares content type for folio-assistant
- `.github/workflows/publish.yml`, `lean_ci.yml`, `blueprint.yml` — content CI
- `scripts/check-lean.sh`, `scripts/setup-lean-mcp.sh` — Lean tooling

#### 4c. Update .mcp.json

```json
{
  "mcpServers": {
    "folio-assistant": {
      "url": "https://folio.litlfred.org/mcp"
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

## Cross-Repo PR Strategy

Since folio-assistant is a separate repo, the migration involves coordinated
changes:

1. **PR in folio-assistant**: Add core server, auth, UI, paper adapter,
   deploy infra — all extracted from qou
2. **PR in qou**: Remove migrated code, add `folio.config.json`, update
   `.mcp.json` and CI workflows

These can reference each other. folio-assistant PRs are independent (additive).
The qou cleanup PR depends on folio-assistant being functional.

**Note:** My GitHub MCP tools are scoped to `litlfred/qou` only. To create
PRs in `litlfred/folio-assistant`, you'll need to either:
- Grant me access to that repo in the MCP config
- Create the PR manually from branches I prepare
- Use a separate Claude Code session pointed at folio-assistant

---

## File-Level Migration Map

| Source (qou) | Destination (folio-assistant) | Changes needed |
|-------------|------------------------------|----------------|
| `scripts/mcp-server/server.ts` | `src/server.ts` | Extract generic HTTP/MCP skeleton; paper-specific logic → adapter |
| `scripts/mcp-server/git.ts` | `src/git.ts` | Reusable as-is (branch ops are generic) |
| `scripts/mcp-server/paths.ts` | `src/paths.ts` | Parameterize REPO_ROOT |
| `scripts/mcp-server/tools/render.ts` | `src/adapters/paper/tools/render.ts` | Paper-specific |
| `scripts/mcp-server/tools/validate.ts` | `src/adapters/paper/tools/validate.ts` | Paper-specific |
| `scripts/mcp-server/tools/preview.ts` | `src/tools/preview.ts` | Mostly generic (LaTeX preview) |
| `scripts/mcp-server/tools/preferences.ts` | `src/tools/preferences.ts` | Generic |
| `scripts/mcp-server/tools/lean.ts` | `src/adapters/paper/tools/lean.ts` | Paper/Lean-specific |
| `scripts/mcp-server/tools/check-deps.ts` | `src/tools/check-deps.ts` | Generic |
| `deploy/auth-gateway/server.ts` | `src/auth/server.ts` | Replace whitelists with GitHub API permission checks |
| `assistant/app.js` | `src/ui/app.js` | Generalize paper → document |
| `assistant/index.html` | `src/ui/index.html` | Add repo selector |
| `assistant/styles.css` | `src/ui/styles.css` | Minimal changes |
| `deploy/docker-compose.folio.yml` | `deploy/docker-compose.yml` | Generalize service names |
| `deploy/Caddyfile.folio.template` | `deploy/Caddyfile.template` | Minimal changes |
| `deploy/provision-hetzner.sh` | `deploy/provision-hetzner.sh` | Update image refs |
| `deploy/self-update-folio.sh` | `deploy/self-update.sh` | Update repo refs |
| `lean-mcp.config.json` | `folio.config.json` | New schema with subscriptions |
| `content/schema/types.ts` | `src/adapters/paper/schema/types.ts` | Paper-specific types |
| `content/schema/constraints.ts` | `src/adapters/paper/schema/constraints.ts` | Paper-specific validation |

---

## Content Type Extension Points

To add a new content type (e.g. WHO SMART guidelines):

1. Create `src/adapters/smart-guideline/index.ts` implementing `ContentAdapter`
2. Add a `package-manifest.json` to `skills/authoring-who-smart-guidelines/`
3. Register the adapter in the adapter registry
4. Content repo adds `folio.config.json` with `"contentType": "smart-guideline"`
5. Subscribe the repo in folio-assistant's deployment config

The adapter handles:
- How to discover/list content items
- How to parse the content structure (FHIR IG vs paper manifests)
- How to render output (IG Publisher vs LaTeX)
- How to validate (FHIR validation vs Zod schema)

The folio server handles generically:
- Authentication + authorization (GitHub OAuth)
- Feedback collection + triage
- Branch management
- UI navigation + rendering

---

## Immediate Next Steps

1. **Add folio-assistant to my MCP scope** so I can create PRs there
2. **Start Phase 1a-1b**: Define adapter interface + refactor auth gateway
3. **Create tracking issue** in folio-assistant referencing this plan
4. **Parallel**: Add `folio.config.json` to qou (non-breaking, additive)
