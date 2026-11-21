#!/usr/bin/env bun
/**
 * corpus_search from the command line: step 0 of the AGENTS.md corpus-grep
 * checklist, without the MCP server.
 *
 * Why (2026-11-20, bean qou-q261). The MCP route depends on the full platform
 * (scripts/setup-folio-assistant.sh, 1.7 GB). A fresh session has only the
 * light platform that the SessionStart hook installs. So step 0 was
 * unavailable in practice, and agents fell back to grep alone. That is
 * exactly the blind spot step 0 exists to cover. This CLI calls the same
 * function the MCP tool calls, `executeGraphTool("corpus_search", …)`, over
 * the same roots, `graphRootsResolved`. It needs only zod, which the light
 * platform installs.
 *
 * Usage:
 *   bun scripts/corpus-search.ts "<query>" [--direction in|out] [--search-text] [--hops N] [--limit N] [--provenance authored|ingested]
 *
 * Prints the tool's JSON. Read `why`, `seedsByProvenance` and `emptyRoots`
 * exactly as AGENTS.md step 0 describes.
 */
import { resolve } from "node:path";
import { graphRootsResolved } from "../folio-assistant/cat-harness-tools/src/tools/graph.ts";
import { executeGraphTool } from "../folio-assistant/cat-harness-tools/adapters/mcp-server/tools/graph.ts";

const argv = process.argv.slice(2);
const flag = (n: string) => {
  const i = argv.indexOf(n);
  return i >= 0 ? argv[i + 1] : undefined;
};
const valued = new Set(["--direction", "--hops", "--limit", "--provenance"]);
const query = argv.find((a, i) => !a.startsWith("--") && !valued.has(argv[i - 1] ?? ""));
if (!query) {
  console.error('usage: bun scripts/corpus-search.ts "<query>" [--direction in|out] [--search-text] [--hops N] [--limit N] [--provenance authored|ingested]');
  process.exit(2);
}
const input: Record<string, unknown> = { query };
if (flag("--direction")) input.direction = flag("--direction");
if (argv.includes("--search-text")) input.searchText = true;
if (flag("--hops")) input.hops = Number(flag("--hops"));
if (flag("--limit")) input.limit = Number(flag("--limit"));
if (flag("--provenance")) input.provenance = flag("--provenance");

const repoRoot = resolve(import.meta.dir, "..");
const { roots, note } = graphRootsResolved(repoRoot);
const text = executeGraphTool("corpus_search", input, roots);
if (text === undefined) {
  console.error("corpus-search: the platform did not recognise corpus_search");
  process.exit(1);
}
console.log(JSON.stringify({ rootsNote: note, ...JSON.parse(text) }, null, 2));
