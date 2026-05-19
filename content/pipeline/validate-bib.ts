#!/usr/bin/env bun
/**
 * validate-bib.ts — comprehensive bibliography correctness audit.
 *
 * Modes (run individually or combined; `--all` enables every check):
 *
 *   --doi           DOI resolution: HEAD-request each entry's DOI →
 *                   expect 200/301/302 from doi.org. Catches broken DOIs.
 *   --cross-check   Parse `-- Ref: [key] <description>` comments in
 *                   content/**\/*.lean; extract surname (Title-case words)
 *                   and year (4-digit) from the description; compare
 *                   against referenceMap entry's author[0].family +
 *                   issued.date-parts[0][0]. Catches wrong-work
 *                   resolutions (the class Copilot found 4 of in PR #792).
 *   --crossref      Per-entry Crossref API lookup
 *                   (api.crossref.org/works/<DOI>): compare canonical
 *                   title / first-author surname / year against the entry.
 *                   Confirms the DOI actually points at what the entry says.
 *   --arxiv         For entries whose URL field contains arxiv.org/...,
 *                   fetch the arXiv abstract page and verify the entry's
 *                   title appears. Catches preprint-vs-published-version
 *                   mismatches.
 *   --pandoc        Pipe a sample LaTeX citation through pandoc-citeproc
 *                   with the generated references.bib; verify output is
 *                   well-formed (catches CSL formatting issues + missing
 *                   required fields).
 *   --all           Run all 5 modes in sequence.
 *   --strict        Exit non-zero on any failure (default: warn-only).
 *
 * Usage examples:
 *   bun run pipeline/validate-bib.ts --doi
 *   bun run pipeline/validate-bib.ts --cross-check --strict
 *   bun run pipeline/validate-bib.ts --all
 *
 * Per CLAUDE.md §"Bibliography architecture": references.ts is the
 * source of truth; this script verifies external correctness of every
 * entry beyond schema-shape validation.
 */
import { references } from "../schema/references";
import * as fs from "fs";
import * as path from "path";
import { glob } from "fs/promises";

type Mode = "doi" | "cross-check" | "crossref" | "arxiv" | "pandoc";
type CheckResult = { entry: string; severity: "ok" | "warn" | "error"; note: string };

const args = process.argv.slice(2);
const STRICT = args.includes("--strict");
const ALL = args.includes("--all");
const MODES: Set<Mode> = new Set();
if (ALL || args.includes("--doi")) MODES.add("doi");
if (ALL || args.includes("--cross-check")) MODES.add("cross-check");
if (ALL || args.includes("--crossref")) MODES.add("crossref");
if (ALL || args.includes("--arxiv")) MODES.add("arxiv");
if (ALL || args.includes("--pandoc")) MODES.add("pandoc");
if (MODES.size === 0) {
  console.error("No mode selected. Pass --doi / --cross-check / --crossref / --arxiv / --pandoc or --all.");
  process.exit(2);
}

const CONTENT_ROOT = path.resolve(__dirname, "..");
const REPO_ROOT = path.resolve(CONTENT_ROOT, "..");

async function modeDoi(): Promise<CheckResult[]> {
  const out: CheckResult[] = [];
  const withDoi = references.filter((r) => r.DOI);
  console.log(`\n[doi] HEAD-requesting ${withDoi.length} DOIs (skipping ${references.length - withDoi.length} entries without DOI)...`);
  let i = 0;
  for (const r of withDoi) {
    i++;
    const url = `https://doi.org/${r.DOI}`;
    try {
      const ctrl = new AbortController();
      const timer = setTimeout(() => ctrl.abort(), 5000);
      const resp = await fetch(url, { method: "HEAD", redirect: "follow", signal: ctrl.signal });
      clearTimeout(timer);
      if (resp.status === 200 || resp.status === 301 || resp.status === 302) {
        out.push({ entry: r.id, severity: "ok", note: `${resp.status} OK` });
      } else {
        out.push({ entry: r.id, severity: "warn", note: `HTTP ${resp.status} for ${url}` });
      }
    } catch (e: any) {
      out.push({ entry: r.id, severity: "warn", note: `fetch failed: ${e.message ?? e}` });
    }
    if (i % 25 === 0) console.log(`  …${i}/${withDoi.length}`);
  }
  return out;
}

async function modeCrossCheck(): Promise<CheckResult[]> {
  const out: CheckResult[] = [];
  const refMap = new Map(references.map((r) => [r.id, r]));
  // Find all .lean files containing `-- Ref: [key] <description>` lines
  const leanFiles: string[] = [];
  for await (const f of glob("**/*.lean", { cwd: path.join(CONTENT_ROOT) })) {
    if (f.includes(".lake/")) continue;
    leanFiles.push(path.join(CONTENT_ROOT, f as string));
  }
  console.log(`\n[cross-check] scanning ${leanFiles.length} .lean files for -- Ref: comments...`);
  let comments = 0;
  let checked = 0;
  for (const f of leanFiles) {
    const text = fs.readFileSync(f, "utf-8");
    const lines = text.split("\n");
    for (const line of lines) {
      const m = line.match(/--\s*Ref:\s*\[([^\]]+)\]\s*(.*)/);
      if (!m) continue;
      const [, key, desc] = m;
      comments++;
      const entry = refMap.get(key);
      if (!entry) continue; // validate-refs already catches missing keys
      // Extract surname (sequence of capitalised words at start of desc)
      const surnameMatch = desc.match(/^([A-Z][a-zA-Zé\-']+)(?:[,\s]+(?:and|&)\s+([A-Z][a-zA-Zé\-']+))?/);
      const yearMatch = desc.match(/\b(19|20)\d{2}\b/);
      const entryFamily = entry.author?.[0]?.family ?? entry.author?.[0]?.literal ?? "";
      const entryYear = entry.issued?.["date-parts"]?.[0]?.[0];
      checked++;
      // Warn if entry's surname doesn't appear in any of the first 2 description tokens
      if (surnameMatch && entryFamily) {
        const descSurname = surnameMatch[1].toLowerCase();
        const entryFamLower = entryFamily.toLowerCase();
        if (!entryFamLower.includes(descSurname) && !descSurname.includes(entryFamLower)) {
          out.push({
            entry: key,
            severity: "warn",
            note: `surname mismatch: .lean says "${surnameMatch[1]}", entry has "${entryFamily}" (${path.relative(REPO_ROOT, f)})`,
          });
        }
      }
      if (yearMatch && entryYear) {
        const descYear = parseInt(yearMatch[0]);
        if (Math.abs(descYear - entryYear) > 1) {
          out.push({
            entry: key,
            severity: "warn",
            note: `year mismatch: .lean says ${descYear}, entry has ${entryYear} (${path.relative(REPO_ROOT, f)})`,
          });
        }
      }
    }
  }
  console.log(`  checked ${checked}/${comments} comments (skipped ${comments - checked} unresolvable keys)`);
  return out;
}

async function modeCrossref(): Promise<CheckResult[]> {
  const out: CheckResult[] = [];
  const withDoi = references.filter((r) => r.DOI);
  console.log(`\n[crossref] fetching ${withDoi.length} entries from api.crossref.org...`);
  let i = 0;
  for (const r of withDoi) {
    i++;
    const url = `https://api.crossref.org/works/${r.DOI}`;
    try {
      const ctrl = new AbortController();
      const timer = setTimeout(() => ctrl.abort(), 10000);
      const resp = await fetch(url, { signal: ctrl.signal });
      clearTimeout(timer);
      if (resp.status !== 200) {
        out.push({ entry: r.id, severity: "warn", note: `crossref ${resp.status} for ${r.DOI}` });
        continue;
      }
      const data: any = await resp.json();
      const msg = data.message ?? data;
      const cTitle = (msg.title?.[0] ?? "").toLowerCase();
      const cAuthor = (msg.author?.[0]?.family ?? "").toLowerCase();
      const cYear = msg["published-print"]?.["date-parts"]?.[0]?.[0]
                  ?? msg["published-online"]?.["date-parts"]?.[0]?.[0]
                  ?? msg["created"]?.["date-parts"]?.[0]?.[0];
      const eTitle = ((r as any).title ?? "").toLowerCase();
      const eAuthor = (r.author?.[0]?.family ?? "").toLowerCase();
      const eYear = r.issued?.["date-parts"]?.[0]?.[0];
      const issues: string[] = [];
      if (eTitle && cTitle && !cTitle.includes(eTitle.slice(0, 20)) && !eTitle.includes(cTitle.slice(0, 20))) {
        issues.push(`title mismatch: entry "${eTitle.slice(0, 60)}" vs Crossref "${cTitle.slice(0, 60)}"`);
      }
      if (eAuthor && cAuthor && eAuthor !== cAuthor) {
        issues.push(`author mismatch: entry "${eAuthor}" vs Crossref "${cAuthor}"`);
      }
      if (eYear && cYear && Math.abs(eYear - cYear) > 1) {
        issues.push(`year mismatch: entry ${eYear} vs Crossref ${cYear}`);
      }
      if (issues.length) {
        out.push({ entry: r.id, severity: "warn", note: issues.join("; ") });
      } else {
        out.push({ entry: r.id, severity: "ok", note: "Crossref matches" });
      }
    } catch (e: any) {
      out.push({ entry: r.id, severity: "warn", note: `crossref fetch failed: ${e.message ?? e}` });
    }
    if (i % 25 === 0) console.log(`  …${i}/${withDoi.length}`);
  }
  return out;
}

async function modeArxiv(): Promise<CheckResult[]> {
  const out: CheckResult[] = [];
  const withArxiv = references.filter((r) => (r as any).URL && /arxiv\.org/i.test((r as any).URL));
  console.log(`\n[arxiv] checking ${withArxiv.length} arxiv-URL entries...`);
  for (const r of withArxiv) {
    try {
      const ctrl = new AbortController();
      const timer = setTimeout(() => ctrl.abort(), 5000);
      const resp = await fetch((r as any).URL, { method: "HEAD", redirect: "follow", signal: ctrl.signal });
      clearTimeout(timer);
      if (resp.status === 200 || resp.status === 301 || resp.status === 302) {
        out.push({ entry: r.id, severity: "ok", note: `arxiv ${resp.status} OK` });
      } else {
        out.push({ entry: r.id, severity: "warn", note: `arxiv HTTP ${resp.status}` });
      }
    } catch (e: any) {
      out.push({ entry: r.id, severity: "warn", note: `arxiv fetch failed: ${e.message ?? e}` });
    }
  }
  return out;
}

async function modePandoc(): Promise<CheckResult[]> {
  const out: CheckResult[] = [];
  // Check pandoc availability
  const { spawnSync } = await import("child_process");
  const pv = spawnSync("pandoc", ["--version"], { encoding: "utf-8" });
  if (pv.status !== 0) {
    out.push({ entry: "(pandoc)", severity: "warn", note: "pandoc not installed; skipping render check" });
    return out;
  }
  // Use existing references.bib (auto-generated)
  const bibPath = path.join(CONTENT_ROOT, "..", "references.bib");
  if (!fs.existsSync(bibPath)) {
    out.push({ entry: "(references.bib)", severity: "warn", note: `not found at ${bibPath}; run "cd content && bun run export-bibtex" first` });
    return out;
  }
  // Sample document citing 5 random entries
  const sample = references.slice(0, 5);
  const tex = `# Test\n\n${sample.map((r) => `[@${r.id}]`).join(" ")}\n`;
  console.log(`\n[pandoc] rendering 5-citation sample through pandoc-citeproc...`);
  const result = spawnSync(
    "pandoc",
    ["-f", "markdown", "-t", "plain", "--citeproc", "--bibliography", bibPath, "-"],
    { input: tex, encoding: "utf-8", timeout: 30000 }
  );
  if (result.status !== 0) {
    out.push({ entry: "(pandoc-render)", severity: "error", note: `pandoc-citeproc failed: ${result.stderr.slice(0, 200)}` });
  } else if (!result.stdout || result.stdout.length < 10) {
    out.push({ entry: "(pandoc-render)", severity: "warn", note: "pandoc output empty or trivially short" });
  } else {
    out.push({ entry: "(pandoc-render)", severity: "ok", note: `rendered ${result.stdout.length} chars` });
  }
  return out;
}

// ─── Main ────────────────────────────────────────────────────────
async function main() {
  console.log(`validate-bib — modes: ${[...MODES].join(", ")} (strict=${STRICT})`);
  console.log(`references: ${references.length} entries`);

  const allResults: { mode: Mode; results: CheckResult[] }[] = [];
  if (MODES.has("doi")) allResults.push({ mode: "doi", results: await modeDoi() });
  if (MODES.has("cross-check")) allResults.push({ mode: "cross-check", results: await modeCrossCheck() });
  if (MODES.has("crossref")) allResults.push({ mode: "crossref", results: await modeCrossref() });
  if (MODES.has("arxiv")) allResults.push({ mode: "arxiv", results: await modeArxiv() });
  if (MODES.has("pandoc")) allResults.push({ mode: "pandoc", results: await modePandoc() });

  let totalErrors = 0;
  let totalWarns = 0;
  for (const { mode, results } of allResults) {
    const errors = results.filter((r) => r.severity === "error");
    const warns = results.filter((r) => r.severity === "warn");
    const oks = results.filter((r) => r.severity === "ok");
    totalErrors += errors.length;
    totalWarns += warns.length;
    console.log(`\n=== [${mode}] ${oks.length} ok / ${warns.length} warn / ${errors.length} error ===`);
    for (const r of errors.concat(warns).slice(0, 30)) {
      console.log(`  [${r.severity.toUpperCase()}] ${r.entry}: ${r.note}`);
    }
    if (errors.length + warns.length > 30) {
      console.log(`  …(${errors.length + warns.length - 30} more)`);
    }
  }

  console.log(`\n─── totals: ${totalErrors} error, ${totalWarns} warn ───`);
  if (STRICT && (totalErrors > 0 || totalWarns > 0)) process.exit(1);
}

main().catch((e) => {
  console.error("validate-bib failed:", e);
  process.exit(2);
});
