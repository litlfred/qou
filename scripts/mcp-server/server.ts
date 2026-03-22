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
import { REPO_ROOT, BUILD_DIR, FEEDBACK_DIR, MAIN_TEX } from "./paths.js";
import {
  currentBranch, listBranches, isCurrentBranch,
  readFileBranch, fileExistsBranch, importTsBranch, listDirBranch,
} from "./git.js";
import { existsSync, readFileSync, writeFileSync, mkdirSync } from "fs";
import { join, resolve, extname } from "path";

// ── Feedback storage (gitignored, branch-scoped) ─────────────────

/** Sanitize branch name for use as directory name. */
function safeBranch(branch?: string): string {
  const b = branch || currentBranch();
  return b.replace(/[^a-zA-Z0-9._-]/g, "_");
}

function feedbackPath(paperId: string, rootName: string, branch?: string): string {
  return join(FEEDBACK_DIR, safeBranch(branch), paperId, `${rootName}.json`);
}

function readFeedback(paperId: string, rootName: string, branch?: string): unknown[] {
  const p = feedbackPath(paperId, rootName, branch);
  if (!existsSync(p)) {
    // Migration: check legacy (non-branch-scoped) path
    const legacy = join(FEEDBACK_DIR, paperId, `${rootName}.json`);
    if (existsSync(legacy)) {
      try { return JSON.parse(readFileSync(legacy, "utf-8")); } catch { return []; }
    }
    return [];
  }
  try { return JSON.parse(readFileSync(p, "utf-8")); } catch { return []; }
}

function writeFeedback(paperId: string, rootName: string, todos: unknown[], branch?: string): void {
  const p = feedbackPath(paperId, rootName, branch);
  const dir = join(FEEDBACK_DIR, safeBranch(branch), paperId);
  mkdirSync(dir, { recursive: true });
  writeFileSync(p, JSON.stringify(todos, null, 2), "utf-8");
}

/** List all feedback items across all papers, optionally filtered by status and branch. */
function listAllFeedback(status?: string, branch?: string): { paperId: string; rootName: string; todo: any }[] {
  const results: { paperId: string; rootName: string; todo: any }[] = [];
  const branchDir = join(FEEDBACK_DIR, safeBranch(branch));
  if (!existsSync(branchDir)) return results;
  const { readdirSync } = require("fs") as typeof import("fs");
  for (const paperId of readdirSync(branchDir)) {
    const paperFbDir = join(branchDir, paperId);
    try {
      for (const file of readdirSync(paperFbDir)) {
        if (!file.endsWith(".json")) continue;
        const rootName = file.replace(/\.json$/, "");
        const todos = readFeedback(paperId, rootName, branch);
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
  proofs?: string[];
  lean?: { decl: string; file?: string; validation?: string; source?: string };
  status?: string;
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

async function resolveFolio(branch?: string): Promise<{ title: string; papers: FolioEntry[]; branch: string }> {
  const br = branch;
  const folioRel = "content/folio.ts";
  let folioData: { title: string; papers: Array<{ dir: string; title?: string; description?: string; tags?: string[] }> };

  if (fileExistsBranch(br, folioRel)) {
    folioData = (await importTsBranch(br, folioRel)) as any;
  } else {
    // Auto-discover: scan content/ for directories with matching .ts manifests
    const dirs = listDirBranch(br, "content").filter(d => {
      if (d === "schema" || d === "pipeline" || d === "node_modules") return false;
      return fileExistsBranch(br, `content/${d}/${d}.ts`);
    });
    folioData = { title: "Papers", papers: dirs.map(d => ({ dir: d })) };
  }

  const papers: FolioEntry[] = [];
  for (const ref of folioData.papers) {
    try {
      const paperMod = (await importTsBranch(br, `content/${ref.dir}/${ref.dir}.ts`)) as any;
      let blockCount = 0, provedCount = 0, todoCount = 0, chapCount = 0;

      for (const chRef of paperMod.chapters || []) {
        const chRel = `content/${ref.dir}/${chRef.dir}/${chRef.dir}.ts`;
        if (!fileExistsBranch(br, chRel)) continue;
        chapCount++;
        const ch = (await importTsBranch(br, chRel)) as any;
        for (const sec of ch.sections || []) {
          if (!("blocks" in sec)) continue;
          for (const rootName of sec.blocks) {
            const blkRel = `content/${ref.dir}/${chRef.dir}/${rootName}.ts`;
            if (!fileExistsBranch(br, blkRel)) continue;
            blockCount++;
            try {
              const blk = (await importTsBranch(br, blkRel)) as any;
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

  return { title: folioData.title, papers, branch: currentBranch() };
}

async function resolvePaper(id: string, branch?: string): Promise<(ResolvedPaper & { branch: string }) | null> {
  const br = branch;
  const paperRel = `content/${id}/${id}.ts`;
  if (!fileExistsBranch(br, paperRel)) return null;

  const paperMod = (await importTsBranch(br, paperRel)) as any;
  const chapters: ResolvedChapter[] = [];

  for (const chRef of paperMod.chapters || []) {
    const chRel = `content/${id}/${chRef.dir}`;
    const chTsRel = `${chRel}/${chRef.dir}.ts`;
    if (!fileExistsBranch(br, chTsRel)) continue;
    const ch = (await importTsBranch(br, chTsRel)) as any;

    const sections: ResolvedSection[] = [];
    for (const sec of ch.sections || []) {
      if ("name" in sec && !("blocks" in sec)) continue;
      const section = sec as { title: string; label?: string; blocks: string[] };
      const blocks: ResolvedBlock[] = [];

      for (const rootName of section.blocks) {
        const blkTsRel = `${chRel}/${rootName}.ts`;
        const blkMdRel = `${chRel}/${rootName}.md`;
        try {
          const blk = (await importTsBranch(br, blkTsRel)) as any;
          const md = readFileBranch(br, blkMdRel) || "";

          // Merge feedback todos (branch-scoped)
          const feedback = readFeedback(id, rootName, br);
          if (feedback.length) {
            blk.todos = [...(blk.todos || []), ...feedback];
          }

          // Read Lean source if available
          let leanSource: string | undefined;
          if (blk.lean) {
            if (blk.lean.file) {
              leanSource = readFileBranch(br, `lean/${blk.lean.file}`) ?? undefined;
            }
            if (!leanSource) {
              leanSource = readFileBranch(br, `${chRel}/${rootName}.lean`) ?? undefined;
            }
            if (!leanSource && blk.lean.decl) {
              const parts = blk.lean.decl.split(".");
              for (let i = parts.length; i >= 2; i--) {
                const candidate = `lean/${parts.slice(0, i).join("/")}.lean`;
                leanSource = readFileBranch(br, candidate) ?? undefined;
                if (leanSource) break;
              }
            }
            // Grep fallback only works for current branch (needs disk access)
            if (!leanSource && blk.lean.decl && isCurrentBranch(br)) {
              const declName = blk.lean.decl.split(".").pop() || "";
              try {
                const result = Bun.spawnSync(["grep", "-rl", declName, join(LEAN_DIR, "QOU")]);
                const files = result.stdout.toString().trim().split("\n").filter(Boolean);
                if (files.length > 0 && existsSync(files[0])) {
                  leanSource = readFileSync(files[0], "utf-8");
                }
              } catch {}
            }
          }

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
            proofs: blk.proofs,
            lean: blk.lean ? { ...blk.lean, source: leanSource } : undefined,
            status: blk.status,
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
    branch: currentBranch(),
  };
}

// ── Diff computation ─────────────────────────────────────────────

interface BlockDiff {
  rootName: string;
  kind: string;
  label?: string;
  title?: string;
  status: "added" | "removed" | "changed" | "unchanged";
  mdDiff?: { base: string; head: string };
  leanDiff?: { base: string; head: string };
  statusDiff?: { base: string; head: string };
}

interface PaperDiff {
  base: string;
  head: string;
  paperId: string;
  blocks: BlockDiff[];
  summary: { added: number; removed: number; changed: number; unchanged: number };
}

function computePaperDiff(
  basePaper: ResolvedPaper | null,
  headPaper: ResolvedPaper | null,
  base: string,
  head: string,
): PaperDiff {
  const paperId = headPaper?.id || basePaper?.id || "";

  // Flatten blocks from both papers
  function flattenBlocks(paper: ResolvedPaper | null): Map<string, ResolvedBlock & { chapterTitle?: string; sectionTitle?: string }> {
    const map = new Map();
    if (!paper) return map;
    for (const ch of paper.chapters || []) {
      for (const sec of ch.sections || []) {
        for (const blk of sec.blocks || []) {
          map.set(blk.rootName, { ...blk, chapterTitle: ch.title, sectionTitle: sec.title });
        }
      }
    }
    return map;
  }

  const baseBlocks = flattenBlocks(basePaper);
  const headBlocks = flattenBlocks(headPaper);
  const allNames = new Set([...baseBlocks.keys(), ...headBlocks.keys()]);

  const blocks: BlockDiff[] = [];
  const summary = { added: 0, removed: 0, changed: 0, unchanged: 0 };

  for (const name of allNames) {
    const baseBlk = baseBlocks.get(name);
    const headBlk = headBlocks.get(name);

    if (!baseBlk && headBlk) {
      blocks.push({ rootName: name, kind: headBlk.kind, label: headBlk.label, title: headBlk.title, status: "added" });
      summary.added++;
    } else if (baseBlk && !headBlk) {
      blocks.push({ rootName: name, kind: baseBlk.kind, label: baseBlk.label, title: baseBlk.title, status: "removed" });
      summary.removed++;
    } else if (baseBlk && headBlk) {
      const mdChanged = baseBlk.md !== headBlk.md;
      const leanChanged = (baseBlk.lean?.source || "") !== (headBlk.lean?.source || "");
      const statusChanged = baseBlk.status !== headBlk.status;

      if (mdChanged || leanChanged || statusChanged) {
        const diff: BlockDiff = {
          rootName: name, kind: headBlk.kind, label: headBlk.label, title: headBlk.title, status: "changed",
        };
        if (mdChanged) diff.mdDiff = { base: baseBlk.md, head: headBlk.md };
        if (leanChanged) diff.leanDiff = { base: baseBlk.lean?.source || "", head: headBlk.lean?.source || "" };
        if (statusChanged) diff.statusDiff = { base: baseBlk.status || "", head: headBlk.status || "" };
        blocks.push(diff);
        summary.changed++;
      } else {
        blocks.push({ rootName: name, kind: headBlk.kind, label: headBlk.label, title: headBlk.title, status: "unchanged" });
        summary.unchanged++;
      }
    }
  }

  return { base, head, paperId, blocks, summary };
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

  // ── API: Branch info ───────────────────────────────────────
  // GET /api/branches → { current, branches[] }
  if (path === "/api/branches") {
    return Response.json({
      current: currentBranch(),
      branches: listBranches(),
    }, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
  }
  // GET /api/branch → { branch } (lightweight, for polling)
  if (path === "/api/branch") {
    return Response.json({
      branch: currentBranch(),
    }, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
  }

  // ── API: Folio (paper listing) ─────────────────────────────
  // Supports ?branch=X to resolve from a different branch
  if (path === "/api/folio") {
    const branch = url.searchParams.get("branch") || undefined;
    try {
      const data = await resolveFolio(branch);
      return Response.json(data, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // ── API: Paper (full resolved tree) ────────────────────────
  // /api/paper?id=quantum-observable-universe&branch=feature-x
  if (path === "/api/paper") {
    const id = url.searchParams.get("id");
    const branch = url.searchParams.get("branch") || undefined;
    if (!id) return Response.json({ error: "Missing ?id= parameter" }, { status: 400 });
    try {
      const data = await resolvePaper(id, branch);
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
    const branch = url.searchParams.get("branch") || undefined;
    return Response.json(listAllFeedback(status, branch));
  }
  if (path === "/api/feedback") {
    const paperId = url.searchParams.get("paperId");
    const rootName = url.searchParams.get("rootName");
    const branch = url.searchParams.get("branch") || undefined;
    if (paperId && rootName) {
      return Response.json(readFeedback(paperId, rootName, branch));
    }
    return null; // POST handled in handlePostRequest
  }

  // ── API: Diff between branches ─────────────────────────────
  // GET /api/diff?id=<paper>&base=main&head=feature-x
  // Returns per-block diff info (added, removed, changed blocks)
  if (path === "/api/diff") {
    const id = url.searchParams.get("id");
    const base = url.searchParams.get("base") || "main";
    const head = url.searchParams.get("head") || currentBranch();
    if (!id) return Response.json({ error: "Missing ?id= parameter" }, { status: 400 });
    try {
      const [basePaper, headPaper] = await Promise.all([
        resolvePaper(id, base),
        resolvePaper(id, head),
      ]);
      const diff = computePaperDiff(basePaper, headPaper, base, head);
      return Response.json(diff, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // ── Legacy viewer SPA ─────────────────────────────────────
  if (path === "/viewer" || path === "/viewer/" || path === "/viewer/index.html") {
    return serveFile(join(VIEWER_DIR, "index.html"));
  }

  // ── API: Render PDF status (check if latexmk is available) ────
  if (path === "/api/render-pdf/status") {
    try {
      const { execSync: ex } = await import("child_process");
      ex("which latexmk", { stdio: "pipe" });
      return Response.json({ available: true }, { headers: { "Access-Control-Allow-Origin": "*" } });
    } catch {
      return Response.json({ available: false, reason: "latexmk not installed" }, { headers: { "Access-Control-Allow-Origin": "*" } });
    }
  }

  // ── API: Render PDF (triggers content_build → latexmk) ────────
  if (path === "/api/render-pdf") {
    try {
      const { spawnSync, execSync: ex } = await import("child_process");
      const { mkdirSync, readFileSync: rf } = await import("fs");

      // Pre-check: is latexmk installed?
      try { ex("which latexmk", { stdio: "pipe" }); } catch {
        return Response.json({
          error: "latexmk not installed. Install TeX Live: apt install texlive-full",
        }, { status: 503, headers: { "Access-Control-Allow-Origin": "*" } });
      }

      // Step 1: Build content objects → .tex chapters
      const buildResult = spawnSync("bun", ["run", join(REPO_ROOT, "content/pipeline/build.ts")], {
        cwd: REPO_ROOT,
        stdio: "pipe",
        timeout: 60_000,
      });

      // Step 2: Run latexmk to produce PDF
      if (!existsSync(BUILD_DIR)) mkdirSync(BUILD_DIR, { recursive: true });
      const latexResult = spawnSync("latexmk", [
        "-pdf",
        `-jobname=quantum-observable-universe`,
        `-output-directory=${BUILD_DIR}`,
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        MAIN_TEX,
      ], {
        cwd: REPO_ROOT,
        stdio: "pipe",
        timeout: 300_000,
      });

      const pdfPath = join(BUILD_DIR, "quantum-observable-universe.pdf");
      if (latexResult.status === 0 && existsSync(pdfPath)) {
        const pdfData = rf(pdfPath);
        return new Response(pdfData, {
          headers: {
            "Content-Type": "application/pdf",
            "Content-Disposition": 'inline; filename="quantum-observable-universe.pdf"',
            "Access-Control-Allow-Origin": "*",
          },
        });
      }

      // Failed — return error details
      const log = latexResult.stderr?.toString().slice(-3000) || "";
      const buildLog = buildResult.stderr?.toString().slice(-1000) || "";
      return Response.json({
        error: "LaTeX compilation failed",
        buildLog,
        latexLog: log,
      }, { status: 500, headers: { "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500, headers: { "Access-Control-Allow-Origin": "*" } });
    }
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

  // ── Submit feedback as todo (branch-scoped) ─────────────────
  if (path === "/api/feedback") {
    try {
      const body = await req.json() as {
        paperId: string; rootName: string;
        summary: string; comment: string; priority: string; assignee: string;
        branch?: string;
      };

      const branch = body.branch || undefined;
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
        branch: branch || currentBranch(),
      };

      const todos = readFeedback(body.paperId, body.rootName, branch);
      todos.push(todo);
      writeFeedback(body.paperId, body.rootName, todos, branch);

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
