#!/usr/bin/env bun
/**
 * `corpus_search` from the command line — the fallback for AGENTS.md
 * §"Before declaring open" step 0 when the MCP tool is not reachable.
 *
 * Usage:
 *   bun run scripts/corpus-search.ts "<query>" [--direction in|out|both] [--search-text]
 *                                    [--hops N] [--limit N] [--provenance authored|ingested]
 *
 * Prints exactly the JSON the platform's `corpus_search` tool returns: it calls
 * the same handler (`executeGraphTool` in
 * `folio-assistant/cat-harness-tools/adapters/mcp-server/tools/graph.ts`), over
 * the same roots the MCP server uses — the declared folio directory plus every
 * declared `library` directory from qou.json, falling back to `folio/` and
 * `library/` when nothing is declared.
 *
 * Why this exists (bean qou-q261): the `paper-assistant` MCP server does not
 * expose `corpus_search` on its tool list at the pinned platform — the handler
 * lives only inside the server's embedded chat agent — so the step-0 check was
 * unrunnable from an agent session. This wrapper makes it runnable today; it
 * does not depend on the platform fix.
 *
 * Query semantics worth knowing: seeding is lexical over labels, titles, kinds
 * and tags (`--search-text` adds companion prose). A short phrase ("Bring",
 * "Temperley-Lieb") seeds; a long multi-word query that is not a phrase present
 * in some node can seed NOTHING, and an empty result then says nothing about
 * the corpus. Read `summary` and `emptyRoots` before reading an absence.
 */
import { existsSync } from "node:fs";
import { join, resolve } from "node:path";

const ROOT = resolve(import.meta.dir, "..");
const PLATFORM = join(ROOT, "folio-assistant");
const GRAPH_MODULE = join(PLATFORM, "cat-harness-tools/adapters/mcp-server/tools/graph.ts");
const DECL_MODULE = join(PLATFORM, "cat-harness/schemas/cat-harness.ts");

function usage(code: number): never {
  const out = code === 0 ? console.log : console.error;
  out(
    'usage: bun run scripts/corpus-search.ts "<query>" [--direction in|out|both] [--search-text]\n' +
      "                                        [--hops N] [--limit N] [--provenance authored|ingested]",
  );
  process.exit(code);
}

const argv = process.argv.slice(2);
if (argv.includes("-h") || argv.includes("--help")) usage(0);

const input: Record<string, unknown> = {};
const positional: string[] = [];
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  const next = () => {
    const v = argv[++i];
    if (v === undefined) {
      console.error(`${a} needs a value`);
      usage(2);
    }
    return v;
  };
  if (a === "--direction") {
    const v = next();
    if (v !== "in" && v !== "out" && v !== "both") {
      console.error(`--direction must be in, out or both (got ${v})`);
      usage(2);
    }
    input.direction = v;
  } else if (a === "--search-text") input.searchText = true;
  else if (a === "--hops") input.hops = Number(next());
  else if (a === "--limit") input.limit = Number(next());
  else if (a === "--provenance") input.provenance = next();
  else if (a.startsWith("--")) {
    console.error(`unknown option ${a}`);
    usage(2);
  } else positional.push(a);
}
if (positional.length !== 1) usage(2);
input.query = positional[0];

if (!existsSync(GRAPH_MODULE) || !existsSync(DECL_MODULE)) {
  console.error(
    `corpus-search: the platform is not set up — ${existsSync(PLATFORM) ? GRAPH_MODULE : PLATFORM} is missing.\n` +
      "Run `bash scripts/setup-folio-assistant.sh` from the repository root, then retry.",
  );
  process.exit(3);
}

const { executeGraphTool } = (await import(GRAPH_MODULE)) as {
  executeGraphTool: (n: string, i: Record<string, unknown>, r: Array<{ name: string; dir: string }>) => string | undefined;
};
const { folioDir, directoriesForGraph } = (await import(DECL_MODULE)) as {
  folioDir: (root: string) => string;
  directoriesForGraph: (root: string, graph: string) => string[];
};

// The same resolution as the server's GRAPH_ROOTS (adapters/mcp-server/server.ts
// and paths.ts LIBRARY_DIRS): the declared folio, then EVERY declared library,
// each named so a hit says which root it came from.
let libraries: string[] = [];
try {
  libraries = directoriesForGraph(ROOT, "library");
} catch {
  // A declaration that cannot be read falls through to the convention below.
}
if (libraries.length === 0) libraries = [join(ROOT, "library")];
const roots = [
  { name: "folio", dir: folioDir(ROOT) },
  ...libraries.map((dir, i) => ({
    name: libraries.length === 1 ? "library" : `library:${dir.slice(ROOT.length + 1) || String(i)}`,
    dir,
  })),
];

const out = executeGraphTool("corpus_search", input, roots);
if (out === undefined) {
  console.error("corpus-search: the platform's graph module does not know `corpus_search` at this pin.");
  process.exit(4);
}
console.log(JSON.stringify(JSON.parse(out), null, 2));
