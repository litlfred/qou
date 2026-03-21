/**
 * Viewer dev server.
 *
 * Serves the content object tree as a JSON API and the viewer HTML/CSS/JS
 * as static files. The viewer polls `/api/paper` for content updates.
 *
 * Usage:
 *   bun run serve.ts                          # default paper
 *   bun run serve.ts --paper quantum-observable-universe
 *   bun run serve.ts --port 3000
 *   bun run serve.ts --open                   # open browser after start
 *
 * API:
 *   GET /                   → viewer HTML
 *   GET /api/paper          → full paper tree as JSON (blocks + md inlined)
 *   GET /api/paper?hash=X   → 304 if unchanged
 *   GET /api/rendered/*     → pre-rendered assets
 *
 * @module viewer/serve
 */

import { readFileSync, existsSync, statSync, readdirSync } from "fs";
import { join, resolve, extname } from "path";
import { createHash } from "crypto";
import type { Paper, ChapterRef, Chapter, Section, Block, RenderedAsset } from "../content/schema/types";

// ── Config ───────────────────────────────────────────────────────

const REPO_ROOT = resolve(import.meta.dir, "..");
const CONTENT_ROOT = join(REPO_ROOT, "content");
const VIEWER_DIR = import.meta.dir;

const args = process.argv.slice(2);
function arg(name: string, fallback: string): string {
  const idx = args.indexOf(`--${name}`);
  return idx >= 0 && args[idx + 1] ? args[idx + 1] : fallback;
}

const PAPER_NAME = arg("paper", "quantum-observable-universe");
const PORT = parseInt(arg("port", "3200"), 10);
const OPEN = args.includes("--open");

const PAPER_DIR = join(CONTENT_ROOT, PAPER_NAME);

// ── Content loader ───────────────────────────────────────────────

interface ResolvedBlock {
  rootName: string;
  kind: string;
  label?: string;
  title?: string;
  uses?: string[];
  lean?: unknown;
  status?: string;
  hasProof?: boolean;
  tex?: string;
  caption?: string;
  rendered?: RenderedAsset[];
  md: string;
  mdModified: string;
  meta?: Record<string, unknown>;
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
}

interface ResolvedPaper {
  title: string;
  authors: string[];
  date?: string;
  chapters: ResolvedChapter[];
  meta?: Record<string, unknown>;
  _hash: string;
  _built: string;
}

/**
 * Walk the content tree starting from a paper manifest .ts,
 * dynamically importing all manifests and reading .md files.
 */
async function loadPaper(): Promise<ResolvedPaper> {
  const paperPath = join(PAPER_DIR, `${PAPER_NAME}.ts`);
  // Bust Bun's module cache by appending a query param
  const paper: Paper = (await import(`${paperPath}?t=${Date.now()}`)).default;

  const chapters: ResolvedChapter[] = [];

  for (const chRef of paper.chapters) {
    const chDir = join(PAPER_DIR, chRef.dir);
    const chPath = join(chDir, `${chRef.dir}.ts`);
    const ch: Chapter = (await import(`${chPath}?t=${Date.now()}`)).default;

    const sections: ResolvedSection[] = [];

    for (const sec of ch.sections) {
      // Skip section refs for now (inline sections only)
      if ("name" in sec && !("blocks" in sec)) continue;
      const section = sec as Section;

      const blocks: ResolvedBlock[] = [];

      for (const rootName of section.blocks) {
        const tsPath = join(chDir, `${rootName}.ts`);
        const mdPath = join(chDir, `${rootName}.md`);

        try {
          const block: Block = (await import(`${tsPath}?t=${Date.now()}`)).default;
          const md = existsSync(mdPath) ? readFileSync(mdPath, "utf-8") : "";
          const mdStat = existsSync(mdPath) ? statSync(mdPath) : null;

          blocks.push({
            rootName,
            kind: block.kind,
            label: "label" in block ? block.label : undefined,
            title: "title" in block ? block.title : undefined,
            uses: "uses" in block ? block.uses : undefined,
            lean: "lean" in block ? block.lean : undefined,
            status: "status" in block ? block.status : undefined,
            hasProof: "hasProof" in block ? block.hasProof : undefined,
            tex: "tex" in block ? block.tex : undefined,
            caption: "caption" in block ? block.caption : undefined,
            rendered: "rendered" in block ? block.rendered : undefined,
            md,
            mdModified: mdStat ? mdStat.mtime.toISOString() : "",
            meta: "meta" in block ? block.meta : undefined,
          });
        } catch (e) {
          blocks.push({
            rootName,
            kind: "error",
            md: `Failed to load: ${e instanceof Error ? e.message : String(e)}`,
            mdModified: "",
          });
        }
      }

      sections.push({
        title: section.title,
        label: section.label,
        blocks,
      });
    }

    chapters.push({
      number: ch.number,
      title: ch.title,
      label: ch.label,
      sections,
    });
  }

  const result: Omit<ResolvedPaper, "_hash"> = {
    title: paper.title,
    authors: paper.authors,
    date: paper.date,
    chapters,
    meta: paper.meta,
    _built: new Date().toISOString(),
  };

  const hash = createHash("sha256")
    .update(JSON.stringify(result))
    .digest("hex")
    .slice(0, 12);

  return { ...result, _hash: hash } as ResolvedPaper;
}

// ── Static file serving ──────────────────────────────────────────

const MIME_TYPES: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".woff2": "font/woff2",
  ".woff": "font/woff",
};

function serveStatic(filePath: string): Response | null {
  if (!existsSync(filePath)) return null;
  const ext = extname(filePath);
  const mime = MIME_TYPES[ext] || "application/octet-stream";
  return new Response(readFileSync(filePath), {
    headers: { "Content-Type": mime, "Cache-Control": "no-cache" },
  });
}

// ── HTTP server ──────────────────────────────────────────────────

let cachedPaper: ResolvedPaper | null = null;

const server = Bun.serve({
  port: PORT,
  async fetch(req) {
    const url = new URL(req.url);
    const path = url.pathname;

    // CORS headers for local dev
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET",
    };

    // API: full paper tree
    if (path === "/api/paper") {
      try {
        const paper = await loadPaper();

        // 304 if hash matches
        const clientHash = url.searchParams.get("hash");
        if (clientHash && clientHash === paper._hash) {
          return new Response(null, { status: 304, headers: corsHeaders });
        }

        cachedPaper = paper;
        return Response.json(paper, {
          headers: { ...corsHeaders, "Cache-Control": "no-cache" },
        });
      } catch (e) {
        return Response.json(
          { error: e instanceof Error ? e.message : String(e) },
          { status: 500, headers: corsHeaders },
        );
      }
    }

    // Pre-rendered assets
    if (path.startsWith("/api/rendered/")) {
      const assetPath = join(REPO_ROOT, "build", "rendered", path.slice("/api/rendered/".length));
      const res = serveStatic(assetPath);
      if (res) return res;
      return new Response("Not found", { status: 404 });
    }

    // KaTeX CSS/fonts from node_modules
    if (path.startsWith("/katex/")) {
      const katexPath = join(VIEWER_DIR, "node_modules", "katex", "dist", path.slice("/katex/".length));
      const res = serveStatic(katexPath);
      if (res) return res;
      return new Response("Not found", { status: 404 });
    }

    // Static viewer files
    if (path === "/" || path === "/index.html") {
      return serveStatic(join(VIEWER_DIR, "index.html"))!;
    }

    const staticRes = serveStatic(join(VIEWER_DIR, path.slice(1)));
    if (staticRes) return staticRes;

    return new Response("Not found", { status: 404 });
  },
});

console.log(`\n  QOU Viewer: http://localhost:${PORT}`);
console.log(`  Paper:      ${PAPER_NAME}`);
console.log(`  API:        http://localhost:${PORT}/api/paper\n`);

if (OPEN) {
  const cmd = process.platform === "darwin" ? "open" : "xdg-open";
  Bun.spawn([cmd, `http://localhost:${PORT}`]);
}
