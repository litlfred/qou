#!/usr/bin/env bun
/**
 * Q-usage audit — walk every content block under
 * `content/quantum-observable-universe/`, run the seven q-usage
 * criteria, and emit (a) per-block `<block>.qa.json` entries, and
 * (b) a global witness summary.
 *
 * Usage:
 *
 *   bun run content/pipeline/q-usage-audit.ts                 # default
 *   bun run content/pipeline/q-usage-audit.ts --no-write      # report only
 *   bun run content/pipeline/q-usage-audit.ts --strict        # exit 1 on fail
 *   bun run content/pipeline/q-usage-audit.ts --chapter <dir> # one chapter
 *   bun run content/pipeline/q-usage-audit.ts --json          # JSON report
 *
 * Output:
 *   - per-block: writes/updates `<block>.qa.json` with one entry per
 *     q-usage criterion (the regime vector lives in the `notes` field
 *     of `q-usage-regime-detected`).
 *   - global witness: `docs/audits/<YYYY-MM-DD>-q-usage-audit.witness.json`
 *     summarising fails/warns by chapter + criterion.
 *
 * @module content/pipeline/q-usage-audit
 */

import { existsSync, readdirSync, readFileSync, statSync, writeFileSync, mkdirSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join, resolve, basename } from "node:path";
import { fileURLToPath } from "node:url";
import {
  Q_USAGE_AUTOMATED_CHECKERS,
  Q_USAGE_CRITERION_IDS,
  CHAPTER_EXPECTED_REGIMES,
  type QRegime,
  type QUsageResult,
} from "./qa-checkers-q-usage.ts";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(SCRIPT_DIR, "..", "..");
const PAPER_ROOT = join(REPO_ROOT, "content", "quantum-observable-universe");

// ── CLI args ────────────────────────────────────────────────────

const args = process.argv.slice(2);
const noWrite = args.includes("--no-write");
const strict = args.includes("--strict");
const jsonReport = args.includes("--json");
const chapterFilterIdx = args.indexOf("--chapter");
const chapterFilter = chapterFilterIdx >= 0 ? args[chapterFilterIdx + 1] : undefined;

// ── Walk block files ────────────────────────────────────────────

interface BlockTriple {
  label: string;
  kind: string;
  chapter: string;
  ts: string;
  md?: string;
  lean?: string;
}

const PROVABLE_KINDS = new Set([
  "definition",
  "theorem",
  "lemma",
  "proposition",
  "corollary",
  "conjecture",
  "remark",
  "example",
  "simulator",
  "prose",
  "diagram",
  "equation",
]);

function walkBlocks(): BlockTriple[] {
  const out: BlockTriple[] = [];
  const chapters = readdirSync(PAPER_ROOT, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name);
  for (const chapter of chapters) {
    if (chapterFilter && chapter !== chapterFilter) continue;
    const chDir = join(PAPER_ROOT, chapter);
    let files: string[];
    try {
      files = readdirSync(chDir);
    } catch {
      continue;
    }
    for (const f of files) {
      if (!f.endsWith(".ts")) continue;
      if (f === `${chapter}.ts`) continue; // chapter manifest, not a block
      const tsPath = join(chDir, f);
      const root = f.replace(/\.ts$/, "");
      const mdPath = join(chDir, `${root}.md`);
      const leanPath = join(chDir, `${root}.lean`);
      const ts = readFileSync(tsPath, "utf-8");
      const kindMatch = ts.match(
        /export\s+default\s+(definition|theorem|lemma|proposition|corollary|conjecture|remark|example|simulator|prose|diagram|equation)\s*\(/,
      );
      if (!kindMatch) continue;
      const kind = kindMatch[1];
      const labelMatch = ts.match(/label:\s*["']([^"']+)["']/);
      const label = labelMatch ? labelMatch[1] : root;
      out.push({
        label,
        kind,
        chapter,
        ts: tsPath,
        md: existsSync(mdPath) ? mdPath : undefined,
        lean: existsSync(leanPath) ? leanPath : undefined,
      });
    }
  }
  return out;
}

function hashFile(path: string): string {
  if (!existsSync(path)) return "";
  return createHash("sha256")
    .update(readFileSync(path))
    .digest("hex")
    .slice(0, 12);
}

// ── Sidecar I/O ─────────────────────────────────────────────────

interface QaEntry {
  field_hash: { md?: string; ts?: string; lean?: string };
  result: "pass" | "fail" | "warn" | "n/a";
  severity?: "critical" | "major" | "minor";
  evidence?: string;
  reviewer: {
    kind: "script";
    id: string;
    script_hash?: string;
  };
  reviewed_at: string;
  reviewed_sha?: string;
  notes?: string;
}

interface QaSidecar {
  $schema: "block-qa/v1";
  label: string;
  kind: string;
  paths: { ts: string; md?: string; lean?: string };
  source_hashes: { md?: string; ts?: string; lean?: string };
  criteria: Record<string, QaEntry[]>;
  updated_at: string;
}

const CRITERION_SEVERITY: Record<string, "critical" | "major" | "minor"> = {
  "q-usage-regime-detected": "minor",
  "q-usage-fixed-q0-leak": "major",
  "q-usage-archimedean-in-categorical-chapter": "major",
  "q-usage-positivity-implicit": "minor",
  "q-usage-modulus-vs-real-mismatch": "minor",
  "q-usage-root-of-unity-undeclared": "minor",
  "q-usage-narrative-chapter-mismatch": "minor",
};

const SCRIPT_PATH = "content/pipeline/qa-checkers-q-usage.ts";
const SCRIPT_HASH = hashFile(join(REPO_ROOT, SCRIPT_PATH));
const NOW_ISO = new Date().toISOString();
const REVIEWER_ID = "q-usage-audit";

function updateSidecar(b: BlockTriple, results: Map<string, QUsageResult>): void {
  const sidecarPath = b.ts.replace(/\.ts$/, ".qa.json");
  let sidecar: QaSidecar;
  if (existsSync(sidecarPath)) {
    try {
      sidecar = JSON.parse(readFileSync(sidecarPath, "utf-8")) as QaSidecar;
    } catch {
      sidecar = makeFreshSidecar(b);
    }
  } else {
    sidecar = makeFreshSidecar(b);
  }

  // Refresh source hashes + paths
  sidecar.source_hashes = {
    ts: hashFile(b.ts),
    md: b.md ? hashFile(b.md) : undefined,
    lean: b.lean ? hashFile(b.lean) : undefined,
  };
  sidecar.paths = {
    ts: b.ts.replace(REPO_ROOT + "/", ""),
    md: b.md ? b.md.replace(REPO_ROOT + "/", "") : undefined,
    lean: b.lean ? b.lean.replace(REPO_ROOT + "/", "") : undefined,
  };
  sidecar.label = b.label;
  sidecar.kind = b.kind;
  sidecar.updated_at = NOW_ISO;

  for (const [criterionId, r] of results.entries()) {
    const entry: QaEntry = {
      field_hash: { ...sidecar.source_hashes },
      result: r.result,
      reviewer: {
        kind: "script",
        id: REVIEWER_ID,
        script_hash: SCRIPT_HASH,
      },
      reviewed_at: NOW_ISO,
    };
    if (r.result === "fail" || r.result === "warn") {
      entry.severity = CRITERION_SEVERITY[criterionId];
      if (r.hits.length > 0) {
        entry.evidence = r.hits
          .slice(0, 4)
          .map((h) => `${h.file}:${h.line} — ${h.text}`)
          .join(" | ");
      }
    }
    if (criterionId === "q-usage-regime-detected") {
      const regimes = r.regimes ?? [];
      entry.notes = JSON.stringify({
        regimes,
        chapter: r.chapter,
        expected: r.chapter && CHAPTER_EXPECTED_REGIMES[r.chapter]
          ? [...CHAPTER_EXPECTED_REGIMES[r.chapter]].sort()
          : null,
      });
    }
    sidecar.criteria[criterionId] = [
      ...(sidecar.criteria[criterionId] ?? []).filter(
        (e) => e.reviewer.id !== REVIEWER_ID,
      ),
      entry,
    ];
  }

  if (!noWrite) {
    writeFileSync(sidecarPath, JSON.stringify(sidecar, null, 2) + "\n", "utf-8");
  }
}

function makeFreshSidecar(b: BlockTriple): QaSidecar {
  return {
    $schema: "block-qa/v1",
    label: b.label,
    kind: b.kind,
    paths: {
      ts: b.ts.replace(REPO_ROOT + "/", ""),
      md: b.md ? b.md.replace(REPO_ROOT + "/", "") : undefined,
      lean: b.lean ? b.lean.replace(REPO_ROOT + "/", "") : undefined,
    },
    source_hashes: {
      ts: hashFile(b.ts),
      md: b.md ? hashFile(b.md) : undefined,
      lean: b.lean ? hashFile(b.lean) : undefined,
    },
    criteria: {},
    updated_at: NOW_ISO,
  };
}

// ── Main ────────────────────────────────────────────────────────

interface ChapterStat {
  chapter: string;
  n_blocks: number;
  by_criterion: Record<string, { pass: number; fail: number; warn: number; "n/a": number }>;
  regime_dist: Record<string, number>;
}

interface BlockFinding {
  label: string;
  kind: string;
  chapter: string;
  criterion: string;
  result: "fail" | "warn";
  severity: string;
  evidence: string;
}

function main(): void {
  const blocks = walkBlocks();
  const stats: Map<string, ChapterStat> = new Map();
  const findings: BlockFinding[] = [];
  let touchedSidecars = 0;

  for (const b of blocks) {
    const stat = stats.get(b.chapter) ?? {
      chapter: b.chapter,
      n_blocks: 0,
      by_criterion: Object.fromEntries(
        Q_USAGE_CRITERION_IDS.map((id) => [id, { pass: 0, fail: 0, warn: 0, "n/a": 0 }]),
      ),
      regime_dist: {},
    };
    stat.n_blocks++;
    const results = new Map<string, QUsageResult>();
    for (const [id, fn] of Object.entries(Q_USAGE_AUTOMATED_CHECKERS)) {
      const r = fn({ md: b.md, ts: b.ts, lean: b.lean });
      results.set(id, r);
      stat.by_criterion[id][r.result]++;
      if (r.result === "fail" || r.result === "warn") {
        findings.push({
          label: b.label,
          kind: b.kind,
          chapter: b.chapter,
          criterion: id,
          result: r.result,
          severity: CRITERION_SEVERITY[id],
          evidence: r.hits
            .slice(0, 3)
            .map((h) => `${h.file.replace(REPO_ROOT + "/", "")}:${h.line} — ${h.text}`)
            .join(" | "),
        });
      }
      if (id === "q-usage-regime-detected" && r.regimes) {
        for (const rg of r.regimes) {
          stat.regime_dist[rg] = (stat.regime_dist[rg] ?? 0) + 1;
        }
      }
    }
    stats.set(b.chapter, stat);
    updateSidecar(b, results);
    if (!noWrite) touchedSidecars++;
  }

  // Global witness
  const witnessPath = join(
    REPO_ROOT,
    "docs",
    "audits",
    `${NOW_ISO.slice(0, 10)}-q-usage-audit.witness.json`,
  );
  const witness = {
    $schema: "q-usage-audit/v1",
    description: "Per-block q-usage regime audit + chapter-mismatch sweep",
    audited_at: NOW_ISO,
    script: SCRIPT_PATH,
    script_hash: SCRIPT_HASH,
    n_blocks: blocks.length,
    n_chapters: stats.size,
    n_fails: findings.filter((f) => f.result === "fail").length,
    n_warns: findings.filter((f) => f.result === "warn").length,
    by_chapter: Object.fromEntries(
      [...stats.entries()].sort().map(([k, v]) => [k, v]),
    ),
    findings: findings.sort((a, b) => {
      const sev: Record<string, number> = { critical: 0, major: 1, minor: 2 };
      const da = sev[a.severity] ?? 9;
      const db = sev[b.severity] ?? 9;
      if (da !== db) return da - db;
      return (a.chapter + a.label).localeCompare(b.chapter + b.label);
    }),
  };
  if (!noWrite) {
    mkdirSync(dirname(witnessPath), { recursive: true });
    writeFileSync(witnessPath, JSON.stringify(witness, null, 2) + "\n", "utf-8");
  }

  if (jsonReport) {
    process.stdout.write(JSON.stringify(witness, null, 2) + "\n");
  } else {
    console.error(`q-usage-audit — ${blocks.length} blocks across ${stats.size} chapters`);
    console.error(
      `  fails=${witness.n_fails}  warns=${witness.n_warns}  sidecars-touched=${touchedSidecars}`,
    );
    console.error("");
    console.error("Chapter regime distribution (top tags only):");
    for (const stat of [...stats.values()].sort((a, b) => a.chapter.localeCompare(b.chapter))) {
      const top = Object.entries(stat.regime_dist)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 6)
        .map(([k, v]) => `${k}=${v}`)
        .join(" ");
      console.error(`  ${stat.chapter.padEnd(40)} blocks=${stat.n_blocks.toString().padStart(3)}  ${top}`);
    }
    console.error("");
    console.error("Findings (severity-sorted):");
    for (const f of witness.findings.slice(0, 40)) {
      console.error(
        `  [${f.severity.padEnd(8)}] ${f.result} ${f.criterion}  ${f.chapter}/${f.label}`,
      );
      if (f.evidence) console.error(`            ${f.evidence.slice(0, 200)}`);
    }
    if (witness.findings.length > 40) {
      console.error(`  …and ${witness.findings.length - 40} more (see witness JSON)`);
    }
    if (!noWrite) {
      console.error("");
      console.error(`Witness written to ${witnessPath.replace(REPO_ROOT + "/", "")}`);
    }
  }

  if (strict && witness.n_fails > 0) process.exit(1);
}

main();
