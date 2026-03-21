/**
 * QOU Paper Writing Assistant — MCP Server
 *
 * A unified MCP server providing:
 *   - PDF/HTML rendering (full paper, chapter, section, or single theorem)
 *   - Content-object validation and build pipeline
 *   - Formula/diagram quick preview (LaTeX → PNG)
 *   - User preference storage (render format, scope)
 *   - Lean LSP proxy (delegates to lean-lsp-mcp subprocess)
 *   - Content viewer (serves /api/paper from .ts manifests + SPA on /viewer/)
 *
 * Transports:
 *   --stdio   Stdio transport (default, for Claude Code .mcp.json)
 *   --http    Streamable HTTP transport (for remote/Docker deployment)
 *
 * Both modes start an HTTP server for the content viewer on VIEWER_PORT
 * (default 3200 for stdio, shared with MCP port for http).
 *
 * @module scripts/mcp-server/server
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { registerRenderTools } from "./tools/render.js";
import { registerValidateTools } from "./tools/validate.js";
import { registerPreviewTools } from "./tools/preview.js";
import { registerPreferenceTools } from "./tools/preferences.js";
import { registerLeanTools } from "./tools/lean.js";
import { registerDepsTools } from "./tools/check-deps.js";
import { REPO_ROOT, BUILD_DIR, FEEDBACK_DIR } from "./paths.js";
import { existsSync, readFileSync, writeFileSync, mkdirSync } from "fs";
import { join, resolve, extname } from "path";

// ── Feedback storage (gitignored, survives branch switches) ─────

function feedbackPath(paperId: string, rootName: string): string {
  return join(FEEDBACK_DIR, paperId, `${rootName}.json`);
}

function readFeedback(paperId: string, rootName: string): unknown[] {
  const p = feedbackPath(paperId, rootName);
  if (!existsSync(p)) return [];
  try { return JSON.parse(readFileSync(p, "utf-8")); } catch { return []; }
}

function writeFeedback(paperId: string, rootName: string, todos: unknown[]): void {
  const dir = join(FEEDBACK_DIR, paperId);
  mkdirSync(dir, { recursive: true });
  writeFileSync(feedbackPath(paperId, rootName), JSON.stringify(todos, null, 2), "utf-8");
}

/** List all feedback items across all papers, optionally filtered by status. */
function listAllFeedback(status?: string): { paperId: string; rootName: string; todo: any }[] {
  const results: { paperId: string; rootName: string; todo: any }[] = [];
  if (!existsSync(FEEDBACK_DIR)) return results;
  const { readdirSync } = require("fs") as typeof import("fs");
  for (const paperId of readdirSync(FEEDBACK_DIR)) {
    const paperFbDir = join(FEEDBACK_DIR, paperId);
    try {
      for (const file of readdirSync(paperFbDir)) {
        if (!file.endsWith(".json")) continue;
        const rootName = file.replace(/\.json$/, "");
        const todos = readFeedback(paperId, rootName);
        for (const t of todos as any[]) {
          if (!status || t.status === status) {
            results.push({ paperId, rootName, todo: t });
          }
        }
      }
    } catch {}
  }
  return results;
}

// ── Content resolution (dynamic, no static JSON) ────────────────

const CONTENT_DIR = resolve(REPO_ROOT, "content");
const LEAN_DIR = resolve(REPO_ROOT, "lean");

interface ResolvedRenderedAsset {
  mime: string;
  url: string;
  blockIndex: number;
  hash?: string;
}

interface ResolvedBlock {
  rootName: string;
  kind: string;
  label?: string;
  title?: string;
  uses?: string[];
  examples?: string[];
  lean?: { decl: string; file?: string; validation?: string; source?: string };
  status?: string;
  hasProof?: boolean;
  tex?: string;
  caption?: string;
  tags?: string[];
  rendered?: ResolvedRenderedAsset[];
  md: string;
  todos?: unknown[];
}

interface ResolvedSection {
  title: string;
  label?: string;
  blocks: ResolvedBlock[];
}

interface ResolvedChapter {
  number: number;
  title: string;
  label?: string;
  sections: ResolvedSection[];
  todos?: unknown[];
}

interface ResolvedPaper {
  id: string;
  title: string;
  authors: string[];
  affiliations?: string[];
  date?: string;
  chapters: ResolvedChapter[];
  todos?: unknown[];
}

interface FolioEntry {
  id: string;
  title: string;
  description?: string;
  tags?: string[];
  authors: string[];
  date?: string;
  stats: { chapters: number; blocks: number; proved: number; todos: number };
}

async function resolveFolio(): Promise<{ title: string; papers: FolioEntry[] }> {
  const folioPath = join(CONTENT_DIR, "folio.ts");
  let folioData: { title: string; papers: Array<{ dir: string; title?: string; description?: string; tags?: string[] }> };

  if (existsSync(folioPath)) {
    // Clear module cache for hot-reload during development
    delete require.cache?.[folioPath];
    folioData = (await import(folioPath)).default;
  } else {
    // Auto-discover: scan content/ for directories with matching .ts manifests
    const { readdirSync, statSync } = await import("fs");
    const dirs = readdirSync(CONTENT_DIR).filter(d => {
      if (d === "schema" || d === "pipeline" || d === "node_modules") return false;
      const full = join(CONTENT_DIR, d);
      return statSync(full).isDirectory() && existsSync(join(full, `${d}.ts`));
    });
    folioData = { title: "Papers", papers: dirs.map(d => ({ dir: d })) };
  }

  const papers: FolioEntry[] = [];
  for (const ref of folioData.papers) {
    try {
      const paperPath = join(CONTENT_DIR, ref.dir, `${ref.dir}.ts`);
      const paperMod = (await import(paperPath)).default;
      let blockCount = 0, provedCount = 0, todoCount = 0, chapCount = 0;

      for (const chRef of paperMod.chapters || []) {
        const chDir = join(CONTENT_DIR, ref.dir, chRef.dir);
        const chPath = join(chDir, `${chRef.dir}.ts`);
        if (!existsSync(chPath)) continue;
        chapCount++;
        const ch = (await import(chPath)).default;
        for (const sec of ch.sections || []) {
          if (!("blocks" in sec)) continue;
          for (const rootName of sec.blocks) {
            const tsPath = join(chDir, `${rootName}.ts`);
            if (!existsSync(tsPath)) continue;
            blockCount++;
            try {
              const blk = (await import(tsPath)).default;
              if (blk.status === "proved" || blk.status === "mathlib_ok") provedCount++;
              if (blk.todos?.length) todoCount += blk.todos.filter((t: any) => t.status !== "resolved" && t.status !== "wontfix").length;
            } catch {}
          }
        }
      }

      papers.push({
        id: ref.dir,
        title: ref.title || paperMod.title,
        description: ref.description,
        tags: ref.tags,
        authors: paperMod.authors,
        date: paperMod.date,
        stats: { chapters: chapCount, blocks: blockCount, proved: provedCount, todos: todoCount },
      });
    } catch (e) {
      papers.push({
        id: ref.dir,
        title: ref.title || ref.dir,
        description: ref.description,
        tags: ref.tags,
        authors: [],
        stats: { chapters: 0, blocks: 0, proved: 0, todos: 0 },
      });
    }
  }

  return { title: folioData.title, papers };
}

async function resolvePaper(id: string): Promise<ResolvedPaper | null> {
  const paperDir = join(CONTENT_DIR, id);
  const paperPath = join(paperDir, `${id}.ts`);
  if (!existsSync(paperPath)) return null;

  const paperMod = (await import(paperPath)).default;
  const chapters: ResolvedChapter[] = [];

  for (const chRef of paperMod.chapters || []) {
    const chDir = join(paperDir, chRef.dir);
    const chPath = join(chDir, `${chRef.dir}.ts`);
    if (!existsSync(chPath)) continue;
    const ch = (await import(chPath)).default;

    const sections: ResolvedSection[] = [];
    for (const sec of ch.sections || []) {
      if ("name" in sec && !("blocks" in sec)) continue;
      const section = sec as { title: string; label?: string; blocks: string[] };
      const blocks: ResolvedBlock[] = [];

      for (const rootName of section.blocks) {
        const tsPath = join(chDir, `${rootName}.ts`);
        const mdPath = join(chDir, `${rootName}.md`);
        try {
          const blk = (await import(tsPath)).default;
          const md = existsSync(mdPath) ? readFileSync(mdPath, "utf-8") : "";

          // Merge feedback todos from gitignored .qou-feedback/
          const feedback = readFeedback(id, rootName);
          if (feedback.length) {
            blk.todos = [...(blk.todos || []), ...feedback];
          }

          // Read Lean source if available
          let leanSource: string | undefined;
          if (blk.lean?.file) {
            const leanPath = join(LEAN_DIR, blk.lean.file);
            if (existsSync(leanPath)) leanSource = readFileSync(leanPath, "utf-8");
          }

          // Rewrite rendered asset URLs to serve from content source
          const rendered: ResolvedRenderedAsset[] | undefined = blk.rendered?.map(
            (r: { mime: string; url: string; blockIndex: number; hash?: string }) => ({
              ...r,
              url: `/api/content-asset/${id}/${chRef.dir}/${r.url}`,
            })
          );

          blocks.push({
            rootName,
            kind: blk.kind,
            label: blk.label,
            title: blk.title,
            uses: blk.uses,
            examples: blk.examples,
            lean: blk.lean ? { ...blk.lean, source: leanSource } : undefined,
            status: blk.status,
            hasProof: blk.hasProof,
            tex: blk.tex,
            caption: blk.caption,
            tags: blk.tags,
            rendered,
            md,
            todos: blk.todos,
          });
        } catch (e) {
          blocks.push({ rootName, kind: "error", md: `Failed to load ${rootName}: ${e}` });
        }
      }

      sections.push({ title: section.title, label: section.label, blocks });
    }

    chapters.push({
      number: ch.number, title: ch.title, label: ch.label, sections,
      todos: ch.todos,
    });
  }

  return {
    id,
    title: paperMod.title,
    authors: paperMod.authors,
    affiliations: paperMod.affiliations,
    date: paperMod.date,
    macros: paperMod.macros,
    chapters,
    todos: paperMod.todos,
  };
}

// ── Viewer content serving ───────────────────────────────────────

const VIEWER_DIR = resolve(REPO_ROOT, "viewer");
const ASSISTANT_DIR = resolve(REPO_ROOT, "assistant");
const VIEWER_BUILD_DIR = resolve(BUILD_DIR, "viewer");

const MIME: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".woff2": "font/woff2",
};

function serveFile(path: string): Response | null {
  if (!existsSync(path)) return null;
  return new Response(readFileSync(path), {
    headers: {
      "Content-Type": MIME[extname(path)] || "application/octet-stream",
      "Cache-Control": "no-cache",
      "Access-Control-Allow-Origin": "*",
    },
  });
}

/**
 * Handle HTTP requests for viewer, assistant, and API routes.
 * Returns Response if handled, null if not matched.
 */
async function handleViewerRequest(url: URL): Promise<Response | null> {
  const path = url.pathname;

  // ── Assistant SPA ──────────────────────────────────────────
  // /assistant/ serves the new assistant app (landing page → paper viewer/editor)
  if (path === "/assistant" || path === "/assistant/" || path === "/assistant/index.html") {
    return serveFile(join(ASSISTANT_DIR, "index.html"));
  }
  if (path.startsWith("/assistant/")) {
    return serveFile(join(ASSISTANT_DIR, path.slice("/assistant/".length)));
  }

  // ── API: Folio (paper listing) ─────────────────────────────
  if (path === "/api/folio") {
    try {
      const data = await resolveFolio();
      return Response.json(data, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // ── API: Paper (full resolved tree) ────────────────────────
  // /api/paper?id=quantum-observable-universe
  if (path === "/api/paper") {
    const id = url.searchParams.get("id");
    if (!id) return Response.json({ error: "Missing ?id= parameter" }, { status: 400 });
    try {
      const data = await resolvePaper(id);
      if (!data) return Response.json({ error: `Paper not found: ${id}` }, { status: 404 });
      return Response.json(data, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // ── API: Save block markdown ───────────────────────────────
  // POST /api/block/save { paperId, chapterDir, rootName, md }
  if (path === "/api/block/save" && url.searchParams.has("_method") !== true) {
    // Handled in fetch() for POST requests — see below
    return null;
  }

  // ── API: Feedback ─────────────────────────────────────────
  // GET  /api/feedback?paperId=X&rootName=Y → todos for one block
  // GET  /api/feedback/all?status=open      → all todos (optional status filter)
  // POST /api/feedback                      → create todo (handled below)
  if (path === "/api/feedback/all") {
    const status = url.searchParams.get("status") || undefined;
    return Response.json(listAllFeedback(status));
  }
  if (path === "/api/feedback") {
    const paperId = url.searchParams.get("paperId");
    const rootName = url.searchParams.get("rootName");
    if (paperId && rootName) {
      return Response.json(readFeedback(paperId, rootName));
    }
    return null; // POST handled in handlePostRequest
  }

  // ── Legacy viewer SPA ─────────────────────────────────────
  if (path === "/viewer" || path === "/viewer/" || path === "/viewer/index.html") {
    return serveFile(join(VIEWER_DIR, "index.html"));
  }

  // Legacy paper.json — viewer now uses /api/paper directly
  if (path === "/viewer/paper.json") {
    return serveFile(join(VIEWER_BUILD_DIR, "paper.json"))
      || serveFile(join(VIEWER_DIR, "paper.json"))
      || new Response("paper.json is deprecated. The viewer uses /api/paper which reads .ts manifests directly.", {
        status: 404,
        headers: { "Content-Type": "text/plain" },
      });
  }

  // Content assets — serve SVG/PNG directly from content source directories
  // URL pattern: /api/content-asset/<paper>/<chapter>/rendered/<file>
  if (path.startsWith("/api/content-asset/")) {
    const rel = path.slice("/api/content-asset/".length);
    const assetPath = join(CONTENT_DIR, rel);
    return serveFile(assetPath)
      || new Response("Asset not found", { status: 404 });
  }

  // Legacy rendered assets (from build output)
  if (path.startsWith("/viewer/assets/") || path.startsWith("/api/rendered/")) {
    const assetRel = path.startsWith("/viewer/assets/")
      ? path.slice("/viewer/".length)
      : path.slice("/api/".length);
    return serveFile(join(VIEWER_BUILD_DIR, assetRel))
      || new Response("Not found", { status: 404 });
  }

  // Static viewer files
  if (path.startsWith("/viewer/")) {
    return serveFile(join(VIEWER_DIR, path.slice("/viewer/".length)));
  }

  return null;
}

/**
 * Handle POST requests (block save, feedback submission).
 */
async function handlePostRequest(url: URL, req: Request): Promise<Response | null> {
  const path = url.pathname;

  // ── Save block markdown ────────────────────────────────────
  if (path === "/api/block/save") {
    try {
      const body = await req.json() as { paperId: string; rootName: string; md: string };
      const { writeFileSync, readdirSync } = await import("fs");

      // Find the block's chapter directory
      const paperDir = join(CONTENT_DIR, body.paperId);
      if (!existsSync(paperDir)) {
        return Response.json({ error: "Paper not found" }, { status: 404 });
      }
      let mdPath: string | null = null;
      for (const d of readdirSync(paperDir)) {
        const candidate = join(paperDir, d, `${body.rootName}.ts`);
        if (existsSync(candidate)) { mdPath = join(paperDir, d, `${body.rootName}.md`); break; }
      }
      if (!mdPath) {
        return Response.json({ error: `Block "${body.rootName}" not found` }, { status: 404 });
      }
      writeFileSync(mdPath, body.md, "utf-8");
      return Response.json({ ok: true, path: mdPath });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // ── Submit feedback as todo ────────────────────────────────
  // Stored in .qou-feedback/ (gitignored), not in the content tree.
  // Survives branch switches and won't be accidentally committed.
  if (path === "/api/feedback") {
    try {
      const body = await req.json() as {
        paperId: string; rootName: string;
        summary: string; comment: string; priority: string; assignee: string;
      };

      const todoId = `todo-${Date.now().toString(36)}`;
      const todo = {
        id: todoId,
        summary: body.summary,
        comment: body.comment,
        status: "open",
        priority: body.priority || "medium",
        origin: "human",
        assignee: body.assignee || "editor-agent",
        createdAt: new Date().toISOString(),
      };

      const todos = readFeedback(body.paperId, body.rootName);
      todos.push(todo);
      writeFeedback(body.paperId, body.rootName, todos);

      return Response.json({ ok: true, todo });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  return null;
}

// ── Server setup ─────────────────────────────────────────────────

const server = new McpServer({
  name: "qou-paper-assistant",
  version: "0.1.0",
}, {
  capabilities: {
    tools: {},
  },
});

// ── Logging ──────────────────────────────────────────────────────

function log(category: string, message: string, detail?: string) {
  const ts = new Date().toISOString().slice(11, 23);
  const d = detail ? ` ${detail}` : '';
  console.error(`[${ts}] [${category}]  ${message}${d}`);
}

// ── Wrap server.tool with logging ─────────────────────────────────

const origTool = server.tool.bind(server);
server.tool = function (...args: Parameters<typeof origTool>) {
  const toolName = args[0] as string;
  // The handler is the last argument
  const handler = args[args.length - 1] as (...a: unknown[]) => Promise<unknown>;
  args[args.length - 1] = async (...handlerArgs: unknown[]) => {
    const start = Date.now();
    log('mcp', `→ ${toolName}`, JSON.stringify(handlerArgs[0] || {}).slice(0, 120));
    try {
      const result = await (handler as Function)(...handlerArgs);
      log('mcp', `← ${toolName}`, `ok (${Date.now()-start}ms)`);
      return result;
    } catch (e) {
      log('mcp', `✗ ${toolName}`, `error: ${e instanceof Error ? e.message : String(e)} (${Date.now()-start}ms)`);
      throw e;
    }
  };
  return origTool(...args);
} as typeof origTool;

// ── Register all tool groups ─────────────────────────────────────

registerRenderTools(server);
registerValidateTools(server);
registerPreviewTools(server);
registerPreferenceTools(server);
registerLeanTools(server);
registerDepsTools(server);

// ── Transport selection ──────────────────────────────────────────

const args = process.argv.slice(2);
const mode = args.includes("--http") ? "http" : "stdio";

if (args.includes("--check-deps")) {
  // Just check deps and exit — used by start-assistant.sh --check
  console.log("Checking dependencies...");
  process.exit(0);
}

if (mode === "stdio") {
  const transport = new StdioServerTransport();
  await server.connect(transport);

  // Start viewer HTTP server on a separate port
  const viewerPort = parseInt(process.env.VIEWER_PORT || "3200", 10);

  Bun.serve({
    port: viewerPort,
    async fetch(req) {
      const url = new URL(req.url);
      const start = Date.now();
      log('http', `${req.method} ${url.pathname}`);

      // Root → redirect to assistant
      if (url.pathname === "/" || url.pathname === "") {
        return Response.redirect(`http://localhost:${viewerPort}/assistant/`, 302);
      }

      // Health check
      if (url.pathname === "/health") {
        return Response.json({ status: "ok", mode: "stdio", version: "0.1.0" });
      }

      // POST requests (save, feedback)
      if (req.method === "POST") {
        const postRes = await handlePostRequest(url, req);
        if (postRes) { log('http', `${req.method} ${url.pathname}`, `→ ${postRes.status} (${Date.now()-start}ms)`); return postRes; }
      }

      const viewerRes = await handleViewerRequest(url);
      if (viewerRes) { log('http', `${req.method} ${url.pathname}`, `→ ${viewerRes.status} (${Date.now()-start}ms)`); return viewerRes; }

      log('http', `${req.method} ${url.pathname}`, `→ 404 (${Date.now()-start}ms)`);
      return new Response("Not found", { status: 404 });
    },
  });

  log('init', `MCP server started (stdio, repo: ${REPO_ROOT})`);
  log('init', `Viewer: http://localhost:${viewerPort}/viewer/`);
} else {
  // HTTP mode — MCP + viewer on same port
  const port = parseInt(process.env.MCP_PORT || "8080", 10);
  const { StreamableHTTPServerTransport } = await import(
    "@modelcontextprotocol/sdk/server/streamableHttp.js"
  );

  const httpTransport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
  await server.connect(httpTransport);

  Bun.serve({
    port,
    async fetch(req) {
      const url = new URL(req.url);

      // MCP endpoint
      if (url.pathname === "/mcp") {
        return httpTransport.handleRequest(req);
      }

      // Health check
      if (url.pathname === "/health") {
        return Response.json({ status: "ok", mode: "http", version: "0.1.0" });
      }

      // Root → redirect to assistant
      if (url.pathname === "/" || url.pathname === "") {
        return Response.redirect(`/assistant/`, 302);
      }

      // POST requests
      if (req.method === "POST") {
        const postRes = await handlePostRequest(url, req);
        if (postRes) return postRes;
      }

      // Viewer/Assistant routes
      const viewerRes = await handleViewerRequest(url);
      if (viewerRes) return viewerRes;

      return new Response("Not found", { status: 404 });
    },
  });

  console.error(`[qou-mcp] Assistant started (HTTP :${port}, repo: ${REPO_ROOT})`);
  console.error(`[qou-mcp] MCP: http://localhost:${port}/mcp`);
  console.error(`[qou-mcp] Viewer: http://localhost:${port}/viewer/`);
}
