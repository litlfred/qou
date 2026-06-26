#!/usr/bin/env bun
/**
 * One-voice audit parameter: **NO self-assessment banners.**
 *
 * The paper speaks with one scholarly voice (AGENTS.md "User
 * accessibility"; `local/one-voice-audit`). A *self-assessment banner*
 * is a bold-labelled paragraph in which the text grades its own
 * contribution — how novel it is, how plausible a formalization gap is
 * to close, how significant the result is. These are author-tracking
 * notes, not scholarly content: per AGENTS.md §4d they belong in the
 * block's `authorNotes` metadata (render-skipped by default), never in
 * the `.md` prose.
 *
 * This scanner flags such banners so they can be migrated to
 * `authorNotes` (the canonical fix) or removed. It is the candidate-
 * finder for the `local/one-voice-audit` Category L criterion
 * `voice-no-self-assessment-banners`.
 *
 * Two confidence tiers:
 *  - DEFAULT — bold labels that are essentially always self-assessment
 *    (`Novelty`, `Plausibility`). A match here is a violation and
 *    drives the non-zero exit (CI gate).
 *  - STRICT (`--strict`) — bold labels that are *often* self-assessment
 *    but sometimes legitimate scholarly "what this means" notes
 *    (`Significance`, `Contribution`, `Impact`, `Importance`,
 *    `Achievement`). Reported for human judgement; only counts toward
 *    the exit code under `--strict`.
 *
 * Self-contained (node:fs only). The canonical QA pipeline lives in the
 * external `folio-assistant` repo; this scanner carries no folio import
 * so it runs and commits standalone, matching
 * `content/pipeline/lean-vacuity-axiom-audit.ts`.
 *
 *   bun run content/pipeline/no-self-assessment-banners.ts \
 *     [root ...]            # default: content/
 *     [--strict]            # also flag Significance/Contribution/...
 *     [--json <path>]       # write findings as JSON
 *     [--quiet]             # suppress per-finding lines
 *
 * Exit 1 if any DEFAULT (or, under --strict, STRICT) banner is found.
 *
 * @module content/pipeline/no-self-assessment-banners
 */
import { readdirSync, readFileSync, statSync, writeFileSync } from "node:fs";
import { join, relative, resolve } from "node:path";

const CRITERION = "voice-no-self-assessment-banners";

// Patterns are tested against the *label text* between `**…**` at the
// start of a paragraph line (case-insensitive, word-bounded).
const DEFAULT_LABELS = [/\bnovelty\b/i, /\bplausibility\b/i];
const STRICT_LABELS = [
  /\bsignificance\b/i,
  /\bcontribution\b/i,
  /\bimpact\b/i,
  /\bimportance\b/i,
  /\bachievement\b/i,
];

// A paragraph-leading bold label: `**Label.**` / `**Label:**` / `**Label**`.
const BOLD_LABEL = /^\s*\*\*([^*]+?)\s*[:.]?\*\*/;

interface Finding {
  criterion: string;
  file: string;
  line: number;
  tier: "default" | "strict";
  label: string;
  snippet: string;
}

function mdFiles(root: string): string[] {
  const out: string[] = [];
  const walk = (d: string) => {
    for (const e of readdirSync(d, { withFileTypes: true })) {
      const p = join(d, e.name);
      if (e.isDirectory()) {
        if (e.name === "node_modules" || e.name === ".git") continue;
        walk(p);
      } else if (e.name.endsWith(".md")) {
        out.push(p);
      }
    }
  };
  if (statSync(root).isDirectory()) walk(root);
  else if (root.endsWith(".md")) out.push(root);
  return out;
}

function scan(file: string, strict: boolean): Finding[] {
  const found: Finding[] = [];
  const lines = readFileSync(file, "utf8").split("\n");
  lines.forEach((line, i) => {
    const m = BOLD_LABEL.exec(line);
    if (!m) return;
    const label = m[1].trim();
    if (DEFAULT_LABELS.some((rx) => rx.test(label))) {
      found.push(mk(file, i, "default", label, line));
    } else if (strict && STRICT_LABELS.some((rx) => rx.test(label))) {
      found.push(mk(file, i, "strict", label, line));
    }
  });
  return found;
}

function mk(
  file: string,
  i: number,
  tier: "default" | "strict",
  label: string,
  line: string,
): Finding {
  return {
    criterion: CRITERION,
    file,
    line: i + 1,
    tier,
    label,
    snippet: line.trim().slice(0, 100),
  };
}

function main() {
  const argv = process.argv.slice(2);
  const strict = argv.includes("--strict");
  const quiet = argv.includes("--quiet");
  const jsonIdx = argv.indexOf("--json");
  const jsonPath = jsonIdx >= 0 ? argv[jsonIdx + 1] : null;
  const roots = argv.filter(
    (a, k) => !a.startsWith("--") && !(jsonIdx >= 0 && k === jsonIdx + 1),
  );
  if (roots.length === 0) roots.push("content");

  const findings: Finding[] = [];
  for (const root of roots) {
    for (const f of mdFiles(resolve(root))) findings.push(...scan(f, strict));
  }

  const def = findings.filter((f) => f.tier === "default");
  const str = findings.filter((f) => f.tier === "strict");

  if (!quiet) {
    for (const f of findings) {
      const rel = relative(process.cwd(), f.file);
      console.log(`[${f.tier}] ${rel}:${f.line}  «${f.label}»  ${f.snippet}`);
    }
  }
  console.log(
    `\n${CRITERION}: ${def.length} default + ${str.length} strict finding(s)` +
      (strict ? " (strict mode)" : " (run --strict for Significance/etc.)"),
  );

  if (jsonPath) {
    writeFileSync(jsonPath, JSON.stringify({ criterion: CRITERION, findings }, null, 2));
    console.log(`wrote ${findings.length} finding(s) -> ${jsonPath}`);
  }

  const failing = strict ? def.length + str.length : def.length;
  process.exit(failing > 0 ? 1 : 0);
}

main();
