#!/usr/bin/env bun
/**
 * Lean compile diagnostics auditor.
 *
 * Populates `docs/audits/lean-compile-diagnostics.json` by invoking
 * the lean-lsp MCP server's `lean_diagnostic_messages` tool on every
 * `.lean` file that has a content-block sibling (`.ts`).
 *
 * Usage (agent-driven):
 *   Agents call `mcp__lean-lsp__lean_diagnostic_messages` per file
 *   and feed results to this script's `--ingest` mode, or run the
 *   script standalone to walk all lean files and shell out to
 *   `lean --run` for diagnostics.
 *
 * Usage (CLI, ingestion mode):
 *   bun run pipeline/lean-compile-audit.ts --ingest <diagnostics.jsonl>
 *
 *   Each line of the JSONL input:
 *     { "file": "<repo-relative-path>", "diagnostics": [...] }
 *
 * Usage (CLI, standalone scan — requires lean toolchain):
 *   bun run pipeline/lean-compile-audit.ts [content-root]
 *
 * Output:
 *   docs/audits/lean-compile-diagnostics.json
 *
 * @module content/pipeline/lean-compile-audit
 */

import { existsSync, readFileSync, writeFileSync, readdirSync, statSync } from "fs";
import { resolve, dirname, join, relative, basename, extname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const REPO_ROOT = resolve(dirname(__filename), "..", "..");
const OUTPUT_PATH = join(REPO_ROOT, "docs/audits/lean-compile-diagnostics.json");

interface DiagnosticEntry {
  line: number;
  severity: string;
  message: string;
}

interface FileEntry {
  errors: DiagnosticEntry[];
  checked_at: string;
}

interface DiagnosticsReport {
  $schema: "lean-compile-diagnostics/v1";
  generated_at: string;
  files: Record<string, FileEntry>;
}

function findLeanFilesWithSiblingTs(dir: string): string[] {
  const results: string[] = [];
  function walk(d: string) {
    let entries: string[];
    try {
      entries = readdirSync(d);
    } catch {
      return;
    }
    for (const e of entries) {
      const full = join(d, e);
      let st;
      try {
        st = statSync(full);
      } catch {
        continue;
      }
      if (st.isDirectory()) {
        if (e === "node_modules" || e === ".lake" || e === "build" || e === "lake-packages") continue;
        walk(full);
      } else if (extname(e) === ".lean") {
        const tsPath = full.replace(/\.lean$/, ".ts");
        if (existsSync(tsPath)) {
          results.push(relative(REPO_ROOT, full));
        }
      }
    }
  }
  walk(dir);
  return results.sort();
}

function ingestJsonl(jsonlPath: string): void {
  const existing: DiagnosticsReport = existsSync(OUTPUT_PATH)
    ? JSON.parse(readFileSync(OUTPUT_PATH, "utf-8"))
    : { $schema: "lean-compile-diagnostics/v1", generated_at: "", files: {} };

  const lines = readFileSync(jsonlPath, "utf-8").trim().split("\n");
  for (const line of lines) {
    if (!line.trim()) continue;
    const { file, diagnostics } = JSON.parse(line) as {
      file: string;
      diagnostics: Array<{ line?: number; severity?: string; message?: string }>;
    };
    const errors: DiagnosticEntry[] = (diagnostics || [])
      .filter((d) => d.severity === "error")
      .map((d) => ({
        line: d.line ?? 0,
        severity: d.severity ?? "error",
        message: (d.message ?? "").slice(0, 500),
      }));
    existing.files[file] = {
      errors,
      checked_at: new Date().toISOString(),
    };
  }
  existing.generated_at = new Date().toISOString();
  writeFileSync(OUTPUT_PATH, JSON.stringify(existing, null, 2) + "\n");
  console.log(`Updated ${OUTPUT_PATH} — ${Object.keys(existing.files).length} files tracked`);
}

function ingestSingleFile(filePath: string, diagnostics: DiagnosticEntry[]): void {
  const existing: DiagnosticsReport = existsSync(OUTPUT_PATH)
    ? JSON.parse(readFileSync(OUTPUT_PATH, "utf-8"))
    : { $schema: "lean-compile-diagnostics/v1", generated_at: "", files: {} };

  existing.files[filePath] = {
    errors: diagnostics.filter((d) => d.severity === "error"),
    checked_at: new Date().toISOString(),
  };
  existing.generated_at = new Date().toISOString();
  writeFileSync(OUTPUT_PATH, JSON.stringify(existing, null, 2) + "\n");
}

// CLI entry
const args = process.argv.slice(2);

if (args[0] === "--ingest" && args[1]) {
  ingestJsonl(args[1]);
} else if (args[0] === "--list") {
  const contentRoot = args[1] || join(REPO_ROOT, "content");
  const files = findLeanFilesWithSiblingTs(contentRoot);
  for (const f of files) console.log(f);
  console.log(`\n${files.length} .lean files with .ts siblings`);
} else {
  console.log(`Usage:
  bun run pipeline/lean-compile-audit.ts --list [content-root]
    List all .lean files with .ts siblings

  bun run pipeline/lean-compile-audit.ts --ingest <diagnostics.jsonl>
    Ingest MCP lean_diagnostic_messages output (JSONL)

Agent workflow:
  1. Run --list to get .lean file paths
  2. Call mcp__lean-lsp__lean_diagnostic_messages(file_path) per file
  3. Write results as JSONL and --ingest, or use the qa-sweep
     proof-lean-compiles criterion which reads the cache at
     docs/audits/lean-compile-diagnostics.json`);
}

export { findLeanFilesWithSiblingTs, ingestSingleFile, DiagnosticEntry, DiagnosticsReport };
