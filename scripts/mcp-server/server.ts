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
  currentBranch, listBranches, fetchOrigin, isCurrentBranch,
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
  /** Flattened O(1) lookup: rootName → block. Not serialized to API responses. */
  blocksByName?: Map<string, ResolvedBlock>;
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
              const fb = readFeedback(ref.dir, rootName);
              if (fb.length) todoCount += fb.filter((t: any) => t.status !== "resolved" && t.status !== "wontfix").length;
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

          // Merge feedback todos from gitignored .qou-feedback/
          // Build a fresh array each time — never mutate the cached ESM module object
          const feedback = readFeedback(id, rootName);
          const blockTodos = feedback.length ? [...feedback] : undefined;

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
            todos: blockTodos,
          });
        } catch (e) {
          blocks.push({ rootName, kind: "error", md: `Failed to load ${rootName}: ${e}` });
        }
      }

      sections.push({ title: section.title, label: section.label, blocks });
    }

    const chTodos = readFeedback(id, `__chapter:${chRef.dir}`);
    chapters.push({
      number: ch.number, title: ch.title, label: ch.label, sections,
      todos: chTodos.length ? chTodos : undefined,
    });
  }

  // Build flattened block lookup map
  const blocksByName = new Map<string, ResolvedBlock>();
  for (const ch of chapters)
    for (const sec of ch.sections)
      for (const blk of sec.blocks)
        blocksByName.set(blk.rootName, blk);

  const paperTodos = readFeedback(id, "__paper");
  return {
    id,
    title: paperMod.title,
    authors: paperMod.authors,
    affiliations: paperMod.affiliations,
    date: paperMod.date,
    macros: paperMod.macros,
    chapters,
    todos: paperTodos.length ? paperTodos : undefined,
    branch: currentBranch(),
    blocksByName,
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
      blocks.push({ rootName: name, kind: headBlk.kind, label: headBlk.label, title: headBlk.title, status: "added",
        mdDiff: headBlk.md ? { base: "", head: headBlk.md } : undefined,
        leanDiff: headBlk.lean?.source ? { base: "", head: headBlk.lean.source } : undefined,
      });
      summary.added++;
    } else if (baseBlk && !headBlk) {
      blocks.push({ rootName: name, kind: baseBlk.kind, label: baseBlk.label, title: baseBlk.title, status: "removed",
        mdDiff: baseBlk.md ? { base: baseBlk.md, head: "" } : undefined,
        leanDiff: baseBlk.lean?.source ? { base: baseBlk.lean.source, head: "" } : undefined,
      });
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
    fetchOrigin(); // silently update remote refs
    const branches = listBranches();
    log('git', `branches: ${branches.length} total, HEAD=${currentBranch()}`);
    return Response.json({
      current: currentBranch(),
      branches,
    }, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
  }
  // GET /api/branch → { branch } (lightweight, for polling)
  if (path === "/api/branch") {
    return Response.json({
      branch: currentBranch(),
    }, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
  }

  // GET /api/git/status → { dirty, branch, changes[] }
  if (path === "/api/git/status") {
    try {
      const { spawnSync } = await import("child_process");
      const r = spawnSync("git", ["status", "--porcelain"], { cwd: REPO_ROOT, stdio: "pipe" });
      const output = r.stdout.toString().trim();
      const changes = output ? output.split("\n").map(l => l.trim()).filter(Boolean) : [];
      log('git', `status: branch=${currentBranch()} dirty=${changes.length > 0} changes=${changes.length}`);
      return Response.json({
        branch: currentBranch(),
        dirty: changes.length > 0,
        changes,
      }, { headers: { "Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      log('git', `status: error — ${e}`);
      return Response.json({ error: String(e) }, { status: 500, headers: { "Access-Control-Allow-Origin": "*" } });
    }
  }

  // POST /api/git/checkout { branch, action? } — switch branches
  // action: "switch" (default), "stash", "commit"
  if (path === "/api/git/checkout") {
    return null; // POST handled below
  }

  // ── API: Import list (available imports) ────────────────────
  if (path === "/api/import/list") {
    try {
      const uploadsDir = join(REPO_ROOT, "uploads");
      const imports: Array<Record<string, unknown>> = [];
      if (existsSync(uploadsDir)) {
        const { readdirSync } = await import("fs");
        for (const d of readdirSync(uploadsDir)) {
          const metaPath = join(uploadsDir, d, "import-meta.json");
          if (existsSync(metaPath)) {
            const meta = JSON.parse(readFileSync(metaPath, "utf-8"));
            // Check if extracted blocks exist
            const extractedPath = join(uploadsDir, d, "extracted-blocks.json");
            const hasExtracted = existsSync(extractedPath);
            let blockCount = 0;
            if (hasExtracted) {
              try { blockCount = JSON.parse(readFileSync(extractedPath, "utf-8")).length; } catch {}
            }
            // Check if content objects were generated
            const contentDir = join(REPO_ROOT, "content", d);
            const hasContent = existsSync(contentDir);
            imports.push({ ...meta, hasExtracted, blockCount, hasContent });
          }
        }
      }
      return Response.json(imports, { headers: { "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
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
      const msg = e instanceof Error ? e.stack || e.message : String(e);
      log('error', `GET /api/paper id=${id} branch=${branch}: ${msg}`);
      return Response.json({ error: msg }, { status: 500 });
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
      log('edit', `block saved: ${body.paperId}/${body.rootName}`, `${body.md.length} chars → ${mdPath}`);
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
      log('feedback', `created: ${body.paperId}/${body.rootName}`, `id=${todo.id} priority=${todo.priority} assignee=${todo.assignee}`);

      return Response.json({ ok: true, todo });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // ── Git checkout (branch switch with dirty-state handling) ───
  if (path === "/api/git/checkout") {
    try {
      const { spawnSync } = await import("child_process");
      const body = await req.json() as { branch: string; action?: "switch" | "stash" | "commit" | "discard" };
      const targetBranch = body.branch;
      const action = body.action || "switch";
      const fromBranch = currentBranch();
      log('git', `checkout: ${fromBranch} → ${targetBranch}`, `action=${action}`);

      // Check if dirty
      const st = spawnSync("git", ["status", "--porcelain"], { cwd: REPO_ROOT, stdio: "pipe" });
      const dirty = st.stdout.toString().trim().length > 0;

      if (dirty) {
        log('git', `checkout: working tree dirty (${st.stdout.toString().trim().split("\n").length} changes)`);
        if (action === "stash") {
          log('git', `stash: saving changes from ${fromBranch}`);
          const stash = spawnSync("git", ["stash", "push", "-m", `folio-auto-stash-${fromBranch}`], { cwd: REPO_ROOT, stdio: "pipe" });
          if (stash.status !== 0) {
            log('git', `stash: FAILED — ${stash.stderr.toString().trim()}`);
            return Response.json({ error: `Stash failed: ${stash.stderr.toString()}` }, { status: 500, headers: { "Access-Control-Allow-Origin": "*" } });
          }
          log('git', `stash: ok`);
        } else if (action === "commit") {
          log('git', `commit: auto-committing changes on ${fromBranch}`);
          spawnSync("git", ["add", "-A"], { cwd: REPO_ROOT, stdio: "pipe" });
          const commit = spawnSync("git", ["commit", "-m", "Folio: auto-save before branch switch"], { cwd: REPO_ROOT, stdio: "pipe" });
          if (commit.status !== 0) {
            log('git', `commit: FAILED — ${commit.stderr.toString().trim()}`);
            return Response.json({ error: `Commit failed: ${commit.stderr.toString()}` }, { status: 500, headers: { "Access-Control-Allow-Origin": "*" } });
          }
          log('git', `commit: ok`);
        } else if (action === "discard") {
          log('git', `discard: discarding all changes on ${fromBranch}`);
          spawnSync("git", ["checkout", "--", "."], { cwd: REPO_ROOT, stdio: "pipe" });
          spawnSync("git", ["clean", "-fd"], { cwd: REPO_ROOT, stdio: "pipe" });
          log('git', `discard: ok`);
        } else {
          log('git', `checkout: blocked — dirty state, no action specified`);
          return Response.json({
            error: "dirty",
            message: "Working tree has uncommitted changes",
            branch: fromBranch,
            changes: st.stdout.toString().trim().split("\n").filter(Boolean),
          }, { status: 409, headers: { "Access-Control-Allow-Origin": "*" } });
        }
      }

      // Do the checkout
      const co = spawnSync("git", ["checkout", targetBranch], { cwd: REPO_ROOT, stdio: "pipe" });
      if (co.status !== 0) {
        log('git', `checkout: FAILED — ${co.stderr.toString().trim()}`);
        return Response.json({ error: `Checkout failed: ${co.stderr.toString()}` }, { status: 500, headers: { "Access-Control-Allow-Origin": "*" } });
      }

      log('git', `checkout: ok — now on ${currentBranch()}`);
      return Response.json({
        ok: true,
        branch: currentBranch(),
      }, { headers: { "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      log('git', `checkout: error — ${e}`);
      return Response.json({ error: String(e) }, { status: 500, headers: { "Access-Control-Allow-Origin": "*" } });
    }
  }

  // ── Claude chat: streaming conversational assistant with tool use ──
  // POST /api/chat { messages[], context?, mode? }
  // Returns SSE stream. LLM can call tools to fetch data from the server
  // before composing a final response.
  if (path === "/api/chat") {
    try {
      const body = await req.json() as {
        messages: Array<{ role: string; content: string }>;
        context?: {
          paperId?: string; blockLabel?: string; blockMd?: string; blockKind?: string;
          selectedText?: string;
          visibleBlocks?: Array<{ label: string; kind: string; title: string }>;
        };
        mode?: "read" | "edit" | "status";
      };

      logDebug("chat", `mode=${body.mode || "read"} msgs=${body.messages.length}`,
        body.context?.blockLabel ? `block=${body.context.blockLabel}` :
        body.context?.visibleBlocks?.length ? `visible=${body.context.visibleBlocks.length} blocks` : undefined);

      const client = getAnthropic();
      if (!client) {
        log("chat", "ANTHROPIC_API_KEY not set — chat unavailable");
        return Response.json(
          { error: "ANTHROPIC_API_KEY not set. Claude chat requires an API key." },
          { status: 503, headers: { "Access-Control-Allow-Origin": "*" } }
        );
      }

      // ── Tool definitions for the chat LLM ──
      const chatTools: Anthropic.Tool[] = [
        {
          name: "get_paper_status",
          description: "Get paper overview: chapters, block counts, proof status, lean formalization stats. Use when the user asks about status, progress, or what needs work.",
          input_schema: {
            type: "object" as const,
            properties: { paperId: { type: "string", description: "Paper ID (optional, uses context if omitted)" } },
            required: [],
          },
        },
        {
          name: "get_todos",
          description: "Get open todos/feedback items. Can filter by paper or specific block. Use when user asks about tasks, what needs attention, or outstanding work. The blockLabel can be a full label like 'def:rigid-monoidal-category' or just the root name like 'rigid-monoidal-category'.",
          input_schema: {
            type: "object" as const,
            properties: {
              paperId: { type: "string", description: "Filter to specific paper" },
              blockLabel: { type: "string", description: "Filter to specific block — accepts full label (e.g. 'def:rigid-monoidal-category') or root name ('rigid-monoidal-category')" },
              status: { type: "string", enum: ["open", "in_progress", "blocked", "resolved"], description: "Filter by status (default: open)" },
            },
            required: [],
          },
        },
        {
          name: "get_block",
          description: "Get full content of a specific block by label (e.g. def:quantum-connection, thm:main-result). Returns kind, title, markdown content, lean status, uses, and tags.",
          input_schema: {
            type: "object" as const,
            properties: { label: { type: "string", description: "Block label (e.g. def:quantum-connection)" } },
            required: ["label"],
          },
        },
        {
          name: "get_chapter_blocks",
          description: "List all blocks in a chapter with their kinds, labels, titles, lean status, and proof status. Use to understand chapter structure or find specific content.",
          input_schema: {
            type: "object" as const,
            properties: {
              paperId: { type: "string", description: "Paper ID" },
              chapterNumber: { type: "number", description: "Chapter number (1-indexed)" },
            },
            required: ["chapterNumber"],
          },
        },
        {
          name: "search_blocks",
          description: "Search blocks by keyword in title, label, tags, or content. Use when user asks about a concept, definition, or theorem by name.",
          input_schema: {
            type: "object" as const,
            properties: { query: { type: "string", description: "Search query" } },
            required: ["query"],
          },
        },
        {
          name: "get_imports",
          description: "List imported papers (from arXiv or uploads). Use when discussing external references or imported results.",
          input_schema: {
            type: "object" as const,
            properties: {},
            required: [],
          },
        },
      ];

      // ── Tool execution (calls server functions directly, no HTTP) ──
      async function executeTool(name: string, input: Record<string, unknown>): Promise<string> {
        const pid = (input.paperId as string) || body.context?.paperId || "";
        logDebug("chat:tool", `${name}`, JSON.stringify(input).slice(0, 200));

        try {
          switch (name) {
            case "get_paper_status": {
              const paper = pid ? await resolvePaper(pid) : null;
              if (!paper) return JSON.stringify({ error: "Paper not found", paperId: pid });
              const stats = {
                title: paper.title,
                chapters: paper.chapters.length,
                totalBlocks: 0, definitions: 0, theorems: 0, lemmas: 0, propositions: 0,
                leanFormalized: 0, leanMissing: 0, leanError: 0, hasSorry: 0, proved: 0,
                openTodos: 0,
              };
              for (const ch of paper.chapters) {
                for (const sec of ch.sections || []) {
                  for (const blk of sec.blocks || []) {
                    stats.totalBlocks++;
                    if (blk.kind === "definition") stats.definitions++;
                    if (blk.kind === "theorem") stats.theorems++;
                    if (blk.kind === "lemma") stats.lemmas++;
                    if (blk.kind === "proposition") stats.propositions++;
                    const nl = ["definition","theorem","lemma","proposition","corollary"].includes(blk.kind);
                    if (nl && blk.lean?.file) stats.leanFormalized++;
                    if (nl && !blk.lean?.file) stats.leanMissing++;
                    if (blk.lean?.validation === "error") stats.leanError++;
                    if (blk.status === "has_sorry") stats.hasSorry++;
                    if (blk.status === "proved" || blk.status === "mathlib_ok") stats.proved++;
                    stats.openTodos += (blk.todos || []).filter((t: any) => t.status === "open").length;
                  }
                }
              }
              // Also count global feedback todos
              const allTodos = listAllFeedback("open");
              const paperTodos = allTodos.filter(t => t.paperId === pid);
              stats.openTodos += paperTodos.length;
              return JSON.stringify(stats);
            }

            case "get_todos": {
              // Accept full label (def:foo-bar) or rootName (foo-bar)
              const rawLabel = (input.blockLabel || input.rootName) as string | undefined;
              const rootName = rawLabel?.replace(/^(def|thm|lem|prop|cor|rem|ex|conj):/, "") || undefined;
              if (rootName && pid) {
                const todos = readFeedback(pid, rootName);
                return JSON.stringify(todos.length ? todos : { message: `No feedback found for '${rootName}' in paper '${pid}'`, rootName });
              }
              const status = (input.status as string) || "open";
              const all = listAllFeedback(status);
              const filtered = pid ? all.filter(t => t.paperId === pid) : all;
              return JSON.stringify(filtered.slice(0, 30));
            }

            case "get_block": {
              const label = input.label as string;
              const paper = pid ? await resolvePaper(pid) : null;
              if (!paper) return JSON.stringify({ error: "Paper not found" });
              for (const ch of paper.chapters) {
                for (const sec of ch.sections || []) {
                  for (const blk of sec.blocks || []) {
                    if (blk.label === label) {
                      return JSON.stringify({
                        kind: blk.kind, label: blk.label, title: blk.title,
                        md: (blk.md || "").slice(0, 3000),
                        lean: blk.lean ? { decl: blk.lean.decl, validation: blk.lean.validation, sorryFree: blk.lean.sorryFree } : null,
                        status: blk.status, uses: blk.uses, tags: blk.tags,
                        chapter: ch.title, section: sec.title,
                      });
                    }
                  }
                }
              }
              return JSON.stringify({ error: `Block not found: ${label}` });
            }

            case "get_chapter_blocks": {
              const chNum = input.chapterNumber as number;
              const paper = pid ? await resolvePaper(pid) : null;
              if (!paper) return JSON.stringify({ error: "Paper not found" });
              const ch = paper.chapters.find((c: any) => c.number === chNum);
              if (!ch) return JSON.stringify({ error: `Chapter ${chNum} not found` });
              const blocks: unknown[] = [];
              for (const sec of ch.sections || []) {
                for (const blk of sec.blocks || []) {
                  blocks.push({
                    kind: blk.kind, label: blk.label, title: blk.title,
                    status: blk.status,
                    lean: blk.lean ? { decl: blk.lean.decl, validation: blk.lean.validation } : null,
                    section: sec.title,
                  });
                }
              }
              return JSON.stringify({ chapter: ch.title, blocks });
            }

            case "search_blocks": {
              const q = (input.query as string || "").toLowerCase();
              const paper = pid ? await resolvePaper(pid) : null;
              if (!paper) return JSON.stringify({ error: "Paper not found" });
              const matches: unknown[] = [];
              for (const ch of paper.chapters) {
                for (const sec of ch.sections || []) {
                  for (const blk of sec.blocks || []) {
                    const searchable = [blk.label, blk.title, blk.kind, ...(blk.tags || []), (blk.md || "").slice(0, 500)].join(" ").toLowerCase();
                    if (searchable.includes(q)) {
                      matches.push({
                        kind: blk.kind, label: blk.label, title: blk.title,
                        status: blk.status, chapter: ch.title, section: sec.title,
                        snippet: (blk.md || "").slice(0, 200),
                      });
                    }
                    if (matches.length >= 15) break;
                  }
                  if (matches.length >= 15) break;
                }
                if (matches.length >= 15) break;
              }
              return JSON.stringify(matches);
            }

            case "get_imports": {
              const uploadsDir = join(REPO_ROOT, "uploads");
              const imports: unknown[] = [];
              if (existsSync(uploadsDir)) {
                const { readdirSync: rd } = await import("fs");
                for (const d of rd(uploadsDir)) {
                  const mp = join(uploadsDir, d, "import-meta.json");
                  if (existsSync(mp)) {
                    try { imports.push(JSON.parse(readFileSync(mp, "utf-8"))); } catch {}
                  }
                }
              }
              return JSON.stringify(imports);
            }

            default:
              return JSON.stringify({ error: `Unknown tool: ${name}` });
          }
        } catch (e) {
          return JSON.stringify({ error: String(e) });
        }
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

You have tools to fetch live data from the paper system. Use them proactively — don't guess at paper status, todos, or block content when you can look it up.

Keep responses concise and well-formatted. Use $...$ for inline math and $$...$$ for display math.`;

      if (mode === "status") {
        systemPrompt += `\n\nThe user is in EDITOR mode. They want to understand the paper's current status — what's complete, what needs work, what the priorities are. Focus on actionable summaries. Use get_paper_status and get_todos to get real data.`;
      } else if (mode === "edit") {
        systemPrompt += `\n\nThe user is in EDITOR mode. They may want to report errors, suggest improvements, or discuss editorial decisions. Use tools to fetch block content and todos before responding.`;
      } else {
        systemPrompt += `\n\nThe user is in READER mode. They're studying the paper and want to understand the content. Use get_block to fetch full content when explaining. Prioritize clear explanations and intuition.`;
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
        if (ctx.visibleBlocks?.length) {
          const vbList = ctx.visibleBlocks.slice(0, 10).map(b => `- ${b.label} (${b.kind}): ${b.title}`).join("\n");
          systemPrompt += `\n\nBlocks currently visible on screen:\n${vbList}`;
        }
        if (ctx.paperId) {
          systemPrompt += `\n\nPaper ID: ${ctx.paperId}`;
          // Eagerly fetch todos for the context block so LLM has them immediately
          if (ctx.blockLabel) {
            const rootName = ctx.blockLabel.replace(/^(def|thm|lem|prop|cor|rem|ex|conj):/, "");
            const blockTodos = readFeedback(ctx.paperId, rootName);
            const openTodos = (blockTodos as any[]).filter((t: any) => t.status === "open" || t.status === "in_progress");
            if (openTodos.length) {
              systemPrompt += `\n\nOpen todos/feedback for this block (${ctx.blockLabel}):\n${JSON.stringify(openTodos, null, 2)}`;
            }
          }
        }
      }

      // ── Tool-use loop: let LLM call tools, then stream final response ──
      const apiMessages: Anthropic.MessageParam[] = body.messages.map(m => ({
        role: m.role as "user" | "assistant",
        content: m.content,
      }));

      // Run tool-use loop (non-streaming, max 3 rounds)
      let toolRounds = 0;
      const MAX_TOOL_ROUNDS = 3;
      while (toolRounds < MAX_TOOL_ROUNDS) {
        const response = await client.messages.create({
          model: "claude-haiku-4-5-20251001",
          max_tokens: 1500,
          system: systemPrompt,
          tools: chatTools,
          messages: apiMessages,
        });

        // Check if the model wants to use tools
        const toolUses = response.content.filter(b => b.type === "tool_use");
        if (toolUses.length === 0) {
          // No tool calls — this is the final response, stream it back
          const textBlocks = response.content.filter(b => b.type === "text");
          const fullText = textBlocks.map(b => (b as any).text).join("");

          const encoder = new TextEncoder();
          const readable = new ReadableStream({
            start(controller) {
              // Send in chunks for streaming feel
              const chunkSize = 20;
              for (let i = 0; i < fullText.length; i += chunkSize) {
                controller.enqueue(encoder.encode(`data: ${JSON.stringify({ text: fullText.slice(i, i + chunkSize) })}\n\n`));
              }
              controller.enqueue(encoder.encode(`data: [DONE]\n\n`));
              logDebug("chat", `complete (${toolRounds} tool rounds, ${fullText.length} chars)`);
              controller.close();
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
        }

        // Execute tool calls
        logDebug("chat:tools", `round ${toolRounds + 1}: ${toolUses.length} tool calls`,
          toolUses.map(t => (t as any).name).join(", "));

        // Add assistant message with tool use
        apiMessages.push({ role: "assistant", content: response.content });

        // Execute all tool calls and add results
        const toolResults: Anthropic.ToolResultBlockParam[] = [];
        for (const tu of toolUses) {
          const toolUseBlock = tu as Anthropic.ToolUseBlock;
          const result = await executeTool(toolUseBlock.name, toolUseBlock.input as Record<string, unknown>);
          toolResults.push({
            type: "tool_result",
            tool_use_id: toolUseBlock.id,
            content: result,
          });
        }
        apiMessages.push({ role: "user", content: toolResults });
        toolRounds++;
      }

      // If we exhausted tool rounds, do a final streaming call without tools
      logDebug("chat", `max tool rounds reached (${MAX_TOOL_ROUNDS}), final call`);
      const stream = await client.messages.stream({
        model: "claude-haiku-4-5-20251001",
        max_tokens: 1500,
        system: systemPrompt,
        messages: apiMessages,
      });

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
            logDebug("chat", "stream complete (after tool rounds)");
            controller.close();
          } catch (e) {
            log("chat", "stream error", String(e));
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

  // ── Paper import: upload file ────────────────────────────────
  // POST /api/import/upload  (multipart/form-data with file + metadata)
  if (path === "/api/import/upload") {
    try {
      const formData = await req.formData();
      const file = formData.get("file") as File | null;
      const paperId = (formData.get("paperId") as string) || "";
      const source = (formData.get("source") as string) || "upload";

      if (!file) return Response.json({ error: "No file uploaded" }, { status: 400 });

      const id = paperId || file.name.replace(/\.[^.]+$/, "").replace(/[^a-z0-9-]/gi, "-").toLowerCase();
      const uploadDir = join(REPO_ROOT, "uploads", id);
      mkdirSync(uploadDir, { recursive: true });

      // Save the file
      const buf = Buffer.from(await file.arrayBuffer());
      const ext = extname(file.name) || (file.type === "application/pdf" ? ".pdf" : ".tex");
      const filename = ext === ".pdf" ? "original.pdf" : file.name;
      writeFileSync(join(uploadDir, filename), buf);

      // Write import metadata
      const meta = {
        source,
        title: formData.get("title") || file.name,
        format: ext === ".pdf" ? "pdf" : "latex",
        files: [filename],
        uploadedAt: new Date().toISOString(),
        paperId: id,
      };
      writeFileSync(join(uploadDir, "import-meta.json"), JSON.stringify(meta, null, 2));
      log("import", `uploaded ${filename} → uploads/${id}/`, `${buf.length} bytes`);

      return Response.json({ ok: true, paperId: id, uploadDir: `uploads/${id}`, meta }, {
        headers: { "Access-Control-Allow-Origin": "*" },
      });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // POST /api/import/arxiv { arxivId }
  if (path === "/api/import/arxiv") {
    try {
      const body = await req.json() as { arxivId: string; paperId?: string };
      const arxivId = body.arxivId.replace(/^(https?:\/\/)?(arxiv\.org\/(abs|pdf)\/)?/, "").replace(/\.pdf$/, "").trim();
      if (!arxivId) return Response.json({ error: "Missing arxivId" }, { status: 400 });

      // Fetch arXiv metadata
      const metaRes = await fetch(`https://export.arxiv.org/api/query?id_list=${encodeURIComponent(arxivId)}`);
      if (!metaRes.ok) throw new Error(`arXiv API: ${metaRes.status}`);
      const xml = await metaRes.text();

      // Parse basic fields from Atom XML
      const title = xml.match(/<title[^>]*>([\s\S]*?)<\/title>/g)?.[1]?.replace(/<[^>]+>/g, "").trim() || arxivId;
      const authors = [...xml.matchAll(/<name>(.*?)<\/name>/g)].map(m => m[1]);
      const summary = xml.match(/<summary>([\s\S]*?)<\/summary>/)?.[1]?.trim() || "";
      const doi = xml.match(/<arxiv:doi[^>]*>(.*?)<\/arxiv:doi>/)?.[1] || "";
      const categories = [...xml.matchAll(/<category[^>]*term="([^"]+)"/g)].map(m => m[1]);
      const published = xml.match(/<published>(.*?)<\/published>/)?.[1] || "";

      const id = body.paperId || `arxiv-${arxivId.replace(/[/.]/g, "-")}`;
      const uploadDir = join(REPO_ROOT, "uploads", id);
      mkdirSync(uploadDir, { recursive: true });

      // Try to fetch LaTeX source
      let sourceFiles: string[] = [];
      let format = "metadata-only";
      try {
        const srcRes = await fetch(`https://arxiv.org/e-print/${arxivId}`);
        if (srcRes.ok) {
          const srcBuf = Buffer.from(await srcRes.arrayBuffer());
          const contentType = srcRes.headers.get("content-type") || "";
          if (contentType.includes("gzip") || contentType.includes("tar")) {
            writeFileSync(join(uploadDir, "source.tar.gz"), srcBuf);
            // Extract using tar
            const { execSync } = await import("child_process");
            try {
              execSync(`tar xzf source.tar.gz`, { cwd: uploadDir, timeout: 15000 });
              const { readdirSync } = await import("fs");
              sourceFiles = readdirSync(uploadDir).filter(f => f.endsWith(".tex"));
              format = "latex";
            } catch { /* tar extract failed — might be single file */ }
            if (!sourceFiles.length) {
              // Try as single .tex file
              try {
                const { renameSync } = await import("fs");
                renameSync(join(uploadDir, "source.tar.gz"), join(uploadDir, "main.tex"));
                sourceFiles = ["main.tex"];
                format = "latex";
              } catch {}
            }
          } else {
            // Plain text source
            writeFileSync(join(uploadDir, "main.tex"), srcBuf);
            sourceFiles = ["main.tex"];
            format = "latex";
          }
        }
      } catch (e) {
        log("import", `arXiv source fetch failed for ${arxivId}:`, String(e));
      }

      // Write import metadata
      const meta = {
        source: "arxiv",
        arxivId,
        url: `https://arxiv.org/abs/${arxivId}`,
        title,
        authors,
        abstract: summary,
        doi,
        categories,
        published,
        format,
        files: sourceFiles,
        fetchedAt: new Date().toISOString(),
        paperId: id,
      };
      writeFileSync(join(uploadDir, "import-meta.json"), JSON.stringify(meta, null, 2));
      log("import", `fetched arXiv:${arxivId} → uploads/${id}/`, `${sourceFiles.length} .tex files`);

      return Response.json({ ok: true, paperId: id, uploadDir: `uploads/${id}`, meta }, {
        headers: { "Access-Control-Allow-Origin": "*" },
      });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // POST /api/import/scan { paperId } — scan uploaded files for environments
  if (path === "/api/import/scan") {
    try {
      const body = await req.json() as { paperId: string };
      const uploadDir = join(REPO_ROOT, "uploads", body.paperId);
      const metaPath = join(uploadDir, "import-meta.json");
      if (!existsSync(metaPath)) {
        return Response.json({ error: `No import found: ${body.paperId}` }, { status: 404 });
      }
      const meta = JSON.parse(readFileSync(metaPath, "utf-8"));

      // Scan .tex files for theorem environments
      const envRe = /\\begin\{(theorem|definition|proposition|lemma|corollary|conjecture|example|remark|proof)\}(\[([^\]]*)\])?([\s\S]*?)\\end\{\1\}/g;
      const labelRe = /\\label\{([^}]+)\}/;
      const blocks: Array<{
        kind: string; title: string; label: string; body: string;
        file: string; line: number; originalEnv: string;
      }> = [];

      const { readdirSync } = await import("fs");
      const texFiles = meta.files?.length ? meta.files : readdirSync(uploadDir).filter((f: string) => f.endsWith(".tex"));

      for (const tf of texFiles) {
        const texPath = join(uploadDir, tf);
        if (!existsSync(texPath)) continue;
        const src = readFileSync(texPath, "utf-8");
        const lines = src.split("\n");

        let match;
        while ((match = envRe.exec(src)) !== null) {
          const kind = match[1];
          const optTitle = match[3] || "";
          const body = match[4].trim();
          const lblMatch = body.match(labelRe);
          const label = lblMatch?.[1] || "";

          // Find line number
          const beforeMatch = src.slice(0, match.index);
          const line = beforeMatch.split("\n").length;

          blocks.push({
            kind,
            title: optTitle,
            label,
            body: body.replace(labelRe, "").trim(),
            file: tf,
            line,
            originalEnv: match[0],
          });
        }

        // Also scan for custom theorem environments (\newtheorem{thm}{Theorem})
        const customRe = /\\newtheorem\{(\w+)\}(?:\[(\w+)\])?\{(\w+)\}/g;
        const customEnvs = new Map<string, string>();
        let cm;
        while ((cm = customRe.exec(src)) !== null) {
          const envName = cm[1];
          const displayName = cm[3].toLowerCase();
          const kindMap: Record<string, string> = {
            theorem: "theorem", definition: "definition", proposition: "proposition",
            lemma: "lemma", corollary: "corollary", conjecture: "conjecture",
            example: "example", remark: "remark",
          };
          customEnvs.set(envName, kindMap[displayName] || "theorem");
        }

        // Scan for custom environments
        for (const [envName, kind] of customEnvs) {
          const customEnvRe = new RegExp(`\\\\begin\\{${envName}\\}(\\[([^\\]]*)\\])?([\\s\\S]*?)\\\\end\\{${envName}\\}`, "g");
          let m;
          while ((m = customEnvRe.exec(src)) !== null) {
            const optTitle = m[2] || "";
            const body = m[3].trim();
            const lblMatch = body.match(labelRe);
            const beforeMatch = src.slice(0, m.index);
            blocks.push({
              kind,
              title: optTitle,
              label: lblMatch?.[1] || "",
              body: body.replace(labelRe, "").trim(),
              file: tf,
              line: beforeMatch.split("\n").length,
              originalEnv: m[0],
            });
          }
        }
      }

      // Cache extraction results
      writeFileSync(join(uploadDir, "extracted-blocks.json"), JSON.stringify(blocks, null, 2));

      // Summary
      const summary: Record<string, number> = {};
      for (const b of blocks) summary[b.kind] = (summary[b.kind] || 0) + 1;

      log("import", `scanned ${body.paperId}:`, `${blocks.length} blocks found`);
      return Response.json({ ok: true, paperId: body.paperId, meta, blocks, summary }, {
        headers: { "Access-Control-Allow-Origin": "*" },
      });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // POST /api/import/generate { paperId, blocks: [{kind, title, label, body, rootName}], chapterTitle }
  // Generates content objects from confirmed blocks
  if (path === "/api/import/generate") {
    try {
      const body = await req.json() as {
        paperId: string;
        chapterTitle?: string;
        chapterDir?: string;
        blocks: Array<{
          kind: string; title: string; label: string; body: string;
          rootName: string; generateLean?: boolean;
        }>;
        source?: { type: string; id: string; url: string; citationKey: string };
      };

      const paperDir = join(REPO_ROOT, "content", body.paperId);
      const chDir = body.chapterDir || `imported-${body.source?.id || "upload"}`.replace(/[^a-z0-9-]/gi, "-").toLowerCase();
      const chapterPath = join(paperDir, chDir);
      mkdirSync(chapterPath, { recursive: true });

      const generated: string[] = [];
      const blockRefs: string[] = [];
      const { writeFileSync: wfs } = await import("fs");

      for (const blk of body.blocks) {
        const rn = blk.rootName;
        blockRefs.push(rn);

        // Generate .ts manifest
        const kindToPrefix: Record<string, string> = {
          definition: "def", theorem: "thm", lemma: "lem", proposition: "prop",
          corollary: "cor", conjecture: "conj", example: "ex", remark: "rem", proof: "prf",
        };
        const prefix = kindToPrefix[blk.kind] || "thm";
        const label = blk.label || `${prefix}:imported-${rn}`;

        const builderName = blk.kind === "proof" ? "proof" : blk.kind;
        const metaFields = body.source ? `\n  meta: { source: "${body.source.type}:${body.source.id}", originalLabel: "${blk.label || ""}", importedAt: "${new Date().toISOString()}" },` : "";
        const tagsField = `\n  tags: ["imported"${body.source ? `, "${body.source.type}:${body.source.id}"` : ""}],`;

        let tsContent = `import { ${builderName} } from "../../schema/builders";\n\nexport default ${builderName}({\n  label: "${label}",`;
        if (blk.title) tsContent += `\n  title: "${blk.title.replace(/"/g, '\\"')}",`;
        tsContent += tagsField;
        tsContent += metaFields;
        if (blk.kind === "definition") {
          tsContent += `\n  lean: { decl: "QOU.Imported.${rn.replace(/-/g, "_")}" },\n  status: "not_started",`;
        }
        tsContent += "\n});\n";
        wfs(join(chapterPath, `${rn}.ts`), tsContent);

        // Generate .md content
        let mdContent = blk.body || "";
        // Basic LaTeX → project markdown conversion
        mdContent = mdContent
          .replace(/\\textbf\{([^}]+)\}/g, "**$1**")
          .replace(/\\emph\{([^}]+)\}/g, "*$1*")
          .replace(/\\cite\{([^}]+)\}/g, "[$1]")
          .replace(/\\ref\{([^}]+)\}/g, "[](#$1)");
        wfs(join(chapterPath, `${rn}.md`), mdContent);

        generated.push(rn);
      }

      // Generate chapter manifest
      const chapterTs = `import { chapter } from "../../schema/builders";\n\nexport default chapter({\n  number: 99,\n  title: "${(body.chapterTitle || `Imported: ${body.source?.id || "Upload"}`).replace(/"/g, '\\"')}",\n  sections: [{\n    title: "Imported Results",\n    blocks: ${JSON.stringify(blockRefs)},\n  }],\n});\n`;
      wfs(join(chapterPath, `${chDir}.ts`), chapterTs);

      log("import", `generated ${generated.length} content objects`, `→ content/${body.paperId}/${chDir}/`);
      return Response.json({
        ok: true,
        paperId: body.paperId,
        chapterDir: chDir,
        generated,
        path: `content/${body.paperId}/${chDir}`,
      }, { headers: { "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // GET /api/import/list — list all imports
  if (path === "/api/import/list") {
    // Handled as GET in handleViewerRequest
  }

  // ── AI triage: review feedback and propose action ────────────
  // POST /api/feedback/triage { paperId, rootName, todoId }
  if (path === "/api/feedback/triage") {
    try {
      const body = await req.json() as { paperId: string; rootName: string; todoId: string };
      const todos = readFeedback(body.paperId, body.rootName);
      const todo = (todos as any[]).find(t => t.id === body.todoId);
      if (!todo) return Response.json({ error: "Todo not found" }, { status: 404 });

      // Read the block content for context (O(1) via blocksByName map)
      const paper = await resolvePaper(body.paperId);
      const blk = paper?.blocksByName?.get(body.rootName);
      const blockContent = blk?.md || "";
      const blockKind = blk?.kind || "";

      const triage = await triageFeedback(todo, blockContent, blockKind, body.paperId, body.rootName);
      return Response.json(triage, { headers: { "Access-Control-Allow-Origin": "*" } });
    } catch (e) {
      return Response.json({ error: String(e) }, { status: 500 });
    }
  }

  // ── Update feedback todo (priority / status) ──────────────────
  if (path === "/api/feedback/update") {
    try {
      const body = await req.json() as {
        paperId: string; rootName: string; todoId: string;
        priority?: string; status?: string;
      };
      const todos = readFeedback(body.paperId, body.rootName) as any[];
      const idx = todos.findIndex((t: any) => t.id === body.todoId);
      if (idx < 0) return Response.json({ error: "Todo not found" }, { status: 404 });
      if (body.priority !== undefined) todos[idx].priority = body.priority;
      if (body.status !== undefined) todos[idx].status = body.status;
      writeFeedback(body.paperId, body.rootName, todos);
      return Response.json({ ok: true, todo: todos[idx] });
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

const LOG_DEBUG = process.env.LOG_LEVEL !== 'quiet';
const LOG_JSON = process.env.LOG_FORMAT === 'json';

function log(category: string, message: string, detail?: string) {
  const ts = new Date().toISOString();
  if (LOG_JSON) {
    const entry: Record<string, unknown> = { ts, cat: category, msg: message };
    if (detail) entry.detail = detail;
    console.error(JSON.stringify(entry));
  } else {
    const d = detail ? ` ${detail}` : '';
    console.error(`[${ts.slice(11, 23)}] [${category}]  ${message}${d}`);
  }
}

function logDebug(category: string, message: string, detail?: string) {
  if (LOG_DEBUG) log(category, message, detail);
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
      logDebug('http', `${req.method} ${url.pathname}`);

      // Root → redirect to assistant
      if (url.pathname === "/" || url.pathname === "") {
        return Response.redirect(`http://localhost:${viewerPort}/assistant/`, 302);
      }

      // Health check
      if (url.pathname === "/health") {
        return Response.json({ status: "ok", mode: "stdio", version: "0.1.0" });
      }

      // POST requests (save, feedback, import)
      if (req.method === "POST") {
        const postRes = await handlePostRequest(url, req);
        if (postRes) { logDebug('http', `${req.method} ${url.pathname}`, `→ ${postRes.status} (${Date.now()-start}ms)`); return postRes; }
      }

      const viewerRes = await handleViewerRequest(url);
      if (viewerRes) { logDebug('http', `${req.method} ${url.pathname}`, `→ ${viewerRes.status} (${Date.now()-start}ms)`); return viewerRes; }

      logDebug('http', `${req.method} ${url.pathname}`, `→ 404 (${Date.now()-start}ms)`);
      return new Response("Not found", { status: 404 });
    },
  });

  log('init', `MCP server started (stdio, repo: ${REPO_ROOT})`);
  const branch = currentBranch();
  const branchSuffix = branch && branch !== 'main' && branch !== 'master'
    ? `#/@${encodeURIComponent(branch)}` : '';
  log('init', `Viewer: http://localhost:${viewerPort}/viewer/${branchSuffix}`);
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
      const start = Date.now();
      logDebug('http', `${req.method} ${url.pathname}`);

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
        if (postRes) { logDebug('http', `${req.method} ${url.pathname}`, `→ ${postRes.status} (${Date.now()-start}ms)`); return postRes; }
      }

      // Viewer/Assistant routes
      const viewerRes = await handleViewerRequest(url);
      if (viewerRes) return viewerRes;

      return new Response("Not found", { status: 404 });
    },
  });

  console.error(`[qou-mcp] Assistant started (HTTP :${port}, repo: ${REPO_ROOT})`);
  console.error(`[qou-mcp] MCP: http://localhost:${port}/mcp`);
  const brH = currentBranch();
  const brSuffix = brH && brH !== 'main' && brH !== 'master'
    ? `#/@${encodeURIComponent(brH)}` : '';
  console.error(`[qou-mcp] Viewer: http://localhost:${port}/viewer/${brSuffix}`);
}
