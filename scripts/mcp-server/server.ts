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
import Anthropic from "@anthropic-ai/sdk";

// ── Feedback storage (gitignored, global with hash-based IDs) ────

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

/** Generate a unique todo ID: timestamp + 4-char hash to avoid collisions. */
function makeTodoId(): string {
  const ts = Date.now().toString(36);
  const hash = Math.random().toString(36).slice(2, 6);
  return `todo-${ts}-${hash}`;
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

          // Merge feedback todos (global)
          const feedback = readFeedback(id, rootName);
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

// ── Claude API: characterize branch changes ──────────────────────

let anthropic: Anthropic | null = null;

function getAnthropic(): Anthropic | null {
  if (anthropic) return anthropic;
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return null;
  anthropic = new Anthropic({ apiKey: key });
  return anthropic;
}

interface BranchCharacterization {
  title: string;
  summary: string;
  categories: string[];
  impact: "minor" | "moderate" | "major";
  suggestions?: string[];
  error?: string;
}

async function characterizeBranchChanges(diff: PaperDiff): Promise<BranchCharacterization> {
  const client = getAnthropic();
  if (!client) {
    // No API key — return a basic characterization from the diff summary
    return fallbackCharacterization(diff);
  }

  // Build a concise prompt from the diff
  const changedBlocks = diff.blocks.filter(b => b.status !== "unchanged");
  const blockDescriptions = changedBlocks.slice(0, 30).map(b => {
    let desc = `[${b.status}] ${b.kind}: ${b.title || b.rootName}`;
    if (b.label) desc += ` (${b.label})`;
    if (b.statusDiff) desc += ` | status: ${b.statusDiff.base} → ${b.statusDiff.head}`;
    if (b.mdDiff) {
      const added = b.mdDiff.head.split("\n").length;
      const removed = b.mdDiff.base.split("\n").length;
      desc += ` | md: ${removed} → ${added} lines`;
    }
    if (b.leanDiff) desc += ` | lean source changed`;
    return desc;
  }).join("\n");

  const prompt = `You are a mathematical paper assistant. Characterize the changes between branch "${diff.base}" and "${diff.head}" for paper "${diff.paperId}".

Summary: +${diff.summary.added} added, -${diff.summary.removed} removed, ~${diff.summary.changed} changed, ${diff.summary.unchanged} unchanged blocks.

Changed blocks:
${blockDescriptions}

Respond in JSON with exactly these fields:
- "title": Short title for these changes (under 60 chars)
- "summary": 2-3 sentence description of what changed and why it matters
- "categories": Array of category tags (e.g. "new-definitions", "proof-progress", "restructuring", "notation", "formalization")
- "impact": One of "minor", "moderate", "major"
- "suggestions": Optional array of 1-3 follow-up suggestions`;

  try {
    const response = await client.messages.create({
      model: "claude-haiku-4-5-20251001",
      max_tokens: 500,
      messages: [{ role: "user", content: prompt }],
    });

    const text = response.content[0]?.type === "text" ? response.content[0].text : "";
    // Extract JSON from response (may be wrapped in ```json ... ```)
    const jsonMatch = text.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      const parsed = JSON.parse(jsonMatch[0]);
      return {
        title: parsed.title || "Branch changes",
        summary: parsed.summary || "",
        categories: parsed.categories || [],
        impact: parsed.impact || "moderate",
        suggestions: parsed.suggestions,
      };
    }
    return fallbackCharacterization(diff);
  } catch (e) {
    return { ...fallbackCharacterization(diff), error: `Claude API error: ${e instanceof Error ? e.message : String(e)}` };
  }
}

function fallbackCharacterization(diff: PaperDiff): BranchCharacterization {
  const { added, removed, changed } = diff.summary;
  const total = added + removed + changed;
  const categories: string[] = [];
  const changedBlocks = diff.blocks.filter(b => b.status !== "unchanged");

  // Infer categories from block kinds
  const kinds = new Set(changedBlocks.map(b => b.kind));
  if (kinds.has("definition")) categories.push("definitions");
  if (kinds.has("theorem") || kinds.has("lemma") || kinds.has("proposition")) categories.push("proofs");
  if (kinds.has("remark") || kinds.has("example")) categories.push("exposition");
  if (changedBlocks.some(b => b.leanDiff)) categories.push("formalization");
  if (added > 0) categories.push("new-content");
  if (removed > 0) categories.push("removals");

  const impact = total > 10 ? "major" : total > 3 ? "moderate" : "minor";
  const title = `${total} block${total !== 1 ? "s" : ""} changed (${diff.base} → ${diff.head})`;
  const summary = `${added} blocks added, ${removed} removed, ${changed} modified. ${categories.length ? "Touches: " + categories.join(", ") + "." : ""}`;

  return { title, summary, categories, impact };
}

// ── AI triage: review feedback and propose actionable edits ──────

interface TriageResult {
  assessment: string;
  actionable: boolean;
  proposedEdit?: {
    description: string;
    newMd?: string;       // proposed replacement markdown
    targetBranch?: string; // suggested branch
  };
  error?: string;
}

async function triageFeedback(
  todo: any,
  blockContent: string,
  blockKind: string,
  paperId: string,
  rootName: string,
): Promise<TriageResult> {
  const client = getAnthropic();
  if (!client) {
    return {
      assessment: `Feedback: "${todo.summary}". Priority: ${todo.priority}. No AI available — set ANTHROPIC_API_KEY to enable triage.`,
      actionable: false,
    };
  }

  const prompt = `You are an editor triaging feedback on a mathematical research paper.

Block: "${rootName}" (kind: ${blockKind}, paper: ${paperId})

Block content (markdown):
\`\`\`
${blockContent.slice(0, 2000)}
\`\`\`

Feedback:
- Summary: ${todo.summary}
- Detail: ${todo.comment || "(none)"}
- Priority: ${todo.priority}
- Assignee: ${todo.assignee}

Respond in JSON with exactly these fields:
- "assessment": 1-2 sentence editorial assessment of the feedback
- "actionable": boolean — can this be addressed with a text edit right now?
- "proposedEdit": (only if actionable) object with:
  - "description": what the edit does
  - "newMd": the full revised markdown for this block (preserving math notation, cross-refs, etc.)`;

  try {
    const response = await client.messages.create({
      model: "claude-haiku-4-5-20251001",
      max_tokens: 1500,
      messages: [{ role: "user", content: prompt }],
    });

    const text = response.content[0]?.type === "text" ? response.content[0].text : "";
    const jsonMatch = text.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      const parsed = JSON.parse(jsonMatch[0]);
      return {
        assessment: parsed.assessment || "No assessment generated.",
        actionable: !!parsed.actionable,
        proposedEdit: parsed.proposedEdit ? {
          description: parsed.proposedEdit.description || "",
          newMd: parsed.proposedEdit.newMd,
        } : undefined,
      };
    }
    return { assessment: "Failed to parse AI response.", actionable: false };
  } catch (e) {
    return {
      assessment: `Feedback: "${todo.summary}". Priority: ${todo.priority}.`,
      actionable: false,
      error: `Claude API error: ${e instanceof Error ? e.message : String(e)}`,
    };
  }
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

  // ── API: Characterize branch changes via Claude ─────────────
  // GET /api/characterize?id=<paper>&base=main&head=feature-x
  if (path === "/api/characterize") {
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
      const summary = await characterizeBranchChanges(diff);
      return Response.json({ ...summary, diff: diff.summary }, {
        headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" },
      });
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

  // ── Submit feedback as todo (global, hash-based ID) ─────────
  if (path === "/api/feedback") {
    try {
      const body = await req.json() as {
        paperId: string; rootName: string;
        summary: string; comment: string; priority: string; assignee: string;
      };

      const todo = {
        id: makeTodoId(),
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

  // ── Claude chat: streaming conversational assistant ──────────
  // POST /api/chat { messages[], context?, mode? }
  // Returns SSE stream of assistant response chunks
  if (path === "/api/chat") {
    try {
      const body = await req.json() as {
        messages: Array<{ role: string; content: string }>;
        context?: { paperId?: string; blockLabel?: string; blockMd?: string; blockKind?: string; selectedText?: string };
        mode?: "read" | "edit" | "status";
      };

      const client = getAnthropic();
      if (!client) {
        return Response.json(
          { error: "ANTHROPIC_API_KEY not set. Claude chat requires an API key." },
          { status: 503, headers: { "Access-Control-Allow-Origin": "*" } }
        );
      }

      // Build system prompt based on mode
      const mode = body.mode || "read";
      let systemPrompt = `You are Folio, an editorial assistant for a formal mathematics research paper. You help readers understand, navigate, and improve the paper.

Your role is that of a knowledgeable editor who:
- Explains mathematical content clearly at the reader's level
- Helps navigate between related definitions, theorems, and proofs
- Identifies potential errors or improvements when asked
- Suggests connections between concepts
- Answers questions about the paper's content and structure

Keep responses concise and well-formatted. Use $...$ for inline math and $$...$$ for display math.`;

      if (mode === "status") {
        systemPrompt += `\n\nThe user is in EDITOR mode. They want to understand the paper's current status — what's complete, what needs work, what the priorities are. Focus on actionable summaries: proof status, open todos, missing Lean formalizations, and suggested next steps.`;
      } else if (mode === "edit") {
        systemPrompt += `\n\nThe user is in EDITOR mode. They may want to report errors, suggest improvements, or discuss editorial decisions. When they identify an issue, help them articulate it clearly so it can be tracked as a todo.`;
      } else {
        systemPrompt += `\n\nThe user is in READER mode. They're studying the paper and want to understand the content. Prioritize clear explanations, motivation, and intuition. When explaining, build from what the reader likely knows.`;
      }

      // Add context about the current block if available
      if (body.context) {
        const ctx = body.context;
        if (ctx.selectedText) {
          systemPrompt += `\n\nThe reader has selected this text:\n"""${ctx.selectedText.slice(0, 1000)}"""`;
        }
        if (ctx.blockLabel && ctx.blockMd) {
          systemPrompt += `\n\nThey are looking at block "${ctx.blockLabel}" (${ctx.blockKind || "unknown"}):\n"""${ctx.blockMd.slice(0, 3000)}"""`;
        }
        if (ctx.paperId) {
          systemPrompt += `\n\nPaper ID: ${ctx.paperId}`;
        }
      }

      // Stream the response
      const stream = await client.messages.stream({
        model: "claude-haiku-4-5-20251001",
        max_tokens: 1500,
        system: systemPrompt,
        messages: body.messages.map(m => ({
          role: m.role as "user" | "assistant",
          content: m.content,
        })),
      });

      // Return as SSE
      const encoder = new TextEncoder();
      const readable = new ReadableStream({
        async start(controller) {
          try {
            for await (const event of stream) {
              if (event.type === "content_block_delta" && event.delta.type === "text_delta") {
                controller.enqueue(encoder.encode(`data: ${JSON.stringify({ text: event.delta.text })}\n\n`));
              }
            }
            controller.enqueue(encoder.encode(`data: [DONE]\n\n`));
            controller.close();
          } catch (e) {
            controller.enqueue(encoder.encode(`data: ${JSON.stringify({ error: String(e) })}\n\n`));
            controller.close();
          }
        },
      });

      return new Response(readable, {
        headers: {
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          "Connection": "keep-alive",
          "Access-Control-Allow-Origin": "*",
        },
      });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500, headers: { "Access-Control-Allow-Origin": "*" } });
    }
  }

  // ── AI triage: review feedback and propose action ────────────
  // POST /api/feedback/triage { paperId, rootName, todoId }
  if (path === "/api/feedback/triage") {
    try {
      const body = await req.json() as { paperId: string; rootName: string; todoId: string };
      const todos = readFeedback(body.paperId, body.rootName);
      const todo = (todos as any[]).find(t => t.id === body.todoId);
      if (!todo) return Response.json({ error: "Todo not found" }, { status: 404 });

      // Read the block content for context
      const paper = await resolvePaper(body.paperId);
      let blockContent = "";
      let blockKind = "";
      if (paper) {
        for (const ch of paper.chapters) {
          for (const sec of ch.sections) {
            for (const blk of sec.blocks) {
              if (blk.rootName === body.rootName) {
                blockContent = blk.md;
                blockKind = blk.kind;
              }
            }
          }
        }
      }

      const triage = await triageFeedback(todo, blockContent, blockKind, body.paperId, body.rootName);
      return Response.json(triage, { headers: { "Access-Control-Allow-Origin": "*" } });
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
