/**
 * Viewer dev server (optional convenience wrapper).
 *
 * Serves the SPA + paper.json with auto-reload via the JSON API.
 * The viewer works without this server — just open index.html with paper.json
 * in the same directory.
 *
 * Usage:
 *   bun run viewer/serve.ts
 *   bun run viewer/serve.ts --port 3200
 *   bun run viewer/serve.ts --open
 *
 * @module viewer/serve
 */

import { readFileSync, existsSync } from "fs";
import { join, resolve, extname } from "path";

const REPO_ROOT = resolve(import.meta.dir, "..");
const VIEWER_DIR = import.meta.dir;
const BUILD_DIR = join(REPO_ROOT, "build", "viewer");

const args = process.argv.slice(2);
const PORT = parseInt(args.find((_, i, a) => a[i - 1] === "--port") || "3200", 10);
const OPEN = args.includes("--open");

const MIME: Record<string, string> = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json",
  ".svg": "image/svg+xml",
  ".png": "image/png",
};

function tryFile(...paths: string[]): Response | null {
  for (const p of paths) {
    if (existsSync(p)) {
      return new Response(readFileSync(p), {
        headers: {
          "Content-Type": MIME[extname(p)] || "application/octet-stream",
          "Cache-Control": "no-cache",
          "Access-Control-Allow-Origin": "*",
        },
      });
    }
  }
  return null;
}

Bun.serve({
  port: PORT,
  fetch(req) {
    const path = new URL(req.url).pathname;

    if (path === "/" || path === "/index.html")
      return tryFile(join(VIEWER_DIR, "index.html"))!;

    // paper.json — try build output first, then viewer dir
    if (path === "/paper.json" || path === "/api/paper")
      return tryFile(join(BUILD_DIR, "paper.json"), join(VIEWER_DIR, "paper.json"))
        || new Response("paper.json not found. Run: bun run content/pipeline/export-json.ts", { status: 404 });

    // Rendered assets
    if (path.startsWith("/assets/"))
      return tryFile(join(BUILD_DIR, path.slice(1))) || new Response("Not found", { status: 404 });

    // Static files from viewer dir
    return tryFile(join(VIEWER_DIR, path.slice(1))) || new Response("Not found", { status: 404 });
  },
});

console.log(`\n  QOU Viewer: http://localhost:${PORT}`);
console.log(`  Paper JSON: ${existsSync(join(BUILD_DIR, "paper.json")) ? BUILD_DIR + "/paper.json" : "(not built yet)"}`);
console.log(`  Run export: bun run content/pipeline/export-json.ts\n`);

if (OPEN) {
  const cmd = process.platform === "darwin" ? "open" : "xdg-open";
  Bun.spawn([cmd, `http://localhost:${PORT}`]);
}
